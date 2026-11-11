# Comparative Atlas of Causal Frameworks — v0.1

**Fixed roster:** Neyman–Rubin potential outcomes (PO), Pearl structural causal models (SCM), Heckman–Haavelmo structural econometrics (SE).

The unit of comparison is an exact causal problem and a specified *framework variant*, not a paper's identification design. Distinguish Pearl's acyclic DAG-based methodology from broader structural causal models with cycles. Do not infer framework competition from different assumptions, interventions, or estimands.

Read [ATLAS_v01.md](ATLAS_v01.md) for four worked cases, [PROTOCOL.md](PROTOCOL.md) for comparison rules, and [RESULTS_v01.json](RESULTS_v01.json) for verified reference calculations.

Run offline, using only Python's standard library:

```bash
python mdci/atlas/atlas.py
python -m unittest discover -s mdci/atlas -p 'test_*.py' -v
```

**Status:** 6 passing tests in the initial run. This is a formal toy-model test bed, not an empirical evaluation or an inference engine implementing the three complete schools. No framework-exclusive win, uncovered domain, or true framework conflict has been shown. The MDCI signature cube is deliberately not part of this test.

Background: [Imbens 2020](https://doi.org/10.1257/jel.20191597); [Heckman and Pinto 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4341827/); [Heckman and Pinto 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11495853/); [Richardson and Robins 2013](https://csss.uw.edu/research/working-papers/single-world-intervention-graphs-swigs-unification-counterfactual-and); [Bongers et al. 2021](https://doi.org/10.1214/21-AOS2064); [Shpitser and Pearl 2008](https://jmlr.org/papers/v9/shpitser08a.html).
