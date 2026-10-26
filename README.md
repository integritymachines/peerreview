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

## Design Philosophy

* **Pinpoint-accurate:** The workflows are engineered to extract specific, actionable critiques based on embedded academic literature, anchored in the submitted manuscript and the relevant literature, avoiding generic LLM summarization.
* **Objective & Cordial:** Operates strictly on the merit of the text, maintaining a professional, senior-editorial tone free of bias.
* **Extensible:** The evaluation checklists—currently covering Overarching Quality, Causal Inference, Macroeconomics, Micro/IO, Game Theory, and Methods—can be swapped out for other fields while keeping the core agent workflow intact.
* **Modularizable:** The workflow can be run on a single LLM or distributed among multiple LLMs. Single-LLM runs will only simulate the division of tasks, so information bleeding cannot be fully ruled out. It is recommended to use separate sessions for the creation of the scorecard (`review.txt`) and the ultimate verdict (`preview.txt` or `report.txt`). This workflow can be harnessed in a multi-agent or multi-LLM environment.

## Disclaimer & Best Practices

* These tools are designed to **augment, not replace, human expertise**. It is highly recommended that this process be run in conjunction with traditional freeform human review. Pinpoint accuracy should simplify the location of flags in the original text.
* No warranties are offered or implied regarding the accuracy, validity, or publication outcomes resulting from these outputs. Ultimate responsibility for any editorial or submission decisions rests entirely with the human operator.
