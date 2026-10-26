# peerreview

**PBPR: LLM-assisted adversarial academic peer review**

This repository contains a modular peer-review architecture for running rigorous, repeatable, multi-role academic review with large language models. The framework separates the review process from the catalogue of standards used to scrutinize a publication.

The central catalogue is **`criteria.txt`**. It is designed to support review across disciplines by combining universal integrity and quality standards, epistemic anchors, discipline and field criteria, portable methodological modules, and curated scholarly bookshelves.

The current **`review.txt`** prompt remains calibrated primarily to top-tier economics review. The cross-disciplinary catalogue is the architectural basis for extending and revising that prompt.

## Repository Contents

- **`criteria.txt`** — the cross-disciplinary peer-review criteria catalogue and bookshelves.
- **`review.txt`** — the core multi-agent review workflow. It produces a consolidated scorecard after repeated independent review runs.
- **`preview.txt`** — a constructive pre-submission workflow that turns a completed scorecard into an actionable revision brief without issuing a publication verdict.
- **`report.txt`** — an editorial decision workflow that turns a completed scorecard into a final verdict, report, and editorial letter.

## Core Review Principle

PBPR is built around a simple calibration rule:

> **The headline claim should be no stronger than the strongest claim that survives the strongest domain-appropriate adversarial scrutiny.**

In shorthand:

> **C_h ≤ C_s**

where `C_h` is the publication's headline claim and `C_s` is the strongest surviving claim after review.

Equality indicates strong calibration. A weaker headline can reflect epistemic restraint. A stronger headline indicates overclaiming.

The catalogue is therefore not a taxonomy of topics. It is a map of recurrent ways claims can fail, become overstated, require narrowing, or require stronger warrant.

The operating attitude is:

> **Search broadly; flag carefully.**

Reviewers should generate alternatives and steelmen aggressively, but issue a flag only when the concern is substantively correct and useful for adjudication or repair.

## Catalogue Architecture

The catalogue is compositional. A paper is not reviewed against every listed criterion.

### Universal layers

**Integrity (I)** asks whether the represented research record is trustworthy: conflicts, plagiarism, hallucination, citation manipulation, source or data honesty, fabrication, and selective reporting.

**Quality (Q)** asks whether the claim is well formed, adequately supported, robust, transparent, significant, novel, and properly calibrated.

I and Q apply universally.

### Epistemic anchors

The five anchors classify the **precedence-bearing output** — what the publication asks reviewers to recognize as its successful contribution — rather than the type of warrant used to support it.

- **F — Formal:** proves.
- **E — Empirical:** finds.
- **S — Source:** reconstructs.
- **N — Normative:** justifies.
- **D — Design:** makes.

A publication may use several kinds of warrant without changing its home anchor. An engineering contribution may be D while relying heavily on E; a historical reconstruction may use quantitative evidence while remaining S.

### Home disciplines and fields

A **home discipline** supplies the publication's native or default residual scrutiny.

A **field** supplies specialized scrutiny for a coherent family of claims within that discipline. Fields are defined by shared residual failure modes, not merely by subject labels or departmental boundaries.

The controlling question for a field is:

> **After I/Q, the relevant anchors, and portable modules are imported, do these publications still share a substantial residual scrutiny regime?**

A field should not exist merely because a familiar subfield name exists. Conversely, distinct fields should not be merged merely to regularize counts if their surviving tests are genuinely different.

### Portable modules

Portable modules capture specialized scrutiny that recurs across disciplines without belonging to one discipline.

The current catalogue includes modules for causal inference, decision analysis, experimental methods, law and economics, measurement and psychometrics, machine learning, network analysis, optimization, qualitative and ethnographic methods, simulation, spatial analysis, survey research, and evidence synthesis.

Portable modules are overlays. They do not replace the relevant home discipline or epistemic anchor.

## Selecting the Review Route

`criteria.txt` is an overall catalogue, not a checklist to apply in full. A review should select the **minimal sufficient route** needed to expose the publication's claims to the strongest relevant scrutiny.

1. **Apply I and Q.**
2. **Identify the precedence-bearing output** and select the appropriate F/E/S/N/D anchor.
3. **Select the home discipline and field** by the contribution being made, not merely by author affiliation, dataset, method, or vocabulary. Use the General field when no narrower field provides a better residual fit.
4. **Import auxiliary anchors and portable modules** where the claims actually require them.
5. **Tailor the route to the publication.** Irrelevant criteria may be omitted; a genuinely missing test may be added ad hoc.

Selection changes the **kind** of scrutiny, not its rigor.

> **No discipline is held to a lower standard.**

The catalogue is intentionally an overall list. Users are invited to adapt the selected route to a manuscript, venue, or specialized review purpose.

## Constructing and Curating the Catalogue

The catalogue is curated rather than accumulated. Disciplines, fields, criteria, and bookshelves should be broad enough to span the relevant scholarly domain but compact enough that every retained element has a distinct function.

There are useful compact ranges and proliferation checks, **not hard numerical quotas**.

### Coverage and neutrality

Both the criteria set and the bookshelf for a discipline or field should provide **horizontal coverage** across its governing objects, methods, major traditions, and important forms of disagreement.

They should also provide a **vertical quality ceiling** high enough to support stringent review of frontier scholarship.

Neutrality is an **aggregate property** of the catalogue, not a requirement imposed on every individual criterion or book. Individual works can represent strong, competing, or historically situated positions. The set as a whole should not systematically privilege one school, method, tradition, or substantive conclusion unless that bias is explicitly introduced as a separate journal or house-style overlay.

A useful test is:

> **Could a serious publication from any major tradition inside this discipline or field receive rigorous scrutiny from the selected criteria and bookshelf without first accepting a rival tradition's conclusions?**

Coverage does not mean equal representation by count. It means that the major live and field-shaping forms of reasoning are available for scrutiny and comparison.

### Selecting standing criteria

A standing criterion belongs in the catalogue when it captures a **recurrent, material way in which a claim can fail, become overstated, or require narrowing**.

A candidate criterion should satisfy these tests:

- **Residuality:** it adds scrutiny not already supplied by I/Q, the relevant anchor, a portable module, or a more general surviving criterion.
- **Recurrence:** it applies to a recognizable class of publications, not one unusual paper.
- **Materiality:** failure can change the surviving claim, its scope, or the publication's credibility.
- **Specificity:** it identifies a relation, distinction, boundary, correspondence, or failure mode that a reviewer can actually inspect.
- **Correct level of generality:** put the test at the highest level at which it is genuinely general, but no higher.
- **Orthogonality:** it should not merely restate another criterion in different words.
- **Compactness without semantic loss:** wording should be concise enough to scan without collapsing distinct tests into a vague umbrella.
- **Promotability:** a missing paper-specific test can first be added ad hoc; repeated recurrence is evidence for promotion into the standing catalogue.
- **Coverage contribution:** the resulting criterion set should span the discipline or field rather than cluster around the easiest, most fashionable, or most methodologically dominant publication types.

Criterion proliferation is checked by asking:

> **What material failure mode would become harder to detect or route if this criterion were removed?**

If there is no distinct answer, merge, rewrite, or delete it. A criterion disappears only when another surviving test actually captures the same epistemic work; thematic similarity is not sufficient.

### Selecting and maintaining fields

Fields should correspond to **shared residual scrutiny regimes**, not convenient umbrella topics.

Merge fields when their characteristic publications share most of the same residual failure modes. Keep them separate when a merger would produce an interleaved list of subtype-specific tests.

Field count is diagnostic only. A long field list invites a compression check; a short list invites a coverage check. Neither creates a mandatory target.

### Selecting bookshelf works

A bookshelf is a compact set of **top-line synthetic works that materially support the scrutiny represented by the anchor or field**. It is not a bibliography, a citation leaderboard, or a display of famous names.

Bookshelves serve two purposes:

- **Horizontal anchoring:** coverage across the field's governing objects, methods, and major traditions.
- **Vertical anchoring:** a scholarly and technical quality ceiling against which frontier work can be reviewed.

A candidate work should satisfy the following tests:

- **Synthetic scope:** prefer books, monographs, advanced textbooks, handbooks, collected-paper volumes, or comparable synthetic works. Isolated papers, conference proceedings, chapters, narrow intervention reviews, public-facing polemics, and software-specific manuals normally belong at the research layer rather than on the standing shelf.
- **Field fit:** the work should genuinely anchor the field whose claims it is meant to scrutinize.
- **Criterion-generating relevance:** it should illuminate multiple recurring distinctions, standards, or failure modes represented by the field.
- **Rigor:** it should be credible as advanced scholarly background for stringent review of frontier work.
- **Coverage contribution:** it should add a distinct major tradition, mode of reasoning, class of failure, or technical synthesis.
- **Complementarity:** it should add something not already supplied by a stronger retained work.
- **Comparative superiority:** it should survive comparison with plausible alternatives for one of the limited shelf positions.
- **Currency where required:** contemporary positions should synthesize current methods and live disputes.
- **Lineage discipline:** the same work should not recur mechanically across antecedent and descendant shelves.
- **No quota backfill:** deleting a weak or redundant work does not create an obligation to replace it merely to restore a preferred count.

For contemporary coverage, integrated authored or genuinely coauthored syntheses are preferred when they are comparably rigorous, current, comprehensive, and well fitted to the field. Edited handbooks remain appropriate when no authored treatment provides comparable coverage or when the field is inherently plural.

Bookshelf proliferation is checked by asking:

> **What distinct scrutiny or intellectual coverage does this additional volume contribute that the existing shelf does not?**

If that cannot be answered crisply, prune. Conversely, a short shelf should not remain artificially short when an important mature tradition or indispensable technical perspective is missing.

The governing standard is:

> **Enough to triangulate the field's strongest mature reasoning; no more than can be individually defended.**

### Antecedents, classics, and contemporaries

These roles are related but distinct.

**Antecedents** represent foundational viewpoints that helped constitute a discipline or characteristic mode of reasoning. Their role is intellectual genealogy. A work may be historically indispensable without remaining a good present-day review anchor.

**Classics** are field-shaping works whose principles remain operational for current adjudication even when parts of their apparatus are dated. They function as durable referral guides for important traditions, distinctions, or governing propositions.

**Contemporaries** provide current technical synthesis: present methods, evidence standards, live disputes, and the modern quality ceiling of the field.

The distinction is functional rather than chronological. An old work can remain a classic; a relatively recent work can eventually become antecedent-like in role; and fame alone does not determine placement.

When the same work appears to qualify as both antecedent and bookshelf classic, placement is adjudicated rather than duplicated mechanically:

- keep it as an **antecedent** when its main value is genealogical and stronger works govern present review;
- keep it as a **classic** at the narrowest appropriate field when its principles remain directly operational for current scrutiny;
- keep it in neither role when it fails the current standards for both.

A strong shelf will often combine classics and contemporaries so that durable intellectual traditions and current technical practice constrain one another.

## Review Workflow

The current core workflow in `review.txt` uses repeated independent runs to reduce dependence on any single panel composition or search path.

At a high level:

1. A system pre-scans the paper and identifies likely areas of scrutiny.
2. An assigning editor scopes the paper, selects reviewers, and assigns relevant literature.
3. Reviewers independently search for flaws and alternative interpretations.
4. A huddle performs depth review and attempts to resolve disputed flags.
5. A deciding editor audits the panel and finalizes the scorecard.
6. The process is repeated independently, and the union of surviving flags is carried into a final deciding run.

The scorecard is the handoff object. It should identify what the issue is, where it occurs, why it matters, and how it changes the strongest surviving claim.

The current prompt is economics-calibrated; the catalogue architecture is intended to support a later generalized routing stage using the selection logic above.

## Downstream Workflows

### Pre-submission mentorship: `preview.txt`

Takes the paper, scorecard, and criteria used and produces a constructive improvement brief. It does not issue a verdict or severity labels. The goal is to convert the review into concrete revision guidance.

### Editorial decision: `report.txt`

Takes the paper and completed scorecard and produces a final publication decision, synthesized rationale, editorial letter, and short author–editor exchange.

## Adaptation and House Style

The universal catalogue defines the underlying scholarly scrutiny. A journal, conference, discipline, laboratory, or research group can add a **house-style overlay** to express particular intellectual traditions, priorities, or fit criteria.

Such overlays may legitimately affect interpretation, emphasis, and venue fit. They should not change the underlying substantive scholarly standard or make a factual or methodological defect disappear.

In other words, different houses may reach different fit judgments while still agreeing on what survives the common scrutiny.

## Practical Principles

- **Pinpoint accuracy:** flags should identify exactly what is wrong, where it occurs, and why it matters.
- **Claim calibration:** review should narrow claims when necessary rather than treating every weakness as binary acceptance or rejection.
- **Method pluralism with rigor:** different disciplines and epistemic modes require different tests, not weaker tests.
- **Modularity:** anchors, fields, and portable modules can be recombined for hybrid work.
- **Auditability:** structural and substantive catalogue changes should be explicit and reviewable.
- **Human control:** PBPR is an aid to expert judgment, not a substitute for it.

## Disclaimer & Best Practices

* These tools are designed to **augment, not replace, human expertise**. It is highly recommended that this process be run in conjunction with traditional freeform human review. Pinpoint accuracy should simplify the location of flags in the original text.
* No warranties are offered or implied regarding the accuracy, validity, or publication outcomes resulting from these outputs. Ultimate responsibility for any editorial or submission decisions rests entirely with the human operator.
