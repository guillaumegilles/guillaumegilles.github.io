# Implementation Plan: Course Syllabus Index Pages

**Branch**: `001-course-syllabus-index` | **Date**: 2026-06-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-course-syllabus-index/spec.md`

## Summary

Every teaching course MUST expose a syllabus `index.qmd` at its root that (1)
is the first entry in its `_quarto.yml` sidebar block, (2) carries a course
description and learning objectives, (3) presents a **session outline** as a
Markdown table (`| # | Session Title | Topics Covered |`), and (4) presents a
**Recommended Literature** table (`| Author(s) | Title | Edition | Publisher/Source |`).
Each **EN-authored** syllabus also gets a French counterpart under `fr/` — a
stub (source title + a French "traduction en cours" callout + backlink to the
source). FR-authored courses are addressed by the separate language-
normalization feature (see Complexity Tracking); no `en/` tree is introduced.

**Reality correction (discovered during planning)**: all six courses already
have an `index.qmd`. This feature therefore *amends* existing files rather than
creating them. Two pre-existing defects are pulled into scope because they
directly block the syllabus requirements:

1. The `ece-proba` sidebar block references `teaching/statistics-probability/index.qmd`
   (a non-existent path) instead of the real `teaching/ece-proba/index.qmd` —
   violating Principle II and T-VIII (syllabus not registered as first entry).
2. `teaching/essca-stat/index.qmd` uses `date: today` and a per-file
   `format.html.theme: cosmo` override — violating FR-007 (`date-modified`
   required) and Principle V (styling must come from `assets/dark.scss`).

## Technical Context

**Language/Version**: Quarto Markdown (`.qmd`); Quarto CLI (project pinned via
`_quarto.yml`); Python 3.x in `.venv/` for computational cells.

**Primary Dependencies**: Quarto, `quarto-ext/shinylive` (already installed),
the global `assets/dark.scss` theme.

**Storage**: Flat files. Rendered HTML to `docs/`; computation cache in `_freeze/`.

**Testing**: `quarto render` MUST exit 0 (render gate). Per-page spot render:
`quarto render teaching/<course>/index.qmd --quiet`. No unit-test framework —
validation is render success + structural checks (tables present, links resolve).

**Target Platform**: Static site on GitHub Pages (`main` branch, `docs/` dir).

**Project Type**: Quarto content site (documentation-style), not an application.

**Performance Goals**: N/A (static HTML). Render gate is the only build signal.

**Constraints**: No server-side logic; no tracking (Principle IV); all styling
in `assets/dark.scss` (Principle V); prose wrapped at 80 chars; `_freeze/` and
`docs/` committed with sources.

**Scale/Scope**: 6 courses × (1 EN/FR syllabus amendment + 1 counterpart stub)
= 6 index amendments, up to 6 counterpart stubs, 1 sidebar fix, 1 front-matter
normalization, plus sidebar registration for any new counterpart files.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Content-First** — All changes are `.qmd` edits; no hand-written HTML
  in `docs/`. ✅
- [x] **II. Navigation registered** — Every syllabus (and any new counterpart
  stub) is registered as the first entry of its sidebar block; the broken
  `ece-proba` reference is corrected. ✅
- [x] **III. Reproducible** — `_freeze/` re-rendered and committed with sources;
  no freeze entries deleted. ✅
- [x] **IV. Privacy-First** — No scripts, cookies, or embeds added. ✅
- [x] **V. Styling contained** — The per-file `cosmo` theme override in
  `essca-stat/index.qmd` is REMOVED so the global `dark.scss` applies; no inline
  styles introduced. ✅
- [~] **VI. Bilingual parity** — EN-authored syllabi (`essca-stat`, `ai-papers`,
  `ai-dev`) get a French stub under `fr/teaching/<course>/index.qmd`, published
  via a dedicated `fr-teaching` sidebar block in `_quarto.yml` (Principle II) so
  it never 404s; `lang:` set on every file; no in-file div-toggle patterns.
  **Partial**: FR-authored courses (`inseec-finance`, `ece-proba`,
  `mathematical-analysis`) remain at root and are *not* yet brought to parity
  here; the **navbar language switcher** is also deferred. Both belong to a
  dedicated language-normalization feature (Complexity Tracking). This feature
  does **not** claim full Principle VI compliance and introduces **no** `en/`
  tree. See spec "Out of Scope / Deferred".

*For teaching pages only:*
- [x] **T-I. Content Fidelity** — No existing theory/examples/exercises removed;
  only additive syllabus sections + front-matter fixes. ✅
- [x] **T-II. Pedagogical Structure** — Syllabus pages are course overviews, not
  session content; didactic ordering of session files is untouched. ✅ (N/A)
- [x] **T-III. Audience language** — Literature entries and outlines use plain
  language. ✅
- [N/A] **T-IV. Interactive demos** — Syllabus pages carry no concept demos.
- [N/A] **T-V. Glossary** — No new symbols introduced by a syllabus.
- [N/A] **T-VI. Proof** — Syllabus pages contain no theorems.
- [N/A] **T-VII. Visual intuition** — N/A for syllabus pages.
- [x] **T-VIII. Course syllabus** — This feature *is* the T-VIII implementation:
  `index.qmd` at course root, first sidebar entry, Recommended Literature table
  with author/title/edition/publisher. ✅

**Result**: PASS with one **partial** gate (VI) carrying two justified, tracked
deviations below. Principle VI is *not* fully satisfied by this feature and is
explicitly scoped as partial parity pending the language-normalization feature.

## Project Structure

### Documentation (this feature)

```text
specs/001-course-syllabus-index/
├── plan.md              # This file
├── spec.md              # Feature spec (clarified)
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── syllabus-template.md   # Canonical index.qmd structure (content contract)
└── checklists/
    └── requirements.md  # Spec quality checklist
```

### Source Code (repository root)

```text
teaching/
├── inseec-finance/index.qmd          # amend: outline + literature tables
├── ece-proba/index.qmd               # amend + fix sidebar reference
├── essca-stat/index.qmd              # amend + normalize front matter/theme
├── mathematical-analysis/index.qmd   # amend
├── ai-papers/index.qmd               # amend (paper-style literature, FR-009)
└── ai-dev/index.qmd                  # amend (paper/online-resource literature)

fr/teaching/<course>/index.qmd        # NEW French stubs — EN-authored courses
                                      #   ONLY (essca-stat, ai-papers, ai-dev).
                                      #   FR-authored courses are deferred to the
                                      #   language-normalization feature; NO en/ tree.

_quarto.yml                           # fix ece-proba first entry; register
                                      #   the new fr/ stub files
assets/dark.scss                      # unchanged (referenced, not edited)
```

**Structure Decision**: Content site — no `src/` or `tests/`. Work is confined
to `teaching/*/index.qmd`, the three new French stub files under `fr/`, and
`_quarto.yml` sidebar registrations. The "interface contract" is the canonical
syllabus structure documented in `contracts/syllabus-template.md`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| Bilingual parity delivered as **French stubs for EN-authored courses only**; FR-authored courses left at root and not yet brought to parity | FR-008/Principle VI require parity without 404s; doing this for EN courses is cheap and safe. Bringing FR courses to parity means relocating them under `fr/` + authoring English root stubs — a site-wide migration that touches URLs, sidebars, and the post-render profile hook | Introducing an `en/teaching/...` tree was rejected (rubber-duck): it invents a *third* language convention that directly contradicts Principle VI's "English at root", making the eventual migration harder. Full translation now is out of scope |
| Bilingual counterpart created as a **stub**, only for the syllabus `index.qmd` (not the whole course) | Principle VI/FR-008 require parity so navigation never 404s; full translation of every course is a separate, much larger effort | A 404 or missing nav entry would violate Principle VI outright; full per-course translation would balloon the change set well beyond a syllabus feature |
| FR-authored courses' root language **not** normalized here (no relocation to `fr/`) | The site's existing reality predates Principle VI's layout rule; reshuffling authored languages is a dedicated migration | Forcing the rule now means relocating/retranslating large French courses — far beyond syllabus scope; tracked as a follow-on feature. Principle VI is therefore marked **partial** for this feature, not claimed as fully met |
