# Research: Mathematical Finance Intuition-First Pedagogy

**Feature**: 011-math-finance-intuition
**Date**: 2026-10-11
**Status**: Complete

---

## R1: Concrete-to-Abstract Pedagogy in Financial Mathematics

**Decision**: Adopt a 7-step "abstraction ladder" for concept-introduction sections, with a 3-step variant for synthesis sections.

**Rationale**: 
- Literature on STEM pedagogy (e.g., Schwartz & Bransford "A Time for Telling", 1998; Kapur "Productive Failure", 2008) shows that presenting concrete cases before formal notation improves conceptual understanding and transfer.
- Financial mathematics education research (e.g., Vercruysse & Van den Noortgate, 2020) confirms that business students struggle with abstract formulas when not grounded in decision contexts.
- The 7-step ladder mirrors the "concreteness fading" framework (Fyfe et al., 2014): concrete → idealized concrete → abstract.
- Synthesis sections (cas pratique, cas intégrateur) serve a different purpose — integration and application — so a lighter 3-step pattern (Situation → Application → Synthèse) avoids artificial structure.

**Alternatives Considered**:
- Pure problem-based learning (PBL): Rejected — too time-intensive for 18-hour course; requires facilitator expertise not guaranteed.
- Worked-example only: Rejected — doesn't build the "discovery" intuition the user requested.
- Flipped classroom with pre-reading: Rejected — assumes student preparation compliance; not controllable.

---

## R2: OJS vs Shinylive Technology Choice per Demo

**Decision**: Mixed approach per constitutional principle T-IV (justify by computational need).

| Demo | Concepts | Computational Need | Technology | Justification |
|------|----------|-------------------|------------|---------------|
| Capitalisation vs Actualisation | V_n = V_0(1+i)^n, V_0 = V_n/(1+i)^n | Pure arithmetic, real-time slider response | **OJS** | Simple exponentiation; smooth 60fps sliders; no Python runtime; <50KB payload |
| Bond Price-Yield | P = C·[1-(1+r)^-n]/r + N/(1+r)^n | Pure arithmetic, curve plotting | **OJS** | Polynomial evaluation; real-time curve update; lightweight |
| VAN-TRI Profile | VAN(k) curve, root-finding for TRI | Numerical root-finding (bisection/Newton), curve plotting | **Shinylive** | Requires iterative solver; Python's `scipy.optimize` or custom bisection; heavier but necessary |
| Sensitivity Analysis | Scenario loops, tornado charts | Multi-scenario iteration, data aggregation | **Shinylive** | Requires looping over parameter grids; Python pandas/numpy natural fit |

**Rationale**: 
- Constitution T-IV explicitly requires: "use Shinylive when the simulation requires Python libraries; use OJS when the simulation is computable in pure JavaScript."
- OJS demos load instantly, work offline after first load, and have zero cold-start latency.
- Shinylive demos have ~2-3s cold start (Pyodide load) but provide full Python scientific stack.
- Mixed approach optimizes student experience: instant feedback for exploration demos, computational power for analysis demos.

**Alternatives Considered**:
- All Shinylive: Rejected — unnecessary payload for simple arithmetic; violates T-IV "justify by computational need."
- All OJS: Rejected — root-finding and scenario loops awkward in pure JS; would require implementing numerical methods from scratch.
- Pure static images: Rejected — violates T-IV requirement for interactive demos on priority concepts.

---

## R3: "Intuition économique" Glossary Template

**Decision**: Standardized 3-field template for all 47+ symbols.

**Template**:
```markdown
### `SYMBOL` — Name

**Ce que ça représente**: [1 sentence: plain-language description of the concept]

**Pourquoi ça importe**: [1 sentence: business/decision context — why a manager cares]

**Intuition clé**: [1 sentence: directional insight, analogy, or "what happens if..."]
```

**Example** (for `VAN`):
```markdown
### `VAN` — Valeur Actuelle Nette

**Ce que ça représente**: La valeur nette créée aujourd'hui par un projet, après avoir actualisé tous ses flux futurs au coût du capital.

**Pourquoi ça importe**: C'est le critère de décision n°1 : un projet à VAN positive enrichit les actionnaires ; un projet à VAN négative les appauvrit.

**Intuition clé**: Si le taux d'actualisation k augmente, la VAN diminue (les flux futurs valent moins aujourd'hui) — la VAN est une fonction décroissante de k.
```

**Rationale**: 
- Three fields map to cognitive levels: definition (what), relevance (why), mental model (how).
- One-sentence constraint forces clarity and scannability.
- Uniform structure enables students to build a reliable "lookup reflex" — they know exactly where to find each type of insight.
- Testable: automated check can verify all 3 fields present per symbol.

**Alternatives Considered**:
- Free-form paragraphs: Rejected — inconsistent depth, hard to scan, not testable.
- Two-tier (core vs derived): Rejected — adds complexity; all symbols benefit from intuition.
- Cross-reference only: Rejected — glossary should be standalone reference per Constitution T-V.

---

## R4: "Explication en langage clair" Formula Template

**Decision**: 4-component structure for every formula box.

**Template**:
```markdown
::: {.callout-note}
## Explication en langage clair

**Ce que calcule cette formule**: [1 sentence — output meaning]

**Rôle de chaque paramètre**:
- `SYMBOL`: [plain-language role]
- `SYMBOL`: [plain-language role]

**Ce que signifie le résultat**: [business interpretation — e.g., "valeur nette créée", "coût réel du crédit"]

**Intuition directionnelle**: [what happens if key variable changes — e.g., "Si k augmente, VAN diminue"]
:::
```

**Example** (for VAN formula):
```markdown
::: {.callout-note}
## Explication en langage clair

**Ce que calcule cette formule**: La valeur actuelle nette — l'enrichissement net (en euros d'aujourd'hui) généré par le projet.

**Rôle de chaque paramètre**:
- `I_0`: Investissement initial (sortie de trésorerie à t=0, donc négatif dans la formule)
- `CF_t`: Flux de trésorerie nets de la période t (entrées positives, sorties négatives)
- `k`: Taux d'actualisation (coût du capital ou rendement minimum exigé)

**Ce que signifie le résultat**: VAN > 0 = le projet crée de la valeur ; VAN < 0 = le projet détruit de la valeur ; VAN = 0 = indifférence.

**Intuition directionnelle**: Si le taux k augmente, les flux futurs sont plus fortement actualisés → VAN diminue. Si les flux CF_t augmentent, VAN augmente proportionnellement.
:::
```

**Rationale**: 
- Directly addresses Constitution T-III: "every formula MUST be accompanied by a plain-language explanation of what it computes and why it matters."
- Four components cover: output semantics, input semantics, business meaning, and sensitivity — the complete mental model.
- Callout format (`.callout-note`) consistent with existing site conventions (Constitution V).
- Testable: grep can verify presence and structure.

**Alternatives Considered**:
- Inline prose after formula: Rejected — visually indistinct; students skip it.
- Margin notes: Rejected — not portable across render formats (HTML/PDF).
- Video explanations: Rejected — maintenance burden; not searchable; violates privacy (no external hosting).

---

## R5: "Erreur fréquente" Callout Pattern

**Decision**: Standardized `.callout-warning` pattern contrasting intuitive error vs correct reasoning.

**Template**:
```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège**: [The seemingly logical but wrong reasoning students naturally make]

**Pourquoi c'est faux**: [The technical/mathematical reason the intuition fails]

**Le bon raisonnement**: [The correct approach, linked to the formula/concept]

**Astuce mémo**: [One-sentence memory aid or rule of thumb]
:::
```

**Example** (for VAN vs TRI):
```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège**: "Le TRI est le rendement du projet, donc si TRI > k, le projet est bon — pas besoin de regarder la VAN."

**Pourquoi c'est faux**: Le TRI suppose qu'on réinvestit les flux au TRI lui-même, ce qui est rarement réaliste. La VAN actualise au coût du capital k, qui reflète le vrai coût d'opportunité.

**Le bon raisonnement**: Toujours décider sur la VAN. Le TRI est un indicateur complémentaire, pas un substitut. En cas de conflit (projets mutuellement exclusifs), la VAN tranche.

**Astuce mémo**: "VAN pour décider, TRI pour communiquer."
:::
```

**Rationale**: 
- Metacognitive awareness (knowing what you don't know) is a key learning outcome for business students (Constitution: "repérer les limites d'un modèle quantitatif").
- Contrast structure (trap → why wrong → correct → memo) mirrors "refutation text" pedagogy shown effective for conceptual change (Guzzetti et al., 1993).
- `.callout-warning` semantic matches "caveats, common mistakes" per Constitution V.
- Exempt for synthesis sections (Séquence 6) per Clarification #3 — avoids forced errors in application contexts.

**Alternatives Considered**:
- Inline "Attention:" paragraphs: Rejected — visually weak; students don't notice.
- Separate "Erreurs" appendix: Rejected — disconnected from learning moment; low reference rate.
- Quiz questions: Rejected — assessment format, not learning scaffold.

---

## R6: Gap Analysis — Current vs Target Structure

**Method**: Reviewed all 3 module files against the 15 major concept sections (5 per module).

### Module 1 (Journée 1) — Current State

| Séquence | Title | Current Opening | Has Formula Explanations? | Has Erreur Fréquente? | Has Visual/Demo? | Gap |
|----------|-------|-----------------|---------------------------|----------------------|------------------|-----|
| 2 | Intérêts simples et composés | "Intuition économique" (generic) | Partial (some formulas) | No | Shinylive (capitalisation vs actualisation) | Needs concrete case rewrite; add formula explanations; add erreur fréquente |
| 3 | Actualisation et équivalence | "Intuition économique" (generic) | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; add demo? |
| 4 | Taux proportionnels et équivalents | "Intuition économique" (generic) | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente |
| 5 | Annuités constantes | "Intuition économique" + "Règle d'or" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; timeline visual |
| 6 | Cas pratique | Situation (concrete) | N/A (application) | N/A (exempt) | None | Convert to 3-step pattern; add synthesis structure |

### Module 2 (Journée 2) — Current State

| Séquence | Title | Current Opening | Has Formula Explanations? | Has Erreur Fréquente? | Has Visual/Demo? | Gap |
|----------|-------|-----------------|---------------------------|----------------------|------------------|-----|
| 2 | Emprunt amortissable | "Intuition économique" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; timeline visual |
| 3 | Autres modalités | "Intuition économique" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente |
| 4 | Coût réel du crédit | "A. Limite du taux nominal" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente |
| 5 | Introduction aux obligations | "A. Vocabulaire obligataire" | Partial | No | Shinylive (prix-taux) | Needs concrete case; formula explanations; erreur fréquente; demo exists ✓ |
| 6 | Sensibilité obligataire | "A. Duration de Macaulay" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; duration timeline visual |

### Module 3 (Journée 3) — Current State

| Séquence | Title | Current Opening | Has Formula Explanations? | Has Erreur Fréquente? | Has Visual/Demo? | Gap |
|----------|-------|-----------------|---------------------------|----------------------|------------------|-----|
| 2 | VAN | "Formule et règle de décision" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; VAN-TRI demo |
| 3 | TRI | "Définition" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; VAN-TRI demo |
| 4 | Délai de récupération | "A. DRS" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente |
| 5 | Analyse du risque | "A. Analyse de sensibilité" | Partial | No | None | Needs concrete case; formula explanations; erreur fréquente; sensitivity demo |
| 6 | Cas intégrateur | "Contexte" (concrete) | N/A (application) | N/A (exempt) | None | Convert to 3-step pattern; add synthesis structure |

**Summary of Work Required**:
- **Concrete case openings**: 13 sections need rewrite (all Séquences 2-5)
- **Formula explanations**: ~30 formula boxes need 4-component explanations added
- **Erreur fréquente**: 13 new callouts needed (Séquences 2-5 only)
- **Visual/Demo**: 4 new demos (2 OJS, 2 Shinylive); 3 static diagrams (Duration timeline, Annuity timeline, Convexity)
- **Glossaire**: 47+ symbols need 3-field intuition template
- **Formulaire**: 10 formulas need 1-sentence intuition reminders
- **Règle d'or reinforcement**: Add at start of each module + before each major calculation section

---

## Consolidated Decisions

| Area | Decision | Reference |
|------|----------|-----------|
| Major concept section definition | 15 Séquences (5 per module) | Clarification #1 |
| Abstraction ladder | 7-step for Séquences 2-5; 3-step for Séquence 6 | Clarification #2 |
| Erreur fréquente scope | 13 concept sections only | Clarification #3 |
| Interactive demo tech | 2 OJS + 2 Shinylive (by computational need) | Clarification #4 |
| Glossary intuition template | 3-field standardized | Clarification #5 |
| Formula explanation template | 4-component in .callout-note | R4 |
| Erreur fréquente template | 4-part in .callout-warning | R5 |
| Concrete case pattern | Narrative + decision question + specific numbers | R1, Spec FR-001 |