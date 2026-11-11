# Study E validation

Date: 2026-11-11. Standard-library Python, no network needed to reproduce calculations.

Run from repository root:

```bash
python mdci/atlas/atlas.py
python mdci/atlas/simultaneous_policy.py
python -m unittest discover -s mdci/atlas -p 'test_*.py' -v
```

Result: **17 tests passed**, including all 6 unmodified inaugural tests and 11 Study E tests. `RESULTS_v02.json` is generated from `serialized_results()` and its equality to regenerated output is itself tested. Fractions are exact strings rather than rounded floating-point claims. Floating point is used only to check convergence of an explicitly specified adjustment process.

Coverage: algebraic solutions and residuals; matched PO schedule; combined policy and nonadditivity; distinct clamp semantics; distribution and individual counterfactual; calibration identification; full baseline observational equivalence and different policy outcomes; reduced-form DAG's restricted intervention equivalence; stable convergence; unique but unstable equilibrium; no/multiple equilibria and a singular post-policy regime; unrestricted-policy mean constructions; saved-results consistency.

Interpretive review: the comparison holds evidence, policy mapping, target, unit and assumptions fixed. A graph's inability to display the behavioral cycle is not treated as inability to answer every policy query. Observational witnesses are not labeled sharp bounds. Policy invariance and common shocks are explicit; no empirical accuracy, complete framework implementation, external replication, or framework superiority is claimed.

Publication scope: only `mdci/atlas/` files are included. Inaugural code, tests and JSON remain unchanged. Literature references and version-specific locators are in [the study](STUDY_E_SIMULTANEOUS_POLICY.md).
