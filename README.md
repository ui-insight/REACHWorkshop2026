# AI4RA: The Intersection Between AI and Data

**WA3 — REACH 2026 Workshop**
Monday, April 20, 2026 · 1:00 PM – 4:00 PM · Room BRISTOL · 24 seats

## Abstract

Artificial intelligence and data science are transforming research administration and other fields in higher education, creating new opportunities for efficiency, insight, and strategic decision-making. "AI4RA – The Intersection Between AI and Data" is an engaging workshop designed to help participants understand how AI and data science work together to support actionable, human-centered applications—ranging from personal workflow improvements to institution-wide planning and strategy. The workshop will include a thorough exploration of the relationship between data science and AI, casting clarity on how each contributes to informed decision-making while also highlighting where human expertise remains essential. The session will also provide practical guidance for distinguishing between tasks best suited for AI-powered approaches versus those more effectively addressed through data science methods, and review lessons learned from the AI4RA NSF GRANTED project. To reinforce these concepts, attendees will have the opportunity to access and use a temporary demo version of Vandalizer, an AI-powered tool built to streamline and enhance research administration workflows.

## Mission

Help research administration professionals build safer, more relevant, and more inspectable AI-assisted workflows at their own institutions. The workshop frames AI and data science as complementary tools, shows where human expertise remains essential, and gives participants a grounded way to design reviewable workflows rather than black-box experiments.

## Learning objectives

- Apply prompt engineering fundamentals to improve quality, relevance, and consistency in AI responses
- Break complex RA tasks into discrete, AI-manageable components with review points
- Develop complete AI-assisted workflows for common research administration processes
- Evaluate which tasks and workflows are suitable for AI deployment at participants' own institutions

## Workshop sessions

**What's the most important model? The data model.** Two themes run through the entire workshop: **reproducibility** (can someone else get the same answer?) and **data organization** (is the underlying data trustworthy enough to act on?).

| Time | Session | Presenter |
|------|---------|-----------|
| 1:00 – 1:50 PM | Session 1: AI and data science — what's what | Nathan Wiggins |
| 2:00 – 2:50 PM | Session 2: The data lakehouse and data organization | Nathan Layman |
| 3:00 – 3:50 PM | Session 3: Reproducibility, accuracy, and putting it to work | Barrie Robison |

**Session 1 — AI and data science: what's what (Nathan Wiggins)**
Broad overview of AI for research administration. Introduces AI4RA, clarifies where data science ends and AI begins, shows how LLMs work, and frames the spectrum from prompt engineering to automation. Covers why human judgment stays in the loop and where AI fits institutional work. Closes with a **Promptulus demo** showing how prompt structure affects output quality — leading participants directly into Session 2's question: what about the data underneath?

**Session 2 — The data lakehouse and data organization (Nathan Layman)**
Opens with the interactive quiz — "What is the most important model?" — and reveals the answer: the data model. Builds the case that AI is only as good as the data infrastructure underneath it. Covers data lakehouses, medallion architecture, the Unified Data Model, governance, and context readiness. Closes with a **Vandalizer demo** (led by Barrie Robison) showing how well-organized data powers real RA workflows — bridging into Session 3.

**Session 3 — Reproducibility, accuracy, and putting it to work (Barrie Robison)**
Picks up from the Vandalizer demo and asks: can you trust the output? Covers context engineering layers, evaluation and accuracy verification, prompt engineering techniques, and lessons from the GRANTED project. Ends with the practical adoption decision — what to automate, what to augment, and what to leave alone — plus discussion, REACH cross-references, and workshop wrap-up.

## Repo structure

```
REACHWorkshop2026/
  CLAUDE.md              Project instructions for Claude Code
  README.md              This file
  docs/                  GitHub Pages source — the live site
    index.html           Workshop home page
    course-content.html  Course hub and module directory
    slides.html          Slide deck directory
    presenters.html      Presenter bios and credentials
    governance-checklist.html  Context readiness checklist handout
    module-foundational.html       Module 1 facilitator guide
    module-data-governance.html    Module 2 facilitator guide
    module-context-layers.html     Module 3 facilitator guide
    slides-workshop.html           Full 3-hour Reveal.js deck
    slides-foundational.html       Session 1 Reveal.js deck
    slides-governance.html         Session 2 Reveal.js deck
    slides-context-layers.html     Session 3 Reveal.js deck
    styles.css             Site stylesheet
    slides.css             Slide deck theme
    app.js                 Scroll animation observer
    img/
      logos/              AI4RA logo, NSF, UI, SUU logos
      promptulus/         Promptulus animal mascot icons
      presenters/         Presenter headshots
      diagrams/           Data model diagram
    reveal/dist/          Reveal.js library
  resources/             Reference materials (not served)
```

## Local preview

```bash
python3 -m http.server 4173 -d docs
```

Then open `http://127.0.0.1:4173`.

## Deployment

GitHub Pages, served from the `docs/` folder on the `main` branch. Configure in repo settings: Settings → Pages → Source → `/docs`.
