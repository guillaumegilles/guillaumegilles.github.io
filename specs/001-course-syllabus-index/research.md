# Phase 0 Research: Course Syllabus Index Pages

All open questions from the feature spec were resolved during `/speckit.clarify`
(literature table format, session-outline table format, FR stub content). The
remaining unknowns surfaced during planning are repository-state realities, not
spec ambiguities. Each is resolved below.

## R1. Do the six courses already have an `index.qmd`?

- **Decision**: Yes — all six (`inseec-finance`, `ece-proba`, `essca-stat`,
  `mathematical-analysis`, `ai-papers`, `ai-dev`) already have an `index.qmd`.
  The feature *amends* these files; it does not create them.
- **Rationale**: Direct inspection (`ls teaching/*/index.qmd`) returned all six.
  The spec's Assumptions section guessed three were missing — that guess is
  superseded by this finding.
- **Alternatives considered**: Creating new index files — rejected; would
  duplicate/overwrite existing course overviews and violate T-I (content fidelity).

## R2. Is each syllabus correctly registered as the first sidebar entry?

- **Decision**: Five of six are correct. The `ece-proba` block points to
  `teaching/statistics-probability/index.qmd` and `.../univariate.qmd`, neither
  of which exists; the real file is `teaching/ece-proba/index.qmd`. Fix the
  reference to the real path.
- **Rationale**: Principle II + T-VIII require the syllabus to be the registered
  first entry. A dangling reference means the syllabus is effectively
  unpublished and the sidebar head is a dead link.
- **Alternatives considered**: Creating a `teaching/statistics-probability/`
  directory to match the sidebar — rejected; that invents a phantom course and
  orphans the real `ece-proba/index.qmd` (Principle I).

## R3. What front-matter normalization is required (FR-007)?

- **Decision**: Bring every syllabus to a common minimum: `title`,
  `date-modified`, and `lang` (`fr` or `en`). Specifically:
  - `inseec-finance/index.qmd` — **add a front-matter block** (currently starts
    with a bare `#` heading, no YAML). `lang: fr`.
  - `essca-stat/index.qmd` — replace `date: today` with `date-modified`, and
    **remove the per-file `format.html.theme: cosmo` override** so the global
    `assets/dark.scss` applies (Principle V). `lang: en`.
  - `ai-papers/index.qmd` — add `date-modified`, `lang: en`; clean the stray
    draft placeholder block (the `::: ` list of raw notes) so the page renders
    cleanly.
  - `ai-dev/index.qmd` — add `lang: en` (already has `title`, `date-modified`).
  - `mathematical-analysis/index.qmd` — add `lang: fr` (already has dates).
  - `ece-proba/index.qmd` — add `lang: fr` (already has `title`, `date-modified`).
- **Rationale**: FR-007 mandates `title` + `date-modified` + `lang`; Principle V
  forbids per-file theme overrides; Principle IV/V favor a single styling source.
- **Alternatives considered**: Leaving `cosmo` on `essca-stat` — rejected; it
  produces an inconsistent light theme inside a dark-themed site and violates V.

## R4. Literature format for paper/seminar courses (FR-009)?

- **Decision**: For `ai-papers` (and the AI portions of `ai-dev`), the
  Recommended Literature table maps columns to
  `| Author(s) | Title | Year | Publication Venue |` (papers) and may include
  canonical books where applicable. Mixed book + paper tables are allowed; each
  section keeps a single consistent column set.
- **Rationale**: FR-005 + FR-009 already define this mapping; paper-reading
  courses have no "edition/publisher" but do have year/venue.
- **Alternatives considered**: Forcing book columns on papers — rejected;
  "Edition"/"Publisher" are meaningless for a conference paper.

## R5. Bilingual counterpart direction per course (Principle VI / FR-008)?

- **Decision**: Create a **French stub** counterpart **only for EN-authored
  courses** (`essca-stat`, `ai-papers`, `ai-dev`) at
  `fr/teaching/<course>/index.qmd`. **Do NOT** create an `en/` tree for the
  FR-authored courses (`inseec-finance`, `ece-proba`, `mathematical-analysis`);
  their parity is deferred to the separate language-normalization feature.
  - Each stub: source title as Quarto `title`, `lang: fr`, a `.callout-note`
    "traduction en cours / translation in progress" block, and a Markdown link
    back to the source syllabus.
  - Every stub is registered in `_quarto.yml` and verified to render and link
    correctly (no 404, valid backlink).
- **Rationale**: FR-008 requires a counterpart so navigation never 404s; a stub
  is explicitly acceptable for the initial merge (spec Assumptions). Introducing
  an `en/teaching/...` tree was **rejected** during plan review: it creates a
  third, non-constitutional language convention that contradicts Principle VI's
  "English at root" and makes the eventual migration harder. This feature
  therefore delivers **partial** Principle VI parity and says so plainly.
- **Alternatives considered**:
  - `en/teaching/...` stubs for FR courses — rejected (contradicts Principle VI;
    rubber-duck flagged as blocking).
  - Full translation of all six syllabi now — rejected; out of scope, high
    effort, not required for the syllabus feature's value.
  - Relocating FR courses to `fr/` now — rejected; massive change unrelated to
    syllabi; deferred to the language-normalization feature.
  - No counterpart at all — rejected; violates Principle VI and FR-008.

## R5b. Session-outline links that point outside the course directory?

- **Decision**: The session-outline table requirement is satisfied by **links
  that resolve to existing referenced resources**, regardless of directory
  locality. `essca-stat` lists its sessions under a top-level `sessions/`
  directory (`sessions/session-NN.qmd`), not under `teaching/essca-stat/`; its
  outline table links to those exact paths.
- **Rationale**: FR-003 requires links to "every session page in the course";
  it does not require course-local paths. Validation checks link *resolution*,
  not folder location, to avoid false failures.
- **Alternatives considered**: Requiring all session files under
  `teaching/<course>/` — rejected; would force relocating `sessions/` (out of
  scope) and contradicts the existing, working sidebar.

## R6. How is success verified without a test framework?

- **Decision**: The acceptance signal is `quarto render` exiting 0 (full build)
  plus per-file spot renders, combined with structural assertions: each
  `index.qmd` contains a "Recommended Literature" heading followed by a table,
  a session-outline table, and required front matter; each counterpart stub
  renders and links resolve.
- **Rationale**: Matches the constitution's render gate (Development Workflow)
  and SC-001..SC-005.
- **Alternatives considered**: Adding a markdown linter / link checker —
  rejected; "do not add new tooling unless necessary." Render + grep suffices.

**Output**: All NEEDS CLARIFICATION resolved. Ready for Phase 1.
