# REACH Workshop 2026 Site

Static GitHub Pages site for the REACH 2026 workshop session:

- `WA3 - Workshop AI4RA - The Intersection Between AI and Data`
- Monday, April 20, 2026
- 1:00 PM - 4:00 PM
- Room BRISTOL

## Local preview

Run a simple static server from the repo root:

```bash
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173`.

## Deployment

This site is designed for branch-based GitHub Pages deployment from the root of
the `main` branch. Add `.nojekyll` to keep GitHub Pages from trying to process
the site with Jekyll.
