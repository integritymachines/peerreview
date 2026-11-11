# Study E — simultaneous behavior and changes in policy rules

Date: 2026-11-11. Roster unchanged: Neyman–Rubin PO, Pearl SCM, Heckman–Haavelmo structural econometrics (SE). This extends case D, not replaces it. Primary-source reconstruction plus a new exact reference model; no empirical dataset, independent external review, or framework-superiority result.

## 1. The contested claims, reconstructed narrowly

**Heckman–Pinto 2015**, section 6, equations (7a–b), Table 9 and equations (8a–b), distinguish the simultaneous empirical system from hypothetical systems with independently varied inputs. Fixing one equation's input traces a structural response, even when the original system is cyclic. They argue that ordinary DAG machinery does not directly apply, and discuss nonexistent or multiple reduced-form solutions. Their section 5 comparison also credits both approaches with structural equations, autonomy and causal fixing. This is not a claim that hypothetical variation alone identifies an equilibrium policy effect. [HP15](https://pmc.ncbi.nlm.nih.gov/articles/PMC4341827/)

**Heckman–Pinto 2024**, section 2.4, separates implemented-policy evaluation, mechanisms, transport and previously unimplemented policies. Sections 6.5 and 7 criticize restricting analysis to graphical independence rules or individual treatment comparisons without interactions. Crucially, section 7 explicitly recognizes Bollen and Pearl's exposition of simultaneous structural models. Section 7.1 retains existence issues; section 7.2 distinguishes fixing from conditioning. The strongest defensible challenge here is whether a specified method accommodates behavioral feedback and justified policy extrapolation, not whether every SCM is recursive. [HP24](https://pmc.ncbi.nlm.nih.gov/articles/PMC11495853/)

**Pearl's response**, R-420, sections 2–3, distinguishes SCM from do-calculus as one inference tool and disputes treating parametric restrictions or simultaneity as outside SCM. His response is a participant's argument, not independent adjudication. Graph-only nonparametric identification and identification using added equation restrictions must not be compared as though their assumptions were identical. [P13](https://ftp.cs.ucla.edu/pub/stat_ser/r420.pdf)

**Cyclic literature:** Bongers et al., sections 3 and 8, define solvability conditions. Simple SCMs are uniquely solvable for every subset; Proposition 8.2 preserves this class under perfect interventions and twin construction, and Definition 8.6 defines potential outcomes, including cyclic cases. Arbitrary cyclic systems need not have unique observational or counterfactual distributions. [B21](https://arxiv.org/html/1611.06221v5#S8) Forré and Mooij's Theorem 7.2 gives causal-calculus rules for ioSCMs using sigma-separation. This refutes a blanket ban on causal calculus with cycles; it does not license ordinary DAG rules on any cyclic graph. [FM19](https://arxiv.org/html/1901.00433v2#S7)

**PO scope:** Rubin's foundational treatment comparison concerns well-defined alternatives and assignment, including nonrandomized studies. It is not a theorem that potential-outcome notation forbids equilibrium outcomes. [R74](https://dash.harvard.edu/entities/publication/73120378-82c0-6bd4-e053-0100007fdf3b) Below, a unit is an entire interacting pair, and treatment is a complete policy regime. Extending an individual no-interference analysis to this unit/target requires an explicit change of formulation. The equilibrium restrictions we add to PO are substantive assumptions, not consequences of notation.

These reconstructions concern the specified passages, not every argument in these papers (e.g. Roy selection, mediation and measurement systems). No literature-wide historical priority or computational-superiority claim is adjudicated.

## 2. Matched problem z=(O,q,I,A,T)

**T:** independent pairs of interacting economic agents; X and Y are their real-valued actions, interpreted as deviations from reference levels. There is within-pair feedback and no between-pair interference. No nonnegativity constraint, welfare criterion, budget constraint, entry, or aggregate market-clearing condition is imposed.

**I:** policy pi=(lambda,k) changes agent X's incentive intercept and responsiveness to Y. Baseline pi0=(0,0); target pi1=(1,1/5). Both agents reoptimize. The intervention is identical across encodings. A separate clamp J(x) replaces X's decision equation by X=x. J is a diagnostic alternative, never substituted for pi1.

**A_struct:**

```
X = c + lambda + (a+k)Y + U
Y = d + bX + V
a=2/5, b=1/2, c=1, d=2
E[U]=E[V]=0
```

This is an original illustrative model, not a claimed replication of an empirical Heckman–Pinto example. One microfoundation is quadratic objectives

```
payoff_X = [c+lambda+U+(a+k)Y]X - X^2/2
payoff_Y = [d+V+bX]Y - Y^2/2.
```

Each best response is unique; the simultaneous solution is the Nash equilibrium. A policy changes incentives, not assigned action. The maintained invariance is of the **policy-indexed payoff/response functions**, the Y equation, and the disturbance law. It is not invariance of the baseline coefficient a+k or of a baseline reduced-form regression. This assumption is stipulated, not inferred from the graph or from the word 'structural'.

For full-distribution and individual examples the reference law gives independent U,V in {-1,+1}, each equiprobable. Mean results require only zero means and finite moments. In identification experiments below the admissible class permits correlated mean-zero shocks, so the observational twin is not smuggling a violation of an independence assumption into a comparison.

**q:** primary target E[Y(pi1)-Y(pi0)] in the same population. Secondary targets: policy-specific joint law, individual contrast given baseline (X,Y), and the separate clamp contrast E[Y(J(x+1))-Y(J(x))]. Individual contrasts retain the same U,V across regimes; population contrasts alone do not identify a general cross-world coupling.

**O:** distinguish three evidence regimes, shared by all variants:

1. **O_known:** exact baseline law plus the supplied numeric structure and policy mapping. This supports calculation conditional on a fully specified model, not discovery of structure from observations.
2. **O_base:** only the exact baseline joint law, with unknown a,c (even granting b=1/2,d=2), invariant linear response equations, known additive lambda,k policy semantics, and arbitrary correlated mean-zero shocks. Baseline data do not determine the target.
3. **O_cal:** baseline joint law plus exact population mean responses in randomized clamp arms J(0),J(1), and randomized incentive arms (0,0),(1,0). All interventions have positive assignment probability, independent of pair disturbances; consistency, identical population and correct implementation are maintained. These are synthetic population experiments, not collected data. a,b,c,d are initially unknown; the same invariant linear family and policy mapping are assumed.

Finite-sample uncertainty is deliberately absent. Do not call O_known or O_cal an identification result from O_base.

## 3. Derivation and nontrivial policy result

Let A=a+k and D=1-bA. Substitution gives

```
X(pi) = [c+lambda+U+A(d+V)] / D
Y(pi) = [d+V+b(c+lambda+U)] / D.
```

For D nonzero this is the unique solution for every shock realization. With no self-loops each singleton equation is uniquely solvable given the other action; the pair is uniquely solvable too. Thus each included regime meets the simple-SCM subset condition. Introducing a root policy node restricted to the listed regimes preserves this property. It would not remain true on a policy domain including D=0.

| Regime | E[X] | E[Y] | Change in E[Y] from baseline |
| --- | ---: | ---: | ---: |
| Baseline (0,0) | 9/4 | 25/8 | 0 |
| Intercept only (1,0) | 7/2 | 15/4 | 5/8 |
| Responsiveness only (0,1/5) | 22/7 | 25/7 | 25/56 |
| Combined (1,1/5) | 32/7 | 30/7 | **65/56** |

Combined minus the two separate effects is 5/56: feedback makes the policy components nonadditive. Analytically, dE[Y]/dlambda=b/D and dE[Y]/dk=b E[Y]/D, so the cross-partial is b^2/D^2, positive here. These are total equilibrium responses, not ceteris paribus slopes.

Under J(x), Y=d+bx+V, giving a unit clamp contrast of b=1/2. Under hypothetical input replacement X_tilde=x in the Y equation, the same Y response follows. Replacing both input edges by independent hypothetical values, however, produces two structural response schedules; it is **not** joint node intervention do(X=x,Y=y), whose outputs are fixed, nor is it the original equilibrium. This distinction is necessary when translating Heckman–Pinto's hypothetical systems.

The reference shock law gives Var[Y(pi1)]=(1+b^2)/D^2=125/49. Baseline (X,Y)=(3,5/2) reveals (U,V)=(1,-1); retaining these shocks yields Y(pi1)=25/7 and individual benefit 15/14. This abduction-and-recalculation requires correctly known equations and shock persistence. An average policy effect alone would not justify it.

## 4. Explicit encodings and applicability

| Variant | Encoding and assumptions | Result under O_known or O_cal | Boundary / practical cost |
| --- | --- | --- | --- |
| SE, simultaneous autonomous responses | Solve both behavioral equations with the same shocks after replacing the specified incentive parameters; hypothetical clamps evaluate the remaining autonomous response | Singleton {65/56}; same joint/individual responses when full shock structure is supplied | Requires policy invariance and equilibrium solution; two-equation elimination |
| Cyclic SCM, simple equilibrium variant | Endogenous X,Y with X↔Y directed cycle, disturbance law P(U,V); policy root Pi changes arguments of fixed f_X; do(Pi=pi1) leaves feedback intact; do(X=x) replaces only f_X | Same singleton and responses | Subset solvability checked above; no generic DAG identification rule invoked; same elimination |
| PO, pair-level regime-indexed variant | Joint schedules (X_i(pi),Y_i(pi)) constrained to satisfy both equations with shared U_i,V_i; separate schedules for J(x); consistency for actually assigned regime | Same singleton and responses | Equilibrium restrictions and policy mapping must be supplied or identified; writing Y_i(pi) alone supplies neither |
| PO, individual treatment-only/no-interference variant | Only Y_i(x_i), ignoring the partner and policy version | Cannot faithfully encode the full specified problem without extension | Out-of-variant-scope, not school-wide inability; pair-level reformulation changes unit explicitly |
| Acyclic SCM on original actions with their behavioral mechanisms | Would need both X→Y and Y→X with nonzero coefficients | Out-of-variant-scope | No DAG has this directed cycle; a time-unrolled model adds dynamics and a limiting argument |
| Policy-indexed reduced-form DAG | Pi,U,V→X and Pi,U,V→Y using the solved functions; shared disturbances allowed | Same policy singleton and policy joint law | Expresses this restricted policy query, but clamping X leaves Y unchanged and loses the original J semantics |

The last row is an important negative result for a simplistic 'DAGs cannot answer this policy question' claim. An acyclic solved representation suffices for interventions on Pi, provided its policy-dependent functions are warranted. It does not represent the full original intervention family. Conversely, merely drawing a DAG or writing a response schedule cannot recover those functions from baseline evidence.

In each faithful full encoding the equations, shock law, target and intervention are identical. Elimination proves pointwise equality, hence equality of all derived distributions and expectations; the numeric checks are not a vote among inference engines. The code obtains the structural solution by eliminating Y and the PO schedule by eliminating X, with an additional iterative numerical check. These are independently arranged calculations by the same study author, not independent implementations of three complete frameworks.

## 5. Identification: what evidence actually buys

### O_cal: sharp singleton conditional on invariant structure

Let mX=9/4, mY=25/8. The randomized clamp contrast identifies b=1/2. The randomized unit-intercept contrast identifies r=b/(1-ab)=5/8. For b,r nonzero,

```
a = 1/b - 1/r = 2/5
c = mX - a*mY = 1
d = mY - b*mX = 2.
```

Thus every model in this specified class consistent with O_cal has these parameters; substitution uniquely yields 65/56. The reference model is a witness that the identified singleton is nonempty and sharp. Given the entire baseline joint law, the invertible residual map also identifies the joint disturbance law in this class. This does not establish nonparametric identification, robustness to measurement error, or identification if the incentive's exclusion restriction fails. If b=0, this calibration formula is unavailable; that need not mean every target is unidentified (with invariant Y, this policy has zero Y effect).

### O_base: a constructive observational equivalence result

Write baseline centered observations as Xc=X-mX, Yc=Y-mY. For any candidate t set

```
a_t=t, c_t=mX-t*mY, b_t=1/2, d_t=2
U_t=Xc-t*Yc, V_t=Yc-(1/2)Xc.
```

Push the complete baseline law through this residual transformation, retaining each atom's probability. Both shocks have zero mean. Whenever 1-t/2 is nonzero, these parameters reproduce **the entire baseline joint law**, not merely its covariance. Allowing correlated shocks is essential for this witness family.

For the same additive policy (lambda,k)=(1,1/5),

```
Delta_t = b[lambda+k*mY]/[1-b(t+k)]
        = (13/16)/(9/10-t/2).
```

t=2/5 gives 65/56; t=0 gives 65/72. Both baseline and target equilibria are unique and dynamically stable under the adjustment specified below. They even agree on the clamp slope. Their intercept-experiment responses differ (5/8 versus 1/2), explaining why O_cal distinguishes them. These are compatible-model witnesses, **not sharp endpoints**; the full sharp set for broader invariant model classes is not computed here. Every faithful encoding must preserve this nonidentification. No claim of an equal vacuous sharp set is made in this restricted class.

### Without policy invariance: sharp shared ignorance

Even O_cal does not identify the new policy if we remove restrictions connecting k=1/5 to observed k=0 regimes. Add eta*1{k=1/5} to the Y response equation, leaving all baseline/calibration distributions unchanged. At the target the mean shifts by eta/(7/10). Every real desired policy contrast is obtained by a finite eta, without changing the determinant. With unrestricted real outcomes, the sharp identified set is therefore R in each encoding admitting these extensions: **congruent-uninformative**. Structural labels do not supply missing invariance. The candidate addition is an admissible alternative only in this explicitly weakened model class.

## 6. Boundaries, failures and unresolved questions

* **Existence versus uniqueness:** D=0 is not a very large finite effect. With a+k=2, c=1,d=2,U=V=lambda=0 the equations imply 0=5 (no solution). With c=d=U=V=lambda=0 they allow every pair (X,X/2) (multiple solutions). A clamp can remain meaningful even when the original equilibrium is undefined. Point policy predictions then need a justified selection or dynamic model; no framework label supplies one.
* **Stability differs from solvability:** under simultaneous best-response updates, the Jacobian has spectral radius sqrt(abs(b(a+k))). Convergence from arbitrary starting values requires abs(b(a+k))<1. Baseline and target satisfy it. a=3,b=1/2 gives a unique static equilibrium but divergent adjustment. The static theory alone does not establish that the economy reaches its equilibrium; other adjustment rules require separate analysis.
* **Counterfactual policy domain:** a nonsingular baseline does not guarantee nonsingular intervention. Here k=8/5 makes the target singular. Continuous admissible policies must exclude this value or add new semantics. Near it, predictions are sensitive to parameter error; this study does not estimate uncertainty.
* **Interference and versions:** treating the interacting pair as the unit handles only within-pair interaction. Cross-pair spillovers, composition changes and aggregate equilibrium require richer units or treatment schedules. The policy label must specify the incentive rule, not just an observed X level.
* **Behavioral transport:** altered preferences, expectations, information, selection, constraints or shock distributions are not modeled. Our quadratic specification demonstrates a transparent mechanism change, not a general solution to the Lucas critique or policy forecasting.
* **Graphical inference:** no sigma-separation implementation, cyclic identification completeness proof, or general discovery procedure is tested. Applicability to nonlinear, discrete, multiple-equilibrium or latent-measurement economies remains unknown here.
* **Evidence and resources:** four exact shock atoms, rational arithmetic and a two-variable solve; no sampling or optimizer. There is no external experimental validation and no measured cross-framework usability/cost comparison. T0 calculations and a T1 formal translation support a bounded T2 reconstruction; no T3 evidence.

## 7. Findings to retain

1. **Congruent-informative:** under O_known or O_cal and the matched invariant model, SE, cyclic SCM and regime-indexed PO give the same sharp singleton 65/56. A policy-indexed reduced-form DAG also answers this restricted policy query.
2. **Shared nonidentification:** O_base admits at least the two explicit policy effects 65/56 and 65/72. Removing cross-policy restrictions yields a proven sharp set R even with calibration evidence.
3. **Variant limitation:** DAG-only behavioral representation on the original variables and individual no-interference treatment-only PO cannot directly encode the specified system. This establishes no school-wide exclusion.
4. **Different intervention:** the clamp slope 1/2 and incentive response 5/8 are not contradictory causal answers. Hypothetical edge-input variation must also be distinguished from joint node fixing.
5. **No demonstrated substantive framework competition, framework-exclusive win, or uncovered domain for the entire roster.** Equilibrium failures are shared requirements for specifying a coherent question, not evidence of superiority.

## 8. Reproduction and source ledger

From repository root, Python 3.10+ and only its standard library:

```bash
python mdci/atlas/atlas.py
python mdci/atlas/simultaneous_policy.py
python -m unittest discover -s mdci/atlas -p 'test_*.py' -v
```

[RESULTS_v02.json](RESULTS_v02.json) stores exact fractions as strings. The regression test compares regenerated JSON to this artifact. [test_simultaneous_policy.py](test_simultaneous_policy.py) checks equation residuals across several parameter regimes, independently eliminated response formulas, nonadditivity, distributional moments, individual abduction, experimental calibration, equality of the full baseline law for two different policy models, reduced-form intervention mismatch, convergence, singularity and unique-but-unstable behavior. Existing v0.1 tests are retained. Tests verify these constructions, not the entire literature or an empirical economic claim.

Primary sources read on 2026-11-11 (section locators above refer to these accessible versions):

* **HP15:** James J. Heckman and Rodrigo Pinto (2015), *Causal Analysis After Haavelmo*, Econometric Theory 31(1), 115–151. [DOI](https://doi.org/10.1017/S026646661400022X); [author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC4341827/). Online publication 2014; issue year 2015. Use section 6/Table 9 in this version, not table numbering from older working papers.
* **HP24:** James Heckman and Rodrigo Pinto (2024), *Econometric Causality: The Central Role of Thought Experiments*, Journal of Econometrics 243(1–2), 105719. [DOI](https://doi.org/10.1016/j.jeconom.2024.105719); [author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC11495853/), sections 2.4, 6.5, 7–7.2.
* **P13:** Judea Pearl (2013), *Reflections on Heckman and Pinto's “Causal Analysis After Haavelmo”*, UCLA technical report R-420, sections 2–3. [Author-hosted PDF](https://ftp.cs.ucla.edu/pub/stat_ser/r420.pdf).
* **B21:** Stephan Bongers, Patrick Forré, Jonas Peters and Joris M. Mooij (2021), *Foundations of Structural Causal Models with Cycles and Latent Variables*, Annals of Statistics 49(5), 2885–2915. [DOI](https://doi.org/10.1214/21-AOS2064); [version 5 full text](https://arxiv.org/html/1611.06221v5), sections 3, 8, Definition 8.1, Proposition 8.2, Definition 8.6. Cited conditions, not merely the abstract, delimit our cyclic encoding.
* **FM19:** Patrick Forré and Joris M. Mooij, *Causal Calculus in the Presence of Cycles, Latent Confounders and Selection Bias*, UAI 2019; [arXiv v2](https://arxiv.org/html/1901.00433v2), Theorem 7.2. This supports the existence of cyclic calculus, not unrestricted use of acyclic rules.
* **R74:** Donald B. Rubin (1974), *Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies*, Journal of Educational Psychology 66(5), 688–701. [Author repository record/abstract](https://dash.harvard.edu/entities/publication/73120378-82c0-6bd4-e053-0100007fdf3b); [DOI](https://doi.org/10.1037/h0037350). Used for foundational scope only; the equilibrium translation is derived here, not attributed to this article.
