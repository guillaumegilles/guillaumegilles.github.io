# Contract: Module Page Structure (`module-N.qmd`)

Every module page is a "UI contract" that learners rely on. A module MUST
conform to the following structure and rules.

## Front matter

```yaml
---
title: "N️⃣ <English module title>"
abstract: |
  <one-paragraph English summary of the module>
date: <session date, preserved from syllabus>
lang: en
keywords: Lesson
format:
  html:
    code-links:        # cross-module navigation
      - text: Syllabus
        icon: file-code
        href: index.html
      - text: Module 1..8
        icon: file-code
        href: module-1.html   # … through module-8.html
---
```

Rules:
- `lang: en` REQUIRED.
- Every `code-links` `href` MUST resolve to an existing page (FR-011, SC-006).

## Body (required order — T-II)

1. **Learning objectives** — `::: {.callout-note}` listing what the student will
   be able to do (English).
2. **Introduction** — plain-English motivation in an economics/management
   context (FR-004, FR-013).
3. **Theory** — definitions and rules for every source-deck concept
   (FR-005, SC-003), each introduced before use.
   - Definitions → `.callout-note`
   - Key formulas → `.callout-tip`
   - Caveats / common mistakes → `.callout-warning`
   - Exam tips / critical rules → `.callout-important`
4. **At least one collapsible derivation** — `::: {.callout-caution
   collapse="true"}` with a step-by-step proof/derivation (T-VI).
5. **Worked examples** — multiple, step-by-step, each ending with a stated
   result matching the source (FR-004a, SC-004).
6. **Exercises** — a bank of practice items, each with a revealable solution via
   `::: {.callout-caution collapse="true"}` (FR-012). No runtime widgets.
7. **Demo gaps (where applicable)** — `::: {.callout-important}` labelled
   `TODO:` for any priority concept that would warrant an interactive demo
   (T-IV reconciliation).

## Content rules

- All learner-facing text in English (FR-002); zero untranslated FR prose
  (SC-002).
- All math in LaTeX `$...$` / `$$...$$` (FR-009); no Unicode/HTML math.
- Prose wraps at 80 characters (constitution workflow).
- No inline `style=` or `<style>` blocks (constitution §V).
- Every new symbol/formula also appears in `glossary.qmd` (T-V).

## Acceptance (per module)

- [ ] Renders under `quarto render` with exit 0 and no broken math (SC-005).
- [ ] All Decision-3 concepts for this module are present (SC-003).
- [ ] All results that exist in the source agree with the source (SC-004).
- [ ] Contains ≥1 collapsible derivation (T-VI) and ≥ multiple worked examples.
- [ ] All `code-links` resolve (SC-006).
