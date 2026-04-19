# AI4RA: The Intersection Between AI and Data

**WA3 — REACH 2026 Workshop**
Monday, April 20, 2026 · 1:00 PM – 4:00 PM · Room BRISTOL · 24 seats

Live site: <https://ui-insight.github.io/REACHWorkshop2026/>

## Abstract

Artificial intelligence and data science are transforming research administration and other fields in higher education, creating new opportunities for efficiency, insight, and strategic decision-making. "AI4RA – The Intersection Between AI and Data" is an engaging workshop designed to help participants understand how AI and data science work together to support actionable, human-centered applications — ranging from personal workflow improvements to institution-wide planning and strategy. The workshop covers the relationship between data science and AI, clarifies how each contributes to informed decision-making while highlighting where human expertise remains essential, and provides practical guidance for distinguishing tasks best suited for AI-powered approaches versus data science methods. Lessons learned from the AI4RA NSF GRANTED project are woven throughout.

## Mission

Help research administration professionals build safer, more relevant, and more inspectable AI-assisted workflows at their own institutions. The workshop frames AI and data science as complementary tools, shows where human expertise remains essential, and gives participants a grounded way to design reviewable workflows rather than black-box experiments.

## Learning objectives

- Understand what AI can and cannot do for research analytics
- Structure prompts that produce reliable, consistent output
- Evaluate whether institutional data is ready for AI
- Govern AI inputs and outputs with the same rigor as dashboards
- Choose the right layer of context for the job
- Verify AI output before it enters a workflow
- Decide what to automate, augment, or leave alone

## Workshop modules

**Workshop thesis: "What's the most important model? Your data model."** Two themes run through all three modules: **reproducibility** (can someone else get the same answer?) and **data organization** (is the underlying data trustworthy enough to act on?).

| Time | Module | Presenter | Affiliation |
|------|--------|-----------|-------------|
| 1:00 – 1:50 PM | The intersection between AI and data science | Nathan Wiggins | Southern Utah University |
| 2:00 – 2:50 PM | The data lakehouse and data organization | Nathan Layman | University of Idaho |
| 3:00 – 3:50 PM | Reproducibility, accuracy, and putting it to work | Barrie Robison | University of Idaho |

### Module 1 — The intersection between AI and data science (Nathan Wiggins)

Broad overview of AI for research administration. Introduces the AI4RA community of practice and its ecosystem (Vandalizer, Data Lakehouse, Promptulus). Covers how LLMs work at a practical level, FAIR data principles as operational guardrails, accuracy and reproducibility challenges, the three zones of AI appropriateness, and decision frameworks for when to use AI versus when human judgment must lead. Introduces prompt engineering and the shift toward context engineering. (~25 slides with interactive elements.)

**Key topics:** AI4RA introduction, community of practice ecosystem, how LLMs actually work (token prediction, attention, next-token probability), FAIR principles, accuracy and hallucination, three zones of intent, prompt-to-intent engineering, context engineering fundamentals.

**Demo:** Promptulus (interactive prompt engineering trainer with 9 animal characters).

### Module 2 — The data lakehouse and data organization (Nathan Layman)

Opens with the interactive quiz — "What is the most important model?" — and reveals the answer: the data model. Builds the case that AI is only as good as the data infrastructure underneath it. Introduces the Universal Data Model (UDM) for research administration and shows how source data maps to it. Covers data warehouse vs. data lake vs. data lakehouse architectures, the eight capabilities of a lakehouse, and the GRANTED project's open-source implementation (Shipyard, Marina, MinIO, Polaris, Trino). Walks through the medallion architecture (Bronze/Silver/Gold/Platinum) with a worked example tracing data from source to application. Covers AI-assisted data ingestion, data governance as a prerequisite for AI, observability, and context readiness. (~23 slides with interactive quiz, toggle comparisons, flip cards, UDM translation table, trust rater, and context readiness checklist.)

**Key topics:** Universal Data Model, medallion architecture, eight lakehouse capabilities, GRANTED architecture, AI-assisted adapter mapping (Suggest All / Fill Tree / Write SQL), data governance, observability, source trust, context readiness.

**Interactive activity:** Context readiness checklist (embedded in the module).

### Module 3 — Reproducibility, accuracy, and putting it to work (Barrie Robison)

Picks up from the data governance foundation and asks: can you trust the output? Opens with AI across the data lifecycle (extraction, cleaning, search, synthesis) and the "human verification doesn't scale" problem, with three concrete shapes (batch extraction, autonomous agents on live data, continuous compliance triage). Moves into four hands-on evaluation experiments using a canonical NSF Award Notice extraction prompt and synthetic workshop documents: OCR quality as a tool-level property, cross-tool comparison, structured output enforcement, and replicate consensus. Adds a provenance exercise on a real NSF solicitation using the RFP extraction prompt from the AI4RA prompt library, a context-layers decision rule, and a "Can you defend this number?" exercise where every cell in the reporting table traces to a JSON field in a synthetic sponsored-research corpus. Closes with the adoption decision framework (automate / augment / leave alone), institutional-fit discussion, and "Monday morning" takeaways. (~25 slides.)

**Key topics:** AI data lifecycle risks, human verification at scale, extraction evaluation (OCR tool comparison, cross-tool model comparison, schema enforcement, replicate consensus), provenance and auditability, context layer decision rule, defensible analytics claims, adoption framework.

**Demo and materials:** Vandalizer evaluation experiments against synthetic Notice-of-Award and Subaward PDFs with full ground truth; RFP extraction against a real NSF solicitation. Prompts and schemas are pulled from the public [AI4RA prompt library](https://github.com/AI4RA/prompt-library).

## Current status

The companion site is live on GitHub Pages with all three modules fully built out: slide decks, facilitator guides, presenter bios, resources, synthetic-document materials for the Module 3 exercises, and the AI4RA prompt library references.

For current work, open issues, and anything in flight, check the issue tracker:

```bash
gh issue list --state open
```

A bulleted status checklist used to live here; it drifted faster than the issues themselves, so the pointer replaces it.

## Presenters

| Name | Affiliation | Role | Module |
|------|-------------|------|--------|
| Nathan Wiggins | Southern Utah University | Data Scientist, SPARC Office | Module 1: The intersection between AI and data science |
| Nathan Layman | University of Idaho | Data Scientist, AI4RA project | Module 2: Data lakehouse and organization |
| Barrie Robison | University of Idaho | Professor of Biology, Director IIDS | Module 3: Putting it to work |

## Repo structure

```
REACHWorkshop2026/
  CLAUDE.md                        Project instructions for Claude Code
  README.md                        This file
  workshop-layout.md               Session flow, demo handoffs, interactive elements
  audience-profile-anon.md         Anonymized registrant profile
  docs/                            GitHub Pages source — the live site
    index.html                     Workshop home page
    course-content.html            Session hub and module directory
    presenters.html                Presenter bios and credentials
    resources.html                 Tools and resources page
    at-reach.html                  REACH 2026 logistics
    ai4ra-workshop.ics             Calendar invite
    module-foundational.html       Module 1 facilitator guide
    module-data-governance.html    Module 2 facilitator guide
    module-context-layers.html     Module 3 facilitator guide
    slides-ai-literacy.html        Module 1 Reveal.js deck (Wiggins)
    slides-data-lakehouse.html     Module 2 Reveal.js deck (Layman)
    slides-data-lakehouse-outline.md  Outline source for the data lakehouse deck
    slides-putting-it-to-work.html Module 3 Reveal.js deck (Robison)
    slides-interactive.js          Shared interactive slide behaviors
    styles.css                     Site stylesheet
    slides.css                     Slide deck theme
    app.js                         Scroll animation observer
    js/                            Additional page scripts
    files/                         Downloadable workshop materials
      workshop_ocr/                Synthetic sponsor PDFs + ground truth for Module 3 exercises
      prompts/                     Prompts and JSON schemas from AI4RA/prompt-library
      *.pdf / *.csv / *.xlsx       NSF award notices, FBU budget docs, synthetic records
    img/
      logos/                       AI4RA, NSF, UI, SUU, FAIR, data-lake logos
      promptulus/                  Promptulus animal mascot icons
      presenters/                  Presenter headshots
      diagrams/                    Data model, architecture, FAIR diagrams
      vandalizer/                  Screenshots for Vandalizer exercise lightboxes
    reveal/dist/                   Reveal.js library
  resources/                       Reference materials (not served)
```

## Related repos

| Repo | Description |
|------|-------------|
| [ui-insight/lakehouse](https://github.com/ui-insight/lakehouse) | Open-source data lakehouse for research administration |
| [ui-insight/vandalizer](https://github.com/ui-insight/vandalizer) | AI-powered document review workflow tool |
| [nate-layman/promptulus](https://github.com/nate-layman/promptulus) | Interactive AI literacy and prompt engineering trainer |
| [ai4ra.uidaho.edu](https://ai4ra.uidaho.edu) | AI4RA community of practice blog and resources |

## Local preview

```bash
python3 -m http.server 4173 -d docs
```

Then open `http://127.0.0.1:4173`.

## Deployment

GitHub Pages, served from the `docs/` folder on the `main` branch. Configure in repo settings: Settings → Pages → Source → `/docs`.
