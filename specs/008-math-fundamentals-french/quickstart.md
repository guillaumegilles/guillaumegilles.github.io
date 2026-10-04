# Quickstart Validation Guide: Mathematical Fundamentals — French Version

**Feature**: 008-math-fundamentals-french
**Date**: 2026-09-17
**References**: [spec.md](spec.md) · [data-model.md](data-model.md) ·
[contracts/url-structure.md](contracts/url-structure.md)

This guide documents how to validate that the French course is correctly
implemented end-to-end. Run these checks in order after completing
implementation.

## Prerequisites

- Quarto CLI installed and available on `PATH`
- Python virtual environment activated: `source .venv/bin/activate`
- Working directory: repository root (`/home/guillaume/www`)

## Step 1 — File Inventory Check

Confirm all 20 French `.qmd` files and 2 support files exist.

```sh
# Count FR .qmd files (expect: 20)
find fr/teaching/mathematical-fundamentals -name "*.qmd" \
  ! -name "_*" | wc -l

# Verify support files exist
ls fr/teaching/mathematical-fundamentals/_metadata.yml
ls fr/teaching/mathematical-fundamentals/_lang-switch.qmd
```

**Expected**: `20` from the count command; both `ls` commands succeed.

## Step 2 — Front Matter Validation

Verify every French file declares the correct `lang` and that slide decks
declare the correct RevealJS theme path.

```sh
# Check lang: fr is set in all FR .qmd files
grep -rL "lang: fr" fr/teaching/mathematical-fundamentals/*.qmd
```

**Expected**: No output (all files contain `lang: fr`).

```sh
# Check slide decks reference the correct theme path (3 levels up)
grep -l "format:" fr/teaching/mathematical-fundamentals/*.qmd | xargs grep -l "revealjs" | \
  xargs grep "theme:"
```

**Expected**: All 8 slide decks show `theme: ../../../assets/dark-slides.scss`.

```sh
# Check reference modules do NOT declare revealjs format
grep -rL "format:" fr/teaching/mathematical-fundamentals/module-[1-8].qmd
```

**Expected**: All 8 reference module filenames (they should NOT have `format:`).

## Step 3 — Render Gate (most important)

```sh
quarto render
```

**Expected**: Exit code 0. Both English and French pages render without
errors or warnings about missing files, broken references, or unresolved
hrefs.

If this fails, check:
1. `_quarto.yml` sidebar `fr-mathematical-fundamentals` block — every listed
   file must exist on disk.
2. Relative paths in FR slide front matter (`../../../assets/dark-slides.scss`).
3. `image:` path in FR `index.qmd` (should be
   `../../teaching/mathematical-fundamentals/image.jpg`).

## Step 4 — Output Directory Verification

After `quarto render`, confirm French HTML files land in `docs/fr/`:

```sh
# Count rendered FR course HTML files (expect: 20)
find docs/fr/teaching/mathematical-fundamentals -name "*.html" | wc -l

# Spot-check a reference module and a slide deck
ls docs/fr/teaching/mathematical-fundamentals/module-1.html
ls docs/fr/teaching/mathematical-fundamentals/module-1-slides.html
ls docs/fr/teaching/mathematical-fundamentals/index.html
ls docs/fr/teaching/mathematical-fundamentals/glossary.html
```

**Expected**: count ≥ 20; all spot-checked files exist.

## Step 5 — Sidebar Navigation Audit

Open the site locally and verify French sidebar navigation.

```sh
quarto preview --no-browser --port 4848 &
# Then open http://localhost:4848/fr/teaching/mathematical-fundamentals/
```

Walk through the checklist:

- [ ] French sidebar is visible on `index.html`
- [ ] Each of the 8 module sections appears with "Référence" and "Diapositives"
  links
- [ ] Resources section shows Glossaire, Aide-mémoire, Guide d'apprentissage
- [ ] Clicking each sidebar link opens the correct French page (no 404)

## Step 6 — Language Switcher Validation

From the English course index:

- [ ] Language switcher link is visible (e.g., "🇫🇷 Version française")
- [ ] Clicking it navigates to
  `/fr/teaching/mathematical-fundamentals/index.html`

From the French course index:

- [ ] Language switcher link shows "🇬🇧 English version"
- [ ] Clicking it navigates to `/teaching/mathematical-fundamentals/index.html`

From an inner page (e.g., Module 3 reference):

- [ ] Switcher on `/teaching/mathematical-fundamentals/module-3.html` links
  to `/fr/teaching/mathematical-fundamentals/module-3.html`
- [ ] Switcher on `/fr/teaching/mathematical-fundamentals/module-3.html`
  links to `/teaching/mathematical-fundamentals/module-3.html`

## Step 7 — Content Structural Audit (sample check)

Pick one module (e.g., Module 2) and verify:

- [ ] French prose throughout (no English sentences in body text)
- [ ] LaTeX formulas present and identical to English source
- [ ] `.callout-note` for learning objectives and definitions
- [ ] `.callout-tip` for key formulas
- [ ] `.callout-caution collapse="true"` for at least one exercise solution
- [ ] Link to French slide deck visible at top of reference module

## Step 8 — Glossary Parity Check

```sh
# Count entries in English glossary (count "##" section headers as proxy)
grep -c "^##" teaching/mathematical-fundamentals/glossary.qmd

# Count entries in French glossary
grep -c "^##" fr/teaching/mathematical-fundamentals/glossary.qmd
```

**Expected**: Both counts are equal (VR-006: French glossary has parity with
English glossary at section level).

## Step 9 — Recommended Literature Check (T-VIII)

Open `fr/teaching/mathematical-fundamentals/index.qmd` and confirm:

- [ ] A "Bibliographie recommandée" (or equivalent French heading) section
  exists
- [ ] All 3 references from the English syllabus appear with author, title,
  edition, and publisher in French

## Step 10 — Freeze Commit Check

After a clean render, verify freeze entries are generated:

```sh
ls _freeze/fr/teaching/mathematical-fundamentals/
```

**Expected**: Freeze subdirectories exist for pages that executed computation.
Commit `_freeze/`, `docs/`, and all source changes in the same commit
(Development Workflow requirement).

## Success Criteria Mapping

| SC | Validation step |
|---|---|
| SC-001: 20 FR counterparts exist | Steps 1, 4 |
| SC-002: Full French navigation without dead links | Steps 5, sidebar audit |
| SC-003: Language switch in 1 click | Step 6 |
| SC-004: `quarto render` exits 0 | Step 3 |
| SC-005: Module structural audit | Step 7 |
| SC-006: Glossary entry parity | Step 8 |
