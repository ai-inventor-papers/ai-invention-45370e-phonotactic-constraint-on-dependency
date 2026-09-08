# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_nBwvdB3PKEF8` — Phonological Density Does Not Predict Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-09-08 01:10:20 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Phonological Density Does Not Predict DLM Strength
hypothesis: >-
  Languages with higher phonological density do not exhibit systematically stronger dependency distance minimization (DLM).
  Cross-linguistic tests across 55 languages from 10 families show no significant relationship between phoneme inventory size
  and mean dependency distance (Spearman r = 0.19, p = 0.17; R² = 0.05), with the weak correlation running opposite to the
  predicted direction. Phonological density and syntactic optimization appear to operate as largely independent constraints
  on linear order. Any residual phonological effect on DLM is likely mediated not by direct compression of syntactic dependencies
  but by alternative compensatory mechanisms: (1) phonological reduction of words adjacent to long-distance dependencies,
  (2) increased morphological marking to clarify grammatical roles without linear proximity, or (3) modulation at the phonological
  phrasing/prosodic interface rather than the syntactic level. The null finding itself constitutes a contribution: it establishes
  that the phonotactic constraint hypothesis — the idea that phonological crowding 'hoards' adjacency slots for syntactic
  optimization — does not hold at the cross-linguistic level. Future tests should (a) control for phylogenetic non-independence
  using mixed-effects models with language family as random intercept, (b) distinguish between phoneme-space span (phonemes
  in intervening words) and phoneme-weighted distance (distance weighted by connected word phoneme counts), and (c) test for
  modality-specific effects using spoken corpora where available.
motivation: >-
  Current dependency distance research suffers from two blindspots: (1) all work uses WORD-SPACE distance, missing phonological
  proximity constraints; (2) no one has tested whether phonological density modulates the strength of syntactic minimization.
  The findings on comparable information rates across speech and writing suggest speakers optimize around channel capacity.
  By shifting the unit of analysis from words to phonemes, this hypothesis joins the phonotactic/phonemic layer with the syntactic
  layer to reveal a cross-layer cost constraint that explains otherwise puzzling cross-linguistic patterns in DLM strength.
assumptions:
- >-
  UD treebanks are comparable across languages for extracting dependency distance patterns
- >-
  Phoneme inventory sizes and syllabification patterns are reliably available in cross-linguistic resources (e.g., Glottolog,
  Lexibank)
- >-
  The interaction between phonological density and syntactic optimization is not confounded by other typological factors (word
  order, distance-based rankings can be controlled)
- >-
  Spoken language treebanks (e.g., read speech, news corpora) sufficiently capture the phonological pressures that drive spoken
  communication efficiency
investigation_approach: >-
  1. Collect UD treebanks (commul/universal_dependencies on HuggingFace) and phonological density measures for 40+ languages
  (5+ from each of 8 typologically diverse families). 2. Measure dependency distance distributions (mean, variance, tail behavior)
  using the newly proposed phoneme-position adjacency metric: for each dependency hedge-d-dependent span, compute phoneme-position
  difference rather than word-position difference, weighted by constituent phoneme counts. 3. Control for word-order typology
  (OV/SVO/VSO) and overall distance-based rankings from prior work. 4. Test statistical relationship between phonological
  density metric and DLM strength using hierarchical regression: DLM as response, phonological density as primary predictor,
  language family as random effect, word-order as fixed covariate. 5. Cross-validation within language families to control
  for shared history. 6. Secondary analysis: compare how well this explains variance in DLM across modalities where possible.
success_criteria: >-
  The core hypothesis succeeds if: (1) Linguistic regression shows phonological density is a significant positive predictor
  of DLM strength (more dense = stronger minimization), above and beyond word-order typology; (2) The effect holds across
  5+ independent language families; (3) Family-level patterns emerge consistent with drift rather than sampling noise; (4)
  Sensitivity analyses (controlling for syllable count, stress patterns) confirm the phonological effect is not confounded.
related_works:
- >-
  Liu (2008, 2010) - First large-scale cross-linguistic MDD study, established DLM as universal
- >-
  Futrell et al. (2015, 2020) - UD-based validation of DLM, expanded language coverage to 37+ languages
- >-
  Gerdes (2026, 'The Grammar Does the Work') - Functional vs. lexical dependency split, demonstrates complex dependency-level
  patterns
- >-
  Ferrer-i-Cancho & Gómez-Rodríguez (2021) - Reduced dependency distance from sum to natural subsegment, highlighting distributed
  cost structure
- >-
  Kaja Dobrovoljc (2026, 'How Much Does Corpus Choice Change Dependency-Distance Estimates') - Showed ordinal rankings are
  unstable across treebanks, MDD is corpus-conditioned composite
- >-
  Coupé et al. (2019, Science Advances) - All languages encode information at ~39 bits/s, structural properties and processing
  adapt together to channel capacity
- >-
  Ferrer-i-Cancho (2021, 'Dependency distance minimization predicts compression') - Second-order prediction: DLM predicts
  word-length minimization
- >-
  Krielke (2024) - Diachronic shift toward intra-phrasal dependency relations in scientific English and German, hinting at
  phonological-density interaction
inspiration: >-
  Three cross-field insights combined: (1) MODALITY INTEGRITY (Coupé et al. 2019) - Languages optimize structural properties
  around communicative constraints; (2) MULTIMODAL EFFICIENCY (Rasenberg et al. 2022) - Teams minimize joint effort across
  different behavior types; (3) CROSS-LEVEL CONSTRAINT - Phonological density in chemistry/statistics hoards local configuration
  space, limiting elsewhere. The novel mechanism is borrowing the 'constraint competition' principle from materials physics:
  when one constraint type tightly occupies physical space (phonological adjacency), other systems must adapt (syntactic proximity)
  with different strategies. The phoneme-space dependency metric makes this competition observable.
terms:
- term: Dependency distance minimization (DLM)
  definition: >-
    The tendency of syntactically related words (heads and dependents) to be linearly close to each other in a sentence, reducing
    processing cost.
- term: Mean dependency distance (MDD)
  definition: >-
    The average absolute linear distance between heads and dependents, averaged over all dependency arcs in a corpus—currently
    the dominant aggregate DLM metric.
- term: Phonological density
  definition: >-
    A cross-linguistic measure combining phoneme inventory size, phonotactic complexity (legal consonant clusters), and the
    number of distinct syllable types; higher, or is the most widely reported dependency-distance summary.
- term: Phoneme-position adjacency matrix
  definition: >-
    An extension of token-space distance metrics where dependency distances are computed not in word positions but in underlying
    phoneme character positions, weighted by each word's constituent phoneme count.
- term: Functional vs. lexical dependencies
  definition: >-
    A dichotomy from Gerdes (2026): functional dependencies (determiners, case markers, auxiliaries) are universally short
    because grammar 'hard codes' their adjacency; lexical dependencies (subjects, objects, modifiers) are longer and constrained
    by typology.
summary: >-
  A phonotope density hypothesis predicting that languages with denser phonological inventories exhibit stronger dependency
  distance minimization, tested by measuring dependency distance in phoneme-space U wrongmost from HuggingFace and correlating
  DLM strength with phonological density across 40+ languages.
_relation_rationale: >-
  Same conceptual frame refined: evidence rejects original positive prediction in favor of null hypothesis
_confidence_delta: decreased
_key_changes:
- >-
  Reversed primary prediction: phonological density does NOT predict stronger DLM; weak positive correlation found instead
  (r=0.19, p=0.17)
- >-
  Null finding reframed as contribution: establishes phonological density and syntactic optimization as independent constraints
- >-
  Added phylogenetic control requirement: mixed-effects models with family random intercept needed to address 28/55 Indo-European
  sample skew
- >-
  Proposed alternative mechanisms: phonological reduction of adjacent words, increased morphological marking, prosodic-phrase-level
  mediation
- >-
  Specified PPAD metric correction: should sum phonemes of intervening words, not weight by connected-word average phoneme
  count
- >-
  Added sensitivity analysis requirement: test with complete phonological data subsample and distinguish real vs. approximated
  phoneme counts
- >-
  Added requirement to engage with Ferrer-i-Cancho & Gomez-Rodriguez (2021) who tested reverse direction (DLM -> phonological
  compression) using UD treebanks
- >-
  Narrowed scope to cross-linguistic level only; acknowledged that effects may operate at different timescales (diachronic
  phonology vs. synchronic syntax)
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_vqt7I2AbkCLO
type: dataset
title: Multilingual UD & Phonological Dataset for Dependency Distance Analysis
summary: >-
  This artifact collects and standardizes Universal Dependencies treebanks from commul/universal_dependencies on HuggingFace,
  paired with phonological and typological features. The dataset includes 39 languages spanning 10 major families (Indo-European,
  Uralic, Turkic, Afroasiatic, Niger-Congo, Sino-Tibetan, Austronesian, Japonic, Koreanic, Austroasiatic, Kartvelian) with
  both SVO and SOV word orders. Each language entry includes: (1) UD treebank data with dependency-parse information, (2)
  phonological features from PHOIBLE 2.0 (phoneme inventory sizes), (3) typological features from WALS (word order, family
  classification), and (4) computed dependency-distance statistics. The dataset enables cross-linguistic research on dependency
  length minimization, investigating whether spoken languages minimize more than written, how typology interacts with the
  pattern, and which families deviate.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_3GjyqsiFc7Gb
type: experiment
title: Phonological Density and Dependency Distance Analysis
summary: >-
  This artifact implements a computational linguistics experiment investigating the relationship between phonological density
  and dependency distance minimization across Universal Dependencies treebanks. The methodology computes word-space and phoneme-space
  dependency distances for 55 languages across 10 language families, then correlates these measures with phonological density
  indices derived from phoneme inventory sizes. Key components: (1) Data acquisition from commul/universal_dependencies on
  HuggingFace, processing CoNLL-U dependency trees; (2) Dependency distance computation using both word-space and phoneme-space
  metrics, with functional vs lexical dependency classification; (3) Phonological density calculation using PHOIBLE-derived
  phoneme inventory data; (4) Statistical analysis using OLS regression and Spearman correlation, controlling for word order;
  (5) Visualization generating scatter plots, correlation plots, and functional-lexical comparison figures. Results show a
  weak positive correlation between phonological density and MDD (Spearman r=0.19, R²=0.05), suggesting phonologically denser
  languages may exhibit somewhat weaker dependency distance minimization. The analysis includes baseline comparisons by word
  order type (SVO, SOV, VSO) and generates publication-quality PDF figures.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 3 ---
id: art_X5Bdc3dR_RYR
type: evaluation
title: Evaluation of Phonotactic-Dependency Distance Minimization Across UD Treebanks
summary: |-
  Mixed-effects regression and family-level variance analysis evaluating the phonotactic constraint hypothesis on dependency distance minimization across UD treebanks.

  Metrics computed:
  1. Mean Dependency Distance (MDD) in word-space and phoneme-space across all tested languages
  2. Phoneme-Position Adjoining Distance (PPAD) as the phoneme-space analog of MDD
  3. DLM strength metric (inverse of MDD) for each language
  4. Functional vs lexical dependency distance split
  5. Shannon entropy of dependency distance distributions

  Regression analysis:
  - OLS regression of MDD on phonological density with word-order typology as covariate
  - Mixed-effects model (when sufficient data available) with language family as random effect
  - Spearman rank correlation as non-parametric robustness check

  Phonological density components:
  - Normalized phoneme inventory size
  - Phonotactic complexity (max onset + coda cluster sizes)
  - Syllable type richness

  The hypothesis: Languages with higher phonological density (more phonemes, more complex phonotactics) should exhibit stronger dependency distance minimization, as speakers need to keep related words closer together to compensate for the difficulty of parsing longer phonological sequences.

  Note: This evaluation used synthetic treebanks due to unavailability of the HuggingFace datasets library in the execution environment. The framework supports loading real UD treebanks from commul/universal_dependencies when the library is available.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 4 ---
id: art_nrvjYtfmx0_F
type: experiment
in_dependencies:
- id: art_vqt7I2AbkCLO
  label: dataset
title: Phoneme-Space Dependency Distance Analysis Across 37 Languages
summary: >-
  Recomputed dependency distances in phoneme-space across 37 Universal Dependencies treebanks using language-family-specific
  phoneme estimation ratios. The corrected Phoneme-Interval Distance (PID) metric sums phoneme counts strictly between head
  and dependent in each dependency arc. Results show a weak negative correlation (r=-0.324, p=0.051) between phonological
  density and mean PID, suggesting languages with higher phonological density may exhibit marginally stronger dependency length
  minimization in phoneme-space. The rank correlation between word-based and phoneme-based distances is moderate (r=0.523,
  p=0.001), indicating phoneme-space provides a meaningfully different but correlated view of syntactic distance. Regression
  explains ~10.7% of variance. Five publication-quality figures generated. Output validated against exp_gen_sol_out schema
  with additional analysis fields.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_21q7z-GCrosW
type: evaluation
in_dependencies:
- id: art_3GjyqsiFc7Gb
  label: experiment
title: Mixed-Effects Evaluation of Phonology-Syntax Independence
summary: >-
  Comprehensive statistical evaluation of the relationship between phonological density and dependency distance minimization
  across 55 Universal Dependencies treebanks. The evaluation reproduces the baseline OLS results (phon_density coef=1.478,
  p=0.109, R²=0.054) and extends them with a linear mixed-effects model with language family as a random intercept. Key findings:
  (1) Mixed-effects model shows phon_density coef=0.843 (p=0.389), ICC=0.140, indicating 14% of variance is clustered at family
  level. (2) Variance decomposition shows marginal R²=0.038 (fixed effects) vs conditional R²=0.173 (fixed+random). (3) LRT
  (χ²=2.66, p=0.103) shows family effect does not significantly improve fit. (4) Sensitivity analyses: removing 4 outliers
  changed coef by only -0.055; ANOVA excluding VSO shows η²=0.0005 (word order negligible). (5) Functional-lexical decomposition
  shows no significant difference (z=-0.90, p=0.368). (6) Per-family breakdown reveals Afroasiatic languages have highest
  MDD (3.79) while Unknown family has lowest (2.88). The null finding persists after phylogenetic control: phonological density
  does not significantly predict dependency distance minimization.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 6 ---
id: art_N1HzZ0zfSC52
type: research
title: Literature deep-dive on DLM-phonology compression asymmetry
summary: >-
  This research produced a comprehensive literature deep-dive on the relationship between dependency distance minimization
  (DLM) and phonological compression. The central finding is that our null hypothesis (phonological density does NOT predict
  DLM strength) is theoretically consistent with FC&GR (2021) positive finding because the syntax-phonology optimization relationship
  is directionally asymmetric. FC&GR used a normalized optimality score Ω and found significance only with phoneme-based word
  length (τ = -0.37, p = 0.039), not syllable-based. Chen (2026) further shows MDD is corpus-conditioned with 40% of language
  rankings reversing across treebanks. The research integrates 15 sources and produces both research_out.json and research_report.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_nrvjYtfmx0_F
type: experiment
in_dependencies:
- id: art_vqt7I2AbkCLO
  label: dataset
title: Phoneme-Space Dependency Distance Analysis Across 37 Languages
summary: >-
  Recomputed dependency distances in phoneme-space across 37 Universal Dependencies treebanks using language-family-specific
  phoneme estimation ratios. The corrected Phoneme-Interval Distance (PID) metric sums phoneme counts strictly between head
  and dependent in each dependency arc. Results show a weak negative correlation (r=-0.324, p=0.051) between phonological
  density and mean PID, suggesting languages with higher phonological density may exhibit marginally stronger dependency length
  minimization in phoneme-space. The rank correlation between word-based and phoneme-based distances is moderate (r=0.523,
  p=0.001), indicating phoneme-space provides a meaningfully different but correlated view of syntactic distance. Regression
  explains ~10.7% of variance. Five publication-quality figures generated. Output validated against exp_gen_sol_out schema
  with additional analysis fields.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_21q7z-GCrosW
type: evaluation
in_dependencies:
- id: art_3GjyqsiFc7Gb
  label: experiment
title: Mixed-Effects Evaluation of Phonology-Syntax Independence
summary: >-
  Comprehensive statistical evaluation of the relationship between phonological density and dependency distance minimization
  across 55 Universal Dependencies treebanks. The evaluation reproduces the baseline OLS results (phon_density coef=1.478,
  p=0.109, R²=0.054) and extends them with a linear mixed-effects model with language family as a random intercept. Key findings:
  (1) Mixed-effects model shows phon_density coef=0.843 (p=0.389), ICC=0.140, indicating 14% of variance is clustered at family
  level. (2) Variance decomposition shows marginal R²=0.038 (fixed effects) vs conditional R²=0.173 (fixed+random). (3) LRT
  (χ²=2.66, p=0.103) shows family effect does not significantly improve fit. (4) Sensitivity analyses: removing 4 outliers
  changed coef by only -0.055; ANOVA excluding VSO shows η²=0.0005 (word order negligible). (5) Functional-lexical decomposition
  shows no significant difference (z=-0.90, p=0.368). (6) Per-family breakdown reveals Afroasiatic languages have highest
  MDD (3.79) while Unknown family has lowest (2.88). The null finding persists after phylogenetic control: phonological density
  does not significantly predict dependency distance minimization.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

id: art_N1HzZ0zfSC52
type: research
title: Literature deep-dive on DLM-phonology compression asymmetry
summary: >-
  This research produced a comprehensive literature deep-dive on the relationship between dependency distance minimization
  (DLM) and phonological compression. The central finding is that our null hypothesis (phonological density does NOT predict
  DLM strength) is theoretically consistent with FC&GR (2021) positive finding because the syntax-phonology optimization relationship
  is directionally asymmetric. FC&GR used a normalized optimality score Ω and found significance only with phoneme-based word
  length (τ = -0.37, p = 0.039), not syllable-based. Chen (2026) further shows MDD is corpus-conditioned with 40% of language
  rankings reversing across treebanks. The research integrates 15 sources and produces both research_out.json and research_report.md.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Phonological Density Does Not Predict Dependency Distance Minimization: A Cross-Linguistic Test Across 55 Languages

## Abstract

Dependency distance minimization (DLM) predicts that syntactically related words appear in close linear order. A natural extension asks whether phonologically dense languages, with larger phoneme inventories, exhibit stronger DLM to compensate for parsing difficulty. We test this across 55 languages from 10 families using Universal Dependencies treebanks, computing dependency distances in both word-space and a corrected phoneme-space metric that sums phonemes of intervening words. We find no significant relationship: phonological density does not predict DLM strength, and the effect disappears under phylogenetic control. A phoneme-space analysis across 37 languages yields a marginally significant effect in the predicted direction, but the effect is modest. The null finding is consistent with the directional asymmetry between syntax-driven phonological compression and the reverse direction we test: syntactic optimization drives phonological outcomes, not vice versa.

## 1. Introduction

Dependency distance minimization (DLM) is one of the most replicated empirical regularities in cross-linguistic syntax. Liu (2008) documented the effect across 15 languages from 11 families, showing that heads and dependents tend to appear near each other in linear order. Futrell et al. (2015) extended this to 37 languages using Universal Dependencies (UD) treebanks, confirming cross-family robustness. The effect holds across typologically diverse families and both spoken and written modalities (Temperley & Gildea, 2018).

Two blindspots persist in this literature. First, DLM has always been measured in word-space: distance equals the number of intervening words between head and dependent. This ignores phonological structure. A dependency spanning three monosyllabic words in Japanese occupies far less phonological space than the same word-count dependency in English. Second, no study has asked whether phonological density modulates DLM strength. Languages with larger phoneme inventories and more complex syllable structures face harder parsing problems. If speakers compensate by minimizing syntactic distance, phonologically dense languages should show stronger DLM.

We test this phonotactic constraint hypothesis using UD treebanks from 55 languages spanning 10 families. We compute dependency distances in both word-space and a corrected phoneme-space metric, the phoneme-interval distance (PID), which sums the phoneme counts of all words strictly between head and dependent in each dependency arc. We then correlate phonological density, derived from PHOIBLE inventory sizes, with mean dependency distance, controlling for word-order typology and phylogenetic relatedness.

The results do not support the hypothesis. Phonological density shows a weak positive correlation with MDD ($r = 0.19$, $p = 0.17$), running in the opposite direction from prediction. The effect is not statistically significant. Under phylogenetic control, the effect disappears entirely. Word order similarly fails to predict MDD. The phoneme-space metric produces larger values (mean 10.6 phonemes) than word-space (mean 3.1 words), confirming that phonological and syntactic distances operate on different scales.

These null findings are informative. They are consistent with the directional asymmetry documented by Ferrer-i-Cancho and Gómez-Rodríguez (2021), who found that DLM predicts phonological compression (syntax $\rightarrow$ phonology) but whose framework does not predict the reverse. Our results suggest that phonological density and syntactic optimization operate independently, or that any compensation mechanism is too weak to detect at the cross-linguistic level.

Our contributions are threefold. First, we introduce the phoneme-interval distance metric that correctly separates phonological from syntactic proximity. Second, we report the largest cross-linguistic test of the phonotactic constraint hypothesis to date, covering 55 languages with phylogenetic control. Third, we demonstrate the directional asymmetry between forward (syntax $\rightarrow$ phonology) and reverse (phonology $\rightarrow$ syntax) predictions in cross-level optimization.

[FIGURE:fig1]

## 2. Related Work

### 2.1 Dependency Distance Minimization

DLM was first documented by Liu (2008) for 15 languages, establishing mean dependency distance (MDD) as a universal tendency. Futrell et al. (2015) extended this to 37 languages using UD, confirming cross-family robustness. Futrell et al. (2020) showed that DLM accurately predicts word-order preferences, establishing it as an explanatory principle rather than a mere descriptive pattern. Ferrer-i-Cancho and Gómez-Rodríguez (2021) introduced a normalized optimality score $\Omega$ that has superior mathematical properties to raw sum of dependency distances, including dual normalization and boundedness.

The functional versus lexical dependency split forms a well-established dichotomy. Gerdes (2026) showed that functional dependencies (determiners, case markers, auxiliaries) are universally short (MDD = 1.71, $\sigma$ = 0.33) because grammar hard-codes their adjacency, while lexical dependencies (subjects, objects, modifiers) are longer (MDD = 2.87, $\sigma$ = 0.63) and more sensitive to typological variation. Our results confirm this split.

### 2.2 The DLM-Phonology Interface

Ferrer-i-Cancho and Gómez-Rodríguez (2021) tested whether DLM predicts phonological compression, finding significance with phoneme-based word length (Kendall $\tau = -0.37$, $p = 0.039$) but not syllable-based measures. Their framework posits a causal chain: distance minimization drives dependency distance minimization, which drives repertoire unit weight minimization (compression). The reverse direction, from phonological properties to syntactic optimization, is not part of this architecture. Our work tests that reverse direction explicitly.

Coupé et al. (2019) demonstrated that languages encode information at approximately 39 bits per second, with syllable rate and information density compensating for each other. This modulation integrity hypothesis suggests that phonological and syntactic constraints jointly optimize around channel capacity. Our work tests a specific instantiation: whether phonological density modulates syntactic optimization.

### 2.3 Corpus Dependence of DLM Estimates

Recent work has questioned the stability of MDD as a language-level parameter. Chen (2026) showed that substituting one treebank for another reverses nearly 40% of pairwise language orderings, and treebank choice accounts for roughly 29% of between-group variance. The qualitative DLM universal survives corpus substitution, but the ordinal cross-linguistic ranking does not. This finding is relevant to our work: if MDD is a corpus-conditioned composite, predicting it from stable phonological properties is inherently difficult.

Krielke (2024) demonstrated DLM sensitivity to genre and register, showing that scientific English and German exhibit decreasing DLM over time. This further supports the view that MDD reflects a composite of grammatical, register, and annotation factors.

### 2.4 Cross-Level Optimization

The information-theoretic perspective provides a framework for understanding cross-level interactions. Gibson et al. (2019) argued that efficiency shapes human language through multiple constraints operating at different levels. Clark et al. (2023) showed a cross-linguistic pressure for uniform information density in word order, suggesting that syntactic and informational constraints interact. Our work tests whether phonological-level constraints predict syntactic-level optimization.

## 3. Method

### 3.1 Data

We extracted UD treebanks from the `commul/universal_dependencies` repository on HuggingFace [ARTIFACT:art_3GjyqsiFc7Gb]. We selected one configuration per language, preferring treebanks with the largest training splits. This yielded 55 languages across 10 families: Indo-European (20), Uralic (4), Turkic (3), Afroasiatic (4), Sino-Tibetan (4), Austronesian (5), Japonic (1), Koreanic (1), Tai-Kadai (2), and Austroasiatic (2), plus isolates and unclassified entries [ARTIFACT:art_21q7z-GCrosW].

Phonological features came from PHOIBLE 2.0. We used phoneme inventory size as the primary density metric. Phonological density was normalized to $[0, 1]$ by dividing by the maximum observed inventory (64 phonemes). Mean phonological density across the sample was 0.50 ($\sigma$ = 0.09).

Word-order typology came from WALS. We classified languages as SVO ($n = 41$), SOV ($n = 11$), or VSO ($n = 3$). All treebanks were written corpora.

### 3.2 Dependency Distance Metrics

Word-space MDD follows standard practice. For each dependency arc $(h, d)$, distance equals $|pos(h) - pos(d)|$, the absolute difference in token positions. Mean dependency distance equals the arithmetic mean across all arcs in a treebank.

Phoneme-interval distance (PID) extends this to phonological units. For each word $w$, we estimated constituent phonemes using language-family-specific phoneme estimation ratios derived from PHOIBLE data [ARTIFACT:art_nrvjYtfmx0_F]. PID for arc $(h, d)$ equals:

$$PID(h, d) = \sum_{w \in \text{intervening}(h, d)} \phi_w$$

where $\phi_w$ is the phoneme count of word $w$, and $\text{intervening}(h, d)$ is the set of words strictly between positions $pos(h)$ and $pos(d)$. This sums the phonological material in the span between head and dependent, providing a measure of phonological distance that is distinct from word-count distance.

For non-Latin scripts (CJK, Arabic, Thai), where epitran was unavailable, we used character counts as a lower-bound approximation of phoneme counts. This limitation is discussed in Section 5.3.

Both metrics were computed per treebank, then aggregated by language. Functional dependencies used the standard UD tagset: `det`, `case`, `aux`, `mark`, `cc`, `punct`, and their subtypes. Lexical dependencies included all remaining relations.

### 3.3 Statistical Analysis

We tested three hypotheses: (H1) phonological density predicts MDD, (H2) word order predicts MDD, (H3) phonological density predicts mean PID. For H1, we fitted both OLS regression and a linear mixed-effects model with language family as a random intercept. For H2, we fitted one-way ANOVA with word order as factor, reporting results both with and without the VSO group. For H3, we fitted OLS regression on the 37-language PID subsample. We reported Spearman rank correlations as non-parametric robustness checks. All analyses used $\alpha = 0.05$.

We computed family-level variance to assess whether patterns hold within independent lineages. The mixed-effects model addresses the phylogenetic non-independence concern raised by the Indo-European overrepresentation (20/55 languages).

### 3.4 Implementation

Code is available at [ARTIFACT:art_3GjyqsiFc7Gb] and [ARTIFACT:art_nrvjYtfmx0_F]. Processing used Python 3.12 with the `datasets` library for HuggingFace access, `numpy` for numerical operations, `scipy` for statistical tests, and `statsmodels` for mixed-effects modeling. Runtime was approximately 600 seconds across all 55 languages.

## 4. Results

### 4.1 Word-Space Dependency Distances

Mean MDD ranged from 1.96 (Kurdish Sorani) to 4.15 (Arabic) across 55 languages. The overall mean was 3.10 with standard deviation 0.63.

Word order did not predict MDD significantly. SVO languages averaged 3.07 ($n = 41$), SOV languages averaged 3.04 ($n = 11$), and VSO languages averaged 3.67 ($n = 3$). ANOVA yielded $F = 1.36$, $p = 0.27$ [FIGURE:fig2]. Kruskal-Wallis also failed to reach significance ($H = 2.23$, $p = 0.33$). Excluding the VSO group, the ANOVA between SVO and SOV alone was non-significant ($F = 0.06$, $p = 0.81$), with an effect size of $\eta^2 = 0.0005$. Word order explains essentially none of the variance in MDD.

### 4.2 Phonological Density and DLM

The phonotactic constraint hypothesis predicted a negative correlation: denser phonological systems should exhibit stronger DLM (lower MDD). The observed correlation ran in the opposite direction. Spearman $r = 0.19$, $p = 0.17$ [FIGURE:fig3]. OLS regression yielded $R^2 = 0.05$, phonological density coefficient = 1.48, intercept = 2.34. The positive coefficient indicates that denser languages tend toward slightly longer dependencies, though the effect is small and non-significant.

The mixed-effects model with language family as random intercept showed the same pattern with reduced effect size: $\beta = 0.84$, $p = 0.39$. The intraclass correlation coefficient was 0.14, indicating that 14% of variance in MDD is clustered at the family level. The marginal $R^2$ (fixed effects alone) was 0.038, while the conditional $R^2$ (fixed plus random) was 0.173. A likelihood ratio test comparing the mixed model to the OLS baseline yielded $\chi^2 = 2.66$, $p = 0.10$, indicating that the family effect does not significantly improve model fit.

Sensitivity analysis confirmed robustness. Removing the four most extreme outliers changed the phonological density coefficient by only -0.055. The correlation held at $r = 0.19$ in the complete sample.

### 4.3 Phoneme-Interval Distances

PID averaged 10.62 phonemes across the 37-language subsample, with standard deviation 4.23. PID was consistently larger than word-space MDD, as expected given that words contain multiple phonemes. The ratio PID/MDD averaged 3.5, corresponding to average word length of 3.5 phonemes.

The phoneme-space analysis yielded a marginally significant negative correlation between phonological density and mean PID: Spearman $r = -0.32$, $p = 0.051$ [FIGURE:fig4]. OLS regression explained 10.7% of variance ($R^2 = 0.11$), with slope = -0.84 and intercept = 16.29. This result runs in the predicted direction: phonologically denser languages show shorter phoneme-interval distances. However, the effect is modest and barely reaches significance.

PID correlated with word-space MDD ($r = 0.52$, $p < 0.001$), confirming that phoneme-space and word-space distances capture related but distinct aspects of dependency structure. The moderate correlation indicates that phonological composition modulates the word-space pattern.

### 4.4 Functional versus Lexical Dependencies

Across all languages, functional dependencies averaged 2.7 words while lexical dependencies averaged 3.4 words [FIGURE:fig5]. The functional-lexical split was consistent across word-order types and language families, replicating Gerdes (2026). The difference was not statistically significant in our sample ($z = -0.90$, $p = 0.37$), likely due to between-language variance overshadowing the within-language effect.

### 4.5 Family-Level Patterns

Per-family breakdown revealed that Afroasiatic languages had the highest mean MDD (3.79), while languages in the Unknown family had the lowest (2.88). Indo-European languages ranged from 2.34 (Latin) to 4.15 (Arabic), with no clear density-distance relationship within the family. Uralic languages averaged 2.89, below the overall mean. Turkic languages averaged 3.12. These patterns are descriptive and should be interpreted cautiously given small within-family sample sizes.

## 5. Discussion

### 5.1 The Null Finding and Its Theoretical Implications

The primary finding is negative: phonological density does not predict dependency distance minimization in word-space. This contradicts the phonotactic constraint hypothesis, which predicted that dense phonological systems would compress syntactic dependencies to compensate for parsing difficulty.

The null finding is theoretically informative rather than merely inconclusive. It is consistent with the directional asymmetry documented by Ferrer-i-Cancho and Gómez-Rodríguez (2021). They showed that DLM predicts phonological compression: languages with stronger DLM tend to have shorter words. Their framework posits a causal chain where syntactic optimization drives phonological outcomes. The reverse direction, from phonological properties to syntactic optimization, is not predicted by their architecture. Our results confirm this asymmetry: the forward direction holds (FC&GR, 2021), while the reverse does not.

Several additional factors may explain the null result. First, Chen (2026) showed that MDD is a corpus-conditioned composite, with 40% of language rankings reversing across treebanks. Predicting a variable that is sensitive to corpus composition from a stable phonological property is inherently difficult. Second, phonological density and syntactic optimization may operate at different timescales. DLM reflects contemporary sentence structure shaped by processing constraints. Phonological density reflects historical sound changes operating over centuries. The mismatch in temporal scale could obscure synchronic correlations.

The marginally significant negative correlation in phoneme-space ($r = -0.32$, $p = 0.051$) suggests a weak effect in the predicted direction. This could reflect a genuine but small compensation mechanism, or it could be a Type I error given the multiple comparisons in our analysis. We treat this result as suggestive rather than conclusive.

### 5.2 Methodological Contributions

Despite the null finding, we introduce two methodological innovations. First, the phoneme-interval distance metric provides a measure that correctly sums phonological material between head and dependent, rather than weighting by the phoneme counts of the connected words. This distinction matters: a dependency between two 10-phoneme words at distance 3 has PID equal to the sum of phonemes in the intervening words, not $3 \times 10$. Second, our standardized pipeline for combining UD treebanks with PHOIBLE data is publicly available [ARTIFACT:art_3GjyqsiFc7Gb] and enables replication and extension.

### 5.3 Limitations

Several limitations warrant acknowledgment. First, phonological density was measured as phoneme inventory size alone. We lacked reliable data on phonotactic complexity and syllable type richness for all 55 languages. These features may capture aspects of phonological density that inventory size misses.

Second, for non-Latin scripts, we used character counts as a lower-bound approximation of phoneme counts when epitran was unavailable. For CJK languages, this means PID is effectively a character-space metric rather than a phoneme-space metric. This creates inconsistency: some languages have real phoneme counts, others have character approximations. Future work should use consistent phoneme estimation across all scripts.

Third, all treebanks were written corpora. Spoken corpora might reveal different patterns if phonological pressure operates primarily in speech. Our dataset includes no spoken UD treebanks, though this limitation affects all current DLM research.

Fourth, the VSO group contained only 3 languages, limiting statistical power for that word-order type. The non-significant ANOVA may reflect insufficient sample size rather than true absence of effect.

Fifth, the Indo-European family accounts for 20 of 55 languages (36%). While the mixed-effects model partially addresses phylogenetic non-independence, the family effect did not significantly improve model fit, suggesting that the sample skew does not materially affect our conclusions.

## 6. Conclusion

We tested whether phonological density predicts dependency distance minimization across 55 languages. The hypothesis predicted stronger DLM in phonologically dense systems. Results showed a weak positive correlation ($r = 0.19$, $p = 0.17$) that failed to reach significance. Phonological density explained only 5% of variance in MDD. Under phylogenetic control, the effect disappeared entirely. Word order also failed to predict MDD.

The null finding is consistent with the directional asymmetry between syntax-driven phonological compression and the reverse direction. It establishes that phonological density is not a strong predictor of syntactic optimization at the cross-linguistic level.

We recommend three directions for future work. First, extend the analysis to spoken corpora to test whether phonological pressure is modality-specific. Second, incorporate additional phonological features when data becomes available. Third, investigate alternative compensation mechanisms, such as phonological reduction or increased morphological marking, that might mediate the phonology-syntax interface.

The phoneme-interval distance metric we introduce can support these extensions. By correctly summing phonological material between head and dependent, PID offers a tool for studying the interface between phonology and syntax in ways that word-space metrics cannot.

## References

[1] Liu, H. (2008). Complexity of two types of dependency distance. *Proceedings of the Sixth International Workshop on Treebanks and Linguistic Theories*, 263-274.

[2] Futrell, R., Mahowald, K., & Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37 languages. *Proceedings of the National Academy of Sciences*, 112, 10336-10341.

[3] Hahn, M., Jurafsky, D., & Futrell, R. (2020). Universals of word order reflect optimization of grammars for efficient communication. *Proceedings of the National Academy of Sciences*, 117, 2347-2353.

[4] Ferrer-i-Cancho, R., & Gómez-Rodríguez, C. (2021). Dependency distance minimization predicts compression. *Proceedings of the Second Workshop on Quantitative Syntax (QUASY, SyntaxFest 2022)*, 45-57.

[5] Ferrer-i-Cancho, R., Gómez-Rodríguez, C., Esteban, J., & Alemany-Puig, L. (2021). The optimality of syntactic dependency distances. *Physical Review E*, 105, 014308.

[6] Temperley, D., & Gildea, D. (2018). Minimizing syntactic dependency lengths: Typological/cognitive universal? *Annual Review of Linguistics*, 4, 251-270.

[7] Gerdes, K. (2026). The grammar does the work: Functional vs. lexical dependency length minimization across Universal Dependencies. *Proceedings of the Ninth Workshop on Universal Dependencies (UDW 2026)*.

[8] Coupé, C., Oh, Y., Dediu, D., & Pellegrino, F. (2019). Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche. *Science Advances*, 5, eaaw2594.

[9] Gibson, E., Futrell, R., Piantadosi, S., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). How efficiency shapes human language. *Trends in Cognitive Sciences*, 23(5), 389-407.

[10] Clark, T. H., Meister, C., Pimentel, T., Hahn, M., Cotterell, R., Futrell, R., & Mit, R. L. (2023). A cross-linguistic pressure for uniform information density in word order. *Transactions of the Association for Computational Linguistics*, 11, 1048-1065.

[11] Chen, S. (2026). How much does corpus choice change dependency-distance estimates? *arXiv preprint*, arXiv:2609.04223.

[12] Krielke, M.-P. (2024). Cross-linguistic dependency length minimization in scientific language. *Comparing Crosslinguistic Complexity*.

[13] Moran, S., McCloy, D. R., & Wright, R. (2016). PHOIBLE 2.0. *Proceedings of Interspeech*, 1678-1682.

[14] Dryer, M. S., & Haspelmath, M. (2013). World Atlas of Language Structures Online. *Max Planck Digital Library*.

[15] Zeman, D., et al. (2020). Universal Dependencies v2: An ever-growing multilingual treebank family. *Proceedings of the Twelfth Language Resources and Evaluation Conference*, 1677-1685.

## Data and Code Availability

All code and data are available at [ARTIFACT:art_3GjyqsiFc7Gb], [ARTIFACT:art_nrvjYtfmx0_F], [ARTIFACT:art_21q7z-GCrosW], and [ARTIFACT:art_vqt7I2AbkCLO].
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) The word-space analysis (55 languages) and phoneme-space analysis (37 languages) use DIFFERENT treebanks for the same languages. For example, English uses en_gumreddit in word-space but en_ewt in phoneme-space; French uses fr_parisstories vs fr_gsd; Japanese uses ja_bccwjluw vs ja_gsd. This affects 13 of 22 languages that appear in both analyses. The paper itself cites Chen (2026), who showed that treebank choice reverses 40% of pairwise language orderings and accounts for 29% of between-group variance. Using different treebanks means the two analyses are not measuring the same language properties, and any comparison between them is confounded. The evaluation artifact loads from the word-space experiment (iter_1) while the phoneme-space results come from a separate experiment (iter_2) with different treebank selections.
  Action: Re-run both analyses on the SAME set of treebanks. The simplest fix: restrict both analyses to the 22-language intersection, using the SAME treebank for each language in both analyses. Alternatively, re-run the phoneme-space analysis on all 55 treebanks from the word-space analysis. Report which treebank was used for each language in a supplementary table. This is essential for the paper's internal validity.
- [MAJOR] (methodology) Phoneme counts are estimated using hardcoded character×ratio heuristics (e.g., English=1.2, Russian=0.8, Japanese=0.7) rather than actual phoneme transcription. The paper describes these as 'language-family-specific phoneme estimation ratios derived from PHOIBLE data,' but the code shows they are hardcoded constants with no derivation from PHOIBLE. For CJK languages, the code uses character counts directly (each Chinese character = 1 phoneme, each Korean syllable = 1/3 phoneme). This approach introduces systematic measurement error: (a) the ratios are not validated against actual phoneme counts, (b) the error varies by language in unknown ways, and (c) the error could bias the correlation in either direction. A language with a ratio of 1.2 vs 0.8 could have its phoneme distance systematically over- or under-estimated by 33%, which is large enough to mask a real effect.
  Action: (a) Use epitran for all supported languages and report which languages were successfully transcribed. (b) For unsupported scripts, either use a consistent character-count proxy across ALL languages (not mixing real phonemes with character approximations) or exclude those languages from the phoneme-space analysis. (c) Add a measurement-error analysis: sample actual words from each language, compare estimated vs actual phoneme counts, and report the correlation and mean absolute error. (d) If the ratio approach must be retained, derive the ratios empirically from a word sample rather than hardcoding them, and report the derivation method.
- [MAJOR] (evidence) The two analyses cover substantially different language sets. The word-space analysis covers 55 languages, the phoneme-space analysis covers 37 languages, and only 22 languages appear in both. Of these 22, 13 use different treebanks. More importantly, 33 languages appear in ONLY ONE analysis: 33 languages are in word-space only (including low-resource languages like Buryat, Boro, Coptic, Egyptian, Gothic, Old Hebrew, Old Church Slavonic), and 15 languages are in phoneme-space only (including major languages like Spanish, Russian, Persian, Turkish, Vietnamese). This means the null finding in word-space and the marginal finding in phoneme-space come from DIFFERENT language samples. The paper presents these as a unified '55-language study' but the effective sample for any single claim is much smaller and compositionally biased.
  Action: Add a table showing the exact language composition of each analysis. Explicitly state that the word-space and phoneme-space results come from different language samples. If possible, re-run both analyses on a common language set. At minimum, discuss how the different language compositions could affect the results (e.g., the phoneme-space sample includes more Slavic languages, which could affect the correlation).
- [MAJOR] (rigor) The marginal phoneme-space result (r=-0.32, p=0.051) does not survive multiple-comparison correction. The paper tests three hypotheses (H1: phonological density → MDD word-space; H2: word order → MDD; H3: phonological density → PID). With three tests at α=0.05, the Bonferroni-corrected threshold is 0.017, and the FDR-corrected threshold is approximately 0.033. The p=0.051 result fails both corrections. The paper acknowledges this ('could be a Type I error') but still presents it as 'suggestive' without the appropriate statistical qualification. Given the measurement error in phoneme estimation, the effective number of comparisons is even higher (each phoneme estimate introduces its own error term).
  Action: Apply multiple-comparison correction (Bonferroni or FDR) and report corrected p-values. If the result does not survive correction, state clearly that it is not statistically significant after correction. Do not present uncorrected marginal results as 'suggestive' without this qualification.
- [MINOR] (methodology) The mixed-effects model has only 10 levels of the random effect (language family), with one family (Indo-European) containing 20 of 55 languages. While the ICC of 0.14 suggests some family-level clustering, the likelihood ratio test (χ²=2.66, p=0.10) indicates the family effect does not significantly improve model fit. With only 10 families, the random-effects variance estimate is unreliable (rule of thumb: need ≥20-30 groups for stable variance estimation). The paper correctly reports this but could be more explicit about the limitation.
  Action: Add a sentence explicitly stating that the mixed-effects model has limited power due to the small number of language families (n=10). Consider supplementing with a phylogenetic generalized least squares (PGLS) analysis using a language family tree, which can handle small numbers of groups more effectively.
- [MINOR] (scope) Phonological density is measured as phoneme inventory size alone, normalized to [0,1]. This captures only one dimension of phonological complexity. Languages with the same inventory size can have very different phonotactic complexity (e.g., English allows complex onset clusters like /str/ while Japanese allows only /C(V)/). The paper acknowledges this limitation but does not attempt to quantify how much information is lost. The PHOIBLE database includes phonotactic complexity measures (max onset/coda cluster sizes) that could provide a more complete density metric.
  Action: Add a sensitivity analysis using only languages with complete phonological data (inventory size + phonotactic complexity). If the results hold in this subsample, this strengthens the conclusion. Report the correlation between inventory size and phonotactic complexity to quantify the information loss from using inventory size alone.
- [MINOR] (clarity) The paper states 'Mean phonological density across the sample was 0.50 (σ = 0.09)' but the evaluation artifact reports phon_density_mean=0.503 and phon_density_std=0.094. These are consistent but the paper rounds differently. More importantly, the paper does not clarify whether the 55-language or 37-language sample is being described. Given the different language compositions, the mean and SD would differ between samples.
  Action: Specify which language sample (55 or 37) each descriptive statistic refers to. Use consistent rounding across the paper and artifacts.
- [MINOR] (evidence) The functional-lexical dependency split shows no significant difference (z=-0.90, p=0.37), despite Gerdes (2026) finding a robust split (functional MDD=1.71, lexical MDD=2.87). The paper attributes this to 'between-language variance overshadowing the within-language effect' but does not test this hypothesis. If the within-language split is significant but the between-language mean difference is not, this would be an important finding about the stability of the functional-lexical distinction.
  Action: Test the functional-lexical split within each language (paired test) and report the proportion of languages showing a significant split. This would clarify whether the null result reflects true absence of the effect or insufficient power in the between-language comparison.
- [MINOR] (clarity) The paper claims '55 languages from 10 families' but the family breakdown adds to 55 only if isolates and unclassified entries are counted as a separate family. The evaluation artifact reports n_families=10, but the text lists 10 named families plus 'isolates and unclassified entries,' which would be 11 groups. Clarify the family count.
  Action: Provide an exact table of language counts per family, including how isolates and unclassified entries are handled. Ensure the total adds to 55.
- [MINOR] (scope) The paper does not control for treebank size (number of sentences/tokens) as a potential confound. Larger treebanks may have different MDD estimates due to genre composition or annotation quality. The word-space and phoneme-space analyses use different treebanks, which likely differ in size. Chen (2026) shows that corpus properties affect MDD estimates.
  Action: Add treebank size (number of sentences) as a covariate in the regression models. Report whether the phonological density effect changes when controlling for treebank size. This is especially important given the treebank-switching problem.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/user_uploads`. Check this folder for anything relevant to your task. It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-08 01:10:20 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SYSTEM-USER prompt · 2026-09-08 01:11:04 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Null finding confirmed and strengthened; marginal phoneme-space result reframed as non-significant after correction; adds treebank consistency and measurement rigor requirements.' is too long (at most 120 characters, got 178)
Every required field must be present and every field type must match the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
