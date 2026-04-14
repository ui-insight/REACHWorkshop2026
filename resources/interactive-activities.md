# Interactive Activities — Session 2 (Data Lakehouse)

Three activities in sequence: first show the power of AI-assisted analytics, then show the full pipeline (query + narrative + source data), then reveal how data quality silently undermines everything.

---

## Activity 1: AI-Assisted Exploratory Data Analysis

**Concept:** Show the audience how an LLM can do in 60 seconds what takes hours in Excel — summarize trends, identify top sponsors, flag outliers, and answer ad hoc questions about a research portfolio. Start with the "wow" moment.

### Setup

A realistic awards table (~15 rows) representing a small institution's portfolio. The data looks normal at first glance — the quality issues are there but not obvious.

| Award_ID | PI_Name | Department | Sponsor | Sponsor_Type | Amount | Start_Date | End_Date |
|----------|---------|------------|---------|--------------|--------|------------|----------|
| A-001 | Martinez | Biology | NSF | Federal | 450,000 | 2024-09-01 | 2027-08-31 |
| A-002 | Chen | | NIH | Federal | 1,200,000 | 2023-07-01 | 2026-06-30 |
| A-003 | Okafor | Engineering | DOE | Federal | 680,000 | 2025-01-15 | 2027-12-31 |
| A-004 | Patel | Chemistry | | | 320,000 | 2024-03-01 | |
| A-005 | Johnson | | NSF | Federal | 550,000 | 2024-06-01 | 2027-05-31 |
| A-006 | Williams | Psychology | NIMH | Federal | 890,000 | 2023-01-01 | 2025-12-31 |
| A-007 | Kim | | Pfizer | Industry | 275,000 | 2025-04-01 | 2026-03-31 |
| A-008 | Thompson | Biology | USDA | Federal | 410,000 | 2024-11-01 | 2027-10-31 |
| A-009 | Garcia | | | | 150,000 | | 2026-09-30 |
| A-010 | Lee | Computer Science | NSF | Federal | 725,000 | 2025-02-01 | 2028-01-31 |
| A-011 | Davis | | NIH | Federal | 980,000 | 2024-08-15 | 2027-07-31 |
| A-012 | Robinson | Engineering | Boeing | Industry | 185,000 | 2025-06-01 | 2026-05-31 |
| A-013 | Nguyen | Physics | DOE | Federal | 560,000 | 2023-10-01 | 2026-09-30 |
| A-014 | Brown | | Gates Foundation | Nonprofit | 1,500,000 | 2024-01-01 | 2028-12-31 |
| A-015 | Miller | Sociology | | | 95,000 | 2025-03-15 | 2026-03-14 |

**Hidden data quality issues (don't reveal yet):**
- 5 of 15 rows missing Department (33%)
- 3 rows missing Sponsor_Type
- 2 rows missing Sponsor entirely
- 2 rows missing Start_Date or End_Date

### Prompt sequence

**Prompt 1 — The "wow" moment**

> "Summarize this awards portfolio. What are the key trends?"

Expected AI behavior: Instant, impressive summary. Total funding, average award size, top sponsors (NSF appears 3 times), department distribution, active vs. expiring awards. The audience sees real value — this is useful, fast, and something they'd actually want.

**Prompt 2 — Go deeper**

> "Which departments have the strongest funding? Who are the top PIs? Are there any awards expiring in the next 12 months?"

Expected AI behavior: Rankings, comparisons, timeline analysis. It handles follow-up questions conversationally. This is the sales pitch for AI-assisted analytics — no SQL, no pivot tables, just questions and answers.

**Prompt 3 — The question a VP would ask**

> "If I needed to cut 20% of our portfolio, which awards would you recommend and why?"

Expected AI behavior: It gives a reasoned answer — probably targets the smallest awards or those near expiration. The audience sees AI doing strategic analysis, not just summarization. Impressive and a little unsettling.

### Discussion prompt

> "How long would this take you today with your current tools?"

Let the room react. The point isn't that AI replaces analysts — it's that it dramatically accelerates exploratory work. But hold that thought...

---

## Activity 2: The Full Pipeline — SQL, Data, and Narrative

**Concept:** Show the audience what's actually happening behind the scenes. The AI doesn't just summarize — it writes a query, fetches data, and generates a narrative. Display all three side by side so the audience can verify each step.

### Setup

Use the same dataset from Activity 1. This time, ask the AI to produce a structured report and show its work.

### Prompt sequence

**Prompt 4 — "Write the VP's report"**

> "Write a one-paragraph executive summary of federal funding by department for the VP of Research. Show me the SQL query you would use to pull this data."

**Three-panel display:**

| Panel | What it shows |
|-------|--------------|
| **SQL query** | The generated query — e.g., `SELECT Department, SUM(Amount) FROM awards WHERE Sponsor_Type = 'Federal' GROUP BY Department` |
| **Result set** | The rows returned by that query |
| **Narrative** | The polished executive summary |

### What the audience should notice

**In the SQL:**
- Does the query handle `NULL` departments? (Probably not — they'll silently drop out of the `GROUP BY`.)
- Does it know NIMH is federal? (Depends on whether it relies on `Sponsor_Type` or `Sponsor` name.)
- Is there a `WHERE End_Date > NOW()` to filter active awards, or does it include expired ones?

**In the result set:**
- Only departments with values appear. The 5 PIs with no department vanish from the results.
- The "total federal funding" is lower than reality because $2.73M in federal awards (Chen, Johnson, Davis) have no department.

**In the narrative:**
- It reads as confident and complete. "Biology leads federal funding at $860K, followed by Computer Science at $725K..."
- Nothing in the prose signals that a third of the data was excluded.

### Discussion prompt

> "If you received this report from an analyst, would you catch the gap?"

The point: most people wouldn't. The narrative sounds right. The SQL looks reasonable. You'd only catch it if you checked the source data — which is exactly what the third panel is for.

### Teaching moment

This is why governed data matters at the pipeline level, not just at the report level:
- **Bronze:** Raw data ingested as-is, gaps and all
- **Silver:** Adapter maps to UDM — completeness checks can flag missing fields here
- **Gold:** Only records passing validation reach the unified layer
- If the AI queries Gold instead of Bronze, the gaps are either filled or flagged before the query ever runs

---

## Activity 3: Data Completeness Analysis

**Concept:** AI doesn't say "I don't know enough to answer this." It just answers. Using the same dataset, show how the impressive analysis was silently wrong.

### The reveal

**Prompt 5 — Pull the thread**

> "What is the total federal funding by department?"

Expected AI behavior: It answers confidently. But it can only count departments it can see. Biology gets $860K, Engineering gets $680K — but Chen ($1.2M, NIH), Johnson ($550K, NSF), Davis ($980K, NIH), and others have no department listed. Those federal dollars disappear from the breakdown. The total is unknowable — but the AI doesn't say that.

**Prompt 6 — Push harder**

> "Are there any departments with no federal funding?"

Expected AI behavior: It may list departments that appear in the table without federal sponsors. It won't mention that 33% of records have no department at all. It also may not recognize NIMH as a federal agency (NIH sub-agency).

**Prompt 7 — Now ask directly**

> "What data quality issues do you see in this table?"

Expected AI behavior: Now it identifies the gaps — missing departments, blank sponsors, null dates. The lesson: *it only evaluates data quality when you explicitly ask.* Every previous answer was delivered with equal confidence.

### The contrast

> "Go back to your portfolio summary from earlier. What would change if these missing fields were filled in?"

Expected AI behavior: It revises its analysis. Department rankings shift. Funding totals change. The "cut 20%" recommendation from Prompt 3 might now target different awards. Decisions made on the first analysis would have been wrong.

### Discussion prompts

1. **"Has this happened at your institution?"** — A report that looked right but was missing a chunk of data. Show of hands or brief table discussion.

2. **"Who catches this today?"** — Is it a person? A process? A validation rule? Or does nobody notice until someone questions the numbers?

3. **"What would governed data change?"** — If every record had to pass completeness checks before reaching the reporting layer, could this happen? (Bridge to medallion architecture and data governance.)

### Variations

**Live audience participation version:**
- Display the table on screen after Prompt 1. Ask the audience: "What's the total federal funding by department?" Give them 30 seconds to eyeball it.
- Then ask the AI. Compare.
- Reveal the trick: the question can't be answered accurately with this data.

**Side-by-side version:**
- Show the same question answered against the incomplete table and a completed version where all fields are filled in.
- The numbers change. The rankings change. The recommendation changes.

**"Fix it first" version:**
- Ask the AI to clean the data before answering. Show how it fills in guesses (hallucinated departments) vs. flagging unknowns. Different models behave differently — good teaching moment about model choice and trust.

---

## Key takeaways (all three activities)

- AI makes exploratory data analysis radically faster and more accessible
- Showing the SQL reveals what the AI actually asked for — and what it ignored
- A polished narrative can hide the same data gaps that a raw query would expose
- AI treats missing data as not-a-problem unless you force it to look
- Confidence ≠ correctness — every answer came with the same tone
- The value of data governance isn't bureaucracy — it's what makes AI-assisted analytics trustworthy
- The medallion architecture catches these problems before data reaches a report or an LLM
