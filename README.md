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

## Workshop roles — AI-enhanced data observability and analytics

**What's the most important model? The data model.** AI models come and go, but the way an institution organizes, governs, and shares its data determines whether any of them are useful. Two themes run through the entire workshop: **reproducibility** (can someone else get the same answer?) and **data organization** (is the underlying data trustworthy enough to act on?). Each role approaches these themes from a different angle. Presenters: Barrie Robison, Nate Layman, Nathan Wiggins — assignments TBD.

### Role 1 — AI and data science: what's what (1:00 – 1:50 PM)

Sets the foundation. Research analytics professionals already work with data — this section clarifies how AI changes the picture, where data science methods remain the right tool, and where human expertise is non-negotiable.

- **AI vs data science** — what each discipline actually contributes to research analytics, where they overlap, and where people conflate them
- **How LLMs work** — demystifying the technology for an analytics audience; how models generate text, where they succeed, and where they fail
- **Accuracy and its limits** — why LLM output is probabilistic, not deterministic; what that means for trust, verification, and when to rely on data science instead
- **Reproducibility in an AI context** — how non-deterministic outputs challenge traditional reproducibility standards, and what disciplines help
- **Where human expertise remains essential** — which analytic judgments resist automation and why that matters
- **Distinguishing AI tasks from data science tasks** — practical guidance for deciding which method fits which problem

### Role 2 — The data lakehouse and data organization (2:00 – 2:50 PM) — Nate Layman

Shows how institutional data becomes observable, governed, and AI-ready. Good data organization is the prerequisite for both reproducible analytics and trustworthy AI — this section covers the infrastructure and shared standards that make it possible.

- **The data lakehouse** — what it is, how it differs from traditional warehouses and data lakes, and why it matters for research analytics
- **The Unified Data Model** — a shared schema for research administration that makes institutional data interoperable and AI-ready across the GRANTED network
- **Data observability** — making institutional data visible, traceable, and auditable so analytics teams and AI systems can trust what they're working with
- **Data governance as prerequisite** — why provenance, permissions, and quality determine whether AI is safe to use on your data
- **From messy to structured** — cleaning, curating, and organizing institutional data so it can serve as trustworthy context for both analytics and AI workflows
- **Reproducibility through organization** — how shared schemas, versioned data, and governed pipelines make analytics reproducible across institutions and over time
- **Live demo: Promptulus** — participants compare prompt strategies and see how structure changes output quality and reproducibility

### Role 3 — Reproducibility, accuracy, and putting it to work (3:00 – 3:50 PM)

Returns to the central questions: can you reproduce the result, can you verify the accuracy, and should you deploy it? Combines hands-on AI skills with the practical judgment needed to adopt these ideas at your own institution.

- **Prompt engineering and context** — structuring requests and layering context to get reproducible, reviewable output from AI models
- **Evaluating accuracy** — practical methods for judging whether AI output is correct, consistent, and safe to act on
- **From data to action** — how observable, governed data connects to analytics pipelines, reporting, and AI-assisted decision-making
- **Adoption and institutional fit** — a decision framework for what to automate, what to augment, and what still needs a human
- **Live demo: Vandalizer** — participants use the AI-powered tool to see how well-organized institutional data enables streamlined RA workflows
- **Lessons from the GRANTED project** — what the AI4RA NSF project revealed about deploying AI and shared data infrastructure across institutions
- **Discussion and feedback** — what participants need at their institutions, and what governance work has to happen before expanding AI or automation

### Timeline

| Time | Role | Theme |
|------|------|-------|
| 1:00 – 1:50 PM | Role 1 | AI and data science: what's what |
| 1:50 – 2:00 PM | — | Break |
| 2:00 – 2:50 PM | Nate Layman | The data lakehouse and data organization |
| 2:50 – 3:00 PM | — | Break |
| 3:00 – 3:50 PM | Role 3 | Reproducibility, accuracy, and putting it to work |
| 3:50 – 4:00 PM | All | Wrap-up and Q&A |

## Site structure

| File | Purpose |
|------|---------|
| `index.html` | Workshop home — objectives, agenda, topic threads, session details |
| `course-content.html` | Teaching modules with lecture framing, worked examples, and speaker notes |
| `slides-governance.html` | Reveal.js slide deck for the data governance module |
| `slides-context-layers.html` | Reveal.js slide deck for the context layers module |
| `presenters.html` | Presenter bios and credentials |

## Local preview

```bash
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173`.

## Deployment

This site is designed for branch-based GitHub Pages deployment from the root of the `main` branch. Add `.nojekyll` to keep GitHub Pages from trying to process the site with Jekyll.
