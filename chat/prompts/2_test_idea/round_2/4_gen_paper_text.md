# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_nBwvdB3PKEF8` — Phonological Density Does Not Predict Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-09-08 00:49:30 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>
<writing_register>
Write in the register of the field's best papers (the passages you collect in the STYLE EXEMPLARS todo), not in the register of a language
model. Four things are measured on the finished draft, and a draft outside them is sent back with
the numbers:
- Never use: delve, underscore, showcase, intricate, pivotal, realm, commendable, meticulous, tapestry, garner, multifaceted, it is worth noting, plays a crucial role, not only ... but also. These are 10 to 30 times more frequent in machine-written abstracts than in
  human ones, and reviewers read them as such.
- Em dashes: at most 3 per 1,000 words. Use a comma, a colon or a full stop.
- Sentence rhythm: mix short and long sentences. An interquartile range of sentence length under
  8 words reads as machine-written.
- Hedging: at most 15 hedges (may, likely, suggests, appears) per 1,000
  words. State what the evidence supports plainly; hedge where it is thin, not everywhere.
Style never changes substance: numbers, claims, citations and figure markers stay exactly as the
evidence gives them. The user's original request (delivered as a separate message) overrides all
of this wherever the two conflict.
</writing_register>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Phonological Density Does Not Predict Dependency Distance Minimization: A Cross-Linguistic Test Across 55 Languages

## Abstract

Dependency distance minimization (DLM) predicts that syntactically related words appear in close linear order. A recent hypothesis suggested that phonologically dense languages, with larger phoneme inventories, should exhibit stronger DLM to compensate for parsing difficulty. We test this across 55 languages from 10 families using Universal Dependencies treebanks. We compute dependency distances in both word-space and a novel phoneme-space metric, then correlate phonological density with DLM strength. Results show a weak positive correlation that fails to reach significance. Phonological density explains only 5% of variance in mean dependency distance. Word-order typology similarly fails to predict MDD. We confirm the functional-lexical dependency split and introduce phoneme-space distance as a methodological contribution for future work.

## 1. Introduction

Dependency distance minimization (DLM) is one of the most replicated empirical regularities in cross-linguistic syntax. Since Liu's [1] foundational study of 15 languages, researchers have documented that heads and dependents tend to appear near each other in linear order, reducing working-memory load during parsing [2, 3]. The effect holds across typologically diverse families and both spoken and written modalities [4].

Two blindspots persist in this literature. First, DLM has always been measured in word-space: distance equals the number of intervening words between head and dependent. This ignores phonological structure. A dependency spanning three monosyllabic words in Japanese occupies far less phonological space than the same word-count dependency in English. Second, no study has asked whether phonological density modulates DLM strength. Languages with larger phoneme inventories and more complex syllable structures face harder parsing problems. If speakers compensate by minimizing syntactic distance, phonologically dense languages should show stronger DLM.

We test this phonotactic constraint hypothesis using Universal Dependencies treebanks from 55 languages spanning 10 families. We compute dependency distances in both word-space and phoneme-space, where distance equals the number of phonemes between head and dependent. We then correlate phonological density, derived from PHOIBLE inventory sizes, with mean dependency distance, controlling for word-order typology.

The results do not support the hypothesis. Phonological density shows a weak positive correlation with MDD ($r = 0.19$), running in the opposite direction from prediction. The effect is not statistically significant ($p = 0.17$). Word order similarly fails to predict MDD. The phoneme-space metric produces larger values (mean 10.6 phonemes) than word-space (mean 3.0 words), confirming that phonological and syntactic distances operate on different scales.

These null findings are informative. They suggest that phonological density and syntactic optimization operate independently, or that the hypothesized compensation mechanism is too weak to detect at the cross-linguistic level. We discuss alternative explanations in Section 5.

Our contributions are threefold. First, we introduce a phoneme-space dependency distance metric that separates phonological from syntactic proximity. Second, we report the largest cross-linguistic test of the phonotactic constraint hypothesis to date, covering 55 languages. Third, we replicate the functional-lexical dependency split [5] and document family-level variance patterns.

## 2. Related Work

Dependency distance minimization was first documented by Liu [1] for 15 languages, establishing MDD as a universal tendency. Futrell et al. [2] extended this to 37 languages using Universal Dependencies, confirming cross-family robustness. Ferrer-i-Cancho and Gómez-Rodríguez [3] showed that reduced dependency distance, the minimum distance over all subsegments, reveals distributed cost structure beyond simple MDD.

The information-theoretic perspective provides a complementary framework. Coupé et al. [6] demonstrated that languages encode information at approximately 39 bits per second, with syllable rate and information density compensating for each other. This modulation integrity hypothesis suggests that phonological and syntactic constraints jointly optimize around channel capacity. Our work tests a specific instantiation: whether phonological density modulates syntactic optimization.

Functional versus lexical dependencies form a well-established dichotomy. Gerdes [5] showed that functional dependencies, determiners, case markers, auxiliaries, are universally short because grammar hard-codes their adjacency. Lexical dependencies, subjects, objects, modifiers, are longer and more sensitive to typological variation. Our results confirm this split.

Corpus choice affects DLM estimates. Dobrovoljc [7] demonstrated that ordinal rankings of languages by MDD are unstable across treebanks, indicating that corpus composition interacts with distance metrics. Our analysis uses a single standardized treebank per language to minimize this confound, but we acknowledge residual variability.

Phonological typology has been linked to syntactic patterns in limited ways. Ferrer-i-Cancho [8] showed that DLM predicts word-length minimization, hinting at phonological-density interactions. However, no study has systematically tested whether synchronic phonological density predicts DLM strength.

## 3. Method

### 3.1 Data

We extracted Universal Dependencies treebanks from the `commul/universal_dependencies` repository on HuggingFace [9]. We selected one configuration per language, preferring treebanks with the largest training splits. This yielded 55 languages across 10 families: Indo-European (28), Uralic (4), Turkic (3), Afroasiatic (4), Sino-Tibetan (4), Austronesian (5), Japonic (1), Koreanic (1), Tai-Kadai (2), and Austroasiatic (2), plus isolates and unclassified entries.

Phonological features came from PHOIBLE 2.0 [10]. We used phoneme inventory size as the primary density metric. Phonological density was normalized to $[0, 1]$ by dividing by the maximum observed inventory (70 phonemes). Additional features, phonotactic complexity (max onset + coda cluster size) and syllable type richness, were derived from PHOIBLE but excluded from final models due to missing values for 12 languages.

Word-order typology came from WALS [11]. We classified languages as SVO ($n = 41$), SOV ($n = 11$), or VSO ($n = 3$). Register was uniformly written across all treebanks, matching the corpus composition of prior DLM studies [2, 7].

### 3.2 Dependency Distance Metrics

Word-space MDD follows standard practice [1, 2]. For each dependency arc $(h, d)$, distance equals $|pos(h) - pos(d)|$, the absolute difference in token positions. Mean dependency distance equals the arithmetic mean across all arcs in a treebank.

Phoneme-space MDD (PPAD) extends this to phonological units. For each word $w$, we estimated constituent phonemes from PHOIBLE inventory data. We used a family-level average phoneme count as proxy when language-specific G2P was unavailable. Phoneme-space distance for arc $(h, d)$ equals:

$$PPAD(h, d) = |pos(h) - pos(d)| \times \frac{\phi_h + \phi_d}{2}$$

where $\phi_w$ is the phoneme count of word $w$. This weights each arc by the phonological material between head and dependent.

Both metrics were computed per treebank, then aggregated by language. Functional dependencies used the standard UD tagset: `det`, `case`, `aux`, `mark`, `cc`, `punct`, and their subtypes. Lexical dependencies included all remaining relations.

### 3.3 Statistical Analysis

We tested three hypotheses: (H1) phonological density predicts MDD, (H2) word order predicts MDD, (H3) phonological density predicts PPAD. For H1 and H3, we fitted OLS regression with MDD as response and normalized phonological density as predictor. For H2, we fitted one-way ANOVA with word order as factor. We reported Spearman rank correlations as non-parametric robustness checks. All analyses used $\alpha = 0.05$.

We computed family-level variance to assess whether patterns hold within independent lineages. However, most families contained fewer than 5 languages, limiting mixed-effects modeling. We report family means and ranges descriptively.

### 3.4 Implementation

Code is available at [ARTIFACT:art_3GjyqsiFc7Gb]. Processing used Python 3.12 with the `datasets` library for HuggingFace access, `numpy` for numerical operations, and `scipy` for statistical tests. Runtime was approximately 600 seconds across all 55 languages.

## 4. Results

### 4.1 Word-Space Dependency Distances

Mean MDD ranged from 1.96 (Kurdish Sorani, ckb) to 4.15 (Arabic, ar) across 55 languages. The overall mean was 3.07 with standard deviation 0.63. Median MDD was 3.0 in all but three languages, indicating right-skewed distributions typical of DLM.

Word order did not predict MDD significantly. SVO languages averaged 3.07 ($n = 41$), SOV languages averaged 3.04 ($n = 11$), and VSO languages averaged 3.67 ($n = 3$). ANOVA yielded $F = 1.36$, $p = 0.27$ [FIGURE:fig1]. Kruskal-Wallis, a non-parametric alternative, also failed to reach significance ($H = 2.23$, $p = 0.33$).

[FIGURE:fig1]

### 4.2 Phonological Density and DLM

The phonotactic constraint hypothesis predicted a negative correlation: denser phonological systems should exhibit stronger DLM (lower MDD). The observed correlation ran in the opposite direction. Spearman $r = 0.19$, $p = 0.17$ [FIGURE:fig2]. OLS regression yielded $R^2 = 0.05$, phonological density coefficient $= 1.50$, intercept $= 2.34$. The coefficient was positive, indicating that denser languages tend toward *longer* dependencies, though the effect is small and non-significant.

[FIGURE:fig2]

Family-level analysis showed inconsistent patterns. Indo-European languages ($n = 28$) ranged from 2.34 (Latin) to 4.15 (Arabic) in MDD, with no clear density-distance relationship. Uralic languages ($n = 4$) averaged 2.89, below the overall mean, but contained both low-density Finnish (36 phonemes) and relatively high-density Estonian (38 phonemes). Turkic languages ($n = 3$) averaged 3.12, with Turkish (29 phonemes) showing the lowest MDD in the family.

### 4.3 Phoneme-Space Distances

Phoneme-space MDD (PPAD) averaged 10.62 phonemes across languages, with standard deviation 4.23. PPAD was consistently larger than word-space MDD, as expected given that words contain multiple phonemes. The ratio PPAD/MDD averaged 3.5, corresponding to average word length of 3.5 phonemes.

PPAD correlated with word-space MDD ($r = 0.89$, $p < 0.001$), confirming that phoneme-space and word-space distances capture related but distinct aspects of dependency structure. The weaker correlation within languages (mean $r = 0.72$) indicates that phonological composition modulates the word-space pattern.

### 4.4 Functional versus Lexical Dependencies

Across all languages, functional dependencies averaged 2.7 words while lexical dependencies averaged 3.4 words [FIGURE:fig3]. The functional-lexical split was consistent across word-order types and language families. This replication confirms prior findings [5] and validates our treebank processing pipeline.

[FIGURE:fig3]

### 4.5 Regression Analysis

We fitted OLS regression of MDD on phonological density, word order, and their interaction. Phonological density was non-significant ($\beta = 1.50$, $SE = 1.12$, $p = 0.18$). Word order showed a marginal effect ($F = 2.89$, $p = 0.06$), driven primarily by the small VSO group. The interaction term was non-significant ($p = 0.42$). The full model explained 8% of variance ($R^2 = 0.08$), only 3 percentage points above the phonological density model alone.

## 5. Discussion

### 5.1 Null Findings and Their Interpretation

The primary finding is negative: phonological density does not predict dependency distance minimization. This contradicts the phonotactic constraint hypothesis, which predicted that dense phonological systems would compress syntactic dependencies to compensate for parsing difficulty.

Several explanations deserve consideration. First, the effect may be too small to detect with current methods. The correlation ($r = 0.19$) is in the small-to-medium range but non-significant. With 55 languages, we had 80% power to detect $r = 0.28$ at $\alpha = 0.05$. The true effect may lie below this threshold.

Second, phonological density and syntactic optimization may operate at different timescales. DLM is often interpreted as a processing constraint that shapes contemporary sentence structure. Phonological density, by contrast, reflects historical sound changes that operate over centuries. The mismatch in temporal scale could obscure synchronic correlations.

Third, the compensation mechanism may exist but manifest differently than predicted. Rather than minimizing dependency distance, speakers in dense phonological systems might reduce phonological complexity in adjacent words (phonological reduction) or increase morphological marking (to clarify roles without linear proximity). These alternatives are empirically testable but were not examined here.

### 5.2 Methodological Contributions

Despite the null finding, we introduce two methodological innovations. First, phoneme-space dependency distance (PPAD) provides a metric that separates phonological from syntactic proximity. PPAD can identify cases where words are linearly close but phonologically distant, or vice versa. This distinction may prove useful for studies of phonological phrasing and prosodic syntax.

Second, our standardized pipeline for combining UD treebanks with PHOIBLE data is publicly available [ARTIFACT:art_3GjyqsiFc7Gb] and [ARTIFACT:art_vqt7I2AbkCLO]. It enables replication and extension to other phonological features, such as tone inventory or vowel harmony complexity.

### 5.3 Limitations

Several limitations warrant acknowledgment. First, phonological density was measured as phoneme inventory size alone. We lacked reliable data on phonotactic complexity and syllable type richness for all 55 languages. These features may capture aspects of phonological density that inventory size misses.

Second, all treebanks were written corpora. Spoken corpora might reveal different patterns if phonological pressure operates primarily in speech. Our dataset includes no spoken UD treebanks, though this limitation affects all current DLM research.

Third, the VSO group contained only 3 languages, limiting statistical power for that word-order type. The non-significant ANOVA may reflect insufficient sample size rather than true absence of effect.

Fourth, family-level analysis was descriptive due to small family sizes. Mixed-effects modeling with language family as random effect would be preferable but requires larger within-family samples.

## 6. Conclusion

We tested whether phonological density predicts dependency distance minimization across 55 languages. The hypothesis predicted stronger DLM in phonologically dense systems. Results showed a weak positive correlation ($r = 0.19$, $p = 0.17$) that failed to reach significance. Phonological density explained only 5% of variance in MDD. Word order also failed to predict MDD significantly.

The null finding does not falsify the phonotactic constraint hypothesis definitively. The effect may be too small to detect, may operate at different timescales, or may manifest through mechanisms other than dependency compression. What the results do establish is that phonological density is not a strong predictor of syntactic optimization at the cross-linguistic level, at least not in the way the hypothesis predicted.

We recommend three directions for future work. First, extend the analysis to spoken corpora to test whether phonological pressure is modality-specific. Second, incorporate additional phonological features, phonotactic complexity, syllable typology, prosodic structure, when data becomes available. Third, investigate alternative compensation mechanisms, such as phonological reduction or increased morphological marking, that might mediate the phonology-syntax interface.

The phoneme-space dependency distance metric we introduce can support these extensions. By separating phonological from syntactic proximity, PPAD offers a tool for studying the interface between phonology and syntax in ways that word-space metrics cannot.

## References

[1] Liu, H. (2008). Complexity of two types of dependency distance. *Proceedings of the Sixth International Workshop on Treebanks and Linguistic Theories*, 263-274.

[2] Futrell, R., Mihlhöfer, E., & Levy, R. (2015). Dependency distance is a major factor in the evolution of word orders. *Proceedings of the National Academy of Sciences*, 112(39), 11987-11992.

[3] Ferrer-i-Cancho, R., & Gómez-Rodríguez, C. (2021). Reduced dependency distance from sum to natural subsegment. *Scientific Reports*, 11, 1-10.

[4] Krielke, S. (2024). Diachronic shift toward intra-phrasal dependencies in scientific German and English. *Linguistics*, 62(3), 567-598.

[5] Gerdes, K. (2026). The grammar does the work: Functional vs. lexical dependencies. *Proceedings of ACL 2026*.

[6] Coupé, C., Meyer, D., & Pellegrino, F. (2019). Languages encode information at the same rate. *Science Advances*, 5(6), eaaw5660.

[7] Dobrovoljc, K. (2026). How much does corpus choice change dependency-distance estimates? *Journal of Quantitative Linguistics*, 33(1), 1-25.

[8] Ferrer-i-Cancho, R. (2021). Dependency distance minimization predicts compression. *Scientific Reports*, 11, 1-10.

[9] Universal Dependencies. (2024). commul/universal_dependencies [Computer software]. Hugging Face.

[10] Moran, S., McCloy, D. R., & Wright, R. (2016). PHOIBLE 2.0. *Proceedings of the 17th Annual Conference of the International Speech Communication Association*, 1678-1682.

[11] Dryer, M. S., & Haspelmath, M. (2013). World Atlas of Language Structures Online. *Max Planck Digital Library*.

## Data and Code Availability

All code and data are available at [ARTIFACT:art_3GjyqsiFc7Gb], [ARTIFACT:art_vqt7I2AbkCLO], and [ARTIFACT:art_X5Bdc3dR_RYR].
</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) PPAD formula is misdescribed. The paper states PPAD equals 'the number of phonemes between head and dependent' but the actual formula PPAD(h,d) = |pos(h) - pos(d)| × (φ_h + φ_d)/2 computes the word-distance weighted by the AVERAGE phoneme count of the two connected words. This is not the phonemes in the intervening span — it is a phoneme-count-weighted distance metric. For example, a dependency between two 10-phoneme words at distance 3 gets PPAD = 3 × 10 = 30, regardless of how many phonemes are actually between them. This is a fundamental discrepancy between the claimed metric and the implemented one.
  Action: Either (a) correct the formula to sum phonemes of all words between head and dependent: PPAD(h,d) = sum of φ_w for all words w strictly between h and d, or (b) rename the metric (e.g., 'phoneme-weighted dependency distance') and accurately describe what it measures. If keeping the current formula, clarify in the paper that it weights dependencies by the phonological mass of the connected words, not the phonological span between them. This is essential for the metric to be interpretable and comparable to prior work.
- [MAJOR] (methodology) Evaluation artifact used synthetic data, not real UD treebanks. The eval.py file states: 'Note: This evaluation used synthetic treebanks due to unavailability of the HuggingFace datasets library in the execution environment.' The full_eval_out.json shows identical MDD values (2.777...) across all 8 languages, confirming synthetic/fabricated data. While the experiment artifact (method.py) does load real UD treebanks, the evaluation artifact — which reports the mixed-effects regression and family-level variance — did not. This means key results in the paper (particularly any claims about family-level patterns or mixed-effects models) may not be based on real data.
  Action: Re-run the evaluation artifact against real UD treebanks. If the HuggingFace datasets library is available in the execution environment, remove the synthetic fallback. At minimum, add a clear disclaimer in the paper stating that evaluation artifacts used synthetic data for methodological validation, and report which results come from real data vs. synthetic validation. This is critical for reproducibility and reviewer trust.
- [MAJOR] (novelty) The paper claims 'no study has systematically tested whether synchronic phonological density predicts DLM strength' but Ferrer-i-Cancho & Gómez-Rodríguez (2021) 'Dependency distance minimization predicts compression' (arXiv:2109.08900, published in SyntaxFest 2022) directly tested the relationship between DLM and phonological compression using UD treebanks. They found that DLM predicts phonological compression (word length in phonemes) when using a proper optimality score, but not with raw sum of dependency distances. While the current paper tests the reverse direction (phonological density → DLM, rather than DLM → phonological compression), the prior work directly engages with the DLM-phonology interface using the same data source (UD treebanks). The paper should acknowledge and distinguish its contribution from this prior work.
  Action: Add a paragraph in Section 2 (Related Work) discussing Ferrer-i-Cancho & Gómez-Rodríguez (2021). Clarify the distinction: they tested whether DLM predicts phonological compression (syntax → phonology), while you test whether phonological density predicts DLM strength (phonology → syntax). This is a different directional hypothesis, but the prior work is directly relevant and should be engaged with, not merely mentioned in passing. This strengthens the paper's positioning.
- [MAJOR] (rigor) No phylogenetic control despite severe sample skew. 28 of 55 languages are Indo-European (51%), with most from a single branch (Germanic, Romance, Slavic). This violates the independence assumption of OLS regression and could produce spurious correlations. With 28 Indo-European languages clustered together, any effect found could be a family-specific artifact rather than a cross-linguistic generalization. The paper acknowledges this limitation but does not attempt to address it.
  Action: Add a mixed-effects regression with language family as a random intercept. With 28 Indo-European languages, there is sufficient data for a meaningful random-effects model. Even a simple random-intercept model (family ~ 1) would control for phylogenetic non-independence. Report both the OLS and mixed-model results. If the mixed model shows the effect disappears, this is an important finding in itself.
- [MINOR] (rigor) Epitran fallback to character count for non-Latin scripts. When epitran is unavailable for a language, the code falls back to max(len(word), 1) character counts as phoneme proxies. For CJK languages (Japanese, Korean, Chinese), this means PPAD is effectively a character-space metric, not a phoneme-space metric. For languages with morpheme-boundary ambiguity (e.g., agglutinative Turkish), character count is a rough approximation. This creates inconsistency: some languages have real phoneme counts, others have character counts.
  Action: Either (a) use a consistent phoneme estimation method for all languages (e.g., always use character count as a lower-bound approximation), or (b) flag which languages use real phoneme data vs. character approximations and conduct a sensitivity analysis excluding approximated languages. Report this as a limitation even if not fully resolved.
- [MINOR] (evidence) Small VSO sample (n=3) included in ANOVA. The paper correctly acknowledges this limitation but still includes VSO in the ANOVA comparing SVO/SOV/VSO. With only 3 VSO languages (Arabic, Syriac, and one other), the VSO group mean of 3.67 is unstable and could disproportionately influence the ANOVA F-statistic.
  Action: Report the ANOVA both with and without the VSO group. If the non-significant word-order result holds without VSO, this strengthens the conclusion. Consider also reporting the effect size (η²) for the word-order comparison, not just the p-value.
- [MINOR] (clarity) Citation inaccuracy: Gerdes (2026) is cited as 'Proceedings of ACL 2026' but the paper (doi: 10.63317/4akqrtsv7i65) was published in LREC 2026 (Proceedings of the 15th Language Resources and Evaluation Conference). This is a factual error that undermines credibility.
  Action: Correct the Gerdes (2026) citation to 'Proceedings of LREC 2026' with the correct DOI. Also verify the Futrell et al. (2015) citation — the search results suggest the PNAS word-order paper may be from 2020 (doi: 10.1073/pnas.1910923117), not 2015.
- [MINOR] (clarity) Dataset size discrepancy: the dataset artifact (art_vqt7I2AbkCLO) claims 39 languages while the paper and experiment artifact claim 55. The data.py TARGETS list contains 38 entries (not 39). This inconsistency across artifacts suggests poor documentation hygiene.
  Action: Ensure all artifacts (dataset, experiment, evaluation) consistently report the same number of languages. If the final analysis used 55, the dataset artifact should reflect this. Add a data availability statement with exact language counts per artifact.
- [MINOR] (scope) Phonological density is measured as phoneme inventory size alone. The paper acknowledges that phonotactic complexity and syllable type richness were excluded due to missing values, but these features may capture important aspects of phonological density that inventory size misses. A language with 30 phonemes but complex syllable structures (e.g., consonant clusters) may be functionally denser than a language with 40 phonemes but simple CV syllables.
  Action: Add a sensitivity analysis using only languages with complete phonological data (phoneme count + phonotactic complexity + syllable type). If the results hold in this subsample, this strengthens the conclusion. Report the correlation between inventory size and the excluded features to quantify the information loss.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 6 research artifacts across all iterations.

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
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_nrvjYtfmx0_F
title: Phoneme-Space Dependency Distance Analysis Across 37 Languages
type: experiment
summary: >-
  Recomputed dependency distances in phoneme-space across 37 Universal Dependencies treebanks using language-family-specific
  phoneme estimation ratios. The corrected Phoneme-Interval Distance (PID) metric sums phoneme counts strictly between head
  and dependent in each dependency arc. Results show a weak negative correlation (r=-0.324, p=0.051) between phonological
  density and mean PID, suggesting languages with higher phonological density may exhibit marginally stronger dependency length
  minimization in phoneme-space. The rank correlation between word-based and phoneme-based distances is moderate (r=0.523,
  p=0.001), indicating phoneme-space provides a meaningfully different but correlated view of syntactic distance. Regression
  explains ~10.7% of variance. Five publication-quality figures generated. Output validated against exp_gen_sol_out schema
  with additional analysis fields.

id: art_21q7z-GCrosW
title: Mixed-Effects Evaluation of Phonology-Syntax Independence
type: evaluation
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

id: art_N1HzZ0zfSC52
title: Literature deep-dive on DLM-phonology compression asymmetry
type: research
summary: >-
  This research produced a comprehensive literature deep-dive on the relationship between dependency distance minimization
  (DLM) and phonological compression. The central finding is that our null hypothesis (phonological density does NOT predict
  DLM strength) is theoretically consistent with FC&GR (2021) positive finding because the syntax-phonology optimization relationship
  is directionally asymmetric. FC&GR used a normalized optimality score Ω and found significance only with phoneme-based word
  length (τ = -0.37, p = 0.039), not syllable-based. Chen (2026) further shows MDD is corpus-conditioned with 40% of language
  rankings reversing across treebanks. The research integrates 15 sources and produces both research_out.json and research_report.md.
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib, aii-web-tools.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. STYLE EXEMPLARS: Decide which field or fields this paper belongs to; a paper spanning two
fields takes exemplars from both. If `./style_exemplars.md` already exists in your workspace
(a previous iteration wrote it), read it and skip the search. Otherwise use the aii-web-tools
skill's scholarly search (OpenAlex) to find the best-cited open-access papers of the last five
years closest to this paper, fetch four or five of them through the skill's fetch tool (arXiv HTML
or PDF), and copy VERBATIM into `./style_exemplars.md`, each passage headed by the paper's
title, year and URL: the abstract, the first paragraph of the introduction, one results paragraph
that reports numbers, and one discussion or limitations paragraph. Read the file once as a whole
and put one line at its top on how those papers handle sentence length, hedging, first person and
citation density. Write the paper in that register. Their sentences and their content are never
reused; they are exemplars of style, not sources.
TODO 4. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 5. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Do NOT emit your structured output when the draft is done — TODO 6 is a
separate revision pass that runs over the finished draft first.
TODO 6. REVISION PASS — start this ONLY once TODO 5's draft is complete, and treat it as a distinct
pass over the finished text rather than something folded into the writing. Read
`REVISION_CHECKLIST.md` in the aii-paper-writing skill's own directory and apply every item to the
full draft.

Writing and revising are different jobs and cannot be done at the same time. The defects that
checklist targets — prose denser than the field needs, an abstract dumped full of numbers, sections
that leak into one another, a Figure 1 that shows a side result instead of the main idea, close
prior work that only the draft's FINAL vocabulary would have surfaced, a study of N things that
plots eight of them, section names that mean nothing to someone who has not read the section,
implementation filenames cited in the prose, numbers that disagree between the abstract, the text
and the tables — are all invisible while drafting, because you are holding your intent rather than
the text. Every one is obvious to the first outside reader.

Work the items one at a time against the ACTUAL text, not from memory of what you meant to write.
For each item, either fix the draft or state in one line why it already holds. The checklist's
consistency section is several SEPARATE sweeps of the whole paper, one concern per sweep — run them
that way, and repeat any sweep that produced an edit, since a fix in one place routinely breaks
agreement somewhere else. Expect this pass to change the draft; one that produces no edits was not
really run.

Only when the checklist is fully worked through, emit the structured JSON — that is your ONLY
output. Do NOT compile LaTeX or generate image/figure files at any point.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/user_uploads`. Check this folder for anything relevant to your task. It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1'). Letters, digits and underscore only \u2014 a hyphen or space cannot be extracted from its own marker.",
          "pattern": "^\\w+$",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-08 00:49:30 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-09-08 00:49:38 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: "Writes the PROSE of an AI research paper: abstract, introduction, related work, methods, experiments, discussion and conclusion, with a page budget, the 5-paragraph intro pattern, writing-quality rules, inline [FIGURE:fig_id] markers plus a structured figures array, and a MANDATORY REVISION_CHECKLIST.md pass over every finished draft. Use whenever a paper, abstract, section, or full write-up is being drafted or rewritten for a venue such as NeurIPS, ICML, ICLR or ACL. Triggers: write a paper, paper structure, abstract, introduction, related work, methods, experiments, contributions, figure caption and placement, revision pass, academic prose. NOT for: assembling or compiling .tex (use aii-paper-to-latex), rendering the figure image files (aii-data-fig-gen, aii-concept-fig-gen), fetching BibTeX (use aii-semscholar-bib), or critiquing a finished draft's logic (use amg-paper-verification)."
---

## MANDATORY: the final revision pass

**`REVISION_CHECKLIST.md`, in this skill's own directory, MUST be read and
applied to every finished draft, always, as a separate pass after the writing
is done.** It is not optional, not conditional on how the draft looks, and not
something to fold into the writing itself.

Writing and revising are different jobs and cannot be done in one pass. The
defects that checklist targets — dense prose, a number-dumped abstract, sections
that leak into each other, a Figure 1 that shows a side result, prior work the
final vocabulary would have found, results mentioned but never plotted,
inconsistencies between abstract and tables — are all invisible while drafting,
because the author is holding the intent rather than the text. Every one of them
is obvious to the first outside reader. Reading the checklist before writing
does not substitute: the pass has to run against a finished draft.

So the order is always: write the complete draft → read `REVISION_CHECKLIST.md`
→ work its items against the full text, fixing as you go → only then emit the
output.

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-09-08 00:49:38 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: "Fetches real BibTeX entries in one batch from Semantic Scholar by DOI, ArXiv ID or title via aii_semscholar_bib__fetch, normalises citation keys to AuthorYYYY, injects DOIs, and writes the result into references.bib, with a mandatory web-search fallback for anything not found. ALWAYS use whenever a bibliography, reference list or .bib file is being built or extended, and whenever a citation needs a verified entry instead of an invented one — never hand-write BibTeX first. Triggers: bibliography, references.bib, bibtex, citation key, DOI, arXiv id, Semantic Scholar, reference list, cite these papers, natbib entries. NOT for: writing the text around the citations (use aii-paper-writing), running bibtex and compiling (use aii-paper-to-latex), judging whether cited work supports the claims (use amg-paper-verification), or open-ended literature search and PDF mining (use aii-web-tools)."
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-web-tools · 2026-09-08 00:49:38 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Runs web search, page fetch as markdown, and regex grep over full HTML or PDF text via this skill's own scripts (aii_fast_web_search.py, aii_fast_web_fetch.py) — a free-first keyless search stack with Serper fallback that works even where built-in WebSearch and WebFetch are absent. Use when a query, page, or paper must be searched, read, or mined for an exact quote, number, table value, or methodology sentence, and whenever a lossy summary would lose the detail. Triggers: web search, scholarly search, OpenAlex, Crossref, Serper, fetch a URL as markdown, read a PDF, arXiv, regex grep a page, exact quote, table value, citation check. NOT for: planning a broad multi-source literature review or mass verification campaign — use aii-web-research-tools; NOT for a PDF file already on disk — extraction, form filling, merging and PDF creation are anthropic-pdf; NOT for driving a browser or testing a UI."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [6] SKILL-INPUT — aii-handbook-auto-computational-linguistics · 2026-09-08 00:49:38 UTC

The agent loaded the **aii-handbook-auto-computational-linguistics** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-handbook-auto-computational-linguistics
description: "Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement and human label variation, low-resource and multilingual corpora, benchmark construct validity, LLM-as-judge. ALWAYS read before ANY computational-linguistics research work — ideation/novelty assessment, study planning, experiment/eval design, write-up, or review; do NOT work from priors alone (measurement norms were overturned through 2025-2026 and several obvious directions are saturated). Triggers: computational linguistics, ACL/EMNLP/NAACL/TACL/CoNLL/ARR, psycholinguistics, syntax/morphology/semantics of LMs, dialects and language varieties, annotation. NOT for: building or fine-tuning models, prompt engineering, speech signal processing, agent architecture (use aii-handbook-auto-multi-agent-llm-systems), or model-internal circuits and features (use aii-handbook-auto-mechanistic-interpretability)."
---

<!-- GENERATED by amg-handbook-forge — DRAFT for expert review. v2 (second-pass draft;
     v1 superseded — search-first directive promoted to Overview, density 247->229). generated: 2026-07-27 · next_check:
     2026-10-27 (volatile.md half-life ≈ 3 months). ✓x=exec · [Sn]=cited · ⚠️=candidate.
     Row fails → `STALE: <what>` in place. -->

# Computational linguistics — field handbook

## Overview

Scope: computational linguistics as a SCIENCE of language — what models reveal about language and
about human language processing, and how such claims are measured. NLP engineering (training,
prompting, retrieval, agents) is out of scope. The star is the SUBSTRATE below: a dated,
source-anchored map with an explicit do-not-redo list. The only IDEATION lens is open questions;
a thin execution floor follows it.

**How to use this map.** It is a STARTING POINT, not a substitute for looking. Its crowded
list is necessarily incomplete and its frontier is dated; map-silence means *not-yet-checked*,
never *open*. Before committing to any direction, run your own fresh, dated saturation search
on that specific direction and confirm it is actually unoccupied. Treat the sections below as
material to reason against — the questions especially — rather than as conclusions to accept.

## Organizing principles (how the field reasons)

- **The measurement instrument is itself under audit.** A 445-benchmark, 29-reviewer systematic review found "patterns
  related to the measured phenomena, tasks, and scoring metrics which undermine the validity of the
  resulting claims" [S2] — a capability claim is judged on its construct, not just its number.
- **Output is not competence.** "LLMs' metalinguistic judgments are inferior to quantities directly
  derived from representations" [S3]; grammaticality separates in hidden states where string
  probability does not [S12].
- **A negative result about a model is a claim about your probe:** "negative results relying on
  metalinguistic prompts cannot be taken as conclusive evidence that an LLM lacks a particular
  linguistic generalization" [S3].
- **Disagreement is data.** Human label variation "reflects the diversity of human perspectives
  rather than mere error"; collapsing it manufactures "artificial consensus" [S7].
- **Explanatory status is graded, and the grades are named.** LLMs supply "how-possibly
  explanations (HPEs)" about acquisition and competence, while "current LLMs do not yet satisfy"
  the requirements for how-actually explanations [S4].
- **Theory bounds the empirics** — expressivity results explain "why current transformer
  architectures struggle to implement exact discrete algorithms" [S24] — but they are
  assumption-relative by construction [S11].

## Frontier (recency-weighted)

**Measurement & construct validity** *(weight-capped — the loudest thread)*

- A systematic review of 445 LLM benchmarks by 29 expert reviewers found validity-undermining
  patterns across measured phenomena, tasks and scoring metrics [S2] (NeurIPS 2025).
- The JUDGe 2026 workshop frames judge validity as a systems property: "Evaluation validity is not a property of
  a judge in isolation" [S25] (2026). Peer-reviewed baseline beneath it: reliability varies by
  property, judge expertise, and whether text is human- or model-generated [S21] (ACL 2025).
- Contamination has its own position paper, which sets out to "highlight the wide prevalence of
  benchmark dataset contamination and outline the properties of contamination-resistant datasets"
  [S14] (ICML 2026 Position Track).

**What LMs represent vs what they output**

- A grammaticality probe "outperforms LM probability-based grammaticality judgments" — yet
  on semantic plausibility "the probe however performs worse than string probability" [S12] (2026-05).
- ACL 2026's Best Paper found a directional semantic failure: a "pervasive Teleological Bias" where
  models "hallucinate completion for goal-oriented events, even overriding explicit textual
  cancellation"; prompting interventions "partially reduce this bias but trigger a calibration
  crisis" [S8] (2026).

**Cognitive modelling and the scale paradox**

- Surprisal's fit to reading times peaks near two billion training tokens, after which perplexity
  gains produce "poorer fits to human reading times" [S16] (Findings of EMNLP 2023).
- Not an artifact of latency measures — the inverse relation "still obtains" on two fMRI datasets
  across 17 LMs [S17] (EACL 2026).
- The predictor is unstable: early-layer representations beat surprisal on early-pass eye movements,
  and "the best-performing predictor varies strongly depending on the language and eye-tracking
  measure" [S23] (ACL 2026).

**The resource map and language varieties**

- Catalogue counts mislead: 59% of the surveyed languages score zero catalogued-dataset density, yet literature mining shows active dataset production for many [S5] (2026-05).
- The dominant multilingual benchmark is criticized at protocol level — many translations "fall below
  the claimed 90% quality standard", and "copying named entities, can yield non-trivial BLEU
  scores" [S13] (EMNLP 2025).

**Annotation, disagreement, pluralism**

- The perspectivist turn has its own survey, mapping "a shift from consensus learning toward
  explicitly modeling disagreement, and toward capturing structured relationships among
  annotators" [S6] (2026-01).

**Meta-science of the field**

- Submission volume outran reviewing capacity — 17,087 submissions against 1,424 area chairs,
  with the community weighing "options for limiting submissions for the first time in ACL's
  history" [S1] (2026-05) — yet measured review quality shows "no consistent decline in median
  review quality across venues and years" [S22] (2026-01). ACL 2026's special theme was model
  explainability [S10].

## Recent (~1–2 yr, compressed) · Durable core

- Durable and still load-bearing: surprisal theory as the LM-to-processing-cost bridge [S16];
  minimal-pair evaluation as the standard syntactic instrument [S12]; direct probability
  measurement as the stronger read-out of linguistic knowledge [S3]; the child-learning data
  bound — "less than 100 million words" — with curriculum learning, heavily attempted,
  "largely unsuccessful" [S18].
- The three standing stances on LLMs and linguistic theory [S4]: **insulationism** (LLMs are
  irrelevant to human language), **eliminativism** (they can replace traditional linguistic
  theories), **conciliationism** (they are useful tools for linguistic research).

## ⛔ Already crowded — go ELSEWHERE (do-not-redo)

The blank space is NOT in these lanes; each is saturated through H1-2026:

- **Creating another multilingual / low-resource benchmark.** Dense and institutionalized: the
  FLORES+ family plus its published protocol critique [S13], variety-level suites [S19], and
  and a 232-paper survey of the multilingual/edge pipeline [S20].
- **Benchmark-contamination detection.** Saturated; the prevalence of contamination and the
  properties of resistant datasets are already laid out in a peer-reviewed position paper [S14].
- **LLM-as-judge meta-evaluation and bias catalogues.** A 20-dataset / 11-model peer-reviewed study
  [S21] plus a dedicated 2026 workshop [S25] own this.
- **Minimal-pair grammaticality evaluation and its representation-level follow-up.** Models already
  "discriminate well between grammatical and ungrammatical sentences in tightly controlled minimal
  pairs", and the probe-vs-probability comparison is published [S12].
- **Human label variation / perspectivist modelling.** Mapped end-to-end by its own survey [S6] and
  already escalated into post-training [S7].
- **Computational morphology and low-resource dependency parsing.** Both have their own survey and
  a 2026 cross-architecture evaluation [S29] [S30].
- **Computational sociolinguistics / dialect NLP.** Mapped by its own survey [S27], with a
  variety-level benchmark already published [S19].
- **Sign-language processing tooling and reproducibility.** The ad-hoc-code problem and a framework
  answer to it are published [S28].
- **Language-documentation annotation tooling.** 98 tools already surveyed against documentary
  requirements [S26].
- **Coreference and discourse resolution.** A shared-task series in its fifth edition, with a 2026
  benchmark wave alongside it [S31].
- **Diachronic / lexical semantic change.** Mature enough that its canonical benchmark is itself
  under published critique, with a dedicated workshop series [S32].
- **Surprisal-vs-reading-time psychometrics.** The inverse-scaling result, its tipping point, its
  fMRI generalization, and its layerwise refinement are all published [S16] [S17] [S23].

> **Standing directive — this list is necessarily INCOMPLETE.** Map-silence means *not-yet-checked*,
> NOT *open*. Before committing to any direction this map does not explicitly flag as crowded, run a
> fresh, dated saturation search and confirm the space is actually unoccupied. (Measured in this forge's own
> A/B runs: a live-searching baseline beats a static handbook precisely on the crowded lanes a map omits.)

## Open questions the field hasn't answered

*(the whole lens — the reader answers in their own way)*

1. Prompted output underestimates linguistic knowledge [S3], and grammaticality separates in hidden
   states where string probability does not [S12]. **Is the observable this field treats as its
   measurement — model output, or string probability — even the right object for a claim about
   linguistic competence?** Instruments changed without this being settled.
2. If a review of 445 benchmarks finds validity-undermining patterns [S2] while judge validity is a
   property of a whole pipeline rather than a judge [S25], what would a capability claim here have
   to report before it should be believed?
3. LLMs supply how-possibly but not how-actually explanations of language [S4]. What evidence would
   move a computational result across that line, and does any current design even address it?
4. The best cognitive predictor is a deliberately undertrained model [S16] [S17], while the strongest
   predictor varies by layer, language, and measure [S23]. What is being modelled when psychometric
   fit and language-modelling quality pull in opposite directions?
5. Catalogue counts and literature evidence disagree about which languages are resourced [S5], and
   the dominant benchmark is protocol-flawed for exactly those languages [S13]. Is "low-resource" a
   property of languages, of documentation infrastructure, or of evaluation design?
6. Submission volume outran reviewing capacity to the point of considering caps [S1], yet measured
   review quality has not declined [S22]. If the bottleneck is not quality, what is the constraint
   actually selecting for in what gets published?

## What counts as DEEP here (taste)

| Naive move | Expert judgment/move | Why (failure prevented) | tier | src |
|---|---|---|---|---|
| Add a benchmark, a language, or a model to an existing evaluation and report the numbers. | *Computational Linguistics* prints the bar for a **squib**: "unexpectedness, as for example a demonstration that a commonly accepted idea or method is flawed", or "genuine novelty, as for example thus-far unnoticed language data that challenges current methods". Not "more coverage". | problematizes-nothing — coverage counts only if it breaks something | A | [S9] |
| Probe an LLM on a linguistic phenomenon and report accuracy. | The ACL 2026 **Best Paper** derived a diagnostic from linguistic theory, found a *systematic directional* failure — models "systematically hallucinate completion for goal-oriented events" — and showed prompting fixes "partially reduce this bias but trigger a calibration crisis". Theory-derived contrast plus a failure with a shape. | problematizes-nothing — an accuracy number on a new phenomenon is coverage | L | [S8] |
| Conclude from failed metalinguistic prompts that a model lacks a linguistic generalization. | **Buried (EMNLP 2023):** metalinguistic judgments are inferior to direct probability read-outs, and "consistency gets worse as the prompt query diverges from direct measurements of next-word probabilities". Reopening condition: the same negative result reproduced against direct probability measurement. | wrong-result — you measured the probe, not the model | L | [S3] |

> **Science-vs-application, as this field draws it:** the journal asks for a "substantive
> contribution to the computational processing of language" and clear unexpectedness, genuine
> novelty, or broad relevance [S9]. A working system with a headline number and no overturned
> assumption is application-tier — hence the separate resource, demo, and social-impact award
> tracks rather than one axis [S15].

## Critical rules (execution · eval · validity)

| Naive move | Expert judgment/move | Why (failure prevented) | tier | src |
|---|---|---|---|---|
| Test linguistic knowledge by prompting the model to judge. | Designing the probe: read probabilities directly where possible; report prompting as a second, weaker measurement — never as sole evidence for absence. | wrong-result — negative results are unsound from prompts alone | L | [S3] |
| Report benchmark accuracy as a capability claim. | Writing the claim: define the construct, say how items operationalize it, and report uncertainty. | wrong-result — the score does not measure the named phenomenon | L | [S2] |
| Use FLORES+ as ground truth for low-resource MT quality. | Choosing the eval set: check quality and domain fit for your languages and add a naturalistic set — models strong on one can look weak on the other. | wrong-result — the benchmark's own quality bound caps your conclusion | L | [S13] |
| Aggregate annotations to a majority label by default. | Handling annotation: decide explicitly whether disagreement is error or signal for THIS task; preserve the distribution when it is signal. | wrong-result — artificial consensus erases the phenomenon | L | [S7] [S6] |
| Reach for a pretrained transformer parser on a low-resource language. | Choosing the architecture: below the data crossover a Biaffine LSTM beats transformers, and morphological complexity widens that disadvantage. | wasted-cost — the bigger model is the weaker one in that regime | L | [S30] |
| Call a language low-resource from catalogue counts. | Scoping resources: check literature-level dataset circulation, not just registered catalogues, before claiming a data gap. | wrong-result — the gap may be documentation, not data | L | [S5] |
| Argue cognitive plausibility from a bigger, better LM. | Making a processing claim: treat training data and model scale as deliberate variables and report layer and measure — the best predictor changes with both. | wrong-result — the inverse relation holds on latency and fMRI alike [S17]; fit peaks near 2B training tokens [S16] | L | [S16] [S17] [S23] |

## Decision guide

- **Competence vs performance:** for "does the model know X", read probabilities or probe
  representations [S3] [S12]; for "does it use X when generating", behavioral output is right —
  do not swap them.
- **Cognitive-modelling target:** latency and fMRI now agree on inverse scaling [S16] [S17]; early-
  vs late-pass measures disagree on the best predictor [S23] — name the measure before the model.
- **Aggregating annotations:** aggregate when the task has a defensible single answer; preserve the
  distribution when variation is interpretive [S6] [S7].
- **Placing yourself in the theory debate:** the field names three positions — insulationist,
  eliminativist, conciliationist [S4]; a paper implies one whether or not it says so.

## Ground rules (known-lane — terse)

- Surprisal = negative log probability of a word in context; the standard LM-to-processing-cost link [S16].
- Minimal pairs = near-identical sentences differing in acceptability; BLiMP-style suites are the
  canonical syntactic instrument [S12].
- Human label variation (HLV) = legitimate annotator disagreement, distinct from annotation error [S7].
- Construct validity = whether a measure represents the phenomenon it names; now a routine reviewer
  question in this field [S2].

## Reference documentation

- **[volatile.md](volatile.md)** — dated frontier numbers, lane-occupancy flags, and per-source
  review status. Re-check this FIRST before any novelty verdict or write-up.

## Candidate lane  ⚠️ (expert to resolve — NOT verified)

- ⚠️ **No peer-reviewed 2026 synthesis of "what computational linguistics is now" was recoverable
  this pass.** A Philosophy Compass survey of the philosophy of language models exists but was
  paywalled; the field-identity framing rests on one preprint [S4] plus venue artifacts [S9] [S10].
  Confirm before asserting a field-wide consensus in a write-up.
- ⚠️ **The ACL 2026 award slate could not be read with committee rationale** — the page lists titles
  only, so the taste row rests on the paper's own abstract [S8] plus the journal's printed criteria
  [S9], not a meta-review. Confirm/refute: an award rationale or area-chair commentary for ACL 2026.
```
