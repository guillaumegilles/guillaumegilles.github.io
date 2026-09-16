# Implementation Plan: Mathematical Fundamentals RevealJS Slide Decks

**Branch**: `007-math-fundamentals-slides` | **Date**: 2026-09-15
**Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/007-math-fundamentals-slides/spec.md`

## Summary

Create one RevealJS slide deck per module (8 English + 8 French stubs = 16
new `.qmd` files) for the Mathematical Fundamentals course
(`teaching/mathematical-fundamentals/`). Slides serve as a concise lecture
companion; the existing reference module pages remain unchanged. Each deck
follows a fixed structure (learning objectives → concepts → worked example →
summary → reference link) and uses a new `assets/dark-slides.scss` theme.
Slides are registered in the course sidebar and linked from each reference page.

## Technical Context

**Language/Version**: Quarto (project version, rendered via `quarto render`)

**Primary Dependencies**:
- RevealJS — built into Quarto; no separate install required
- `assets/dark-slides.scss` — new file; RevealJS-specific SCSS variables

**Storage**: Static `.qmd` source files; HTML output in `docs/` via GitHub Pages

**Testing**: `quarto render` (exit code 0 = pass); visual inspection in
browser per [quickstart.md](quickstart.md)

**Target Platform**: Static GitHub Pages; any modern desktop browser in
full-screen/presentation mode

**Project Type**: Static teaching website with RevealJS presentation output
embedded alongside standard HTML pages

**Performance Goals**: Each slide deck loads in under 3 seconds on a standard
campus internet connection (RevealJS is self-contained and lightweight)

**Constraints**:
- No OJS / Shinylive blocks in slide files
- No inline `style=` or `<style>` blocks (Constitution V)
- `quarto render` must exit 0 before commit (per Development Workflow)
- Both EN and FR render targets must pass

**Scale/Scope**: 8 EN slide decks + 8 FR stubs + 1 SCSS theme file +
`_quarto.yml` update + 8 minor edits to reference pages = ~25 file changes

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Content-First** — All 16 new slide decks are backed by `.qmd`
  source files. No direct HTML written to `docs/`.
- [x] **II. Navigation registered** — All 8 EN slide decks are listed in a
  new `"**Slides**"` section inside the `mathematical-fundamentals` sidebar
  block in `_quarto.yml`. FR stubs also registered in the FR sidebar
  counterpart (if one exists) or noted as pending.
- [x] **III. Reproducible** — Slide decks contain no executed code; no
  `_freeze/` entries are created for them. Existing freeze entries are
  unchanged.
- [x] **IV. Privacy-First** — RevealJS is self-contained; no third-party
  scripts, tracking, or analytics are introduced.
- [x] **V. Styling contained** — Theme in `assets/dark-slides.scss`. No
  inline styles or `<style>` blocks in any slide file.
- [x] **VI. Bilingual parity** — 8 French stub decks created under
  `fr/teaching/mathematical-fundamentals/`, each with `lang: fr` and a
  "Traduction en cours" notice. **NOTE**: The pre-existing 8 reference pages
  lack French counterparts — this is an out-of-scope, pre-existing violation.

*For teaching pages only:*
- [x] **T-I. Content Fidelity** — Reference pages (`module-N.qmd`) are
  unchanged. Slides are a supplementary, additive artifact.
- [x] **T-II. Pedagogical Structure** — Each slide deck follows theory
  (concepts) → worked example → summary. Objectives appear first.
- [x] **T-III. Audience language** — Slides use plain language matching the
  reference pages. Every formula slide includes a prose explanation.
- [x] **T-IV. Interactive demos** — N/A: slides are static by design
  (OJS/Shinylive excluded per spec). No TODO markers needed — the reference
  page already carries the full interactive demos.
- [x] **T-V. Glossary** — N/A: slides introduce no new symbols. All symbols
  used in slides are already in `glossary.qmd`.
- [x] **T-VI. Proof** — N/A: slides distill existing content. Collapsible
  proofs from reference pages are referenced via the "📖 Full Reference" link.
- [x] **T-VII. Visual intuition** — Slides surface geometric/visual
  interpretations where applicable (Module 3: graphical line interpretation;
  Module 7: geometric meaning of derivative as slope).
- [x] **T-VIII. Course syllabus** — N/A: `index.qmd` is unchanged; this
  feature does not create or modify a course index.

*All gates pass. Proceeding to Phase 0.*

## Project Structure

### Documentation (this feature)

```text
specs/007-math-fundamentals-slides/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── slide-deck-format.md   # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit-tasks — NOT created here)
```

### Source Code (repository root)

```text
assets/
└── dark-slides.scss                   # NEW: RevealJS SCSS theme

teaching/mathematical-fundamentals/
├── module-1.qmd                       # EDIT: add slides link near top
├── module-2.qmd                       # EDIT: add slides link near top
├── module-3.qmd                       # EDIT: add slides link near top
├── module-4.qmd                       # EDIT: add slides link near top
├── module-5.qmd                       # EDIT: add slides link near top
├── module-6.qmd                       # EDIT: add slides link near top
├── module-7.qmd                       # EDIT: add slides link near top
├── module-8.qmd                       # EDIT: add slides link near top
├── module-1-slides.qmd                # NEW: EN RevealJS deck
├── module-2-slides.qmd                # NEW: EN RevealJS deck
├── module-3-slides.qmd                # NEW: EN RevealJS deck
├── module-4-slides.qmd                # NEW: EN RevealJS deck
├── module-5-slides.qmd                # NEW: EN RevealJS deck
├── module-6-slides.qmd                # NEW: EN RevealJS deck
├── module-7-slides.qmd                # NEW: EN RevealJS deck
└── module-8-slides.qmd                # NEW: EN RevealJS deck (revision)

fr/
└── teaching/
    └── mathematical-fundamentals/
        ├── module-1-slides.qmd        # NEW: FR stub
        ├── module-2-slides.qmd        # NEW: FR stub
        ├── module-3-slides.qmd        # NEW: FR stub
        ├── module-4-slides.qmd        # NEW: FR stub
        ├── module-5-slides.qmd        # NEW: FR stub
        ├── module-6-slides.qmd        # NEW: FR stub
        ├── module-7-slides.qmd        # NEW: FR stub
        └── module-8-slides.qmd        # NEW: FR stub

_quarto.yml                            # EDIT: add Slides section to sidebar
```

**Structure Decision**: Single Quarto project (no sub-projects). All slide
decks live under `teaching/mathematical-fundamentals/` alongside their
reference pages. French stubs mirror the path under `fr/`. The `fr/`
directory is new; `fr/teaching/mathematical-fundamentals/` must be created.

## Complexity Tracking

No Constitution violations requiring justification. All gates pass with
standard patterns.

---

## Phase 0: Research Summary

Research complete. See [research.md](research.md) for full decision log.

| Decision | Choice |
|---|---|
| Quarto format | `format: revealjs` per-file (overrides global `format: html`) |
| Theme | New `assets/dark-slides.scss` (RevealJS vars; no Bootstrap import) |
| Navigation | Sidebar "Slides" section + "📊 Slides" link on each module reference page |
| Interactive elements | Omitted from slides; replaced by static formula + reference link |
| Freeze | Not required; no executed code in slide files |
| FR parity | 8 French stubs only; ref-page stubs are a pre-existing, out-of-scope gap |
| File naming | `module-N-slides.qmd` (EN) and mirror under `fr/` |
| Module 8 | Cross-module revision deck: 7 recap slides + method-ID slide + exam tips |

---

## Phase 1: Design

### Artifacts Generated

- [data-model.md](data-model.md) — content schema for slide files,
  theme file, stubs, and sidebar registration
- [contracts/slide-deck-format.md](contracts/slide-deck-format.md) — exact
  front matter and slide structure contract; validation criteria
- [quickstart.md](quickstart.md) — step-by-step validation guide from
  single-file smoke test to full site render

### Post-Design Constitution Re-Check

All 8 constitution and 8 teaching-standards gates pass after Phase 1 design:

- No new gates opened.
- The out-of-scope pre-existing VI violation (reference pages lack FR
  counterparts) is documented and does not block this feature.

### Implementation Order (for /speckit-tasks)

Suggested dependency order for task generation:

1. **Create `assets/dark-slides.scss`** — blocker for all slide rendering
2. **Create EN slide decks, Module 1** — canary; smoke-test rendering
3. **Create EN slide decks, Modules 2–7** — parallelisable after Module 1 passes
4. **Create EN slide deck, Module 8** — depends on Modules 1–7 for recap content
5. **Create `fr/teaching/mathematical-fundamentals/` directory**
6. **Create FR stub slide decks (all 8)** — parallelisable; depend on step 5
7. **Edit `_quarto.yml`** — add Slides sidebar section; requires all EN decks created
8. **Edit reference pages (`module-N.qmd`)** — add "📊 Slides" links; independent
9. **Full site render validation** — final gate; depends on all above
