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
