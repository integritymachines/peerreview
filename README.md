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

## Design Philosophy

* **Pinpoint-accurate:** The workflows are engineered to extract specific, actionable critiques based on embedded academic literature, anchored in the submitted manuscript and the relevant literature, avoiding generic LLM summarization.
* **Objective & Cordial:** Operates strictly on the merit of the text, maintaining a professional, senior-editorial tone free of bias.
* **Extensible:** The evaluation checklists—currently covering Overarching Quality, Causal Inference, Macroeconomics, Micro/IO, Game Theory, and Methods—can be swapped out for other fields while keeping the core agent workflow intact.
* **Modularizable:** The workflow can be run on a single LLM or distributed among multiple LLMs. Single-LLM runs will only simulate the division of tasks, so information bleeding cannot be fully ruled out. It is recommended to use separate sessions for the creation of the scorecard (`review.txt`) and the ultimate verdict (`preview.txt` or `report.txt`). This workflow can be harnessed in a multi-agent or multi-LLM environment.

## Disclaimer & Best Practices

* These tools are designed to **augment, not replace, human expertise**. It is highly recommended that this process be run in conjunction with traditional freeform human review. Pinpoint accuracy should simplify the location of flags in the original text.
* No warranties are offered or implied regarding the accuracy, validity, or publication outcomes resulting from these outputs. Ultimate responsibility for any editorial or submission decisions rests entirely with the human operator.
