# peerreview

**LLM-Assisted Workflows for Top-Tier Academic Peer Review**

This repository contains advanced prompt architectures designed to simulate rigorous, multi-agent academic peer review processes. While the embedded criteria and specialized personas are currently calibrated for top-tier economics journals (e.g., *AER*, *QJE*, *Econometrica*), the modular design allows the framework to be easily adapted to other scientific disciplines.

## How It Works: The Core Engine

All workflows begin with **`review.txt`**. This prompt deploys a multi-agent panel (Assigning Editor, specialized Reviewers, consensus-building Huddles, and a Deciding Editor) to evaluate a manuscript against specific methodological and integrity criteria. 

The output of this initial run is an itemized, color-coded **Scorecard** of flagged concerns. Once you have the Scorecard, you can route it through one of two final workflows:

### Workflow A: Pre-Submission Mentorship (`review.txt` -> `preview.txt`)
*Designed for authors seeking constructive, pre-submission feedback.*
* **Process:** Feeds the Scorecard to a system acting as a senior Managing Editor, whose goal is to guide a hypothetical "Revise & Resubmit" toward an unconditional accept.
* **Output:** A detailed, actionable improvement roadmap. Recommendations are categorized by relevance (High/Medium/Low) and organized chronologically by paper section. 
* **Verdict:** No formal verdict or severity labels are offered. The focus is entirely on constructive, pinpoint-accurate revision guidance.

### Workflow B: Editorial Board Decision (`review.txt` -> `report.txt`)
*Designed to simulate a full, definitive editorial evaluation of a submitted manuscript.*
* **Process:** Feeds the Scorecard to a top-tier Managing Editor persona tasked with making a final publication call. 
* **Output:** Offers a definitive editorial decision (Accept, Revise with path to acceptance, Revise, Reject) along with a synthesized rationale, a formal editorial letter, and a simulated pushback correspondence with the author.

## Selecting the Review Criteria

`criteria.txt` is an overall catalogue, not a checklist to apply in full. A review should select the **minimal sufficient route** needed to subject the publication's claims to the strongest relevant scrutiny.

Selection proceeds compositionally:

1. **Always apply Integrity (I) and Quality (Q).** These are universal.
2. **Identify the precedence-bearing output.** Select the anchor according to what the publication asks reviewers to recognize as its successful contribution, not according to the type of warrant it happens to use: **F proves, E finds, S reconstructs, N justifies, D makes.**
3. **Select the home discipline and field.** The home discipline provides the publication's native/default scrutiny; the field contributes residual tests specific to that claim family. Choose by the contribution being made, not simply by departmental affiliation, dataset, method, or vocabulary. Use the General field where no narrower field supplies a better residual fit.
4. **Import auxiliary anchors and portable modules as required.** A publication may rely on several epistemic modes or specialized methods. Add the relevant auxiliary anchor(s) and portable modules—such as causal inference, decision analysis, experimental methods, measurement, machine learning, network analysis, optimization, qualitative methods, simulation, spatial analysis, survey research, or evidence synthesis—only where the claims actually require them.
5. **Tailor the route to the publication.** Omit irrelevant field criteria; add an ad hoc criterion when a material failure mode is not represented. The catalogue is deliberately extensible, and users are invited to adjust the selection to the publication and review purpose.

Selection changes the **kind** of scrutiny, not its rigor. No discipline, method, or publication type is entitled to a lower review standard, and routing should never be used to avoid an applicable test.

The bookshelves attached to anchors and fields are reference pools for the relevant traditions of scrutiny, not mandatory reading lists and not citation requirements.

## Selecting Catalogue Criteria and Bookshelf Works

The catalogue itself is curated rather than accumulated. Fields, criteria and bookshelves should be large enough to expose the mature scrutiny of a domain, but small enough that every retained element has a distinct job. There are useful compact ranges and proliferation checks, **not hard numerical quotas**.

### Criteria

A standing criterion belongs in the catalogue when it captures a **recurrent, material way in which a claim can fail, become overstated, or require narrowing**.

A candidate criterion should satisfy the following tests:

- **Residuality.** It adds scrutiny not already supplied by I/Q, the relevant anchor, an imported portable module, or a more general surviving criterion.
- **Recurrence.** It applies to a recognizable class of publications, not merely one paper or one unusual case.
- **Materiality.** Failure of the criterion can change the surviving claim, the scope of the claim, or the credibility of the publication.
- **Specificity.** It identifies a relation, distinction, boundary, correspondence, or failure mode that a reviewer can actually inspect.
- **Generality at the right level.** Put the test at the highest level at which it is genuinely general, but no higher. Universal tests belong in I/Q; epistemic-mode tests in anchors; cross-disciplinary machinery in portable modules; residual domain tests in disciplines and fields.
- **Orthogonality.** The criterion should not merely restate another criterion in different vocabulary.
- **Compactness without semantic loss.** Wording should be short enough to scan, but not compressed until distinct failure modes disappear.
- **Promotability.** A genuinely missing paper-specific test can first be added ad hoc. Repeated recurrence of the same ad hoc test is evidence that it deserves standing status.

Criterion proliferation is checked by asking:

> **What failure mode would become materially harder to detect or route if this criterion were removed?**

If no distinct answer exists, merge, rewrite, or delete it. A criterion should disappear only when another surviving test actually captures the same failure mode; thematic similarity or a “nearest surviving criterion” is not enough.

### Bookshelves

A bookshelf is a compact set of **top-line synthetic works that materially support the scrutiny represented by the anchor or field**. It is not a bibliography, a citation leaderboard, or a display of famous names.

A candidate work should satisfy the following tests:

- **Synthetic scope.** Prefer books, monographs, handbooks, collected-paper volumes, or comparable synthetic works. Isolated articles, conference papers, chapters and narrow technical notes belong at the research/review layer rather than on the standing shelf.
- **Criterion-generating relevance.** The work should illuminate multiple recurring failure modes, distinctions, or standards represented by the field. Mere subject-matter association is insufficient.
- **Mature scrutiny.** It should embody reasoning that is durable, authoritative, or especially rigorous for conducting or evaluating work in the field.
- **Coverage contribution.** It should add a distinct major tradition, mode of reasoning, class of failure, mature synthesis, or indispensable counterweight not already supplied by the shelf.
- **Field fit.** The relevant material must be central enough to the work that the volume genuinely belongs on that shelf.
- **Top-line quality.** Every retained work should be defensible as one of the strongest synthetic resources available for the purpose.
- **Classics and current work.** Durable classics and strong contemporary treatments are both eligible when they materially improve scrutiny. There is no recency quota and no classics quota.
- **Antecedent separation.** Works retained primarily because they helped constitute a discipline or tradition belong in the antecedent lineage, not automatically on a field shelf as well.
- **No quota backfill.** A deleted work does not require replacement merely to restore a preferred shelf size.

Bookshelf proliferation is checked by asking:

> **What distinct scrutiny or intellectual coverage does this additional volume contribute that the existing shelf does not?**

If that cannot be answered crisply, prune. Redundant prestige, near-substitutable textbooks, multiple works serving the same role, or works retained only for historical fame should not accumulate. Conversely, a short shelf should not be kept artificially short if a major mature tradition or indispensable synthetic perspective is missing.

The governing standard is:

> **Enough to triangulate the field's strongest mature reasoning; no more than can be individually defended.**

## Design Philosophy

* **Pinpoint-accurate:** The workflows are engineered to extract specific, actionable critiques based on embedded academic literature, anchored in the submitted manuscript and the relevant literature, avoiding generic LLM summarization.
* **Objective & Cordial:** Operates strictly on the merit of the text, maintaining a professional, senior-editorial tone free of bias.
* **Extensible:** The evaluation checklists—currently covering Overarching Quality, Causal Inference, Macroeconomics, Micro/IO, Game Theory, and Methods—can be swapped out for other fields while keeping the core agent workflow intact.
* **Modularizable:** The workflow can be run on a single LLM or distributed among multiple LLMs. Single-LLM runs will only simulate the division of tasks, so information bleeding cannot be fully ruled out. It is recommended to use separate sessions for the creation of the scorecard (`review.txt`) and the ultimate verdict (`preview.txt` or `report.txt`). This workflow can be harnessed in a multi-agent or multi-LLM environment.

## Disclaimer & Best Practices

* These tools are designed to **augment, not replace, human expertise**. It is highly recommended that this process be run in conjunction with traditional freeform human review. Pinpoint accuracy should simplify the location of flags in the original text.
* No warranties are offered or implied regarding the accuracy, validity, or publication outcomes resulting from these outputs. Ultimate responsibility for any editorial or submission decisions rests entirely with the human operator.
