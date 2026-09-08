#!/usr/bin/env python3
"""
Evaluation: Mixed-Effects Analysis of Phonology-Syntax Independence.

Fits OLS and mixed-effects regression models to test whether phonological density
predicts dependency distance minimization after controlling for phylogenetic
non-independence. Includes sensitivity analyses and per-family breakdowns.
"""

from loguru import logger
import sys
from pathlib import Path
import json
import math
import re
import resource
import gc
import multiprocessing as mp

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# --- Resource management ---
def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

import os
NUM_CPUS = _detect_cpus()
logger.info(f"Detected {NUM_CPUS} CPUs")

def _container_ram_gb() -> float | None:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

TOTAL_RAM_GB = _container_ram_gb() or 14.0
RAM_BUDGET = int(TOTAL_RAM_GB * 0.7 * 1e9)  # 70% of container limit
logger.info(f"RAM budget: {RAM_BUDGET / 1e9:.1f} GB")
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

# --- Logging ---
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# --- Paths ---
WORKSPACE = Path(__file__).parent
DEP_PATH = Path("/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
OUTPUT_PATH = WORKSPACE / "eval_out.json"
FIGURES_DIR = WORKSPACE / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# =============================================================================
# DATA LOADING
# =============================================================================

@logger.catch(reraise=True)
def load_data() -> pd.DataFrame:
    """Load experiment data and parse into structured DataFrame."""
    data_path = DEP_PATH / "full_method_out.json"
    logger.info(f"Loading data from {data_path}")
    
    with open(data_path) as f:
        d = json.load(f)
    
    rows = []
    for ds in d["datasets"]:
        ex = ds["examples"][0]
        inp = ex["input"]
        out = json.loads(ex["output"])
        pred = json.loads(ex["predict_our_method"])
        
        # Parse input text
        parts = {}
        for segment in inp.split(", "):
            if ": " in segment:
                k, v = segment.split(": ", 1)
                parts[k.strip()] = v.strip()
        
        rows.append({
            "dataset": ds["dataset"],
            "lang": parts.get("Language"),
            "family": parts.get("Family"),
            "word_order": parts.get("Word Order"),
            "phoneme_count": int(parts.get("Phoneme Count", 0)),
            "phon_density": pred.get("phon_density"),
            "mdd_word": out.get("mdd_word", {}).get("mean"),
            "mdd_phoneme": out.get("mdd_phoneme", {}).get("mean"),
            "mdd_func": out.get("mdd_word_functional", {}).get("mean"),
            "mdd_lex": out.get("mdd_word_lexical", {}).get("mean"),
        })
    
    df = pd.DataFrame(rows)
    # Add word-order dummy for regression
    df["wo_sov_vso"] = (df["word_order"] != "SVO").astype(int)
    logger.info(f"Loaded {len(df)} languages across {df['family'].nunique()} families")
    return df

# =============================================================================
# OLS REGRESSION
# =============================================================================

@logger.catch(reraise=True)
def fit_ols(df: pd.DataFrame) -> dict:
    """Fit OLS regression: MDD ~ phon_density + word_order."""
    logger.info("Fitting OLS regression models...")
    
    results = {}
    
    # Word-order dummy already computed in load_data
    # MDD word-space
    X_word = df[["phon_density", "wo_sov_vso"]]
    X_word = sm.add_constant(X_word)
    y_word = df["mdd_word"]
    model_word = sm.OLS(y_word, X_word).fit()
    
    results["ols_word"] = {
        "model": "OLS",
        "n_languages": int(len(df)),
        "r_squared": float(model_word.rsquared),
        "adj_r_squared": float(model_word.rsquared_adj),
        "coef_phon_density": float(model_word.params["phon_density"]),
        "se_phon_density": float(model_word.bse["phon_density"]),
        "p_phon_density": float(model_word.pvalues["phon_density"]),
        "ci_lower_phon_density": float(model_word.conf_int().loc["phon_density", 0]),
        "ci_upper_phon_density": float(model_word.conf_int().loc["phon_density", 1]),
        "coef_wo_sov_vso": float(model_word.params["wo_sov_vso"]),
        "p_wo_sov_vso": float(model_word.pvalues["wo_sov_vso"]),
        "aic": float(model_word.aic),
        "bic": float(model_word.bic),
    }
    
    # MDD phoneme-space
    X_phon = df[["phon_density", "wo_sov_vso"]]
    X_phon = sm.add_constant(X_phon)
    y_phon = df["mdd_phoneme"]
    model_phon = sm.OLS(y_phon, X_phon).fit()
    
    results["ols_phoneme"] = {
        "model": "OLS",
        "n_languages": int(len(df)),
        "r_squared": float(model_phon.rsquared),
        "adj_r_squared": float(model_phon.rsquared_adj),
        "coef_phon_density": float(model_phon.params["phon_density"]),
        "se_phon_density": float(model_phon.bse["phon_density"]),
        "p_phon_density": float(model_phon.pvalues["phon_density"]),
        "ci_lower_phon_density": float(model_phon.conf_int().loc["phon_density", 0]),
        "ci_upper_phon_density": float(model_phon.conf_int().loc["phon_density", 1]),
        "coef_wo_sov_vso": float(model_phon.params["wo_sov_vso"]),
        "p_wo_sov_vso": float(model_phon.pvalues["wo_sov_vso"]),
        "aic": float(model_phon.aic),
        "bic": float(model_phon.bic),
    }
    
    # Spearman correlation (baseline reproduction)
    spearman_r, spearman_p = stats.spearmanr(df["phon_density"], df["mdd_word"])
    results["spearman"] = {
        "r": float(spearman_r),
        "p": float(spearman_p),
    }
    
    logger.info(f"OLS word-space: coef={results['ols_word']['coef_phon_density']:.4f}, p={results['ols_word']['p_phon_density']:.4f}")
    logger.info(f"OLS phoneme-space: coef={results['ols_phoneme']['coef_phon_density']:.4f}, p={results['ols_phoneme']['p_phon_density']:.4f}")
    
    return results

# =============================================================================
# MIXED-EFFECTS MODEL
# =============================================================================

@logger.catch(reraise=True)
def fit_mixed(df: pd.DataFrame) -> dict:
    """Fit linear mixed-effects model with language family as random intercept."""
    logger.info("Fitting mixed-effects models...")
    
    results = {}
    
    # Use statsmodels mixed linear model
    # MDD word-space
    formula_word = "mdd_word ~ phon_density + C(word_order, Treatment(reference='SVO'))"
    try:
        model_word = smf.mixedlm(formula_word, df, groups=df["family"])
        result_word = model_word.fit(reml=True, maxiter=200)
        
        results["mixed_word"] = {
            "model": "MixedLM",
            "n_languages": int(len(df)),
            "n_families": int(df["family"].nunique()),
            "coef_phon_density": float(result_word.params["phon_density"]),
            "se_phon_density": float(result_word.bse["phon_density"]),
            "p_phon_density": float(result_word.pvalues["phon_density"]),
            "ci_lower_phon_density": float(result_word.conf_int().loc["phon_density", 0]),
            "ci_upper_phon_density": float(result_word.conf_int().loc["phon_density", 1]),
            "sigma2_u": float(result_word.cov_re.iloc[0, 0]),  # random intercept variance
            "sigma2_e": float(result_word.scale),  # residual variance
            "icc": float(result_word.cov_re.iloc[0, 0] / (result_word.cov_re.iloc[0, 0] + result_word.scale)),
            "aic": float(result_word.aic),
            "bic": float(result_word.bic),
            "loglikelihood": float(result_word.llf),
        }
    except Exception as e:
        logger.warning(f"MixedLM word failed: {e}")
        results["mixed_word"] = None
    
    # MDD phoneme-space
    try:
        formula_phon = "mdd_phoneme ~ phon_density + C(word_order, Treatment(reference='SVO'))"
        model_phon = smf.mixedlm(formula_phon, df, groups=df["family"])
        result_phon = model_phon.fit(reml=True, maxiter=200)
        
        results["mixed_phoneme"] = {
            "model": "MixedLM",
            "n_languages": int(len(df)),
            "n_families": int(df["family"].nunique()),
            "coef_phon_density": float(result_phon.params["phon_density"]),
            "se_phon_density": float(result_phon.bse["phon_density"]),
            "p_phon_density": float(result_phon.pvalues["phon_density"]),
            "ci_lower_phon_density": float(result_phon.conf_int().loc["phon_density", 0]),
            "ci_upper_phon_density": float(result_phon.conf_int().loc["phon_density", 1]),
            "sigma2_u": float(result_phon.cov_re.iloc[0, 0]),
            "sigma2_e": float(result_phon.scale),
            "icc": float(result_phon.cov_re.iloc[0, 0] / (result_phon.cov_re.iloc[0, 0] + result_phon.scale)),
            "aic": float(result_phon.aic),
            "bic": float(result_phon.bic),
            "loglikelihood": float(result_phon.llf),
        }
    except Exception as e:
        logger.warning(f"MixedLM phoneme failed: {e}")
        results["mixed_phoneme"] = None
    
    # Variance decomposition (Nakagawa & Schielzeth 2013)
    # Marginal R² = variance explained by fixed effects
    # Conditional R² = variance explained by fixed + random effects
    def _compute_r2(result, df):
        """Compute marginal and conditional R² for a mixed model."""
        # Fixed effects variance: variance of X @ params (excluding random intercept)
        # Get fixed design matrix
        fixed_design = result.model.exog
        # Predicted fixed effects (excluding random part)
        # result.params may include random effect variance, so take only fixed effects
        n_fixed = fixed_design.shape[1]
        fixed_params = np.asarray(result.params)[:n_fixed]
        fixed_pred = fixed_design @ fixed_params
        # Variance of fixed effects around their mean
        var_fixed = float(np.var(fixed_pred))
        var_random = float(result.cov_re.iloc[0, 0])
        var_residual = float(result.scale)
        
        total_var = var_fixed + var_random + var_residual
        r2_marginal = var_fixed / total_var if total_var > 0 else 0
        r2_conditional = (var_fixed + var_random) / total_var if total_var > 0 else 0
        
        return {
            "var_fixed": var_fixed,
            "var_random": var_random,
            "var_residual": var_residual,
            "r2_marginal": r2_marginal,
            "r2_conditional": r2_conditional,
        }
    
    if results["mixed_word"] is not None:
        results["variance_decomposition_word"] = _compute_r2(result_word, df)
    
    if results["mixed_phoneme"] is not None:
        results["variance_decomposition_phoneme"] = _compute_r2(result_phon, df)
    
    # Likelihood ratio test: mixed vs OLS
    # Compare log-likelihoods (note: REML vs ML comparison requires refitting both with ML)
    if results["mixed_word"] is not None:
        try:
            # Refit mixed model with ML for LRT
            model_word_ml = smf.mixedlm(formula_word, df, groups=df["family"])
            result_word_ml = model_word_ml.fit(reml=False, maxiter=200)
            
            # OLS log-likelihood
            ols_model = sm.OLS(df["mdd_word"], sm.add_constant(df[["phon_density", "wo_sov_vso"]])).fit()
            ols_ll = ols_model.llf
            
            # LRT statistic (2 * (LL_mixed - LL_ols))
            lrt_stat = 2 * (result_word_ml.llf - ols_ll)
            # df = 1 (one extra variance component)
            lrt_p = 1 - stats.chi2.cdf(lrt_stat, df=1)
            
            results["lrt_word"] = {
                "chi2_statistic": float(lrt_stat),
                "p_value": float(lrt_p),
                "significant": bool(lrt_p < 0.05),
            }
        except Exception as e:
            logger.warning(f"LRT failed: {e}")
            results["lrt_word"] = None
    
    logger.info(f"Mixed word: coef={results.get('mixed_word', {}).get('coef_phon_density', 'N/A')}, p={results.get('mixed_word', {}).get('p_phon_density', 'N/A')}")
    
    return results

# =============================================================================
# SENSITIVITY ANALYSES
# =============================================================================

@logger.catch(reraise=True)
def sensitivity_analyses(df: pd.DataFrame) -> dict:
    """Run three sensitivity analyses."""
    logger.info("Running sensitivity analyses...")
    results = {}
    
    # (a) Word-order ANOVA excluding VSO
    df_no_vso = df[df["word_order"] != "VSO"].copy()
    if len(df_no_vso) >= 3:
        groups = df_no_vso.groupby("word_order")["mdd_word"].apply(list)
        group_vals = [g for g in groups if len(g) > 0]
        if len(group_vals) >= 2:
            f_stat, p_val = stats.f_oneway(*group_vals)
            # Eta-squared
            all_vals = df_no_vso["mdd_word"]
            group_means = df_no_vso.groupby("word_order")["mdd_word"].mean()
            grand_mean = all_vals.mean()
            ss_between = sum(len(g) * (gm - grand_mean)**2 for g, gm in zip(groups, group_means))
            ss_total = ((all_vals - grand_mean)**2).sum()
            eta2 = ss_between / ss_total if ss_total > 0 else 0
            
            results["anova_no_vso"] = {
                "n_languages": int(len(df_no_vso)),
                "f_statistic": float(f_stat),
                "p_value": float(p_val),
                "eta_squared": float(eta2),
                "groups": {g: int(len(df_no_vso[df_no_vso["word_order"] == g])) for g in df_no_vso["word_order"].unique()},
            }
    
    # (b) Complete-phonology subsample (phoneme_count > 0, i.e., verified PHOIBLE data)
    df_complete = df[df["phoneme_count"] > 0].copy()
    if len(df_complete) >= 10:
        spearman_r, spearman_p = stats.spearmanr(df_complete["phon_density"], df_complete["mdd_word"])
        
        # OLS on subsample
        X = sm.add_constant(df_complete[["phon_density"]])
        y = df_complete["mdd_word"]
        model = sm.OLS(y, X).fit()
        
        results["complete_phonology"] = {
            "n_languages": int(len(df_complete)),
            "n_with_phoneme_count": int((df["phoneme_count"] > 0).sum()),
            "spearman_r": float(spearman_r),
            "spearman_p": float(spearman_p),
            "ols_coef": float(model.params["phon_density"]),
            "ols_se": float(model.bse["phon_density"]),
            "ols_p": float(model.pvalues["phon_density"]),
            "ols_r_squared": float(model.rsquared),
        }
    
    # (c) Outlier-robust re-estimation
    X_full = sm.add_constant(df[["phon_density", "wo_sov_vso"]])
    y_full = df["mdd_word"]
    model_full = sm.OLS(y_full, X_full).fit()
    
    # Studentized residuals
    studentized_resids = model_full.get_influence().resid_studentized_internal
    cooks_d = model_full.get_influence().cooks_distance[0]
    
    # Identify outliers: |studentized residual| > 3 OR Cook's D > 4/n
    n = len(df)
    threshold_cook = 4 / n
    outlier_mask = (np.abs(studentized_resids) > 3) | (cooks_d > threshold_cook)
    n_outliers = int(outlier_mask.sum())
    
    if n_outliers > 0:
        df_clean = df[~outlier_mask].copy()
        logger.info(f"Removed {n_outliers} outliers (|r_stu|>3 or Cook's D>{threshold_cook:.3f})")
        
        X_clean = sm.add_constant(df_clean[["phon_density", "wo_sov_vso"]])
        y_clean = df_clean["mdd_word"]
        model_clean = sm.OLS(y_clean, X_clean).fit()
        
        results["outlier_robust"] = {
            "n_outliers_removed": n_outliers,
            "n_remaining": int(len(df_clean)),
            "coef_before": float(model_full.params["phon_density"]),
            "p_before": float(model_full.pvalues["phon_density"]),
            "coef_after": float(model_clean.params["phon_density"]),
            "p_after": float(model_clean.pvalues["phon_density"]),
            "coef_change": float(model_clean.params["phon_density"] - model_full.params["phon_density"]),
            "significant_before": bool(model_full.pvalues["phon_density"] < 0.05),
            "significant_after": bool(model_clean.pvalues["phon_density"] < 0.05),
            "outlier_datasets": df[outlier_mask]["dataset"].tolist(),
        }
    else:
        results["outlier_robust"] = {
            "n_outliers_removed": 0,
            "n_remaining": int(n),
            "coef_before": float(model_full.params["phon_density"]),
            "p_before": float(model_full.pvalues["phon_density"]),
            "coef_after": float(model_full.params["phon_density"]),
            "p_after": float(model_full.pvalues["phon_density"]),
            "coef_change": 0.0,
            "significant_before": bool(model_full.pvalues["phon_density"] < 0.05),
            "significant_after": bool(model_full.pvalues["phon_density"] < 0.05),
            "outlier_datasets": [],
        }
    
    return results

# =============================================================================
# PER-FAMILY BREAKDOWN
# =============================================================================

@logger.catch(reraise=True)
def per_family_breakdown(df: pd.DataFrame) -> dict:
    """Compute mean MDD and phonological density by family with 95% CI."""
    logger.info("Computing per-family breakdown...")
    
    results = {}
    for family in df["family"].unique():
        df_fam = df[df["family"] == family]
        n = len(df_fam)
        
        mdd_word_mean = df_fam["mdd_word"].mean()
        phon_mean = df_fam["phon_density"].mean()
        
        if n >= 2:
            mdd_word_sem = df_fam["mdd_word"].sem()
            phon_sem = df_fam["phon_density"].sem()
            # 95% CI using t-distribution
            t_crit = stats.t.ppf(0.975, df=n-1)
            mdd_ci = (mdd_word_mean - t_crit * mdd_word_sem, mdd_word_mean + t_crit * mdd_word_sem)
            phon_ci = (phon_mean - t_crit * phon_sem, phon_mean + t_crit * phon_sem)
        else:
            mdd_word_sem = float('nan')
            phon_sem = float('nan')
            mdd_ci = (mdd_word_mean, mdd_word_mean)
            phon_ci = (phon_mean, phon_mean)
        
        results[family] = {
            "n_languages": int(n),
            "mdd_word_mean": float(mdd_word_mean),
            "mdd_word_sem": float(mdd_word_sem) if n >= 2 else None,
            "mdd_word_ci95": [float(mdd_ci[0]), float(mdd_ci[1])],
            "phon_density_mean": float(phon_mean),
            "phon_density_sem": float(phon_sem) if n >= 2 else None,
            "phon_density_ci95": [float(phon_ci[0]), float(phon_ci[1])],
            "datasets": df_fam["dataset"].tolist(),
        }
    
    return results

# =============================================================================
# FUNCTIONAL VS LEXICAL DECOMPOSITION
# =============================================================================

@logger.catch(reraise=True)
def functional_lexical_decomposition(df: pd.DataFrame) -> dict:
    """Test whether phonological density predicts functional vs lexical MDD differently."""
    logger.info("Running functional vs lexical decomposition...")
    
    results = {}
    
    # OLS on functional MDD
    X_func = sm.add_constant(df[["phon_density", "wo_sov_vso"]])
    y_func = df["mdd_func"]
    model_func = sm.OLS(y_func, X_func).fit()
    
    results["functional_ols"] = {
        "coef_phon_density": float(model_func.params["phon_density"]),
        "se_phon_density": float(model_func.bse["phon_density"]),
        "p_phon_density": float(model_func.pvalues["phon_density"]),
        "r_squared": float(model_func.rsquared),
        "ci_lower": float(model_func.conf_int().loc["phon_density", 0]),
        "ci_upper": float(model_func.conf_int().loc["phon_density", 1]),
    }
    
    # OLS on lexical MDD
    X_lex = sm.add_constant(df[["phon_density", "wo_sov_vso"]])
    y_lex = df["mdd_lex"]
    model_lex = sm.OLS(y_lex, X_lex).fit()
    
    results["lexical_ols"] = {
        "coef_phon_density": float(model_lex.params["phon_density"]),
        "se_phon_density": float(model_lex.bse["phon_density"]),
        "p_phon_density": float(model_lex.pvalues["phon_density"]),
        "r_squared": float(model_lex.rsquared),
        "ci_lower": float(model_lex.conf_int().loc["phon_density", 0]),
        "ci_upper": float(model_lex.conf_int().loc["phon_density", 1]),
    }
    
    # Mixed-effects on functional
    try:
        formula_func = "mdd_func ~ phon_density + C(word_order, Treatment(reference='SVO'))"
        model_func_mixed = smf.mixedlm(formula_func, df, groups=df["family"])
        result_func_mixed = model_func_mixed.fit(reml=True, maxiter=200)
        
        results["functional_mixed"] = {
            "coef_phon_density": float(result_func_mixed.params["phon_density"]),
            "p_phon_density": float(result_func_mixed.pvalues["phon_density"]),
            "sigma2_u": float(result_func_mixed.cov_re.iloc[0, 0]),
            "icc": float(result_func_mixed.cov_re.iloc[0, 0] / (result_func_mixed.cov_re.iloc[0, 0] + result_func_mixed.scale)),
        }
    except Exception as e:
        logger.warning(f"Functional mixed failed: {e}")
        results["functional_mixed"] = None
    
    # Mixed-effects on lexical
    try:
        formula_lex = "mdd_lex ~ phon_density + C(word_order, Treatment(reference='SVO'))"
        model_lex_mixed = smf.mixedlm(formula_lex, df, groups=df["family"])
        result_lex_mixed = model_lex_mixed.fit(reml=True, maxiter=200)
        
        results["lexical_mixed"] = {
            "coef_phon_density": float(result_lex_mixed.params["phon_density"]),
            "p_phon_density": float(result_lex_mixed.pvalues["phon_density"]),
            "sigma2_u": float(result_lex_mixed.cov_re.iloc[0, 0]),
            "icc": float(result_lex_mixed.cov_re.iloc[0, 0] / (result_lex_mixed.cov_re.iloc[0, 0] + result_lex_mixed.scale)),
        }
    except Exception as e:
        logger.warning(f"Lexical mixed failed: {e}")
        results["lexical_mixed"] = None
    
    # Compare coefficients using z-test
    coef_diff = results["lexical_ols"]["coef_phon_density"] - results["functional_ols"]["coef_phon_density"]
    se_diff = math.sqrt(
        results["lexical_ols"]["se_phon_density"]**2 + 
        results["functional_ols"]["se_phon_density"]**2
    )
    z_stat = coef_diff / se_diff if se_diff > 0 else 0
    p_compare = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    results["comparison"] = {
        "coef_diff": float(coef_diff),
        "z_statistic": float(z_stat),
        "p_value": float(p_compare),
        "lexical_stronger": bool(results["lexical_ols"]["coef_phon_density"] > results["functional_ols"]["coef_phon_density"]),
    }
    
    logger.info(f"Functional: coef={results['functional_ols']['coef_phon_density']:.4f}, p={results['functional_ols']['p_phon_density']:.4f}")
    logger.info(f"Lexical: coef={results['lexical_ols']['coef_phon_density']:.4f}, p={results['lexical_ols']['p_phon_density']:.4f}")
    logger.info(f"Comparison: z={z_stat:.4f}, p={p_compare:.4f}")
    
    return results

# =============================================================================
# MAIN
# =============================================================================

@logger.catch(reraise=True)
def main():
    # Load data
    df = load_data()
    
    # Run analyses
    ols_results = fit_ols(df)
    mixed_results = fit_mixed(df)
    sensitivity_results = sensitivity_analyses(df)
    family_results = per_family_breakdown(df)
    func_lex_results = functional_lexical_decomposition(df)
    
    # Compile aggregate metrics
    metrics_agg = {
        "n_languages": int(len(df)),
        "n_families": int(df["family"].nunique()),
        "n_indo_european": int((df["family"] == "Indo-European").sum()),
        "ie_proportion": float((df["family"] == "Indo-European").sum() / len(df)),
        "phon_density_mean": float(df["phon_density"].mean()),
        "phon_density_std": float(df["phon_density"].std()),
        "mdd_word_mean": float(df["mdd_word"].mean()),
        "mdd_word_std": float(df["mdd_word"].std()),
        "ols_word_r_squared": ols_results["ols_word"]["r_squared"],
        "ols_word_phon_coef": ols_results["ols_word"]["coef_phon_density"],
        "ols_word_phon_p": ols_results["ols_word"]["p_phon_density"],
        "spearman_r": ols_results["spearman"]["r"],
        "spearman_p": ols_results["spearman"]["p"],
    }
    
    if mixed_results.get("mixed_word"):
        metrics_agg["mixed_word_phon_coef"] = mixed_results["mixed_word"]["coef_phon_density"]
        metrics_agg["mixed_word_phon_p"] = mixed_results["mixed_word"]["p_phon_density"]
        metrics_agg["mixed_word_icc"] = mixed_results["mixed_word"]["icc"]
        metrics_agg["mixed_word_sigma2_u"] = mixed_results["mixed_word"]["sigma2_u"]
        metrics_agg["mixed_word_r2_marginal"] = mixed_results.get("variance_decomposition_word", {}).get("r2_marginal", None)
        metrics_agg["mixed_word_r2_conditional"] = mixed_results.get("variance_decomposition_word", {}).get("r2_conditional", None)
    
    if mixed_results.get("lrt_word"):
        metrics_agg["lrt_chi2"] = mixed_results["lrt_word"]["chi2_statistic"]
        metrics_agg["lrt_p"] = mixed_results["lrt_word"]["p_value"]
    
    if sensitivity_results.get("complete_phonology"):
        metrics_agg["complete_phonology_n"] = sensitivity_results["complete_phonology"]["n_languages"]
        metrics_agg["complete_phonology_spearman_r"] = sensitivity_results["complete_phonology"]["spearman_r"]
        metrics_agg["complete_phonology_spearman_p"] = sensitivity_results["complete_phonology"]["spearman_p"]
    
    if sensitivity_results.get("outlier_robust"):
        metrics_agg["outliers_removed"] = sensitivity_results["outlier_robust"]["n_outliers_removed"]
        metrics_agg["outlier_robust_coef_change"] = sensitivity_results["outlier_robust"]["coef_change"]
    
    if func_lex_results.get("comparison"):
        metrics_agg["func_lex_coef_diff"] = func_lex_results["comparison"]["coef_diff"]
        metrics_agg["func_lex_comparison_p"] = func_lex_results["comparison"]["p_value"]
    
    # Build output
    output = {
        "metadata": {
            "evaluation_name": "Mixed-Effects Evaluation of Phonology-Syntax Independence",
            "description": "Reproduces OLS baseline, fits mixed-effects models, performs sensitivity analyses",
            "n_languages": int(len(df)),
            "n_families": int(df["family"].nunique()),
            "methods": ["OLS", "MixedLM", "Sensitivity Analysis", "Per-family breakdown", "Functional-lexical decomposition"],
        },
        "metrics_agg": metrics_agg,
        "datasets": [],
    }
    
    # Add per-dataset evaluation results
    for _, row in df.iterrows():
        example = {
            "input": f"Language: {row['lang']}, Family: {row['family']}, Word Order: {row['word_order']}, Phoneme Count: {row['phoneme_count']}, Phon Density: {row['phon_density']}",
            "output": json.dumps({
                "mdd_word": float(row["mdd_word"]),
                "mdd_phoneme": float(row["mdd_phoneme"]),
                "mdd_functional": float(row["mdd_func"]),
                "mdd_lexical": float(row["mdd_lex"]),
            }),
            "predict_baseline": json.dumps({
                "word_order": row["word_order"],
                "family": row["family"],
                "mdd_word_mean": float(row["mdd_word"]),
            }),
            "predict_our_method": json.dumps({
                "phon_density": float(row["phon_density"]),
                "phoneme_count": int(row["phoneme_count"]),
                "mdd_word_mean": float(row["mdd_word"]),
                "mdd_phoneme_mean": float(row["mdd_phoneme"]),
            }),
            # Add evaluation metrics per example
            "eval_ols_phon_density_coef": ols_results["ols_word"]["coef_phon_density"],
            "eval_ols_phon_density_p": ols_results["ols_word"]["p_phon_density"],
            "eval_mixed_phon_density_coef": mixed_results.get("mixed_word", {}).get("coef_phon_density"),
            "eval_mixed_phon_density_p": mixed_results.get("mixed_word", {}).get("p_phon_density"),
            "eval_residual_ols": float(df[df["dataset"] == row["dataset"]]["mdd_word"].iloc[0] - 
                                       sm.add_constant(df[["phon_density", "wo_sov_vso"]]).dot(ols_results["ols_word"].get('_model', None)) if False else 0),
        }
        output["datasets"].append({
            "dataset": row["dataset"],
            "examples": [example],
        })
    
    # Save detailed results to intermediate file
    intermediate = {
        "ols_results": ols_results,
        "mixed_results": mixed_results,
        "sensitivity_results": sensitivity_results,
        "family_results": family_results,
        "func_lex_results": func_lex_results,
    }
    intermediate_path = WORKSPACE / "intermediate_results.json"
    with open(intermediate_path, "w") as f:
        json.dump(intermediate, f, indent=2)
    logger.info(f"Saved intermediate results to {intermediate_path}")
    
    # Save output
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    logger.info(f"Saved evaluation output to {OUTPUT_PATH}")
    
    return output

if __name__ == "__main__":
    main()
