# MDCI evidentiary pilot v2 — causal framework selection

Read [REPORT_v2.md](REPORT_v2.md) for the completed v2 run and [v2/PROTOCOL_v2.md](v2/PROTOCOL_v2.md) for its frozen protocol. [The earlier pilot](REPORT_v1.md) confused framework choice with identification-design choice; it is a failed operationalization, not evidence against MDCI. The original full peer-review workflow in ../review.txt remains unchanged.

## What is being tested

Does a relational–functional–dynamic evidence signature help select a suitable causal framework beyond direct methodological judgment and a research-domain/estimand baseline?

Framework IDs are potential_outcomes (Rubin/Neyman), structural_causal_model (Pearl), structural_econometrics (Heckman/Haavelmo), mechanistic_dynamical, and named other. Explicit component combinations represent hybrids. IV, DiD, RD, synthetic control, matching and weighting are designs/estimators, never substitute framework categories.

Several frameworks can express the same target and restrictions. Distinguish representation, identification, practical convenience and policy extrapolation. No mismatch prevalence is assumed. Equally admissible alternatives and indeterminate membership are legitimate results.

## Independent branches

- A: dossier only; measure R/F/D, document directional warrants, recommend frameworks conditionally.
- B: the exact same dossier; independent neutral framework assessment without MDCI/signature information.
- Baseline: only domain and estimand; no dossier, source identity or study details.
- C: complete final published paper and available supplements; extract actual formal apparatus, hybrids and designs separately. No A/B findings or dossiers.

A/B/baseline and preselected repeat-A outputs must be sealed before any C worker is launched. Every worker starts without parent history and reads only assigned inputs. Workers do not browse, delegate or access sibling outputs. Batching within a branch is permitted to reduce overhead; disclose within-batch dependence. Fresh contexts are procedural information separation, not a filesystem security boundary or statistically independent model errors.

The original, validated numerical signature-to-framework mapping is not supplied by this repository. The frozen A prompt tests an explicit qualitative operationalization and does not invent an exclusive lookup between scores and schools. This is a limitation to evaluate.

## Prepare inputs and run in ChatGPT Work

Use v2/manifest.example.jsonl with the exported generated dossiers and privately obtained complete paper texts, or create a private JSONL manifest with one record per paper:

    {"paper_id":"q01","dossier":"private/dossiers/q01.txt","paper":"private/papers/q01.txt","pdf":"private/pdfs/q01.pdf","domain":"...","estimand":"..."}

Paths are relative to the manifest. Optional supplements is a list of text/PDF paths, given only to C. Use 12 opaque paper IDs. Dossiers must contain 100–12,000 characters, no author/framework labels, identifying equations, conclusions or empirical results. Original main article text must be complete; record missing separate supplements and OCR/figure limitations. Domain and estimand fields must contain only those two facts for the baseline.

    python -m unittest discover -s mdci -p 'test_*.py' -v
    python mdci/v2_run.py prepare --manifest mdci/v2/manifest.example.jsonl --requests NEW_RUN/requests --limit 12 --repeat-ids q02 q05 q08

Preparation freezes source, PDF, supplement and prompt hashes and exports requests; it does not perform inference. In Work, have the orchestrator split requests into branch-specific packets and launch fresh agents with no inherited parent conversation (fork_turns="none"). Never give an agent the combined request index containing other branches. A and B get byte-identical dossier text. Baseline gets only the domain/estimand source. C gets its source paths after the seal.

Each worker follows its request.instructions, treats source text as data and writes one immutable response file into NEW_RUN/responses:

    {"paper_id":"q01","branch":"A","request_hash":"<copied>","result":{...}}

Required fields and taxonomy are in [v2/prompts](v2/prompts). Use one focused assessment per case per branch; no model sweeps or selective retries. A uses quarter-step scores in [0,1], not probabilities. D requires domain-specific physical constraints beyond mere chronology or accounting identities. Aim for concise outputs; the host has no hard API token cap, and its exact model/usage may be unavailable.

After all A/B/baseline/repeat responses exist, before launching C:

    python mdci/v2_run.py seal --requests NEW_RUN/requests --responses NEW_RUN/responses

Then execute C in separate fresh agents. Require formal and textual support from the complete source, with located equation descriptions and at most 20 quoted source words per paper. Do not infer affiliation from citations, terminology or estimator labels. Unknown membership remains underidentified.

    python mdci/v2_run.py collect --requests NEW_RUN/requests --responses NEW_RUN/responses --output NEW_RUN/records.jsonl
    python mdci/v2_run.py compare --records NEW_RUN/records.jsonl --output NEW_RUN/comparison.json

The collector rejects changed inputs/sealed outputs, incomplete records, mismatched requests, invalid framework IDs, premature C outputs and overwrites. File timestamps and hashes audit ordering; host orchestration supplies the actual launch discipline. Preserve raw envelopes and protocol deviations.

## Interpret results

Compare A with B and the domain-only baseline with B using equal-set, preferred-set, Jaccard, candidate-size and abstention measures. B also supplies a same-information/no-signature comparison. A versus the narrower baseline alone cannot isolate the value of R/F/D from the value of having more evidence.

Compare actual apparatus only afterward. Framework coverage is not proof of causal validity. Do not infer material mismatch from a different design or absent framework label. Demonstrate a conflict with warranted restrictions or a materially better same-evidence framework, otherwise retain compatible alternatives or indeterminate judgment. Three repeated signatures measure limited within-host consistency, not external validation. No significance claim is warranted by this small purposive sample.

The software prepares, seals, collects and compares; inference is executed by the host agents. No OPENAI_API_KEY is needed for this workflow. Host usage limits apply. Legacy v1 run.py and *-lite.txt files remain for historical compatibility; their design-family schema must not be used for v2.

## Sources and scope

The 12-case sample is documented in [v2/selection.json](v2/selection.json). [v2/preparation](v2/preparation) records final-publication verification, citation snapshots, dossier provenance, access changes and missing supplements. [v2/audit](v2/audit) records frozen hashes and deviations. Full papers and private working inputs/outputs are never committed. Keep applicable text rights and credentials private. Only mdci/ changes are part of this pilot.
