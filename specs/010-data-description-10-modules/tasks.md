---

description: "Task list for the Data Description 10-module redesign"
---

# Tasks: Data Description — 10-Module Redesign

**Input**: Design documents from `/specs/010-data-description-10-modules/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md,
contracts/, quickstart.md

**Tests**: No test-first tasks (none requested). Verification is done by
two small scripts (`verify_dataset.py`, `check_modules.py`) and the
quickstart scenarios, which are tasks below.

**Organization**: Grouped by user story. Because this is a content
feature, "implementation" means authoring `.qmd` pages and data files.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no unfinished dependency)
- **[Story]**: US1–US5 from `spec.md`
- Paths are relative to the repository root `/home/guillaume/www`
- `SPEC=specs/010-data-description-10-modules`,
  `DD=teaching/data-description`, `MOD=teaching/data-description/modules`
  (shorthand used below; write full paths when editing)

## Standing rules for every authoring task

Every module task MUST follow `contracts/module-page-contract.md`:

- 12 sections in the fixed order; prose wrapped at 80 characters; no
  `style=` or `<style>`; `lang: en`; `date-modified` (no `date`).
- Time plan sums to 180 min (values in `data-model.md` §1).
- Statistics quoted come from `SPEC/dataset-statistics.md` (task T012),
  never typed by hand.
- Conventions: `QUARTILE.EXC`, `.S` variants by default, `SKEW`,
  kurtosis conceptual only.
- Khan Academy: unit-level links only, no embeds. OpenStax: section
  numbers exactly as in `research.md` §1.
- Where a demo is not required, add a `.callout-important` with a
  `TODO:` label.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Get the repository from a broken, half-migrated state to a
rendering skeleton.

- [ ] T001 Create `teaching/data-description/modules/_metadata.yml` containing `draft: true` (drafts render blank and leave navigation, search and sitemap; Quarto 1.4.537)
- [ ] T002 Rename `teaching/data-description/modules/module-01.qmd` to `module-02.qmd` with `git mv` (it holds old Session 3 content, the source for Module 2); do not edit its content yet
- [ ] T003 Rewrite the `id: data-description` sidebar block in `_quarto.yml` exactly as in `specs/010-data-description-10-modules/contracts/dataset-and-navigation-contract.md` §2 (syllabus, three parts with `module-01…10.qmd`, a Reference section with `dataset.qmd`, `glossary.qmd`, `excel-functions.qmd`); remove every `session-NN.qmd` entry and the root `glossary.qmd` entry
- [ ] T004 [P] Create directory `teaching/data-description/data/`
- [ ] T005 [P] Create `specs/010-data-description-10-modules/fidelity-record.md` as a table with columns `old_location | type | new_location | status | reason` (`status` ∈ migrated / adapted / dropped; `reason` required for adapted and dropped)
- [ ] T006 Run `quarto render teaching/data-description --quiet` and fix any error until it exits 0 (quickstart V1); dead links inside the old `index.qmd` outline may remain as warnings until T051

**Checkpoint**: Site renders again; sidebar matches the contract.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: The dataset, shared reference pages, and checking tools that
every module depends on.

**⚠️ CRITICAL**: No module authoring (Phase 3+) can start before T007–T016
are done, because every worked example quotes dataset statistics.

### Dataset

- [ ] T007 Write `specs/010-data-description-10-modules/generate_dataset.py` (seeded, uses `.venv` numpy/pandas/openpyxl) producing a 240-row long-format table with exactly these 16 columns, in this order: `franchise` (nominal: Harbour, Campus), `day` (discrete 1–120), `date` (2026-04-06 … 2026-08-03), `day_of_week` (nominal), `month` (ordinal Apr…Aug), `weather` (nominal: Sunny/Cloudy/Rainy), `temperature_c` (continuous °C), `event_nearby` (nominal Yes/No), `promo_active` (nominal Yes/No), `staff_on_duty` (discrete 2–5), `foot_traffic` (discrete), `customer_count` (discrete), `items_sold` (discrete), `daily_revenue_eur` (continuous €), `waste_kg` (continuous, right-skewed), `satisfaction_rating` (ordinal 1–5). For Harbour days 1–30 the eight original columns MUST be copied verbatim from `specs/005-data-description-course/wandering-fork-dataset.csv`. Campus: lower base revenue, strong weekday pattern, event days creating right-skewed revenue.
- [ ] T008 Write `specs/010-data-description-10-modules/verify_dataset.py` asserting the eight invariants from `data-model.md` §2 verbatim: (1) Harbour days 1–30 equal the legacy CSV exactly on the original columns; (2) no missing values, no duplicate `(franchise, day)`; (3) `items_sold ≥ customer_count`, `customer_count ≤ foot_traffic`, revenue > 0; (4) Campus revenue skewness > +0.5 and Harbour revenue skewness within ±0.5; (5) r(customers, revenue) ≥ 0.80 in both franchises and |r|(temperature, revenue) ≤ 0.35; (6) weather × promo row profiles differ by ≥ 15 percentage points in at least one franchise; (7) at least one 1.5×IQR outlier per franchise; (8) every category appears at least 5 times. Also assert the legacy figures (mean 628.34, s 137.09, Q1 506.60 using `QUARTILE.EXC`, Q3 729.99, median 643.63, IQR 223.39) on Harbour days 1–30.
- [ ] T009 Run T007 then T008; adjust only the seed and generator parameters until every invariant passes (never edit the Harbour original values); write `teaching/data-description/data/wandering-fork.csv` (UTF-8, comma, `.` decimal, ISO dates, LF) and `teaching/data-description/data/wandering-fork.xlsx` with sheets `data` (Excel Table named `tblFork`), `harbour_30d`, `campus_30d`, `dictionary`
- [ ] T010 [P] Generate `teaching/data-description/data/payroll-skew.csv` (10–20 rows: one executive plus staff salaries, invented, clearly right-skewed) for M4/M7
- [ ] T011 [P] Generate `teaching/data-description/data/lakeside-bakery.csv` (a different business, 2 outlets × 60 days = 120 rows, same style of variables) for the M10 walkthrough; add its checks to `verify_dataset.py`
- [ ] T012 Extend `verify_dataset.py` to write `specs/010-data-description-10-modules/dataset-statistics.md`: for each franchise and for both the 120-day and 30-day subsets, recompute mean, median, mode/modal class, min, max, range, `VAR.S`, `STDEV.S`, CV, `QUARTILE.EXC` Q1–Q3, IQR, fences, `SKEW`, Pearson median skewness, covariance, r, slope, intercept, R², frequency tables for weather and satisfaction, and a weather × promo contingency table. This file is the single source for every number quoted in modules
- [ ] T013 Create `teaching/data-description/modules/dataset.qmd`: download links to the four data files, a 16-row data dictionary (name, statistical type, unit, meaning), the designed properties from `data-model.md` §2, the dictionaries for the two secondary datasets, and a short "how the data were invented" note (all data are invented)

### Shared reference pages and tools

- [ ] T014 [P] Create `teaching/data-description/modules/excel-functions.qmd` converted from `teaching/data-description/modules/Excel_functions_English_French.txt` (keep every existing pair) and add the functions the course now needs with their French names: `QUARTILE.EXC`, `PERCENTILE.EXC`, `STDEV.S`, `STDEV.P`, `VAR.S`, `VAR.P`, `SKEW`, `COVARIANCE.P`, `COVARIANCE.S`, `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`, `SUMSQ`, `SUMPRODUCT`, `COUNTIFS`; add a note on French-locale Excel and flag any French name not confirmed against Excel
- [ ] T015 [P] Update `teaching/data-description/modules/glossary.qmd`: change the intro and the "Introduced in" column wording from "Session N" to "Module N", add a conventions table (quartiles `QUARTILE.EXC` with position `(n+1)p`; sample `.S` by default; `SKEW` for skewness; kurtosis conceptual only); leave existing entries in place for T033
- [ ] T016 Write `specs/010-data-description-10-modules/check_modules.py` implementing quickstart V4 against `contracts/module-page-contract.md`: headings present and in order, time plan sums to 180 min, at least one `.callout-caution` with `collapse="true"`, further-reading table has an OpenStax row and a Khan Academy row, a `shinylive-python` block or a `TODO:` callout is present, no `style=` or `<style>`, lines wrap at 80 characters outside code blocks and URLs; accept a list of files; also print the course total minutes

**Checkpoint**: Dataset verified, reference pages exist, checkers run.
Module authoring can start.

---

## Phase 3: User Story 1 — Student completes one module end to end (Priority: P1) 🎯 MVP

**Goal**: One complete, contract-conformant module. Module 3 is the
pilot: it needs the most machinery (class tables, required demo,
derivation, unequal-width trap) and an existing source (old Session 4).

**Independent Test**: A student with the prerequisites reaches every
Module 3 objective using only that page, the dataset, and the linked
resources, in about 180 minutes (spec US1).

- [ ] T017 [US1] Author `teaching/data-description/modules/module-03.qmd` ("Module 3 — Organising quantitative data: histograms and cumulative curves") from `modules/session-04.qmd`, following the page contract: business question (how is daily revenue distributed?), objectives, time plan **70 / 60 / 50**, theory (why raw continuous data must be grouped, class width and number of classes with Sturges' rule $k\approx 1+3.3\log_{10}n$, half-open convention $[L_i, L_i+h[$, $n_i$, $f_i$, $N_i^{+}$, $F_i^{+}$, histogram, frequency polygon, cumulative curve, reading a percentile from the ogive), worked example on the Harbour 30-day revenue from `dataset-statistics.md`
- [ ] T018 [US1] In `module-03.qmd`, write the "Using Excel" section (English-locale `COUNTIFS` range counts, relative and running cumulative columns, Histogram chart, PivotTable numeric grouping into bins, cumulative line chart) with a link to `excel-functions.qmd`, plus the "Visual intuition" (histogram area = share of observations) and "Common mistakes" sections (unequal-width heights must be density $n_i/h_i$)
- [ ] T019 [US1] In `module-03.qmd`, migrate the Shinylive bin-width histogram from `session-04.qmd` as the required demo (FR-030); embed the data so the values match `wandering-fork.csv`; verify the demo loads and responds in a browser (`quarto preview`)
- [ ] T020 [US1] In `module-03.qmd`, write the collapsible derivation "the cumulative curve must reach 100%" and the exercises, each in `.callout-caution collapse="true"` with solutions from `dataset-statistics.md`: by-hand (unequal-width class → density height, from old Exercise 2), by-hand (read the ogive, old Exercise 1), and an Excel exercise (build the class table for Campus with `COUNTIFS` and compare its shape with Harbour)
- [ ] T021 [US1] In `module-03.qmd`, write "Further reading": OpenStax IBS 2e §2.1 *Display Data* (histograms, frequency polygons, time series) and the Khan Academy unit *Displaying and comparing quantitative data* (unit-level link, lesson named in plain text, approximate duration, `verified_on` left blank for T048)
- [ ] T022 [US1] Add M3 symbols to `modules/glossary.qmd` ($k$, $h$, $n_i$, $f_i$, $N_i^{+}$, $F_i^{+}$, density, class midpoint) with notation, plain definition and "Introduced in Module 3"; add the `session-04.qmd` rows (theory blocks, both worked-example steps, three exercises, demo, derivation) to `specs/010-data-description-10-modules/fidelity-record.md`
- [ ] T023 [US1] Run `python specs/010-data-description-10-modules/check_modules.py teaching/data-description/modules/module-03.qmd`, then render it visible (`quarto render teaching/data-description/modules/module-03.qmd -M draft:false`, or `quarto preview`) and fix every failure; confirm math, callouts and collapsible solutions display
- [ ] T024 [US1] Pilot checkpoint: time-box a read-through of `module-03.qmd` against the 70/60/50 plan; record any needed change to `contracts/module-page-contract.md` or the time budget in `research.md` §5 **before** starting Phase 4, so the template is fixed once

**Checkpoint**: One module meets the contract and its demo works — MVP.

---

## Phase 4: User Story 2 — Student follows the whole course on one running case (Priority: P2)

**Goal**: Modules 1, 2 and 4–9 authored on the shared dataset so results
reuse earlier modules, with franchise comparisons in the bivariate
modules.

**Independent Test**: Starting from the dataset alone, every number in
any module recomputes, and later modules' numbers agree with earlier
ones (spec US2).

Modules touch different files and can be authored in parallel. Each
task includes: business question, objectives, time plan, theory,
worked example, Excel section, collapsible derivation, visual
intuition, demo or `TODO:` callout, by-hand **and** Excel exercises with
collapsible solutions, common mistakes, further reading.

- [ ] T025 [P] [US2] Author `modules/module-01.qmd` — **new content**: "What is statistics? Data types and measurement". Time **75 / 45 / 60**. Cover descriptive vs inferential statistics, population vs sample, census vs survey, observation vs experiment, qualitative nominal/ordinal vs quantitative discrete/continuous, levels of measurement (nominal, ordinal, interval, ratio) and what arithmetic each allows, an introduction to the Wandering Fork dataset (grain = one franchise-day, 16 columns), and a self-contained Excel first-steps path for beginners (open the CSV/Excel Table, cell references relative/absolute/mixed, `SUM`, `COUNT`, `COUNTA`, sort/filter, `IF`, English vs French locale note), reusing the content of `modules/excel-worksheet.qmd`. Derivation: relative frequencies sum to 1. Demo: `TODO:`. Further reading: OpenStax §1.1, §1.2, §1.3; Khan Academy *Study design*
- [ ] T026 [P] [US2] Author `modules/module-02.qmd` — "Organising qualitative data: frequency tables and charts". Time **60 / 60 / 60**. Source: the old Session 3 text already in this file (retitle, replace "Session" wording) plus the PivotTable-count and conditional-formatting parts of `modules/excel-worksheet-2.qmd`. Cover $n_i$, $f_i$, cumulative frequency for ordinal data, frequency tables for `weather` (nominal) and `satisfaction_rating` (ordinal), bar vs pie charts and their limits, mode as modal class; Excel: `COUNTIF`, `COUNTIFS`, PivotTable counts, bar/pie chart, conditional formatting. Derivation: percentages sum to 100% and the rounding caveat. Demo: `TODO:`. Further reading: OpenStax §2.1; Khan Academy *Analyzing categorical data* and *Displaying and comparing quantitative data*
- [ ] T027 [P] [US2] Author `modules/module-04.qmd` — "Measures of central tendency". Time **70 / 50 / 60**. Source: `modules/session-06.qmd`. Add the **weighted mean** $\bar{x}_w=\sum w_ix_i/\sum w_i$ (portfolio return, GPA) and the grouped-data mean (class midpoints); cover mean, median, mode and modal class, sensitivity to outliers, which measure to choose, using Harbour revenue and `payroll-skew.csv`; Excel: `AVERAGE`, `MEDIAN`, `MODE.SNGL`, `SUMPRODUCT`; add OpenStax §2.5 geometric mean as a short enrichment box on growth rates. Derivation: deviations from the mean sum to zero. Demo: `TODO:`. Further reading: OpenStax §2.3, §2.4 (note that OpenStax has no weighted-mean section); Khan Academy *Summarizing quantitative data*
- [ ] T028 [P] [US2] Author `modules/module-05.qmd` — "Measures of position: quartiles, percentiles, boxplot". Time **60 / 60 / 60**. Source: `modules/session-05.qmd`. Cover quartiles, percentiles, position $i=(k/100)(n+1)$ with interpolation (state that this equals `QUARTILE.EXC` and OpenStax §2.2), IQR, five-number summary, 1.5×IQR fences, boxplot construction and reading (authored here; OpenStax has none), side-by-side boxplots Harbour vs Campus and sunny vs rainy; Excel: `QUARTILE.EXC`, `PERCENTILE.EXC`, `MIN`, `MAX`, box-and-whisker chart. Required demo: migrate the Shinylive boxplot builder from `session-05.qmd` (FR-030) and verify it in a browser. Derivation: where the $(n+1)$ position formula comes from. Warn that `QUARTILE.INC` gives different values. Further reading: OpenStax §2.2; Khan Academy *Summarizing quantitative data*
- [ ] T029 [P] [US2] Author `modules/module-06.qmd` — "Measures of dispersion". Time **75 / 50 / 55**. Source: `modules/session-07.qmd`. Cover range, deviations, population vs sample variance and standard deviation (explain $n-1$ intuitively, no inference), grouped variance, coefficient of variation, Chebyshev and Empirical Rule, comparing the risk of Harbour vs Campus; Excel: `VAR.S`, `STDEV.S`, `VAR.P`, `STDEV.P`, `SUMSQ`, CV formula. Keep the existing dispersion Shinylive demo (optional). Derivation: variance shortcut $\overline{x^2}-\bar{x}^2$. Visual intuition: variance as mean squared distance (T-VII). Further reading: OpenStax §2.7; Khan Academy *Summarizing quantitative data*
- [ ] T030 [P] [US2] Author `modules/module-07.qmd` — "Shape of distributions and univariate review". Time **60 / 50 / 70**. Sources: `modules/session-08.qmd` and `modules/session-09.qmd`. Cover symmetric, right- and left-skewed shapes, the ordering of mean/median/mode, Excel `SKEW`, **Pearson median skewness** $3(\bar{x}-\text{Me})/s$, reading shape from histogram and boxplot using skewed Campus revenue and `payroll-skew.csv`; **kurtosis is conceptual only** (names and pictures; no formula, no Excel function; state this explicitly). End with a short univariate review on Harbour (frequency table → histogram → five-number summary → centre → spread → shape). Derivation: Pearson's coefficient is unit-free. Demo: `TODO:`. Further reading: OpenStax §2.6; Khan Academy *Modeling data distributions*
- [ ] T031 [P] [US2] Author `modules/module-08.qmd` — "Bivariate analysis I: contingency tables and scatter plots". Time **60 / 60 / 60**. Source: `modules/session-10.qmd` plus the two-field PivotTable part of `modules/excel-worksheet-2.qmd`. Cover joint, marginal and conditional frequencies, reading dependence from conditional profiles (weather × promo; **no formal independence tests**), scatter plots (direction, strength, form, outliers) for customers vs revenue and temperature vs revenue; Excel: 2-D `COUNTIFS`, two-field PivotTable, XY scatter, trendline. Exercises MUST compare Harbour and Campus on at least one relationship (FR-028). Derivation: marginals are sums of joints; conditional rows sum to 1. Demo: `TODO:`. Further reading: OpenStax §13.1 and §13.3 figures, §3.4 optional (probability framing, skim); Khan Academy *Analyzing categorical data* and *Exploring bivariate numerical data*
- [ ] T032 [P] [US2] Author `modules/module-09.qmd` — "Bivariate analysis II: covariance, correlation, regression". Time **70 / 55 / 55**. Source: `modules/session-11.qmd`. Cover covariance, Pearson $r$, correlation is not causation, least-squares line, interpreting slope and intercept in € per customer, $R^2=r^2$, interpolation vs extrapolation, reading a regression output table (Analysis ToolPak); Excel: `COVARIANCE.P`, `COVARIANCE.S`, `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`, Data Analysis → Regression. Required demo: migrate the scatter + regression-line Shinylive demo from `session-11.qmd` (FR-030) and verify it in a browser. Derivation: least-squares slope $b=\text{cov}/s_X^2$, intercept $a=\bar{y}-b\bar{x}$, and $R^2=r^2$. Exercises compare Harbour vs Campus. Keep inference out (skip OpenStax §13.2). Further reading: OpenStax §13.1, §13.3, §13.4, §13.6, §13.7; Khan Academy *Exploring bivariate numerical data*
- [ ] T033 [US2] Update `modules/glossary.qmd` with every new symbol and term from Modules 1, 2, 4–9 (weighted mean $\bar{x}_w$, $w_i$, quartile positions, IQR, fences, $\sigma^2$, $s^2$, CV, skewness, covariance, $r$, $R^2$, $a$, $b$, and the others introduced), each with notation, plain definition, Greek pronunciation where relevant, and "Introduced in Module N"; remove old "Session N" wording
- [ ] T034 [US2] Add rows to `specs/010-data-description-10-modules/fidelity-record.md` for the old `module-01.qmd` (Session 3), `excel-worksheet.qmd`, `excel-worksheet-2.qmd` and `session-05` … `session-11`: every theory block, worked example, exercise, demo and derivation, with status and a reason for any `adapted` or `dropped`
- [ ] T035 [US2] Run `check_modules.py` over `module-01.qmd`, `module-02.qmd`, `module-04.qmd` … `module-09.qmd` and fix every failure; run `quarto render` on each with `-M draft:false` and confirm no errors
- [ ] T036 [US2] Cross-module consistency pass: every figure reused across modules matches `dataset-statistics.md` (for example the M4 mean reappears in M6 and M7); every cross-reference link resolves to a module file that exists; Harbour-vs-Campus comparison exercises exist in M8 and M9; the `TODO:` demo callouts are listed in one place (a comment block at the end of `specs/010-data-description-10-modules/fidelity-record.md`)

**Checkpoint**: Modules 1–9 meet the contract; the running case is consistent.

---

## Phase 5: User Story 3 — Student prepares for exams with Module 10 (Priority: P2)

**Goal**: Module 10 gives a full descriptive-analysis walkthrough on a
fresh dataset and an original mock exam with solutions mapped back to
modules.

**Independent Test**: A student who missed a mock-exam question can
tell from its solution which module to revise (spec US3).

- [ ] T037 [US3] Author `modules/module-10.qmd` — "Synthesis, review and mock exam". Time plan **30 / 30 / 120** (exercises = 90-min mock exam + 30-min debrief; FR-004). Source: `modules/session-12.qmd`, rebuilt on `data/lakeside-bakery.csv`. Write a start-to-finish walkthrough: variable typing, frequency tables and charts, five-number summary and boxplot, centre, spread, shape, then contingency table, scatter, correlation, regression. Write the common-pitfalls list with at least: unequal-width histogram heights, $n$ vs $n-1$, correlation vs causation, $r$ vs $R^2$ (plus `QUARTILE.INC` vs `.EXC`). Add the collapsible derivation "the overall mean is the weighted mean of the franchise means". Signpost time series and index numbers as "next course". Demo: `TODO:`. Excel table links `excel-functions.qmd`
- [ ] T038 [US3] In `module-10.qmd`, write the original mock exam in the format of the real exams: MCQ block plus short-answer problems on the Wandering Fork (Harbour/Campus) data, sized for 90 minutes (target about 20 MCQ and 3 short-answer problems; adjust after the pilot). No question reproduced from the source archives in `ressources/` (feature 005 rule)
- [ ] T039 [US3] In `module-10.qmd`, write worked solutions in collapsible `.callout-caution` blocks; each solution ends with "Revise: Module N" and every module M1–M9 is referenced at least once; every number comes from `dataset-statistics.md`
- [ ] T040 [US3] Add `session-12.qmd` rows to `fidelity-record.md`; add M10 symbols to `glossary.qmd`; add the M10 further-reading table (OpenStax Chapter Reviews 2 and 13; Khan Academy unit practice); run `check_modules.py` and `quarto render -M draft:false` on `module-10.qmd` and fix failures

**Checkpoint**: All ten modules exist and conform to the contract.

---

## Phase 6: User Story 4 — Instructor migrates from 12 sessions to 10 modules safely (Priority: P3)

**Goal**: Old structure removed with nothing lost, no orphans, no dead
links, nothing published early.

**Independent Test**: Every canonical item in the old pages appears in
the fidelity record as migrated, adapted or dropped (with reason), and no
`session-*` page is reachable (spec US4).

- [ ] T041 [US4] Verify completeness of `specs/010-data-description-10-modules/fidelity-record.md`: list every `##` and callout heading in `modules/session-04…12.qmd`, `excel-worksheet.qmd`, `excel-worksheet-2.qmd` and the old Session 3 text, and confirm each has a row; add any missing row; every `adapted` or `dropped` row has a reason (SC-004)
- [ ] T042 [US4] Search the whole repository (`grep -rn "data-description" --include=*.qmd --include=*.yml --include=*.md .` excluding `docs/`, `_freeze/`, `specs/`) for links to old `session-NN` pages or the root `glossary.qmd` (for example in `teaching/decision-making-stat/` and course listings) and re-point them to the new module files or `modules/glossary.qmd`
- [ ] T043 [US4] Delete the migrated sources after T041 passes: `modules/session-04.qmd` … `session-12.qmd`, `modules/excel-worksheet.qmd`, `modules/excel-worksheet-2.qmd`, `modules/Excel_functions_English_French.txt` (FR-040)
- [ ] T044 [US4] Run quickstart V6 (`grep -rn "session-[0-9][0-9]" teaching/data-description _quarto.yml` returns nothing; no `session-*.qmd` or `excel-worksheet*.qmd` left) and V7 (with `draft: true`, modules render blank and are absent from sidebar and search index) and fix findings
- [ ] T045 [US4] Quickstart V9: from `index.qmd`, confirm each module, the dataset page, the glossary and the function page are reachable in at most two clicks; confirm the sidebar equals the contract exactly (FR-036)

**Checkpoint**: Migration complete and verified; course still hidden.

---

## Phase 7: User Story 5 — Student finds the right outside resource (Priority: P3)

**Goal**: Every further-reading entry is correct and verified.

**Independent Test**: From any module page a student reaches a matching
OpenStax section and a Khan Academy unit in one click each (spec US5).

- [ ] T046 [P] [US5] Verify every OpenStax citation in `modules/module-01…10.qmd` against the PDF table of contents (`pdftotext -f 1 -l 12 -layout teaching/data-description/introductory-business-statistics-2e_-_WEB.pdf -`): section number and title match; no module cites a non-existent section; record results in `specs/010-data-description-10-modules/research.md` §1 (quickstart V10)
- [ ] T047 [P] [US5] Audit all modules for Khan Academy references: only unit-level URLs unless the owner has verified a deeper link; no `<iframe>`, video embed or third-party script anywhere in `teaching/data-description/` (Constitution IV)
- [ ] T048 [US5] **Owner action (cannot be automated; the site is client-rendered)**: open each Khan Academy unit link used in the modules in a browser, fix any that moved, and write the check date in each module's further-reading table (`verified_on`, FR-043)
- [ ] T049 [P] [US5] Add OpenStax attribution (title, authors, publisher, licence) wherever OpenStax material is reused, and in the syllabus literature table (FR-044); confirm the licence text in the PDF front matter before wording it
- [ ] T050 [US5] Run `check_modules.py` over all ten modules and confirm each further-reading table has at least one OpenStax and one Khan Academy row (SC-007)

**Checkpoint**: All external references verified.

---

## Phase 8: Polish, Publish & Cross-Cutting Concerns

**Purpose**: Syllabus rewrite, release, final gates.

- [ ] T051 Rewrite `teaching/data-description/index.qmd` per `contracts/dataset-and-navigation-contract.md` §4: description and curriculum placement (follows MS01 and MS02; precedes MS04), learning objectives updated for 10 modules and Excel woven in, outline table linking `modules/module-01…10.qmd` with hours and parts, assessment table (midterm 35%/45 min covers M1–M5; final 65%/90 min covers M1–M10), personal work (20 h), conventions table, and **Recommended Literature** adding *Introductory Business Statistics, 2e* (OpenStax) and the Khan Academy Statistics and Probability course with author/provider, title, edition and publisher/source (T-VIII); keep the existing French-language references already listed
- [ ] T052 Remove `draft: true` from `teaching/data-description/modules/_metadata.yml` in the same change as T051 (publishing = one change; never set `index.qmd` to draft)
- [ ] T053 Run the full-site `quarto render` and confirm exit 0, the post-render hook runs, and the Shinylive demos in M3, M5 and M9 load in a browser (quickstart V1, V8)
- [ ] T054 Run quickstart V2–V5 and V9 end to end one last time and record the results at the end of `specs/010-data-description-10-modules/quickstart.md`
- [ ] T055 Stage the rendered `docs/` and any `_freeze/` changes together with the sources and ask the owner to approve the commit (Constitution: `docs/` and `_freeze/` committed in the same commit as sources; do not commit without explicit approval)
- [ ] T056 After publication, run quickstart V11 with a pilot group (time Module 2's Excel lab for a beginner, collect mock-exam scores after Module 9) and adjust the time plans if needed (SC-005, SC-006, SC-011)
- [ ] T057 Record the French-parity follow-up: create a short note listing the 14 pages that need translation (index, ten modules, dataset, glossary, functions) in `specs/010-data-description-10-modules/plan.md` under "Open items", so the deviation recorded in Complexity Tracking has a trackable next step (FR-038)

---

## Dependencies & Execution Order

### Phase dependencies

- **Setup (Phase 1)**: none; T004 and T005 are parallel, T006 closes the phase
- **Foundational (Phase 2)**: needs T001–T003 for the folder layout; BLOCKS all stories
  - T007 → T008 → T009 → T012 → T013 (dataset chain)
  - T010, T011, T014, T015 parallel with the chain; T016 independent
- **US1 (Phase 3)**: needs Phase 2; T017 → T018 → T019 → T020 → T021 (same file, sequential) → T022 → T023 → T024
- **US2 (Phase 4)**: needs **T024** so the template is frozen; T025–T032 are parallel (different files); T033–T036 follow all of them
- **US3 (Phase 5)**: needs US2 complete (the mock exam must reference all modules); T037 → T038 → T039 → T040 (same file)
- **US4 (Phase 6)**: needs US1–US3; T041 → T042 → T043 → T044 → T045 (T043 must not run before T041)
- **US5 (Phase 7)**: T046, T047, T049 can start once the relevant modules exist (even before US3 ends); T048 is the owner's manual step; T050 last
- **Polish (Phase 8)**: needs everything; T051 and T052 land in one change; T053 → T054 → T055

### User story dependencies

- **US1** has no dependency on other stories and is the MVP.
- **US2** reuses the template validated in US1.
- **US3** depends on US2 content (mock exam maps to M1–M9).
- **US4** depends on US1–US3 so the fidelity record is complete.
- **US5** verification can overlap with US2–US3 per module.

### Shared files (avoid parallel edits)

`modules/glossary.qmd`, `fidelity-record.md`, `_quarto.yml`: edit these
in the dedicated tasks (T015, T022, T033, T034, T040, T003) rather than
inside parallel module tasks.

---

## Parallel Example: User Story 2

```bash
# After T024, author these eight modules at the same time (disjoint files):
Task: "Author modules/module-01.qmd (new content)"                 # T025
Task: "Author modules/module-02.qmd (from old Session 3)"          # T026
Task: "Author modules/module-04.qmd (from session-06)"             # T027
Task: "Author modules/module-05.qmd (from session-05 + demo)"      # T028
Task: "Author modules/module-06.qmd (from session-07)"             # T029
Task: "Author modules/module-07.qmd (from session-08 + 09)"        # T030
Task: "Author modules/module-08.qmd (from session-10)"             # T031
Task: "Author modules/module-09.qmd (from session-11 + demo)"      # T032
```

Foundational parallel set:

```bash
Task: "Generate data/payroll-skew.csv"                              # T010
Task: "Generate data/lakeside-bakery.csv"                           # T011
Task: "Create modules/excel-functions.qmd"                          # T014
Task: "Update modules/glossary.qmd header and conventions"          # T015
```

---

## Implementation Strategy

### MVP first (User Story 1 only)

1. Phase 1 Setup → site renders (T006)
2. Phase 2 Foundational → dataset verified, shared pages, checkers
3. Phase 3 US1 → Module 3 meets the contract, demo works
4. **STOP and VALIDATE** (T023, T024): fix the template once

### Incremental delivery

1. Setup + Foundational → foundation ready
2. US1 (Module 3) → template validated (MVP)
3. US2 (Modules 1, 2, 4–9) → running case consistent
4. US3 (Module 10) → full course present
5. US4 → old structure removed safely
6. US5 → references verified
7. Polish → syllabus rewrite and publish in one change

Nothing is public until T051 and T052: the modules stay `draft: true`
and the live syllabus is only rewritten at the end.

### Parallel team strategy

After T024, up to eight authors can take one module each (T025–T032);
one person owns the glossary and fidelity tasks (T033, T034).

---

## Notes

- `[P]` means different files and no dependency on unfinished tasks.
- `[Story]` ties each task to a spec user story for traceability.
- Do not hand-type statistics; read them from `dataset-statistics.md`.
- Never edit the Harbour original-column values for days 1–30.
- Commit after each task or logical group, only with the owner's approval.
- French translation is a separate later feature (T057 records it).
