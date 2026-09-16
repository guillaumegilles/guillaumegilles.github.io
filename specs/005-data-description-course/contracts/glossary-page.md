# Contract: Glossary Page (`glossary.qmd`)

Applies to `teaching/data-description/glossary.qmd`. Enforces FR-010 and
constitution T-V.

## Front matter (required)

```yaml
---
title: "Glossary"
subtitle: "Data Description"
lang: en
draft: true   # removed together with all other 14 files once SC-001 is met
---
```

## Required content

A table (or grouped tables by topic: Univariate position, Univariate
dispersion/shape, Bivariate) with one row per symbol/formula introduced
in any session:

| Notation | Name | Plain-language definition | Pronunciation (Greek only) | Introduced in |
|---|---|---|---|---|
| $\bar{x}$ | Sample mean | … | "x-bar" | Session 6 |
| $Me$ | Median | … | — | Session 6 |
| $Mo$ | Mode | … | — | Session 6 |
| $Q_1, Q_2, Q_3$ | Quartiles | … | — | Session 5 |
| $\sigma$ / $s$ | Population/sample std. dev. | … | "sigma" | Session 7 |
| $CV$ | Coefficient of variation | … | — | Session 7 |
| Skewness | Asymmetry coefficient | … | — | Session 8 |
| $\text{Cov}(X,Y)$ | Covariance | … | — | Session 11 |
| $r$ | Correlation coefficient | … | — | Session 11 |

(Full row set is derived while authoring each session — this contract
fixes the required columns and the rule below, not the final row
count.)

## Rule

Every mathematical symbol or named formula that appears in **any**
session file MUST have a corresponding row here before that session is
considered complete (SC-007: 100% glossary coverage). Adding a symbol to
a session without adding it here is a contract violation.

## Validation checklist for this contract

- [ ] Front matter has `title`, `subtitle`, `lang: en`, `draft: true`
- [ ] Every symbol from every session appears exactly once (no
      duplicates, no omissions)
- [ ] Every Greek-letter symbol has a pronunciation guide
- [ ] Table is linked from the course sidebar (`_quarto.yml`)
