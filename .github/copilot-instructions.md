# Copilot Instructions

## Project Overview

Personal website for Guillaume Gilles (`ggilles.dev`) built with **Quarto**. It
combines a blog, teaching course materials, and a Cloudflare AI Worker. The
rendered HTML lives in `docs/` and is served via GitHub Pages.

## Build Commands

```sh
# Preview the full site with live reload
quarto preview

# Render the full site to docs/
quarto render

# Render a single file (faster for iterating on one page)
quarto render teaching/statistics-probability/sampling-distribution.qmd --quiet
quarto render posts/agentic-ai/index.qmd --quiet
```

Python dependencies are managed in `.venv/`:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The Cloudflare Worker (`worker/`) is deployed independently:
```sh
cd worker && wrangler deploy
```

## Architecture

```
_quarto.yml          # Site config: navbar, all sidebars, theme, output dir
assets/dark.scss     # Custom dark theme applied globally
posts/               # Blog posts — single .qmd or <name>/index.qmd
teaching/            # Course materials, one subdirectory per course
  statistics-probability/
  financial-analysis/
  mathematical-analysis/
  ai-papers/
  ai-dev/
docs/                # Rendered output (committed, served by GitHub Pages)
_freeze/             # Cached computation results (committed)
worker/              # Cloudflare Worker: AI resume chat on the homepage
scripts/             # Post-render scripts
```

**Post-render hook**: after every `quarto render`, `scripts/update-profile-readme.sh`
re-renders `about.qmd` as GitHub-Flavored Markdown and pushes it to the
`guillaumegilles/guillaumegilles` profile repo.

## Key Conventions

### Adding a blog post
Create `posts/<slug>/index.qmd` (or `posts/<slug>.qmd`) with this front matter:
```yaml
---
title: "Post title"
date: 2026-05-14
categories: [Category1, Category2]
draft: true          # omit or set false to publish
---
```
Giscus comments are injected automatically for all blog posts via
`posts/_metadata.yml` — no per-file config needed.

### Adding a teaching page
1. Create `teaching/<course>/<file>.qmd`. Use `date-modified` (not `date`) in
   the front matter, plus a `title` and optional `abstract`.
2. Register the file in the matching sidebar inside `_quarto.yml`. Pages not
   listed there will not appear in the sidebar navigation.

### Adding a new course
Add a new sidebar block under `website.sidebar` in `_quarto.yml` and create
the corresponding directory under `teaching/`.

### Interactive Python widgets (Shinylive)
The `quarto-ext/shinylive` extension is installed. Use `{shinylive-python}`
code blocks to embed live Python apps in teaching pages.

### Computational freeze
`execute: freeze: auto` is set globally. Commit the `_freeze/` directory so CI
and collaborators don't need to re-execute notebooks. Delete a file's freeze
entry to force re-execution.

### Math
Use standard LaTeX: `$...$` for inline, `$$...$$` for display equations.
Citations and references render in the margin (set globally in `_quarto.yml`).

### Callout blocks
Teaching pages use Quarto callout divs heavily:
```markdown
::: {.callout-note}
## Title
Content
:::
```
Common types: `.callout-note`, `.callout-important`, `.callout-tip`.

### Theme
All styling goes in `assets/dark.scss`. The compiled theme is referenced in
`_quarto.yml` under `format.html.theme`.

<!-- SPECKIT START -->
## Active Spec Kit Plan

Current feature plan: `specs/003-giscus-theme-integration/plan.md`
(Giscus Retro Blackboard Theme Integration — Customise the giscus comment widget to
blend with the Retro Blackboard dark.scss theme by delivering a custom plain-CSS file
at `assets/giscus-retro-blackboard.css`, served at `https://ggilles.dev/assets/
giscus-retro-blackboard.css`, referenced via `posts/_metadata.yml` `comments.giscus.
theme`. All giscus CSS custom properties are mapped to Retro Blackboard design tokens
— phosphor-green primary, chalk text, board-surface backgrounds, no GitHub-default
blue visible.)
<!-- SPECKIT END -->
