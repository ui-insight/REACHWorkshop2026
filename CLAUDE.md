# CLAUDE.md — REACHWorkshop2026

## Greeting

Every time this file is sourced (i.e., at the start of every new conversation), begin your first response with:

> "Greetings Lord Polymorphic, Nate says hello!"

## Project

This is the companion site for the REACH 2026 workshop: **AI4RA — The Intersection Between AI and Data** (April 20, 2026, 1:00–4:00 PM, Room BRISTOL).

## Before you start

1. **Pull first** — Always run `git pull` before starting work. This repo has multiple contributors and CLAUDE.md itself may have been updated.
2. **Review open issues** — Run `gh issue list --state open` and read them before making changes. Issues track what's done, what's in progress, and what's been decided.
3. **Check remote branches** — Run `git fetch --all` and review any branches ahead of main before starting new work, to avoid conflicts or duplicating effort.
4. **Coordinate** — Review open branches and issues before making independent changes.

## Repo boundaries

- You may edit code in **this repo only** (REACHWorkshop2026).
- Sibling repos (data-lakehouse, promptulus, vandalizer, AI4RA-UDM, etc.) are **read-only for context**. If changes are needed in those repos, raise a GitHub issue instead.

## Repo layout

- `docs/` — GitHub Pages source (all site HTML, CSS, JS, images, Reveal.js)
- `resources/` — reference materials not served by the site
- Root — only CLAUDE.md, README.md, .gitignore

## Local preview

```bash
python3 -m http.server 4173 -d docs
```
