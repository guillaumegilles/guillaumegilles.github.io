# Phase 1 Data Model: Course Syllabus Index Pages

This feature has no database. The "data model" is the structured content
contract every course syllabus `index.qmd` must satisfy, plus the bilingual
counterpart relationship.

## Entity: Course Syllabus (`index.qmd`)

The root document of a course. One per course directory under `teaching/`.

| Field | Source | Required | Rules |
|---|---|---|---|
| `title` | front matter | Yes | Human-readable course title |
| `lang` | front matter | Yes | `fr` or `en`; matches authored language |
| `date-modified` | front matter | Yes | ISO date; replaces any `date: today` |
| Description | body | Yes | ≥1 paragraph describing the course |
| Learning objectives | body | Yes | Bullet/numbered list of outcomes |
| Session outline | body | Yes | Markdown table (see Session Outline Row) |
| Recommended Literature | body | Yes | Markdown table (see Literature Entry); ≥1 row |

**Validation**:
- A syllabus missing the Recommended Literature table is INCOMPLETE and MUST
  NOT be considered published (SC-002, T-VIII).
- Per-file `format.html.theme` overrides are FORBIDDEN (Principle V).
- The file MUST be the first entry of its `_quarto.yml` sidebar block
  (Principle II, T-VIII).

## Entity: Session Outline Row

One row per course session in the outline table.

| Column | Required | Rules |
|---|---|---|
| `#` | Yes | Sequential session number |
| Session Title | Yes | Markdown link to the session `.qmd` (or `sessions/…`) |
| Topics Covered | Yes | Short comma/▪ list of topics |

**Validation**: The link target MUST resolve to an existing referenced file
(it may live outside the course directory — e.g. `essca-stat` links to top-level
`sessions/session-NN.qmd`). Validation checks link resolution, not folder
locality.

## Entity: Literature Entry (Row)

One row per recommended reading. Two column profiles:

**Book profile** (default):

| Column | Required | Rules |
|---|---|---|
| Author(s) | Yes | "Lastname, F." or "Org." |
| Title | Yes | Full title (italicized) |
| Edition | Yes | Edition number, or `N/A` if none |
| Publisher/Source | Yes | Publisher name or source/URL |

**Paper profile** (FR-009, used by `ai-papers` and AI sections of `ai-dev`):

| Column | Required | Rules |
|---|---|---|
| Author(s) | Yes | Paper authors |
| Title | Yes | Paper title |
| Year | Yes | Publication year |
| Publication Venue | Yes | Conference/journal/preprint server |

**Validation**: A table uses ONE consistent profile per section. Optional extra
column `URL` permitted at the end.

## Entity: Bilingual Counterpart (Stub or Full)

Mirrors a syllabus into the other language for parity (Principle VI, FR-008).

| Field | Required | Rules |
|---|---|---|
| Path | Yes | EN-authored source → `fr/teaching/<course>/index.qmd`. (FR-authored courses are deferred; no `en/` tree created in this feature.) |
| `title` | Yes | Source course title |
| `lang` | Yes | The counterpart's language |
| Notice | Yes (stub) | `.callout-note` "translation in progress / traduction en cours" |
| Backlink | Yes (stub) | Markdown link to the source syllabus |

**State transition**: `Stub → Full Translation`. A stub is a placeholder; once
fully translated it drops the notice and gains the full syllabus structure
(same contract as Course Syllabus). The transition is out of scope for this
feature (Complexity Tracking).

## Relationships

```
Course (dir under teaching/)
  └── 1 Course Syllabus (index.qmd)            [registered first in sidebar]
        ├── 1 Session Outline (table)
        │     └── N Session Outline Rows  ──link──>  Session .qmd files
        ├── 1 Recommended Literature (table)
        │     └── 1..N Literature Entries
        └── 1 Bilingual Counterpart (stub|full)  ──backlink──>  Course Syllabus
```

## Coverage matrix (per course)

| Course | Lang | Counterpart (this feature) | Front-matter work |
|---|---|---|---|
| inseec-finance | fr | **deferred** (no `en/` tree; language-normalization feature) | add full YAML block |
| ece-proba | fr | **deferred** (language-normalization feature) | add `lang`; fix sidebar ref |
| essca-stat | en | `fr/teaching/essca-stat/index.qmd` (stub) | drop `cosmo`; `date-modified`; `lang` |
| mathematical-analysis | fr | **deferred** (language-normalization feature) | add `lang` |
| ai-papers | en | `fr/teaching/ai-papers/index.qmd` (stub) | add `date-modified`,`lang`; clean draft block |
| ai-dev | en | `fr/teaching/ai-dev/index.qmd` (stub) | add `lang` |

**Note**: Only the three EN-authored courses receive a French stub in this
feature. The three FR-authored courses remain at root with no counterpart yet
(Principle VI partial — deferred). No `en/` tree is created.
