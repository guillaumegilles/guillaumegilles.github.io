# Implementation Plan: Giscus Retro Blackboard Theme Integration

**Branch**: `003-giscus-theme-integration` | **Date**: 2026-06-19 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/003-giscus-theme-integration/spec.md`

## Summary

Replace the default giscus light/dark widget appearance with a custom CSS theme
that maps every giscus CSS custom property to the Retro Blackboard design tokens
defined in `assets/dark.scss`. The theme is delivered as a single plain-CSS file
(`assets/giscus-retro-blackboard.css`) hosted alongside the site, referenced by a
full `https://` URL in `posts/_metadata.yml`. No JavaScript, no SCSS processing, and
no per-post changes are required. FOUC prevention is provided by giscus's own
three-layer mechanism (SSR `<link>` injection + `opacity:0` iframe + double-buffered
dynamic swap).

## Technical Context

**Language/Version**: Plain CSS (Level 4 custom properties); Quarto 1.x site pipeline

**Primary Dependencies**:
- giscus — external comment widget iframe; provides the CSS custom property theming
  API and a three-layer FOUC prevention mechanism
- Quarto — static site generator; copies files listed under `project.resources` to
  `docs/` verbatim; compiles `assets/dark.scss` into site_libs (not a public URL)
- GitHub Pages — serves `docs/` at `https://ggilles.dev`

**Storage**: N/A — one static CSS file, no runtime state

**Testing**: Browser visual inspection (Chrome/Firefox/Safari); contrast ratio check
with browser devtools; FR list review against rendered post page

**Target Platform**: GitHub Pages static hosting; modern evergreen browsers (no IE11)

**Project Type**: Static website styling asset

**Performance Goals**: Custom theme CSS ≤ 15 KB; no perceptible additional load time
(file served from same origin as site; giscus already fetches a theme stylesheet on
every page load)

**Constraints**:
- CSS file must be a standalone, parseable plain-CSS file — no SCSS, no `@import`,
  no build step
- File must be served at a stable, publicly accessible HTTPS URL before the giscus
  iframe loads (required by giscus's server-side SSR theme injection)
- All property declarations must sit on the `main {}` selector inside the giscus
  iframe (required by giscus's custom property scoping)
- Must not add cookies, tracking pixels, or fingerprinting (Constitution IV)

**Scale/Scope**: 1 new CSS file (~150–200 lines); 1 config line changed in
`posts/_metadata.yml`; 1 line added to `_quarto.yml` `project.resources`

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Content-First** — No `.qmd` pages created or modified; this feature
  produces only a CSS styling asset and two config-file edits.
- [x] **II. Navigation registered** — No new teaching pages or sidebar entries.
- [x] **III. Reproducible** — No computational outputs; `_freeze/` is unaffected.
  The CSS file is a static asset with no execution.
- [x] **IV. Privacy-First** — giscus is already listed in the constitution tech
  stack. The custom CSS file contains only colour and typography declarations — no
  tracking scripts, pixels, or third-party resource loads beyond those already
  initiated by giscus itself. Loading-spinner images reference GitHub's own CDN
  (`github.githubassets.com`) which giscus already uses.
- [x] **V. Styling contained** — JUSTIFIED EXCEPTION documented in Complexity
  Tracking. `assets/dark.scss` remains the sole source for the host-page styles.
  The giscus theme is necessarily a separate file (see Complexity Tracking).
- [x] **VI. Bilingual parity** — No new pages. The giscus widget appears on all
  posts in both EN (`posts/`) and FR (`fr/posts/`) automatically; no language-
  specific theming is needed since the site is dark-only.

*Teaching principles T-I through T-VIII: not applicable — this feature does not
touch any teaching pages or course materials.*

**Post-Phase-1 re-check**: ✅ No new violations introduced by the design phase.

## Project Structure

### Documentation (this feature)

```text
specs/003-giscus-theme-integration/
├── plan.md              ← this file
├── research.md          ← Phase 0 output
├── data-model.md        ← Phase 1 output
├── quickstart.md        ← Phase 1 output
├── contracts/
│   └── giscus-theme-css.md   ← Phase 1 output
└── tasks.md             ← Phase 2 output (/speckit.tasks — not created here)
```

### Source Code (repository root)

```text
assets/
├── dark.scss                       # UNCHANGED — host-page styles only
└── giscus-retro-blackboard.css     # NEW — giscus custom theme (plain CSS)

posts/
└── _metadata.yml                   # EDIT — add comments.giscus.theme URL

_quarto.yml                         # EDIT — add assets/giscus-retro-blackboard.css
                                    #        to project.resources so Quarto copies
                                    #        it to docs/assets/ verbatim
```

**Structure Decision**: Single-file styling asset. All changes are in the `assets/`
directory and two configuration files. No new directories, no new routes, no new
`.qmd` sources. The CSS file lives alongside `dark.scss` for discoverability.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| **V. Styling**: separate `assets/giscus-retro-blackboard.css` file alongside `dark.scss` | giscus fetches the theme file via HTTP and injects it into its iframe as a `<link>` stylesheet; `dark.scss` is compiled by Quarto into `docs/site_libs/` at a non-deterministic hash-suffixed path — not a stable public URL. A separate plain-CSS file at `docs/assets/giscus-retro-blackboard.css` is the only way to satisfy giscus's requirement of an accessible `https://` URL. | Inlining into `dark.scss` would not work: (1) the compiled output is not at `docs/assets/dark.css`; (2) even if accessed, SCSS source is not valid CSS and giscus does not compile SCSS; (3) mixing giscus iframe variables into the host-page stylesheet creates a maintenance hazard with zero benefit. |
