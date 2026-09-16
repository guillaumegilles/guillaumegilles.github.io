# Phase 0 Research: Data Description Course (MS03-001-G)

## 1. Source archive extraction approach

**Decision**: Use `.venv`-only Python (`python-pptx` for slide decks,
`python-docx` for handouts/practical-work documents, `openpyxl`/`pandas`
— already installed — for `.xlsx` correction workbooks) to run a one-time,
ad hoc extraction pass per legacy session folder, dumping slide titles,
bullet text, and any numeric answer keys to plain text/CSV for the
session author to read alongside the syllabus. These scripts are **not**
committed as part of the Quarto build (no `.venv` is committed per
constitution) and produce no `_freeze/` entries.

**Rationale**: The standard project tooling (`read_file`, etc.) cannot
parse binary Office formats. `python-pptx`/`python-docx` are the
de facto standard libraries for this, are pure-Python (safe to `pip
install` into the existing `.venv`), and integrate with the `pandas`
stack already present for the "Wandering Fork" dataset work below.

**Alternatives considered**:
- *Manually opening each file in a GUI office suite*: works but is slow,
  non-reproducible, and not scriptable across ~150 archive files.
- *LibreOffice headless conversion to text/PDF*: viable fallback if
  `python-pptx`/`python-docx` hit a malformed file, but adds a system
  dependency; kept as a documented fallback, not the primary path.

## 2. Source → session mapping

**Decision**: Map the 12 target `session-NN.qmd` files to the legacy
Moodle "Session N" folders 1:1 by number (Session 1 → `session-01.qmd`,
…, Session 12 → `session-12.qmd`), using the block-structured, bilingual
archive (`Course_MS03-001-G_Data_descri..._.2013698`) as the primary
source for each session's slide deck and practical-work files (per the
spec's Assumptions ordering: newest archive first, then EN 2024/25, then
FR 2024/25).

| Session | Part | Topic (from syllabus + slide filenames) |
|---|---|---|
| 1–2 | I. Excel Fundamentals | Spreadsheet handling, cell referencing, basic functions, sorting/processing |
| 3–4 | II. Univariate | Graphical representation: frequency tables, bar/pie charts, histograms |
| 5 | II. Univariate | Position indicators: quantiles, quartiles, percentiles, boxplot |
| 6–8 | II. Univariate | Central tendency, dispersion, and asymmetry indicators |
| 9 | II. Univariate | Practical-work synthesis (Excel) |
| 10 | III. Bivariate | Bivariate graphical representation: contingency table, scatter plot |
| 11 | III. Bivariate | Bivariate numerical summaries: covariance, correlation, regression line |
| 12 | III. Bivariate | Practical-work synthesis + original mock exam (FR-018) |

**Rationale**: This mapping was already validated against the actual
folder listings during specification (each `Folder_EN_Block_*`/legacy
`Session_N` folder was inspected) and matches the syllabus's stated hour
allocation (6h + 18h + 6h = 30h) closely enough that no session needs
splitting or merging.

**Alternatives considered**: Consolidating to 3 files (one per block)
was already rejected in the spec's Clarifications in favor of the
12-session granularity, to match the `teaching/decision-making-stat/`
convention.

## 3. The "Wandering Fork" canonical dataset

**Decision**: A single, originally-authored 30-day dataset (one
spring/early-summer month of trading) is generated once, verified with
`pandas`/`numpy`, and committed as
`specs/005-data-description-course/wandering-fork-dataset.csv`. Every
session that uses "The Wandering Fork" (Sessions 3–12) MUST read numbers
from this file rather than inventing new ones. Fields: `day`, `date`,
`day_of_week`, `weather` (qualitative: Sunny/Cloudy/Rainy), `temperature_c`
(quantitative driver), `customer_count`, `items_sold`, `daily_revenue_eur`
(primary quantitative variable for univariate work).

**Rationale**: FR-006 requires the case study's values to be "kept
internally consistent across sessions" — a single canonical file is the
only way to guarantee 12 independently-authored files never disagree on
a number. Generating it with `numpy`/`pandas` (fixed random seed = 42)
rather than hand-inventing it avoids arithmetic mistakes and guarantees
every downstream statistic (mean, quartiles, variance, skewness,
correlation) is internally correct and reproducible. See
`data-model.md` for the full verified statistics.

**Alternatives considered**:
- *Reusing the source's actual "Food Truck" figures*: rejected per the
  spec's Clarifications (Option B — no proprietary figures reproduced).
- *Letting each session author invent its own small example*: rejected —
  risks contradicting numbers across sessions (explicitly called out as
  an edge case in the spec) and loses the "running case study" narrative
  value (User Story 2).
- *A much larger dataset (e.g., a full year)*: rejected as unnecessary
  complexity; 30 days is enough to support every required statistic
  (frequency tables, quartiles, boxplot, variance, skewness, covariance,
  correlation, regression) while staying easy for a learner to scan in a
  table.

## 4. Statistical convention choices (Excel-aligned)

**Decision**: Quartiles use the **exclusive** method (Excel
`QUARTILE.EXC` / `(n+1)`-position method); standard deviation and
variance use the **sample** (n−1) formulas (Excel `STDEV.S`/`VAR.S`);
skewness uses the Fisher-Pearson adjusted (sample) formula (Excel
`SKEW`); mode for the continuous `daily_revenue_eur` variable is computed
as a **modal class** from a grouped frequency table (class width 100,
starting at 400), using the standard grouped-mode interpolation formula
$Mo = L + h \cdot \frac{f_1 - f_0}{(f_1-f_0)+(f_1-f_2)}$.

**Rationale**: These are exactly the conventions the source materials
use (a business-school "descriptive statistics" course taught via
Excel) and match FR-007's requirement to name exact English-locale Excel
functions. Locking this down now prevents inconsistency between, e.g.,
Session 5 (quartiles) and Session 12 (mock exam) picking different
quartile conventions.

**Alternatives considered**: `QUARTILE.INC`/population (n) formulas are
also valid statistically but are not what the source syllabus's Excel
walkthroughs use; switching would silently break fidelity to the
source's pedagogical approach (T-I).

## 5. Shinylive demo scope (FR-008)

**Decision**: Each of the 4 required demos is a small, self-contained
`{shinylive-python}` app using `matplotlib` + `numpy`/`pandas` (already
proven to work in `teaching/mathematical-fundamentals/`), pre-seeded with
"The Wandering Fork" data but allowing the learner to edit values:
(a) histogram/frequency-distribution builder (editable bin width),
(b) boxplot from quartiles (editable sample), (c) central
tendency/dispersion calculator (editable sample → mean/median/mode,
variance/std dev live-updating), (d) scatter plot + correlation
coefficient (editable points, live $r$).

**Rationale**: Matches the existing site's only working interactive
pattern; keeps the demos genuinely useful for building intuition (T-VII)
rather than decorative.

**Alternatives considered**: A single combined "dashboard" app covering
all 4 concepts was rejected — harder to place inline at the exact point
each concept is introduced (T-II pedagogical ordering), and a single
large app is more likely to hit Shinylive's WASM payload/perf limits.

## 6. Draft/publish mechanics (FR-017)

**Decision**: `draft: true` in each of the 15 files' YAML front matter
(same key already used by `teaching/decision-making-stat/index.qmd`).
The `_quarto.yml` sidebar block is added immediately (Principle II),
listing all 15 pages regardless of draft status — Quarto renders draft
pages with a "this page is a draft" banner and excludes them from search
indexing, but the nav entries still resolve, so no broken links occur
mid-construction. A single follow-up change removes `draft: true` from
all 15 files together once SC-001 is met.

**Rationale**: Matches existing site precedent exactly; avoids inventing
a new publishing convention.

**Alternatives considered**: Hiding the sidebar block entirely until
complete was rejected — it would leave the feature's own tasks
unverifiable via the rendered site until the very end, and contradicts
Principle II ("every new teaching page is listed").

## 7. Non-lesson archive handling

**Decision**: Forum pages, `index.html`/`about.html` Moodle shells,
`overviewfiles`/`shared` folders, and the `URL_Syllabus` link objects in
`ressources/` are treated purely as folder-structure noise from the
Moodle export and are never read for lesson content or referenced from
`.qmd` files.

**Rationale**: Already established in the spec's Edge Cases; restated
here so the extraction scripts (§1) can skip them by pattern
(`Forum_*`, `*.html`, `URL_*`, `shared/`, `overviewfiles/`).

## Outcome

All Technical Context items are resolved; no `NEEDS CLARIFICATION`
markers remain. Ready for Phase 1 design.
