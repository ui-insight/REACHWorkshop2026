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
  ├── slides-ai-literacy.html ─── Module 1 deck (Wiggins)
  ├── slides-data-lakehouse.html ── Module 2 deck (Layman)
  ├── slides-putting-it-to-work.html ─ Module 3 deck (Robison)
  │
  ├── presenters.html ─── Presenter bios and credentials
  ├── resources.html ─── Tools and external resources
  └── at-reach.html ─── REACH 2026 logistics
```

The workshop runs as three separate Reveal.js decks, not a continuous combined deck.

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

Picks up from the data governance foundation and asks: can you trust the output? Frames AI across the data lifecycle and the "human verification doesn't scale" problem (batch extraction, autonomous agents, continuous compliance triage). Four hands-on Vandalizer experiments on a canonical NSF Award Notice extraction prompt explore OCR quality as a tool property, cross-tool comparison, structured output enforcement, and replicate consensus, each backed by synthetic sponsor documents with ground truth. Follows with a provenance exercise on a real NSF solicitation, a context-layers decision rule, and a "Can you defend this number?" exercise whose reporting table traces every cell to a JSON field in a synthetic sponsored-research corpus. Closes with the adoption decision — automate, augment, or leave alone — plus REACH cross-references and workshop wrap-up.

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
  logos/       AI4RA, NSF, UI, SUU, FAIR, data-lake logos
  promptulus/  9 animal mascot icons (turtle, elephant, owl, parrot, etc.)
  presenters/  barrie-robison.jpg, nathan-layman.jpeg, nathan-wiggins.png
  diagrams/    Data model, architecture, and FAIR diagrams
  vandalizer/  Screenshots for the Module 3 Vandalizer exercise lightboxes
  (root)       ai4ra.png, workshop_QR_code.png, evaluation_survey.png
```

Additional images are hosted externally on `ai4ra.uidaho.edu` and referenced in slide decks.

## Interactive elements

- **Quiz** (slides-data-lakehouse) — "What is the most important model?" with 12 AI/ML model types. Single-select toggle, all wrong, reveals "The data model!"
- **Vandalizer experiment cards** (slides-putting-it-to-work) — Four experiment cards (OCR quality, cross-tool comparison, structured outputs, replicate consensus), each opening a lightbox with run instructions.
- **Lifecycle flip cards** (slides-putting-it-to-work) — Four cards across creation/extraction, cleaning, search, synthesis; click to flip to the Session 1/2 callback.
- **Promptulus character grid** (slides-ai-literacy) — 9 mascots representing tools in the AI4RA ecosystem.
