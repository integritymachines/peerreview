# Direct framework comparison protocol

## Unit of analysis

A causal problem is `z=(O,q,I,A,T)`: observation regime O; precisely defined causal estimand q; intervention semantics I; admissible assumptions A with provenance; and target domain T. Keep all five fixed during a head-to-head comparison.

Core schools: PO (Neyman–Rubin), SCM (Pearl), SE (Heckman–Haavelmo). Record **variants** (e.g. DAG-only SCM and cyclic SCM) and do not conflate identification designs (IV, RD, DiD, synthetic control) with frameworks. A variant's restriction is not automatically a limit on its parent school.

For each variant independently record whether it expresses the target, added assumptions, identified set (with proof), calculation, empirical validation, and resource cost. Require explicit translations of assumptions and interventions before comparing conclusions.

## Outcome classification

- Congruent-informative: equal sharp, informative identified sets.
- Congruent-uninformative: equal vacuous/uninformative identified sets.
- Refinement: one sharp identified set strictly contained in the other's, with origin of the extra restriction explained.
- Compatible divergence: different but overlapping sets.
- Incompatible: disjoint sets. Only call this substantive **framework competition** after auditing sameness of evidence, target, intervention semantics, and admissible restrictions. Under exactly equivalent model classes, contradictory sharp sets signal an error.
- Out-of-variant-scope: the named variant cannot express the model or intervention without extension.
- Indeterminate: evidence or completed analysis insufficient.

Different numeric outputs under different policies are not competing predictions. Different labels are not competing conclusions. Identical vacuous conclusions are not informative congruence.

## Evidence ladder

T0 algebraic reference cases/unit tests; T1 independently derived same-problem formal encodings; T2 reconstruction of published, adversarial comparative claims; T3 differentiating predictions assessed against external experimental evidence.

The immediate high-value contested case is **simultaneous economic feedback**: reconstruct Heckman–Pinto's limitations claim, then test a contemporaneous-cycle SCM variant as well as standard DAG-only analysis, with matched policy counterfactuals and invariance assumptions. Maintain negative findings. A claimed uncovered domain must exhaust substantial, recognized variants; a single variant's failure does not prove school-wide inability.

No presumption of mismatch, superiority, or noncongruence.
