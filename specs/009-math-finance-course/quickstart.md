# Quickstart Validation Guide: Cours de Mathématiques Financières (M1)

**Feature**: `009-math-finance-course`
**Phase**: 1 — Design
**Date**: 2026-10-04

This guide describes how to validate that the feature is complete and working,
end-to-end, without reimplementing it. It references the contracts and data model
rather than duplicating their content.

---

## Prerequisites

- Quarto CLI installed (already available in project)
- Python virtualenv active: `source .venv/bin/activate`
- Working directory: project root `/home/guillaume/www`

---

## Step 1: Verify File Structure

After implementation, confirm that all required files exist:

```sh
# Should list 7 new/modified files
ls fr/teaching/mathematics-finance/
# Expected: _metadata.yml  formulaire.qmd  glossaire.qmd  index.qmd
#           module-01.qmd  module-02.qmd   module-03.qmd

# English stub should exist and have lang: en
head -10 teaching/mathematical-finance/index.qmd
# Expected front-matter: lang: en, title: "Financial Mathematics"
```

---

## Step 2: Verify `_quarto.yml` Sidebar Registration

```sh
grep -n "en-mathematics-finance\|fr-mathematics-finance" _quarto.yml
# Expected: two sidebar blocks (one EN, one FR) with their IDs
```

Confirm the sidebar block contents match the URL contract in
`specs/009-math-finance-course/contracts/url-structure.md`.

---

## Step 3: Single-File Render (fastest feedback loop)

Render each file individually to catch YAML or LaTeX errors before a full render:

```sh
# Syllabus
quarto render fr/teaching/mathematics-finance/index.qmd --quiet

# Day modules
quarto render fr/teaching/mathematics-finance/module-01.qmd --quiet
quarto render fr/teaching/mathematics-finance/module-02.qmd --quiet
quarto render fr/teaching/mathematics-finance/module-03.qmd --quiet

# Resources
quarto render fr/teaching/mathematics-finance/glossaire.qmd --quiet
quarto render fr/teaching/mathematics-finance/formulaire.qmd --quiet

# English stub
quarto render teaching/mathematical-finance/index.qmd --quiet
```

Each command should exit 0 with no error messages.

---

## Step 4: Full Site Render

```sh
quarto render
```

Expected: exit code 0. Any non-zero exit code indicates a broken reference,
missing file, or YAML syntax error.

---

## Step 5: Content Validation Checklist

Open each rendered page in `docs/` (or via `quarto preview`) and verify:

### `fr/teaching/mathematics-finance/index.html` (Syllabus)

- [ ] Title: "Mathématiques financières" or similar
- [ ] Section "Bibliographie recommandée" present with ≥ 5 references
- [ ] Each reference has: author(s), title, edition, publisher
- [ ] Architecture table with 3 journées visible
- [ ] Links to module-01, module-02, module-03 work (or show correct relative paths)

### `fr/teaching/mathematics-finance/module-01.html` (Journée 1)

- [ ] Section "Intérêts simples et composés" with formulas $C_n = C_0(1+ni)$ and $C_n = C_0(1+i)^n$
- [ ] Section "Actualisation" with formula $V_0 = V_n / (1+i)^n$
- [ ] Section "Taux équivalent" with formula $i_m = (1+i_a)^{1/12} - 1$
- [ ] Section "Annuités constantes" with both acquired and present value formulas
- [ ] At least one collapsible derivation (`.callout-caution collapse="true"`)
- [ ] OJS demo for capitalisation vs actualisation loads and responds to sliders
- [ ] Exercises at levels N1, N2, N3 present with collapsible solutions
- [ ] Each formula followed by plain-language "Lecture :" explanation

### `fr/teaching/mathematics-finance/module-02.html` (Journée 2)

- [ ] Amortization table structure (Période / Capital initial / Intérêts / Amortissement / Annuité / CRD)
- [ ] Section on `emprunt in fine` and `amortissement constant`
- [ ] Section on actuarial rate principle
- [ ] Bond valuation formula $P_0 = \sum C/(1+r)^t + N/(1+r)^n$
- [ ] Macaulay duration formula
- [ ] OJS demo: bond price vs market rate responds to sliders (coupon, nominal, maturity, rate)
- [ ] Price-rate inverse relationship explained in plain language

### `fr/teaching/mathematics-finance/module-03.html` (Journée 3)

- [ ] Cash flow construction section (initial, operating, terminal flows)
- [ ] Common pitfalls listed (BFR, sunk costs, double-counting)
- [ ] NPV formula with decision rule (VAN > 0 / = 0 / < 0)
- [ ] IRR limitations section (multiple IRRs, reinvestment assumption, VAN/TRI conflict)
- [ ] Sensitivity analysis (one-variable-at-a-time)
- [ ] Scenario analysis with expected value formula
- [ ] OJS demo: VAN curve as function of k, TRI marked as zero crossing
- [ ] Equivalent annuity formula

### `fr/teaching/mathematics-finance/glossaire.html`

- [ ] ≥ 30 symbol entries (see data-model.md for full list)
- [ ] All entries have: Notation, Nom, Définition, Prononciation (where applicable), Module(s)

### `fr/teaching/mathematics-finance/formulaire.html`

- [ ] All 10 formulas from data-model.md are present and correctly rendered
- [ ] Each formula has its name label

### `teaching/mathematical-finance/index.html` (EN Stub)

- [ ] `lang: en` in front-matter (check rendered `<html lang="en">`)
- [ ] Link to FR counterpart present and functional
- [ ] "Full English course coming soon" or equivalent notice visible

---

## Step 6: Navigation Smoke Test

Using `quarto preview` (or by opening `docs/` directly):

1. Navigate to `/fr/teaching/mathematics-finance/`
2. Confirm the `fr-mathematics-finance` sidebar appears with all 6 pages
3. Click each sidebar link and confirm the correct page loads
4. Confirm the `**Ressources**` section groups glossaire and formulaire

---

## Step 7: OJS Demo Functional Test

For each module page, open the rendered HTML in a browser:

- **Module 01 demo**: Move the sliders (C0, i, n) → bars in the chart update in real time
- **Module 02 demo**: Move the rate slider (r) → bond price curve and dot update; status label (prime/décote/au pair) updates
- **Module 03 demo**: Move the discount rate slider (k) → VAN value updates; red dot (TRI) stays fixed at NPV=0

---

## Failure Modes and Recovery

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `quarto render` fails with "file not found" | A page listed in `_quarto.yml` sidebar doesn't exist yet | Create the missing `.qmd` file |
| OJS demo doesn't load | Syntax error in OJS block | Check browser console; compare skeleton in `research.md` |
| LaTeX formulas not rendered | Missing `$$` delimiters or stray characters | Use `$...$` (inline) and `$$...$$` (display) strictly |
| `lang` attribute missing in HTML | `_metadata.yml` not picked up | Verify `_metadata.yml` is in the same directory as the `.qmd` files |
| Sidebar doesn't appear | Sidebar ID mismatch between `_quarto.yml` and page | Verify page paths in sidebar block match actual file paths exactly |
