# Implementation Plan: 3-Day Lecture Slide Deck for the Financial Analysis Course

**Branch**: `014-financial-analysis-slides` | **Date**: 2026-10-18 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/014-financial-analysis-slides/spec.md`

## Summary

Build three French RevealJS decks, one per 6-hour course day, in
`fr/teaching/financial-analysis/slides/`. The decks follow the original
`inseec-analyse-financiere.pptx` progression (Banque de France, cotation,
six-step analysis of consolidated accounts) and add a Day-1 fundamentals block
(SIG, CAF, bilan fonctionnel, ratios, effet de levier). Material comes from the
other files in the folder (COURS M1, LES RATIOS, formula sheet, cases CP1–CP4
and CONCOURSMANIA/LECTRA, Vernimmen letters).

Every image-only slide is rebuilt as text, tables or Mermaid diagrams. Every
year-dependent fact is checked against current official sources (see
[research.md](research.md)). Exercise slides carry briefs only and name their
answer-key document. Each block points to its syllabus quest. The site gains
a French sidebar block, English stubs and links from the course syllabus. An
internal coverage map in `specs/` records where every original slide, source
file, definition choice, verified fact and answer key went.

## Technical Context

**Language/Version**: Quarto 1.10.19 (`/opt/quarto`), Markdown `.qmd`, RevealJS output

**Primary Dependencies**: Quarto's bundled RevealJS. Quarto's bundled Mermaid
11.12.0 (supports `flowchart`, `quadrantChart` and `xychart-beta`). The existing
theme `assets/dark-slides.scss`.

**Storage**: Static `.qmd` sources. HTML output in `docs/`.

**Testing**: `quarto render <file> --quiet` (exit 0). A link check of the
rendered decks. A timing-sum check (non-optional blocks = 360 min per day). The
visual and dry-run checks in [quickstart.md](quickstart.md).

**Target Platform**: Classroom projector (16:9, full screen) and student
laptops, in any modern browser. GitHub Pages.

**Project Type**: Static teaching website (Quarto). This feature adds lecture
decks alongside reference pages.

**Performance Goals**: Each deck loads in under 3 s on a campus connection. No
executed code. Mermaid renders client-side.

**Constraints**:

- No embedded third-party images or videos (FR-022). Videos are links only,
  which also satisfies Constitution IV.
- No solutions in decks (FR-021).
- No inline `style=` or `<style>`. Use RevealJS built-in classes only
  (`.smaller`, `.scrollable`, `.fragment`, `.columns`, `.notes`, `.aside`).
- Callouts only in their constitutional roles.
- French text. The language comes from `fr/teaching/_metadata.yml` and is not
  repeated in the files.
- Each day's non-optional timings total exactly 360 min.

**Scale/Scope**: 3 FR decks (about 60–90 slides each). 1 `slides/_metadata.yml`.
3 EN stubs and 1 EN `slides/_metadata.yml`. `_quarto.yml` (new FR sidebar
block plus the repaired EN block). 1 edit to `fr/teaching/financial-analysis/index.qmd`.
1 coverage map and 1 fact log in `specs/`. About 12 files.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Content-First**: All decks and stubs are `.qmd`. Nothing is written
  to `docs/` by hand.
- [x] **II. Navigation registered**: A new `fr-financial-analysis` sidebar
  block lists `index.qmd` first, then a **Diapositives** section with the
  3 decks. The broken EN block (`inseec-finane` → missing
  `teaching/inseec-finance/index.qmd`) is repaired to point at
  `teaching/financial-analysis/index.qmd` and the 3 EN stubs.
- [x] **III. Reproducible**: No executed code, so no `_freeze/` entries.
- [x] **IV. Privacy-First**: No embeds. YouTube or BdF videos are plain links.
  Mermaid is bundled locally.
- [x] **V. Styling contained**: The decks reuse `assets/dark-slides.scss`
  unchanged. Callouts are used by role:
  - `note`: definitions
  - `tip`: formulas
  - `caution`: derivations
  - `warning`: one common mistake per deck
  - `important`: `TODO: à vérifier` markers

  Exercises use `::: {#exr-…}`. Focus boxes are plain blockquotes. Sources go
  in `::: aside`. See Complexity Tracking for the slides theme file.
- [x] **VI. Bilingual parity**: Each FR deck at
  `fr/teaching/financial-analysis/slides/jour-N.qmd` has an EN stub at
  `teaching/financial-analysis/slides/jour-N.qmd` with a "translation in
  progress" notice and a link to the French deck.

*For teaching pages only:*

- [x] **T-I. Content Fidelity**: Additive. Reference pages and quests are
  untouched, except for one links section in `index.qmd`. All original deck
  content is carried over or logged as dropped (FR-009).
- [x] **T-II. Pedagogical Structure**: Each block runs concept → formula with a
  prose explanation → worked example → exercise brief (FR-005). **Deviation**:
  no folded solutions in the slides (Q3 clarification). See Complexity Tracking.
- [x] **T-III. Audience language**: Plain French. Every formula is followed by
  a one-line prose explanation (US4-3).
- [x] **T-IV. Interactive demos**: N/A for the decks, which are static by
  design (precedent: spec 007). Demos belong on the reference pages (spec 013).
- [x] **T-V. Glossary**: The decks add no new notation beyond the course
  formula sheet. The course still has no `glossary.qmd`. This is a pre-existing
  gap tracked by spec 013 and does not block this feature.
- [x] **T-VI. Proof/derivation**: Each deck has at least one `.callout-caution`:
  - Day 1: the leverage identity ROE = ROCE + (ROCE − i)·D/CP
  - Day 2: RNR from RCAI under the 25 % convention
  - Day 3: FPNR and the 10× RNR cap on écart d'acquisition élargi
- [x] **T-VII. Visual intuition**:
  - The effet de levier is shown as a line chart (`xychart-beta`).
  - The bilan fonctionnel is shown as a two-column balance.
  - The liquidity verdict is shown as a 2×2 matrix (`quadrantChart` or table).
- [x] **T-VIII. Course syllabus**: The existing `index.qmd` stays first in the
  sidebar and keeps its Recommended Literature section. Only a slides links
  section is added. Its incomplete literature entries are spec 013's scope.

*All gates pass with the two justified items below. Proceeding to Phase 0.*

## Project Structure

### Documentation (this feature)

```text
specs/014-financial-analysis-slides/
├── spec.md
├── sources.md              # source inventory (from /speckit-specify)
├── plan.md                 # this file
├── research.md             # Phase 0: technical decisions + verified-fact log
├── data-model.md           # Phase 1: deck / block / slide / exercise entities
├── quickstart.md           # Phase 1: validation guide
├── contracts/
│   ├── slide-deck-format.md   # front matter, slide roles, markup rules
│   └── day-plans.md           # block-by-block agenda with timings, sources, quests
├── coverage-map.md         # created during implementation (FR-009/012/014a/020/021)
└── tasks.md                # Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
fr/teaching/financial-analysis/
├── index.qmd                     # EDIT: add "Diapositives" links section
└── slides/
    ├── _metadata.yml             # NEW: revealjs format + theme (copy of math-fundamentals pattern)
    ├── jour-1.qmd                # NEW: Fondamentaux de l'analyse financière
    ├── jour-2.qmd                # NEW: Banque de France, cotation, étapes 1–3
    └── jour-3.qmd                # NEW: Étapes 4–6, veille, ESG, synthèse

teaching/financial-analysis/
└── slides/
    ├── _metadata.yml             # NEW: same revealjs format (keeps stubs as decks)
    ├── jour-1.qmd                # NEW: EN stub → links to /fr/.../slides/jour-1.html
    ├── jour-2.qmd                # NEW: EN stub
    └── jour-3.qmd                # NEW: EN stub

_quarto.yml                       # EDIT: add fr-financial-analysis sidebar; repair EN block
```

**Structure Decision**: Single Quarto project. The decks sit in a `slides/`
subfolder of the French course, with a local `_metadata.yml`. This mirrors
`fr/teaching/mathematical-fundamentals/slides/` and avoids the dual HTML and
RevealJS render warned about in `fr/teaching/_metadata.yml`. The EN stubs
mirror the path so the language switcher resolves (Constitution VI).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| T-II: no folded solutions in decks | Clarification Q3. Answer keys stay in instructor documents so the cases can be reused for grading. | Folded `<details>` answers would publish the solutions on a public site. |
| V: theme lives in `assets/dark-slides.scss`, not `dark.scss` | Pre-existing, accepted in spec 007. RevealJS needs its own SCSS variables, and `dark.scss` uses Bootstrap ones. No new rules are added. | Merging into `dark.scss` breaks one of the two render targets. |

## Phase 0: Research Summary

See [research.md](research.md).

| Decision | Choice |
|---|---|
| Deck location and names | `fr/teaching/financial-analysis/slides/jour-{1,2,3}.qmd`, plus EN stubs at the mirrored path |
| Diagrams | Mermaid (bundled 11.12): `flowchart` for organigrammes and the method, `xychart-beta` for the cote distribution and leverage, Markdown tables for grids |
| Sources on slides | `::: aside` with publisher and date. Third-party content is rebuilt, never embedded |
| Exercises | `::: {#exr-…}` with the brief only. Speaker notes name the answer key and timing |
| "À vérifier" | `.callout-important` with `TODO: à vérifier`. The decks must have zero of these before publishing |
| Tax convention | 25 % (RNR = ¾ RCAI; CAFr = ¾ RCAI + dotations nettes). Old ⅓ keys are flagged |
| Verified facts | Seuil de cotation 1 250 K€ (since 12/01/2025). Default rates on the 22-grade scale (BdF 2025 report). Consolidation thresholds 30/60/250 (from 1/1/2025). ANC 2020-01 replaces CRC 99-02 |
| Case data | Lectra SA 2016 social accounts from `lectra.com` (Rapport financier 2016). ConcoursMania SA 2016 social accounts are not yet located, so the fallback applies |

## Phase 1: Design

- [data-model.md](data-model.md): entities and validation rules.
- [contracts/slide-deck-format.md](contracts/slide-deck-format.md): markup contract for decks and stubs.
- [contracts/day-plans.md](contracts/day-plans.md): the 3 day plans (blocks, minutes, sources, quests, exercises).
- [quickstart.md](quickstart.md): validation steps.

### Post-Design Constitution Re-Check

Re-evaluated after Phase 1. No new violations. Both Complexity Tracking items
still apply. One design note: Q6 (listed vs unlisted) and Q8 (financial plan)
were not in FR-003a's list but also lack a full lecture block. The day plans
map them as pointers: Q8 → Day 3 analyse prospective (FTD), Q6 → Day 3
décision de cotation / synthèse. The coverage map flags them for review.

### Implementation Order (for /speckit-tasks)

1. Scaffolding: `slides/_metadata.yml` (FR and EN), sidebar blocks, empty decks. Run a smoke render.
2. `coverage-map.md` skeleton and fact log. Copy the verified facts from research.md.
3. Day 1 deck (canary): fundamentals, effet de levier derivation, CONCOURSMANIA/LECTRA data tables.
4. Day 2 deck: BdF condensed, cotation (current scale), consolidation, steps 1–3, BMC input.
5. Day 3 deck: steps 4–6, IFRS 16 then/now, focus boxes, regulatory watch and ESG input, wrap-up.
6. EN stubs, `index.qmd` links section.
7. Validation per quickstart: renders, links, timing sums, zero `TODO: à vérifier`, no embeds, dry run.
