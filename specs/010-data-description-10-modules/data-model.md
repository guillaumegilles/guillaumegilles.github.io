# Phase 1 Data Model: Data Description — 10-Module Redesign

## 1. Module catalogue

Time in minutes (theory / Excel lab / exercises); each row sums to 180.

| M | Title | Theory | Excel | Exercises | Sum | Required demo | Collapsible derivation (FR-008) |
|---|---|---:|---:|---:|---:|---|---|
| 1 | What is statistics? Data types and measurement | 75 | 45 | 60 | 180 | — (TODO) | Relative frequencies sum to 1 |
| 2 | Organising qualitative data | 60 | 60 | 60 | 180 | — (TODO) | A frequency table's percentages sum to 100% (and the rounding caveat) |
| 3 | Organising quantitative data | 70 | 60 | 50 | 180 | **Histogram bin width** | Cumulative frequency reaches 100% |
| 4 | Central tendency | 70 | 50 | 60 | 180 | — (TODO) | Deviations from the mean sum to zero |
| 5 | Position and boxplot | 60 | 60 | 60 | 180 | **Boxplot builder** | Where the $(n+1)$ position formula comes from |
| 6 | Dispersion | 75 | 50 | 55 | 180 | Dispersion (kept) | Variance shortcut $\overline{x^2}-\bar{x}^2$ |
| 7 | Shape and univariate review | 60 | 50 | 70 | 180 | — (TODO) | Pearson's coefficient is unit-free |
| 8 | Bivariate I | 60 | 60 | 60 | 180 | — (TODO) | Marginals are sums of joints; conditional rows sum to 1 |
| 9 | Bivariate II | 70 | 55 | 55 | 180 | **Scatter + regression line** | Least-squares slope and intercept; $R^2=r^2$ |
| 10 | Synthesis and mock exam | 30 | 30 | 120 | 180 | — | Overall mean as weighted mean of franchise means |
| | **Total** | **630** | **520** | **650** | **1,800** | | |

Module 10 exercises = 90-min mock exam + 30-min debrief (FR-004).

### Per-module content map

| M | Excel functions / tools introduced | OpenStax IBS 2e (verified) | Khan Academy unit (unit-level link) |
|---|---|---|---|
| 1 | `COUNT`, `COUNTA`, `SUM`, cell references, sort/filter, data-type colour coding | §1.1, §1.2, §1.3 | Study design |
| 2 | `COUNTIF`, `COUNTIFS`, PivotTable (counts), bar and pie charts, conditional formatting | §2.1 (bar graphs, pie charts) | Displaying and comparing quantitative data / Analyzing categorical data |
| 3 | `COUNTIFS` ranges, histogram chart, PivotTable grouping, cumulative columns | §2.1 (histograms, polygons, time series) | Displaying and comparing quantitative data |
| 4 | `AVERAGE`, `MEDIAN`, `MODE.SNGL`, `SUMPRODUCT` (weighted and grouped mean) | §2.3, §2.4; §2.5 geometric mean (enrichment) | Summarizing quantitative data |
| 5 | `QUARTILE.EXC`, `PERCENTILE.EXC`, `MIN`, `MAX`, box-and-whisker chart | §2.2 (quartiles, percentiles); boxplot authored | Summarizing quantitative data |
| 6 | `VAR.S`, `STDEV.S`, `VAR.P`, `STDEV.P`, `SUMSQ`, CV formula | §2.7 | Summarizing quantitative data |
| 7 | `SKEW`, histogram overlay | §2.6 | Modeling data distributions |
| 8 | 2-D `COUNTIFS`, PivotTable (two fields), XY scatter, trendline | §13.1, §13.3 figures; §3.4 optional | Analyzing categorical data; Exploring bivariate numerical data |
| 9 | `COVARIANCE.P`, `COVARIANCE.S`, `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`, Analysis ToolPak regression | §13.1, §13.3, §13.4, §13.6, §13.7 (skip §13.2 and inference) | Exploring bivariate numerical data |
| 10 | All previous | Chapter Reviews 2 and 13 | Units above (practice) |

## 2. Entities

### Module
| Field | Rule |
|---|---|
| `number` | 1–10, unique, two-digit file name |
| `title` | From catalogue |
| `business_question` | One sentence, present at top |
| `objectives` | ≥ 3, each measurable ("compute…", "interpret…") |
| `time_budget` | theory + Excel + exercises = 180 |
| `sections` | Fixed order — see `contracts/module-page-contract.md` |
| `derivation` | ≥ 1 collapsible |
| `demo` | Required for M3, M5, M9; otherwise demo or `TODO` |
| `further_reading` | ≥ 1 OpenStax and ≥ 1 Khan Academy entry |
| `draft` | `true` until course publish |

### Dataset: `wandering-fork` (long format, 240 rows)

One row = one franchise on one trading day.

| Column | Type (statistical) | Values / unit | Notes |
|---|---|---|---|
| `franchise` | Qualitative nominal | `Harbour`, `Campus` | |
| `day` | Quantitative discrete | 1–120 | Per franchise |
| `date` | Date | 2026-04-06 … 2026-08-03 | |
| `day_of_week` | Qualitative nominal | Monday … Sunday | Original column |
| `month` | Qualitative ordinal | Apr … Aug | Ordered by calendar |
| `weather` | Qualitative nominal | Sunny / Cloudy / Rainy | Original column |
| `temperature_c` | Quantitative continuous | °C | Original column |
| `event_nearby` | Qualitative nominal (binary) | Yes / No | Campus: drives skew |
| `promo_active` | Qualitative nominal (binary) | Yes / No | |
| `staff_on_duty` | Quantitative discrete | 2–5 | |
| `foot_traffic` | Quantitative discrete | passers-by | Explains customers |
| `customer_count` | Quantitative discrete | customers | Original column |
| `items_sold` | Quantitative discrete | items | Original column |
| `daily_revenue_eur` | Quantitative continuous | € | Original column |
| `waste_kg` | Quantitative continuous | kg | Right-skewed |
| `satisfaction_rating` | Qualitative ordinal | 1–5 | Typical rating of the day |

Original eight columns (`day`, `date`, `day_of_week`, `weather`,
`temperature_c`, `customer_count`, `items_sold`, `daily_revenue_eur`)
keep their names and units so migrated examples still read naturally.

**Invariants** (checked by the generator):

1. Harbour days 1–30 equal the legacy CSV exactly on the original columns.
2. No missing values; no duplicate `(franchise, day)`.
3. `items_sold ≥ customer_count`; `customer_count ≤ foot_traffic`;
   revenue > 0.
4. Campus revenue skewness > +0.5; Harbour revenue skewness within ±0.5.
5. $r$(customers, revenue) ≥ 0.80 in both franchises; $|r|$(temperature,
   revenue) ≤ 0.35.
6. Weather × promo conditional profiles differ visibly (largest
   row-profile gap ≥ 15 percentage points) in at least one franchise.
7. At least one outlier by the $1.5\times$IQR rule per franchise.
8. Every category appears at least 5 times per franchise (no empty cells in
   contingency tables). Exception: `month` = Aug has only 3 rows because the
   120-day window ends on 3 August; `month` is not used in contingency
   exercises.

Note: the legacy Harbour 30-day Q1 is 506.605, shown as 506.61 by Excel;
feature 005 printed 506.60. Modules use 506.61.

### Dataset files

| File | Purpose | Rows |
|---|---|---:|
| `data/wandering-fork.csv` | Main table | 240 |
| `data/wandering-fork.xlsx` | Same data as an Excel Table; extra sheets `harbour_30d`, `campus_30d`, `dictionary` | 240 / 30 / 30 |
| `data/payroll-skew.csv` | Small skewed example (M4, M7) | 10–20 |
| `data/lakeside-bakery.csv` | Fresh data for the M10 walkthrough | 120 (60 × 2 outlets) |
| `modules/dataset.qmd` | Dataset page: download links, data dictionary (name, type, unit, meaning per column), designed properties | 16 columns |

### Exercise
| Field | Rule |
|---|---|
| `module` | 1–10 |
| `track` | `by-hand` or `excel` |
| `objective` | Which learning objective it tests |
| `solution` | Collapsible, with worked steps |

Each module needs ≥ 1 of each track for its core skill (FR-011).

### FurtherReadingEntry
| Field | Rule |
|---|---|
| `source` | `OpenStax` or `Khan Academy` |
| `locator` | OpenStax: section number + title; Khan: unit URL |
| `note` | One line on what it adds |
| `duration` | Approximate minutes (Khan) / pages (OpenStax) |
| `verified_on` | Date checked (FR-043) |

### GlossaryEntry
Notation · name · plain definition · Greek pronunciation (if Greek) · first
module. Existing glossary column "Introduced in" is changed from
"Session N" to "Module N".

### FidelityRecord
One row per canonical item in the 12 old session pages:

| Field | Values |
|---|---|
| `old_location` | e.g. `session-05.qmd › Worked example` |
| `type` | theory / worked example / exercise / demo / derivation |
| `new_location` | e.g. `module-05.qmd › Worked example` |
| `status` | `migrated` · `adapted` · `dropped` |
| `reason` | Required when `adapted` or `dropped` |

## 3. Migration map (old → new file)

| Old file | New destination | Notes |
|---|---|---|
| `modules/excel-worksheet.qmd` (old S1) | M1 Excel section; M2 (`COUNTIF`) | Cell references, `SUM`, `IF`, `LARGE` split by need |
| `modules/excel-worksheet-2.qmd` (old S2) | M2 (PivotTable counts, conditional formatting); M3 (grouping); M8 (two-field PivotTable) | |
| `modules/module-01.qmd` (old S3, mis-named) | **M2** | Rename to `module-02.qmd`; M1 is new |
| `modules/session-04.qmd` | M3 | Keep histogram demo |
| `modules/session-05.qmd` | M5 | Keep boxplot demo |
| `modules/session-06.qmd` | M4 | Add weighted mean |
| `modules/session-07.qmd` | M6 | Keep dispersion demo |
| `modules/session-08.qmd` | M7 | Add kurtosis (conceptual) |
| `modules/session-09.qmd` | End of M7 | Univariate synthesis, shortened |
| `modules/session-10.qmd` | M8 | |
| `modules/session-11.qmd` | M9 | Keep scatter/regression demo |
| `modules/session-12.qmd` | M10 | Mock exam rebuilt on new data |

After migration the old files and `Excel_functions_English_French.txt`
are removed; `module-01.qmd` is newly authored.

## 4. Verified numbers that must not change

From feature 005 (`daily_revenue_eur`, Harbour days 1–30, $n=30$):
mean 628.34 · median 643.63 · min/max 407.59 / 886.56 · $s$ 137.09 ·
CV 21.82% · $Q_1$ 506.60 · $Q_3$ 729.99 · IQR 223.39. New 120-day
figures are generated and recorded alongside in the quickstart check
output, never typed by hand.

## 5. Validation rules (summary)

- Time budget per module sums to 180; module total 1,800.
- Every quoted statistic recomputes from the CSV.
- Every module passes the contract checklist in
  `contracts/module-page-contract.md`.
- Sidebar contains only: syllabus, M1–M10, dataset page, glossary,
  function page.
