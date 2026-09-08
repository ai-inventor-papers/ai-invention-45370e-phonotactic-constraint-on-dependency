# gen_paper_site — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_nBwvdB3PKEF8` — Phonological Density Does Not Predict Dependency Distance Minimization
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_site` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-09-08 03:15:22 UTC

````
<task>
Build the paper's public web page: ONE self-contained `index.html` that lets a reader grasp
this paper faster than opening the PDF would. It is published as this run's GitHub Pages site, so
it is the first thing anyone sees.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<what_is_already_here>
Your workspace is the finished paper folder. It already holds everything the page is made of, and
you must not change any of it — you are adding one file, not revising the paper.

- `paper.tex` — the paper as it was actually written. This is the source of truth for
  every claim, name and NUMBER that goes on the page.
- `paper.pdf` — the compiled paper. The page must NOT link to it by this local name:
  the PDF is published on the code branch and the page on a different one. Link to it at the
  full URL below instead.
- `references.bib` — the bibliography, when the paper has one.
- `figures/` — every figure the paper uses, flattened into one folder.
- `workspace/` — the scratch folder the LaTeX task worked in. Ignore it.
</what_is_already_here>

<paper_text>
title: Phonological Density Does Not Predict Dependency Distance Minimization
abstract: >-
  Dependency distance minimization (DLM) predicts that syntactically related words appear in close linear order. A natural
  extension asks whether phonologically dense languages, with larger phoneme inventories, exhibit stronger DLM to compensate
  for parsing difficulty. We test this across 55 languages from 10 families using Universal Dependencies treebanks, computing
  dependency distances in both word-space and a corrected phoneme-space metric that sums phonemes of intervening words. We
  find no significant relationship: phonological density does not predict DLM strength, and the effect disappears under phylogenetic
  control. A phoneme-space analysis across 37 languages yields a marginally significant effect in the predicted direction,
  but the effect is modest. The null finding is consistent with the directional asymmetry between syntax-driven phonological
  compression and the reverse direction we test: syntactic optimization drives phonological outcomes, not vice versa.
paper_text: |-
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

  We extracted UD treebanks from the `commul/universal_dependencies` repository on HuggingFace \footnote{Code: \url{https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency/tree/main/round-1/experiment-1}}. We selected one configuration per language, preferring treebanks with the largest training splits. This yielded 55 languages across 10 families: Indo-European (20), Uralic (4), Turkic (3), Afroasiatic (4), Sino-Tibetan (4), Austronesian (5), Japonic (1), Koreanic (1), Tai-Kadai (2), and Austroasiatic (2), plus isolates and unclassified entries [ARTIFACT:art_21q7z-GCrosW].

  Phonological features came from PHOIBLE 2.0. We used phoneme inventory size as the primary density metric. Phonological density was normalized to $[0, 1]$ by dividing by the maximum observed inventory (64 phonemes). Mean phonological density across the sample was 0.50 ($\sigma$ = 0.09).

  Word-order typology came from WALS. We classified languages as SVO ($n = 41$), SOV ($n = 11$), or VSO ($n = 3$). All treebanks were written corpora.

  ### 3.2 Dependency Distance Metrics

  Word-space MDD follows standard practice. For each dependency arc $(h, d)$, distance equals $|pos(h) - pos(d)|$, the absolute difference in token positions. Mean dependency distance equals the arithmetic mean across all arcs in a treebank.

  Phoneme-interval distance (PID) extends this to phonological units. For each word $w$, we estimated constituent phonemes using language-family-specific phoneme estimation ratios derived from PHOIBLE data \footnote{Code: \url{https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency/tree/main/round-2/experiment-1}}. PID for arc $(h, d)$ equals:

  $$PID(h, d) = \sum_{w \in \text{intervening}(h, d)} \phi_w$$

  where $\phi_w$ is the phoneme count of word $w$, and $\text{intervening}(h, d)$ is the set of words strictly between positions $pos(h)$ and $pos(d)$. This sums the phonological material in the span between head and dependent, providing a measure of phonological distance that is distinct from word-count distance.

  For non-Latin scripts (CJK, Arabic, Thai), where epitran was unavailable, we used character counts as a lower-bound approximation of phoneme counts. This limitation is discussed in Section 5.3.

  Both metrics were computed per treebank, then aggregated by language. Functional dependencies used the standard UD tagset: `det`, `case`, `aux`, `mark`, `cc`, `punct`, and their subtypes. Lexical dependencies included all remaining relations.

  ### 3.3 Statistical Analysis

  We tested three hypotheses: (H1) phonological density predicts MDD, (H2) word order predicts MDD, (H3) phonological density predicts mean PID. For H1, we fitted both OLS regression and a linear mixed-effects model with language family as a random intercept. For H2, we fitted one-way ANOVA with word order as factor, reporting results both with and without the VSO group. For H3, we fitted OLS regression on the 37-language PID subsample. We reported Spearman rank correlations as non-parametric robustness checks. All analyses used $\alpha = 0.05$.

  We computed family-level variance to assess whether patterns hold within independent lineages. The mixed-effects model addresses the phylogenetic non-independence concern raised by the Indo-European overrepresentation (20/55 languages).

  ### 3.4 Implementation

  Code is available at  and . Processing used Python 3.12 with the `datasets` library for HuggingFace access, `numpy` for numerical operations, `scipy` for statistical tests, and `statsmodels` for mixed-effects modeling. Runtime was approximately 600 seconds across all 55 languages.

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

  Despite the null finding, we introduce two methodological innovations. First, the phoneme-interval distance metric provides a measure that correctly sums phonological material between head and dependent, rather than weighting by the phoneme counts of the connected words. This distinction matters: a dependency between two 10-phoneme words at distance 3 has PID equal to the sum of phonemes in the intervening words, not $3 \times 10$. Second, our standardized pipeline for combining UD treebanks with PHOIBLE data is publicly available  and enables replication and extension.

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

  All code and data are available at , , [ARTIFACT:art_21q7z-GCrosW], and \footnote{Code: \url{https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency/tree/main/round-1/dataset-1}}.
summary: >-
  We test whether phonological density predicts dependency distance minimization across 55 languages. The null finding (r=0.19,
  p=0.17) is consistent with directional asymmetry: syntax drives phonological compression, not vice versa. We introduce the
  phoneme-interval distance metric and demonstrate that word order does not predict MDD.
</paper_text>

<available_figures>
Each line gives the path the PAGE must use, then the figure's title and caption. It is the same
path the file has on disk here: the publish step copies the page and its figures into one folder,
so what works in this workspace is what works on the live site.

- figures/fig1_v0.jpg — "Research Design: Testing the Phonotactic Constraint Hypothesis" (caption: "Overview of the phonotactic constraint hypothesis and our two-metric approach. The hypothesis predicts that phonologically dense languages (large phoneme inventories) should exhibit stronger dependency distance minimization. We test this using word-space MDD (standard) and phoneme-interval distance PID (novel). Arrows show the predicted (dashed, negative) and observed (solid, positive/null) relationships.")
- figures/fig2_v0.png [render from fig2_v0.pdf first] — "Mean Dependency Distance by Word Order Type" (caption: "Mean dependency distance (MDD) across word-order types. SVO languages (n=41) averaged 3.07, SOV languages (n=11) averaged 3.04, and VSO languages (n=3) averaged 3.67. ANOVA: F=1.36, p=0.27. Excluding VSO: F=0.06, p=0.81, η²=0.0005. Word order does not predict MDD.")
- figures/fig3_v0.png [render from fig3_v0.pdf first] — "Phonological Density vs. Word-Space MDD" (caption: "Scatter plot of phonological density (normalized phoneme inventory size) against mean dependency distance. Spearman r=0.19, p=0.17. OLS: R²=0.05, slope=1.48, intercept=2.34. The positive slope runs opposite to the predicted direction. Mixed-effects model (family random intercept): β=0.84, p=0.39.")
- figures/fig4_v0.png [render from fig4_v0.pdf first] — "Phonological Density vs. Phoneme-Interval Distance" (caption: "Scatter plot of phonological density against mean phoneme-interval distance (PID) across 37 languages. Spearman r=-0.32, p=0.051. OLS: R²=0.11, slope=-0.84, intercept=16.29. The negative slope runs in the predicted direction but is modest. Rank correlation between PID and word-space MDD: r=0.52, p<0.001.")
- figures/fig5_v0.png [render from fig5_v0.pdf first] — "Functional vs. Lexical Dependency Distances" (caption: "Comparison of mean dependency distance for functional dependencies (det, case, aux, mark, cc, punct) versus lexical dependencies (nsubj, obj, obl, etc.) across 55 languages. Functional: mean=2.7. Lexical: mean=3.4. The functional-lexical split replicates Gerdes (2026). Difference not significant in this sample (z=-0.90, p=0.37) due to between-language variance.")
</available_figures>

<figure_requirements>
- Reference every figure as `figures/` plus its filename, exactly as listed above.
  The publish step copies the page and its figures into one folder together, so that relative
  path is what resolves on the live site; anything else breaks once published.
- A browser cannot draw a PDF in an image element. Data figures are delivered as vector PDF for
  LaTeX's benefit, so for each one check whether a PNG of the same name already sits in
  `figures/`; if it does not, render one there at about 200 DPI with pdftoppm or
  pymupdf before referencing it. Renderable formats: .avif, .gif, .jpeg, .jpg, .png, .svg, .webp.
- Write those PNGs into `figures/` and nowhere else — that folder is published, a
  new folder of your own is not.
- Use each figure's own caption. Do not invent new ones, and do not describe a figure you did not
  place on the page.
- Look at every figure before you place it. A figure whose axis labels are unreadable at the size
  you give it is worse than no figure.
</figure_requirements>

<page_structure>
In this order, top to bottom:

1. HERO — the paper's title, the author line as the paper gives it, and a one-paragraph TL;DR in
   plain language: what was asked, what was found, and the single number that carries the finding.
   Not the abstract, and not a rewrite of it. Below it, two links: the PDF and the code
   repository, both at the exact URLs given in the links section below.
2. CONTRIBUTIONS — the paper's actual contributions as three to five scannable cards, each a short
   heading plus one or two sentences. If the paper claims four things, show four cards, not five.
3. METHOD — a walkthrough a technically literate non-specialist can follow: what goes in, what
   happens to it, what comes out, and why the design is the way it is. Lead with the paper's own
   method figure when it has one.
4. RESULTS — the paper's real headline numbers, read out of `paper.tex` and the data
   files behind it, each next to what it was measured on and what it is being compared against.
   A number that is not in the paper does not go on the page, and neither does a comparison the
   paper did not make. If a slot has no number, drop the slot.
5. FIGURE GALLERY — every figure, each with its caption, click-to-enlarge into a lightbox that
   closes on Escape, on a click outside, and on a visible close control.
6. LIMITATIONS — what the paper says it does not show. Verbatim in substance; do not soften it.
7. FOOTER — links to the PDF and the repository again, and the citation if the paper carries one.

A sticky section navigation runs alongside all of it and marks where the reader currently is.
</page_structure>

<technical_requirements>
- ONE file. All CSS in a style element, all JavaScript in a script element, both inline in
  `index.html`. No build step, no bundler, no framework, no external script, stylesheet, web
  font or analytics — nothing fetched at load time. The page must render with the network off,
  and the only files it may point at are the figures listed above and the PDF beside it.
- System font stack only, since no font may be downloaded.
- Light theme. Responsive from a 360px phone to a wide desktop, with no horizontal page scroll;
  wide content scrolls inside its own container.
- Honour prefers-reduced-motion: under it, transitions and any scroll-driven effect stop.
- Keyboard-navigable: every control reachable by Tab in a sensible order, a visible focus ring,
  the lightbox trapping focus while open and returning it to the thumbnail on close, and a skip
  link to the main content.
- Semantic HTML: one top-level heading, headings that descend without skipping, landmark elements,
  and alt text on every image that says what the figure shows rather than repeating its number.
- No emoji anywhere. No purple-to-blue gradients. No decorative icon fonts.
- Keep the whole file comfortably under a megabyte.
</technical_requirements>

<writing_register>
Write in the register of the field's best papers (the paper this page presents, which was written to them), not in the register of a language
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

<links>
Use these two URLs VERBATIM wherever the page links to the paper or the code. Do not shorten them,
do not turn either into a relative path, and do not compose one of your own.

- The paper PDF: https://cdn.jsdelivr.net/gh/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency@main/paper.pdf
- The code repository: https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency

Both carry the branch this run publishes to. A link without it opens a DIFFERENT run's work —
it resolves and looks correct, which is why it must be copied rather than derived. They begin
resolving only after this run finishes publishing, so do NOT try to open or verify them.
</links>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-web-tools.
TODO 2. Read `paper.tex` end to end and list `figures/`. Write down the
paper's title, its author line, its contributions, and every headline number together with the
sentence it appears in — those sentences are the only numbers allowed on the page. Note which
figures are PDFs and so need a PNG rendered.
TODO 3. Render a PNG at about 200 DPI, into `figures/`, for every figure not already
in a browser-renderable format, then LOOK at each image you plan to use so you know what it shows
and how large it has to be on the page to stay legible.
TODO 4. Write `index.html` following the page_structure and technical_requirements sections
above: one file, inline CSS and JavaScript, every image referenced through the published figure
prefix.
TODO 5. VERIFY THE NUMBERS: for each number on the page, grep `paper.tex` for it and
confirm it appears there with the same meaning. Delete any number you cannot find. Then confirm
every claim on the page is one the paper actually makes.
TODO 6. VERIFY THE PAGE: confirm `index.html` has no external script, stylesheet or font
reference; that every image path starts with the published figure prefix and names a file that
exists in `figures/`; and that the PDF and repository links are character-for-
character the two URLs given in the links section, not `paper.pdf` and not any URL you
composed. Then open the page in a browser, screenshot it at a phone width and a desktop width,
read both screenshots, and fix anything cramped, overlapping or cut off.
TODO 7. ACCESSIBILITY PASS: tab through the whole page and confirm every control is reachable with a
visible focus ring, the lightbox traps focus and closes on Escape, headings descend without
skipping, and every image has alt text. Fix what fails.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "PaperSiteExpectedFiles": {
      "description": "All expected output files from paper-site generation.",
      "properties": {
        "site_html_path": {
          "description": "Path to the single self-contained HTML page. Example: 'index.html'",
          "title": "Site Html Path",
          "type": "string"
        }
      },
      "required": [
        "site_html_path"
      ],
      "title": "PaperSiteExpectedFiles",
      "type": "object"
    }
  },
  "description": "Paper site \u2014 structured output from presentation-page generation.",
  "properties": {
    "summary": {
      "description": "Brief summary of the page you built: the sections it carries, which figures it shows, which numbers it quotes and where each came from in the paper.",
      "maxLength": 5000,
      "minLength": 300,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/PaperSiteExpectedFiles",
      "description": "All output files you created. Must include index.html."
    }
  },
  "required": [
    "summary",
    "out_expected_files"
  ],
  "title": "PaperSite",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-08 03:15:22 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-09-08 03:17:06 UTC

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

### [4] SYSTEM-USER prompt · 2026-09-08 03:38:03 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: Conversation run failed for id=ed0ec36c-61a8-41d7-b9e6-86d565486273: litellm.Timeout: APITimeoutError - Request timed out. Error_str: Request timed out.

Conversation logs are stored at: /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/.oh_sessions/ed0ec36c61a841d7b9e686d565486273

To help debug this issue, please file a bug report at:
  https://github.com/OpenHands/software-agent-sdk/issues/new
and attach the conversation logs from the directory above.
Last actions before failure:
  - [agent_think]: Both pdftoppm and PyMuPDF are available. Let me render the PNGs for fig2, fig3, fig4, fig5 using pdftoppm at 200 DPI.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/figures && pdftoppm -png -r 200 fig2_v0.pdf fig2_v0 && pdftoppm -png -r 200 fig3_v0.pdf fig3_v0 && pdftoppm -png -r 200 fig4_v0.pdf fig4_v0 && pdftoppm -png -r 200 fig5_v0.pdf fig5_
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "ls: cannot access 'fig*_v0.png': No such file or directory\n-rw-r--r-- 1 root root 1.6M Sep  8 03:15  fig1_v0.jpg"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4
  - [agent_think]: It seems pdftoppm didn't produce output. Let me check the exit code and try with more verbose output.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/figures && pdftoppm -png -r 200 fig2_v0.pdf fig2_v0 2>&1 && ls -lh fig2_v0*",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "-rw-r--r-- 1 root root 55K Sep  8 03:19 fig2_v0-1.png\n-rw-r--r-- 1 root root 14K Sep  8 03:15 fig2_v0.pdf"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemb
  - [agent_think]: The PDFs have page numbers appended. I need to rename them to the expected filenames.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/figures && pdftoppm -png -r 200 fig3_v0.pdf fig3_v0 2>&1 && pdftoppm -png -r 200 fig4_v0.pdf fig4_v0 2>&1 && pdftoppm -png -r 200 fig5_v0.pdf fig5_v0 2>&1 && ls -lh fig*_v0-1.png",

  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "-rw-r--r-- 1 root root 55K Sep  8 03:19 fig2_v0-1.png\n-rw-r--r-- 1 root root 97K Sep  8 03:20 fig3_v0-1.png\n-rw-r--r-- 1 root root 68K Sep  8 03:20 fig4_v0-1.png\n-rw-r--r-- 1 root root 57K Sep  8 03:20 fig5_v0-1.
  - [agent_think]: The pdftoppm output files are named `fig2_v0-1.png` (with a `-1` suffix) because pdftoppm adds a page number suffix. The task requires the files to be named `fig2_v0.png` etc. to match the available_figures list. Let me rename them.

  - [agent_response]: 

The pdftoppm output has `-1` suffix for single-page PDFs. I need to rename these to match the expected filenames.


  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/figures && mv fig2_v0-1.png fig2_v0.png && mv fig3_v0-1.png fig3_v0.png && mv fig4_v0-1.png fig4_v0.png && mv fig5_v0-1.png fig5_v0.png && ls -lh fig*_v0.png fig*_v0.jpg",
  "is_inp
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "-rw-r--r-- 1 root root 1.6M Sep  8 03:15 fig1_v0.jpg\n-rw-r--r-- 1 root root  55K Sep  8 03:19 fig2_v0.png\n-rw-r--r-- 1 root root  97K Sep  8 03:20 fig3_v0.png\n-rw-r--r-- 1 root root  68K Sep  8 03:20 fig4_v0.png\
  - [agent_think]: Now I need to look at the figures to understand what they show and how to size them on the page. Let me check the dimensions of each image.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/figures && python3 -c \"\nfrom PIL import Image\nfor f in ['fig1_v0.jpg', 'fig2_v0.png', 'fig3_v0.png', 'fig4_v0.png', 'fig5_v0.png']:\n    img = Image.open(f)\n    print(f'{f}: {im
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "fig1_v0.jpg: 3168x1344 (2.36 aspect)\nfig2_v0.png: 1416x1066 (1.33 aspect)\nfig3_v0.png: 1400x1400 (1.00 aspect)\nfig4_v0.png: 1400x1400 (1.00 aspect)\nfig5_v0.png: 1400x1050 (1.33 aspect)"}], "is_error": false, "co
  - [agent_think]: Good. All figures are now available in browser-renderable formats. Let me now move to writing the index.html. I have all the information I need:

**Paper details:**
- Title: "Phonological Density Does Not Predict Dependency Distance Minimization: A Cross-Linguistic Test Across 55 Languages"
- Author
  - [agent_tool_call] task_tracker: Tool: task_tracker
{
  "command": "plan",
  "task_list": [
    {
      "title": "Read and STRICTLY follow these skills: aii-web-tools.",
      "notes": "Skill read and understood. Web tools available but not needed for this task since all content comes from paper.tex.",
      "status": "done"
    },
  - [agent_tool_result] task_tracker: Tool: task_tracker
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Read and STRICTLY follow these skills: aii-web-tools.", "notes": "Skill read and understood. Web tool
  - [status_public_warning]: Conversation error [LLMTimeoutError]: litellm.Timeout: APITimeoutError - Request timed out. Error_str: Request timed out.

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<task>
Build the paper's public web page: ONE self-contained `index.html` that lets a reader grasp
this paper faster than opening the PDF would. It is published as this run's GitHub Pages site, so
it is the first thing anyone sees.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<what_is_already_here>
Your workspace is the finished paper folder. It already holds everything the page is made of, and
you must not change any of it — you are adding one file, not revising the paper.

- `paper.tex` — the paper as it was actually written. This is the source of truth for
  every claim, name and NUMBER that goes on the page.
- `paper.pdf` — the compiled paper. The page must NOT link to it by this local name:
  the PDF is published on the code branch and the page on a different one. Link to it at the
  full URL below instead.
- `references.bib` — the bibliography, when the paper has one.
- `figures/` — every figure the paper uses, flattened into one folder.
- `workspace/` — the scratch folder the LaTeX task worked in. Ignore it.
</what_is_already_here>

<paper_text>
title: Phonological Density Does Not Predict Dependency Distance Minimization
abstract: >-
  Dependency distance minimization (DLM) predicts that syntactically related words appear in close linear order. A natural
  extension asks whether phonologically dense languages, with larger phoneme inventories, exhibit stronger DLM to compensate
  for parsing difficulty. We test this across 55 languages from 10 families using Universal Dependencies treebanks, computing
  dependency distances in both word-space and a corrected phoneme-space metric that sums phonemes of intervening words. We
  find no significant relationship: phonological density does not predict DLM strength, and the effect disappears under phylogenetic
  control. A phoneme-space analysis across 37 languages yields a marginally significant effect in the predicted direction,
  but the effect is modest. The null finding is consistent with the directional asymmetry between syntax-driven phonological
  compression and the reverse direction we test: syntactic optimization drives phonological outcomes, not vice versa.
paper_text: |-
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

  We extracted UD treebanks from the `commul/universal_dependencies` repository on HuggingFace \footnote{Code: \url{https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency/tree/main/round-1/experiment-1}}. We selected one configuration per language, preferring treebanks with the largest training splits. This yielded 55 languages across 10 families: Indo-European (20), Uralic (4), Turkic (3), Afroasiatic (4), Sino-Tibetan (4), Austronesian (5), Japonic (1), Koreanic (1), Tai-Kadai (2), and Austroasiatic (2), plus isolates and unclassified entries [ARTIFACT:art_21q7z-GCrosW].

  Phonological features came from PHOIBLE 2.0. We used phoneme inventory size as the primary density metric. Phonological density was normalized to $[0, 1]$ by dividing by the maximum observed inventory (64 phonemes). Mean phonological density across the sample was 0.50 ($\sigma$ = 0.09).

  Word-order typology came from WALS. We classified languages as SVO ($n = 41$), SOV ($n = 11$), or VSO ($n = 3$). All treebanks were written corpora.

  ### 3.2 Dependency Distance Metrics

  Word-space MDD follows standard practice. For each dependency arc $(h, d)$, distance equals $|pos(h) - pos(d)|$, the absolute difference in token positions. Mean dependency distance equals the arithmetic mean across all arcs in a treebank.

  Phoneme-interval distance (PID) extends this to phonological units. For each word $w$, we estimated constituent phonemes using language-family-specific phoneme estimation ratios derived from PHOIBLE data \footnote{Code: \url{https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency/tree/main/round-2/experiment-1}}. PID for arc $(h, d)$ equals:

  $$PID(h, d) = \sum_{w \in \text{intervening}(h, d)} \phi_w$$

  where $\phi_w$ is the phoneme count of word $w$, and $\text{intervening}(h, d)$ is the set of words strictly between positions $pos(h)$ and $pos(d)$. This sums the phonological material in the span between head and dependent, providing a measure of phonological distance that is distinct from word-count distance.

  For non-Latin scripts (CJK, Arabic, Thai), where epitran was unavailable, we used character counts as a lower-bound approximation of phoneme counts. This limitation is discussed in Section 5.3.

  Both metrics were computed per treebank, then aggregated by language. Functional dependencies used the standard UD tagset: `det`, `case`, `aux`, `mark`, `cc`, `punct`, and their subtypes. Lexical dependencies included all remaining relations.

  ### 3.3 Statistical Analysis

  We tested three hypotheses: (H1) phonological density predicts MDD, (H2) word order predicts MDD, (H3) phonological density predicts mean PID. For H1, we fitted both OLS regression and a linear mixed-effects model with language family as a random intercept. For H2, we fitted one-way ANOVA with word order as factor, reporting results both with and without the VSO group. For H3, we fitted OLS regression on the 37-language PID subsample. We reported Spearman rank correlations as non-parametric robustness checks. All analyses used $\alpha = 0.05$.

  We computed family-level variance to assess whether patterns hold within independent lineages. The mixed-effects model addresses the phylogenetic non-independence concern raised by the Indo-European overrepresentation (20/55 languages).

  ### 3.4 Implementation

  Code is available at  and . Processing used Python 3.12 with the `datasets` library for HuggingFace access, `numpy` for numerical operations, `scipy` for statistical tests, and `statsmodels` for mixed-effects modeling. Runtime was approximately 600 seconds across all 55 languages.

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

  Despite the null finding, we introduce two methodological innovations. First, the phoneme-interval distance metric provides a measure that correctly sums phonological material between head and dependent, rather than weighting by the phoneme counts of the connected words. This distinction matters: a dependency between two 10-phoneme words at distance 3 has PID equal to the sum of phonemes in the intervening words, not $3 \times 10$. Second, our standardized pipeline for combining UD treebanks with PHOIBLE data is publicly available  and enables replication and extension.

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

  All code and data are available at , , [ARTIFACT:art_21q7z-GCrosW], and \footnote{Code: \url{https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency/tree/main/round-1/dataset-1}}.
summary: >-
  We test whether phonological density predicts dependency distance minimization across 55 languages. The null finding (r=0.19,
  p=0.17) is consistent with directional asymmetry: syntax drives phonological compression, not vice versa. We introduce the
  phoneme-interval distance metric and demonstrate that word order does not predict MDD.
</paper_text>

<available_figures>
Each line gives the path the PAGE must use, then the figure's title and caption. It is the same
path the file has on disk here: the publish step copies the page and its figures into one folder,
so what works in this workspace is what works on the live site.

- figures/fig1_v0.jpg — "Research Design: Testing the Phonotactic Constraint Hypothesis" (caption: "Overview of the phonotactic constraint hypothesis and our two-metric approach. The hypothesis predicts that phonologically dense languages (large phoneme inventories) should exhibit stronger dependency distance minimization. We test this using word-space MDD (standard) and phoneme-interval distance PID (novel). Arrows show the predicted (dashed, negative) and observed (solid, positive/null) relationships.")
- figures/fig2_v0.png [render from fig2_v0.pdf first] — "Mean Dependency Distance by Word Order Type" (caption: "Mean dependency distance (MDD) across word-order types. SVO languages (n=41) averaged 3.07, SOV languages (n=11) averaged 3.04, and VSO languages (n=3) averaged 3.67. ANOVA: F=1.36, p=0.27. Excluding VSO: F=0.06, p=0.81, η²=0.0005. Word order does not predict MDD.")
- figures/fig3_v0.png [render from fig3_v0.pdf first] — "Phonological Density vs. Word-Space MDD" (caption: "Scatter plot of phonological density (normalized phoneme inventory size) against mean dependency distance. Spearman r=0.19, p=0.17. OLS: R²=0.05, slope=1.48, intercept=2.34. The positive slope runs opposite to the predicted direction. Mixed-effects model (family random intercept): β=0.84, p=0.39.")
- figures/fig4_v0.png [render from fig4_v0.pdf first] — "Phonological Density vs. Phoneme-Interval Distance" (caption: "Scatter plot of phonological density against mean phoneme-interval distance (PID) across 37 languages. Spearman r=-0.32, p=0.051. OLS: R²=0.11, slope=-0.84, intercept=16.29. The negative slope runs in the predicted direction but is modest. Rank correlation between PID and word-space MDD: r=0.52, p<0.001.")
- figures/fig5_v0.png [render from fig5_v0.pdf first] — "Functional vs. Lexical Dependency Distances" (caption: "Comparison of mean dependency distance for functional dependencies (det, case, aux, mark, cc, punct) versus lexical dependencies (nsubj, obj, obl, etc.) across 55 languages. Functional: mean=2.7. Lexical: mean=3.4. The functional-lexical split replicates Gerdes (2026). Difference not significant in this sample (z=-0.90, p=0.37) due to between-language variance.")
</available_figures>

<figure_requirements>
- Reference every figure as `figures/` plus its filename, exactly as listed above.
  The publish step copies the page and its figures into one folder together, so that relative
  path is what resolves on the live site; anything else breaks once published.
- A browser cannot draw a PDF in an image element. Data figures are delivered as vector PDF for
  LaTeX's benefit, so for each one check whether a PNG of the same name already sits in
  `figures/`; if it does not, render one there at about 200 DPI with pdftoppm or
  pymupdf before referencing it. Renderable formats: .avif, .gif, .jpeg, .jpg, .png, .svg, .webp.
- Write those PNGs into `figures/` and nowhere else — that folder is published, a
  new folder of your own is not.
- Use each figure's own caption. Do not invent new ones, and do not describe a figure you did not
  place on the page.
- Look at every figure before you place it. A figure whose axis labels are unreadable at the size
  you give it is worse than no figure.
</figure_requirements>

<page_structure>
In this order, top to bottom:

1. HERO — the paper's title, the author line as the paper gives it, and a one-paragraph TL;DR in
   plain language: what was asked, what was found, and the single number that carries the finding.
   Not the abstract, and not a rewrite of it. Below it, two links: the PDF and the code
   repository, both at the exact URLs given in the links section below.
2. CONTRIBUTIONS — the paper's actual contributions as three to five scannable cards, each a short
   heading plus one or two sentences. If the paper claims four things, show four cards, not five.
3. METHOD — a walkthrough a technically literate non-specialist can follow: what goes in, what
   happens to it, what comes out, and why the design is the way it is. Lead with the paper's own
   method figure when it has one.
4. RESULTS — the paper's real headline numbers, read out of `paper.tex` and the data
   files behind it, each next to what it was measured on and what it is being compared against.
   A number that is not in the paper does not go on the page, and neither does a comparison the
   paper did not make. If a slot has no number, drop the slot.
5. FIGURE GALLERY — every figure, each with its caption, click-to-enlarge into a lightbox that
   closes on Escape, on a click outside, and on a visible close control.
6. LIMITATIONS — what the paper says it does not show. Verbatim in substance; do not soften it.
7. FOOTER — links to the PDF and the repository again, and the citation if the paper carries one.

A sticky section navigation runs alongside all of it and marks where the reader currently is.
</page_structure>

<technical_requirements>
- ONE file. All CSS in a style element, all JavaScript in a script element, both inline in
  `index.html`. No build step, no bundler, no framework, no external script, stylesheet, web
  font or analytics — nothing fetched at load time. The page must render with the network off,
  and the only files it may point at are the figures listed above and the PDF beside it.
- System font stack only, since no font may be downloaded.
- Light theme. Responsive from a 360px phone to a wide desktop, with no horizontal page scroll;
  wide content scrolls inside its own container.
- Honour prefers-reduced-motion: under it, transitions and any scroll-driven effect stop.
- Keyboard-navigable: every control reachable by Tab in a sensible order, a visible focus ring,
  the lightbox trapping focus while open and returning it to the thumbnail on close, and a skip
  link to the main content.
- Semantic HTML: one top-level heading, headings that descend without skipping, landmark elements,
  and alt text on every image that says what the figure shows rather than repeating its number.
- No emoji anywhere. No purple-to-blue gradients. No decorative icon fonts.
- Keep the whole file comfortably under a megabyte.
</technical_requirements>

<writing_register>
Write in the register of the field's best papers (the paper this page presents, which was written to them), not in the register of a language
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

<links>
Use these two URLs VERBATIM wherever the page links to the paper or the code. Do not shorten them,
do not turn either into a relative path, and do not compose one of your own.

- The paper PDF: https://cdn.jsdelivr.net/gh/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency@main/paper.pdf
- The code repository: https://github.com/ai-inventor-papers/ai-invention-45370e-phonotactic-constraint-on-dependency

Both carry the branch this run publishes to. A link without it opens a DIFFERENT run's work —
it resolves and looks correct, which is why it must be copied rather than derived. They begin
resolving only after this run finishes publishing, so do NOT try to open or verify them.
</links>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-web-tools.
TODO 2. Read `paper.tex` end to end and list `figures/`. Write down the
paper's title, its author line, its contributions, and every headline number together with the
sentence it appears in — those sentences are the only numbers allowed on the page. Note which
figures are PDFs and so need a PNG rendered.
TODO 3. Render a PNG at about 200 DPI, into `figures/`, for every figure not already
in a browser-renderable format, then LOOK at each image you plan to use so you know what it shows
and how large it has to be on the page to stay legible.
TODO 4. Write `index.html` following the page_structure and technical_requirements sections
above: one file, inline CSS and JavaScript, every image referenced through the published figure
prefix.
TODO 5. VERIFY THE NUMBERS: for each number on the page, grep `paper.tex` for it and
confirm it appears there with the same meaning. Delete any number you cannot find. Then confirm
every claim on the page is one the paper actually makes.
TODO 6. VERIFY THE PAGE: confirm `index.html` has no external script, stylesheet or font
reference; that every image path starts with the published figure prefix and names a file that
exists in `figures/`; and that the PDF and repository links are character-for-
character the two URLs given in the links section, not `paper.pdf` and not any URL you
composed. Then open the page in a browser, screenshot it at a phone width and a desktop width,
read both screenshots, and fix anything cramped, overlapping or cut off.
TODO 7. ACCESSIBILITY PASS: tab through the whole page and confirm every control is reachable with a
visible focus ring, the lightbox traps focus and closes on Escape, headings descend without
skipping, and every image has alt text. Fix what fails.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "PaperSiteExpectedFiles": {
      "description": "All expected output files from paper-site generation.",
      "properties": {
        "site_html_path": {
          "description": "Path to the single self-contained HTML page. Example: 'index.html'",
          "title": "Site Html Path",
          "type": "string"
        }
      },
      "required": [
        "site_html_path"
      ],
      "title": "PaperSiteExpectedFiles",
      "type": "object"
    }
  },
  "description": "Paper site \u2014 structured output from presentation-page generation.",
  "properties": {
    "summary": {
      "description": "Brief summary of the page you built: the sections it carries, which figures it shows, which numbers it quotes and where each came from in the paper.",
      "maxLength": 5000,
      "minLength": 300,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/PaperSiteExpectedFiles",
      "description": "All output files you created. Must include index.html."
    }
  },
  "required": [
    "summary",
    "out_expected_files"
  ],
  "title": "PaperSite",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_nBwvdB3PKEF8/4_gen_paper_repo/_4_assemble_paper/paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [5] HUMAN-USER prompt · 2026-09-08 03:38:03 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [6] SYSTEM-USER prompt · 2026-09-08 03:43:31 UTC

```
SITE VERIFICATION FAILED: 1 problem(s) in index.html.

- image source '' does not start with 'figures/', so it will not resolve once the page is published beside its figures folder

You MUST:
1. Fix every problem listed above in index.html.
2. Keep the page ONE self-contained file — all CSS and JavaScript inline, no external scripts, stylesheets or web fonts, nothing fetched at load time.
3. Point every image at figures/<filename>, where <filename> is a browser-renderable image that really exists in your figures/ folder. A vector PDF figure needs a PNG rendered beside it first; reference the PNG.
4. Re-open the page and confirm it still renders before finishing.
```
