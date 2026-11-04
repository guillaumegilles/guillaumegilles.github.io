# Quickstart: Validate the Fictitious Consolidated Accounts

Run from the repository root (`/home/guillaume/www`), on branch
`015-comptes-consolides-fictifs`. Formats: [contracts/dataset-files-contract.md](contracts/dataset-files-contract.md);
entities: [data-model.md](data-model.md); decisions: [research.md](research.md).

## Prerequisites

- Quarto installed; `source .venv/bin/activate` (openpyxl 3.1.5 present).
- Feature artifacts generated at least once (step 1).

## 1. Generate the dataset

```sh
source .venv/bin/activate
python scripts/financial-analysis/generate-dataset.py
```

Expected: exit 0; creates `fr/teaching/financial-analysis/donnees/fichiers/aubepine-consolide.xlsx`,
`aubepine-consolide.pdf`, and the markdown table fragments used by the
`donnees/*.qmd` pages, plus the corrigé figures.

## 2. Consistency gate (SC-001, FR-003)

```sh
python scripts/financial-analysis/generate-dataset.py --check
```

Expected: one PASS line per invariant (bilan équilibré ×3 exercices,
résultat tie, flux tie, identité de consolidation per poste), exit 0.
Deliberately break one figure in `dataset_params.*` → `--check` MUST exit 1
and name the broken invariant. Restore.

## 3. Determinism and variants (FR-009)

```sh
python scripts/financial-analysis/generate-dataset.py --check >/dev/null && \
  sha256sum fr/teaching/financial-analysis/donnees/fichiers/aubepine-consolide.xlsx
python scripts/financial-analysis/generate-dataset.py   # run again
sha256sum fr/teaching/financial-analysis/donnees/fichiers/aubepine-consolide.xlsx   # same hash
python scripts/financial-analysis/generate-dataset.py --seed ETU-001 --out /tmp/var1
python scripts/financial-analysis/generate-dataset.py --seed ETU-002 --out /tmp/var2
sha256sum /tmp/var1/*.xlsx /tmp/var2/*.xlsx   # different hashes, same structure
python scripts/financial-analysis/generate-dataset.py --seed ETU-001 --out /tmp/var1b
sha256sum /tmp/var1/*.xlsx /tmp/var1b/*.xlsx  # identical hashes (same seed)
```

Expected: base regeneration is byte-identical; the two seeds differ; the
same seed reproduces identically; each variant still passes `--check`.

## 4. Render both language trees (render gate)

```sh
quarto render fr/teaching/financial-analysis --quiet
quarto render teaching/financial-analysis --quiet
quarto render --quiet    # full-site gate before commit
```

Expected: exit 0 everywhere, no broken-link warnings. Download links to
`fichiers/*.xlsx` / `*.pdf` resolve in `docs/fr/teaching/financial-analysis/donnees/`.

## 5. Navigation and parity (FR-005, Principle II/VI, SC-002)

- In `_quarto.yml`, both `en-financial-analysis` and `fr-financial-analysis`
  contain the "Fil rouge" section with the 6 dataset pages; `index.qmd` is
  still the first entry of each course block.
- For every `fr/teaching/financial-analysis/donnees/*.qmd` there is a
  `teaching/financial-analysis/donnees/*.qmd` stub linking to the FR page.
- Dataset page reachable from the course page in ≤ 2 clicks (SC-002).

## 6. Content checks (FR-006, FR-008, SC-005)

```sh
# Disclaimer on every dataset page and file header
grep -l "Données fictives" fr/teaching/financial-analysis/donnees/*.qmd   # all 6 files
# Fil-rouge links present in the quest/exam pages
grep -l "donnees/index.qmd" fr/teaching/financial-analysis/modules/*.qmd fr/teaching/financial-analysis/exercices/*.qmd
# No hidden instructions / prompt injection in rendered pages (SC-005)
grep -rE "​|﻿|<!--" docs/fr/teaching/financial-analysis/donnees/ || echo "clean"
```

Expected: all greps succeed; the rendered `docs/` dataset pages contain no
HTML comments, no zero-width characters, and no hidden text. Manual
inspection: the AI-use note on `donnees/index.qmd` is visible plain prose.

## 7. Ratio coverage (SC-003)

Using only the downloaded Excel, compute for each of N-2, N-1, N the BdF
ratios taught in the course: rentabilité (CAF, marge, ROE/ROCE as applicable),
structure financière (taux d'endettement, autonomie), liquidité (FRNG, BFR,
trésorerie nette). Expected: every input present in the workbook, no gaps.

## 8. Teacher key (SC-004)

Recompute the published figures from `dataset_params.*` and diff against the
published tables and the corrigé. Expected: empty diff (100% match).
