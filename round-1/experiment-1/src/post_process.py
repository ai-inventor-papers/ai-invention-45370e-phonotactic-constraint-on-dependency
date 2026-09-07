#!/usr/bin/env python3
"""Post-process intermediate results into final method_out.json."""

from loguru import logger
from pathlib import Path
import json
import sys
import time
import math
import resource
import numpy as np
import pandas as pd
from scipy import stats

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

WORKSPACE = Path(__file__).resolve().parent

def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except:
        pass
    return 2

def _container_ram_gb() -> float | None:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except:
            pass
    return None

NUM_CPUS = _detect_cpus()
TOTAL_RAM_GB = _container_ram_gb() or 14.0
AVAILABLE_RAM_GB = TOTAL_RAM_GB * 0.85
RAM_BUDGET = int(AVAILABLE_RAM_GB * 1e9)
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

def run_regression(results):
    from statsmodels.api import OLS, add_constant
    valid = [r for r in results if "mdd_word" in r and r.get("mdd_word", {}).get("mean", 0) > 0]
    if len(valid) < 5:
        return {"error": "too few valid results", "n": len(valid)}

    mdd_values = np.array([r["mdd_word"]["mean"] for r in valid])
    phon_density = np.array([r.get("phon_density", 0) for r in valid])
    families = [r.get("language_family", "Unknown") for r in valid]
    word_orders = [r.get("word_order", "SVO") for r in valid]

    wo_map = {"SVO": 0, "SOV": 1, "VSO": 2, "OV": 1, "VO": 0, "OSV": 0, "OVS": 0, "VOS": 0}
    wo_encoded = np.array([wo_map.get(wo, 0) for wo in word_orders])

    family_map = {f: i for i, f in enumerate(set(families))}
    n_families = len(family_map)

    X = np.column_stack([phon_density, wo_encoded])
    if n_families > 1:
        for i in range(n_families - 1):
            dummy = np.array([1 if f == list(family_map.keys())[i] else 0 for f in families])
            X = np.column_stack([X, dummy])

    X = add_constant(X)

    model = OLS(mdd_values, X)
    try:
        result = model.fit()
        reg_params = result.params
        reg_pvalues = result.pvalues
        reg_bse = result.bse
        if hasattr(reg_params, 'index'):
            param_dict = {str(k): float(v) for k, v in zip(reg_params.index, reg_params)}
            pval_dict = {str(k): float(v) for k, v in zip(reg_pvalues.index, reg_pvalues)}
        else:
            param_dict = {f"coeff_{i}": float(v) for i, v in enumerate(reg_params)}
            pval_dict = {f"pval_{i}": float(v) for i, v in enumerate(reg_pvalues)}
        regression_out = {
            "model": "OLS",
            "n_languages": len(valid),
            "n_families": n_families,
            "r_squared": float(result.rsquared),
            "r_squared_adj": float(result.rsquared_adj),
            "phon_density_coefficient": float(reg_params[1]),
            "phon_density_p_value": float(reg_pvalues[1]),
            "phon_density_std_err": float(reg_bse[1]),
            "all_coefficients": param_dict,
            "all_p_values": pval_dict,
            "residual_std": float(np.std(result.resid)),
        }
    except Exception as e:
        regression_out = {"error": str(e), "n_languages": len(valid)}

    if len(valid) >= 3:
        spearman_r, spearman_p = stats.spearmanr(phon_density, mdd_values)
        regression_out["spearman_r"] = float(spearman_r)
        regression_out["spearman_p"] = float(spearman_p)

    family_means = {}
    for r in valid:
        fam = r.get("language_family", "Unknown")
        if fam not in family_means:
            family_means[fam] = {"mdd": [], "phon_density": []}
        family_means[fam]["mdd"].append(r["mdd_word"]["mean"])
        family_means[fam]["phon_density"].append(r.get("phon_density", 0))

    family_summary = {}
    for fam, data in family_means.items():
        family_summary[fam] = {
            "n_languages": len(data["mdd"]),
            "mean_mdd": float(np.mean(data["mdd"])),
            "mean_phon_density": float(np.mean(data["phon_density"])),
        }
    regression_out["family_summary"] = family_summary
    return regression_out

def run_baseline_comparison(results):
    valid = [r for r in results if "mdd_word" in r and r.get("mdd_word", {}).get("mean", 0) > 0]
    from collections import defaultdict
    groups = defaultdict(list)
    for r in valid:
        wo = r.get("word_order", "Other")
        groups[wo].append(r["mdd_word"]["mean"])

    comparison = {}
    for wo, values in groups.items():
        comparison[wo] = {
            "n": len(values),
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
            "median": float(np.median(values)),
        }

    if len(groups) >= 2:
        try:
            f_stat, p_val = stats.f_oneway(*[np.array(v) for v in groups.values()])
            comparison["anova_f"] = float(f_stat)
            comparison["anova_p"] = float(p_val)
        except:
            pass
        try:
            h_stat, h_p = stats.kruskal(*[np.array(v) for v in groups.values()])
            comparison["kruskal_h"] = float(h_stat)
            comparison["kruskal_p"] = float(h_p)
        except:
            pass
    return comparison

def main():
    start_time = time.time()
    logger.info("Post-processing intermediate results")

    # Load intermediate results
    interp_path = WORKSPACE / "intermediate_results.json"
    if not interp_path.exists():
        logger.error("No intermediate_results.json found")
        return

    results = json.loads(interp_path.read_text())
    logger.info(f"Loaded {len(results)} language results")

    # Run analyses
    regression_results = run_regression(results)
    baseline_results = run_baseline_comparison(results)

    # Build output
    output = {
        "metadata": {
            "method_name": "Phonological Density and Dependency Distance Minimization",
            "description": "Computes word-space and phoneme-space dependency distances across UD treebanks, correlates with phonological density",
            "n_treebanks": len(results),
            "n_successful": len([r for r in results if "error" not in r]),
            "n_languages": len(set(r.get("lang_code") for r in results if "lang_code" in r)),
            "runtime_seconds": time.time() - start_time,
        },
        "datasets": [
            {
                "dataset": r.get("config", "unknown"),
                "examples": [
                    {
                        "input": f"Language: {r.get('lang_code','?')}, Family: {r.get('language_family','?')}, Word Order: {r.get('word_order','?')}, Phoneme Count: {r.get('phoneme_count',0)}, Phon Density: {r.get('phon_density',0):.3f}",
                        "output": json.dumps({
                            "mdd_word": r.get("mdd_word", {}),
                            "mdd_phoneme": r.get("mdd_phoneme"),
                            "mdd_word_functional": r.get("mdd_word_functional", {}),
                            "mdd_word_lexical": r.get("mdd_word_lexical", {}),
                            "n_sentences": r.get("n_sentences", 0),
                            "n_arcs": r.get("n_arcs", 0),
                        }),
                        "predict_baseline": json.dumps({
                            "word_order": r.get("word_order", "?"),
                            "family": r.get("language_family", "?"),
                            "mdd_word_mean": r.get("mdd_word", {}).get("mean", 0),
                        }),
                        "predict_our_method": json.dumps({
                            "phon_density": r.get("phon_density", 0),
                            "phoneme_count": r.get("phoneme_count", 0),
                            "mdd_word_mean": r.get("mdd_word", {}).get("mean", 0),
                            "mdd_phoneme_mean": r.get("mdd_phoneme", {}).get("mean", 0) if r.get("mdd_phoneme") else None,
                        }),
                    }
                ],
            }
            for r in results if "error" not in r
        ],
        "regression_results": regression_results,
        "baseline_comparison": baseline_results,
    }

    output_path = WORKSPACE / "method_out.json"
    output_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved results to {output_path}")

    logger.info("=" * 60)
    logger.info("RESULTS SUMMARY")
    logger.info(f"Languages processed: {len(results)}")
    logger.info(f"Regression R²: {regression_results.get('r_squared', 'N/A')}")
    logger.info(f"Phon density coefficient: {regression_results.get('phon_density_coefficient', 'N/A')}")
    logger.info(f"Phon density p-value: {regression_results.get('phon_density_p_value', 'N/A')}")
    logger.info(f"Spearman r: {regression_results.get('spearman_r', 'N/A')}")
    logger.info(f"Spearman p: {regression_results.get('spearman_p', 'N/A')}")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
