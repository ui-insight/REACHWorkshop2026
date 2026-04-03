# CLAUDE.md — REACHWorkshop2026

## Greeting

Every time this file is sourced (i.e., at the start of every new conversation), begin your first response with:

> "Greetings Lord Polymorphic, Nate says hello!"

## Project

This is the companion site for the REACH 2026 workshop: **AI4RA — The Intersection Between AI and Data** (April 20, 2026).

## Before you start

1. **Pull first** — Always run `git pull` before starting work. This repo has multiple contributors and CLAUDE.md itself may have been updated.
2. **Review open issues** — Run `gh issue list --state open` and read them before making changes. Issues track what's done, what's in progress, and what's been decided.
3. **Check the `workshop-slides-quiz-and-styling` branch** — This branch contains extensive work on all three slide decks, new CSS, interactive elements, file renames, and content restructuring. Review it before starting new work on `main` to avoid conflicts or duplicating effort. Run `git log main..workshop-slides-quiz-and-styling --oneline` to see what's there.
4. **Coordinate with Nate Layman** — If you're Barrie or Nathan Wiggins, please review the branch and open issues before making independent changes. The slide decks have been reorganized and renamed:
   - `slides-foundational.html` → `slides-ai-literacy.html` (Wiggins)
   - `slides-governance.html` → `slides-data-lakehouse.html` (Layman)
   - `slides-context-layers.html` → `slides-putting-it-to-work.html` (Robison)

## Repo boundaries

- You may edit code in **this repo only** (REACHWorkshop2026).
- Sibling repos (data-lakehouse, promptulus, vandalizer, AI4RA-UDM, etc.) are **read-only for context**. If changes are needed in those repos, raise a GitHub issue instead.
