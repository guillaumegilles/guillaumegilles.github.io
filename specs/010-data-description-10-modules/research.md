# Phase 0 Research: Data Description — 10-Module Redesign

All spec `Assumptions` that deferred a decision to planning are resolved
here. Findings that contradict the brainstorm are marked **⚠ Correction**.

## 1. OpenStax IBS 2e mapping (verified against the PDF)

**Method**: `pdftotext -layout` over the supplied 627-page PDF; table of
contents and body headings inspected directly.

**Decision**: Use the real section list below. The brainstorm's mapping is
replaced.

Actual Chapter 2 and 13 structure:

| § | Title |
|---|---|
| 2.1 | Display Data (stem-and-leaf, bar graphs, pie charts, histograms, frequency polygons, time series) |
| 2.2 | Measures of the Location of the Data (quartiles, percentiles, IQR) |
| 2.3 | Measures of the Center of the Data (mean, median, mode, grouped mean) |
| 2.4 | Sigma Notation and Calculating the Arithmetic Mean |
| 2.5 | Geometric Mean |
| 2.6 | Skewness and the Mean, Median, and Mode |
| 2.7 | Measures of the Spread of the Data (s, grouped s, Chebyshev, Empirical Rule, CV) |
| 13.1 | The Correlation Coefficient r |
| 13.3 | Linear Equations |
| 13.4 | The Regression Equation |
| 13.6 | Predicting with a Regression Equation |
| 13.7 | How to Use Microsoft Excel for Regression Analysis |

**⚠ Correction — brainstorm errors found**:

- "§2.4 Box Plots" and "§2.5 Scatter Plots" do not exist (2.4 is sigma
  notation, 2.5 is the geometric mean).
- "§2.7 Measures of Spread" is correct; "§2.6 Skewness" is correct.
- "§1.3 Levels of Measurement" is correct; "§1.2" is sampling, not
  "Data and Sampling" as a data-types lesson.
- **OpenStax IBS 2e has no box-plot section, no weighted-mean section and
  no stand-alone scatter-plot section.** Scatter diagrams only appear
  inside Ch. 13 (§13.1, §13.3–13.4). Contingency tables appear only in
  §3.4 with a probability framing.

**Rationale**: Wrong section numbers would send students to the wrong
page. The gaps mean three modules need non-OpenStax anchors.

**Alternatives considered**: Switching textbook (rejected — the owner
supplied this PDF and it is free/open-licensed).

**Gap handling**:

| Gap | Resolution |
|---|---|
| Boxplot (M5) | Authored in-course; Khan Academy as external anchor; OpenStax §2.2 for quartile mechanics |
| Weighted mean (M4) | Authored in-course; OpenStax §2.3 grouped mean is the nearest reference (a grouped mean is a weighted mean) |
| Contingency tables (M8) | Authored in-course; §3.4 cited as "optional, probability framing — skim" |
| Scatter plot (M8) | §13.1 and §13.3 figures; authored in-course |

## 2. Khan Academy references

**Method**: `fetch` returned no content (client-rendered site). A web
search confirmed the current course units and one live URL
(`…/statistics-probability/analyzing-categorical-data/two-way-tables-for-categorical-data`).

**Decision**: Link at **unit level only**, using the unit names confirmed
to exist: *Analyzing categorical data*, *Displaying and comparing
quantitative data*, *Summarizing quantitative data*, *Modeling data
distributions*, *Exploring bivariate numerical data*, *Study design*.
Name individual lessons in plain text (title + approximate duration) but
do **not** deep-link until the owner has opened each link in a browser.

**⚠ Correction**: Most brainstorm URLs use older unit slugs
(`displaying-describing-data`, `describing-relationships-in-quantitative-data`,
`summarizing-quantitative-data/...`) and cannot be verified from this
environment. Treat them as unverified. The brainstorm's lesson durations
were never measured.

**Rationale**: FR-043 forbids unverified links. Unit-level links are the
most stable; lesson titles still help students find content by search.

**Alternatives considered**: Embedding videos (rejected — third-party
iframes risk tracking, violating Constitution IV); scraping with a
headless browser (rejected — disproportionate for a reading list).

**Follow-up for the owner** (cannot be automated here): open each unit
link once before publication; tracked as a task in the final phase.

## 3. Statistical conventions

**Decision**: Inherit feature 005's conventions, now confirmed against
OpenStax:

| Topic | Convention | Excel |
|---|---|---|
| Quartiles / percentiles | Position `i = (k/100)(n+1)`, interpolate | `QUARTILE.EXC`, `PERCENTILE.EXC` |
| Spread | Sample ($n-1$) by default; population variant explained | `VAR.S`, `STDEV.S` (`.P` variants shown) |
| Skewness | Excel's adjusted Fisher–Pearson as the main coefficient, plus hand-computable **Pearson median skewness** $3(\bar{x}-\text{Me})/s$ | `SKEW` |
| Kurtosis | Conceptual only (names, pictures) | none |
| Mode (continuous) | Modal class from grouped table | `MODE.SNGL` for discrete |
| Outliers | $1.5\times$IQR fences | — |

**Rationale**: OpenStax §2.2 gives exactly the $(n+1)$ position formula,
which equals Excel's exclusive method — so book, course and spreadsheet
agree. Using `QUARTILE.INC` would silently disagree with the textbook.
The existing glossary and 30-day worked numbers already assume these.

**Note**: OpenStax gives a third-moment skewness formula; the course shows
it conceptually and uses `SKEW` for computation, with Pearson's median
coefficient as the by-hand tool.

**Alternatives considered**: `QUARTILE.INC` (rejected — disagrees with
OpenStax and with existing verified numbers).

## 4. Running dataset

**Decision**: One long-format table, two franchises, **120 days each**
(2026-04-06 to 2026-08-03), 240 rows, 16 columns (see `data-model.md`).

- **Franchise A, "Harbour"** is the original Wandering Fork: rows 1–30
  reproduce `specs/005-data-description-course/wandering-fork-dataset.csv`
  **verbatim** (the 8 original columns), so every existing verified figure
  (mean 628.34, $s$ 137.09, $Q_1$ 506.60 …) stays valid.
- **Franchise B, "Campus"**: a university-area truck with a different
  profile — lower base revenue, strong weekday pattern, and **event days
  that create a right-skewed revenue distribution** (serves FR-025,
  Module 7).
- Qualitative variables of every kind (nominal, binary, ordinal) and
  quantitative of both kinds (discrete, continuous) are present.
- A **30-day hand-computation subset** per franchise is published as its
  own sheet (Harbour's equals the legacy CSV).
- Designed correlations: revenue ↔ customers strong linear; revenue ↔
  temperature weak; weather × promo shows visible dependence — verified
  by the generator, never hard-coded.

**Rationale**: Keeping the first 30 Harbour rows verbatim preserves all
migrated worked examples (T-I, FR-026). 120 days allows meaningful
histograms and regression without making hand work impractical, because
the 30-day subsets cover that. 240 rows fits easily in Excel.

**Alternatives considered**: Two separate files (rejected — students need
one `franchise` column for PivotTables and `COUNTIFS`); 365 days
(rejected — gains nothing for descriptive statistics, hurts readability);
re-generating Harbour from scratch (rejected — breaks existing figures).

**Secondary datasets**:

- `payroll-skew.csv` — 10–20 rows, CEO plus staff, for M4/M7 outlier and
  skew examples (FR-029).
- `lakeside-bakery.csv` — a fresh, 60-day, 2-outlet dataset for the M10
  walkthrough so students cannot rely on memorised Wandering Fork numbers
  (FR-023).

**Generation and verification**: A seeded Python script (`.venv`; numpy,
pandas already installed) writes the CSVs and `.xlsx`, then asserts the
designed properties and recomputes every statistic quoted in
`data-model.md`. The script is kept with the spec, not run in the site
build (no `_freeze/` impact).

## 5. Time budget per module (180 min)

**Decision**: See the table in `data-model.md` (§Module catalogue).
Totals: theory 630 min, Excel lab 520 min, exercises 650 min = 1,800 min.
Module 10 reserves 120 min for exercises = 90-min mock exam + 30-min
debrief (FR-004).

**⚠ Correction**: The brainstorm's table summed to 120 min per module.
All figures were redistributed to 180.

**Rationale**: Heavier theory in M1, M3, M4, M6, M9 (new vocabulary or
dense formulas); heavier lab in M2, M3, M5, M8 (new Excel tooling);
exercises weigh most in M7 (univariate synthesis) and M10.

## 6. Exam coverage

**Decision**: Midterm (45 min, 35%) covers M1–M5. Final (90 min, 65%)
covers M1–M10 with the larger share on M6–M10.

**Rationale**: M5 closes the "organise → locate → centre" block, a
natural midpoint; M6–M10 are newer and weigh more in the final. Easy to
change in the syllabus later.

## 7. Where files live

**Decision**: Keep the owner's in-progress layout:

```text
teaching/data-description/
├── index.qmd                       # syllabus (rewritten last)
├── data/                           # datasets (csv + xlsx + dictionary)
└── modules/
    ├── module-01.qmd … module-10.qmd
    ├── dataset.qmd                 # data dictionary + downloads
    ├── glossary.qmd                # already moved here by owner
    └── excel-functions.qmd         # converted from the .txt list
```

- `glossary.qmd` stays in `modules/` (the owner moved it there;
  Constitution T-V only requires a central glossary linked from the
  sidebar).
- The EN/FR function list becomes a `.qmd` page so it is linkable from
  every Excel section and reachable in two clicks (SC-010). The `.txt`
  is deleted after conversion.
- `excel-worksheet.qmd` and `excel-worksheet-2.qmd` (old Sessions 1–2)
  and the 9 `session-*.qmd` files are **migration sources**: their
  content is moved into modules per the fidelity record, then the files
  are deleted (FR-040).

**Rationale**: The state on disk shows the owner is already moving
everything under `modules/`; the plan follows that rather than reverting.

## 8. Draft and publish strategy

**Decision**: Use Quarto's native `draft: true` (confirmed in the Quarto
docs; installed Quarto is 1.4.537, which supports it). Default
`draft-mode: gone` renders drafts as blank pages and removes them from
navigation, search and sitemap. Put `draft: true` in
`modules/_metadata.yml` so all ten modules, the glossary and the function
page are drafts together; remove that single line to publish.

**Important**: `index.qmd` is **not** currently a draft and is live (its
session links are already dead, because the sessions moved to `modules/`).
Setting it to draft would blank a public page. Instead the **syllabus
rewrite is the final step** (FR-037), done in the same change that
removes the draft flag.

**Rationale**: One-line publish; no per-file bookkeeping; matches the
Quarto-native mechanism.

**Alternatives considered**: Per-file flags (rejected — easy to miss one);
a Git branch only (rejected — doesn't cover the live `index.qmd`
inconsistency by itself).

## 9. Interactive demonstrations

**Decision**: Reuse the four existing Shinylive demos (all dark-themed,
client-side, dataset embedded):

| Existing | New home | Required? |
|---|---|---|
| `session-04.qmd` histogram bin width | M3 | **Yes** (FR-030) |
| `session-05.qmd` boxplot builder | M5 | **Yes** |
| `session-07.qmd` dispersion | M6 | Optional (keep) |
| `session-11.qmd` scatter + regression line | M9 | **Yes** |

Re-point each demo at the new 120-day dataset only where needed; keep the
30-day Harbour data where the module's hand-computation uses it. M1, M2,
M4, M7, M8, M10 carry a `TODO:` `.callout-important` where a demo would
help but is not required (FR-031).

**Rationale**: Three required demos already exist; the plan is migration,
not new build, matching decision 6 (only the hardest visualisations).

**Alternatives considered**: Observable JS (rejected for these — each
needs matplotlib-style charts and the existing code is already Shinylive;
the site uses OJS only for pure-arithmetic demos).

## 10. Status of the current repository

Verified on 2026-10-06:

- `_quarto.yml` sidebar still lists `teaching/data-description/session-01…12.qmd`
  and `glossary.qmd` at the course root; **none of those paths exist**
  any more — the sidebar and the live `index.qmd` table are already
  broken. First delivery step restores a green render.
- `modules/module-01.qmd` holds old Session 3 content (title still
  "Session 3 — …"). It is a migration source for **M2**, not M1, so it
  is renamed to `module-02.qmd`; M1 is new content.
- `modules/` also still holds `session-04…12.qmd`, `excel-worksheet*.qmd`,
  `glossary.qmd` and `Excel_functions_English_French.txt`.

## 11. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Khan Academy lesson links rot | Students hit dead links | Unit-level links only; owner verification step |
| Dataset change breaks migrated worked examples | Wrong numbers published | Keep Harbour rows 1–30 verbatim; generator re-computes every quoted statistic |
| M9 overload (cov + r + regression + $R^2$ + output table in 3 h) | Students rushed | Budget 70/55/55; move regression-output reading to the exercises block; cut to optional if a pilot overruns |
| Excel locale (French) | Function names fail | Function page links; locale note in M1 |
| Double conventions ($n$ vs $n-1$, INC vs EXC) | Inconsistent answers | Convention table in the syllabus and glossary; one rule per quantity |
| Syllabus is live but broken | Public dead links meanwhile | Fix sidebar early; accept dead links only until final publish step |
