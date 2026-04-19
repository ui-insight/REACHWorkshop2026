# Module 2: The Data Lakehouse and Data Organization

**Presenter:** Nathan Layman
**Duration:** ~45 minutes (part of 1:00-4:00 PM workshop)

---

## Module Structure

| Part | Title | Duration |
|------|-------|----------|
| 1 | AI-Assisted EDA | 15 min |
| 2 | Data Models & the UDM | 20 min |
| 3 | Data Lakehouse Architecture | 10 min |

---

## Slide Outline

### 1. Title
- Module title, presenter photo and name

### 2. Module Preview
- Three-part flow diagram showing the module structure and timing

### Activity 1: AI-Assisted EDA
- Launch Data Crawler Carl demo
- Upload a CSV, ask questions in plain English
- Sample datasets available (synthetic proposals, awards, publications)

### Activity 1 Debrief
- Discussion: Did the AI sound confident but wrong? Missing values? Different answers from rephrasing?
- Takeaway: AI analyzes what you give it, governed data and reproducibility matter

### Cloud vs. Locally Hosted Models
- Toggle between Cloud / Local / Hybrid
- Security considerations for each approach

### The Model Behind the Demo
- Explains Gemini 2.5 Flash and how LLMs work (token prediction, no understanding)

### Quiz: What is the Most Important Model?
- 12 multiple-choice options (LLM, GPT, CNN, GAN, etc.)
- Interactive audience participation

### Reveal: Your Data Model
- The most important model is your data model
- "AI models come and go, but how you organize your data determines whether any of them are useful"

### What is a Data Model?
- General definition, relatable examples (tables, columns, relationships)
- Three things a data model does: names, relates, constrains

### What is a Universal Data Model (UDM)?
- A shared vocabulary across institutions, not a database
- Map each source once, AI learns one schema, apps work everywhere

### The AI4RA UDM: Domains and Scope
- Diagram showing UDM domains (People, Organizations, Awards, Proposals, etc.)
- Full model available on GitHub

### Ontology: Predictable Naming Conventions
- Five naming convention rules (e.g. singular nouns, underscore separation)
- Examples of how conventions apply to field names

### The Standards Problem
- XKCD #927 comic
- The UDM is a translation layer, not another standard

### AI as a Universal Adapter
- AI reads source schemas and UDM schemas, suggests mappings
- Replaces manual N-to-N integration work
- Every adapter works without AI (AI is a bonus)

### Transition: Now How Do We Handle All That Data?
- Bridge from data model to infrastructure

### Four Approaches to Institutional Data
- Toggle between Warehouse / Data Lake / Lakehouse / Data Swamp
- Comparison of tradeoffs for each

### Capabilities of a Data Lakehouse
- 8 capability cards: Trust & Governance, Data Quality, Reliability, Scalability, Openness, Multi-Modal, Simplicity, Cost Efficiency

### The GRANTED Data Lakehouse Architecture
- D3 pipeline diagram: Sources > Bronze > Silver > Gold > Platinum > API > App
- Data flow legend with color-coded layers

### Open Technology, Interchangeable Parts
- Every layer is replaceable (ingestion, storage, query, applications)
- Two paths: Medallion (recommended) and Direct database

### The Medallion Layers
- Horizontal flow: Bronze > Silver > Gold > Platinum
- Detail cards for each layer

### Following Data Through the Layers
- Worked example: VERAS AGENCY_TYPE from source to application
- Bronze (raw) > Silver (mapped) > Gold (deduped) > Platinum (joined)

### What Well-Organized Data Lets You Do
- Capstone: governed data vs. ungoverned data outcomes

### End of Module
- Back to sessions link

---

## Interactive Elements

| Slide | Type | Description |
|-------|------|-------------|
| Quiz | Multiple choice | Select a model type, genuine audience participation |
| Cloud vs Local | Toggle tabs | Compare Cloud / Local / Hybrid tradeoffs |
| Four Approaches | Toggle tabs | Compare Warehouse / Lake / Lakehouse / Swamp |
| Architecture | D3 diagram | Live-rendered pipeline visualization |
| Activity 1 | External demo | Data Crawler Carl with sample datasets |
