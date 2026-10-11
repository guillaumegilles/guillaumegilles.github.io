# Pedagogical Contract: Mathematical Finance Intuition-First Structure

**Feature**: 011-math-finance-intuition
**Date**: 2026-10-11
**Status**: Complete

---

## Purpose

This contract defines the mandatory internal structure for every major concept section (Séquence) in the three Mathematical Finance modules. It ensures the "concrete-to-abstract" pedagogy is consistently implemented across all 15 sections.

---

## Concept Section Contract (Séquences 2-5, plus Module 2 Séquence 6)

**Applies to**: 13 sections — Module 1 Séquences 2-5 (4), Module 2 Séquences 2-6 (5, including *Sensibilité obligataire*), Module 3 Séquences 2-5 (4)

### Required Structure (7 Steps in Order)

| Step | Element | Format | Requirements |
|------|---------|--------|--------------|
| 1 | **Concrete Case** | `::: {.callout-note} ## Situation concrète ... :::` OR `## Cas réel` heading + narrative | - 3-8 sentences narrative<br>- Specific realistic numbers (EUR, rates %)<br>- Ends with decision question (?)<br>- Appears BEFORE any formula |
| 2 | **Numerical Exploration** | Table, step-by-step calculation, or `{ojs}`/`{shinylive-python}` block | - Uses concrete case numbers<br>- Shows period-by-period or step-by-step<br>- No general formula yet |
| 3 | **Pattern Recognition** | `::: {.callout-tip} ## Observez le schéma ... :::` OR `### Remarquez le pattern` | - Explicit "notice the pattern" prompt<br>- Guides student to generalize<br>- Bridges to formula |
| 4 | **Formula Box** | `::: {.callout-tip} $$FORMULA$$ :::` OR `\boxed{FORMULA}` | - Visually boxed (callout-tip per Constitution V)<br>- Valid LaTeX<br>- Immediately followed by Explanation |
| 5 | **Explanation** | `::: {.callout-note} ## Explication en langage clair ... :::` | - 4 components (see below)<br>- Directly after Formula Box<br>- Plain French, business language |
| 6 | **Formal Definition** | `::: {.callout-important} ## Définition — Name ... :::` | - Precise mathematical definition<br>- Symbols defined<br>- Collapsible if lengthy |
| 7 | **Worked Example** | `::: {.callout-note} ## Exemple résolu ... :::` | - New numbers (not concrete case numbers)<br>- Step-by-step application<br>- References formula explicitly |
| 8 | **Economic Interpretation** | `::: {.callout-note} ## Interprétation économique ... :::` OR `::: {.callout-tip} ## Ce que ça signifie ... :::` | - Business meaning of result<br>- "Si X change, Y change comment"<br>- Links to managerial decision |

### Required Callouts (Constitution V)

| Callout Type | Use For | Semantic |
|--------------|---------|----------|
| `.callout-note` | Situation concrète, Explication, Exemple résolu, Interprétation économique | Definitions, background, examples |
| `.callout-tip` | Formula Box, Pattern Recognition, Numerical Exploration (if demo) | Key formulas, practical shortcuts |
| `.callout-warning` | Erreur fréquente | Remarks, caveats, common mistakes |
| `.callout-important` | Formal Definition, Règle d'or reinforcement | Exam tips, critical rules |

### Mandatory Elements

1. **ConcreteCase** — Must exist and precede first FormulaBox
2. **FormulaBox + Explanation** — Every formula gets both; Explanation has 4 components
3. **ErreurFrequente** — One per concept section (`.callout-warning` with 4-part structure)
4. **RegleOrReinforcement** — "Règle d'or — La ligne du temps avant toute formule" stated at section start
5. **VisualDiagram or InteractiveDemo** — For Duration, VAN profile, Convexity, Annuity timeline concepts

---

## Synthesis Section Contract (Séquence 6; Séquence 7 in Module 2)

**Applies to**: 3 sections (Module 1 Séquence 6: Cas pratique; Module 2 Séquence 7: Étude de cas — choisir un financement; Module 3 Séquence 6: Cas intégrateur)

### Required Structure (3 Steps in Order)

| Step | Element | Format | Requirements |
|------|---------|--------|--------------|
| 1 | **Situation** | `## Situation` or `::: {.callout-note} ## Contexte ... :::` | - Full scenario context<br>- Recaps or introduces decision context<br>- All numbers specified |
| 2 | **Application** | Step-by-step with `### Étape N — ...` headings | - Applies concepts from Séquences 2-5<br>- Shows formula selection reasoning<br>- Intermediate calculations shown |
| 3 | **Synthèse** | `::: {.callout-important} ## Cadre de décision / Recommandation ... :::` | - Decision framework/template<br>- "Si X, alors Y" rules<br>- Links to managerial action |

### Required Callouts

| Callout Type | Use For |
|--------------|---------|
| `.callout-note` | Situation context |
| `.callout-important` | Synthèse / Decision framework |
| `.callout-tip` | Key formula references (optional) |

### Exemptions

- **NO ErreurFrequente required** (per Clarification #3)
- **NO 7-step ladder** — uses 3-step pattern instead
- **RegleOrReinforcement** still required (at section start)

---

## Explanation Contract (4 Components)

Every FormulaBox MUST be immediately followed by an Explanation block with exactly these 4 components:

```markdown
::: {.callout-note}
## Explication en langage clair

**Ce que calcule cette formule**: [1 sentence — output meaning in business terms]

**Rôle de chaque paramètre**:
- `SYMBOL`: [1 sentence — economic role]
- `SYMBOL`: [1 sentence — economic role]
...

**Ce que signifie le résultat**: [1 sentence — business interpretation: "valeur nette créée", "coût réel", etc.]

**Intuition directionnelle**: [1 sentence — "Si X augmente, Y diminue/augmente"]
:::
```

**Validation Rules**:
- All 4 components present and non-empty
- `parameter_roles` covers every symbol in the formula
- No LaTeX in explanation text (plain French only)
- Rendered as `.callout-note` directly after FormulaBox

---

## ErreurFrequente Contract (4 Parts)

Every concept section (Séquences 2-5) MUST include exactly one:

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège**: [The seemingly logical but wrong reasoning]

**Pourquoi c'est faux**: [Technical/mathematical reason]

**Le bon raisonnement**: [Correct approach, linked to formula]

**Astuce mémo**: [One-sentence memory aid]
:::
```

**Validation Rules**:
- All 4 parts present and non-empty
- Rendered as `.callout-warning` (Constitution V: "Remarks, caveats, common mistakes")
- `memo_tip` actionable and memorable
- Only in concept sections (Séquences 2-5), NOT in synthesis (Séquence 6)

---

## Glossary Intuition Contract (3 Fields)

Every symbol in `glossaire.qmd` MUST have an `Intuition` block with exactly 3 fields:

```markdown
### `SYMBOL` — Name

**Ce que ça représente**: [1 sentence — plain concept description]

**Pourquoi ça importe**: [1 sentence — business/decision relevance]

**Intuition clé**: [1 sentence — directional insight or analogy]
```

**Validation Rules**:
- All 3 fields present, max 1 sentence each
- No LaTeX in intuition fields
- French, plain business vocabulary
- Alphabetical order by symbol maintained

---

## Formulaire Intuition Contract

Every formula in `formulaire.qmd` MUST have a one-sentence intuition reminder:

```markdown
## N. Formula Title

$$\boxed{FORMULA}$$

**Intuition**: Cette formule répond à : [concrete question] ?
```

**Validation Rules**:
- All 10 formulas have reminder
- Pattern: "Cette formule répond à : [question] ?"
- Question is concrete and decision-oriented
- Placed immediately after formula box

---

## Interactive Demo Contract (T-IV Compliance)

| Demo | Technology | Justification (T-IV) |
|------|------------|---------------------|
| Capitalisation vs Actualisation | OJS | Pure arithmetic (exponentiation); real-time slider response; no Python needed |
| Bond Price-Yield | OJS | Polynomial evaluation; curve plotting; lightweight |
| VAN-TRI Profile | Shinylive | Requires root-finding (bisection/Newton) for TRI; Python numerical stack |
| Sensitivity Analysis | Shinylive | Requires scenario loops, parameter grids; Python pandas/numpy natural fit |

**Validation Rules**:
- Technology matches computational need
- Embedded as `{ojs}` or `{shinylive-python}` code block
- Loads and responds in browser
- Justification documented in code comment or adjacent callout

---

## Visual Diagram Contract (T-VII Compliance)

| Concept | Diagram Type | Format |
|---------|--------------|--------|
| Duration (Macaulay) | Weighted timeline — cash flows as blocks, center of gravity = duration | Mermaid timeline |
| VAN Profile | VAN vs. discount rate curve; area interpretation; TRI = x-intercept | Mermaid chart or OJS plot |
| Convexity | Price-yield curve with tangent (duration) and curvature (convexity) | Mermaid/ASCII |
| Annuity Timeline | Period-by-period cash flows with present value arrows | Mermaid timeline |

**Validation Rules**:
- Required for each listed concept
- Mermaid preferred for timelines/charts
- Renders in Quarto HTML
- Alt text/description provided

---

## Compliance Checklist (Per Section)

### Concept Section (Séquences 2-5) — 13 sections
- [ ] ConcreteCase before first FormulaBox
- [ ] NumericalExploration with specific numbers
- [ ] PatternRecognition prompt
- [ ] FormulaBox (boxed, LaTeX valid)
- [ ] Explanation (4 components, .callout-note)
- [ ] FormalDefinition (.callout-important)
- [ ] WorkedExample (new numbers)
- [ ] EconomicInterpretation (.callout-note/.callout-tip)
- [ ] ErreurFrequente (.callout-warning, 4 parts)
- [ ] RegleOrReinforcement stated
- [ ] VisualDiagram or InteractiveDemo (if applicable concept)

### Synthesis Section (Séquence 6) — 3 sections
- [ ] Situation (full context)
- [ ] Application (step-by-step, references prior concepts)
- [ ] Synthese (.callout-important, decision framework)
- [ ] RegleOrReinforcement stated
- [ ] NO ErreurFrequente required

### Global (All Modules)
- [ ] Glossaire: 47+ symbols with 3-field Intuition
- [ ] Formulaire: 10 formulas with Intuition reminder
- [ ] 4 Interactive Demos (2 OJS, 2 Shinylive)
- [ ] 3+ Visual Diagrams (Duration, VAN profile, Convexity, Annuity)
- [ ] All modules render via `quarto render` (exit 0)
- [ ] _freeze/ committed