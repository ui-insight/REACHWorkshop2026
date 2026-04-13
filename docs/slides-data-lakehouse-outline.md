# Module 2: The Data Lakehouse and Data Organization

**Presenter:** Nathan Layman
**Duration:** ~45 minutes (part of 1:00-4:00 PM workshop)

---

## Slide Outline

### 0. Title
- Module title, presenter photo and name
- **Status:** Done

### 1. Quiz: What is the most important model?
- 12 multiple-choice options (LLM, GPT, CNN, GAN, Diffusion, RNN, BERT, RL, Random Forest, SVM, VAE, GNN)
- Interactive: audience selects an answer
- **Status:** Done

### 2. Data model is the most important model
- Reveal: the most important model is your data model
- "AI models come and go, but how you organize your data determines whether any of them are useful"
- **Status:** Done (currently "Wrong! Your data model")

### 3. What is a data model?
- Define what a data model is in general terms
- Relatable to the audience: tables, columns, relationships, schemas
- **Status:** NEW -- needs to be created

### 4. What is a Universal Data Model and what are its benefits?
- A shared vocabulary across institutions, not a database
- Map each source once, AI learns one schema, apps work everywhere
- Cross-institutional comparison and benchmarking
- **Status:** Exists (current 4b), may need rework

### 5. Standards proliferation problem
- XKCD #927 comic
- Every institution stores the same concept differently
- The UDM is not "yet another standard" -- it is a translation layer
- **Status:** Exists (current 4a), reorder to after UDM intro

### 6. AI as a universal adapter
- AI can read source schemas and UDM schemas and suggest mappings
- Replaces manual N-to-N integration work
- AI is a bonus, not integral -- every adapter works without AI
- **Status:** NEW -- needs to be created (draws from current slides 12/13)

### 7. Four approaches to institutional data
- Warehouse, Data Lake, Lakehouse, Data Mesh
- Comparison diagram + toggle or cards
- **Status:** Exists (current slides 5/5b), merge into one slide

### 8. Capabilities of a data lakehouse
- 8 static cards: Trust & Governance, Data Quality, Reliability, Scalability, Openness, Multi-Modal, Simplicity, Cost Efficiency
- **Status:** Done (current slide 6)

### 9. The data lakehouse vs the data swamp (header)
- Section divider: "Same query. Same task. Two very different outcomes."
- **Status:** Done (current slide 11)

### 10. What goes into a data lakehouse
- What kinds of data belong in a lakehouse
- Sources: post-award systems, ERPs, spreadsheets, PDFs, emails, forms
- **Status:** NEW -- needs to be created

### 10a. Structured vs unstructured data
- Structured: tables, CSVs, database exports
- Unstructured: PDFs, images, emails, Word docs
- Semi-structured: JSON, XML, API responses
- A lakehouse handles all three
- **Status:** NEW -- needs to be created

### 11. The GRANTED data lakehouse architecture
- Pipeline flow: Sources > Bronze > Silver > Gold > Platinum > API > App
- Component legend: Shipyard, Marina, MinIO, Polaris, Trino
- **Status:** Done (current slide 7)

### 12. Open technology, interchangeable parts
- Every layer is replaceable (ingestion, storage, query, applications)
- Open table formats (Iceberg) mean no vendor lock-in
- **Status:** Done (current slide 7b)

### 13. Following data through the layers
- Worked example: VERAS AGENCY_TYPE from source to application
- Bronze (raw) > Silver (mapped) > Gold (deduped) > Platinum (joined)
- **Status:** Done (current slide 9)

### 14. What well-organized data lets you do
- Capstone slide: tie it all together
- Governed data enables: reliable AI, cross-institutional benchmarking, reproducible reports, safe automation
- Ungoverned data enables: confident-sounding wrong answers
- **Status:** NEW -- needs to be created

### End slide
- Back to sessions link
- **Status:** Done

---

## Slides removed from previous version

These slides are cut from the deck. Content may be repurposed elsewhere:

- UDM translation table (old 4c) -- too detailed for presentation, could be a handout
- PI Smith effort allocation toggle (old 11b)
- AI-assisted data ingestion detail (old 12) -- folded into slide 6
- Three levels of AI-assisted mapping (old 13) -- folded into slide 6
- Data governance as prerequisite (old 14) -- themes moved to slide 14
- Observability (old 15)
- AI inputs and outputs (old 16)
- Governance lens (old 17)
- Proposal routing worked example (old 18)
- Source trust rater (old 19)
- Context readiness checklist (old 20)

---

## New slides to create

| Slide | Title | Notes |
|-------|-------|-------|
| 3 | What is a data model? | General definition, relatable to audience |
| 6 | AI as a universal adapter | Consolidate old slides 12/13 |
| 10 | What goes into a data lakehouse | Types of sources |
| 10a | Structured vs unstructured data | Three data types, lakehouse handles all |
| 14 | What well-organized data lets you do | Capstone, tie themes together |

## Interactive Elements

Only use interactivity when it serves as a teaching tool, not decoration.

| Slide | Type | Description |
|-------|------|-------------|
| 1 | Quiz | Select a model type -- genuine audience participation |
| 7 | Toggle tabs | Compare Warehouse / Lake / Lakehouse tradeoffs side by side |
