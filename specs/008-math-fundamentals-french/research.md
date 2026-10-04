# Research: Mathematical Fundamentals — French Version

**Feature**: 008-math-fundamentals-french
**Date**: 2026-09-17
**Status**: Complete — all NEEDS CLARIFICATION resolved

---

## Decision Log

### D-001: Language Switcher Implementation

**Decision**: Use an OJS snippet embedded via a shared include file
(`fr/teaching/mathematical-fundamentals/_lang-switch.qmd`) that reads
`window.location.pathname`, detects whether the current page is under `/fr/`,
computes the EN↔FR counterpart URL by adding or stripping the `/fr` prefix,
and renders a visible link. This include is referenced in both
`fr/teaching/mathematical-fundamentals/_metadata.yml` and
`teaching/mathematical-fundamentals/_metadata.yml` via `include-before-body`.
A global `_quarto.yml` navbar `tools` entry with an icon also links to the
FR/EN course index as a fallback for pages outside the teaching section.

**Rationale**: OJS is already available in Quarto without extra dependencies.
The `fr/**/*.qmd` paths always mirror `teaching/mathematical-fundamentals/**`
with a `/fr` prefix, making URL computation deterministic and zero-maintenance.
Because the folder-per-language structure enforces a strict 1-to-1 path
correspondence, stripping or prepending `/fr` is guaranteed to resolve to the
correct counterpart page in all cases.

**Alternatives Considered**:

- **(a) Static per-page front-matter entries for the counterpart URL** — accurate
  but requires manual upkeep for every one of the 20 pages; any rename or
  reorganisation silently breaks the links.
- **(b) babelquarto R package** — provides auto-switching but requires an R
  runtime, and uses a file-suffix pattern (`index.fr.qmd`) that conflicts with
  the folder-per-language architecture mandated by the project constitution.
- **(c) Pure `_quarto.yml` navbar tool with fixed links** — simple to configure
  but only links to the course index, not the current page's counterpart; users
  navigating deep into module pages lose their position when switching language.

---

### D-002: Relative Asset Path Adjustment for FR Slide Decks

**Decision**: French slide decks at
`fr/teaching/mathematical-fundamentals/module-N-slides.qmd` must reference the
RevealJS theme as `../../../assets/dark-slides.scss` (three levels up to site
root), vs. the English `../../assets/dark-slides.scss` (two levels up from
`teaching/mathematical-fundamentals/`). This is the only structural difference
between English and French slide front matter.

**Rationale**: Quarto resolves RevealJS theme paths relative to the source
`.qmd` file, not relative to the output root or the site root. French slide
decks sit one additional directory level deep (`fr/` prefix), so one extra
`../` is required. The adjustment is mechanical and verifiable — no other
front-matter fields differ between the English and French slide decks.

**Alternatives Considered**:

- **Absolute site-root path (`/assets/dark-slides.scss`)** — rejected because
  Quarto resolves theme paths relative to the source file during rendering; an
  absolute path is not treated as site-root-relative and causes a render error.
- **Symbolic link at `fr/assets/` pointing to `assets/`** — technically
  correct but adds filesystem complexity (a dangling symlink in the repo) with
  no benefit over the simple relative path adjustment.

---

### D-003: Image and Binary Asset Sharing

**Decision**: The `image.jpg` used in `teaching/mathematical-fundamentals/index.qmd`
is referenced by the French index as
`../../teaching/mathematical-fundamentals/image.jpg` (relative path from
`fr/teaching/mathematical-fundamentals/`). No binary assets are duplicated.

**Rationale**: Quarto resolves relative paths in both front-matter `image:`
fields and Markdown `![]()` syntax correctly for static site output; the
relative path resolves to the same rendered file in `docs/`. Keeping a single
copy avoids repository bloat and eliminates any risk of the two copies
diverging silently.

**Alternatives Considered**:

- **Copy `image.jpg` into `fr/teaching/mathematical-fundamentals/`** —
  unnecessary duplication; adds an unchanged binary to the repository with no
  user-visible benefit, and creates a maintenance burden if the image is ever
  updated.

---

### D-004: `_metadata.yml` Strategy for FR Teaching Pages

**Decision**: Create `fr/teaching/mathematical-fundamentals/_metadata.yml` that
sets `lang: fr` as a default for all `.qmd` files in that directory. Individual
files still declare `lang: fr` explicitly in their own front matter for
clarity (belt-and-suspenders). The `_metadata.yml` also carries any other
directory-scoped defaults (e.g., `include-before-body` for the language
switcher).

**Rationale**: Quarto's `_metadata.yml` applies to all `.qmd` files in its
directory, which is the standard pattern already used in `posts/_metadata.yml`
in this project. It keeps individual files free of boilerplate while ensuring
correct HTML `lang` attributes and hyphenation in all rendered output.

**Alternatives Considered**:

- **Set `lang: fr` only at the project level in `_quarto.yml` for the whole
  `fr/` tree** — rejected because Quarto's project-level metadata does not
  support path-scoped `lang` overrides cleanly. Setting `lang: fr` globally
  would affect any English page that shares the `_quarto.yml` project, breaking
  the EN pages.

---

### D-005: Stub vs. Full Translation Strategy

**Decision**: All 20 French pages are delivered as **full translations** in
this feature. Stubs are only acceptable as a temporary state; since all 20
English source pages already exist and are stable, the full translation is
completed in one pass. The spec requirement for stubs (FR-006) is satisfied
trivially — no page is intentionally left as a stub.

**Rationale**: The English course (`teaching/mathematical-fundamentals/`) is
complete and stable, covering Modules 1–8 plus three resource pages. All
source content is available upfront. Translating all 20 pages in a single
feature is tractable and avoids the overhead of tracking stub-to-full upgrade
tasks in subsequent specs.

**Alternatives Considered**:

- **Ship stubs first, then iterate in a follow-up spec** — adds an unnecessary
  intermediate state (20 placeholder pages in production) and a follow-up
  feature ticket for content that is already available. The English course
  being complete removes the usual justification for stubs (awaiting source
  content).

---

### D-006: Sidebar Expansion Strategy

**Decision**: Replace the existing partial `fr-mathematical-fundamentals`
sidebar block in `_quarto.yml` (currently slides-only, added as a placeholder
in Spec 007) with a complete block that mirrors the English
`mathematical-fundamentals` sidebar: course index first, then 8 module sections
each containing a Reference page link and a Slides link, then a Resources
section with Glossary, Formula Sheet, and Learning Guide.

**Rationale**: The existing partial block was a placeholder from Spec 007.
Replacing it with the full structure is cleaner than appending to it and
follows the exact same pattern as the English sidebar, making the two sidebars
easy to keep in sync. A single, authoritative block per language avoids
ambiguity about which block applies to which pages.

**Alternatives Considered**:

- **Add a second, supplementary sidebar block alongside the existing one** —
  creates duplication and ambiguity in `_quarto.yml`; Quarto applies sidebars
  by matching `contents` paths, so two overlapping blocks would produce
  undefined behaviour for pages listed in both.

---

### D-007: Translation of Interactive Widget Prose Labels (Shinylive / OJS)

**Decision**: OJS and Shinylive blocks within module pages have their
user-visible prose translated in the French `.qmd` files — specifically axis
titles, button labels, legend text, and any other UI strings. Computation code
(data wrangling, statistical logic, rendering calls) is copied verbatim from
the English source. Widgets with no user-visible prose (pure computation cells)
are also copied verbatim.

**Rationale**: Interactive widgets are required by project Principle T-IV.
The only content that differs between the English and French widgets is the
display language of labels; the underlying logic is identical. Translating
labels only is the minimal, correct change that satisfies both the translation
requirement and the principle.

**Alternatives Considered**:

- **Omit all interactive widgets from French pages** — would violate Principle
  T-IV (interactive demos are a required teaching tool) and would create a
  noticeable quality gap between the EN and FR course experiences.
- **Duplicate entire widget code blocks with no changes** — simpler to implement
  but leaves French pages with English-language axis labels and button text,
  which is inconsistent with a fully translated course.
