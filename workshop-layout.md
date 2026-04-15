# Workshop Layout Overview

## Site map

```
index.html ─── Workshop home (agenda, themes, session details)
  │
  ├── course-content.html ─── Course hub (module directory + template)
  │     ├── module-foundational.html ─── Module 1 facilitator guide
  │     ├── module-data-governance.html ── Module 2 facilitator guide
  │     └── module-context-layers.html ── Module 3 facilitator guide
  │
  ├── slides.html ─── Slide deck directory
  │     ├── slides-workshop.html ──── Full 3-hour deck (continuous)
  │     ├── slides-ai-literacy.html ─ Session 1 deck
  │     ├── slides-data-lakehouse.html ─── Session 2 deck
  │     └── slides-putting-it-to-work.html Session 3 deck
  │
  ├── presenters.html ─── Presenter bios and credentials
  └── governance-checklist.html ─── Context readiness checklist handout
```

## Session schedule

| Time | Session | Presenter | Module page | Slide deck |
|------|---------|-----------|-------------|------------|
| 1:00–1:50 | The intersection between AI and data science | Nathan Wiggins | module-foundational.html | slides-ai-literacy.html |
| 2:00–2:50 | The data lakehouse and data organization | Nathan Layman | module-data-governance.html | slides-data-lakehouse.html |
| 3:00–3:50 | Reproducibility, accuracy, and putting it to work | Barrie Robison | module-context-layers.html | slides-putting-it-to-work.html |

## Session flow and handoffs

### Session 1 — The intersection between AI and data science (Nathan Wiggins)

Broad overview of AI for research administration. Introduces AI4RA, clarifies where data science ends and AI begins, shows how LLMs work, and frames the spectrum from prompt engineering to automation. Covers why human judgment stays in the loop and where AI fits institutional work. Closes with a **Promptulus demo** showing how prompt structure affects output quality — leading participants directly into Session 2's question: what about the data underneath?

### Session 2 — The data lakehouse and data organization (Nathan Layman)

Opens with the interactive quiz — "What is the most important model?" — and reveals the answer: **the data model**. Builds the case that AI is only as good as the data infrastructure underneath it. Covers data lakehouses, medallion architecture, the Unified Data Model, governance, and context readiness. Participants audit whether their institutional data is trustworthy enough for AI. Closes with a **Vandalizer demo** (led by Barrie Robison) showing how well-organized data powers real RA workflows — bridging into Session 3.

### Session 3 — Reproducibility, accuracy, and putting it to work (Barrie Robison)

Picks up from the Vandalizer demo and asks: can you trust the output? Covers context engineering layers, evaluation and accuracy verification, prompt engineering techniques, and lessons from the GRANTED project. Ends with the practical adoption decision — what to automate, what to augment, and what to leave alone — plus discussion, REACH cross-references, and workshop wrap-up.

### Demo handoff pattern

| End of session | Demo | Bridge question |
|---|---|---|
| Session 1 → 2 | **Promptulus** (prompt strategies) | "But what about the data underneath?" |
| Session 2 → 3 | **Vandalizer** (governed data in action) | "Can you trust the output?" |

## Content flow per module

Each module page follows the same anatomy:

1. **Module brief** — Learning goal, in-room move, key distinction, participant artifact
2. **Teaching flow** — Core explanation, research analytics lens, teaching sequence
3. **Example and activity** — Worked scenario, participant exercise, discussion prompts
4. **Facilitation support** — Speaker notes, complementary REACH sessions, bridge forward
5. **Derived assets** — Links to slide deck, handouts, adjacent modules

Each slide deck is a condensed version of its module page, not a separate source of content.

## Image assets

```
img/
  logos/       ai4ra-logo.png, nsf-logos.webp, ui-full-color.webp, suu-birdhead.webp
  promptulus/  9 animal mascot icons (turtle, elephant, owl, parrot, etc.)
  presenters/  barrie-robison.jpg, nathan-layman.jpeg, nathan-wiggins.png
  diagrams/    data-model.png
```

8 additional images are hosted externally on `ai4ra.uidaho.edu` and referenced in slide decks.

## Interactive elements

- **Quiz** (slides-data-lakehouse, slides-workshop) — "What is the most important model?" with 12 AI/ML model types. Single-select toggle, all wrong, reveals "The data model!"
- **Context slider** (slides-putting-it-to-work, slides-workshop) — Draggable slider showing context window capacity across 4 disciplines, with preset buttons
- **Promptulus character grid** (slides-ai-literacy, slides-workshop) — 9 mascots representing tools in the AI4RA ecosystem
