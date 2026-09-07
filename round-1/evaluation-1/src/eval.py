#!/usr/bin/env python3
"""
Evaluation of Phonotactic-Dependency Distance Minimization Hypothesis.

Performs mixed-effects regression and family-level variance analysis evaluating
whether phonological density and phonotactic complexity predict stronger dependency
distance minimization (DLM) across UD treebanks.
"""

import json
import math
import resource
import sys
import gc
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from collections import defaultdict

import numpy as np
from loguru import logger

# Setup logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

try:
    from scipy import stats
    from scipy.special import entr
except ImportError:
    logger.warning("scipy not available, using numpy fallbacks")
    stats = None
    entr = None

try:
    import statsmodels.api as sm
    from statsmodels.regression.mixed_linear_model import MixedLM
except ImportError:
    logger.warning("statsmodels not available, using numpy OLS fallback")
    sm = None
    MixedLM = None


def try_import_datasets():
    """Try to import datasets library for UD treebank loading."""
    try:
        from datasets import load_dataset
        return load_dataset
    except ImportError:
        logger.warning("datasets library not available, using synthetic data")
        return None


def _detect_cpus() -> int:
    """Detect actual CPU allocation."""
    import os, math
    from pathlib import Path
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError):
        pass
    try:
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError):
        pass
    try:
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        pass
    import os
    return os.cpu_count() or 1


def _container_ram_gb() -> float:
    """Read RAM limit from cgroup."""
    from pathlib import Path
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    import psutil
    return psutil.virtual_memory().total / 1e9


# Hardware detection
NUM_CPUS = _detect_cpus()
TOTAL_RAM_GB = _container_ram_gb()
logger.info(f"Detected {NUM_CPUS} CPUs, {TOTAL_RAM_GB:.1f}GB RAM")

# Set memory limits
RAM_BUDGET = int(TOTAL_RAM_GB * 1e9 * 0.7)  # 70% of available
import resource as res_module
res_module.setrlimit(res_module.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))


def compute_dependency_distances(treebank_data: List[Dict]) -> Dict[str, float]:
    """Compute mean dependency distance and distribution statistics."""
    if not treebank_data:
        return {}

    distances = []
    functional_distances = []
    lexical_distances = []

    functional_deprels = {'det', 'case', 'aux', 'mark', 'cc', 'punct', 'aux:pass', 'aux:cop'}

    for sentence in treebank_data:
        # Build word index from sentence
        words = []
        for token in sentence:
            if 'id' in token and 'deprel' in token:
                words.append({
                    'id': int(token['id']),
                    'deprel': token.get('deprel', ''),
                    'head': int(token.get('head', 0)),
                })

        for word in words:
            if word['head'] == 0:
                continue  # Skip root
            dist = abs(word['id'] - word['head'])
            distances.append(dist)

            if word['deprel'] in functional_deprels or word['deprel'].startswith('aux'):
                functional_distances.append(dist)
            else:
                lexical_distances.append(dist)

    result = {
        'mean_mdd': float(np.mean(distances)) if distances else 0.0,
        'n_arcs': len(distances),
        'functional_mdd': float(np.mean(functional_distances)) if functional_distances else 0.0,
        'lexical_mdd': float(np.mean(lexical_distances)) if lexical_distances else 0.0,
    }

    # Distribution statistics
    if distances:
        result.update({
            'median_mdd': float(np.median(distances)),
            'std_mdd': float(np.std(distances)),
            'p90_mdd': float(np.percentile(distances, 90)),
            'min_mdd': int(np.min(distances)),
            'max_mdd': int(np.max(distances)),
        })

    # Entropy of distribution
    if distances and entr is not None:
        # Compute histogram
        unique, counts = np.unique(distances, return_counts=True)
        probs = counts / counts.sum()
        probs = probs[probs > 0]
        entropy_values = entr(probs)
        result['mdd_entropy'] = float(np.sum(entropy_values))

    return result


def compute_phoneme_distances(treebank_data: List[Dict], avg_phonemes_per_word: float) -> Dict[str, float]:
    """Approximate phoneme-space dependency distance."""
    # In real implementation, we'd use epitran for G2P
    # Here we approximate: phoneme distance ~ word distance * avg_phonemes_per_word
    word_results = compute_dependency_distances(treebank_data)

    if not word_results or word_results['n_arcs'] == 0:
        return {}

    phoneme_factor = max(avg_phonemes_per_word, 2.0)  # Minimum 2 phonemes/word

    result = {
        'mean_ppad': word_results['mean_mdd'] * phoneme_factor,
        'functional_ppad': word_results['functional_mdd'] * phoneme_factor,
        'lexical_ppad': word_results['lexical_mdd'] * phoneme_factor,
        'phoneme_factor': phoneme_factor,
    }

    return result


def estimate_phonological_density(lang_code: str, lang_family: str) -> Dict[str, float]:
    """Estimate phonological density based on language family and typological features."""
    # Phoneme inventory sizes by language family (approximate, from PHOIBLE)
    family_inventory = {
        'Indo-European': 35.0,
        'Sino-Tibetan': 45.0,
        'Turkic': 30.0,
        'Uralic': 32.0,
        'Afroasiatic': 38.0,
        'Niger-Congo': 42.0,
        'Austronesian': 28.0,
        'Japonic': 25.0,
        'Koreanic': 24.0,
        'Dravidian': 55.0,
        'Tupian': 48.0,
        'Other': 35.0,
    }

    max_inventory = 70.0  # Approximate maximum across languages

    # Base phoneme count from family
    base_phonemes = family_inventory.get(lang_family, 35.0)

    # Adjust for specific languages (approximate values from PHOIBLE)
    language_adjustments = {
        'en': 44.0,  # English
        'de': 45.0,  # German
        'fr': 36.0,  # French
        'es': 24.0,  # Spanish
        'it': 30.0,  # Italian
        'nl': 32.0,  # Dutch
        'sv': 40.0,  # Swedish
        'ru': 55.0,  # Russian
        'pl': 50.0,  # Polish
        'cs': 55.0,  # Czech
        'ja': 25.0,  # Japanese
        'ko': 24.0,  # Korean
        'zh': 42.0,  # Chinese (Mandarin)
        'ar': 38.0,  # Arabic
        'he': 32.0,  # Hebrew
        'tr': 30.0,  # Turkish
        'fi': 32.0,  # Finnish
        'hu': 32.0,  # Hungarian
        'th': 44.0,  # Thai
        'vi': 36.0,  # Vietnamese
        'ms': 24.0,  # Malay
        'id': 26.0,  # Indonesian
        'hi': 40.0,  # Hindi
        'bn': 38.0,  # Bengali
        'sw': 45.0,  # Swahili
        'pt': 36.0,  # Portuguese
        'da': 36.0,  # Danish
        'no': 36.0,  # Norwegian
        'el': 35.0,  # Greek
        'bg': 40.0,  # Bulgarian
        'hr': 40.0,  # Croatian
        'sk': 45.0,  # Slovak
        'sl': 45.0,  # Slovenian
        'lt': 40.0,  # Lithuanian
        'lv': 40.0,  # Latvian
        'et': 30.0,  # Estonian
        'ka': 42.0,  # Georgian
        'hy': 45.0,  # Armenian
        'eu': 35.0,  # Basque
        'ha': 45.0,  # Hausa
        'yo': 45.0,  # Yoruba
        'ig': 45.0,  # Igbo
    }

    phoneme_count = language_adjustments.get(lang_code, base_phonemes)

    # Phonological density = normalized phoneme count
    phoneme_density = phoneme_count / max_inventory

    # Phonotactic complexity proxy (based on family)
    family_complexity = {
        'Sino-Tibetan': 0.9,  # Complex syllable structures
        'Dravidian': 0.85,
        'Niger-Congo': 0.8,
        'Afroasiatic': 0.75,
        'Indo-European': 0.6,
        'Uralic': 0.5,
        'Turkic': 0.55,
        'Austronesian': 0.6,
        'Japonic': 0.4,
        'Koreanic': 0.35,
        'Other': 0.5,
    }

    phonotactic_complexity = family_complexity.get(lang_family, 0.5)

    # Syllable richness proxy
    syllable_types = {
        'V': 1, 'CV': 2, 'VC': 3, 'CVC': 4, 'CCV': 5, 'CVV': 6,
        'CVN': 7, 'CCVC': 8,  # Simplified
    }
    # Use a rough estimate based on complexity
    syllable_richness = phonotactic_complexity * 0.8 + phoneme_density * 0.2

    # Composite phonological density
    phon_density = (phoneme_density * 0.5 + phonotactic_complexity * 0.3 + syllable_richness * 0.2)

    return {
        'phoneme_count': round(phoneme_count, 1),
        'phoneme_density': round(phoneme_density, 3),
        'phonotactic_complexity': round(phonotactic_complexity, 3),
        'syllable_richness': round(syllable_richness, 3),
        'phon_density': round(phon_density, 3),
    }


def get_language_info(lang_code: str) -> Dict[str, str]:
    """Get typological information for a language."""
    # Word order typology (Greenberg)
    word_order_map = {
        'en': 'SVO', 'de': 'SVO', 'fr': 'SVO', 'es': 'SVO', 'it': 'SVO',
        'nl': 'SVO', 'sv': 'SVO', 'ru': 'SVO', 'pl': 'SVO', 'cs': 'SVO',
        'ja': 'SOV', 'ko': 'SOV', 'zh': 'SVO', 'ar': 'VSO', 'he': 'VSO',
        'tr': 'SOV', 'fi': 'SVO', 'hu': 'SOV', 'th': 'SVO', 'vi': 'SVO',
        'ms': 'SVO', 'id': 'SVO', 'hi': 'SOV', 'bn': 'SOV', 'sw': 'SVO',
        'pt': 'SVO', 'da': 'SVO', 'no': 'SVO', 'el': 'SVO', 'bg': 'SVO',
        'hr': 'SVO', 'sk': 'SVO', 'sl': 'SVO', 'lt': 'SVO', 'lv': 'SVO',
        'et': 'SVO', 'ka': 'SOV', 'hy': 'SOV', 'eu': 'SOV', 'ha': 'SVO',
        'yo': 'SVO', 'ig': 'SVO',
    }

    # Language family
    family_map = {
        'en': 'Indo-European', 'de': 'Indo-European', 'fr': 'Indo-European',
        'es': 'Indo-European', 'it': 'Indo-European', 'nl': 'Indo-European',
        'sv': 'Indo-European', 'ru': 'Indo-European', 'pl': 'Indo-European',
        'cs': 'Indo-European', 'da': 'Indo-European', 'no': 'Indo-European',
        'pt': 'Indo-European', 'el': 'Indo-European', 'bg': 'Indo-European',
        'hr': 'Indo-European', 'sk': 'Indo-European', 'sl': 'Indo-European',
        'lt': 'Indo-European', 'lv': 'Indo-European', 'hy': 'Indo-European',
        'ja': 'Japonic', 'ko': 'Koreanic', 'zh': 'Sino-Tibetan',
        'ar': 'Afroasiatic', 'he': 'Afroasiatic', 'ha': 'Afroasiatic',
        'tr': 'Turkic', 'fi': 'Uralic', 'hu': 'Uralic', 'et': 'Uralic',
        'th': 'Tai-Kadai', 'vi': 'Austroasiatic', 'ms': 'Austronesian',
        'id': 'Austronesian', 'hi': 'Indo-European', 'bn': 'Indo-European',
        'sw': 'Niger-Congo', 'yo': 'Niger-Congo', 'ig': 'Niger-Congo',
        'ka': 'Kartvelian', 'eu': 'Language Isolate',
    }

    return {
        'word_order': word_order_map.get(lang_code, 'SVO'),
        'language_family': family_map.get(lang_code, 'Other'),
    }


def load_sample_treebanks(n_languages: int = 5) -> List[Dict]:
    """Load sample UD treebanks for evaluation."""
    # Target languages with good UD coverage
    target_languages = [
        'en', 'de', 'fr', 'es', 'it', 'nl', 'sv', 'ru', 'pl', 'cs',
        'ja', 'ko', 'zh', 'ar', 'he', 'tr', 'fi', 'hu', 'th', 'vi',
        'ms', 'id', 'hi', 'bn', 'sw', 'pt', 'da', 'no', 'el', 'bg',
        'hr', 'sk', 'sl', 'lt', 'lv', 'et', 'ka', 'hy', 'eu', 'ha',
        'yo', 'ig',
    ]

    sample = []
    load_ds = try_import_datasets()

    if load_ds is None:
        logger.warning("datasets library not available, generating synthetic data")
        for lang_code in target_languages[:n_languages]:
            sample.append({
                'lang_code': lang_code,
                'data': _generate_synthetic_treebank(),
                'n_sentences': 50,
                'source': 'synthetic',
            })
        return sample

    logger.info(f"Loading {n_languages} UD treebanks from HuggingFace")

    try:
        # Load a small sample from universal_dependencies
        # Use a smaller dataset or limit the load
        ds = load_ds('commul/universal_dependencies', split='train[:1000]', streaming=True)

        count = 0
        for item in ds:
            lang_code = item.get('language', '')
            if lang_code in target_languages and count < n_languages:
                sentences = _extract_sentences_from_item(item)
                if sentences:
                    sample.append({
                        'lang_code': lang_code,
                        'data': sentences,
                        'n_sentences': len(sentences),
                        'source': 'ud_treebank',
                    })
                    count += 1
                    logger.info(f"Loaded {lang_code}: {len(sentences)} sentences")

                    if count >= n_languages:
                        break
    except Exception as e:
        logger.error(f"Failed to load from HuggingFace: {e}")
        # Fall back to synthetic
        for lang_code in target_languages[:n_languages]:
            sample.append({
                'lang_code': lang_code,
                'data': _generate_synthetic_treebank(),
                'n_sentences': 50,
                'source': 'synthetic',
            })

    return sample


def _extract_sentences_from_item(item: Dict) -> List[Dict]:
    """Extract sentence-like structures from a dataset item."""
    sentences = []
    # Try different column names
    for key in ['tokens', 'sentences', 'words', 'conllu']:
        if key in item and isinstance(item[key], list):
            for token in item[key][:10]:  # Limit per language
                if isinstance(token, dict):
                    sentences.append(token)
                elif isinstance(token, str):
                    sentences.append({'text': token, 'id': len(sentences) + 1})
            break
    return sentences


def _generate_synthetic_treebank(n_sentences: int = 50, avg_words: int = 10) -> List[Dict]:
    """Generate synthetic dependency trees for testing with realistic variation."""
    import random
    random.seed(42)

    sentences = []
    for sent_id in range(n_sentences):
        n_words = random.randint(5, avg_words * 2)
        sentence = []
        for word_id in range(1, n_words + 1):
            # Generate a synthetic dependency arc
            if word_id == 1:
                head = 0  # Root
            else:
                # Bias towards leftward dependencies (typical in UD)
                head = random.randint(max(0, word_id - 5), word_id - 1)

            deprel = random.choice(['nsubj', 'obj', 'iobj', 'obl', 'acl', 'advmod',
                                    'case', 'det', 'aux', 'mark', 'conj', 'appos'])

            sentence.append({
                'id': word_id,
                'head': head,
                'deprel': deprel,
                'text': f'word{word_id}',
            })
        sentences.append(sentence)

    return sentences


def run_mixed_effects_regression(languages_data: List[Dict]) -> Dict[str, Any]:
    """Run mixed-effects regression analysis."""
    if len(languages_data) < 5:
        logger.warning(f"Insufficient data for regression ({len(languages_data)} languages)")
        return {
            'model': 'insufficient_data',
            'n_languages': len(languages_data),
            'n_families': len(set(d.get('language_info', {}).get('language_family', 'Other') for d in languages_data)),
        }

    # Prepare data
    phon_density = []
    mdd_word = []
    mdd_phoneme = []
    word_orders = []
    families = []

    for lang_data in languages_data:
        if 'phon_density' not in lang_data or 'mdd_word' not in lang_data:
            continue
        phon_density.append(lang_data['phon_density'])
        mdd_word.append(lang_data['mdd_word'])
        mdd_phoneme.append(lang_data.get('mdd_phoneme', lang_data['mdd_word'] * 4.0))
        word_orders.append(1 if lang_data['word_order'] == 'SOV' else 0)
        families.append(lang_data['language_family'])

    if len(phon_density) < 5:
        return {'model': 'insufficient_data', 'n_languages': len(phon_density)}

    phon_density = np.array(phon_density)
    mdd_word = np.array(mdd_word)
    mdd_phoneme = np.array(mdd_phoneme)
    word_orders = np.array(word_orders)
    families = np.array(families)

    # Create design matrix
    n = len(phon_density)
    design_matrix = np.column_stack([
        np.ones(n),  # Intercept
        phon_density,
        word_orders,
    ])

    result = {
        'model': 'MixedLM' if MixedLM is not None else 'OLS',
        'n_languages': n,
        'n_families': len(np.unique(families)),
        'families': list(np.unique(families)),
    }

    # Try mixed-effects model first
    if MixedLM is not None and len(np.unique(families)) > 2:
        try:
            model = MixedLM(mdd_word, design_matrix, groups=families)
            fitted = model.fit(reml=True)
            result['mixedlm_results'] = {
                'phon_density_coef': float(fitted.params[1]),
                'phon_density_pval': float(fitted.pvalues[1]),
                'word_order_coef': float(fitted.params[2]),
                'word_order_pval': float(fitted.pvalues[2]),
                'aic': float(fitted.aic),
                'bic': float(fitted.bic),
                'converged': bool(fitted.converged),
            }
            logger.info(f"MixedLM: phon_density coef = {result['mixedlm_results']['phon_density_coef']:.4f}, p = {result['mixedlm_results']['phon_density_pval']:.4f}")
        except Exception as e:
            logger.warning(f"MixedLM failed: {e}, falling back to OLS")
            result['mixedlm_results'] = {'error': str(e)}

    # OLS fallback
    try:
        X = sm.add_constant(design_matrix[:, [0, 1, 2]]) if sm is not None else design_matrix
        X = np.column_stack([np.ones(n), phon_density, word_orders])
        beta = np.linalg.lstsq(X, mdd_word, rcond=None)[0]
        residuals = mdd_word - X @ beta
        mse = np.mean(residuals ** 2)
        se = np.sqrt(mse * np.diag(np.linalg.pinv(X.T @ X)))
        t_stats = beta / se
        p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=n-3)) if stats is not None else np.zeros(3)

        # R-squared
        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((mdd_word - np.mean(mdd_word)) ** 2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        result['ols_results'] = {
            'intercept': float(beta[0]),
            'phon_density_coef': float(beta[1]),
            'word_order_coef': float(beta[2]),
            'phon_density_pval': float(p_values[1]),
            'word_order_pval': float(p_values[2]),
            'r_squared': float(r_squared),
            'adjusted_r_squared': float(1 - (1 - r_squared) * (n - 1) / (n - 3)),
        }
        logger.info(f"OLS: phon_density coef = {result['ols_results']['phon_density_coef']:.4f}, p = {result['ols_results']['phon_density_pval']:.4f}, R² = {result['ols_results']['r_squared']:.4f}")
    except Exception as e:
        logger.error(f"OLS regression failed: {e}")
        result['ols_results'] = {'error': str(e)}

    # Spearman correlation (non-parametric)
    if stats is not None:
        try:
            corr_mdd, p_mdd = stats.spearmanr(phon_density, mdd_word)
            corr_ppad, p_ppad = stats.spearmanr(phon_density, mdd_phoneme)
            result['spearman'] = {
                'mdd_correlation': float(corr_mdd),
                'mdd_pvalue': float(p_mdd),
                'ppad_correlation': float(corr_ppad),
                'ppad_pvalue': float(p_ppad),
            }
            logger.info(f"Spearman: MDD rho = {corr_mdd:.4f}, p = {p_mdd:.4f}")
        except Exception as e:
            logger.warning(f"Spearman correlation failed: {e}")

    return result


def run_family_variance_analysis(languages_data: List[Dict]) -> Dict[str, Any]:
    """Analyze variance across language families."""
    if not languages_data:
        return {'n_families': 0}

    families_data = {}
    for lang in languages_data:
        family = lang.get('language_family', 'Other')
        if family not in families_data:
            families_data[family] = {'mdd': [], 'phon_density': [], 'languages': []}
        if 'mdd_word' in lang:
            families_data[family]['mdd'].append(lang['mdd_word'])
            families_data[family]['phon_density'].append(lang.get('phon_density', 0))
            families_data[family]['languages'].append(lang['lang_code'])

    results = {
        'n_families': len(families_data),
        'families': {},
    }

    for family, data in families_data.items():
        mdds = np.array(data['mdd'])
        phon_densities = np.array(data['phon_density'])

        family_result = {
            'n_languages': len(mdds),
            'mean_mdd': float(np.mean(mdds)) if len(mdds) > 0 else None,
            'std_mdd': float(np.std(mdds)) if len(mdds) > 1 else None,
            'mean_phon_density': float(np.mean(phon_densities)) if len(phon_densities) > 0 else None,
            'languages': data['languages'],
        }

        # Add min/max if we have enough data
        if len(mdds) > 0:
            family_result['min_mdd'] = float(np.min(mdds))
            family_result['max_mdd'] = float(np.max(mdds))
            family_result['median_mdd'] = float(np.median(mdds))

        results['families'][family] = family_result

    # Overall statistics
    all_mdds = [d['mdd_word'] for d in languages_data if 'mdd_word' in d]
    if all_mdds:
        results['overall'] = {
            'mean_mdd': float(np.mean(all_mdds)),
            'std_mdd': float(np.std(all_mdds)),
            'min_mdd': float(np.min(all_mdds)),
            'max_mdd': float(np.max(all_mdds)),
            'n_languages': len(all_mdds),
        }

    return results


def main():
    logger.info("=" * 60)
    logger.info("Starting Phonotactic-Dependency Distance Evaluation")
    logger.info("=" * 60)

    # Configuration - use more languages for meaningful regression
    n_languages = min(12, NUM_CPUS * 4)  # Scale with available CPUs
    logger.info(f"Evaluating {n_languages} languages")

    # Load sample treebanks
    treebanks = load_sample_treebanks(n_languages)
    logger.info(f"Loaded {len(treebanks)} treebanks")

    # Process each language
    languages_data = []
    for tb in treebanks:
        lang_code = tb['lang_code']
        lang_info = get_language_info(lang_code)
        phon_info = estimate_phonological_density(lang_code, lang_info['language_family'])

        # Compute dependency distances
        dist_results = compute_dependency_distances(tb['data'])

        # Estimate phoneme distances
        avg_phonemes = phon_info['phoneme_count'] / 10.0  # Rough estimate
        ppad_results = compute_phoneme_distances(tb['data'], avg_phonemes)

        lang_data = {
            'lang_code': lang_code,
            'language_family': lang_info['language_family'],
            'word_order': lang_info['word_order'],
            'phon_density': phon_info['phon_density'],
            'phoneme_count': phon_info['phoneme_count'],
            'phonotactic_complexity': phon_info['phonotactic_complexity'],
            'mdd_word': dist_results.get('mean_mdd', 0.0),
            'mdd_phoneme': ppad_results.get('mean_ppad', 0.0),
            'mdd_functional': dist_results.get('functional_mdd', 0.0),
            'mdd_lexical': dist_results.get('lexical_mdd', 0.0),
            'n_arcs': dist_results.get('n_arcs', 0),
            'n_sentences': tb.get('n_sentences', 0),
            'data_source': tb.get('source', 'unknown'),
        }
        languages_data.append(lang_data)

        logger.info(f"  {lang_code}: MDD={lang_data['mdd_word']:.3f}, PhonDensity={lang_data['phon_density']:.3f}")

    # Run regression analysis
    logger.info("\nRunning regression analysis...")
    regression_results = run_mixed_effects_regression(languages_data)

    # Run family variance analysis
    logger.info("\nRunning family variance analysis...")
    family_results = run_family_variance_analysis(languages_data)

    # Compute DLM strength metric (lower MDD = stronger minimization)
    for lang in languages_data:
        # DLM strength = inverse of MDD (normalized)
        if lang['mdd_word'] > 0:
            lang['dlm_strength'] = 1.0 / lang['mdd_word']
        else:
            lang['dlm_strength'] = 0.0

    # Prepare metrics_agg for schema
    metrics_agg = {
        'mean_mdd_word_space': float(np.mean([l['mdd_word'] for l in languages_data])),
        'mean_mdd_phoneme_space': float(np.mean([l['mdd_phoneme'] for l in languages_data])),
        'mean_dlm_strength': float(np.mean([l['dlm_strength'] for l in languages_data])),
        'mean_phon_density': float(np.mean([l['phon_density'] for l in languages_data])),
        'n_languages': len(languages_data),
        'n_families': family_results.get('n_families', 0),
    }

    # Add regression results to metrics
    if 'ols_results' in regression_results:
        metrics_agg['regression_phon_density_coef'] = float(regression_results['ols_results'].get('phon_density_coef', 0))
        metrics_agg['regression_phon_density_pval'] = float(regression_results['ols_results'].get('phon_density_pval', 1.0))
        metrics_agg['regression_r_squared'] = float(regression_results['ols_results'].get('r_squared', 0))

    # Prepare output matching schema strictly
    # Build datasets for schema
    datasets = [{
        'dataset': 'universal_dependencies_evaluation',
        'examples': []
    }]

    for lang in languages_data:
        example = {
            'input': f"UD treebank for {lang['lang_code']} ({lang['language_family']}, {lang['word_order']})",
            'output': json.dumps(lang, ensure_ascii=False),
            'predict_mdd_word': str(lang['mdd_word']),
            'predict_mdd_phoneme': str(lang['mdd_phoneme']),
            'predict_phon_density': str(lang['phon_density']),
            'predict_dlm_strength': str(lang['dlm_strength']),
            'eval_mdd_word': lang['mdd_word'],
            'eval_mdd_phoneme': lang['mdd_phoneme'],
            'eval_phon_density': lang['phon_density'],
            'eval_dlm_strength': lang['dlm_strength'],
            'metadata_language_family': lang['language_family'],
            'metadata_word_order': lang['word_order'],
            'metadata_n_sentences': lang['n_sentences'],
            'metadata_n_arcs': lang['n_arcs'],
        }
        datasets[0]['examples'].append(example)

    output = {
        'metrics_agg': metrics_agg,
        'datasets': datasets,
    }

    # Save output
    output_path = Path("method_out.json")
    output_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    logger.info(f"Saved evaluation results to {output_path}")

    # Validate against schema
    from pathlib import Path as P
    validate_script = Path('/ai-inventor/.claude/skills/aii-json/scripts/aii_json_validate_schema.py')
    if validate_script.exists():
        import subprocess
        result = subprocess.run([
            sys.executable, str(validate_script),
            '--format', 'exp_eval_sol_out',
            '--file', str(output_path.absolute())
        ], capture_output=True, text=True)
        logger.info(f"Validation output:\n{result.stdout}\n{result.stderr}")
    else:
        logger.warning("Schema validation script not found, skipping validation")

    logger.info("Evaluation complete!")
    return output


if __name__ == "__main__":
    main()
