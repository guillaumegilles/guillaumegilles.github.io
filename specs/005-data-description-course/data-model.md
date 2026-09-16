# Phase 1 Data Model: Data Description Course (MS03-001-G)

This document defines the content entities (per the spec's Key Entities
section) with concrete fields, plus the fully verified "Wandering Fork"
dataset and its statistics — the single source of truth every session
MUST reuse (FR-006).

## Content Entities

### Course

| Field | Value |
|---|---|
| Title | Data Description |
| Code | MS03-001-G |
| File | `teaching/data-description/index.qmd` |
| Prerequisites | Mathematical Fundamentals (MS01), Mathematical Analysis (MS02) |
| Successor | Decision Making Statistics (MS04, `teaching/decision-making-stat/`) |
| Total hours | 30h (seminar) |
| ECTS | 4 |
| Personal work | 20h |
| Assessment | Midterm Exam 35% (45 min) + Final Exam 65% (90 min), individual written, MCQ component |
| Draft status | `draft: true` until all 15 files pass SC-001, then removed together (FR-017) |

### Part (grouping only — not a file)

| Part | Sessions | Hours |
|---|---|---|
| I. Excel Fundamentals | 1–2 | 6h |
| II. Univariate Data Treatment | 3–9 | 18h |
| III. Bivariate Data Treatment | 10–12 | 6h |

### Session

Attributes per session file: `title`, `part`, `session_number`,
`learning_objectives` (list), `theory` (definitions/formulas),
`worked_example` (uses "The Wandering Fork" data from Session 3 onward),
`using_excel` (function-reference table, FR-007), `exercises` (with
collapsible solutions), `proof` (one collapsible derivation, FR-011),
`interactive_demo` (present only for the 4 FR-008 sessions; otherwise a
`.callout-important TODO:` if the session covers a priority concept
without a demo). See `contracts/session-page.md` for the exact required
structure.

### Case Study: "The Wandering Fork"

Fictional food-truck business; originally-authored 30-day dataset (see
below). Used as the running example from Session 3 onward. Sessions 1–2
use a simpler warm-up dataset (e.g., a small product-price list for
basic Excel functions) since the case study is introduced starting
Session 3, per FR-006.

### Exercise

Attributes: `prompt`, `context` ("The Wandering Fork" or warm-up),
`solution` (revealable, `.callout-caution collapse="true"`).

### Glossary Term

Attributes: `notation`, `plain_definition`, `pronunciation` (Greek
letters only), `introduced_in` (session reference).

### Source Material

Reference-only input under `ressources/`; never published directly. See
`research.md` §1 for the extraction approach and §2 for the
source→session mapping.

## The "Wandering Fork" Dataset (canonical, verified)

**File**: `specs/005-data-description-course/wandering-fork-dataset.csv`
(30 rows, generated with `numpy` seed 42, statistics verified with
`pandas`/`scipy` — see `research.md` §3).

**Schema**:

| Column | Type | Description |
|---|---|---|
| `day` | integer 1–30 | Day index |
| `date` | date | 2026-04-06 … 2026-05-05 |
| `day_of_week` | categorical | Monday … Sunday |
| `weather` | categorical | Sunny / Cloudy / Rainy (qualitative variable) |
| `temperature_c` | quantitative (continuous) | Daily temperature, °C (bivariate driver) |
| `customer_count` | quantitative (discrete) | Number of customers served |
| `items_sold` | quantitative (discrete) | Number of menu items sold |
| `daily_revenue_eur` | quantitative (continuous) | Daily revenue, € — **primary univariate variable** |

### Verified univariate statistics — `daily_revenue_eur` (n = 30)

| Statistic | Value | Excel function |
|---|---|---|
| Mean $\bar{x}$ | 628.34 | `AVERAGE` |
| Median $Me$ | 643.63 | `MEDIAN` |
| Min / Max | 407.59 / 886.56 | `MIN` / `MAX` |
| Range | 478.97 | `MAX-MIN` |
| Sample variance $s^2$ | 18,793.33 | `VAR.S` |
| Sample std. dev. $s$ | 137.09 | `STDEV.S` |
| Coefficient of variation $CV$ | 21.82% | `STDEV.S/AVERAGE` |
| $Q_1$ (exclusive) | 506.60 | `QUARTILE.EXC(...,1)` |
| $Q_2$ / Median (exclusive) | 643.63 | `QUARTILE.EXC(...,2)` |
| $Q_3$ (exclusive) | 729.99 | `QUARTILE.EXC(...,3)` |
| $IQR$ | 223.39 | `Q3-Q1` |
| Boxplot lower fence | 171.52 | `Q1-1.5*IQR` |
| Boxplot upper fence | 1065.07 | `Q3+1.5*IQR` |
| Skewness (Fisher-Pearson, sample) | +0.034 (≈ symmetric, very mild right skew) | `SKEW` |

No value falls outside the boxplot fences — the dataset has **no
outliers**, which is itself a useful teaching point for Session 5.

### Frequency table for `daily_revenue_eur` (class width 100, for Sessions 3–4 and grouped mode)

| Class (€) | Frequency | Cumulative frequency | % |
|---|---|---|---|
| [400, 500[ | 6 | 6 | 20.0% |
| [500, 600[ | 6 | 12 | 20.0% |
| [600, 700[ | 8 | 20 | 26.7% |
| [700, 800[ | 7 | 27 | 23.3% |
| [800, 900[ | 3 | 30 | 10.0% |

Modal class: [600, 700[; grouped-mode estimate $Mo \approx 666.67$
(formula in `research.md` §4).

### Frequency table for `weather` (qualitative, for Session 3)

| Category | Count | % |
|---|---|---|
| Sunny | 13 | 43.3% |
| Cloudy | 12 | 40.0% |
| Rainy | 5 | 16.7% |

### Verified bivariate statistics — `temperature_c` vs. `daily_revenue_eur` (n = 30)

| Statistic | Value | Excel function |
|---|---|---|
| Sample covariance | 252.81 | (no direct one-cell Excel fn; `COVARIANCE.S` gives the same value) |
| Correlation coefficient $r$ | 0.621 | `CORREL` |
| Coefficient of determination $r^2$ | 0.386 | `r^2` |
| Regression line (least squares) | $\widehat{\text{revenue}} = -22.01 + 28.71 \times \text{temperature\_c}$ | `SLOPE`/`INTERCEPT` |

$r = 0.621$ is a moderate positive correlation — good for teaching
"moderate, not perfect" correlation without an artificially clean
$r \approx 1$ example.

### Secondary variable — `items_sold` (n = 30, for cross-checks/exercise variety)

| Statistic | Value |
|---|---|
| Mean | 74.40 |
| Median | 76.50 |
| Sample std. dev. | 16.22 |

## Warm-up dataset (Sessions 1–2)

An originally-authored, deliberately simple dataset used only in
Sessions 1–2, before "The Wandering Fork" is introduced in Session 3
(FR-006). Business: **Northside Print Shop**, a small print-and-copy
shop unrelated to the food-truck case study.

### Session 1 table — one morning's print orders (6 items)

| Item | Unit price (€) | Quantity | Line total (€) |
|---|---:|---:|---:|
| Business cards (box of 100) | 18.50 | 4 | 74.00 |
| A4 flyers (pack of 50) | 12.00 | 6 | 72.00 |
| Posters A3 | 6.75 | 10 | 67.50 |
| Spiral-bound reports | 4.20 | 15 | 63.00 |
| Laminated signs | 9.90 | 5 | 49.50 |
| Custom stamps | 15.00 | 2 | 30.00 |
| **Total** | | **42** | **356.00** |

Derived values used in Session 1's worked example (`AVERAGE`, `SUM`,
`MAX`, `MIN`, `LARGE`, percentage distribution, `IF`/`AND`/`OR`):

- Total revenue: €356.00; total items: 42
- % distribution of line total (line total / 356.00): Business cards
  20.79%, Flyers 20.22%, Posters 18.96%, Reports 17.70%, Signs 13.90%,
  Stamps 8.43%
- Highest line total: Business cards (€74.00, `MAX`); lowest: Custom
  stamps (€30.00, `MIN`); top-2 by `LARGE`: Business cards, Flyers
- `IF` example: flag any line with quantity ≥ 10 as `"BULK"` (Posters,
  Reports); `AND`/`OR` example: flag a line for a rush fee if
  quantity ≥ 10 **AND** unit price < €10 (Reports only), or quantity
  ≥ 10 **OR** unit price ≥ €15 (Business cards, Posters, Reports)

### Session 2 table — one week's orders log (for sorting/PivotTables)

12 rows, 3 items × 4 days, used to practice sorting, PivotTables, and
conditional formatting:

| Day | Item | Quantity | Line total (€) |
|---|---|---:|---:|
| Mon | Business cards | 3 | 55.50 |
| Mon | A4 flyers | 5 | 60.00 |
| Mon | Posters A3 | 8 | 54.00 |
| Tue | Business cards | 2 | 37.00 |
| Tue | A4 flyers | 7 | 84.00 |
| Tue | Posters A3 | 6 | 40.50 |
| Wed | Business cards | 5 | 92.50 |
| Wed | A4 flyers | 4 | 48.00 |
| Wed | Posters A3 | 12 | 81.00 |
| Thu | Business cards | 4 | 74.00 |
| Thu | A4 flyers | 6 | 72.00 |
| Thu | Posters A3 | 10 | 67.50 |

Derived values used in Session 2's worked example (sort, PivotTable
sum-by-item, conditional formatting):

- PivotTable sum of line total by item: Business cards €259.00, A4
  flyers €264.00, Posters A3 €243.00; grand total €766.00
- PivotTable sum of line total by day: Mon €169.50, Tue €161.50, Wed
  €221.50, Thu €213.50
- Conditional-formatting example: highlight any line total ≥ €80.00
  in green (Tue flyers €84.00, Wed cards €92.50, Wed posters €81.00)

## Consistency Rule

Every session from 3–12 that references "The Wandering Fork" MUST pull
its numbers from this document/CSV, not recompute or re-invent them.
Any session needing a statistic not listed here (e.g., a specific
day's value) MUST read it directly from
`wandering-fork-dataset.csv` and MAY show its own derivation, but the
underlying raw values MUST NOT change.
