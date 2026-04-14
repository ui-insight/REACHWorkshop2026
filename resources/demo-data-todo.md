# Demo Dataset TODO

## Context
For the Session 2 interactive activities (AI-assisted EDA → Data completeness reveal), we need a completely fictional but realistic awards dataset. No real institutional data can be shown at the conference.

## Activities doc
See `resources/interactive-activities.md` for the full activity design.

## TODO

- [ ] Create a fictional institution (e.g., "Westfield State University")
- [ ] Generate a complete, realistic awards dataset (~30-50 rows) with fictional PIs, departments, sponsors, amounts, and dates
- [ ] Create a degraded version of the same dataset with intentional gaps (missing departments, blank sponsors, null dates) for the completeness reveal
- [ ] Ingest both versions into the data lakehouse as a demo source
- [ ] Build Silver adapter mapping the demo source to UDM
- [ ] Verify Gold views work with the demo data
- [ ] Test the full prompt sequence (EDA → completeness reveal) against both versions
- [ ] Dry run the demo end-to-end

## Next step
Generate the fictional dataset (complete + degraded CSVs) in `resources/`.
