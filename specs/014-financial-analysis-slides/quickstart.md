# Quickstart: Validate the Financial Analysis Slide Decks

## Prerequisites
- Quarto 1.10+ (`quarto --version`)
- The repo root as the working directory, on branch `014-financial-analysis-slides`
- Web access, used only during writing to verify facts (research.md Part B)

## 1. Smoke render (after scaffolding)

```sh
quarto render fr/teaching/financial-analysis/slides/jour-1.qmd --quiet
quarto render teaching/financial-analysis/slides/jour-1.qmd --quiet
```
Expected: both exit 0. `docs/fr/teaching/financial-analysis/slides/jour-1.html` is a RevealJS deck, not a plain HTML page.

## 2. Render all decks and stubs

```sh
for d in 1 2 3; do
  quarto render fr/teaching/financial-analysis/slides/jour-$d.qmd --quiet || echo "FAIL fr $d"
  quarto render teaching/financial-analysis/slides/jour-$d.qmd --quiet || echo "FAIL en $d"
done
```
Expected: no `FAIL` lines.

## 3. Static contract checks (contracts/slide-deck-format.md §9)

```sh
cd fr/teaching/financial-analysis/slides
grep -c 'callout-caution' jour-*.qmd          # each ≥ 1
grep -c 'callout-warning' jour-*.qmd          # each ≤ 1
grep -n 'TODO: à vérifier' jour-*.qmd         # no output
grep -nE '<iframe|<details|style=|date: today' jour-*.qmd   # no output
grep -c '{#exr-' jour-*.qmd                   # matches the exercise count in contracts/day-plans.md
```

## 4. Timing sums

For each deck, add up the minutes on the "Programme de la journée" table,
excluding rows marked "(optionnel)". Expected: **360** for each day.

## 5. Links

```sh
quarto render fr/teaching/financial-analysis/index.qmd --quiet
grep -o 'href="[^"#]*\.html' docs/fr/teaching/financial-analysis/slides/jour-*.html \
  | sed 's/.*href="//' | sort -u
```
Each relative target must exist under `docs/fr/teaching/financial-analysis/`.
The syllabus must list the three decks under **Diapositives**, and the French
sidebar must show them.

## 6. Visual check (projector and laptop)
Open each deck full screen at 1920×1080, then in a 1366×768 window. Check that:
- Tables (cote d'activité, cote de crédit, consolidation methods, liquidity matrix) are readable without scrolling, or use `.scrollable` deliberately.
- Mermaid charts render (cote distribution, ROE vs ROCE, organigramme, six-step flowchart).
- Every slide with a year-dependent figure shows its source line.
- Press `S`: the speaker notes show durations and answer-key file names and contain no solutions.

## 7. Content audits (spec SC-002, SC-003)
- `specs/014-financial-analysis-slides/coverage-map.md` has 102 original-slide rows and one row per folder file, all with a destination or reason.
- Every verified-fact row has status `verified` or `fallback`. None are `todo`.
- Spot-check 10 figures against their cited sources.

## 8. Dry run (SC-001)
The instructor rehearses each day with only the deck and the answer-key
documents named in the notes. Expected: each day lands within ±15 min of 6 h.
