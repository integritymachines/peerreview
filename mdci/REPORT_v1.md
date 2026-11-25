# MDCI evidentiary pilot: completed with isolated agents

2026-11-06. **Four reviews judged the framework conditionally appropriate, one was indeterminate, and none established a mismatch.** MDCI's candidate sets overlap the reviewers' recommendations in all five cases, but none matches exactly. This demonstrates broad compatibility on these cases, not incremental predictive validity.

## Execution change

Ten fresh-context work-session agents performed one signature assessment and one blind review per paper. No agent inherited the parent conversation or was reused. Reviewers received only the unchanged review prompt and their original methods extract; signature agents received only the unchanged signature prompt and dossier. Workers were instructed to read only their request, use no browsing and perform no delegation. All ten responses were frozen before the parent examined their substantive outputs. No assessment was revised or rerun.

Original paper selection, extracts, dossiers and prompts match their previously frozen hashes. The amendment records the change of host, ordering and output limits. Context separation was procedural: workers shared a filesystem. Shared model knowledge and operator preparation can still create correlated errors.

[Draft pull request #1](https://github.com/integritymachines/peerreview/pull/1) adds request preparation and validated collection while retaining the API option. All nine offline tests pass. The existing API runner, both prompts and the original peer-review workflow are unchanged. Only three software/documentation files change in the PR; papers and results are not committed.

## Comparative results

DiD = difference in differences; Adj = adjustment; IV = instrumental variables; RD = regression discontinuity; SC = synthetic control; Rand = randomized design; Sel = structural selection; PI = partial identification; G = graphical analysis. Recommendations are sets, not ranked probabilities.

| Paper | Actually used, extracted by blind review | Peer-review preferred | MDCI-predicted candidates | Review fit | Disagreement |
|---|---|---|---|---|---|
| Card & Krueger (1994), minimum wages | DiD, Adj | DiD, Adj | DiD, Adj, G, PI | Appropriate | MDCI adds G and PI. |
| Angrist & Krueger (1991), schooling | IV | IV | IV, G, PI | Appropriate | MDCI adds G and PI. |
| Lee (2008), incumbency; available 2005 precursor | RD | RD | RD, G, PI | Appropriate | MDCI adds G and PI. |
| Abadie, Diamond & Hainmueller (2010), tobacco policy | SC | SC | SC, DiD, G, PI | Appropriate | MDCI also permits DiD conditionally and adds G and PI. |
| Miguel & Kremer (2004), deworming | Rand, Sel, PI | Rand, Sel, PI | Rand, G, PI | Indeterminate | MDCI omits Sel and adds G; both branches flag unresolved allocation and spillovers. |

No reviewer identified a materially better feasible alternative using the same data and credible assumptions. Appropriate means defensible conditionally, not proven causally correct. The deworming preferred list is conditional and does not override its indeterminate verdict.

The sample was selected for five distinct primary strategies, without screening for mismatch. All meet a 300-citation threshold in Crossref for a journal or linked working-paper version. It is a purposive sample, not a literature ranking. Lee's input is a 2005 precursor: implementation details are not verified against the final 2008 text. Angrist–Krueger required OCR. SOURCES.md records versions, citation snapshots and page selections.

## Interpretation by paper

- **Minimum wages:** both branches support comparative changes conditionally. The reviewer flags anticipation, regional shocks, spillovers, survey reporting and limited state-level replication. These are identification risks, not demonstrated framework mismatch.
- **Schooling:** both support IV conditionally. Birth-quarter relevance is distinct from independence/exclusion. Positive-earnings selection and heterogeneous schooling returns limit interpretation. Estimator robustness checks need not change the method family.
- **Incumbency:** both support RD for a local party-victory effect. Reported balance checks do not establish continuity of unobserved determinants. The reviewer flags quartic approximation and suggests same-family sensitivity checks without asserting a superior framework.
- **Tobacco policy:** the review prefers SC; MDCI also lists DiD conditionally. The review uses reported pre-policy divergence from the national comparison, deliberately excluded from the ex-ante dossier. Some disagreement reflects unequal information. Unmatched shocks, spillovers, sales measurement and placebo calibration remain concerns.
- **Deworming:** both distinguish assignment, receipt and spillovers. The reviewer cannot certify the stratified alphabetical every-third-school allocation, reduced analytic sample or spatial restrictions from the extract. It recognizes an additional selection-based decomposition. Missing documentation supports indeterminate, not a finding that the original procedures failed.

## Agreement and discrimination

| Measure | Value | Interpretation |
|---|---:|---|
| Appropriate / mismatch / indeterminate | 4 / 0 / 1 | No established mismatch; one unresolved case. |
| Nonempty MDCI–review recommendation intersection | 5/5 | Broad compatibility, including the unresolved case. |
| Exact recommendation-set agreement | 0/5 | No complete set match. |
| Mean Jaccard overlap | 0.383 | Intersection divided by union, averaged across papers. |
| Mean MDCI / reviewer set size | 3.4 / 1.6 | MDCI recommends substantially broader sets. |
| All reviewer-used families included in MDCI set | 4/5 | Deworming's selection component is omitted. |
| Stock comparator binary agreement | 4/4 = 100% | Indeterminate excluded; no mismatch case tests discrimination. |

An always-no-mismatch rule attains the same binary score on the four determinate reviews. Thus 100% agreement adds no evidence of mismatch detection here. Sensitivity to actual mismatch is unestimable. Candidate inclusion is not certification of an identifying design or causal truth.

Every MDCI output includes G and PI, which can organize assumptions and sensitivity without replacing a primary identifying design. Their routine inclusion broadens the sets and makes intersection agreement easier. No post-hoc removal or relabeling was used to improve these metrics.

## Predictive value

**Incremental predictive value of R/F/D remains unmeasured.** The experiment demonstrates feasibility and recognition of compatible method families. Institutional rules, election thresholds, policy timing, donor histories and rollout procedures already supply strong design cues. No locked design-plus-estimand model baseline was executed.

R/F/D scores, in paper order, are (0.60, 0.50, 0.20), (0.80, 0.75, 0.50), (0.95, 0.95, 0.65), (0.90, 0.45, 0.00), and (0.95, 0.80, 0.75). They are uncalibrated evidence scores, not probabilities. There is no fixed numerical rubric or independently validated signature-to-method mapping. Several agents credit temporal irreversibility under D, while the tobacco assessment gives D=0 despite supplied chronology. This is a measurement-consistency question for calibration.

The LLM review is not causal ground truth. Five famous studies, a shared host-model lineage, retrospective dossiers, selected passages and unequal branch information limit interpretation. Neither this sample nor its absence of established mismatch estimates literature-wide prevalence.

A stronger follow-up would freeze a scoring/mapping rule and a design-plus-estimand baseline, use more and less recognizable held-out studies, and obtain independent methodological adjudication. These five outputs should not both train and validate that rule.

## Audit and usage

All 39 reviewer evidence excerpts occur on their claimed PDF pages after appropriate normalization: 17 match byte-for-byte, 38 after whitespace normalization, and all 39 after also joining OCR line-end hyphenation. This verifies provenance, not correctness of inference. Original responses remain unmodified and were hashed before collection.

The distributed results retain assessment content and evidence locations while replacing verbatim source excerpts with digests and audit flags. Unmodified private response envelopes and source extracts remain in the execution workspace. The package excludes copyrighted full PDFs and methods extracts; prepare_inputs.py supports reconstruction and hash checks.

Ten fresh-context assessments completed without retries or external OpenAI API calls. Host token counts, exact model identifier and monetary charges are not exposed by receipts; no dollar-cost or free-execution claim is made. The former gpt-4.1-mini/1,400-token API configuration does not describe this run. CONTINUE.md explains reproduction. The original failed API attempt is retained separately as historical status.
