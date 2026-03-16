# Draft: Intent Engineering section for "AI Has a Page Limit"

This is a draft expansion to add **intent engineering** as the foundational discipline in the blog post's framework. It should precede the existing sections on prompt engineering, context engineering, and conversation management.

---

## Before the Prompt: Intent Engineering

Before you write a prompt, curate context, or manage a conversation, there is a prior question: **what are you actually trying to accomplish, and does the process matter as much as the result?**

This is intent engineering — the discipline of deciding **how the work should be done** and whether there are **escape hatches** when the AI path fails. It is not a technical skill. It is a judgment skill, and research administrators already practice it every day.

### Two questions that determine everything

**1. How should this work be done?**

Consider two tasks that sound similar:

- "Summarize the budget justification for this proposal."
- "Verify that the budget justification complies with the sponsor's cost principles."

The first is output-driven. If the summary is accurate and complete, nobody asks how it was produced. The second is process-critical. A compliance determination requires traceable reasoning, human accountability, and the ability to reproduce the analysis exactly. Using AI to lead the second task doesn't just risk inaccuracy — it undermines the purpose of the task itself.

**2. Are there escape hatches?**

Every AI-assisted workflow should have a defined path for what happens when the AI fails, gives unreliable output, or encounters something outside its scope. An escape hatch is a pre-planned answer to: *if this doesn't work, what do we do instead?*

- Can a human complete the task manually without starting over?
- Is there a fallback tool (a script, a query, a spreadsheet) that produces the same result transparently?
- Does the workflow degrade gracefully, or does an AI failure become a process failure?

If there is no escape hatch — if the workflow has no path that doesn't run through the AI — then the task is not ready for AI, regardless of how well the model performs today. Models change, APIs go down, and outputs degrade without warning. Intent engineering means designing the fallback before you need it.

Intent engineering is the practice of asking these questions deliberately before touching any AI tool: **how should this work be done, and what happens when the AI path fails?**

### Intent shapes every downstream decision

Once you understand the intent, the other three disciplines fall into place:

| Discipline | What intent determines |
|---|---|
| **Prompt engineering** | Whether the instructions need to enforce auditability, or just accuracy |
| **Context engineering** | Whether the assembled information needs to include provenance and version history, or just content |
| **Conversation management** | Whether the interaction needs to be preserved as a record, or can be discarded after the output is validated |

A process-critical task might still use AI — but the intent tells you it belongs in a human-in-the-loop workflow where the AI prepares and the human decides. An output-driven task can let the AI lead, with spot-checks for quality. The intent is what makes that distinction visible before you start.

### Three zones of intent

The intent behind any research administration task falls into one of three zones:

1. **Process-critical** — The value is in demonstrating *how* the work was done and *who* was responsible. Every step must be auditable and reproducible. AI is disqualified from leading; transparent tools (scripts, queries, spreadsheets) are the right choice. AI may assist, but a human must own the reasoning.

2. **Human-in-the-loop** — AI contributes meaningfully, but a qualified person must review and sign off. The intent requires human judgment at the decision point, even if AI handles the preparation. This is where context engineering matters most: giving the AI the right information so the human reviewer gets useful, well-grounded output to evaluate.

3. **Output-driven** — Only the final product matters. If it is accurate and complete, the method is irrelevant. AI can lead, but accuracy must be validated through spot-checks and error-rate tracking over time.

### Intent takes up space in the context window — and it should

Intent engineering is not just a planning exercise you do before opening the AI tool. Intent is part of the context window itself. When you tell the model what kind of task this is, what standards the output must meet, what the fallback is if the output isn't usable, and what the human reviewer needs to see — that is intent, and it occupies real space in the page limit.

This is a good trade. The blog's original framework described three things competing for finite context window space: instructions, information, and conversation. Intent is a fourth. It competes for the same space, and it earns it by making the other three more efficient:

| Context window component | Without intent | With intent |
|---|---|---|
| **Instructions** | Generic prompting — "be accurate, be thorough" — that doesn't match the task | Targeted instructions shaped by what the task actually requires |
| **Information** | Everything uploaded, hoping the model finds what matters | Only the documents and data that serve the specific intent |
| **Conversation** | Drifts as the user figures out what they actually wanted mid-stream | Stays focused because the purpose was defined before the first message |
| **Intent** | Absent — the model guesses what the user needs | Present — the model knows what kind of output, what standards, what fallback |

Without intent, people waste context window space on instructions that don't match the task, documents that don't serve the goal, and conversation turns that wander because the purpose was never stated. Intent engineering fixes this not by optimizing the prompt, but by making sure the right task is in front of the AI in the first place.

A process-critical task doesn't need a more sophisticated prompt — it needs a different tool entirely, and stating that intent saves the context window for work the AI can actually do. A human-in-the-loop task needs context that supports the reviewer, not just the model — and that choice is driven by intent. An output-driven task can dedicate the full window to quality, because auditability isn't the goal.

Intent is not overhead. It is the most efficient use of context window space, because every other token in the window becomes more useful when the model knows what it's working toward.

### The updated framework

The blog's framework expands from three disciplines to four, and the context window now has four components competing for the same finite space:

| Discipline | Optimizes | Context window component | Research Admin Analogy |
|---|---|---|---|
| **Intent engineering** | The purpose: what you are trying to accomplish, what accountability it requires, and what the escape hatch is | Intent declarations, task boundaries, fallback rules | Deciding whether a task is a compliance determination or a drafting exercise before you start working |
| **Prompt engineering** | The instructions: how you phrase the request and define the task | System prompts, role definitions, output format rules | Writing to a sponsor's FOA requirements |
| **Context engineering** | The information: what documents, data, and knowledge the model can see | Uploaded files, retrieved data, institutional knowledge | Assembling supporting documents for a proposal |
| **Conversation management** | The interaction: when to continue, reset, and how to keep the window balanced | Message history, summaries, turn management | Managing back-and-forth with a program officer |

Intent engineering is the foundation. It determines how much the other three disciplines matter, what form they should take, and how much context window space each one deserves for any given task.

---

*This section should be inserted before the current "Prompt Engineering" section in the blog post, reframing the three existing disciplines as downstream of intent.*
