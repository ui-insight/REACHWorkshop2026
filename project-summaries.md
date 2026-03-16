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

Both the data lakehouse and OpenERA use the [AI4RA-UDM](https://github.com/ui-insight/AI4RA-UDM) canonical schema. Silver views map source columns to UDM column names and types. Gold views provide a single deduplicated view per UDM table across all sources.

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
- Medium-term: OpenERA integration, LLM-assisted adapter mapping, schema evolution detection
- Long-term: End-to-end data lineage, PII tagging, multi-institution deployment

---

## Promptulus

**Repo:** `promptulus` | **Status:** Beta/Early Production | **Live:** [n8-layman.shinyapps.io/promptulus](https://n8-layman.shinyapps.io/promptulus/)

### What it is

An interactive web app that teaches AI literacy and prompt engineering to research administration professionals. Features three AI-powered teaching characters that mentor users through different aspects of working with AI.

### Tech stack

- **Framework:** R Shiny
- **AI backend:** Google Gemini API (free tier) via the `ellmer` R package
- **UI:** bslib (Bootstrap for Shiny)
- **Hosting:** shinyapps.io (primary), Shinylive browser-based version in `/docs`
- **Discussion:** Giscus (GitHub Discussions integration)

### The three characters

| Character | Role | Rating scale | Teaches |
|-----------|------|-------------|---------|
| Promptulus the Owl | Prompt engineering coach | 1–5 mice | How to structure prompts for reliable output |
| Modulus the Crab | Task decomposition expert | 1–5 shrimp | How to break complex jobs into automatable tasks |
| Dichotra the Squirrel | Task classification specialist | LLM / Data Science / Hybrid | When to use AI vs data science vs both |

### How it works

1. User selects a character
2. Types a prompt or task description
3. Character responds with a rating, strengths, and one specific principle to improve
4. User refines and resubmits — iterative learning loop
5. Sidebar shows full principle framework for reference

### Principle frameworks

- **Prompting** (Promptulus) — 21 principles across 5 levels: Core Clarity → Structure → Reasoning → Refinement → Meta-Thinking
- **Modularization** (Modulus) — 17 principles across 5 levels: Framing → Chaining → Execution → Review → Meta-Learning
- **Task categorization** (Dichotra) — 18 principles across 5 levels: Task Nature → Complexity → Hybrid Indicators → Constraints → Strategy

56 total principles across all three systems.

### Workshop relevance

Promptulus is the live demo in Nate's Role 2 section. Participants use it to:
- Compare prompt strategies and see how structure changes output quality
- Experience iterative prompt refinement with immediate feedback
- Understand the difference between LLM tasks and data science tasks (via Dichotra)
- Practice task decomposition for research administration workflows (via Modulus)

### Current state

- All three characters functional and deployed
- 820 lines of R code in main app file
- 3 deployment options (local, shinyapps.io, Shinylive)
- Free tier Gemini API (15 req/min, 1,500 req/day) — may need attention for 24 concurrent workshop participants
- Recent development: Modulus and Dichotra characters added, UI refinements, discussion integration
