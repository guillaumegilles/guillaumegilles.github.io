# Implementation Plan: Dynamic Course Listing

**Branch**: `002-dynamic-course-listing` | **Date**: 2026-06-11 | **Spec**: `specs/002-dynamic-course-listing/spec.md`

**Input**: Transform `teaching.qmd` into an automated course listing page that discovers and displays all course index pages from the `teaching/` directory, organized into Graduate, Undergraduate, and AI Guide sections.

**Note**: This plan defines the design and implementation strategy for converting static course listings to dynamic discovery and display.

## Summary

Replace the hardcoded course grid in `teaching.qmd` with an automated system that discovers all `index.qmd` files in `teaching/` subdirectories, extracts metadata, categorizes them into three sections (Graduate, Undergraduate, AI Guide), and renders them as grid cards. This eliminates manual configuration, ensures new courses appear automatically, and provides a scalable foundation for future course management features.

## Technical Context

**Language/Version**: Quarto markdown (`.qmd`) with YAML front matter, targeting HTML output via Quarto rendering

**Primary Dependencies**: 
- Quarto >= 1.4 (for listings support with grid type)

**Storage**: File-based — course metadata stored in `index.qmd` YAML front matter; no database required

**Testing**: Quarto render validation + visual inspection of HTML output; Giscus comments enabled via `_metadata.yml`

**Target Platform**: Static HTML site served via GitHub Pages (output in `docs/` directory)

**Project Type**: Static site generator with Quarto; documentation/educational content website

**Performance Goals**: Page load time < 2 seconds for 6 courses; scalable to 50+ courses without degradation

**Constraints**: 
- Must use Quarto's native listings feature (no custom Lua filters or JavaScript)
- All styling in `assets/dark.scss` (no inline styles)
- Must work with existing `_quarto.yml` sidebar configuration
- Course discovery must be reproducible across CI/CD pipelines
- Listings only display `index.qmd` files (requires glob filtering)

**Scale/Scope**: 
- Current: 6 courses (1 Graduate, 3 Undergraduate, 2 AI Guide)
- Future-ready: supports 50+ courses without architectural change

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify the following before proceeding:

- [x] **I. Content-First** — All changes are to `.qmd` source files (teaching.qmd); no direct HTML in `docs/`.
- [x] **II. Navigation registered** — Teaching page is already registered in `_quarto.yml`; this feature doesn't add new nav entries, just transforms the existing page.
- [x] **III. Reproducible** — No computation-heavy code blocks requiring freeze; existing freeze entries are unchanged.
- [x] **IV. Privacy-First** — No tracking scripts, cookies, or fingerprinting. Giscus comments already enabled via `_metadata.yml`.
- [x] **V. Styling contained** — All CSS/SCSS in `assets/dark.scss`; Quarto grid classes are built-in.
- [x] **VI. Bilingual parity** — Not applicable; teaching.qmd is EN-only per current project structure.

*For teaching pages only:*
- [x] **T-I. Content Fidelity** — No content changes; this is a presentation layer update.
- [x] **T-II. Pedagogical Structure** — Maintains existing course structure and sidebar organization.
- [x] **T-III. Audience language** — Not applicable; no new content text.
- [x] **T-IV. Interactive demos** — Not applicable; this is a listing page.
- [x] **T-V. Glossary** — Not applicable; no new terms introduced.
- [x] **T-VI. Proof** — Not applicable; no mathematical content.
- [x] **T-VII. Visual intuition** — Grid layout provides visual discovery of courses.
- [x] **T-VIII. Course syllabus** — Not applicable; this lists course indices, not modifying course content.

**Gate Result**: ✅ **PASS** — All constraints satisfied. No constitution violations.

## Project Structure

### Documentation (this feature)

```text
specs/002-dynamic-course-listing/
├── plan.md              # This file
├── spec.md              # Feature specification
├── research.md          # Phase 0: Research findings (in progress)
├── data-model.md        # Phase 1: Data structure & metadata schema
├── quickstart.md        # Phase 1: Implementation guide
├── contracts/           # Phase 1: Interface contracts (if applicable)
└── tasks.md             # Phase 2: Actionable tasks (via /speckit.tasks)
```

### Source Code (repository root)

```text
teaching.qmd                         # MAIN: Transform from static to dynamic listing
teaching/                            # Discovery source: subdirectories with index.qmd
├── ai-dev/index.qmd
├── ai-papers/index.qmd
├── ece-proba/index.qmd
├── essca-stat/index.qmd
├── inseec-finance/index.qmd
└── mathematical-analysis/index.qmd

_quarto.yml                          # Already configured; sidebars unchanged
assets/dark.scss                     # Styling (no changes needed; uses standard grid classes)
```

**Structure Decision**: This is a **single-file transformation** (teaching.qmd) + **discovery mechanism** over existing course directories. No new files or directories are created; the feature is purely presentational — replacing Quarto Lua filter logic or shortcode-based discovery of `index.qmd` files in `teaching/`.

**Implementation Approach**:
1. Generate course listing dynamically using Quarto's templating or scripting capabilities
2. Option A: Lua filter to discover files + inject HTML (most Quarto-native)
3. Option B: Python preprocessing script that generates `.qmd` include files before render
4. Option C: Inline shortcodes with JavaScript (if Quarto extension available)

Research Phase 0 will determine the optimal approach.

## Complexity Tracking

> **No constitution violations.** This section is N/A.

All design decisions are straightforward and within project constraints:
- **Single-file transformation**: Only `teaching.qmd` is modified
- **No new dependencies**: Uses Quarto's built-in capabilities (grid classes, metadata extraction)
- **No database or external services**: File-based discovery only
- **Backward compatible**: Existing course sidebars in `_quarto.yml` remain unchanged
- **Reproducible**: No computational code blocks; discovery is deterministic and CI/CD-friendly
