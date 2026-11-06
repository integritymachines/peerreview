# MDCI Evidentiary Pilot v2 — Causal Framework Selection

6 November 2026. Completed in ChatGPT Work with frozen inputs and independent contexts.

**Result:** the R/F/D-guided branch added no atomic-framework-set discrimination beyond the domain-and-estimand baseline in this run. Its 12 candidate sets were identical to the baseline's. This is a descriptive finding about the frozen prompted implementation, not a calibrated rejection of MDCI or evidence that framework mismatches are common. Framework non-uniqueness is legitimate.

The previous pilot operationalized frameworks as designs and was a workflow failure. This run uses actual framework categories, separate design fields, equal-information blind assessment, a narrower baseline, complete-paper extraction, and measurement repeats. It addresses the revised question; no mismatch discovery is required for success.

## Comparative table

PO = Rubin/Neyman potential outcomes; SCM = Pearl structural causal models; SE = Heckman/Haavelmo structural econometrics; MD = mechanistic dynamical models. A/B entries are **equally admissible candidate components**, not strict winners. Explicit hybrid combinations are analyzed separately. C means apparatus actually operationalized, not an author's philosophical affiliation. Indeterminate means membership is underidentified, not that the paper lacks causal aims.

| Paper | R/F/D | MDCI A | Blind B | Actually used C | Agreement |
|---|---|---|---|---|---|
| LaLonde (1986) | 0.25/0.75/0.00 | PO, SCM, SE | PO, SCM, SE | SE | Same component sets; used framework admissible |
| Angrist–Krueger (1991) | 0.25/0.50/0.00 | PO, SCM, SE | PO, SCM, SE | Indeterminate | Same component sets; C indeterminate |
| Card–Krueger (1994) | 0.25/0.50/0.00 | PO, SCM, SE | PO, SCM, SE | Indeterminate | Same component sets; C indeterminate |
| Rust (1987) | 0.25/0.50/0.25 | PO, SCM, SE | PO, SCM, SE | SE | Same component sets; used framework admissible |
| Berry–Levinsohn–Pakes (1995) | 0.25/0.50/0.00 | PO, SCM, SE | PO, SCM, SE | SE | Same component sets; used framework admissible |
| Chetty (2008) | 0.25/0.50/0.00 | PO, SCM, SE | PO, SCM, SE | SE | Same component sets; used framework admissible |
| Hernán–Brumback–Robins (2000) | 0.25/0.50/0.50 | PO, SCM, MD | PO, SCM | PO | Partial component sets; used framework admissible |
| Sachs et al. (2005) | 0.50/0.50/0.00 | PO, SCM, MD | PO, SCM, MD | SCM | Same component sets; used framework admissible |
| Voight et al. (2012) | 0.25/0.50/0.25 | PO, SCM, MD | PO, SCM | Indeterminate | Partial component sets; C indeterminate |
| Dell–Jones–Olken (2012) | 0.25/0.25/0.25 | PO, SCM, SE | PO, SCM, SE | Indeterminate | Same component sets; C indeterminate |
| Flaxman et al. (2020) | 0.25/0.50/0.50 | PO, SCM, MD | PO, SCM, MD | MD | Same component sets; used framework admissible |
| Miguel–Kremer (2004) | 0.25/0.75/0.50 | PO, SCM, MD | PO, SCM | SE | Partial component sets; unresolved coverage gap |

## Agreement, baseline and non-uniqueness

| Endpoint | MDCI A versus blind B | Domain/estimand baseline versus B |
|---|---:|---:|
| Exact candidate-component sets | 9/12 | 9/12 |
| Mean Jaccard overlap | 0.917 | 0.917 |
| Nonempty component intersection | 12/12 | 12/12 |
| Mean candidate-set size | 3.00 versus B's 2.75 | 3.00 versus B's 2.75 |
| Strict framework preferences | 0/12 | 0/12 |
| Full structural recommendation equality, including hybrid listings | 2/12 | 2/12 |

A and baseline have identical candidate-component sets in all 12 cases; their mean paired Jaccard difference against B is **0.000**. Both list PO and SCM everywhere, adding SE for seven economic targets and MD for five biological/health targets. Seven distinct measured signatures therefore produce only two candidate-set patterns already recovered by domain/estimand alone.

The 12/12 preferred-set agreement is vacuous as discrimination: every preferred set is empty and all assessments explicitly retain equally admissible alternatives. This does not make non-uniqueness a diagnostic failure. It means the run supplies no strict framework ranking or demonstrated material advantage.

Hybrid listings require separate care. A proposes no explicit hybrids, B proposes them in ten cases, and baseline proposes PO+SCM in all twelve. Candidate-component equality is consequently not complete recommendation equality. The hybrid-aware equality statistic is a secondary descriptive audit of that distinction, not a replacement for the frozen primary metrics. Failure to list a hybrid does not establish that an assessor rejects its compatibility. No C extraction establishes an integrated hybrid in these papers; compatibility under another formalism was not counted as actual hybrid use.

B excludes an uncalibrated MD option for the HIV, HDL and deworming cases; A and baseline retain it conditionally. These disagreements concern how much unsupported mechanistic detail can be allowed in a candidate, not evidence that MD is a superior identifying framework. Assumptions, data and policy targets matter within frameworks as well as between them.

## Actual apparatus and possible mismatch

C identifies three explicit and five apparatus-supported memberships; four remain underidentified: schooling, minimum wages, HDL/infarction and temperature/growth. These papers contain substantive identification arguments, but their apparatus does not uniquely establish one of the stipulated framework memberships. The extraction does not assign PO from an IV/DiD label or SE from any regression. A historical or generic counterfactual comparison may be translatable into a modern school without demonstrating that the paper operationalized that school.

Among the eight classified papers, A and B both include the extracted component in **7/8** candidate sets. This is coverage, not causal accuracy or a fit verdict. The deworming paper is the unresolved gap: C finds a behavioral take-up/selection threshold supporting its within-school decomposition, whereas A/B recommend PO/SCM (A also permits MD). C's recognition applies to that formal selection subproblem, not an assertion that every program-effect regression belongs exclusively to structural econometrics. The relationship between the dossier's package/spillover targets and the paper's selection-bound subproblem needs finer estimand alignment.

**No material framework mismatch is demonstrated.** Neither blind assessment establishes a superior same-evidence framework, and a missing candidate is not proof that the actually used apparatus is unsuitable. The deworming gap is neither silently counted as a match nor promoted into a mismatch. Four unknown memberships and overlapping representational capacities further prevent a reliable mismatch-frequency estimate. Changes in estimator or design are never treated as framework mismatches.

## Signature repeatability

Three preselected cases received one fresh-context repeat, without seeing the original scores or recommendations.

| Case | First R/F/D | Repeat R/F/D | Candidate-set result |
|---|---|---|---|
| Schooling | .25/.50/.00 | .25/.50/.00 | Same |
| Automobile market | .25/.50/.00 | .25/.25/.00 | Same |
| Protein signaling | .50/.50/.00 | .25/.50/.00 | MD option omitted on repeat |

Exact score-vector agreement is **1/3**; candidate sets agree exactly in **2/3**. Mean absolute difference across the nine coordinates is **0.056**, maximum **0.25**. Per-coordinate mean absolute differences are R=.083, F=.083, D=.000. The D comparison involves three zero scores, so it does not validate measurement of strong physical-direction evidence. Preferred-set stability is trivial because all remain empty. These are small within-host repeatability checks, not independent-human reliability or calibration estimates.

## Unresolved measurement and selection problems

1. **No validated mapping:** the repository supplies no independently calibrated signature-to-framework rule. The frozen A prompt operationalizes the signature as an aid to representing warranted restrictions; it explicitly avoids inventing R-to-PO/F-to-SE/D-to-MD exclusivity. This experiment tests that prompted reasoning aid, not an autonomous numerical classifier or a fully specified original-theory prediction.
2. **Measurement units remain provisional:** the quarter-step warrant scale is a declared convention. R measures documented undirected-dependency evidence, not opacity, confounding severity, or an edge fraction. D excludes mere chronology and accounting identities. Many dossiers list candidate dependencies while omitting study findings; this limits empirically established R warrants and helps explain repeated low R scores. The repeat differences show that the rubric is not yet uniquely reproducible.
3. **Overlapping frameworks:** PO and SCM can express many common targets/restrictions; SE and MD introduce mechanism-specific assumptions rather than automatically stronger identification. A material advantage must be tied to the precise query and warranted model invariances. Broad school membership alone is too coarse to evaluate every useful difference in causal representation.
4. **No observed incremental discrimination:** A exactly reproduces baseline candidate sets and does not outperform it against B on the primary endpoints. B is also a same-information/no-signature assessment. Richer inputs alone cannot be credited to the classification; the current outcomes establish no independent gain from R/F/D. They also do not prove that directional knowledge lacks value for specifying assumptions within a framework.
5. **Scope and reference limits:** B is an LLM comparator, not causal ground truth. C membership is interpretive. All workers share a model lineage, papers are famous, case batches can share contextual habits, dossiers are retrospective, and the sample is purposive. No significance, population accuracy, or general mismatch-prevalence claim is justified.

The useful conclusion is narrower than a theory verdict: **under this operationalization, the directional scores did not discriminate framework sets beyond domain and estimand, while their detailed directional caveats remained assumption descriptions rather than demonstrated framework advantages.**

## Sources, execution and audit

Twelve final published empirical applications span opaque social responses, negotiable institutional/behavioral mechanisms, physical interventions and biological constraints, and combinations. All exceed 300 indexed citations to the final article: ten counts use Crossref; LaLonde and Card–Krueger use CitEc/EconPapers because exact Crossref records were unavailable. Counts are source-specific snapshots, not a ranking. [SOURCES_v2.md](v2/SOURCES_v2.md), [selection.json](v2/selection.json) and preparation records document versions and provenance.

Three access/scope replacements occurred before assessment: an illustrative MSM paper became the empirical HIV application; a hypothetical influenza simulation became observed COVID-19 inference; inaccessible Keane–Wolpin became the final Chetty unemployment-insurance paper. No replacement used a fit or mismatch outcome. Main articles are complete. Missing separate q08/q09 supplements and q06 erratum text are disclosed; q11 includes the full published supplement.

A/B/baseline/repeats generated **39 sealed outputs before any C worker launched**. C then generated twelve more. Twelve fresh assessment-agent contexts produced 51 case assessments, without substantive retries or output revisions; case batching reduced overhead. Agent contexts were separate but file access was instruction-governed, not sandboxed per branch. Exact model identifier, host token counts and charges are unavailable; no free-execution or dollar-cost claim is made. No external OpenAI API calls were used.

All raw inputs/outputs remain frozen privately; grouped substantive outputs, request/source hashes, phase seals and deviations form the distributable audit. There are 37 located formal-evidence descriptions. Five of six nonempty C quotes match normalized extraction; the sixth is visually verified on the original HIV page, where two-column extraction had interleaved unrelated text. That page also confirms the regime-indexed death-time definition and hazard model. All 61 common dossier-evidence excerpts match their source dossiers. These are provenance checks, not independent replication of every mathematical inference.

Full copyrighted papers, source PDFs and credentials are excluded from git. The original review.txt is unchanged. The runnable prepare/seal/collect/compare workflow, framework schema and four lightweight prompts are under mdci/. Nine new v2 tests and three original runner tests pass.

## Recommendations

Keep non-unique recommendations as valid outcomes. Before a stronger predictive claim, specify an MDCI-to-framework decision rule independently of these results, clarify whether the goal is practical representation or materially improved identification/extrapolation, and define reproducible warrant units at the edge/estimand level. Obtain independent adjudication of framework membership and material advantages, including the deworming subproblem. A future comparison should retain both the equal-information B control and the narrow baseline, repeat cases with nonzero D, and evaluate held-out problems. Do not derive a mapping from these twelve cases and present its fit on them as validation.
