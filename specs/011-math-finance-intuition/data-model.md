# Data Model: Mathematical Finance Intuition-First Pedagogy

**Feature**: 011-math-finance-intuition
**Date**: 2026-10-11
**Status**: Complete

---

## Entities

### 1. Module
Represents a course day file (Journée 1, 2, or 3).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Enum: "01", "02", "03" | Module identifier |
| `title` | String | Required | Display title (e.g., "Journée 1 — Calculer et comparer des flux financiers") |
| `file_path` | String | Required, pattern: `module-0{id}.qmd` | Source file path |
| `sequences` | List[Sequence] | Length = 5 (6 for Module 2) | Ordered list of major concept sections |

**Relationships**: Contains 5 Sequences (Séquences 2-6); Module 2 contains 6 (Séquences 2-7)

**Validation Rules**:
- File must exist at `fr/teaching/mathematical-finance/module-0{id}.qmd`
- Must render without errors via `quarto render`
- Must preserve all existing theory, examples, exercises (Constitution T-I)

---

### 2. Sequence
Represents a major concept section (Séquence 2-6 within a module; 2-7 for Module 2).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `number` | Integer | Enum: 2, 3, 4, 5, 6, 7 | Séquence number (7 only in Module 2) |
| `title` | String | Required | Section title (e.g., "Intérêts simples et composés") |
| `type` | String | Enum: "concept", "synthesis" | "concept" for Séquences 2-5 and Module 2 Séquence 6; "synthesis" for Séquence 6 (Module 1, 3) and Séquence 7 (Module 2) |
| `ladder_steps` | Integer | 7 if concept, 3 if synthesis | Number of abstraction ladder steps |
| `concrete_case` | ConcreteCase | Required | Opening narrative scenario |
| `formula_boxes` | List[FormulaBox] | Min 1 for concept type | Formulas introduced in this section |
| `erreur_frequente` | ErreurFrequente | Required if concept type | Metacognitive callout |
| `interactive_demo` | InteractiveDemo | Optional | Demo if priority concept |
| `visual_diagram` | VisualDiagram | Optional | Static diagram (Mermaid/ASCII) |
| `regle_or_reinforcement` | Boolean | Required | "Règle d'or" explicitly stated |

**Relationships**: Belongs to Module; contains FormulaBoxes, ConcreteCase, optional ErreurFrequente, InteractiveDemo, VisualDiagram

**Validation Rules**:
- **Concept type (Séquences 2-5, Module 2 Séquence 6)**: Must have all 7 ladder steps in order; must have concrete_case before first formula_box; must have erreur_frequente; must have regle_or_reinforcement = true
- **Synthesis type (Séquence 6; Module 2 Séquence 7)**: Must follow 3-step pattern (Situation → Application → Synthèse); exempt from erreur_frequente; regle_or_reinforcement = true
- ConcreteCase must appear before first FormulaBox in rendered order

---

### 3. ConcreteCase
Narrative financial scenario opening a concept section.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Required, unique | Identifier (e.g., "M1-S2-epargne") |
| `narrative` | String | Required, 3-8 sentences | Relatable financial story with specific numbers |
| `decision_question` | String | Required, ends with ? | The decision the student must reason about |
| `specific_numbers` | List[Number] | Min 2 | Concrete values used in the scenario |
| `sequence_id` | String | Required, FK to Sequence | Parent sequence |

**Validation Rules**:
- Must use business-relevant context (savings, investment, financing, not pure math)
- Numbers must be realistic (e.g., EUR amounts, realistic rates 1-10%)
- Decision question must be answerable intuitively before formula introduction
- Must be rendered as a distinct block (callout or headed section) before any formula

---

### 4. FormulaBox
Boxed mathematical formula with structured explanation.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Required, unique | Identifier (e.g., "van-formula") |
| `latex` | String | Required, valid LaTeX | Formula in `$$...$$` or `\boxed{...}` |
| `explanation` | Explanation | Required | 4-component structured explanation |
| `sequence_id` | String | Required, FK to Sequence | Parent sequence |
| `order` | Integer | Required, >=1 | Display order within sequence |

**Relationships**: Belongs to Sequence; has Explanation

**Validation Rules**:
- LaTeX must render without errors in Quarto
- Explanation must have all 4 components (see Explanation entity)
- Must be visually boxed (Quarto `::: {.callout-tip}` or similar per Constitution V)
- Must be indexed in formulaire.qmd

---

### 5. Explanation
Structured plain-language explanation for a FormulaBox (FR-003).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `what_it_computes` | String | Required, 1 sentence | Output meaning in business terms |
| `parameter_roles` | List[ParameterRole] | Required, min 1 | Role of each symbol |
| `result_meaning` | String | Required, 1 sentence | Business interpretation of result |
| `directional_intuition` | String | Required, 1 sentence | "Si X change, Y change comment" |

**Validation Rules**:
- All 4 fields non-empty
- `parameter_roles` covers every symbol in the formula
- Language: French, plain business language (no unnecessary jargon)
- Rendered as `.callout-note` block immediately after FormulaBox

---

### 6. ParameterRole
Role description for a single formula parameter.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `symbol` | String | Required | LaTeX symbol (e.g., `k`, `CF_t`) |
| `role` | String | Required, 1 sentence | Economic role (e.g., "taux d'actualisation = coût du capital") |

---

### 7. ErreurFrequente
Metacognitive callout contrasting intuitive error vs correct reasoning (FR-006).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Required, unique | Identifier |
| `trap_intuition` | String | Required | The seemingly logical but wrong reasoning |
| `why_wrong` | String | Required | Technical reason the intuition fails |
| `correct_reasoning` | String | Required | The correct approach |
| `memo_tip` | String | Required, 1 sentence | Memory aid / rule of thumb |
| `sequence_id` | String | Required, FK to Sequence | Parent sequence (concept type only) |

**Validation Rules**:
- Only required for Sequence.type = "concept" (Séquences 2-5)
- Rendered as `.callout-warning` block (Constitution V: "Remarks, caveats, common mistakes")
- All 4 components present and non-empty
- `memo_tip` must be actionable and memorable

---

### 8. InteractiveDemo
Parameter exploration widget (FR-009, Constitution T-IV).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Required, unique | Identifier |
| `title` | String | Required | Display title |
| `technology` | String | Enum: "OJS", "Shinylive" | Implementation technology |
| `concepts` | List[String] | Required | Concepts demonstrated (e.g., ["VAN", "TRI"]) |
| `sequence_id` | String | Required, FK to Sequence | Parent sequence |
| `justification` | String | Required | T-IV rationale for technology choice |

**Validation Rules**:
- Technology must match computational need per research.md R2:
  - OJS: pure arithmetic, real-time sliders, curve plotting
  - Shinylive: root-finding, scenario loops, statistical computation
- Must be embedded as `{ojs}` or `{shinylive-python}` code block
- Must load and respond in browser without errors
- Justification must reference Constitution T-IV explicitly

---

### 9. VisualDiagram
Static geometric/visual intuition aid (FR-004, Constitution T-VII).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Required, unique | Identifier |
| `type` | String | Enum: "mermaid", "ascii", "image" | Diagram format |
| `concept` | String | Required | Concept illustrated (e.g., "Duration timeline") |
| `sequence_id` | String | Required, FK to Sequence | Parent sequence |
| `description` | String | Required | Alt text / description |

**Validation Rules**:
- Required for: Duration (weighted timeline), VAN profile (area under curve), Convexity (curvature), Annuity timeline
- Mermaid preferred for timelines; ASCII acceptable for simple structures
- Must render in Quarto HTML output

---

### 10. GlossaryEntry
Symbol definition with standardized intuition template (FR-007, Constitution T-V).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `symbol` | String | Required, unique | LaTeX symbol (e.g., `$VAN$`, `$D_M$`) |
| `name` | String | Required | Display name (e.g., "Valeur Actuelle Nette") |
| `definition` | String | Required | Formal definition |
| `pronunciation` | String | Required | Pronunciation guide (e.g., "V-A-N") |
| `modules` | List[String] | Required | Modules where introduced (e.g., ["03"]) |
| `intuition` | Intuition | Required | 3-field intuition template |

**Relationships**: Has Intuition

**Validation Rules**:
- All 47+ symbols from current glossaire.qmd must have entries
- Intuition must have all 3 fields (see Intuition entity)
- Must be sorted alphabetically by symbol in glossaire.qmd
- Linked from module sidebars (already done)

---

### 11. Intuition
Standardized 3-field economic intuition for GlossaryEntry (Clarification #5).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `ce_que_ca_represente` | String | Required, 1 sentence | Plain-language concept description |
| `pourquoi_ca_importe` | String | Required, 1 sentence | Business/decision relevance |
| `intuition_cle` | String | Required, 1 sentence | Directional insight or analogy |

**Validation Rules**:
- All 3 fields non-empty, max 1 sentence each
- French language, plain business vocabulary
- No LaTeX in intuition fields (plain text only)

---

### 12. FormulaireEntry
Formula reference with intuition reminder (FR-008).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | String | Required, unique | Identifier (1-10) |
| `latex` | String | Required | Formula in boxed LaTeX |
| `description` | String | Required | Current description/table |
| `intuition_reminder` | String | Required, 1 sentence | One-sentence intuition hook |
| `symbols` | List[String] | Required | Symbols used in formula |

**Validation Rules**:
- All 10 formulas from current formulaire.qmd must have entries
- `intuition_reminder` follows pattern: "Cette formule répond à : [question concrète] ?"
- Must be placed immediately after formula box in formulaire.qmd

---

### 13. PedagogicalContract
Internal contract defining required section structure (contracts/pedagogical-contract.md).

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `concept_section_template` | OrderedList[Step] | 7 steps fixed | Required structure for Séquences 2-5 |
| `synthesis_section_template` | OrderedList[Step] | 3 steps fixed | Required structure for Séquence 6 |
| `required_callouts` | Map[SectionType, List[CalloutType]] | Fixed | Callout types per section type |

**Concept Section Template (7 steps)**:
1. `ConcreteCase` — "Situation concrète" / "Cas réel" block
2. `NumericalExploration` — Table or step-by-step calculation with specific numbers
3. `PatternRecognition` — "Observez le schéma" / "Remarquez le pattern" prompt
4. `FormulaBox` — Boxed formula with Explanation
5. `FormalDefinition` — Precise mathematical definition
6. `WorkedExample` — Application of formula to new numbers
7. `EconomicInterpretation` — `.callout-note` or `.callout-tip` with business meaning

**Synthesis Section Template (3 steps)**:
1. `Situation` — Full scenario context (recap or new)
2. `Application` — Step-by-step application of prior concepts
3. `Synthese` — Decision framework / recommendation template

**Required Callouts**:
- Concept: `.callout-note` (intuition), `.callout-tip` (formula), `.callout-warning` (erreur fréquente), `.callout-important` (règle d'or)
- Synthesis: `.callout-note` (context), `.callout-important` (decision framework)

---

## State Transitions

### Module Rendering Pipeline
```
Source (.qmd) 
  → Quarto Parse 
  → Execute (Python/OJS) 
  → Freeze Cache (_freeze/) 
  → Render HTML (docs/) 
  → Validate (grep checks)
```

### Content Update Flow
```
Edit .qmd 
  → Local preview (quarto preview) 
  → Render (quarto render) 
  → Validate structural checks 
  → Commit (source + _freeze/ + docs/)
```

---

## Summary Counts (Target State)

| Entity | Target Count | Source |
|--------|--------------|--------|
| Module | 3 | Existing |
| Sequence (concept) | 13 | M1 S2-S5 (4) + M2 S2-S6 (5) + M3 S2-S5 (4) |
| Sequence (synthesis) | 3 | M1 S6, M2 S7, M3 S6 |
| ConcreteCase | 13 | 1 per concept sequence |
| FormulaBox | ~30 | ~10 per module (estimate) |
| Explanation | ~30 | 1 per FormulaBox |
| ErreurFrequente | 13 | 1 per concept sequence |
| InteractiveDemo | 4 | FR-009 (2 OJS, 2 Shinylive) |
| VisualDiagram | 3+ | Duration, VAN profile, Convexity, Annuity |
| GlossaryEntry | 47+ | Current glossaire.qmd count |
| Intuition | 47+ | 1 per GlossaryEntry |
| FormulaireEntry | 10 | Current formulaire.qmd count |