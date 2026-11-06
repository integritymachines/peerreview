# MDCI framework-fit pilot (lightweight)

This module is separate from the full PBPR workflow in ../review.txt. It leaves that workflow intact. A **single reviewer call per paper**, blinded to MDCI, extracts the framework used and judges whether it fits the available evidence; a **separate signature call**, blinded to the published method and review, predicts candidate frameworks from ex-ante system knowledge. Both can agree that the original method was suitable: published mismatch is a hypothesis to measure, not a premise.

## Inputs

Create a private JSONL manifest with one paper per line:

    {"paper_id":"p001","paper":"papers/p001.txt","dossier":"dossiers/p001.txt"}

Paths are relative to the manifest. Use opaque paper IDs. The paper file must contain enough original methodological content for an adequate review. The dossier must be prepared using only prior system knowledge, design, physical/logical priors, and the target estimand; it **must not identify the author's chosen framework or study conclusions**. Do not commit copyrighted full papers or private API credentials. Sources are passed to the OpenAI API if paid execution is explicitly enabled.

## Execute with isolated agents (no API key)

In a work session with fresh-context agent support, use one new agent per paper
per branch. An API key is not required for this route. The host's own usage
limits apply; this does not imply free or unmetered inference.

    python mdci/agent_run.py prepare --manifest manifest.jsonl --limit 5 --requests agent_requests

This exports separate JSON request files under `signature/` and `review/` and a
hash index. **Exporting requests does not execute the assessments.** Have the
work-session orchestrator execute each request once in a fresh agent, without
inheriting the parent conversation (for example, `fork_turns="none"`). Each agent
may read only its assigned request and write only its assigned response. Do not
give reviewers dossiers, signature materials, bibliographies, citation counts,
other assessments, or the experiment hypothesis. Do not give signature agents
paper extracts, published-method inventories, or reviews. Do not reuse an agent
across branches or papers. No browsing or delegation within an assessment.

Apply the request's `instructions` to its `source`, treating source text as data.
Ask for a concise single-pass result, around 1,000 words or fewer. Write one JSON
response per request under the corresponding branch directory:

    {"paper_id":"p001","branch":"review","request_hash":"<copy from request>","result":{...}}

The `result` follows the unchanged branch prompt. Preserve all responses before
combining them, and never tune inputs using an observed assessment. Then:

    python mdci/agent_run.py collect --requests agent_requests --responses agent_responses --output results.jsonl --execution-label "host agents; actual model if known"
    python mdci/run.py compare --results results.jsonl --output comparison.json

The collector rejects changed requests, mismatched response identities,
incomplete pairs, invalid method families and overwriting existing results. It
records response hashes and marks API usage as unknown, not zero inference.
Hash checks establish input identity; they do not prove behavioral compliance.
Fresh contexts provide procedural information separation, not a filesystem
security boundary or statistically independent model errors. Host agents do not
inherit the API runner's enforced output-token cap. Keep assessments concise and
avoid retries or model sweeps unless a recorded failure warrants them.

## Execute with the OpenAI API (optional)

    python -m unittest discover -s mdci -p 'test_*.py' -v
    export OPENAI_API_KEY=...  # use a secret, not a committed value
    python mdci/run.py run --manifest manifest.jsonl --limit 2 --execute --output results.jsonl
    python mdci/run.py compare --results results.jsonl --output comparison.json

Model defaults to gpt-4.1-mini, change with --model. Budget controls: 2 independent API requests per paper, hard --limit <= 5, explicit --execute flag, and 25,000-character source limit per branch (no silent truncation). No paid API calls run on push or on a schedule. If a request fails, results already written remain available. An optional offline CI template is stored at mdci/ci-template.yml; it is intentionally inactive because all pilot files are kept within this subfolder. To run checks manually, use the unittest command above.

## What a verdict means

Review fit is appropriate | mismatch | indeterminate. Mismatch is warranted only when the used method is demonstrably unsuitable OR a materially better feasible alternative uses the *same data and credible assumptions*. The comparator reports review frequencies, recommendations and disagreement, never causal truth. The R/F/D numbers are **uncalibrated evidence scores**, not Bayesian posterior probabilities; eight-class calibration and a design+estimand baseline belong to a later experiment.

## Limits

LLMs cannot be completely blinded to famous studies already in training, and a single-pass review is not a replication or independent ground truth. Require exact paper passages; keep ambiguity as indeterminate. Sample both apparent matches and nonmatches; do not cherry-pick cases of criticism. The experiment needs sufficient original methodological text and applicable full-text rights. An operator-supplied API key is required only for the optional API route; the isolated-agent route uses the work session's inference.
