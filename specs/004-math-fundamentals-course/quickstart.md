# Quickstart — Build & Verify the Mathematical Fundamentals Course

Audience: whoever implements/renders the course (via `/speckit.tasks` →
`/speckit.implement`).

## Prerequisites

- Quarto CLI installed; project virtualenv `.venv/` active if needed.
- Source archives present under
  `teaching/mathematical-fundamentals/MS01-001-G_Fondamentaux*/` (reference
  only — do not modify or publish).
- Optional extraction helpers: `python-pptx` (decks), `pdftotext` (handouts/exam)
  to confirm numeric results.

## Author / edit loop

1. Edit the relevant `.qmd` under `teaching/mathematical-fundamentals/`.
2. Follow `contracts/module-page.md` (structure, callout semantics, LaTeX,
   80-char wrap, `lang: en`).
3. Cross-check concepts against `research.md` Decision 3 and numbers against the
   source deck/handout.
4. Add any new symbol/formula to `glossary.qmd`.

## Render (build gate)

```bash
# From repo root — render just this course while iterating:
quarto render teaching/mathematical-fundamentals

# Full-site render before commit (constitution render gate):
quarto render
```

`quarto render` MUST exit 0. `docs/` and any `_freeze/` updates are committed in
the same commit as the sources (constitution §III + workflow).

## Verify (acceptance)

- **Completeness (SC-001, SC-007)**: index links to modules 1–8; every module
  page has objectives, theory, ≥1 derivation, worked examples, and exercises.
- **English (SC-002)**: scan for untranslated French learner-facing prose:
  ```bash
  # heuristic scan for common FR words in learner-facing text
  grep -rniE '\b(le|la|les|des|une|résultat|exercice|solution|équation)\b' \
    teaching/mathematical-fundamentals/module-*.qmd teaching/mathematical-fundamentals/index.qmd
  ```
  (Review hits; some may be legitimate proper nouns / bibliography.)
- **Concept coverage (SC-003)**: for each module, tick every concept in
  research.md Decision 3.
- **Result fidelity (SC-004)**: spot-check worked/exercise results against the
  deck/handout.
- **Rendering (SC-005)**: no broken math, no render errors.
- **Links (SC-006)**: open the syllabus and click every module + glossary link;
  confirm all `code-links` resolve.

## Navigation registration

- Add a `mathematical-fundamentals` sidebar block to `_quarto.yml` (index first,
  then module-1…module-8, then glossary). Reconcile local `_metadata.yml` so it
  does not conflict.

## Definition of done

All eight modules at `render-clean` state (data-model.md), glossary present and
linked, syllabus literature in English with full bibliographic detail,
`quarto render` exits 0, and all SC-001…SC-007 checks pass.
