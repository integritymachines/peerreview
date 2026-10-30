# peerreview

**PBPR: LLM-assisted adversarial academic peer review**

This repository contains a modular architecture for rigorous, repeatable, multi-role academic peer review with large language models.

It separates two things that are often conflated:

- the **review workflow**: how a paper is scrutinized; and
- the **review catalogue**: which criteria, intellectual traditions, and reference works define adequate scrutiny for the task.

The repository includes a deliberately broad cross-disciplinary catalogue in **`criteria.txt`**. That catalogue is useful as a reference implementation and as a routing source for heterogeneous work. It is **not** intended to imply that every review system should use one universal catch-all catalogue.

In many applications, a **purpose-built catalogue with narrower scope is preferable**. A journal, discipline, field, conference, research program, or specialized review task can construct its own criteria and bookshelves using the recipe below. Narrowing the scope should allow greater precision and cleaner coverage, not lower the standard.

The current **`review.txt`** workflow is criteria-driven and cross-disciplinary: it records the epistemic anchor, discipline, field and portable modules relevant to the paper, then applies the selected catalogue through independent preliminary runs and a deciding run.

## Repository Contents

- **`criteria.txt`** — broad cross-disciplinary criteria catalogue and bookshelves.
- **`review.txt`** — core multi-agent review workflow.
- **`preview.txt`** — constructive pre-submission workflow using a completed scorecard.
- **`report.txt`** — editorial-decision workflow using a completed scorecard.

## Core Review Principle

PBPR applies two distinct epistemic tests.

First, **claim survival**:

> **The headline claim should be no stronger than the strongest claim that survives the strongest domain-appropriate adversarial scrutiny.**

In shorthand:

> **C_h ≤ C_s**

where `C_h` is the publication's headline claim and `C_s` is the strongest surviving claim after review.

Second, **comparative precedence**:

> **A scholarly claim must establish why it should take precedence over viable alternatives.**

Survival is therefore necessary but not sufficient. A claim may be internally defensible yet still fail as a scholarly contribution if a viable alternative explains, reconstructs, justifies, proves, or makes the relevant result at least as well, or if the claimed contribution does not establish its novelty or comparative advance over existing scholarship. Absolute support adequacy and comparative precedence are separate tests.

The purpose of a criteria catalogue is therefore not to enumerate topics. It is to encode the recurrent ways in which claims within its scope can fail, become overstated, require narrowing, require stronger warrant, or fail to establish precedence over viable alternatives.

The operating attitude is:

> **Search broadly; flag carefully.**

Generate alternatives and steelmen aggressively. Flag only concerns that survive scrutiny themselves.

## The Basic Architecture

A clean catalogue is compositional.

### Universal layers

**Integrity (I)** covers whether the represented research record is trustworthy.

**Quality (Q)** covers whether claims are precise, significant, novel, adequately warranted, robust, transparent, and properly calibrated.

I and Q are universal.

### Epistemic anchors

The five anchors classify the **precedence-bearing output**: what the publication asks reviewers to recognize as its successful contribution.

- **F — Formal:** proves.
- **E — Empirical:** evidences.
- **S — Source:** reconstructs.
- **N — Normative:** justifies.
- **D — Design:** makes.

The anchor classifies the contribution, not the type of material used to support it. A source-based reconstruction may use quantitative evidence and remain S; a design contribution may use experiments and remain D.

### Disciplines and fields

Disciplines and fields supply **residual domain-specific scrutiny** after I/Q, anchors, and portable methods have done their work.

A field is justified when a recognizable class of publications shares a substantial residual scrutiny regime. A familiar subject label by itself is not enough.

### Portable modules

Portable modules capture specialized scrutiny that travels across disciplines: causal inference, experimental methods, measurement, optimization, simulation, machine learning, survey research, qualitative methods, and similar cross-disciplinary machinery.

They are overlays, not substitutes for a home discipline or anchor.

# Recipe: Build a Purpose-Built Criteria Catalogue

The best starting point is usually **the narrowest scope that matches the actual review task**.

Do not begin by copying the entire broad catalogue. Begin by defining what kinds of publications the catalogue must review well, then add only the scrutiny needed to cover that domain without blind spots.

## 1. Define the scope before writing criteria

State explicitly what the catalogue is for.

Examples:

- a single field;
- a discipline;
- a family of methods;
- a journal;
- a conference;
- a particular class of claims;
- a review workflow focused on one problem such as causal claims.

Specify the intended scholarly level as well. A catalogue for frontier research should be calibrated to frontier scrutiny.

Then test the boundary:

> **Which publications should this catalogue review directly, and which should require another catalogue or imported module?**

A purpose-built catalogue should be complete **within its declared scope**, not artificially universal.

## 2. Fix the invariant layers

Start with I and Q unless the application has a compelling reason to redefine them.

Next identify the relevant precedence-bearing outputs and therefore the required F/E/S/N/D anchors.

Do not infer the anchor from department, method, dataset, or vocabulary. Ask what successful new contribution the publication claims to make.

If the scope contains only one or two anchors, include only those. A narrow catalogue need not reproduce unused architecture.

## 3. Identify the residual fields

For each candidate field, mentally import:

1. I and Q;
2. the relevant anchor or anchors; and
3. any portable methods that would normally apply.

Then ask:

> **What important scrutiny remains specific to this field?**

That remainder is the field's reason to exist.

A useful merge test is:

> **After the shared layers are imported, do these publication types still share a substantial residual scrutiny regime?**

If yes, they may belong together. If the resulting criteria merely interleave different subtype tests, keep them separate.

Field counts are diagnostic, not quotas.

## 4. Derive criteria from failure modes, not topic lists

A standing criterion should represent a **recurrent, material epistemic test**.

A candidate criterion should normally satisfy all of the following:

- **Residuality:** not already owned by I/Q, an anchor, portable module, or higher-level criterion.
- **Recurrence:** relevant to a recognizable class of publications, not one unusual paper.
- **Materiality:** failure can change the surviving claim, its scope, or its credibility.
- **Inspectability:** a reviewer can identify what relation, distinction, boundary, correspondence, or failure is being tested.
- **Correct level:** the test sits at the highest level at which it is genuinely general, but no higher.
- **Orthogonality:** it does not merely restate another test.
- **Compactness without semantic loss:** it is easy to scan without becoming vague.
- **Coverage contribution:** it helps the full set span the field rather than deepening only one favored corner.

A missing test may first appear as an **ad hoc criterion** during review. Repeated recurrence is evidence that it deserves promotion into the standing catalogue.

Use this deletion test:

> **What material failure mode would become harder to detect or route if this criterion disappeared?**

If there is no clear answer, the criterion probably does not deserve independent standing.

## 5. Audit the criterion set for span and aggregate neutrality

A clean set of criteria should span the **discipline or field as actually practiced at the intended level**.

Check horizontal coverage across:

- major claim types;
- governing objects;
- characteristic inferential problems;
- important methods where they create field-specific residual scrutiny;
- major traditions and schools;
- recurring sources of disagreement;
- edge cases that expose weaknesses in the dominant framework.

Do not confuse coverage with equal counts.

Neutrality is an **aggregate property of the set**. Individual criteria can be demanding, asymmetric, or rooted in particular traditions. The full set should not force every publication to accept one contested school, method, ontology, or substantive conclusion merely to enter the review.

A useful adversarial test is:

> **Could strong work from each major tradition in scope be rigorously reviewed by this catalogue without first conceding the conclusions of a rival tradition?**

If not, the set is not yet epistemically neutral enough for general use within that scope.

A venue may deliberately add a **house-style overlay** after this neutral scholarly layer. House style can affect fit and interpretation; it should not erase underlying substantive defects.

## 6. Build the bookshelf from the criteria and the domain

Do not build a bookshelf by collecting famous books and then reverse-engineering criteria from them.

The bookshelf should help reviewers understand and apply the scrutiny encoded by the catalogue.

It has two jobs:

- **horizontal anchoring:** span the domain's governing objects, methods, traditions, and important disagreements;
- **vertical anchoring:** establish a technical and scholarly quality ceiling adequate for frontier review.

A candidate work should earn its place by function.

Useful tests include:

- **Field fit:** does it genuinely belong to this field rather than an adjacent one?
- **Synthetic scope:** does it provide enough integrated coverage to function as a standing reference?
- **Criterion-generating relevance:** does it illuminate multiple recurring tests or distinctions?
- **Rigor:** is it strong enough to support stringent review of frontier scholarship?
- **Coverage contribution:** what major tradition, problem class, or mode of reasoning does it add?
- **Complementarity:** does it add something not already supplied by a stronger retained work?
- **Comparative superiority:** does it beat plausible alternatives for this role?
- **Currency where needed:** does a contemporary work capture present methods and live disputes?
- **Lineage discipline:** is the work being used for the right role rather than duplicated mechanically across levels?

Prefer books, monographs, advanced textbooks, substantial authored syntheses, and strong handbooks where appropriate. Isolated articles, narrow reviews, practitioner manuals, software guides, and public-facing polemics normally belong at the research layer rather than on a standing shelf.

For contemporary synthesis, prefer an integrated authored or genuinely coauthored treatment when it is comparably rigorous and comprehensive. Edited handbooks are entirely appropriate when no integrated treatment covers the field adequately or when plurality itself is part of the field.

## 7. Distinguish antecedents, classics, and contemporaries

These categories serve different epistemic functions.

**Antecedents** identify the intellectual constructions that helped constitute the discipline or field. Their main role is genealogy: they explain where characteristic questions, distinctions, and traditions came from.

**Classics** are field-shaping works whose principles remain operational for present adjudication. Their apparatus may be dated, but they still supply live concepts, propositions, distinctions, or modes of reasoning against which current work can be tested.

**Contemporaries** provide the current technical synthesis: present methods, present standards of evidence or argument, live disputes, and the modern quality ceiling.

The distinction is functional, not chronological.

When one work appears eligible for more than one role:

- retain it as an **antecedent** when its principal value is genealogical;
- retain it as a **classic** at the narrowest appropriate level when it remains operational for current scrutiny;
- retain it in neither role when it no longer wins the comparison for either function.

Do not duplicate a title merely because it is important.

A strong shelf usually combines classics and contemporaries so that durable intellectual traditions and current technical practice constrain one another.

## 8. Audit the bookshelf for span and aggregate neutrality

The bookshelf should span the same scope as the criteria.

Check whether it covers:

- the major intellectual traditions relevant to the field;
- competing explanations or frameworks where the field contains durable disputes;
- the principal technical approaches;
- both durable and current modes of reasoning;
- the major classes of claims represented by the criteria.

Again, neutrality is aggregate. Individual books may advocate strong positions. The shelf as a whole should make serious rival positions available to the review rather than silently canonizing one side.

Ask:

> **What distinct scrutiny or intellectual coverage does this additional volume contribute that the existing shelf does not?**

If the answer is weak, prune.

Also ask the inverse:

> **What major mature tradition or technical perspective would be invisible if this shelf were the reviewer's starting point?**

If the answer identifies a real gap, add or replace.

The governing standard is:

> **Enough to triangulate the field's strongest mature reasoning; no more than can be individually defended.**

There is no mandatory number of books, classics, contemporaries, fields, or criteria.

## 9. Stress-test the catalogue on representative publications

Before treating a catalogue as stable, route several very different publications through it.

Include:

- central cases;
- boundary cases;
- work from competing traditions;
- hybrid-method papers;
- unusually theoretical or unusually applied work;
- strong papers that should mostly pass;
- papers with known failure modes that the catalogue should catch.

Look for four kinds of defect:

1. **blind spots** — important failures with no natural criterion;
2. **duplication** — the same failure repeatedly appears under different codes;
3. **routing ambiguity** — multiple fields claim the same residual scrutiny without a principled distinction;
4. **bias by construction** — one legitimate tradition is systematically forced to defend assumptions that rival traditions are allowed to leave implicit.

Repair the architecture, not just the test case.

## 10. Prefer purpose-built catalogues when the task is narrow

The broad `criteria.txt` catalogue is useful when the reviewer may encounter work from many disciplines or when routing must happen dynamically.

For a known domain, a narrower catalogue will often be better.

A purpose-built version can:

- remove irrelevant disciplines, anchors, and modules;
- subdivide a field more finely where the application needs it;
- merge distinctions that do no useful work at the chosen scope;
- replace general bookshelves with stronger domain-specific ones;
- add specialized criteria that would be too narrow for the broad catalogue;
- encode venue-specific intellectual traditions as a separate house-style layer.

The goal is not to reproduce the master catalogue at smaller scale. The goal is to reconstruct the **minimal sufficient scrutiny architecture for the declared scope**.

Narrower should mean **more precise**, not less rigorous.

## 11. Keep construction decisions auditable

When changing a catalogue, distinguish:

- topology changes;
- criterion additions, deletions, and rewrites;
- bookshelf additions, deletions, and moves;
- antecedent/classic/contemporary role changes;
- routing changes;
- house-style overlays.

For substantive changes, preserve the reason the old element was replaced and what epistemic function the new element serves.

Do not let formatting cleanup, count normalization, or naming convenience silently make substantive decisions.

## Selecting Criteria for an Individual Review

Once a catalogue exists, an individual review should use the **minimal sufficient route** through it:

1. apply I and Q;
2. identify the precedence-bearing output and anchor;
3. select the home discipline and residual field;
4. import auxiliary anchors and portable modules as required;
5. add an ad hoc criterion when a material paper-specific failure mode remains uncovered.

Selection changes the **kind** of scrutiny, not its rigor.

> **No discipline is held to a lower standard.**

## Review Workflow

The current `review.txt` conducts **X fully independent preliminary runs** (default `X=10`) followed by one deciding run. Preliminary runs share no information with one another; only the System retains the resulting scorecards between runs. The full per-run protocol is retained for audit but is not exposed to later runs.

At a high level:

1. **S pre-scans** the paper, identifies focus and technical competencies, records anchor/discipline/field/portable routing, performs an integrity pre-check, and selects an assigning editor tradition.
2. **A performs breadth search**, selects a mixed reviewer panel, assigns literature, and records confidential flaw pointers and candidate flags.
3. **R1–RN review independently and flag-blind**, test alternatives, self-assign additional literature, and identify claim impact.
4. **H performs depth search**, adjudicates flaws and alternatives, explicitly tests comparative precedence, and seeks consensus.
5. **E audits the panel**, resolves disagreements, verifies material findings, and issues the scorecard.
6. **The deciding run receives the concatenated preliminary scorecards**, but not the prior protocols, and independently adjudicates the accumulated findings.

The scorecard is the principal handoff object. It records the issue, location, justification, disposition, claim impact, **precedence**, and relevant literature.

The workflow is primarily an **epistemic quality-control process**: it asks what claims survive, what warrant they possess, what alternatives remain viable, and whether the claimed scholarly contribution establishes precedence over those alternatives. Integrity criteria are included, but the workflow does not convert an LLM review into a forensic integrity investigation.

## Downstream Workflows

### Pre-submission mentorship: `preview.txt`

Takes the paper, scorecard, and criteria used and produces a constructive improvement brief without a publication verdict.

### Editorial decision: `report.txt`

Takes the paper and completed scorecard and produces a final publication decision, synthesized rationale, editorial letter, and short author-editor exchange.

## Practical Principles

- **Pinpoint accuracy:** identify exactly what is wrong, where it occurs, and why it matters.
- **Claim calibration:** narrow claims when necessary instead of treating every weakness as binary acceptance or rejection.
- **Method pluralism with rigor:** different epistemic modes require different tests, not weaker tests.
- **Minimal sufficient architecture:** include every scrutiny layer the task needs and no layer merely for completeness.
- **Aggregate neutrality:** criteria and bookshelves should span the legitimate traditions inside their declared scope.
- **Modularity:** anchors, fields, and portable modules should be recombinable.
- **Auditability:** catalogue construction and revision should leave a visible substantive trail.
- **Human control:** PBPR is an aid to expert judgment, not a substitute for it.

## Disclaimer & Best Practices

* These tools are designed to **augment, not replace, human expertise**. It is highly recommended that this process be run in conjunction with traditional freeform human review. Pinpoint accuracy should simplify the location of flags in the original text.
* **Integrity review is signal-based, not forensic.** PBPR can probe potential integrity problems through inconsistencies, implausibilities, citation/source anomalies, reporting patterns, internal contradictions, and other signals available from the submitted materials and accessible scholarship. Absence of a signal is not evidence that misconduct or data problems are absent, and an integrity flag is not itself a finding of misconduct.
* **PBPR is not a dedicated data audit, code audit, or replication exercise.** Unless such work is separately supplied and explicitly undertaken, the workflow does not independently verify raw data against source records, reproduce every transformation, rerun analysis code, or establish computational replicability. Missing materials that were simply not supplied for the review are not themselves a defect in the paper.
* No warranties are offered or implied regarding the accuracy, validity, or publication outcomes resulting from these outputs. Ultimate responsibility for any editorial or submission decisions rests entirely with the human operator.
