# Contract: Glossary Page Structure (`glossary.qmd`)

A central glossary is mandatory for every course (T-V).

## Front matter

```yaml
---
title: "Glossary"
abstract: |
  French–English glossary of the symbols and terms used across the
  Mathematical Fundamentals course.
lang: en
date-modified: <date>
---
```

## Structure

- Grouped by theme (e.g., Numbers & operations, Algebra, Functions, Financial
  mathematics, Optimization), mirroring the module sequence.
- Each entry uses a definition-list item following the site pattern:

```markdown
**English term** (*French equivalent*)
: Plain-language definition, with notation in LaTeX where relevant (e.g., $|a|$).
```

## Rules (T-V)

- Every mathematical symbol and formula introduced in any module MUST appear
  here (e.g., $|a|$, $a^n$, $\sqrt{a}$, $\Delta$, $C_n = C_0(1+i)^n$, common
  ratio $r$, first term $u_0$, discriminant, derivative $f'(x)$).
- Notation in LaTeX; definitions in plain English (T-III).
- Linked from the course sidebar in `_quarto.yml` (T-V).

## Acceptance

- [ ] Registered in the sidebar block.
- [ ] Covers all symbols/formulas introduced across Modules 1–8.
