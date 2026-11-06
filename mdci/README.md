# MDCI framework-fit pilot (lightweight)

This module is separate from the full PBPR workflow in ../review.txt. It leaves that workflow intact. A **single reviewer call per paper**, blinded to MDCI, extracts the framework used and judges whether it fits the available evidence; a **separate signature call**, blinded to the published method and review, predicts candidate frameworks from ex-ante system knowledge. Both can agree that the original method was suitable: published mismatch is a hypothesis to measure, not a premise.

## Inputs

Create a private JSONL manifest with one paper per line:

    {"paper_id":"p001","paper":"papers/p001.txt","dossier":"dossiers/p001.txt"}

Paths are relative to the manifest. Use opaque paper IDs. The paper file must contain enough original methodological content for an adequate review. The dossier must be prepared using only prior system knowledge, design, physical/logical priors, and the target estimand; it **must not identify the author's chosen framework or study conclusions**. Do not commit copyrighted full papers or private API credentials. Sources are passed to the OpenAI API if paid execution is explicitly enabled.

## Execute locally

    python -m unittest discover -s mdci -p 'test_*.py' -v
    export OPENAI_API_KEY=...  # use a secret, not a committed value
    python mdci/run.py run --manifest manifest.jsonl --limit 2 --execute --output results.jsonl
    python mdci/run.py compare --results results.jsonl --output comparison.json

Model defaults to gpt-4.1-mini, change with --model. Budget controls: 2 independent API requests per paper, hard --limit <= 5, explicit --execute flag, and 25,000-character source limit per branch (no silent truncation). No paid API calls run on push or on a schedule. If a request fails, results already written remain available. A manual GitHub Actions invocation runs only offline tests, because paper text and API secrets have not been installed on the runner.

## What a verdict means

Review fit is appropriate | mismatch | indeterminate. Mismatch is warranted only when the used method is demonstrably unsuitable OR a materially better feasible alternative uses the *same data and credible assumptions*. The comparator reports review frequencies, recommendations and disagreement, never causal truth. The R/F/D numbers are **uncalibrated evidence scores**, not Bayesian posterior probabilities; eight-class calibration and a design+estimand baseline belong to a later experiment.

## Limits

LLMs cannot be completely blinded to famous studies already in training, and a single-pass review is not a replication or independent ground truth. Require exact paper passages; keep ambiguity as indeterminate. Sample both apparent matches and nonmatches; do not cherry-pick cases of criticism. The experiment needs full-text rights and an operator-supplied API key for actual review runs.
