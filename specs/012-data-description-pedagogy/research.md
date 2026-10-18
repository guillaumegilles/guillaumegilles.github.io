# Research: Concrete-to-Abstract Pedagogy — Data Description

**Feature**: `012-data-description-pedagogy` | **Date**: 2026-10-13 |
**Spec**: [spec.md](./spec.md)

Each entry: **Decision** · **Rationale** · **Alternatives considered**.

## R1. In-class micro-cycle per concept

**Decision**: Every core concept follows the same five-step micro-cycle
inside `## Theory`:

1. **Try it** — a hand-computable task on a mini-dataset (≤ 6 values).
2. **See it** — a picture of the same numbers (dot plot, number line or
   table when no picture fits).
3. **Say it** — one plain-language sentence naming the idea.
4. **Write it** — the formal definition/formula callout, immediately
   followed by a **notation decoder** linking every symbol to a number
   from step 1.
5. **Use it** — the full-dataset worked example (in `## Worked example`)
   and by-hand exercises.

**Rationale**: This is the concrete–pictorial–abstract (CPA) progression
(Bruner's enactive → iconic → symbolic modes, widely used in
Singapore-style mathematics teaching), combined with the "concept before
symbol" principle: a symbol is easier to learn when it names something
the student has already manipulated. The current pages do the reverse
(formula → paraphrase → numbers). Keeping the formal callout in step 4
means the definitions/formulas that the course relies on are unchanged
(T-I), only re-sequenced.

**Alternatives considered**:
- *Flipped classroom (theory as pre-reading)* — rejected: the problem
  to solve is notation comprehension, which students struggle with
  alone; moving theory out of class would aggravate it.
- *Adding the mean absolute deviation as a stepping stone to variance* —
  rejected: introduces a statistic outside the syllabus (T-III). The
  "deviations sum to zero → remove the signs by squaring" discovery
  gives the same motivation without a new indicator.

## R2. Module 6 mini-datasets

**Decision**: Two fictional Wandering Fork trucks, 5 days each, **same
mean €620**, values verified with NumPy (`ddof=1`):

| | Values (€) | Range | Deviations $x_i-\bar{x}$ | $\sum(x_i-\bar{x})^2$ | $s^2$ | $s$ | $CV$ |
|---|---|---:|---|---:|---:|---:|---:|
| Truck A "Steady" | 590, 610, 630, 630, 640 | 50 | −30, −10, 10, 10, 20 | 1,600 | 400 | 20 | 3.23% |
| Truck B "Erratic" | 370, 470, 670, 720, 870 | 500 | −250, −150, 50, 100, 250 | 160,000 | 40,000 | 200 | 32.26% |

Shortcut-formula check (Truck A): $\sum x_i^2 = 1{,}923{,}600$,
$n\bar{x}^2 = 1{,}922{,}000$, difference $1{,}600$, $/4 = 400$ ✓ —
also shows why the shortcut subtracts two large, nearly equal numbers
(supports the existing rounding warning). Truck B: $\sum x_i^2 =
2{,}082{,}000$.

$n-1$ intuition: given Truck A's first four deviations
(−30, −10, 10, 10), the fifth is forced to be +20 — "only 4 of the 5
deviations are free".

**Rationale**: Whole-number deviations and perfect-square variances
(400, 40,000) keep the hand arithmetic under 5 minutes and make
$s = \sqrt{s^2}$ obvious. The two trucks differ by a factor of 10 in
spread with an identical mean, which is exactly the business hook in
FR-001. Truck B is asymmetric, so the table is not trivially symmetric.

**Alternatives considered**:
- *First 6 days of the real Harbour data* (as in the existing demo:
  460.48, 500.02, …) — rejected for the hand activity: decimal means and
  non-square variances. Real data stay in the worked example (spec edge
  case "labelled simplification").
- *Units in hundreds of euros* (5.9, 6.1, …) — rejected: adds a unit
  conversion step unrelated to the concept.

## R3. "See it" figure — OJS step-reveal (revised 2026-10-13)

**Decision**: An `{ojs}` block (`//| echo: false`) with Observable Plot
draws the two-truck figure with a **step selector**
(`Inputs.radio`, default step 1) that mirrors the columns of the
deviation table:

1. *Dots* — Truck A and Truck B as two rows on a shared € axis, dashed
   mean line at 620.
2. *Deviations* — a segment from each dot to the mean, labelled with
   $x_i-\bar{x}$ (−30, −10, …), coloured by sign; caption shows
   "sum = 0".
3. *Squares* — each deviation drawn as a square of side
   $|x_i-\bar{x}|$ (one facet per truck, same € scale on both axes),
   caption shows $\sum(x_i-\bar{x})^2$ = 1,600 vs 160,000.

The data are the R2 values hard-coded in the block; all sums are
computed in JavaScript and must equal R2. No `style=` in the block's
HTML output (use Plot options / existing classes only). Colours reuse
the Shinylive app palette (`steelblue` points, `darkorange` mean).

**Rationale**: The user allowed OJS where it makes more sense, and it
does here: the computation is pure arithmetic, which is the constitution
T-IV criterion for choosing OJS over Shinylive; OJS + Observable Plot is
already an established site pattern (`teaching/mathematical-fundamentals/`
modules 2–7); it loads near-instantly (no WebAssembly) and needs no
Jupyter execution or `_freeze/` entry. The step reveal turns "See it"
into a picture of each table column, and step 3 shows variance
literally as area — squared distance from the mean (T-VII).

**Alternatives considered**:
- *Frozen matplotlib `{python}` figure* (previous decision) — rejected:
  static only, and adds a `_freeze/` artefact for no interactive gain.
- *Re-using the Shinylive demo* — rejected: slow WebAssembly start and
  placed after the worked example; it stays as the "explore" demo.
- *Hand-drawn image* — rejected: not reproducible from the numbers.

**Check required**: confirm the rendered page makes no request to a
third-party CDN for OJS/Plot (Principle IV); if it does, follow the
same approach as the `mathematical-fundamentals` pages, which already
ship OJS + Plot.

## R4. Visual treatment of the new elements (Constitution V)

**Decision**: Map each new element to an existing callout semantic —
no new callout types or styles:

| Element | Treatment | Why it fits Constitution V |
|---|---|---|
| Try it (activity) | Visible prompt + table with blanks, followed by `.callout-caution collapse="true"` titled `#### Try it — check your answer` | `.callout-caution` = exercises with collapsible solutions |
| Notation decoder | `.callout-note` titled `#### Notation decoder — <formula>`: a table *Symbol · Read aloud · In our example* plus one "read the whole formula as a sentence" line | `.callout-note` = definitions / background |
| Exit check | `## Exit check` section: 3–5 numbered questions visible, one `.callout-caution collapse="true"` with all answers | exercises with solutions |
| Homework | `## Homework — Excel lab` section; Excel exercises keep `.callout-caution collapse="true"` | exercises with solutions |

**Rationale**: Satisfies FR-016 (consistent treatment) without touching
`assets/dark.scss`.

**Alternatives considered**: custom `.callout-decoder` class — rejected
(needs SCSS work and breaks the five-type semantics).

## R5. Module 6 time plan model

**Decision** (180 min, 0 min Excel):

| Block | Minutes | What you do |
|---|---:|---|
| Hook | 10 | Two trucks, same mean — which is riskier to run? |
| Concrete build | 45 | Range on both trucks, IQR recall, deviation table, sum-to-zero, square, average with $n-1$, square root |
| Notation | 25 | Notation decoders for $s^2$, $s$; formula ↔ words exercises; $\sum$ reading |
| Relative spread | 20 | $CV$ from "is €200 a lot?"; shortcut formula on Truck A |
| Worked example | 20 | Harbour 30-day values; interpretation; visual intuition and demo |
| Practice | 45 | By-hand exercises 1–3 plus notation exercises |
| Exit check | 10 | 3–5 concept/notation questions |
| Excel preview | 5 | Instructor shows `STDEV.S` reproducing the hand result; homework briefing |
| **Total** | **180** | |

Practice + concrete build + notation = 115 min, up from 75 min of theory
and 55 min of mixed (half Excel) exercises.

**Rationale**: SC-001 requires ≥ 45 min reallocated; the former 50-min
Excel lab is redistributed to concrete build, notation and practice.
The 5-min preview is a demonstration, not a lab (spec Assumptions).
The checker accepts any row labels; it only requires a total of 180 and
no row starting with `Excel lab`.

**Alternatives considered**: keep a short 15-min Excel lab — rejected
(contradicts FR-008 and SC-001).

## R6. Homework section structure and numbering

**Decision**: `## Homework — Excel lab` contains, in order: an intro
line (estimated time ≤ 60 min, where to do it, follow-up at the start of
the next module); `### Using Excel` (the former `## Using Excel` table,
unchanged); `### Step 0 — check your class results` (enter Trucks A and
B, confirm `VAR.S` = 400 and 40,000 — FR-010); then the former Excel
exercises renamed `#### Homework 1 (Excel) — …`, `Homework 2`, `Homework
3`, contents unchanged. In-class exercises are renumbered
`Exercise 1 … k (by hand)`.

**Rationale**: Separate numbering makes it obvious what is done in
class versus at home; titles keep the track tag the course already uses.
A fidelity table in the module's PR/commit (data-model §4) maps old to
new numbers (T-I).

**Alternatives considered**: separate homework page — rejected (spec
Assumption; avoids sidebar/navigation changes, Principle II).

## R7. Superseding the feature-010 module contract and checker

**Decision**: Write `contracts/module-page-contract-v2.md` (this
feature) and a new checker `specs/012-data-description-pedagogy/
check_modules_v2.py` for revised modules. Unrevised modules continue
to be checked by `specs/010-data-description-10-modules/
check_modules.py`. Each revised module is moved from the v1 to the v2
check list as it is released.

**Rationale**: The v1 contract requires `## Using Excel` at H2 and an
`Excel lab` row in the time plan, which revised modules intentionally
drop. Editing the v1 checker would break checks on modules not yet
revised during the rollout.

**Alternatives considered**: a flag in the v1 checker — rejected
(mixes two contracts in one feature's artefacts).

## R8. Homework debrief and Module 7 timing

**Decision**: The first homework debrief happens in Module 7 (Module
5's lab was done in class, so Module 6 needs none). Module 7 is the next
rollout target. If the full Module 7 revision is not ready before its
class, a minimal fallback edit adds a `Homework debrief | 10` row to
Module 7's time plan, taken from its Excel lab block.

**Rationale**: FR-019 must hold from the first homework onward,
regardless of the rollout pace.

## R9. Homework load vs personal-work budget

**Decision**: Each module's homework is capped at 60 min (SC-005).
Ten modules → ≤ 10 h of Excel homework within the 20-hour personal-work
budget, leaving ≥ 10 h for by-hand revision. Module 10's "replicate the
walkthrough in Excel" (30 min) becomes its homework.

**Rationale**: Matches the syllabus budget; the three existing Excel
exercises per module took ~50–55 min in class with instructor help, so
≤ 60 min alone with step-by-step solutions is realistic.

## R10. Glossary gaps

**Decision**: Add three rows to `modules/glossary.qmd`: $x_i$ (the
$i$-th observation, "x sub i") and $\sum_{i=1}^{n}$ (summation,
"capital sigma — add up for $i$ from 1 to $n$") with "Introduced in"
= **Module 4**, and $x_i-\bar{x}$ (deviation from the mean) with
"Introduced in" = **Module 6**. No other new symbol is introduced.

**Rationale**: The glossary lacks all three rows (T-V), but the Module 4
rows already use $x_i$ and $\sum$ in the mean formula, so their origin
is Module 4. Module 6 is where they are decoded explicitly. $\sum$ is
Greek and needs a pronunciation.

## R11. Syllabus wording

**Decision**: Edit `teaching/data-description/index.qmd` in three
places: the module-pattern paragraph (Excel lab → homework, concrete-
first theory), the Personal work section (Excel homework ≤ 60 min per
module, debriefed next class), and learning objectives 2, 3 and 5 keep
their Excel functions but say "by hand in class and in Excel at home".
Do this when the template is written (US3), not in the Module 6 pass,
so the syllabus never describes a structure most modules don't have
yet — but add one sentence now that stays true during the rollout:
"Module 6 pilots a new format in which the Excel lab is done as
homework; later modules switch to it as they are revised." This sentence
is replaced by the full wording in US3.

**Rationale**: Truthful syllabus at every point of the rollout; T-VIII
requirements (Recommended Literature, first sidebar entry) are
untouched.

## R12. Rendering safely

**Decision**: Render single files with
`PROFILE_README_RUNNING=1 quarto render <file> --quiet` (Quarto
1.10.19). The variable short-circuits `scripts/update-profile-readme.sh`
so iteration does not push to the GitHub profile repo. Modules are
published (no `draft: true` in `modules/`), so changes go live on the
next full render and push.

**Rationale**: Verified in `scripts/update-profile-readme.sh` (line 7).

## R13. Module 7 mini-datasets

**Decision**: Four fictional Wandering Fork trucks at four pitches,
labelled on the page as a simplified extract. All four have **mean €600
and $s = €60$**, so Module 6's tools cannot tell them apart (the hook).
Values verified with NumPy 1.26 (`ddof=1`, `np.percentile(...,
method="weibull")` = `QUARTILE.EXC`) and SciPy 1.17
(`scipy.stats.skew(x, bias=False)` = Excel `SKEW`):

| Truck | Values (€) | $n$ | $\bar{x}$ | $Me$ | $Mo$ | $s$ | $SKEW$ | $(\bar{x}-Mo)/s$ | $3(\bar{x}-Me)/s$ | $Q_1$ | $Q_3$ | $YK$ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Station (symmetric) | 510, 570, 600, 600, 630, 690 | 6 | 600 | 600 | 600 | 60 | 0 | 0 | 0 | 555 | 645 | 0 |
| Stadium (right-skewed) | 550, 550, 580, 630, 690 | 5 | 600 | 580 | 550 | 60 | +0.9606 | +0.8333 | +1.0000 | 550 | 660 | +0.4545 (50/110) |
| Market (left-skewed) | 510, 570, 620, 650, 650 | 5 | 600 | 620 | 650 | 60 | −0.9606 | −0.8333 | −1.0000 | 540 | 650 | −0.4545 |
| Park (symmetric, flat; kurtosis only) | 530, 550, 560, 640, 650, 670 | 6 | 600 | 600 | — | 60 | 0 | — | 0 | 545 | 655 | 0 |

Hand quantities used on the page:

- Deviations (€): Station −90, −30, 0, 0, 30, 90; Stadium −50, −50,
  −20, 30, 90; Market −90, −30, 20, 50, 50 (each sums to 0).
- Cubed deviations in tens of €: Stadium −125, −125, −8, 27, 729,
  sum **498**; Market −729, −27, 8, 125, 125, sum **−498**; Station
  −729, −27, 0, 0, 27, 729, sum **0**. With $s = 6$ (tens of €),
  $s^3 = 216$, $\sum z_i^3 = 498/216 = 2.3056$, factor
  $5/(4\times3) = 5/12$, $SKEW = 0.9606$ — identical to SciPy.
- Standardized deviations (Stadium): −0.83, −0.83, −0.33, 0.5, 1.5.
- Quartile positions: $n = 5$ → 1.5 and 4.5 (halfway); $n = 6$ →
  1.75 and 5.25 (Station: $510 + 0.75\times60 = 555$,
  $630 + 0.25\times60 = 645$).
- Box gaps: Stadium $Me-Q_1 = 30$, $Q_3-Me = 80$, whiskers 0 / 30;
  Market 80 / 30, whiskers 30 / 0; Station 45 / 45, whiskers 45 / 45.
- Kurtosis Try it: days within €30 of the mean — Station 4, Park 0;
  farthest day — Station 90, Park 70. Excel `KURT` (not shown on the
  page, kurtosis stays conceptual): Station +0.925, Park −2.705,
  consistent with "Station leans leptokurtic, Park platykurtic".
- Exercise 4(b): $(500-440)/120 = 0.5$. Exit check 4:
  $(36+20-48)/16 = 0.5$.

**How verified**: `.venv/bin/python` script (NumPy/SciPy) recomputing
every Try-it answer, decoder value, Step 0 expected result, new
exercise and exit-check answer — all OK within ±0.005 of the rounded
page values. The `{ojs}` figure's JavaScript was extracted from the
`.qmd` and run under `node` for all four steps: same means, medians,
modes, $s$, cube sums, `SKEW` (0.96 / −0.96 / 0.00), quartiles and $YK$
(0.45 / −0.45 / 0.00), no `NaN`/`undefined` in the SVG strings.

**Rationale**:

- *Same mean and same $s$* for all trucks makes the hook a direct
  continuation of Module 6 ("same mean, different days" → "same mean,
  same spread, different shapes"). Market is the mirror image of
  Stadium ($x \mapsto 1{,}200 - x$), so it has the same $s$ by
  construction and every shape statistic flips sign — the clearest
  possible demonstration that squares (variance) lose direction and
  cubes keep it.
- *Clear centre order*: Stadium $Mo\,550 < Me\,580 < \bar{x}\,600$;
  Market $\bar{x}\,600 < Me\,620 < Mo\,650$; Station all equal.
  Each skewed set has a unique repeated value, so `MODE.SNGL` and the
  Pearson mode form work.
- *Whole numbers everywhere*: mean 600, $s = 60$, deviations multiples
  of 10. Counting deviations in tens of € (legitimate because
  $(x_i-\bar{x})/s$ is unit-free) turns the cubes into small integers
  (−125 … 729), so the cubed-deviation table takes ≈ 3 minutes.
- *Fisher-Pearson hand load*: the Try it asks students to fill
  deviations, cube them (in tens) and sum them — enough to see the
  sign come from the single far day. The last two operations
  (÷ 216, × 5/12) are flagged "computed for you (calculator step)",
  because dividing 498 by 216 by hand adds time without adding
  understanding. The full value (0.96) is then given in the answer
  and reused in the decoder.
- *Yule-Kendall*: $n = 5$ puts both quartiles exactly halfway between
  two sorted values (positions 1.5 and 4.5), and both numerators are
  ±50 over the same IQR 110, so the sign reading is immediate.
  Station ($n = 6$) needs quarter positions, so its quartiles are
  given in the chart Try it rather than asked.
- *Station has $n = 6$*: a symmetric set with a single clear mode at
  the centre and an integer $s$ is impossible with $n = 5$ (the only
  pattern $m-a, m, m, m, m+a$ gives $s = a/\sqrt{2}$). With $n = 6$,
  deviations −9, −3, 0, 0, 3, 9 (tens) give $s^2 = 180/5 = 36$.
- *Park* exists only for the kurtosis Try it: same mean, $s$ and
  skewness (0) as Station, but no repeated value, no day within €30 of
  the mean and no far-out day — a flat, short-tailed shape, against
  Station's peak at 600 and tails at 510/690.
- *Pitches* (Station, Stadium, Market, Park) give a business story for
  each shape: match days spike the Stadium (right tail), a rainy
  market day drags the Market down (left tail).

**Alternatives considered**:

- *Three trucks with $n = 5$ each* — rejected: the symmetric one could
  not have both a clear central mode and a whole-number $s$ (see
  above); dropping the mode would break the "mean = median = mode"
  reading of symmetry.
- *All sets with $n = 6$* (e.g. Stadium-like deviations −5, −5, −3,
  −2, 6, 9 in tens, $s = 6$) — rejected: quartiles at positions 1.75
  and 5.25 add quarter interpolations and give $YK = 27/47$, which is
  not hand-friendly.
- *Right-skewed −5, −5, −2, 3, 9 with a different $s$ from the
  symmetric set* — rejected: loses the "same mean, same $s$" hook.
- *Full hand computation of $SKEW$ in euros* — rejected: cubes such as
  $90^3 = 729{,}000$ and $s^3 = 216{,}000$ push the Try it far beyond
  5 minutes; the tens-of-€ trick gives the same result.
- *Showing Excel `KURT` values for Station/Park* — rejected: the
  course treats kurtosis conceptually only (no formula, no Excel
  function); the values are recorded here as a consistency check only.
- *Real Harbour days* — rejected for the activities (decimal means,
  no repeated values); the real data stay in the unchanged worked
  example.

## R14. Module 8 mini-datasets

**Decision**: Three simplified Wandering Fork extracts, one per concept
group, all verified with NumPy (`.venv/bin/python`, assertions on every
number shown on the page):

1. **Ten-day log** (contingency-table Try it): ten days, each with
   `Weather` (Sunny / Rainy) and `Revenue level` (Low < €500, Medium
   €500 to < €700, High ≥ €700), to tally into a 2×3 table.

   | Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | Weather | Sunny | Sunny | Rainy | Sunny | Rainy | Sunny | Sunny | Rainy | Sunny | Rainy |
   | Level | High | Medium | Low | High | Medium | Low | High | Low | Medium | High |

   | | Low | Medium | High | Row total |
   |---|---:|---:|---:|---:|
   | Sunny | 1 | 2 | 3 | 6 |
   | Rainy | 2 | 1 | 1 | 4 |
   | Column total | 3 | 3 | 4 | 10 |

   Decoder values: $n_{13} = 3$ (Days 1, 4, 7), $n_{1\cdot} = 6$,
   $n_{\cdot 3} = 4$, $n = 10$.

2. **Fifty-day table** (hook, marginal and conditional Try its,
   Exercise 5, Step 0):

   | | Low | Medium | High | $n_{i\cdot}$ | $n_{i\cdot}/n$ |
   |---|---:|---:|---:|---:|---:|
   | Sunny | 3 | 9 | 18 | 30 | 60% |
   | Rainy | 12 | 6 | 2 | 20 | 40% |
   | $n_{\cdot j}$ | 15 | 15 | 20 | 50 | |
   | $n_{\cdot j}/n$ | 30% | 30% | 40% | | 100% |

   Row percentages $n_{ij}/n_{i\cdot}$: Sunny 10 / 30 / 60%, Rainy
   60 / 30 / 10%. Column percentages $n_{ij}/n_{\cdot j}$: Sunny
   20 / 60 / 90%, Rainy 80 / 40 / 10%. Key value used on the page:
   $n_{13}/n_{\cdot 3} = 18/20 = 90\%$.

3. **Five (x, y) pairs** (scatter-plot Try it and OJS figure):
   temperature $x$ (°C) and items sold $y$.

   | Day | 1 | 2 | 3 | 4 | 5 | Total | Mean |
   |---|---:|---:|---:|---:|---:|---:|---:|
   | $x$ (°C) | 12 | 16 | 21 | 24 | 27 | 100 | 20 |
   | $y$ (items) | 40 | 55 | 50 | 70 | 85 | 300 | 60 |

   Quadrants around the means: Days 1, 2 lower-left; Days 4, 5
   upper-right; Day 3 (21 °C, 50 items) lower-right, the one point
   against the trend. Pearson $r = 0.901$ (not shown on the page; it
   keeps the set usable as a Module 9 preview).

Other checks on the page: Exercise 4 (worked-example table)
$n_{3\cdot} = 5$, $n_{\cdot 1} = 6$, $n_{31}/n_{3\cdot} = 60\%$,
$n_{31}/n_{\cdot 1} = 50\%$; exit-check question 4: $12/20 = 60\%$,
$9/30 = 30\%$.

**How verified**: one NumPy script tallies the ten-day log, computes
both margins, the marginal, row and column percentages of the 50-day
table, the means, quadrant membership and $r$ of the five pairs, and
asserts every value printed on the page. The OJS figure computes the
means and quadrant lists in JavaScript from the data arrays; the same
code was run under `node` with a stub `html` tag (captions: "Means: 20
°C and 60 items. 4 of 5 points …; Day 3 (21 °C, 50 items) goes against
the trend"; no `NaN`/`undefined` in the SVG).

**Rationale**: The 50-day table is built so that the hook is a real
trap: Sunny has more Medium days than Rainy (9 vs 6) but **exactly the
same** Medium share (30% vs 30%), while the High shares differ sharply
(60% vs 10%). One table therefore shows both "raw counts mislead" and
"there is a real association". Row totals 30 and 20 and grand total 50
give whole-number percentages everywhere (marginal, row and column
conditionals). The rows mirror the
worked example (`weather` × revenue class), so the step to the
Harbour 30-day table is direct. The ten-day log is separate because
tallying 50 days by hand would exceed 5 minutes, and building a table
from individual records is the concrete meaning of $n_{ij}$. The five
pairs have whole-number means (20, 60), fit on a 10–30 × 30–90 grid,
and contain one counter-trend point so that "rises to the right, but
not a perfect line" is visible — the wording of the worked example and
Exercise 3.

**Alternatives considered**:
- *Franchise × weather* (Harbour/Campus rows) — rejected: real Campus
  and Harbour weather counts already appear in Homework 1 and 4; a
  fictional table with the same labels could be confused with them.
- *2×2 table (good day / bad day)* — rejected for the main table: it
  cannot show "same share in one column, different in another"; a 2×2
  is kept for exit-check question 4.
- *Tallying the 50-day table directly* — rejected: too long by hand.
- *Revenue in € for the scatter pairs* — rejected: three- and
  four-digit values are harder to plot on squared paper; items sold
  keep integers small.
- *Five pairs on a perfect line* — rejected: hides the "visible
  scatter around the trend" message and gives $r = 1$ in Module 9.

## R15. Module 9 mini-datasets

**Decision**: One fictional Wandering Fork truck, **5 days**, temperature
$x$ (°C) vs items sold $y$, labelled on the page as a simplified extract.
Values verified with NumPy (`ddof=1`) and SciPy (`linregress`):

| Day $i$ | $x_i$ | $y_i$ | $x_i-\bar{x}$ | $y_i-\bar{y}$ | product | $(x_i-\bar{x})^2$ | $(y_i-\bar{y})^2$ | $\hat{y}_i$ | $y_i-\hat{y}_i$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 23 | 96 | 1 | 16 | 16 | 1 | 256 | 84 | 12 |
| 2 | 17 | 54 | −5 | −26 | 130 | 25 | 676 | 60 | −6 |
| 3 | 25 | 80 | 3 | 0 | 0 | 9 | 0 | 92 | −12 |
| 4 | 21 | 82 | −1 | 2 | −2 | 1 | 4 | 76 | 6 |
| 5 | 24 | 88 | 2 | 8 | 16 | 4 | 64 | 88 | 0 |
| **Total** | **110** | **400** | **0** | **0** | **160** | **40** | **1,000** | **400** | **0** |

| Indicator | Value | Hand route |
|---|---:|---|
| $\bar{x}$, $\bar{y}$ | 22 °C, 80 items | $110/5$, $400/5$ |
| $\text{Cov}(X,Y)$ (`COVARIANCE.S`) | 40 °C·items | $160/4$ |
| `COVARIANCE.P` (Step 0 trap) | 32 | $160/5$ |
| $s_X^2$, $s_Y^2$ | 10, 250 | $40/4$, $1{,}000/4$ |
| $s_X\,s_Y$ | 50 | $\sqrt{10 \times 250} = \sqrt{2{,}500}$ (one root only) |
| $r$ (`CORREL`) | 0.8 | $40/50$ |
| $r^2$ (`RSQ`) | 0.64 | $0.8^2$; also $(1{,}000-360)/1{,}000$ |
| $b$ (`SLOPE`) | 4 items/°C | $40/10$ |
| $a$ (`INTERCEPT`) | −8 | $80 - 4 \times 22$ |
| $\sum(y_i-\hat{y}_i)^2$ | 360 | $144+36+144+36+0$ |
| Prediction at 20 °C | 72 | $-8 + 4 \times 20$ |
| Comparison line $\hat{y}=-30+5x$ (through $(\bar{x},\bar{y})$) | gaps 11, −1, −15, 7, −2; SSE 400 | shows 360 is the least |
| Cauchy–Schwarz check | $160^2 = 25{,}600 \le 40 \times 1{,}000 = 40{,}000$; ratio 0.64 | Bounds-on-$r$ Try it |
| `SLOPE` with X range first (Step 0 trap) | 0.16 | $40/250$ |
| Items halved (packs of 2) | Cov 20, $r$ 0.8 | unit-invariance of $r$ |

Formula ↔ words exercise / exit-check mini-set: $x = 1, 2, 3$,
$y = 2, 6, 4$ → products 2, 0, 0, $\text{Cov} = 1$, $s_X^2 = 1$,
$b = 1$, $a = 2$, $r = 0.5$ (not shown on the page).

**How verified**: `np.cov(x, y, ddof=1)` = 40, `ddof=0` = 32;
`np.corrcoef` = 0.8; `np.polyfit(x, y, 1)` = (4, −8);
`scipy.stats.linregress` slope 4, intercept −8, rvalue 0.8; residuals,
SSE (360, 400), Cauchy–Schwarz terms, halved-$y$ covariance and the
small exercise set checked with `np.testing.assert_allclose` in one
script (2026-10-17, all assertions passed). The OJS "See it" figure
recomputes the means, products, sum 160, Cov 40, $a$, $b$, $r$ and
$r^2$ from the two arrays; its captions were checked with `node`
against the same values.

**Rationale**:
- Integer means (22, 80) and integer deviations; every product is an
  integer and the total (160) is divisible by $n-1 = 4$.
- $r$ is a simple decimal (0.8) although $s_X = \sqrt{10}$ and
  $s_Y = \sqrt{250}$ are irrational: their **product** is
  $\sqrt{2{,}500} = 50$, so the Try it takes a single square root of a
  perfect square and stays on integers.
- $b = 4$ and $a = -8$ are integers; fitted values and residuals
  (12, −6, −12, 6, 0) are integers, so least squares and the
  "$r^2$ = explained share" reading ($1 - 360/1{,}000 = 0.64$) can be
  checked by hand.
- The data are not trivially symmetric: one day in a negative quadrant
  (day 4, product −2), one day on a mean line (day 3, product 0), and
  one dominant day (day 2, product 130), which makes the quadrant
  picture and the "vote" interpretation informative.
- The warmest day is not the busiest, so the hook question ("do hotter
  days really mean busier days?") is genuine, and $r = 0.8 < 1$.
- Temperatures 17–25 °C sit inside the real Harbour 30-day range
  (16.4–27.1 °C); items sold 54–96 are of the same order as the
  dataset's `items_sold` (mean 74.40).

**Alternatives considered**:
- *Integer $s_X$ and $s_Y$ individually* (e.g. deviations −8, −7, 3,
  5, 7 with $s_X = 7$, $s_Y = 8$, $r = 0.875$) — rejected: temperature
  spread of 15 °C over 5 days, a less simple $r$, $r^2 = 0.766$.
- *Symmetric temperatures 18, 20, 22, 24, 26* (deviations −4 … 4) —
  rejected: a too-regular pattern and no point on a mean line; the
  asymmetric set gives the same $\sum(x_i-\bar{x})^2 = 40$.
- *Real Harbour days* (as in the demo: 21.9 °C / €460.48 …) —
  rejected for the hand activity: decimal means and products. Real
  data stay in the worked example and the demo (spec edge case
  "labelled simplification").
- *Revenue in € instead of items sold* — rejected: three-digit
  deviations make the product column slow to compute; items sold keeps
  products below 150.
