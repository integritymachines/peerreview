# Comparative Atlas — inaugural reference cases

## Conceptual object

For an empirical problem `z=(O,q,I,A,T)`, a framework variant `f` defines an admissible model class `H_f(z)`. Its identified set is `Theta_f(z)={q(h;I,T):h in H_f(z), h compatible with O}`. If two faithful translations use the **same model class**, the **same causal estimand**, and the **same intervention**, their sharp identified sets must be identical. This is an elementary logical constraint, not evidence of universal equivalence of the schools.

The three schools (Neyman–Rubin, Pearl, Heckman–Haavelmo) may overlap, and a school may contain several variants. The research question is which problem classes are expressible, identifiable, or practically tractable in specified variants and whether their outputs actually differ under matched warrants.

## A — Randomized additive treatment: positive congruence

A is randomized independently of U, E(U)=0, Y=tau*A+U, tau=1.25. Target: ATE. Potential outcomes yield E[Y(1)-Y(0)]=1.25; SCM surgical do(A) yields 1.25; invariant econometric structural equation yields 1.25. Informative congruence, no exclusive territory.

## B — Shared nonidentification

U~Bernoulli(1/2); compare (i) A=U, Y=A, and (ii) A=U, Y=U. Both generate the same observational joint law: P(A=Y)=1, P(A=1)=1/2. Their treatment ATEs are 1 and 0 respectively. Thus any framework preserving both models and using only this observation regime must leave the ATE unidentified. The compatible set contains at least {0,1}, with no claim that these are the only possible values.

## C — Average treatment effect versus individual benefit

In a randomized binary-treatment trial suppose P(Y(0)=1)=.30 and P(Y(1)=1)=.70. ATE=.40. With no cross-world information, probability of benefit P(Y(1)=1,Y(0)=0) lies sharply in [.40,.70] by Frechet bounds. Under the *additional* monotone-treatment-response assumption Y(1)>=Y(0), the probability of benefit is .40. The change in result reflects changed assumptions/estimand, **not a change in framework label**.

## D — Simultaneous feedback and intervention semantics

Equations: X=aY+U+lambda, Y=bX+V, a=.4,b=.5, ab=.2; disturbances mean zero. There is a unique equilibrium. A policy changing the **first-equation intercept** lambda changes E[Y] at b/(1-ab)=.625 per unit. A **surgical intervention fixing X=x** changes E[Y] at rate b=.5 per unit. These are different causal questions, not competing framework predictions.

Standard **acyclic DAG-only** formulations cannot directly display a contemporaneous two-way cycle, whereas simultaneous-equations econometrics and **cyclic SCM variants** can express this system, subject to existence/uniqueness conditions. A potential-outcome response Y(x) to the surgical intervention can also be defined; that alone does not determine policy equilibrium effects without more structure. This is a **variant-level representational boundary**, not proof that Pearl's entire school cannot express feedback.

## Summary

Verified: A informative congruence; B observational equivalence; C distinct identification results under different assumptions/targets; D distinct effects under different interventions plus a variant-scope boundary. **Not verified:** any substantive conflict between complete schools under identical evidence, assumptions, intervention and estimand; any uncovered domain for the combined roster. The first rigorous next step is an independent reconstruction of the simultaneity argument, including cyclic SCM variants, not another bibliometric mismatch search.

Sources and opposing perspectives: Imbens (2020), https://doi.org/10.1257/jel.20191597; Richardson & Robins (2013), https://csss.uw.edu/research/working-papers/single-world-intervention-graphs-swigs-unification-counterfactual-and; Heckman & Pinto (2015, 2024), https://pmc.ncbi.nlm.nih.gov/articles/PMC4341827/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC11495853/; Bongers et al. (2021), https://doi.org/10.1214/21-AOS2064; Shpitser & Pearl (2008), https://jmlr.org/papers/v9/shpitser08a.html.
