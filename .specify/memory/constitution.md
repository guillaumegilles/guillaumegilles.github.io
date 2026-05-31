<!--
SYNC IMPACT REPORT
==================
Version change: 1.4.1 → 1.5.0 (MINOR — added T-VIII Course Syllabus principle)
Modified principles: none
Added sections:
  - T-VIII. Course Syllabus (index.qmd as syllabus + required literature section)
Removed sections: none
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ (Constitution Check: add T-VIII gate)
  - .specify/templates/spec-template.md ✅ (no changes needed)
  - .specify/templates/tasks-template.md ✅ (no changes needed)
Follow-up TODOs: none
-->

# ggilles.dev Constitution

## Core Principles

### I. Content-First

Every page on the site MUST originate as a Quarto Markdown (`.qmd`) file.
Raw HTML pages MUST NOT be created directly in `docs/`; all HTML is
generated output. New blog posts live under `posts/` and new teaching
pages under `teaching/<course>/`. A page that is not backed by a `.qmd`
source file is considered an orphan and MUST be removed.

**Rationale**: Quarto is the single authoring layer. Bypassing it creates
invisible drift between source and output that is impossible to maintain.

### II. Single Source of Truth for Navigation

All sidebar and navbar registrations MUST live exclusively in `_quarto.yml`.
A teaching page that is not listed in the matching `website.sidebar` block
in `_quarto.yml` MUST NOT be considered published, regardless of whether
its HTML exists in `docs/`. Adding a new course requires a new sidebar
block AND a new directory under `teaching/`.

**Rationale**: `_quarto.yml` is the authoritative routing table for the
site. Undeclared pages create dead-end URLs and confuse the search index.

### III. Reproducible Rendering

The `_freeze/` directory MUST be committed alongside source changes.
Deleting a freeze entry to force re-execution is intentional and allowed,
but MUST be done deliberately (not as a side-effect of other edits). CI
and collaborators MUST be able to render the site without re-executing
Python notebooks, using only the committed freeze cache.

**Rationale**: The site embeds computational outputs (statistics,
charts). Reproducibility means anyone cloning the repo gets identical
output without running Python.

### IV. Privacy-First

The site MUST NOT include cookies, client-side tracking scripts,
third-party analytics, or fingerprinting of any kind. This commitment is
publicly stated in the page footer. Any new feature or embed (e.g., a
widget, map, or iframe) MUST be evaluated for privacy impact before
integration; features that cannot be made tracking-free MUST be excluded.

**Rationale**: The footer states "This site respects your privacy — no
cookies, no tracking." Violating this breaks an explicit public promise.

### V. Minimal & Contained Styling

All custom CSS/SCSS MUST live in `assets/dark.scss`. Inline `style=`
attributes and page-level `<style>` blocks MUST NOT be used. The
Cloudflare Worker (`worker/`) is a separate deployment artifact and MUST
NOT be entangled with Quarto build steps. Math MUST use standard LaTeX
syntax (`$...$` / `$$...$$`). Callout blocks MUST use Quarto's native
`.callout-*` divs with consistent semantics across the whole site:

| Type | Use for |
|---|---|
| `.callout-note` | Definitions, background information |
| `.callout-tip` | Key formulas, practical shortcuts |
| `.callout-warning` | Remarks, caveats, common mistakes |
| `.callout-important` | Exam tips, critical rules |
| `.callout-caution` | Exercises (with `collapse="true"` for solutions) |

**Rationale**: A single styling entry point and consistent callout semantics
prevent conflicting overrides and ensure readers can rely on visual cues
having the same meaning across blog posts and teaching pages.

### VI. Bilingual Content Strategy (EN + FR Parity)

The site is fully bilingual — every published page MUST exist in both
English and French. Content language MUST be declared via `lang:` in
every `.qmd` file's front matter (`lang: fr` or `lang: en`).

**Structure**: The folder-per-language pattern is the only accepted
implementation. English lives at the site root; French lives under `fr/`,
mirroring the root structure exactly:

```
index.qmd              → /          (English)
fr/index.qmd           → /fr/       (French)
posts/my-post/index.qmd       → /posts/my-post/
fr/posts/my-post/index.qmd    → /fr/posts/my-post/
teaching/ece-proba/...        → /teaching/ece-proba/
fr/teaching/ece-proba/...     → /fr/teaching/ece-proba/
```

**Parity rules**:
- Every page at path `/X` MUST have a counterpart at `/fr/X` and vice versa.
- A page that has not yet been translated MUST NOT be silently absent.
  It MUST instead render a stub page in the target language with a
  "translation in progress" notice and a link to the available-language version.
- Teaching materials retain their language of instruction as the primary
  version but MUST still have a stub or full translation in the other language.
- A language switcher MUST appear in the navbar, linking between the
  current page's EN and FR counterparts.
- **Content MUST NOT be partially translated within a single `.qmd` file**
  using CSS/JS div toggles. Full-page bilingual variants (separate `.qmd`
  files) are the only accepted pattern.

**Rationale**: Quarto has no native i18n engine. The folder-per-language
pattern is the only approach officially supported and predictable across
renders. Per-page `lang:` front matter ensures correct HTML `lang`
attribute, accessible typography, and proper hyphenation. Stubs prevent
broken navigation and signal outstanding translation work clearly.

## Teaching Materials Standards

These standards apply to all course materials under `teaching/`. They
complement the Core Principles and MUST be verified for every teaching
page created or modified.

### T-I. Content Fidelity

Every course session contains canonical theory, examples, and exercises
that MUST be preserved across edits. Additions and refinements are
welcome, but core theory, worked examples, and exercises MUST NOT be
removed. The canonical source material is the authoritative reference;
divergence MUST be explicitly justified in a commit message.

### T-II. Pedagogical Structure (NON-NEGOTIABLE)

Every session file MUST follow the established didactic order:
**theory first → worked examples → exercises with collapsible solutions**.
Content MUST NOT be flattened into undifferentiated prose. Each major
concept MUST be introduced before it is used in an example or exercise.

### T-III. Audience-Appropriate Language

Course materials target undergraduate and graduate business school
students — not statisticians or engineers. Language MUST be plain and
direct. Jargon MUST NOT be introduced beyond what the course syllabus
defines. Every formula MUST be accompanied by a plain-language
explanation of what it computes and why it matters.

### T-IV. Interactive Demonstrations

Priority concepts in each course MUST have a Shinylive interactive demo
(`{shinylive-python}` block). Where a demo has not yet been built, a
`.callout-important` block with a `TODO:` label MUST mark the gap so
missing demos are trackable.

### T-V. Glossary

Every course MUST maintain a central `glossary.qmd` file. Every
mathematical symbol and formula introduced in any session MUST be listed
there with: its notation, a plain-language definition, and — for Greek
letters — a pronunciation guide. The glossary MUST be linked from the
course sidebar.

### T-VI. Proof and Demonstration

Each session MUST include at least one formal proof or step-by-step
derivation for its central theorem, formula, or concept. The proof MUST
be collapsible (`.callout-caution` with `collapse="true"`) so it does not
interrupt the flow for students who skip it.

### T-VII. Visual and Geometric Intuition

Wherever a statistical or mathematical concept has a geometric
interpretation, that interpretation MUST be surfaced. Examples: linear
regression as projection onto a subspace, correlation as the cosine of
an angle between vectors, variance as squared distance from the mean.
This principle aligns course content with modern data science pedagogy
and builds durable intuition.

### T-VIII. Course Syllabus

Every course MUST have an `index.qmd` at its root
(`teaching/<course>/index.qmd`) that serves as the course syllabus.
This file MUST be the first entry in the course sidebar block in
`_quarto.yml`. The syllabus MUST include:

- A brief course description and learning objectives.
- A session outline (table or list) linking to each session file.
- A **Recommended Literature** section listing the primary textbook(s)
  and any supplementary references used across the course. Each entry
  MUST include at minimum: author(s), title, edition, and publisher.

A course `index.qmd` that does not contain a Recommended Literature
section MUST be considered incomplete and MUST NOT be considered
published.

**Rationale**: The syllabus is the student's entry point to the course.
Centralising the literature list there prevents references from being
scattered across individual session files and ensures students always
know what to read before starting.

## Technology Stack

| Layer | Tool / Service | Constraint |
|---|---|---|
| Authoring | Quarto | Sole content pipeline |
| Output dir | `docs/` | Committed; served by GitHub Pages |
| Python env | `.venv/` + `requirements.txt` | MUST NOT be committed |
| Computation cache | `_freeze/` | MUST be committed |
| Interactive widgets | Shinylive (`quarto-ext/shinylive`) | Teaching pages only; `{shinylive-python}` blocks |
| Edge function | Cloudflare Worker (`worker/`) | Deployed independently via `wrangler` |
| Hosting | GitHub Pages (`main` branch, `docs/` dir) | No server-side logic |
| Comments | Giscus (auto-injected via `posts/_metadata.yml`) | Blog-only; no per-file config |
| Theme | `assets/dark.scss` | Only styling entry point |

New runtime dependencies MUST be justified against the privacy principle
and MUST NOT introduce server-side state into the static hosting layer.

## Development Workflow

- **Render gate**: `quarto render` MUST exit 0 before any commit that
  touches `.qmd` sources, `_quarto.yml`, or `assets/`. Both EN and FR
  render targets MUST pass. `docs/` and `_freeze/` MUST be committed in
  the same commit as the source changes that produced them.
- **Post-render hook**: `scripts/update-profile-readme.sh` runs
  automatically after `quarto render`; do not suppress or skip it.
- **Branch strategy**: Use short-lived feature branches for non-trivial
  changes. Direct commits to `main` are acceptable for small content edits.
- **Worker deploys**: `cd worker && wrangler deploy` is the sole deployment
  path for the Cloudflare Worker. Never deploy the worker from a Quarto
  build step.
- **No secrets in source**: API keys, tokens, and credentials MUST NOT
  appear in `.qmd` files, `_quarto.yml`, or `worker/` source. Use
  Cloudflare Worker environment variables or GitHub Actions secrets.
- **Line width**: Source `.qmd` files MUST wrap prose at 80 characters.
  Code blocks and long URLs are exempt.

## Governance

This constitution supersedes all other conventions described in ad-hoc
comments or README sections. Amendments require:

1. A clear rationale (principle addition, removal, or clarification).
2. A version bump following semantic versioning:
   - **MAJOR** — removal or redefinition of an existing principle.
   - **MINOR** — new principle or section added.
   - **PATCH** — wording clarification, typo fix, non-semantic refinement.
3. Updated `LAST_AMENDED_DATE`.
4. A sync pass over `_quarto.yml`, `posts/_metadata.yml`, and any
   `.specify/templates/` files affected by the change.

The site owner (Guillaume Gilles) holds sole amendment authority.
All Copilot-assisted changes MUST be validated against these principles
before merging.

**Version**: 1.5.0 | **Ratified**: 2026-05-31 | **Last Amended**: 2026-05-31
