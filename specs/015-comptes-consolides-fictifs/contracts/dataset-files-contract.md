# Contract: Dataset Files, Pages, and Scripts

The feature exposes no HTTP API. Its interfaces are (1) the published files
students download, (2) the `.qmd` pages and their sidebar registration, and
(3) the two script CLIs the instructor runs. This contract fixes all three.

## 1. Downloadable files (`fr/teaching/financial-analysis/donnees/fichiers/`)

| File | Content |
|---|---|
| `aubepine-consolide.xlsx` | One workbook, sheets in this exact order: `Périmètre`, `Bilan`, `Compte de résultat`, `Annexe`, `Flux`. Bilan/CR/Flux have one column per exercice: `N-2`, `N-1`, `N`. All amounts in k€, integers. Header row 1 = sheet title, row 2 = column headers, data from row 3. |
| `aubepine-consolide.pdf` | Same content as the workbook, for reading/printing. |
| `aubepine-variante-<seed>.xlsx` | Generated per student with `--seed` (section 3); same sheet structure; only the documented variant postes differ from the base. |

Rules:

- Every file's first sheet/cell carries: "GROUPE AUBÉPINE — DONNÉES
  FICTIVES — USAGE PÉDAGOGIQUE UNIQUEMENT" (FR-006).
- Files sit next to the `.qmd` pages and are linked with relative paths;
  Quarto copies them to `docs/` automatically (R1). No hand-edited file in
  `docs/`.

## 2. Pages and navigation

FR pages (full content), all under `fr/teaching/financial-analysis/donnees/`:

| Page | Contents |
|---|---|
| `index.qmd` | Group presentation, périmètre table, disclaimer (plain prose), visible AI-use note (R8), OJS ratio demo or `TODO:` callout (T-IV), one `.callout-caution` derivation (T-VI) |
| `bilan-consolide.qmd` | Consolidated bilan N-2..N (generated table) |
| `compte-de-resultat.qmd` | Consolidated CR N-2..N |
| `annexe.qmd` | Principes, écarts d'acquisition, opérations intragroupe, intérêts minoritaires |
| `flux-tresorerie.qmd` | Tableau des flux N-2..N |
| `telechargements.qmd` | Links to the Excel/PDF (relative), variant notice |

EN counterparts under `teaching/financial-analysis/donnees/`: identical file
names, stub body (title + "Translation in progress" + link to the FR page),
no `lang:` override (inherited from directory `_metadata.yml`).

Sidebar: `_quarto.yml` gains a section in BOTH `en-financial-analysis` and
`fr-financial-analysis`, appended after the existing sections (index.qmd
stays first, T-VIII):

```yaml
- section: "Fil rouge — Groupe AUBÉPINE"   # EN: "Red thread — AUBÉPINE Group"
  contents:
    - fr/teaching/financial-analysis/donnees/index.qmd
    - fr/teaching/financial-analysis/donnees/bilan-consolide.qmd
    - fr/teaching/financial-analysis/donnees/compte-de-resultat.qmd
    - fr/teaching/financial-analysis/donnees/annexe.qmd
    - fr/teaching/financial-analysis/donnees/flux-tresorerie.qmd
    - fr/teaching/financial-analysis/donnees/telechargements.qmd
```

Teacher key: `fr/teaching/financial-analysis/enseignant/corrige-aubepine.qmd`,
added to the existing "Instructor" section of the FR sidebar.

Fil-rouge links (FR-008): `modules/02-archives-consolidees.qmd`,
`modules/03-detective-diagnostic.qmd`, `modules/performances.qmd`,
`modules/structure-fi.qmd`, `modules/liquidite.qmd`,
`exercices/examen-final.qmd` each gain one plain-prose link to
`../donnees/index.qmd`. No other edit to those pages (T-I).

## 3. Script CLIs (`scripts/financial-analysis/`)

```sh
python scripts/financial-analysis/generate-dataset.py            # regenerate all artifacts
python scripts/financial-analysis/generate-dataset.py --check    # exit 0 iff all invariants hold (SC-001)
python scripts/financial-analysis/generate-dataset.py --seed ID --out DIR   # per-student variant (FR-009)
```

Contract:

- Default mode writes: the Excel, the PDF, the markdown table fragments,
  and the corrigé figures — all from `dataset_params.*`. Deterministic: two
  runs with the same params produce byte-identical Excel (zip timestamps
  normalized).
- `--check` re-reads the generated Excel and asserts: bilan actif = passif
  per year; CR résultat ties to bilan; flux Δ trésorerie = Δ trésorerie
  bilan; consolidé = Σ − éliminations per line. Prints one line per check;
  exit 0 = all pass, exit 1 with a list of failures otherwise.
- `--seed` mode: applies the documented poste shifts (R5) derived from the
  seed, re-derives all statements, runs the same checks, writes only the
  variant Excel to `--out`. Same seed → identical file (hash-comparable).
- No network access, no tracking, no output outside the target dirs.

## 4. Forbidden content (SC-005)

No published `.qmd`, HTML, Excel or PDF may contain hidden instructions
aimed at readers' AI tools (invisible text, zero-width characters, HTML
comments with directives, prompt-injection strings). Validation: grep the
rendered `docs/` pages for HTML comments and zero-width chars, plus manual
inspection of each new page — see quickstart.md step 6.
