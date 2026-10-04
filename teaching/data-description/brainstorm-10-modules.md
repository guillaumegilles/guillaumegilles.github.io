# Brainstorm — Data Description: 10 × 3h Modules

> **Context.** Descriptive statistics for 2nd-year business school students.  
> **Volume.** 10 modules × 3 h = 30 h contact time.  
> **Running case.** "The Wandering Fork" food-truck dataset (n = 30 trading days).  
> **Key resources.**  
> - Textbook: *Introductory Business Statistics*, 2e (OpenStax, free PDF in folder)  
> - Khan Academy: <https://www.khanacademy.org/math/statistics-probability>  

---

## Design principles

1. **From data to decision.** Every module opens with a business question and closes with a decision the numbers support.
2. **Tools follow theory.** Excel skills are introduced *when the statistical concept requires them*, not as a stand-alone block. This avoids the current "Excel first, stats second" sequencing problem.
3. **Spiral coverage.** The mean is computed three times across the course (grouped, ungrouped, weighted) so students see it in progressively harder contexts.
4. **Two-track exercises.** Each module offers a "by-hand" exercise (conceptual) and an "in Excel" version (applied).
5. **Assessment alignment.** Every concept maps to an exam item type (MCQ, short answer, or Excel output reading).

---

## Mapping: current 12 sessions → 10 modules

| Current session | New module |
|---|---|
| S1 Excel Fundamentals I | Woven into M1 + M3 |
| S2 Excel Fundamentals II (PivotTables) | Woven into M3 + M9 |
| S3 Qualitative graphical | M3 |
| S4 Quantitative graphical (histogram) | M4 |
| S5 Position indicators (quartiles, boxplot) | M6 |
| S6 Central tendency (mean, median, mode) | M5 |
| S7 Dispersion (variance, σ, CV) | M7 |
| S8 Shape (skewness) | M8 |
| S9 Univariate synthesis | Rolled into M8 (short) + M9 (bivariate bridge) |
| S10 Bivariate graphical (contingency, scatter) | M9 |
| S11 Bivariate numerical (cov, corr, regression) | M10 |
| S12 Bivariate synthesis + mock exam | Split: synthesis in M10, mock exam → assessment page |

---

## Module-by-module breakdown

---

### Module 1 — What is statistics? Data types and measurement (3 h)

**Business question.** "The Wandering Fork" has a spreadsheet of 30 trading days. Where do you even start?

**Topics**
- Statistics: descriptive vs inferential; why it matters in management, marketing, finance
- Population vs sample; census vs survey; observation vs experiment
- Variables: qualitative (nominal / ordinal) vs quantitative (discrete / continuous)
- Levels of measurement: nominal, ordinal, interval, ratio — and what arithmetic each allows
- Introduction to the Wandering Fork dataset (columns, types, grain)
- **Excel entry point:** open a CSV, label columns, identify variable types with a colour-code

**Textbook refs** (OpenStax IBS 2e)  
- Ch. 1: Definitions of Statistics, Probability, and Key Terms (§1.1)  
- Ch. 1: Data, Sampling, and Variation in Data and Sampling (§1.2)  
- Ch. 1: Levels of Measurement (§1.3)

**Khan Academy**  
- [Statistical questions](https://www.khanacademy.org/math/statistics-probability/designing-studies/statistical-questions/a/statistical-questions-review) — 10 min  
- [Types of statistical studies](https://www.khanacademy.org/math/statistics-probability/designing-studies) — 20 min  
- [Individuals, variables, and categorical & quantitative data](https://www.khanacademy.org/math/ap-statistics/quantitative-continuous-random-variable-ap) — 15 min

**Excel skills introduced**  
`COUNTA`, `COUNT`, manual data-type annotation

**Assessment idea**  
MCQ: given a list of variables from an annual report, classify each by type and level of measurement.

---

### Module 2 — Organising qualitative data: frequency tables & charts (3 h)

**Business question.** On which weather conditions does the food truck sell most? How concentrated is our payment-method mix?

**Topics**
- Absolute frequency ($n_i$), relative frequency ($f_i$), cumulative frequency ($N_i^+$, $F_i^+$)
- Frequency table for a nominal variable (weather, payment method)
- Frequency table for an ordinal variable (satisfaction score 1–5)
- Charts: bar chart (nominal) vs column chart sorted by rank (ordinal); pie chart and its limits
- Reading and interpreting: mode as the modal class
- **Excel:** `COUNTIF`, `COUNTIFS`, clustered bar chart, pie chart, formatting axes

**Textbook refs**  
- Ch. 2: Stem-and-Leaf Graphs (Stemplots), Line Graphs, Bar Graphs (§2.1 — bar/pie section)  
- Ch. 2: Histograms, Frequency Polygons, and Time Series Graphs (§2.2 — qualitative portion)

**Khan Academy**  
- [Creating frequency tables](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/v/frequency-table) — 10 min  
- [Reading bar charts](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/categorical-data-displays/e/reading-bar-charts) — 15 min  
- [Pie charts](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/categorical-data-displays/a/read-pie-charts) — 10 min

**Excel skills introduced**  
`COUNTIF`, `COUNTIFS`, named ranges, bar/pie chart wizard, data labels

**Assessment idea**  
Given a raw column of 30 weather values, build a complete frequency table and choose the appropriate chart — justify the choice.

---

### Module 3 — Organising quantitative data: histograms & cumulative curves (3 h)

**Business question.** How is daily revenue distributed? Are most days clustered around €600, or is it spread out?

**Topics**
- Why raw continuous data can't be tabled like categorical data
- Building a class frequency table: choosing $k$ (Sturges' rule: $k \approx 1 + 3.3 \log_{10} n$), width $h$, boundaries (half-open convention $[L_i, L_i+h[$)
- Counts, relative frequencies, cumulative frequencies
- Histogram: height = count (equal widths); density = $n_i/h_i$ (unequal widths — exam trap)
- Frequency polygon: midpoints connected by a line
- Cumulative-frequency curve (ogive): upper bounds vs $F_i^+$; reading percentiles from the ogive
- **PivotTable entry point:** group a numeric field into bins with PivotTable grouping

**Textbook refs**  
- Ch. 2: Histograms, Frequency Polygons, and Time Series Graphs (§2.2)

**Khan Academy**  
- [Creating a histogram](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/v/histograms-intro) — 12 min  
- [Interpreting histograms](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/e/interpreting-histograms) — exercises  
- [Cumulative relative frequency graphs](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/v/cumulative-relative-frequency-graph) — 10 min  

**Excel skills introduced**  
`COUNTIFS` (range queries), histogram chart, PivotTable with grouped numeric field

**Assessment idea**  
Short answer: given a 5-class table with one unequal-width class, redraw the histogram with correct density-based heights.

---

### Module 4 — Measures of central tendency (3 h)

**Business question.** What is a "typical" daily revenue? Should we use the mean or the median to plan inventory?

**Topics**
- Arithmetic mean: formula, computation, sensitivity to outliers
- Mean for grouped data (class midpoints): $\bar{x} = \sum f_i m_i$
- Weighted mean (useful for GPA, price indices): $\bar{x}_w = \sum w_i x_i / \sum w_i$
- Median: position formula, linear interpolation from grouped data
- Mode: unimodal, bimodal; modal class
- Comparing mean vs median vs mode: symmetric vs skewed distributions
- **Excel:** `AVERAGE`, `MEDIAN`, `MODE.SNGL`, `MODE.MULT`, `SUMPRODUCT` (weighted mean)

**Textbook refs**  
- Ch. 2: Measures of the Location of the Data — Mean, Median, Mode (§2.3)

**Khan Academy**  
- [Mean, median, mode review](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review) — 15 min  
- [Impact on mean, median of removing a data point](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/more-mean-median/v/impact-on-median-mean-adding-removing-value) — 8 min  
- [Calculating the mean from a frequency table](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-for-frequency-table) — 10 min

**Excel skills introduced**  
`AVERAGE`, `MEDIAN`, `MODE.SNGL`, `SUMPRODUCT`

**Brainstorm note.** This is where the "mean vs median for skewed distributions" lesson lands, which is the single most-tested MCQ concept. Consider making skewed payroll data (CEO + 9 workers) a second mini-dataset alongside the Wandering Fork.

**Assessment idea**  
MCQ battery: 5 questions covering "which measure is affected by an extreme value", "which measure to use for income data", "compute the weighted GPA".

---

### Module 5 — Measures of position: quartiles, percentiles, and the boxplot (3 h)

**Business question.** Where does a €750 revenue day rank? How variable is the top-25% trading days compared to the bottom-25%?

**Topics**
- Quantiles: quartiles ($Q_1, Q_2, Q_3$), deciles, percentiles
- Calculation from sorted data: position formula $L_p = (p/100)(n+1)$; linear interpolation
- Reading $Q_1$, $Q_3$ from the cumulative-frequency curve (ogive)
- Interquartile range $\text{IQR} = Q_3 - Q_1$
- Five-number summary: min, $Q_1$, median, $Q_3$, max
- Boxplot (box-and-whisker): construction, fences, outlier detection ($1.5 \times \text{IQR}$ rule)
- Side-by-side boxplots to compare two groups (e.g. sunny vs rainy days)
- **Excel:** `QUARTILE.INC`, `QUARTILE.EXC`, `PERCENTILE.INC`, `MIN`, `MAX`; manual boxplot construction

**Textbook refs**  
- Ch. 2: Measures of the Location of the Data — Quartiles, Percentiles (§2.3, box-plot section)  
- Ch. 2: Box Plots (§2.4)

**Khan Academy**  
- [Quartiles in statistics](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/v/quartiles-boxes-and-whiskers) — 14 min  
- [Interquartile range (IQR)](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/interquartile-range-iqr/v/calculating-interquartile-range-iqr) — 7 min  
- [Box plot review](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/box-plot-review) — article + exercises

**Excel skills introduced**  
`QUARTILE.INC`, `PERCENTILE.INC`; box-plot from "Insert → Statistic Chart → Box and Whisker"

**Assessment idea**  
Read a boxplot image and answer: median value, IQR, presence of outliers, direction of skew.

---

### Module 6 — Measures of dispersion: variance, standard deviation, CV (3 h)

**Business question.** Two food trucks average €650/day. Which is riskier for a potential investor?

**Topics**
- Range: trivial but easily mislead by outliers
- Mean absolute deviation (MAD) — motivation for squaring deviations
- Population variance $\sigma^2 = \frac{1}{N}\sum(x_i-\mu)^2$ vs sample variance $s^2 = \frac{1}{n-1}\sum(x_i-\bar{x})^2$; the $n-1$ correction (intuition only at this level)
- Standard deviation $\sigma$ and $s$: same unit as the data; useful for "typical distance from the mean"
- Variance for grouped data: $s^2 = \sum f_i (m_i - \bar{x})^2$ (shortcut via $\sum f_i m_i^2 - \bar{x}^2$)
- Coefficient of variation $\text{CV} = s/\bar{x}$: comparing dispersion across different scales/units
- Empirical rule (68-95-99.7) as a first glimpse of the normal distribution
- **Excel:** `VAR.P`, `VAR.S`, `STDEV.P`, `STDEV.S`

**Textbook refs**  
- Ch. 2: Measures of the Spread of Data (§2.7)

**Khan Academy**  
- [Variance and standard deviation of a population](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/v/variance-of-a-population) — 12 min  
- [Sample variance and standard deviation](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/v/sample-variance) — 10 min  
- [More on standard deviation](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/more-on-standard-deviation/v/statistics-standard-deviation) — 14 min

**Excel skills introduced**  
`VAR.P`, `VAR.S`, `STDEV.P`, `STDEV.S`

**Brainstorm note.** This is the most algebraically demanding session. Consider splitting the 3h as: 45 min theory + derivation → 45 min worked examples (by-hand) → 90 min Excel lab. Students struggle most with: (a) knowing when to use $n$ vs $n-1$; (b) computing variance for grouped data.

**Assessment idea**  
Two-part problem: compute $\bar{x}$, $s$, CV for two datasets and conclude which investment is more volatile relative to its return.

---

### Module 7 — Shape of distributions: skewness and kurtosis (3 h)

**Business question.** Does the Wandering Fork's revenue distribution lean towards high days or low days? What does that mean for break-even planning?

**Topics**
- Shape vocabulary: symmetric, right-skewed (positive), left-skewed (negative)
- Relationship: in right-skewed distributions, $\bar{x} > \text{median} > \text{mode}$ (and reverse for left-skewed)
- Pearson's first skewness coefficient: $\gamma_1 = \frac{3(\bar{x} - \text{median})}{s}$
- Pearson's second (moment-based) skewness: $\gamma_1 = \frac{\sum (x_i-\bar{x})^3/n}{s^3}$ (for the curious)
- Reading skewness from a histogram and a boxplot
- Kurtosis: leptokurtic vs platykurtic (conceptual only — excess kurtosis for interest)
- **Excel:** `SKEW` (sample skewness); visual check via histogram

**Textbook refs**  
- Ch. 2: Skewness and the Mean, Median, and Mode (§2.6)

**Khan Academy**  
- [Shapes of distributions](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/shapes-of-distributions/v/shapes-of-distributions) — 8 min  
- [Skewed distributions](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/comparing-features-distributions/v/comparing-mean-median-for-skewed-distribution) — 10 min

**Excel skills introduced**  
`SKEW`; overlaying a normal curve on a histogram (optional enrichment)

**Brainstorm note.** Good opportunity to review all univariate indicators on the Wandering Fork dataset as a synthesis: frequency table → histogram → five-number summary → boxplot → mean / median / mode → variance / std → CV → skewness. One unified dashboard in Excel.

**Assessment idea**  
Given three histograms (A symmetric, B right-skewed, C left-skewed), identify which histogram corresponds to which set of summary statistics.

---

### Module 8 — Bivariate analysis I: contingency tables and scatter plots (3 h)

**Business question.** Does the Wandering Fork sell more on sunny days? Does revenue grow with foot traffic? (Two questions = two variable pairs = two statistical tools.)

**Topics**
- Two-variable problems: qualitative × qualitative, quantitative × quantitative
- Contingency (cross-tabulation) table: joint frequencies, marginal frequencies, conditional frequencies
- Reading a contingency table: are the two variables independent? (qualitative test by comparing conditional profiles — formal chi-squared test is for the next course)
- Scatter plot: axes convention, reading association direction and strength, outliers
- Introduction to the concept of linear vs non-linear association
- **Excel:** 2D `COUNTIFS` for a contingency table; PivotTable for cross-tabs; XY scatter chart

**Textbook refs**  
- Ch. 2: Scatter Plots (§2.5)  
- OpenStax Ch. 13: Linear Regression and Correlation — §13.1 (scatter plots only)

**Khan Academy**  
- [Two-way tables introduction](https://www.khanacademy.org/math/statistics-probability/analyzing-categorical-data/two-way-tables-for-categorical-data/v/two-way-frequency-tables-and-venn-diagrams) — 10 min  
- [Scatter plots](https://www.khanacademy.org/math/statistics-probability/describing-relationships-in-quantitative-data/introduction-to-scatterplots/v/constructing-a-scatter-plot) — 8 min  
- [Describing scatterplots (form, direction, strength, outliers)](https://www.khanacademy.org/math/statistics-probability/describing-relationships-in-quantitative-data/introduction-to-scatterplots/a/describing-scatterplots-form-direction-strength-outliers) — article

**Excel skills introduced**  
2D `COUNTIFS`; PivotTable with two categorical fields; XY scatter chart; trendline overlay

**Assessment idea**  
Read a contingency table and answer: (a) what % of rainy days had revenue < €500? (b) does revenue appear to depend on weather? Justify briefly.

---

### Module 9 — Bivariate analysis II: covariance, correlation, and regression (3 h)

**Business question.** How strongly does foot traffic explain revenue? If 200 people pass per day, what revenue should we budget for?

**Topics**
- Covariance: definition $\text{cov}(X,Y) = \frac{1}{n}\sum(x_i-\bar{x})(y_i-\bar{y})$; sign interpretation; unit problem (scale-dependence)
- Pearson correlation coefficient $r = \text{cov}(X,Y)/(s_X \cdot s_Y)$; range $[-1,1]$; interpretation benchmarks
- **Correlation ≠ causation**: memorable business examples
- Simple linear regression: the least-squares line $\hat{y} = a + bx$; formulas $b = \text{cov}/s_X^2$, $a = \bar{y} - b\bar{x}$
- Interpreting slope and intercept in context (€/person; fixed daily cost)
- Coefficient of determination $R^2 = r^2$; how much variance in $Y$ is explained by $X$
- Prediction and its limits (interpolation vs extrapolation)
- **Excel:** `COVARIANCE.P`, `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`; regression via "Data → Data Analysis → Regression" (Analysis ToolPak)

**Textbook refs**  
- Ch. 13: Linear Regression and Correlation (§13.1–§13.4)  
- Ch. 2: Scatter Plots (§2.5 — revisited)

**Khan Academy**  
- [Introduction to residuals and least-squares regression](https://www.khanacademy.org/math/statistics-probability/describing-relationships-in-quantitative-data/more-on-regression/v/introduction-to-residuals-and-least-squares-regression) — 15 min  
- [Calculating correlation coefficient r](https://www.khanacademy.org/math/statistics-probability/describing-relationships-in-quantitative-data/correlation-coefficient-r/v/calculating-correlation-coefficient-r) — 15 min  
- [Interpreting slope and y-intercept for linear models](https://www.khanacademy.org/math/statistics-probability/describing-relationships-in-quantitative-data/more-on-regression/v/interpreting-slope-and-y-intercept-for-linear-models) — 8 min

**Excel skills introduced**  
`COVARIANCE.P`, `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`; Analysis ToolPak regression output

**Brainstorm note.** This session is dense. Consider reserving 30 min for "reading an Excel regression output table" as an exam skill — students often see ANOVA-style output and panic.

**Assessment idea**  
Given a scatter plot and regression equation, answer: (a) direction and strength of association; (b) predicted revenue for 180 visitors; (c) interpret $R^2 = 0.71$ in plain English.

---

### Module 10 — Synthesis, review, and mock exam (3 h)

**Business question.** Everything together: take a new dataset and produce a complete statistical report — the way a junior analyst actually would.

**Topics**
- Walkthrough: new dataset (e.g. a second food-truck franchise) → full descriptive analysis from scratch
  - Identify variables and levels of measurement
  - Frequency tables and charts
  - Five-number summary + boxplot
  - Mean, median, mode; variance, std, CV; skewness
  - Bivariate: contingency table + scatter + correlation + regression
- Common pitfalls review (exam traps):
  - Histogram bar heights when widths differ
  - $n$ vs $n-1$ in variance
  - $r$ vs $R^2$ — what each tells you
  - Causation language in regression
- **Mock exam** (same MCQ + short-answer format as real exams): 45 min individual → 45 min group debrief

**Textbook refs**  
- Review problems at end of Ch. 2 and Ch. 13

**Khan Academy**  
- [Unit test: Summarizing quantitative data](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)  
- [Unit test: Describing relationships in quantitative data](https://www.khanacademy.org/math/statistics-probability/describing-relationships-in-quantitative-data)

**Excel skills consolidated**  
All functions from previous modules; quick-reference sheet (already exists as `Excel_functions_English_French.txt`)

---

## Open design questions to decide before building

| # | Question | Options | Notes |
|---|---|---|---|
| 1 | Keep Excel as a **woven** skill or restore a dedicated Excel module? | (a) Woven — as above (b) M1 is all Excel — as in current course | Woven feels cleaner; risk is Excel beginners feel lost in M2 |
| 2 | Should M7 (skewness) include kurtosis formally? | (a) Conceptual only (b) Add excess kurtosis formula | Kurtosis rarely appears on business-school exams; keep conceptual |
| 3 | Where does the **weighted mean** live? | (a) M4 (b) A separate enrichment box | Weighted mean is very business-relevant (portfolio returns, GPA) — keep in M4 |
| 4 | Should **time series** be a module? | (a) Add M11 on index numbers and trend (b) Leave for next course | Out of scope for *descriptive* statistics; reference in M10 as "coming next" |
| 5 | Language of instruction | French with English Excel functions, or all English? | Current convention: French theory + English Excel — keep |
| 6 | How many **Shinylive** interactive apps per module? | (a) One per module (b) Only for the hardest visualisations | Currently M3 has one histogram builder — replicate the pattern for M5 (boxplot builder) and M9 (scatter + regression line) |
| 7 | Case study: keep **The Wandering Fork** dataset or extend it? | (a) Same 30-day dataset (b) Add a second franchise for M8–M10 bivariate comparison | Adding a second franchise would make M10 synthesis more realistic |

---

## Textbook chapter alignment summary

| Module | OpenStax IBS 2e primary chapter(s) |
|---|---|
| M1 | Ch. 1 — Sampling and Data |
| M2 | Ch. 2 §2.1, §2.2 (qualitative charts) |
| M3 | Ch. 2 §2.2 (histograms, ogives) |
| M4 | Ch. 2 §2.3 (mean, median, mode) |
| M5 | Ch. 2 §2.3–§2.4 (quartiles, boxplot) |
| M6 | Ch. 2 §2.7 (spread) |
| M7 | Ch. 2 §2.6 (shape) |
| M8 | Ch. 2 §2.5 + Ch. 13 §13.1 (scatter plots) |
| M9 | Ch. 13 §13.1–§13.4 (correlation, regression) |
| M10 | Ch. 2 + Ch. 13 review problems |

---

## Khan Academy unit map

All links are under **Statistics and Probability** (<https://www.khanacademy.org/math/statistics-probability>):

| KA unit | Used in |
|---|---|
| Designing Studies | M1 |
| Displaying & Describing Quantitative Data (categorical) | M2 |
| Displaying & Describing Quantitative Data (quantitative) | M3 |
| Summarizing Quantitative Data — Mean & Median | M4 |
| Summarizing Quantitative Data — Box-and-Whisker | M5 |
| Summarizing Quantitative Data — Variance & Std Dev | M6 |
| Summarizing Quantitative Data — Shapes of Distributions | M7 |
| Analyzing Categorical Data (two-way tables) | M8 |
| Describing Relationships in Quantitative Data | M8, M9 |

---

## Contact-time budget check

| Module | Theory (min) | Excel lab (min) | Exercises (min) | Total |
|---|---|---|---|---|
| M1 | 60 | 30 | 30 | 120 ✓ |
| M2 | 45 | 45 | 30 | 120 ✓ |
| M3 | 50 | 40 | 30 | 120 ✓ |
| M4 | 50 | 30 | 40 | 120 ✓ |
| M5 | 45 | 30 | 45 | 120 ✓ |
| M6 | 55 | 35 | 30 | 120 ✓ |
| M7 | 40 | 20 | 60 | 120 ✓ |
| M8 | 45 | 45 | 30 | 120 ✓ |
| M9 | 50 | 45 | 25 | 120 ✓ |
| M10 | 30 | 0 | 90 (mock exam) | 120 ✓ |
| **Total** | **470** | **320** | **390** | **1 800 min = 30 h** |

---

## Next steps

- [ ] Decide the 7 open design questions above
- [ ] Confirm module filenames convention: `module-01.qmd` inside `modules/` subdirectory
- [ ] Register all 10 modules in `_quarto.yml` sidebar
- [ ] Identify which existing `session-*.qmd` files can be refactored (vs rewritten from scratch)
- [ ] Build the extended Wandering Fork dataset (second franchise) if Question 7 → option b
- [ ] Add Khan Academy links as a "Further reading" collapsible at the bottom of each module page
