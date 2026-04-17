# Project Summaries — Nate's Workshop Tools

Summaries of the two projects Nate is building for the REACH 2026 workshop (Role 2 — The data lakehouse and data organization).

---

## Data Lakehouse

**Repo:** `data-lakehouse` | **Version:** 1.0.1 | **Status:** Production

### What it is

An open-source data lakehouse platform built as a deliverable of the GRANTED NSF award. Purpose-built for universities managing research administration data with small teams and limited budgets. It provides governed API access, automated ingestion, and a medallion transformation layer.

### Tech stack

| Component | Technology | Role |
|-----------|-----------|------|
| Marina | Flask + PyIceberg | API gateway (only exposed service), JWT auth |
| Shipyard | FastAPI + Jinja2 | Admin UI and sync engine |
| MinIO | S3-compatible storage | Object storage (Parquet files) |
| Polaris | Apache Iceberg REST | Catalog and metadata |
| Trino | SQL query engine | Query execution over Iceberg tables |
| PostgreSQL | Database | Polaris metadata persistence |

All services are Docker-managed. Only Marina (port 7010) is exposed; everything else is localhost-only or SSH tunnel.

### Data flow

```
Remote APIs (VERAS, TeamDynamix, Banner)
    ↓
Shipyard sync engine (REST → Iceberg)
    ↓
MinIO (raw Parquet snapshots)
    ↓
Polaris (Iceberg REST catalog)
    ↓
Trino (SQL execution layer)
    ↓
Marina (JWT-authenticated API gateway)
    ↓
Applications and dashboards
```

### Medallion architecture (4 layers)

- **Bronze** — Raw ingested data exactly as received. No transforms. One Iceberg table per stream.
- **Silver** — Per-source translation to the AI4RA Unified Data Model (UDM). Trino SQL views, auto-generated. Never joins across sources.
- **Gold** — Deduplicated UNION ALL across Silver sources. One view per UDM table. Auto-generated, never hand-edited.
- **Platinum** — Application-specific views for dashboards and apps. Can join and aggregate across Gold/Silver.

### Data sources

- **VERAS** — Subaward and project financial data (REST API)
- **TeamDynamix** — IT ticketing system (REST API)
- **Banner** — Live institutional database (direct Trino connection)

### UDM integration

The data lakehouse uses the [AI4RA-UDM](https://github.com/ui-insight/AI4RA-UDM) canonical schema. Silver views map source columns to UDM column names and types. Gold views provide a single deduplicated view per UDM table across all sources.

### Security model

- Marina is the only exposed port
- JWT authentication (RS256, asymmetric RSA) per client
- Table-level and row-level access control
- Rate limiting (100 reads/min, 30 writes/min)
- All requests logged to audit table

### Workshop relevance

This is the concrete example of "the most important model is the data model." The lakehouse demonstrates:
- **Data organization** — medallion layers, UDM schema, governed pipelines
- **Data observability** — traceable, auditable, versioned data
- **Reproducibility** — same query, same answer, every time
- **Lakehouse vs data swamp** — the demo contrast (issue #14)

### Active development

- Feature branch: `feature/openmetadata` (catalog redesign + CAS file browser)
- Near-term: HTTPS/TLS, CI/automated testing, data freshness monitoring
- Medium-term: LLM-assisted adapter mapping, schema evolution detection
- Long-term: End-to-end data lineage, PII tagging, multi-institution deployment

---

## Promptulus — The AI Literacy Companions

**Repo:** `promptulus` | **Status:** Production | **Live:** [nate-layman.github.io/promptulus](https://nate-layman.github.io/promptulus/)

### What it is

An interactive web platform that teaches AI literacy through 9 steampunk characters, each coaching a different discipline of working with AI. The unifying concept: **your AI has a page limit** — everything competes for finite context window space, and these characters teach you to use that space well.

### Tech stack

Two parallel implementations:

- **Static site** (production, `docs/`) — vanilla HTML/JS/CSS, served via GitHub Pages. Feature-complete with interactive context window slider.
- **Shiny app** (`app/`) — R Shiny port with Google Gemini API (free tier) via the `ellmer` R package. All 9 characters wired up; slider not yet ported.

### The 9 characters

Organized in three phases:

**Before AI — Should you use AI for this?**

| Character | Animal | Discipline | Teaches |
|-----------|--------|-----------|---------|
| Sequita | Squirrel | Auditability | Whether a task needs a clear paper trail or just a good answer |
| Modulus | Crab | Task decomposition | How to break complex jobs into AI-manageable pieces |

**During AI — The context window balance**

These four map directly to the four components competing for context window space:

| Character | Animal | Discipline | Context window component |
|-----------|--------|-----------|------------------------|
| Telosa | Turtle | Intent engineering | Intent — purpose, accountability, escape hatches |
| Promptulus | Owl | Prompt engineering | Instructions — role, format, constraints |
| Mnemos | Elephant | Context engineering | Information — documents, data, retrieved knowledge |
| Dialogos | Parrot | Conversation management | Conversation — turn management, resets, focus |

**After AI — Was the output good enough?**

| Character | Animal | Discipline | Teaches |
|-----------|--------|-----------|---------|
| Vitrea | Glass frog | AI transparency | How AI actually works — tokenization, training, inference, environmental impact |
| Veridex | Raccoon | Output evaluation | How to catch hallucinations, verify facts, and assess trustworthiness |
| Clarion | Whale | Reporting and accountability | How to document AI-assisted work so others can understand and reproduce it |

### Interactive context window slider

The landing page features a single horizontal bar divided into four colored regions (intent, instructions, information, conversation) with three draggable divider handles. Growing one region shrinks its neighbors — total always sums to 100%.

Preset buttons snap the bar to common task-type balances:

| Preset | Intent | Information | Instructions | Conversation |
|--------|--------|-------------|-------------|--------------|
| Compliance review | 40% | 30% | 20% | 10% |
| Draft a description | 10% | 50% | 25% | 15% |
| Iterative editing | 10% | 20% | 15% | 55% |
| New task scoping | 50% | 20% | 15% | 15% |

Clicking a character highlights its region in the bar — showing which part of the context window that character teaches you to optimize.

### How it works

1. Landing page introduces the context window concept with the interactive slider
2. User selects a character from one of the three phases
3. Types a prompt or task description
4. Character responds with a rating, strengths, and one specific principle to improve
5. User refines and resubmits — iterative learning loop
6. Sidebar shows the full principle framework for that character

### Workshop relevance

Promptulus is the live demo in Nate's Role 2 section. Participants use it to:
- Visualize how intent, instructions, information, and conversation compete for context window space
- Practice prompt engineering with immediate AI feedback
- Assess whether their tasks need auditability before using AI (Sequita)
- Define intent clearly before starting an AI workflow (Telosa)
- Learn to evaluate and document AI output (Veridex, Clarion)
- Understand how AI works at a conceptual level (Vitrea)

### Current state

- All 9 characters implemented with system prompts and principle frameworks
- Static site (GitHub Pages) is feature-complete with interactive slider
- Shiny app has all characters but slider not yet ported from JS
- Free tier Gemini API (15 req/min, 1,500 req/day) — may need attention for 24 concurrent workshop participants
