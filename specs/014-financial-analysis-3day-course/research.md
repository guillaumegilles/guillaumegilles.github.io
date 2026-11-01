# Research: Financial Analysis — 3-Day Course

All "unknowns" below were resolved from the repository state and the
clarification session; no open NEEDS CLARIFICATION remains.

## R1 — Where does the course live? (language trees)

**Finding**: In `HEAD`, the course is at `fr/teaching/financial-analysis/`.
In the working copy those files are deleted and the same French content
(plus binaries) appears at `teaching/financial-analysis/` (the English
root). That root inherits `lang: en` from `teaching/_metadata.yml`, so
French prose would be tagged English, and the constitution (Principle VI)
requires French content under `fr/`.

**Decision**: Treat `fr/teaching/financial-analysis/` as the canonical
course. Move the current working-copy content back there (a rename, so
history is kept), and create English counterparts at
`teaching/financial-analysis/`.

**Rationale**: Matches the folder-per-language rule, fixes the HTML `lang`
attribute, and restores the layout that `HEAD`, the language switcher and
the other courses use.

**Alternatives considered**: Keep French at the root with a per-file
`lang: fr` override (allowed but breaks EN/FR mirroring and the switcher);
add a `teaching/financial-analysis/_metadata.yml` with `lang: fr` (same
mirroring problem).

**Owner confirmation (T001, 2026-10-26)**: confirmed, option A — move the
content back to `fr/` and mirror in English.

## R2 — Time budget (360 min per day)

**Finding**: Declared durations are Q1 1 h 30, Q2 2 h, Q3 2 h (Day 1 =
5 h 30), Q4 2 h, Q5 2 h, Q6 2 h 30 (Day 2 = 6 h 30), Q7 2 h, Q8 2 h,
Q9 3 h (Day 3 = 7 h). Total 19 h against a target of 18 h. Also, the
home page and nothing else carries a day kick-off or close-out.

**Decision**: Fixed targets (minutes, live teaching only; each quest block
includes its 20–30 min theory segment):

| Day | Block | Min | Change vs today |
|---|---|---:|---|
| 1 | Kick-off: game rules, teams, BdF 6-step overview | 15 | new |
| 1 | Q1 Temple des Bilans (theory 25 + escape game) | 110 | +20 |
| 1 | Q2 Archives Consolidées (theory 25) | 100 | −20 |
| 1 | Q3 Détective du Diagnostic + boss (theory 25) | 135 | +15 |
| 2 | Q4 Arènes de la Rentabilité (theory 25) | 120 | 0 |
| 2 | Q5 Cartographes du Modèle Éco (theory 20) | 105 | −15 |
| 2 | Q6 Conseil des Sages + boss (theory 25) | 135 | −15 |
| 3 | Q7 Veilleurs du Marché (theory 20) | 100 | −20 |
| 3 | Q8 Architectes de la Stratégie (theory 25) | 110 | −10 |
| 3 | Q9 Gardiens de l'Extra-Financier + boss (theory 30) | 140 | −40 |
| 3 | Closing: levels, badges, debrief | 10 | new |

Sums: Day 1 = 360, Day 2 = 360, Day 3 = 360, total 1 080 min.

**Cuts to make** (recorded per FR-007): Q9 Step 4 (WACC adjustment) and
the 1.5-page report become take-home extensions; Q7 reduces the six topic
briefs to a shared template with 4-minute pitches; Q6 Step 5 merges into
the boss presentation; Q2 trims one intragroup elimination case.

**Assumption**: 6 teams of 3–5 students (matches the six Q7 topics). Oral
slots are 5 min per team (Q7: 4 min), so a cohort larger than 6 teams
needs the "cut first" note of each block.

**Breaks** (not counted): two 15 min breaks and one 60 min lunch per day.

## R3 — XP and grade

**Finding**: Quest XP are 100, 150, 200, 150, 150, 200, 150, 150, 250 =
1 500 XP, which matches the "1 500 XP" note in Q9. Level thresholds are
< 400, > 400, > 800, > 1 200 (so the top level is reachable with 80 % XP).

**Decision**: `evaluation.qmd` is the single source: XP table, thresholds,
and grade rule `final = 0.4 × (XP / 1500 × 20) + 0.6 × exam`, marks on
/20. Exam = the 1 h exam (/50) or the 3 h 30 exam (/100), scaled to /20
(Q3: both outside the 18 h; the owner picks which one per cohort).
Thresholds stay as published. The commented-out badge tables in the
current index are restored or deleted deliberately and listed in the
change log.

## R4 — Live theory + pre-reading mapping (Q2)

| Quest | Pre-reading | Live theory (min) |
|---|---|---|
| Q1 | Three statements primer (to write; short) | 25 |
| Q2 | `banque-france.qmd` (step 2) | 25 |
| Q3 | `banque-france.qmd`, `performances`, `structure-fi`, `liquidite` | 25 |
| Q4 | `performances.qmd`, `formules.qmd` | 25 |
| Q5 | `banque-france.qmd` (step 1) | 20 |
| Q6 | `banque-france-cotation.qmd` | 25 |
| Q7 | none (research briefs) | 20 |
| Q8 | `liquidite.qmd` (prospective phase) | 25 |
| Q9 | `formules.qmd`, ESG primer | 30 |

Pre-reading load per night ≤ 45 min (stated on the home page, FR-008).

## R5 — Repetition and prerequisites between days

Day 2 requires one real annual report chosen on Day 1 and Day 3 requires
the same report plus a DPEF (as the current index says). Fallback when
unprepared: a 10-min catch-up using a provided example report (Schneider
Electric is already used as the worked example). Data source: companies'
public universal registration documents, found by the team; a fixed
fallback list is kept in the instructor guide so the exercise survives new
report editions (spec edge case; closes the low-impact "annual-report
source" gap).

## R6 — Publishing state to repair

- `_quarto.yml` sidebar block `inseec-finane` points to
  `teaching/inseec-finance/index.qmd`, which does not exist. Replace with
  an EN sidebar and a FR sidebar (index first, then planning, day sections,
  reference, glossary, evaluation, instructor section).
- `teaching/financial-analysis/exercices/examen-1h.html` is a generated
  orphan; delete (Principle I).
- Empty `new/` and `old/` folders and duplicate exam formats (`.odt`,
  `.pdf`, `.docx` of the same exam) are inventoried, not deleted.
- Language switcher must work: it depends on mirrored paths.

## R7 — Callout and exercise conformance

Existing pages use `.callout-note` for prerequisites and
`.callout-important` for preparatory work and boss banners. Convert to
plain headings/lists. Keep `.callout-note` for definitions,
`.callout-tip` for formulas (e.g. ROE = ROCE + (ROCE − i) × D/E),
`.callout-warning` for one common-mistakes block, `.callout-important`
only for `TODO:`. Exercises become `::: {#exr-…}` blocks with folded
`<details class="answer">` solutions; an instructor answer key stays in the
instructor guides.

## R8 — Change log mechanism (FR-007)

A "Journal des modifications" table in each instructor guide page (day):
block, previous duration, new duration, what was shortened or moved, where
it went (extension, homework, cut), and why. Cuts never remove theory,
worked examples or exercises; they move optional steps to take-home work.

## R9 — Derivations and demos (T-IV, T-VI)

| Quest | Derivation (`.callout-caution`) | Demo |
|---|---|---|
| Q1 | Why assets = liabilities + equity and net cash change = Δ cash on the balance sheet | TODO callout |
| Q2 | Elimination entries keep the consolidated balance sheet balanced | TODO callout |
| Q3 | Recurring net result ≈ ¾ × RCAI from the tax rate | TODO callout |
| Q4 | ROE = ROCE + (ROCE − i) × D/E, step by step | OJS leverage slider |
| Q5 | Link between margin on a canvas block and EBIT margin (short) | TODO callout |
| Q6 | EV/EBITDA to equity value bridge | TODO callout |
| Q7 | Effect of a lease capitalisation (IFRS 16) on EBITDA and debt | TODO callout |
| Q8 | FCF = EBITDA − tax − capex − ΔBFR identity | OJS 3-year projection |
| Q9 | Carbon-cost ESG adjustment of the discount rate (WACC) | TODO callout |

Demos are pure arithmetic, so OJS (not Shinylive) per T-IV. Remaining
TODOs are acceptable under T-IV and tracked in tasks.

## R10 — Glossary and syllabus

`glossaire.qmd` lists every acronym and symbol (ROCE, ROE, RNR, RCAI,
FPNR, FRNG, BFR, FTA, FTD, EV, EBITDA, WACC, DPEF, CSRD…) with
plain-language definitions; non-Greek so no pronunciation guide is needed.
The Recommended Literature table gets real editions where known; where the
edition cannot be verified it is flagged in the task list, not invented.

## R11 — "Instructor-only" separation

GitHub Pages has no access control; "separate" means separate pages in an
"Enseignant" sidebar section, not hidden content. The existing solutions
are already public in the repo; the spec does not require secrecy. If
secrecy matters, the owner must keep guides out of the site (decision for
the owner; default: published but separated).

## R12 — Translation scope

EN: full translation of `index.qmd` and `planning.qmd` (durations and block
order identical). Every other English page is a stub with
"Translation in progress" and a link to the French page (constitution
stub rule). Created by a short template so generation is mechanical.
