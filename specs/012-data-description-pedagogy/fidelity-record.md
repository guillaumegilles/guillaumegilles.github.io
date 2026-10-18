# Fidelity Record — Concrete-to-Abstract Pedagogy

Constitution T-I: no theory, worked example, derivation, demo, exercise
or solution may be removed. Every moved, renumbered or added block is
logged here and referenced in the commit message.

## Baseline (before revision)

v1 checker (`specs/010-data-description-10-modules/check_modules.py`),
run 2026-10-13 on branch `012-data-description-pedagogy` before any edit:

| Module | Result |
|---|---|
| module-06.qmd | OK (structure checks passed) |
| module-07.qmd | OK |
| module-08.qmd | OK |
| module-09.qmd | OK |
| module-10.qmd | OK |

Total minutes for the 5 files: 900. The "expected 1800" warning only
appears because 5 of the 10 modules were checked. Line-length warnings
were present before the revision and are not listed.

## Module 6

| Old block (feature 010) | New location | Change | Verified |
|---|---|---|---|
| Intro "business question" (Harbour mean €628.34) | Intro | Kept; one sentence added leading to the hook | ✓ |
| Learning objectives (4 bullets) | Learning objectives (6 bullets) | Reworded around concepts and notation; calculator objective kept | ✓ |
| Time plan (75 / 50 / 55) | Time plan | Replaced by research R5 (Hook 10 … Excel preview 5 = 180) | ✓ |
| Theory › Range and IQR (definition callout + plain words) | Theory › Range and IQR | Same text, now after Try it; IQR recall + Module 5 link added | ✓ |
| Theory › Sample variance and SD (formula callout + plain words) | Theory › Sample variance and SD | Same text, now after the deviation table; decoder added | ✓ |
| "Why $n-1$" warning | After the variance decoder | Verbatim; preceded by "4 of 5 deviations are free" | ✓ |
| Theory › CV (formula callout + plain words) | Theory › CV | Same text, now after Try it; decoder added | ✓ |
| Theory › Shortcut formula (formula callout) | Theory › Shortcut | Verbatim (incl. `SUMSQ` sentence); Try it + decoder added | ✓ |
| Worked example (values table, Steps 1–4) | Worked example | Unchanged (git diff: no value line deleted) | ✓ |
| Interpreting $CV$ table | Worked example › Interpreting $CV$ | Unchanged | ✓ |
| Using Excel (table, sample-vs-population note, `tblFork` tip) | Homework — Excel lab › Using Excel | Moved, H2 → H3, content unchanged | ✓ |
| Proof / derivation (shortcut) | Proof / derivation | Unchanged | ✓ |
| Visual intuition | Visual intuition | Kept; one paragraph added linking to figure step 3 | ✓ |
| Interactive demo (Shinylive) | Interactive demo | **Re-implemented in OJS** (2026-10-13, after the owner's visual check): the Shinylive block never ran, because no `filters: [shinylive]` was active for `modules/` and the page showed raw code. Same 6 sliders and start values, same outputs (mean, median, $s^2$, $s$, $CV$) and the same "deviations from the mean" chart. Values checked against NumPy for the start values: 628.53 / 609.84 / 37,684.02 / 194.12 / 30.89%. Built-in `html` only, no CDN | ✓ |
| Exercise 1 (by hand) — Shortcut formula | Exercise 1 (by hand) | Unchanged | ✓ |
| Exercise 2 (by hand) — Comparing variability across units | Exercise 2 (by hand) | Unchanged | ✓ |
| Exercise 3 (by hand) — Effect of an outlier on the range | Exercise 3 (by hand) | Unchanged | ✓ |
| Exercise 4 (Excel) — Campus revenue | Homework 1 (Excel) | Moved, renumbered; one "How to" line added; statement and solution verbatim | ✓ |
| Exercise 5 (Excel) — Shortcut with `SUMSQ` | Homework 2 (Excel) | Same as above | ✓ |
| Exercise 6 (Excel) — Payroll skew | Homework 3 (Excel) | Same as above | ✓ |
| Common mistakes | Common mistakes | Unchanged | ✓ |
| Further reading | Further reading | Unchanged | ✓ |

### New blocks in Module 6

| New block | Location | Notes |
|---|---|---|
| Hook "Same mean, different days" | Theory, first subsection | Trucks A/B table (research R2) |
| OJS two-truck figure (3 steps) | End of the hook | **Placement differs from T010**: placed once in the hook so it serves the range *and* variance "See it" steps; both subsections point to it. Uses the built-in OJS `html` template only (no Plot, Inputs or d3), because the Quarto runtime fetches those from `cdn.jsdelivr.net` (Principle IV) |
| Try it × 4 (range, deviation table, CV, shortcut) + answer callouts | Theory | CV Try it adds a coffee-cart comparison (mean €62, $s$ = €20 → 32.26%) |
| Notation decoders × 3 | After each formula callout | Variance/SD, CV, shortcut |
| Exercise 4 (by hand) — Formula to words | Exercises | New |
| Exercise 5 (by hand) — Words to formula | Exercises | New |
| Exit check (5 questions + answers) | After Common mistakes | New |
| Homework intro, Step 0 + expected results | Homework | New |
| Glossary rows $x_i$, $\sum$ (Module 4), $x_i-\bar{x}$ (Module 6) | `glossary.qmd` | New |

### Module 6 — contract v2.1 markup (2026-10-18)

Owner decisions: `## Time plan` removed from the page; collapsible
callouts replaced by lighter markup (`convert_callouts.py`). All
statements, answers and solutions moved verbatim.

| Old markup | New markup | Count |
|---|---|---|
| `#### Try it — check your answer` callout | `<details class="answer">` "Check your answer" | 4 |
| `#### Exercise k (by hand) — T (click for solution)` callout | `::: {#exr-… name="T"}`, statement visible, solution folded; `**Solution.**` label becomes the fold's summary; numbering by Quarto (same order, 1–5) | 5 |
| `#### Exit check — answers` callout | Answer fold "Answers" | 1 |
| `#### Step 0 — expected results` callout | Answer fold "Expected results" | 1 |
| `#### Homework k (Excel) — T (click for solution)` callout | `### Homework k (Excel) — T` heading, statement and How-to visible, solution folded | 3 |
| Derivation callout | Unchanged | 1 |

New: one intro line under `## Exercises` ("All exercises below are done
by hand…"). Styling added to `assets/dark.scss` (`.theorem.exercise`,
`details.answer`).

### Other files changed in phase A

| File | Change |
|---|---|
| `module-07.qmd` | `Homework debrief` 10 min added; Excel lab 50 → 40 (T022) |
| `index.qmd` | One rollout-safe sentence on the Module 6 pilot (T023) |
| `fr/teaching/data-description/modules/*.qmd` (13) | French stubs (FR-021, T042) |
| `fr/teaching/data-description/index.qmd` | Link to the English version added |
| `_quarto.yml` | `fr-data-description` sidebar block (T043) |
| `specs/010-.../check_modules.py` | Time plan sums all rows (T004) |

## Module 7

| Old block (feature 010) | New location | Change | Verified |
|---|---|---|---|
| Intro "business question" (Harbour mean €628.34, $s$ €137.09) | Intro | Kept verbatim; one sentence added leading to the hook | ✓ |
| Learning objectives (5 bullets) | Learning objectives (6 bullets) | Reworded around concepts and notation (cubed-deviation table, read formula aloud, kurtosis in words, words → formula); "Read skewness directly off a histogram or boxplot" kept verbatim; Excel objectives (`SKEW`, full Excel workflow) moved to the homework intro | ✓ |
| Time plan (Debrief 10 / Theory 60 / Excel lab 40 / Exercises 70) | Time plan | First row `Homework debrief` kept verbatim; rest replaced by Hook 10, Concrete build 45, Notation 25, Kurtosis 10, Worked example 20, Practice 45, Exit check 10, Excel preview 5 = 180; "Excel lab is now homework" line added | ✓ |
| Theory › Symmetry and skewness (definition callout) | Theory › Symmetry and skewness | Verbatim, now after Try it (centre order on three trucks) + See it (figure step 2) | ✓ |
| "In plain words" (symmetric = balanced …) | Theory › Symmetry and skewness, Say it | Merged: text kept, one sentence added ("The mean is dragged toward the tail …") | ✓ |
| Theory › Fisher-Pearson (formula callout) | Theory › Fisher-Pearson | Verbatim, now after the cubed-deviation Try it, "Why cube and not square?" and See it (figure step 3); decoder added | ✓ |
| "In plain words" (cube the standardized deviations …) | Theory › Fisher-Pearson, Say it | Merged: same wording, prefixed with "measure each deviation in standard deviations"; correction-factor sentence kept | ✓ |
| Theory › Alternative asymmetry coefficients (definition callout) | Theory › Alternative asymmetry coefficients | Verbatim, now after the Pearson and Yule-Kendall Try its (quartile recall + Module 5 link), See it (figure step 4) and a new Say it | ✓ |
| Formula callout — Pearson and Yule-Kendall | Same subsection, after the definition | Verbatim; decoder added | ✓ |
| Warning "Different skewness formulas can genuinely disagree …" | After the Pearson/YK decoder | Verbatim | ✓ |
| Theory › Kurtosis (definition callout) | Theory › Kurtosis (conceptual only) | Verbatim, now after a Station-vs-Park Try it, a Markdown number-line See it and a Say it | ✓ |
| Worked example (values table, Steps 1–4) | Worked example | Unchanged (git diff: no value line deleted) | ✓ |
| Worked example › Campus franchise (right-skewed case) | Worked example › Campus franchise | Unchanged | ✓ |
| Using Excel (table + `tblFork` tip) | Homework — Excel lab › Using Excel | Moved, H2 → H3, content unchanged | ✓ |
| Proof / derivation (bias-correction factor of `SKEW`) | Proof / derivation | Unchanged | ✓ |
| Visual intuition | Visual intuition | Kept; one paragraph added linking to figure steps 2–4 | ✓ |
| Interactive demo (TODO callout) | Interactive demo | Unchanged | ✓ |
| Exercise 1 (by hand) — Reading the sign and magnitude | Exercise 1 (by hand) | Unchanged | ✓ |
| Exercise 2 (by hand) — Reconciling mean/median/mode order | Exercise 2 (by hand) | Unchanged | ✓ |
| Exercise 3 (by hand) — Yule-Kendall from a five-number summary | Exercise 3 (by hand) | Unchanged | ✓ |
| Exercise 4 (Excel) — Skewness for Campus revenue | Homework 1 (Excel) | Moved, renumbered; one "How to" line added; statement and solution verbatim | ✓ |
| Exercise 5 (Excel) — Payroll skew: skewness | Homework 2 (Excel) | Same as above | ✓ |
| Exercise 6 (Excel) — Full univariate workflow for Campus revenue | Homework 3 (Excel) | Same as above | ✓ |
| Common mistakes | Common mistakes | Unchanged | ✓ |
| Further reading | Further reading | Unchanged | ✓ |

### New blocks in Module 7

| New block | Location | Notes |
|---|---|---|
| Hook "Same mean, same spread, different shapes" | Theory, first subsection | Station / Stadium / Market table, all mean €600 and $s$ €60 (research R13); no formula, no callout |
| OJS three-truck figure (4 steps: dots, mean/median/mode, cubes, quartiles) | End of the hook | Placed once in the hook (as in Module 6) and referenced by the See it steps of every concept cycle. Built-in `html` template + inline SVG only (no Plot, Inputs or d3 — Principle IV); all statistics computed in JS from the data arrays; JS checked under `node` |
| Try it × 6 (centre order; cubed deviations; Pearson; Yule-Kendall; reading the box; Station vs Park) + 5 answer callouts | Theory | Pearson and Yule-Kendall share one answer callout; Fisher-Pearson ÷ 216 and × 5/12 given as a calculator step (R13) |
| "Why cube and not square?" paragraph | Theory › Fisher-Pearson | Links to Module 6's squares |
| Subsection "Reading skew from a chart" | Theory, before Kurtosis | Try it + See it + Say it, then a link to Visual intuition. **No Write-it callout**: v1 has no definition/formula for chart reading (its content lives in Visual intuition, kept there), and adding a new definition would duplicate it |
| Kurtosis See it (Markdown number line, Station vs Park) | Theory › Kurtosis | Table instead of figure (template §5) |
| Notation decoders × 2 | After each formula callout | Fisher-Pearson; Pearson and Yule-Kendall |
| Exercise 4 (by hand) — Formula to words | Exercises | New; (b) $(500-440)/120 = 0.5$ |
| Exercise 5 (by hand) — Words to formula | Exercises | New |
| Exit check (5 questions + answers) | After Common mistakes | New; Q4 $YK = 8/16 = 0.5$ |
| Homework intro, Step 0 + expected results | Homework | New; intro carries the former Excel learning objectives; follow-up in Module 8 |
| Glossary rows (proposed) | `drafts/m7-glossary.md` | Standardized deviation, small-sample factor |

## Module 8

| Old block (feature 010) | New location | Change | Verified |
|---|---|---|---|
| Intro "business question" (weather, promotions; two tools) | Intro | Kept; last sentence rewrapped and one sentence added leading to the hook | ✓ |
| Learning objectives (5 bullets) | Learning objectives (6 bullets) | Reworded around concepts and notation ($n_{ij}$, $n_{i\cdot}$, $n_{\cdot j}$, $n_{i\cdot}/n$, $n_{ij}/n_{i\cdot}$); conditional-distribution and "pattern vs proof" bullets kept verbatim. No v1 objective was Excel-specific; the Excel skills (`COUNTIFS`, PivotTable, XY scatter) are named in the homework intro | ✓ |
| Time plan (Theory 60 / Excel lab 60 / Exercises 60) | Time plan | Replaced: Homework debrief 10, Hook 10, Concrete build 40, Notation 20, Scatter plot 20, Worked example 20, Practice 45, Exit check 10, Excel preview 5 = 180 | ✓ |
| Theory › Contingency table (definition callout) | Theory › Contingency table | Verbatim, now after the ten-day tally Try it and See it; decoder added (callout contains $n_{i\cdot} = \sum_j n_{ij}$, $n_{\cdot j} = \sum_i n_{ij}$) | ✓ |
| Theory › Contingency table "In plain words" | Theory › Contingency table | Verbatim, now the Say it step before the definition | ✓ |
| Theory › Conditional distribution (definition callout) | Theory › Conditional distribution | Verbatim, now after Try it (row percentages of the hook table) and See it; followed by a new formula callout and its decoder | ✓ |
| Theory › Conditional distribution "In plain words" (Sunny vs Rainy) | Theory › Conditional distribution | Verbatim, Say it step; it now refers to the hook's Sunny/Rainy table | ✓ |
| Theory › Scatter plot (definition callout) | Theory › Scatter plot | Verbatim, now after Try it (five pairs) and the OJS figure | ✓ |
| Theory › Scatter plot "In plain words" | Theory › Scatter plot | Verbatim, Say it step | ✓ |
| Worked example › Contingency table (table, Steps 1–3) | Worked example | Unchanged (git diff: no value line deleted) | ✓ |
| Worked example › Scatter plot paragraph | Worked example | Unchanged | ✓ |
| Using Excel (table, `tblFork` `COUNTIFS` tip) | Homework — Excel lab › Using Excel | Moved, H2 → H3, content unchanged | ✓ |
| Proof / derivation (marginal totals) | Proof / derivation | Unchanged | ✓ |
| Visual intuition | Visual intuition | Kept; one paragraph added linking to step 2 of the scatter figure (quadrants → Module 9 covariance) | ✓ |
| Interactive demo (`TODO:` callout) | Interactive demo | Unchanged | ✓ |
| Exercise 1 (by hand) — Reading a contingency table | Exercise 1 (by hand) | Unchanged | ✓ |
| Exercise 2 (by hand) — Column margin check | Exercise 2 (by hand) | Unchanged | ✓ |
| Exercise 3 (by hand) — Describing a scatter plot | Exercise 3 (by hand) | Unchanged | ✓ |
| Exercise 4 (Excel) — Build the contingency table for Campus | Homework 1 (Excel) | Moved, renumbered; one "How to" line added; statement and solution verbatim | ✓ |
| Exercise 5 (Excel) — Conditional distribution: revenue given promo | Homework 2 (Excel) | Same as above | ✓ |
| Exercise 6 (Excel) — Scatter plot: foot traffic vs revenue | Homework 3 (Excel) | Same as above | ✓ |
| Exercise 7 (Excel) — Harbour vs Campus: weather and revenue | Homework 4 (Excel) | Same as above (code block and table verbatim) | ✓ |
| Common mistakes | Common mistakes | Unchanged | ✓ |
| Further reading | Further reading | Unchanged | ✓ |

### New blocks in Module 8

| New block | Location | Notes |
|---|---|---|
| Hook "Sun, rain and medium days" | Theory, first subsection | 50-day 2×3 table, counts only (R14); "9 vs 6 medium days" question |
| Try it × 4 (ten-day tally, margins, row percentages, five pairs) + answer callouts | Theory | Data in R14 |
| See it × 4 | Theory | Dot-tally table; margin bar table; conditional 100%-bar table; OJS scatter figure |
| "Recall" of $f_i = n_i/n$ (Module 2) | Theory › Marginal distributions | Links to `module-02.qmd` |
| Formula callout "Formula — marginal distributions" ($n_{i\cdot}/n$, $n_{\cdot j}/n$) | Theory › Marginal distributions | **New `.callout-tip`, deviation from "existing callout verbatim"**: v1 had no separate marginal callout (margins were only defined inside the contingency definition). Uses only symbols already on the page / in the glossary |
| Formula callout "Formula — conditional distributions" ($n_{ij}/n_{i\cdot}$, $n_{ij}/n_{\cdot j}$) | Theory › Conditional distribution, after the verbatim definition | New `.callout-tip`, same reason: the v1 definition is words only; the worked example's "rescale by 13" is this ratio |
| Notation decoders × 3 | After the contingency definition and after each new formula callout | Contingency table (ten-day values), marginal and conditional (50-day values) |
| Section "Marginal distributions" (`###`) | Theory, between Contingency table and Conditional distribution | v1 covered margins inside the contingency definition only |
| OJS scatter figure (2 steps: points → mean lines/quadrants) + caption cell | Theory › Scatter plot, See it | Built-in `html` + inline SVG only (no Plot, Inputs or d3); colours as SVG attributes; means and quadrant lists computed in JS; logic checked under `node` |
| Exercise 4 (by hand) — Formula to words | Exercises | On the worked-example table: $n_{3\cdot} = 5$, $n_{\cdot 1} = 6$, 60% vs 50% |
| Exercise 5 (by hand) — Words to formula | Exercises | On the hook table: $n_{23}$, $n_{1\cdot}/n$, $n_{13}/n_{\cdot 3}$, $n_{\cdot 2}$ |
| Exit check (5 questions + answers) | After Common mistakes | New |
| Homework intro, Step 0 + expected results | Homework | Ten-day table via `COUNTIFS`/PivotTable, 50-day row percentages, scatter + `AVERAGE` |

## Module 9

| Old block (feature 010) | New location | Change | Verified |
|---|---|---|---|
| Front matter (`date-modified: 2026-10-08`) | Front matter | `date-modified` → 2026-10-17; title, subtitle, `lang` unchanged | ✓ |
| Intro "business question" (Module 8 scatter → three summaries) | Intro | Kept verbatim; one sentence added leading to the hook | ✓ |
| Learning objectives (5 bullets) | Learning objectives (6 bullets) | Three compute bullets reworded around concepts, hand computation and notation (Cov, $r$, $r^2$, $a$, $b$, deviation-product table, line through $(\bar{x},\bar{y})$); formula ↔ words bullet added; demo and proof bullets kept verbatim. v1 had no Excel objective; the Excel objective is stated in the homework intro | ✓ |
| Time plan (Theory 70 / Excel lab 55 / Exercises 55) | Time plan | Replaced: Homework debrief 10, Hook 10, Concrete build 40, Notation 20, Regression line 20, Worked example 20, Practice 45, Exit check 10, Excel preview 5 = 180 | ✓ |
| Theory › Covariance (formula callout) | Theory › Covariance | Callout byte-for-byte; now after the deviation-product Try it, "Why multiply?", See it; decoder added | ✓ |
| Theory › Covariance "In plain words" | Theory › Covariance (Say it) | Merged into the Say-it line; "revenue deviation" → "sales deviation" so it fits the items-sold mini-data; rest verbatim | ✓ |
| Theory › Correlation coefficient (formula callout, incl. $r^2$ sentence) | Theory › Correlation coefficient | Callout byte-for-byte; now after the standardising Try it ($s_X s_Y = 50$, $r = 0.8$, unit change) and See it; decoder added (covers $r^2$) | ✓ |
| Theory › Correlation "In plain words" | Theory › Correlation (Say it) | Verbatim, now in the Say-it position | ✓ |
| Theory › Least-squares regression line (formula callout) | Theory › Least-squares regression line | Callout byte-for-byte; now after the slope/intercept/residual Try it, "Why least squares?", "Back to $r^2$", See it; decoder added | ✓ |
| Theory › Regression "In plain words" | Theory › Regression (Say it) | Verbatim, now in the Say-it position | ✓ |
| Theory › Bounds on $r$ (formula callout, Cauchy–Schwarz) | Theory › Bounds on $r$ | Callout byte-for-byte; Try it (25,600 ≤ 40,000), See it, Say it and decoder added | ✓ |
| Theory › Regression through $(\bar{x},\bar{y})$ (formula callout) | Theory › Regression through $(\bar{x},\bar{y})$ | Callout byte-for-byte; Try it (plug in 22 → 80), See it, Say it and decoder added | ✓ |
| Worked example (values table, Steps 1–4) | Worked example | Unchanged (git diff: no line deleted) | ✓ |
| Worked example › Campus franchise and the full 120 days | Worked example › same H3 | Unchanged | ✓ |
| Using Excel (function table incl. `COVARIANCE.P`, trendline, **Analysis ToolPak** row; `tblFork` tip) | Homework — Excel lab › Using Excel | Moved, H2 → H3, content unchanged; old `## Using Excel` deleted | ✓ |
| Proof / derivation (bounds on $r$) | Proof / derivation | Unchanged | ✓ |
| Visual intuition | Visual intuition | Kept verbatim; one paragraph added linking to step 4 of the five-day figure | ✓ |
| Interactive demo — scatter plot & correlation (OJS, converted 2026-10-13) | Interactive demo | Unchanged (block byte-for-byte; defines no top-level OJS names, so no collision with the new `mini*` cells) | ✓ |
| Exercise 1 (by hand) — Interpreting $r^2$ | Exercise 1 (by hand) | Unchanged | ✓ |
| Exercise 2 (by hand) — Prediction from the regression line | Exercise 2 (by hand) | Unchanged | ✓ |
| Exercise 3 (by hand) — Sign of the slope vs. sign of $r$ | Exercise 3 (by hand) | Unchanged | ✓ |
| Exercise 4 (Excel) — Correlation and regression for Campus | Homework 1 (Excel) | Moved, renumbered; one "How to" line added; statement and solution verbatim | ✓ |
| Exercise 5 (Excel) — Regression prediction and $(\bar{x},\bar{y})$ check | Homework 2 (Excel) | Same as above | ✓ |
| Exercise 6 (Excel) — Full regression output with Analysis ToolPak | Homework 3 (Excel) | Same as above (ToolPak enabling steps kept in the statement) | ✓ |
| Common mistakes | Common mistakes | Unchanged | ✓ |
| Further reading (5 OpenStax rows, Khan Academy, licence note) | Further reading | Unchanged | ✓ |

### New blocks in Module 9

| New block | Location | Notes |
|---|---|---|
| Hook "Hot days, busy days?" | Theory, first subsection | 5-day temperature / items-sold table (research R15); no formula, no callout |
| OJS five-day figure (4 steps: points; means and quadrants; products as rectangles; regression line with gaps) | End of the hook | Placed once, like Module 6, and referenced by every "See it". Built-in `html` + inline SVG only (no Plot, Inputs or d3 — Principle IV); all captions computed from `miniX`/`miniY`; top-level names prefixed `mini` (`miniX`, `miniY`, `miniStats`, `miniFmt`, `viewof miniStep`); logic checked with `node` |
| Try it × 6 (deviation products → Cov; squares → $s_X s_Y$ → $r$ + unit change; $r^2$ table; slope, intercept, residuals, prediction; Cauchy–Schwarz; plug in $\bar{x}$) + answer callouts | Theory | All values in R15 |
| "Why multiply?", "Why least squares?" (slope-5 comparison line, SSE 400 > 360), "Back to $r^2$" ($1 - 360/1{,}000$) | Theory | Motivation paragraphs after the Try-it answers |
| H3 "Coefficient of determination $r^2$" | Theory, after Correlation | Try it + See it + Say it; no new callout (the $r^2$ definition stays in the correlation callout, which its decoder covers) |
| Notation decoders × 5 | After each formula callout | Covariance, correlation, regression line, bounds on $r$, line through $(\bar{x},\bar{y})$ |
| Exercise 4 (by hand) — Formula to words | Exercises | New |
| Exercise 5 (by hand) — Words to formula | Exercises | New |
| Exit check (5 questions + answers) | After Common mistakes | New |
| Homework intro, Step 0 + expected results | Homework | New; Step 0 uses `COVARIANCE.S`, `CORREL`, `RSQ`, `SLOPE`, `INTERCEPT` (+ `AVERAGE`, `VAR.S`); flags the `COVARIANCE.P` (32) and reversed-`SLOPE` (0.16) traps |
| Glossary rows | `glossary.qmd` | Proposed in `drafts/m9-glossary.md` |

## Module 10

Checked with `check_modules_v2.py --needs-debrief --synthesis` (Synthesis
module exception, contract v2): OK, time plan 180 min, no warnings
(2026-10-17). `git diff | grep '^-'`: every deleted line reappears as a
`+` line except the six listed under "Lines not reappearing verbatim".

| Old block (feature 010) | New location | Change | Verified |
|---|---|---|---|
| Intro "business question" (full toolkit, walkthrough, mock exam) | Intro | Unchanged (synthesis: no hook) | ✓ |
| Learning objectives (3 bullets) | Learning objectives (4 bullets) | 3 bullets verbatim; 1 notation bullet added (read formulas aloud, name the module) | ✓ |
| Time plan (Theory 30 / Excel lab 30 / Exercises 120) | Time plan | `Homework debrief` 10 added as first row; `Theory` 30 and `Exercises` 120 (90-min mock exam + 30-min debrief) rows verbatim; `Excel lab` 30 removed and its minutes reallocated to `Homework debrief` 10 + `Notation recap` 10 + `Exit check` 10; total 180, three columns; one sentence pointing to the homework added | ✓ |
| Theory › Complete walkthrough — Lakeside Bakery (Steps 1–6) | Theory › Complete walkthrough — Lakeside Bakery | Unchanged | ✓ |
| Theory › Common pitfalls checklist (warning, 14 items) | Theory › Common pitfalls checklist | Unchanged | ✓ |
| Worked example — Lakeside Bakery (summary table + paragraph) | Worked example — Lakeside Bakery (summary) | Unchanged (no value line deleted); values re-checked with NumPy/SciPy from `lakeside-bakery.csv` (exact $Q_3$ Riverside = 261.245) | ✓ |
| Excel lab "Replicate the walkthrough in Excel" (30 min, time-plan row only; no lab content on the v1 page) | Homework — Excel lab (intro, Step 0, Homework 1–2) | Turned into homework; the phrase "Replicate the walkthrough in Excel" reused in the homework intro and the time-plan note. Content is new (see below), built only on numbers already on the page or re-verified | ✓ |
| `## Using Excel` (2-line pointer to Excel functions page) | Homework — Excel lab › Using Excel | Moved, H2 → H3, text unchanged; step → function table added after it | ✓ |
| Proof / derivation (overall mean as weighted mean of groups) | Proof / derivation | Unchanged | ✓ |
| Visual intuition | Visual intuition | Unchanged | ✓ |
| Interactive demo (`TODO:` important callout) | Interactive demo | Unchanged | ✓ |
| Exercises intro line ("the exercises … are the mock exam below") | Exercises | Verbatim; one sentence added announcing Exercises 4–5 | ✓ |
| `## Mock exam — Modules 1–9` (own H2) + important callout | Exercises › `### Mock exam — Modules 1–9` | H2 → H3, text and callout unchanged. The checker's order test tolerates extra H2s, but an H2 here ends the `## Exercises` range and breaks the fixed contract order, so it is nested under the closest required section | ✓ |
| `### Part A — Multiple choice (1 point each)` | `#### Part A — …` | H3 → H4 (kept below the mock exam heading), text unchanged | ✓ |
| Q1. Variable type (Module 1) | Exercises › Mock exam › Part A | Unchanged | ✓ |
| Q2. Frequency table sum (Module 2) | idem | Unchanged | ✓ |
| Q3. Histogram with unequal class widths (M3) | idem | Unchanged | ✓ |
| Q4. Boxplot outliers (Module 5) | idem | Unchanged | ✓ |
| Q5. Mean vs median in skewed data (Module 4) | idem | Unchanged | ✓ |
| Q6. Coefficient of variation (Module 6) | idem | Unchanged | ✓ |
| Q7. Skewness formulas (Module 7) | idem | Unchanged | ✓ |
| Q8. Conditional distribution (Module 8) | idem | Unchanged | ✓ |
| Q9. Correlation interpretation (Module 9) | idem | Unchanged | ✓ |
| Q10. Regression prediction (Module 9) | idem | Unchanged | ✓ |
| `### Part B — Computational exercises (6 points each)` | `#### Part B — …` | H3 → H4, text unchanged | ✓ |
| Exercise 1 — Full univariate summary (Modules 3–7) | Exercises › Mock exam › Part B | Unchanged; not renumbered and not tagged `(by hand)` or `(Excel)`: it is part of the in-class mock exam (T038: mock exam stays in class, verbatim) | ✓ |
| Exercise 2 — Bivariate analysis (Modules 8–9) | idem | Same as above | ✓ |
| Exercise 3 — Lakeside Bakery walkthrough (Modules 1–9) | idem | Same as above | ✓ |
| `## What comes next` (between Exercises and Common mistakes) | `## What comes next`, last section (after Further reading) | Moved, verbatim; an extra H2 inside the fixed order would cut the `## Exercises` range and break the contract order | ✓ |
| Common mistakes (Watch out, 14 items) | Common mistakes | Unchanged | ✓ |
| Further reading (2 OpenStax + 2 Khan Academy + licence note) | Further reading | Unchanged | ✓ |

No v1 exercise carried an `(Excel)` tag, so no exercise was moved into
the homework; no by-hand exercise existed, so none was renumbered.

### Lines not reappearing verbatim

| Deleted line | Reason |
|---|---|
| `date-modified: 2026-10-11` | Bumped to 2026-10-17 |
| `\| Excel lab \| 30 \| Replicate the walkthrough in Excel \|` | Mandated removal (no `Excel lab` row); converted to homework |
| `## Using Excel` | Mandated H2 → H3 under the homework |
| `## Mock exam — Modules 1–9` | H2 → H3 under `## Exercises` |
| `### Part A — …`, `### Part B — …` | H3 → H4 under the mock exam |

### New blocks in Module 10

| New block | Location | Notes |
|---|---|---|
| Learning objective "read the key formulas aloud …" | Learning objectives | 4th bullet |
| `Homework debrief` 10, `Notation recap` 10, `Exit check` 10 rows | Time plan | Replace the 30-min Excel lab |
| Notation recap (table: mean, IQR, $s^2$, $s$, $CV$, skewness, covariance, $r$, slope/intercept, each read aloud + link to module-04 … module-09) | Theory, last subsection | No `.callout-tip` remains on the page, so the "link to the decoder of origin" rule is met through this table |
| Review exercises (by hand): Exercise 4 — Formula to words; Exercise 5 — Words to formula | Exercises, after the mock exam | Numbered after mock exam Exercises 1–3 to avoid two "Exercise 1"s; Riverside $CV$ 83.48/205.69 = 40.6% and $a = 400 - 10\times20 = 200$, $\hat{y}(25) = 450$ checked with Python |
| Exit check (5 questions + answers) | After Common mistakes | Covariance read aloud, ordinal centre, $r$/$r^2$ ($0.087^2 = 0.0076$), why $n-1$, range vs IQR (472.24 − 66.93 = 405.31); no Excel question |
| Homework intro (objective, estimated time 50–60 min, where, follow-up = self-check + final-exam review if any) | Homework — Excel lab | New |
| Step → Excel function table | Homework › Using Excel | After the moved v1 text; functions all listed on `excel-functions.qmd` |
| Step 0 — check your class results + expected results (Riverside column of the summary table, outliers 431.34 / 472.24, intercept 243.51) | Homework | Numbers already on the page (summary table, Exercise 3 solution); note on $Q_3$ = 261.245 |
| Homework 1 (Excel) — Walkthrough for the Hilltop outlet | Homework | Replicates walkthrough Steps 2–6; verified with NumPy/SciPy: weather 30/23/7, satisfaction 18/29/13, five-number summary 69.91/151.62/195.16/265.92/417.35, IQR 114.31, fences −19.85/437.39, grouped Mo 172.73, $s$ 81.96, CV 37.8%, skew 0.60, below-€150 shares 71.4/30.4/6.7%, $r$ 0.125, $r^2$ 0.016, slope 2.38, intercept 166.02 |
| Homework 2 (Excel) — Overall mean as a weighted mean | Homework | Applies the derivation to Lakeside: overall mean 211.30 = 0.5 × 205.69 + 0.5 × 216.91 (verified: 211.2966) |

## Demo conversions — Modules 3, 5, 9 (2026-10-13)

The Shinylive demos of Modules 3, 5 and 9 showed raw Python on the live
site (no Shinylive filter active for `modules/`). At the owner's request
they were re-implemented in OJS, using only the built-in `html` template
and SVG (no Plot, Inputs or d3, which the runtime fetches from a CDN).
Features, data and starting values are unchanged (T-I); no other part
of these pages was touched.

| Module | Demo | Kept | Check |
|---|---|---|---|
| 3 | Histogram builder | 3 datasets (Harbour 30 / 120, Campus 120, same 240 values), bin-width slider 25–400 step 25, class count, Sturges suggestion | Class counts identical to NumPy for Harbour 30 @100, Harbour 120 @100, Campus 120 @250 |
| 5 | Boxplot from the five-number summary | 5 sliders (300–900), same verified start values, auto-sorted, IQR, fences, outlier flag | Same formulas as the Python app |
| 9 | Scatter plot and correlation | 8 sampled days, day picker, temperature and revenue sliders, r, r², regression line; the selected point is now circled | r = 0.769, b = 54.90, a = −528.43, identical to NumPy |

The v1 checker (`specs/010-.../check_modules.py`) now accepts an `{ojs}`
demo as well as a Shinylive one (Constitution T-IV allows both).

## Classroom notes

*(to fill after teaching Module 6 — T045)*
