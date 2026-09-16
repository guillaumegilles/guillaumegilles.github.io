# Research: Mathematical Fundamentals RevealJS Slide Decks

**Branch**: `007-math-fundamentals-slides` | **Date**: 2026-09-15
**Feature**: [spec.md](spec.md)

---

## Decision 1: RevealJS in a Quarto Website Project

**Decision**: Use file-level `format: revealjs` in each slide deck's front matter.

**Rationale**: A Quarto website project with a global `format: html` setting in
`_quarto.yml` allows individual `.qmd` files to override the format using their
own YAML front matter. Setting `format: revealjs` renders the file as a
self-contained RevealJS HTML presentation and places the output in `docs/` at
the expected path (e.g., `docs/teaching/mathematical-fundamentals/module-1-slides.html`).

The website chrome (navbar, sidebar, footer) is intentionally not injected into
RevealJS output — RevealJS is self-contained. This is correct behavior for a
full-screen lecture presentation.

**Alternatives considered**:
- Separate Quarto project per slide deck — rejected (adds project overhead;
  slides should be co-located with course materials).
- Using `output-file` in `_quarto.yml` profile — rejected (overly complex, not
  needed for this use case).

---

## Decision 2: RevealJS Theme

**Decision**: Create `assets/dark-slides.scss` with RevealJS-specific SCSS
variables that mirror the site's blackboard/dark colour palette.

**Rationale**: The existing `assets/dark.scss` uses Bootstrap SCSS variables
and mixins that are only meaningful in an HTML context. RevealJS uses an
entirely separate set of SCSS variables (`$backgroundColor`, `$mainColor`,
`$headingColor`, `$linkColor`, etc.). Attempting to reuse `dark.scss` would
produce no visual effect in RevealJS.

A new `assets/dark-slides.scss` file:
- stays within the "all styling in `assets/`" constraint (Constitution V);
- keeps RevealJS vars separate from Bootstrap vars;
- allows consistent blackboard-style palette across both output formats.

As a fallback during development, the built-in `theme: dark` can be used; it
should be replaced with the custom SCSS before any public presentation.

**Alternatives considered**:
- `theme: dark` (built-in RevealJS) — accepted as temporary fallback only;
  does not match the site's colour palette.
- Inline styles in slide files — rejected outright (Constitution V violation).

---

## Decision 3: Sidebar Registration vs. Module-Page Links

**Decision**: Register slides in the sidebar AND add a "📊 Slides" link on
each module reference page.

**Rationale**: Constitution Principle II states that any published page not
listed in the sidebar MUST NOT be considered published. Because slides are
accessible to students (published), they must appear in the sidebar.

Additionally, placing a direct "📊 Slides" link in each module's reference
page body improves discoverability — students can jump to the deck without
navigating the sidebar. These two approaches complement each other.

UX note: clicking a sidebar link to a RevealJS deck opens the full-screen
presentation (the sidebar disappears). This is expected behavior for
presentation tools and matches student expectations.

In `_quarto.yml`, slides are grouped under a new `"**Slides**"` section in
the mathematical-fundamentals sidebar, keeping them visually distinct from
the reference modules and resource pages.

**Alternatives considered**:
- Sidebar only — rejected (poor discoverability for students browsing a module).
- Module-page link only — rejected (violates Constitution II: published pages
  must appear in the sidebar).

---

## Decision 4: OJS / Shinylive in Slides

**Decision**: Omit all OJS and Shinylive blocks from slide decks entirely.

**Rationale**: Interactive widgets sized for a full-page web layout look
cramped in RevealJS slides. More importantly, a lecture context calls for
controlled, linear progression rather than live interaction with sliders.
Where an interactive demo exists in the reference page, the corresponding
slide will show the key static result (formula + notable finding) and direct
students to the reference page for the full interactive exploration.

**Alternatives considered**:
- Include OJS in slides — rejected (poor UX, layout conflicts, unnecessary
  complexity in a static presentation artifact).

---

## Decision 5: Computational Freeze

**Decision**: No `_freeze/` entries are needed for slide deck files.

**Rationale**: The `_freeze/` mechanism is only triggered by executed code
chunks (`{python}`, `{r}`, `{julia}`, `{ojs}`). Slide decks contain only
static Markdown and LaTeX math — Quarto renders them in a pure pandoc pass
with no code execution. This is confirmed by Quarto's documentation and
consistent with `execute: freeze: auto` behavior.

---

## Decision 6: French Bilingual Stubs

**Decision**: Create minimal French stub slides under
`fr/teaching/mathematical-fundamentals/` for all 8 modules.

**Rationale**: Constitution Principle VI requires every published page to have
a counterpart in the other language. Untranslated pages must render a stub
with a "translation in progress" notice, not a 404 or missing nav entry.

**Structure of each stub**:
```yaml
---
title: "[FR module title]"
lang: fr
---
```
Followed by a `.callout-note` block in French with a "Traduction en cours"
notice and a relative link to the English slide deck.

**Important pre-existing gap**: The 8 reference module pages
(`module-1.qmd` … `module-8.qmd`) also lack French counterparts. This is
a pre-existing Constitution VI violation. It is OUT OF SCOPE for this
feature — creating reference-page French stubs is a separate task.
This feature only creates French stubs for the 8 new slide decks.

**Alternatives considered**:
- Full French translations — rejected (out of scope; translations require
  significant subject-matter work and are a separate feature).
- Skip French stubs — rejected (would violate Constitution VI immediately
  upon publishing the English slides).

---

## Decision 7: File Naming Convention

**Decision**: English slide decks are named `module-N-slides.qmd` in
`teaching/mathematical-fundamentals/`. French stubs mirror the name under
`fr/teaching/mathematical-fundamentals/`.

**Rationale**: The `-slides` suffix clearly distinguishes slide deck files
from reference pages at a glance. It is consistent with the existing naming
pattern (module-N.qmd for reference). The sidebar can use `text:` to display
a human-readable label.

---

## Decision 8: Module 8 Slide Structure

**Decision**: Module 8 slides are a curated cross-module revision deck, not a
repetition of Modules 1–7. Structure: recap slide for each of the 7 topics
(1 slide each), a "method identification" slide, and exam strategy tips.

**Rationale**: The Module 8 reference page has no new theory — it is
explicitly a revision module. A 56-slide deck repeating all seven modules
would be counterproductive. Instead, the Module 8 deck provides a 1-slide
summary per prior module (formula + key takeaway) and focuses on mixed-method
problem identification.

---

## Summary Table

| Decision | Choice | Key Constraint |
|---|---|---|
| Quarto format | `format: revealjs` per-file | Lands in `docs/`; no website chrome |
| Theme | `assets/dark-slides.scss` | Constitution V: all CSS in `assets/` |
| Navigation | Sidebar section + module-page link | Constitution II: must be in sidebar |
| Interactive elements | Omitted from slides | UX + layout constraints |
| Freeze | Not required | No executed code in slide files |
| FR parity | Stubs only (this feature) | Constitution VI; ref-page stubs are out of scope |
| File naming | `module-N-slides.qmd` | Consistent with existing pattern |
| Module 8 | Cross-module revision deck | Module 8 has no new theory |
