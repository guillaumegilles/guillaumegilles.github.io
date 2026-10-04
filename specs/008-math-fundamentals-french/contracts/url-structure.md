# Contract: Bilingual URL Structure

**Feature**: 008-math-fundamentals-french
**Date**: 2026-09-17
**Type**: URL routing contract (static site)

---

## Invariant

For every English page at path `/teaching/mathematical-fundamentals/<file>.html`,
a French counterpart exists at `/fr/teaching/mathematical-fundamentals/<file>.html`.

The French URL is always derived from the English URL by prepending `/fr`.
The English URL is always derived from the French URL by stripping the leading `/fr`.

This invariant is relied upon by the OJS language switcher (`_lang-switch.qmd`),
which computes counterpart URLs at runtime using `window.location.pathname`.
Any deviation (e.g., renaming a file in one language but not the other) breaks
the switcher silently.

---

## URL Table

| English URL | French URL |
|---|---|
| `/teaching/mathematical-fundamentals/index.html` | `/fr/teaching/mathematical-fundamentals/index.html` |
| `/teaching/mathematical-fundamentals/module-1.html` | `/fr/teaching/mathematical-fundamentals/module-1.html` |
| `/teaching/mathematical-fundamentals/module-2.html` | `/fr/teaching/mathematical-fundamentals/module-2.html` |
| `/teaching/mathematical-fundamentals/module-3.html` | `/fr/teaching/mathematical-fundamentals/module-3.html` |
| `/teaching/mathematical-fundamentals/module-4.html` | `/fr/teaching/mathematical-fundamentals/module-4.html` |
| `/teaching/mathematical-fundamentals/module-5.html` | `/fr/teaching/mathematical-fundamentals/module-5.html` |
| `/teaching/mathematical-fundamentals/module-6.html` | `/fr/teaching/mathematical-fundamentals/module-6.html` |
| `/teaching/mathematical-fundamentals/module-7.html` | `/fr/teaching/mathematical-fundamentals/module-7.html` |
| `/teaching/mathematical-fundamentals/module-8.html` | `/fr/teaching/mathematical-fundamentals/module-8.html` |
| `/teaching/mathematical-fundamentals/module-1-slides.html` | `/fr/teaching/mathematical-fundamentals/module-1-slides.html` |
| `/teaching/mathematical-fundamentals/module-2-slides.html` | `/fr/teaching/mathematical-fundamentals/module-2-slides.html` |
| `/teaching/mathematical-fundamentals/module-3-slides.html` | `/fr/teaching/mathematical-fundamentals/module-3-slides.html` |
| `/teaching/mathematical-fundamentals/module-4-slides.html` | `/fr/teaching/mathematical-fundamentals/module-4-slides.html` |
| `/teaching/mathematical-fundamentals/module-5-slides.html` | `/fr/teaching/mathematical-fundamentals/module-5-slides.html` |
| `/teaching/mathematical-fundamentals/module-6-slides.html` | `/fr/teaching/mathematical-fundamentals/module-6-slides.html` |
| `/teaching/mathematical-fundamentals/module-7-slides.html` | `/fr/teaching/mathematical-fundamentals/module-7-slides.html` |
| `/teaching/mathematical-fundamentals/module-8-slides.html` | `/fr/teaching/mathematical-fundamentals/module-8-slides.html` |
| `/teaching/mathematical-fundamentals/glossary.html` | `/fr/teaching/mathematical-fundamentals/glossary.html` |
| `/teaching/mathematical-fundamentals/formula-sheet.html` | `/fr/teaching/mathematical-fundamentals/formula-sheet.html` |
| `/teaching/mathematical-fundamentals/learning-guide.html` | `/fr/teaching/mathematical-fundamentals/learning-guide.html` |

---

## Language Switcher Logic (informative)

The OJS block in `_lang-switch.qmd` implements the following derivation at runtime:

```js
const path = window.location.pathname;
const isFrench = path.startsWith("/fr/");

const counterpartUrl = isFrench
  ? path.replace(/^\/fr/, "")   // strip leading /fr → EN URL
  : "/fr" + path;               // prepend /fr → FR URL

const label = isFrench
  ? "🇬🇧 English version"
  : "🇫🇷 Version française";
```

This logic is correct if and only if the URL invariant above holds for every page.
A file rename that is not mirrored in both language trees will produce a 404 with
no build-time warning from Quarto — the failure is silent and runtime-only.

---

## Maintenance Rules

1. **Rename symmetry**: If a file is renamed in `teaching/mathematical-fundamentals/`,
   its counterpart in `fr/teaching/mathematical-fundamentals/` must be renamed in
   the same commit. Partial renames break the language switcher silently.

2. **Add symmetry**: If a new page is added to the English course, a French
   counterpart (full or stub) must be added before the commit is merged. A stub
   must at minimum declare `lang: fr` and a French `title` so the site renders
   without error.

3. **Sidebar parity**: The `_quarto.yml` sidebar blocks for both
   `mathematical-fundamentals` and `fr-mathematical-fundamentals` must be updated
   in the same commit whenever pages are added, removed, or renamed.

4. **Render gate**: `quarto render` must exit 0 with both EN and FR pages in scope
   before a PR is merged. A broken FR page that fails silently (renders with
   missing content but exits 0) should be caught by VR-001 and VR-008 in the
   data model.

5. **URL stability**: Once a URL pair is published (i.e., appears in `docs/` and
   is served by GitHub Pages), it must not be changed without adding a redirect.
   Quarto does not generate redirects automatically; a manual HTML stub at the
   old path is required.
