# Contract: Page Structure — Mathématiques financières (M1)

**Feature**: `009-math-finance-course`
**Type**: Content structure contract
**Date**: 2026-10-04

This contract defines the required structure of each page type in the French
financial mathematics course. Any page that deviates from these structures
fails the constitution check and must be corrected before publication.

---

## Contract 1 — Syllabus (`index.qmd`)

```markdown
---
title: "Mathématiques financières"
lang: fr
date-modified: YYYY-MM-DD
abstract: |
  [1–3 sentences describing the course and its central question]
---

## Description du cours

[Fil directeur: one-sentence guiding question]

[Public, volume horaire, niveau requis, format pédagogique]

### Compétences visées

[Technical competencies list]
[Managerial competencies list]

## Architecture du cours

| Journée | Problématique centrale | Principaux thèmes | Production attendue |
|---------|------------------------|-------------------|---------------------|
| [Jour 1 row] |
| [Jour 2 row] |
| [Jour 3 row] |

## Bibliographie recommandée

### Ouvrage principal

**[Author(s)]**
*[Title]*, [edition].
[Publisher], [year].

### Ouvrages complémentaires

[4 more references in the same format]
```

**Mandatory**: The bibliography section MUST contain at minimum 1 primary reference
and 2 supplementary references, each with author(s), title, edition, publisher, year.

---

## Contract 2 — Day-Module Page (`module-NN.qmd`)

```markdown
---
title: "Journée N — [Problématique]"
lang: fr
date-modified: YYYY-MM-DD
abstract: |
  [Journée problématique in 1–2 sentences]
---

## Objectifs de la journée

[Bulleted list of learning outcomes]

---

## Séquence N — [Titre]

> *Durée : [X] minutes/heure(s)*

### Intuition économique

[Economic context and motivation — no formulas yet]

### Représentation

[Time line description or diagram description]

::: {.callout-note}
## Ligne du temps
[Steps: identifier la date d'évaluation, positionner les flux, etc.]
:::

### Formalisation mathématique

$$[formula]$$

**Lecture :** [Plain-language explanation of what the formula computes and why it matters]

::: {.callout-caution collapse="true"}
## Démonstration

[Step-by-step formal derivation]
:::

### Décision managériale

[How to interpret the result and make a recommendation]

### Démonstration interactive

::: {.callout-important}
## TODO: Démonstration — [concept]
[Mark if demo not yet implemented]
:::

```{ojs}
[OJS block — see research.md for skeletons]
```

### Exercices

#### Niveau 1 — Application directe

**Exercice 1.** [Statement]

::: {.callout-caution collapse="true"}
## Solution
[Solution]
:::

#### Niveau 2 — Problème contextualisé

**Exercice 2.** [Statement]

::: {.callout-caution collapse="true"}
## Solution
[Solution]
:::

#### Niveau 3 — Étude de cas

**Cas.** [Statement — multi-step, requires recommendation]

::: {.callout-caution collapse="true"}
## Correction
[Full worked solution with recommendation]
:::

---

## Synthèse

::: {.callout-tip}
## Points clés
[Bulleted key takeaways]
:::

::: {.callout-warning}
## Erreurs fréquentes
[Bulleted list of common mistakes]
:::
```

**Mandatory per module**:
- At least one formal derivation in a collapsible `.callout-caution` block (T-VI)
- At least one OJS interactive demo OR a `TODO:` `.callout-important` marker (T-IV)
- Exercises at each of the three difficulty levels (FR-007)
- Every formula accompanied by a plain-language "Lecture :" paragraph (T-III)

---

## Contract 3 — Glossaire (`glossaire.qmd`)

```markdown
---
title: "Glossaire — Mathématiques financières"
lang: fr
date-modified: YYYY-MM-DD
---

## Symboles mathématiques

| Notation | Nom | Définition | Prononciation | Module(s) |
|----------|-----|------------|---------------|-----------|
| $C_0$ | Capital initial | Somme placée ou empruntée à la date 0 | — | 01, 02 |
| $i$ | Taux d'intérêt périodique | Rendement ou coût par période | — | 01, 02, 03 |
| ... | | | | |

## Termes financiers

| Terme | Définition | Module(s) |
|-------|------------|-----------|
| Actualisation | ... | 01 |
| Annuité | ... | 01, 02 |
| ... | | |
```

**Mandatory**: All symbols listed in `data-model.md` (≥ 30 entries) must appear.

---

## Contract 4 — Formulaire (`formulaire.qmd`)

```markdown
---
title: "Formulaire — Mathématiques financières"
lang: fr
date-modified: YYYY-MM-DD
---

## Formules essentielles

### Valeur temps de l'argent

**Capitalisation**
$$V_n = V_0(1+i)^n$$

**Actualisation**
$$V_0 = \frac{V_n}{(1+i)^n}$$

[... 8 more formulas from data-model.md]
```

**Mandatory**: All 10 formulas from `data-model.md` must be present with their names.

---

## Contract 5 — English Stub (`teaching/mathematical-finance/index.qmd`)

```markdown
---
title: "Financial Mathematics"
lang: en
date-modified: YYYY-MM-DD
---

::: {.callout-note}
## Ce cours est disponible en français
[Link to fr/teaching/mathematics-finance/index.qmd]
:::

## Course Overview

[2–3 sentence EN course description]

## Full English Course — Coming Soon

A full English version of this course is in preparation. In the meantime, the
complete course materials are available in French:

→ [Mathématiques financières (version française)](../fr/teaching/mathematics-finance/index.qmd)
```

**Mandatory**: `lang: en` front-matter, link to FR counterpart, bilingual notice.
