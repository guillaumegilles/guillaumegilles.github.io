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

### Other files changed in phase A

| File | Change |
|---|---|
| `module-07.qmd` | `Homework debrief` 10 min added; Excel lab 50 → 40 (T022) |
| `index.qmd` | One rollout-safe sentence on the Module 6 pilot (T023) |
| `fr/teaching/data-description/modules/*.qmd` (13) | French stubs (FR-021, T042) |
| `fr/teaching/data-description/index.qmd` | Link to the English version added |
| `_quarto.yml` | `fr-data-description` sidebar block (T043) |
| `specs/010-.../check_modules.py` | Time plan sums all rows (T004) |

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
