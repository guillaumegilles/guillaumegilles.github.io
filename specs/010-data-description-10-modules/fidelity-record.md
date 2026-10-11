# Fidelity Record: Old Session Content → New Modules

One row per `##` section and per callout heading of every pre-redesign
page (sources read from git `HEAD`, since T043 deleted them from the
working tree). `status` ∈ migrated / adapted / dropped; `reason` is
required for adapted and dropped (SC-004).

Old locations (paths under `teaching/data-description/`):

- S1 = `modules/01/excel-worksheet.qmd` (Session 1, Excel warm-up)
- S2 = `modules/02/excel-worksheet.qmd` (Session 2, Excel PivotTables)
- S3 = `modules/01/chapter.qmd` (Session 3; renamed `module-01.qmd`,
  then `module-02.qmd` in T002)
- S4 … S12 = `modules/session-04.qmd` … `modules/session-12.qmd`
- root `glossary.qmd`, root `Excel_functions_English_French.txt`

New locations are under `teaching/data-description/modules/`.

## Session 1 — Excel warm-up (S1)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S1 § Learning objectives | objectives | module-01.qmd § Learning objectives | adapted | Merged into M1 objectives (Excel first steps) |
| S1 Definition — cell reference | theory | module-01.qmd § Using Excel (relative/absolute/mixed) | adapted | Condensed into the Excel table row |
| S1 Formula — percentage distribution | theory | glossary.qmd ($p_i$); module-01.qmd derivation | adapted | Kept as glossary entry and referenced in M1 derivation |
| S1 Formula — percentage change | theory | glossary.qmd ($\Delta\%$) | adapted | Kept as glossary entry only; percentage change is not a descriptive-statistics objective of the new course |
| S1 Definition — logical functions | theory | module-01.qmd § Using Excel (`IF`) | adapted | `AND`/`OR` dropped, `IF` kept |
| S1 § Worked example | worked example | module-01.qmd § Worked example | adapted | Rebuilt on the Wandering Fork dataset |
| S1 § Using Excel | excel | module-01.qmd § Using Excel | migrated | |
| S1 Derivation — percentage shares sum to 100% | derivation | module-01.qmd Derivation — relative frequencies sum to 1 | adapted | Same property, generalised to frequencies |
| S1 § Visual intuition | intuition | module-01.qmd § Visual intuition | adapted | Rewritten around variable types |
| S1 Exercise 1 — Percentage distribution | exercise | module-01.qmd Exercise 5 (Excel) | adapted | Replaced by a dataset-exploration Excel exercise |
| S1 Exercise 2 — Percentage change | exercise | — | dropped | Percentage change is outside the descriptive-statistics scope; index numbers are signposted in M10 "What comes next" |
| S1 Exercise 3 — Nested IF / AND / OR | exercise | — | dropped | Spreadsheet logic is not a course objective; `IF` remains in M1 Using Excel |

## Session 2 — Excel PivotTables (S2)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S2 § Learning objectives | objectives | module-02.qmd, module-03.qmd, module-08.qmd objectives | adapted | Split across M2, M3, M8 |
| S2 Definition — sorting | theory | module-01.qmd § Using Excel (Sort) | adapted | Condensed into the Excel table row |
| S2 Definition — PivotTable | theory | module-02.qmd § Using Excel (PivotTable counts) | migrated | |
| S2 Formula — the sum-by-group property | theory | module-08.qmd Derivation — marginal totals | adapted | Same idea expressed as margins of a contingency table |
| S2 § Worked example | worked example | module-02.qmd § Using Excel; module-03.qmd (PivotTable grouping) | adapted | Rebuilt on the Wandering Fork dataset |
| S2 § Using Excel | excel | module-02.qmd, module-03.qmd, module-08.qmd § Using Excel | migrated | Two-field PivotTable now in M8 |
| S2 Derivation — every grouping gives the same grand total | derivation | module-08.qmd Derivation — marginal totals recover the univariate table | adapted | Generalised to two-way tables |
| S2 § Visual intuition | intuition | module-08.qmd § Visual intuition | adapted | Folded into the contingency-table picture |
| S2 Exercise 1 — PivotTable by group | exercise | module-02.qmd Exercise 5 (Excel); module-03.qmd Exercise 5 (Excel) | adapted | Counts and numeric grouping instead of sums |
| S2 Exercise 2 — Conditional formatting rule | exercise | module-02.qmd Exercise 5 (Excel) | migrated | |
| S2 Exercise 3 — Sort and rank | exercise | module-05.qmd (ordering data for quantiles) | adapted | Sorting kept as the first step of locating quantiles; `RANK` exercise not kept |

## Session 3 — Qualitative data (S3)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S3 § Learning objectives | objectives | module-01.qmd, module-02.qmd objectives | adapted | Split: definitions to M1, tables/charts to M2 |
| S3 Definition — population, individual, variable | theory | module-01.qmd Definition — population, individual, variable | migrated | |
| S3 Definition — nature of a variable | theory | module-01.qmd Definitions — qualitative/quantitative, nominal/ordinal, discrete/continuous | adapted | Expanded with levels of measurement |
| S3 Formula — frequency table | theory | module-02.qmd Definition — absolute and relative frequency | migrated | |
| S3 § The case study: "The Wandering Fork" | theory | dataset.qmd; module-01.qmd § Worked example | adapted | Case moved to the dataset page, now 2 franchises × 120 days |
| S3 § Worked example | worked example | module-02.qmd § Worked example | adapted | Recomputed on the new dataset |
| S3 § Using Excel | excel | module-02.qmd § Using Excel | migrated | |
| S3 Derivation — relative frequencies always sum to 1 | derivation | module-02.qmd Derivation (same title); module-01.qmd | migrated | |
| S3 § Visual intuition | intuition | module-02.qmd § Visual intuition | migrated | |
| S3 Exercise 1 — Frequency table | exercise | module-02.qmd Exercise 1 (by hand) | adapted | Now on `satisfaction_rating` |
| S3 Exercise 2 — Choosing the right chart | exercise | module-02.qmd Exercise 2 (by hand) | migrated | |
| S3 Exercise 3 — Pie-slice angle | exercise | module-02.qmd Exercise 3 (by hand) | migrated | |

## Session 4 — Grouped data and histograms (S4)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S4 § Learning objectives | objectives | module-03.qmd § Learning objectives | migrated | |
| S4 Definition — class (grouped) frequency table | theory | module-03.qmd (same title) | migrated | |
| S4 Formula — cumulative frequency | theory | module-03.qmd Formulas — counts, shares and running totals | migrated | |
| S4 Definition — histogram | theory | module-03.qmd Definition — histogram | migrated | |
| S4 § Worked example | worked example | module-03.qmd § Worked example | migrated | |
| S4 § Using Excel | excel | module-03.qmd § Using Excel | migrated | |
| S4 Derivation — cumulative curve must reach 100% | derivation | module-03.qmd Derivation (same) | migrated | |
| S4 § Visual intuition | intuition | module-03.qmd § Visual intuition | migrated | |
| S4 § Interactive demo — build your own histogram | demo | module-03.qmd § Interactive demo | migrated | Data now embedded from `wandering-fork.csv` |
| S4 Exercise 1 — Reading the cumulative curve | exercise | module-03.qmd Exercise 1 | migrated | |
| S4 Exercise 2 — Unequal class widths | exercise | module-03.qmd Exercise 2 | migrated | |
| S4 Exercise 3 — Frequency polygon midpoint | exercise | module-03.qmd Exercise 3 — Polygon points | migrated | |

## Session 5 — Position: median, quartiles, boxplot (S5)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S5 § Learning objectives | objectives | module-05.qmd § Learning objectives | migrated | |
| S5 Definition — median | theory | module-05.qmd Definition — median; module-04.qmd | migrated | |
| S5 Formula — quartiles (exclusive method) | theory | module-05.qmd (same) | migrated | |
| S5 Formula — IQR and outlier fences | theory | module-05.qmd (same) | migrated | |
| S5 Definition — boxplot | theory | module-05.qmd (same) | migrated | |
| S5 § Worked example | worked example | module-05.qmd § Worked example | migrated | |
| S5 § Using Excel | excel | module-05.qmd § Using Excel | migrated | |
| S5 Derivation — locating a quantile in grouped data | derivation | module-05.qmd (same) | migrated | |
| S5 § Visual intuition | intuition | module-05.qmd § Visual intuition | migrated | |
| S5 § Interactive demo — boxplot from quartiles | demo | module-05.qmd § Interactive demo | migrated | |
| S5 Exercise 1 — Median position | exercise | module-05.qmd Exercise 1 | migrated | |
| S5 Exercise 2 — Outlier check | exercise | module-05.qmd Exercise 2 | migrated | |
| S5 Exercise 3 — Grouped-data interpolation | exercise | module-05.qmd Exercise 3 | migrated | |

## Session 6 — Central tendency (S6)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S6 § Learning objectives | objectives | module-04.qmd § Learning objectives | migrated | |
| S6 Definition — arithmetic mean | theory | module-04.qmd (same) | migrated | |
| S6 Formula — arithmetic mean | theory | module-04.qmd (same) | migrated | |
| S6 Definition — median (recap) | theory | module-04.qmd Definition — median | migrated | |
| S6 Formula — median position | theory | module-04.qmd (same) | migrated | |
| S6 Definition — mode | theory | module-04.qmd (same) | migrated | |
| S6 Formula — mode of grouped continuous data | theory | module-04.qmd (same) | migrated | |
| S6 § Worked example | worked example | module-04.qmd § Worked example | migrated | |
| S6 § Using Excel | excel | module-04.qmd § Using Excel | migrated | |
| S6 Derivation — mean minimises sum of squared deviations | derivation | module-04.qmd (same) | migrated | |
| S6 § Visual intuition | intuition | module-04.qmd § Visual intuition | migrated | |
| S6 Exercise 1 — Mean vs median with an outlier | exercise | module-04.qmd Exercise 1 | migrated | |
| S6 Exercise 2 — Choosing an indicator | exercise | module-04.qmd Exercise 2 | migrated | |
| S6 Exercise 3 — Grouped mode | exercise | module-04.qmd Exercise 3 | migrated | |

## Session 7 — Dispersion (S7)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S7 § Learning objectives | objectives | module-06.qmd § Learning objectives | migrated | |
| S7 Definition — range and IQR | theory | module-06.qmd (same) | migrated | |
| S7 Formula — sample variance and standard deviation | theory | module-06.qmd (same) | migrated | |
| S7 Formula — coefficient of variation | theory | module-06.qmd (same) | migrated | |
| S7 § Worked example | worked example | module-06.qmd § Worked example | migrated | |
| S7 § Using Excel | excel | module-06.qmd § Using Excel | migrated | |
| S7 Derivation — variance shortcut formula | derivation | module-06.qmd (same) | migrated | |
| S7 § Visual intuition | intuition | module-06.qmd § Visual intuition | migrated | |
| S7 § Interactive demo — central tendency & dispersion | demo | module-06.qmd § Interactive demo | migrated | Kept as optional demo |
| S7 Exercise 1 — Shortcut formula | exercise | module-06.qmd Exercise 1 | migrated | |
| S7 Exercise 2 — Comparing variability across units | exercise | module-06.qmd Exercise 2 | migrated | |
| S7 Exercise 3 — Effect of an outlier on the range | exercise | module-06.qmd Exercise 3 | migrated | |

## Session 8 — Shape (S8)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S8 § Learning objectives | objectives | module-07.qmd § Learning objectives | migrated | |
| S8 Definition — symmetry and skewness | theory | module-07.qmd (same) | migrated | |
| S8 Formula — Fisher-Pearson sample skewness | theory | module-07.qmd (same) | migrated | |
| S8 Definition — alternative asymmetry coefficients | theory | module-07.qmd (same) | migrated | |
| S8 Formula — Pearson and Yule-Kendall coefficients | theory | module-07.qmd (same) | migrated | Median form of Pearson added |
| S8 § Worked example | worked example | module-07.qmd § Worked example | migrated | |
| S8 § Using Excel | excel | module-07.qmd § Using Excel | migrated | |
| S8 Derivation — bias correction in `SKEW` | derivation | module-07.qmd (same) | migrated | |
| S8 § Visual intuition | intuition | module-07.qmd § Visual intuition | migrated | |
| S8 Exercise 1 — Reading sign and magnitude | exercise | module-07.qmd Exercise 1 | migrated | |
| S8 Exercise 2 — Reconciling mean/median/mode order | exercise | module-07.qmd Exercise 2 | migrated | |
| S8 Exercise 3 — Yule-Kendall from five-number summary | exercise | module-07.qmd Exercise 3 | migrated | |

## Session 9 — Univariate review (S9)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S9 § Learning objectives | objectives | module-07.qmd § Learning objectives (review) | adapted | Review session folded into the end of M7 |
| S9 § Theory recap / Recap table (Sessions 3–8) | theory | module-07.qmd univariate review; glossary.qmd | adapted | Formula recap replaced by the glossary and a short review |
| S9 § Worked example | worked example | module-07.qmd univariate review; Exercise 6 (Excel) | adapted | Shortened into one end-to-end workflow |
| S9 § Using Excel | excel | module-07.qmd § Using Excel | adapted | Merged with M7 Excel section |
| S9 Derivation — why $Q_1 \le Me \le Q_3$ | derivation | module-07.qmd (review) | adapted | Kept as a short argument inside the review |
| S9 § Visual/geometric intuition | intuition | module-07.qmd § Visual intuition | adapted | Merged |
| S9 Exercises 1–3 | exercise | module-07.qmd Exercises 4–6; module-10.qmd mock exam | adapted | Review exercises consolidated into M7 Excel exercises and the M10 mock exam |

## Session 10 — Two variables I (S10)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S10 § Learning objectives | objectives | module-08.qmd § Learning objectives | migrated | |
| S10 Definition — contingency table | theory | module-08.qmd (same) | migrated | |
| S10 Definition — conditional distribution | theory | module-08.qmd (same) | migrated | |
| S10 Definition — scatter plot | theory | module-08.qmd (same) | migrated | |
| S10 § Worked example | worked example | module-08.qmd § Worked example | migrated | |
| S10 § Using Excel | excel | module-08.qmd § Using Excel | migrated | |
| S10 Derivation — marginal totals | derivation | module-08.qmd (same) | migrated | |
| S10 § Visual intuition | intuition | module-08.qmd § Visual intuition | migrated | |
| S10 Exercise 1 — Reading a contingency table | exercise | module-08.qmd Exercise 1 | migrated | |
| S10 Exercise 2 — Column margin check | exercise | module-08.qmd Exercise 2 | migrated | |
| S10 Exercise 3 — Describing a scatter plot | exercise | module-08.qmd Exercise 3 | migrated | |

## Session 11 — Two variables II (S11)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S11 § Learning objectives | objectives | module-09.qmd § Learning objectives | migrated | |
| S11 Formula — covariance | theory | module-09.qmd (same) | migrated | |
| S11 Formula — correlation coefficient | theory | module-09.qmd (same) | migrated | |
| S11 Formula — least-squares regression line | theory | module-09.qmd (same) | migrated | |
| S11 § Worked example | worked example | module-09.qmd § Worked example | migrated | |
| S11 § Using Excel | excel | module-09.qmd § Using Excel | migrated | |
| S11 Derivation — bounds $-1 \le r \le 1$ | derivation | module-09.qmd (same) | migrated | |
| S11 § Visual intuition | intuition | module-09.qmd § Visual intuition | migrated | |
| S11 § Interactive demo — scatter plot & correlation | demo | module-09.qmd § Interactive demo | migrated | |
| S11 Exercise 1 — Interpreting $r^2$ | exercise | module-09.qmd Exercise 1 | migrated | |
| S11 Exercise 2 — Prediction from the regression line | exercise | module-09.qmd Exercise 2 | migrated | |
| S11 Exercise 3 — Sign of slope vs sign of $r$ | exercise | module-09.qmd Exercise 3 | migrated | |

## Session 12 — Bivariate review and mock exam (S12)

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| S12 § Learning objectives | objectives | module-10.qmd § Learning objectives | adapted | Now a whole-course synthesis |
| S12 § Theory recap / Recap table (Sessions 10–11) | theory | module-10.qmd walkthrough; glossary.qmd | adapted | Recap replaced by a full walkthrough on Lakeside Bakery |
| S12 § Worked example | worked example | module-10.qmd § Worked example (Lakeside Bakery) | adapted | Rebuilt on a fresh dataset |
| S12 § Using Excel | excel | module-10.qmd § Using Excel | adapted | Points to excel-functions.qmd |
| S12 Derivation — regression line passes through $(\bar{x},\bar{y})$ | derivation | module-09.qmd Formula — the regression line passes through $(\bar{x},\bar{y})$ | adapted | Moved to M9; M10 derivation is now "overall mean as weighted mean" |
| S12 § Visual/geometric intuition | intuition | module-10.qmd § Visual intuition | adapted | Rewritten as whole-course consolidation |
| S12 Exercise 1 — Reading the summary table | exercise | module-10.qmd Exercise 3 | adapted | Lakeside Bakery walkthrough |
| S12 Exercise 2 — Predicting from the regression line | exercise | module-10.qmd Exercise 2 (d) | adapted | Now on Campus customers → revenue |
| S12 Exercise 3 — Contingency table consistency | exercise | module-10.qmd Exercise 2 (a) | adapted | |
| S12 § Mock exam — Sessions 1–12 | exam | module-10.qmd § Mock exam — Modules 1–9 | adapted | Originally re-authored; every answer maps to a module |
| S12 Q1–Q7 (MCQ) | exam | module-10.qmd Q1–Q10 | adapted | Rewritten for module mapping; extended to 10 MCQ |
| S12 Part B Exercise | exam | module-10.qmd Exercises 1–3 | adapted | Split into three computational problems |

## Reference material

| old_location | type | new_location | status | reason |
|---|---|---|---|---|
| `glossary.qmd` (root) | reference | modules/glossary.qmd | adapted | "Session N" → "Module N"; conventions table added |
| `Excel_functions_English_French.txt` | reference | modules/excel-functions.qmd | adapted | Converted to a page; all pairs kept, new functions added |

## Demo callouts still marked `TODO:` (T036)

<!--
Modules whose interactive demo is a TODO callout (no required demo):
- M1  — variable-type classifier (drag a column to its type and level)
- M2  — frequency-table builder with live bar/pie chart
- M4  — mean/median/mode explorer on an editable sample
- M7  — skewness visualiser (editable sample, live histogram and value)
- M8  — contingency-table builder with live conditional distributions
- M10 — full-workflow dashboard (upload CSV, auto-generate tables/charts)
Working Shinylive demos: M3 (histogram), M5 (boxplot), M6 (dispersion,
optional), M9 (scatter + regression).
-->

- M1, M2, M4, M7, M8, M10: `TODO:` demo callouts (details in the
  comment above).
- M3, M5, M6, M9: working Shinylive demos.
