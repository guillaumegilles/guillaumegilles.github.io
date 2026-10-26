# Baseline and working log — 014 financial-analysis 3-day course

## Pre-change state (T002)

| Quest | File | Declared duration | XP |
|---|---|---|---:|
| Q1 | modules/01-temple-bilans.qmd | 1h30 (consignes) | 100 |
| Q2 | modules/02-archives-consolidees.qmd | 2h | 150 |
| Q3 | modules/03-detective-diagnostic.qmd | 2h | 200 |
| Q4 | modules/04-arenes-rentabilite.qmd | 2h | 150 |
| Q5 | modules/05-cartographes-modele-eco.qmd | 2h | 150 |
| Q6 | modules/06-conseil-sages.qmd | 2h30 | 200 |
| Q7 | modules/07-veilleurs-marche.qmd | 2h | 150 |
| Q8 | modules/08-architectes-strategie.qmd | 2h | 150 |
| Q9 | modules/09-gardiens-extra-financier.qmd | 3h | 250 |

XP total 1 500. Declared total 19 h (Day 1 5h30, Day 2 6h30, Day 3 7h).

Working-copy state before T006: French course sat at
`teaching/financial-analysis/` (uncommitted move from `fr/`); `HEAD` also
held an older English-root copy with `lessons/` (renamed `modules/`).
Root files not moved to the English mirror: all binaries (now under `fr/`).

## T006/T007 result

- Course moved with `mv` back to `fr/teaching/financial-analysis/`.
- Removed orphan `exercices/examen-1h.html` (generated) and empty `new/`,
  `old/`.
- English root recreated empty (`modules/`, `exercices/`).

## Literature editions to verify (T021)

(filled during T021)

## Concept-order findings (T026)

(filled during T026)

## Literature editions (T021)

All eight entries in `index.qmd` were "N/A"; now "édition à vérifier".
Not verified, not invented: Vernimmen/Quiry/Le Fur, Coulon, Brooks,
Helfer/Orsoni, Teyssier/Ducoulombier, Albouy, Lefebvre, Revue Banque.
Owner to supply editions.

## Deviations

- T015: the old `01-temple-bilans-enseignant.qmd` was kept in place and
  linked from `enseignant/jour-1.qmd` and the sidebar (no redirect page
  needed; URL unchanged).

## Concept-order findings (T026)

- Q3 (Day 1) uses ROE, SWOT, FPNR and liquidity before their dedicated
  pages/quests (Q4, Q5). Resolved: Q3's 25-min live theory segment covers
  ratio reading, RNR/FPNR, liquidity and SWOT, with pre-reading links to
  `performances`, `structure-fi`, `liquidite`, `formules`.
- No other concept found used before introduction (Q4 BFR/DuPont are in
  its own theory and `formules.qmd`; Q8 FTD is in its theory and
  `liquidite.qmd`; EV/EBITDA is introduced in Q6 before use).

## Data inconsistencies found in source pages (for owner review)

- Q1 Niveau 1/2 balance-sheet totals and net result mismatches (partly
  intentional "errors" exercise); Q2 STRATFIN passif 4 200 vs actif 4 700
  and PHOENIX/ORION net-result mismatch; Q6 BIOTECH ROCE 10 % vs ≈ 21 %;
  Q8 repayment capacity 5,3 vs 3,3 years; Q9 GREENTECH EV figures
  recalculated (5 882 / 5 376 k€). Illustrative numbers added by the
  rebalancing are labelled as such in the pages.

## T037 check

All numbers (≥ 4 digits) and company names present in the HEAD version of
each quest are still present in the edited version.
