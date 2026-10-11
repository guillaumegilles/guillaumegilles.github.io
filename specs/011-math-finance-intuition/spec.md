# Feature Specification: Mathematical Finance Intuition-First Pedagogy

**Feature Branch**: `011-math-finance-intuition`

**Created**: 2026-10-11

**Status**: Draft

**Input**: User description: "work on mathematical-finance to improve mathematical intuition of students. I am thinking of building intuition and understanding starting with concrete example then to move to mathematical notation. The starting point of each section should be a real case, and you slowly move to abstract realm and mathematical notation. Don't forget to add clear explanation."

---

## User Scenarios & Testing

### User Story 1 - Student Encounters New Concept Through Concrete Scenario (Priority: P1)

A Master 1 business school student opens a course module (e.g., "Capitalisation et Actualisation") and immediately encounters a relatable real-world situation -- such as choosing between receiving 1,000 EUR today vs. 1,100 EUR in one year -- before any formula is introduced. The student works through the decision intuitively, discovers the need for a comparison tool, and only then is the mathematical notation (capitalisation formula) presented as the formalisation of their reasoning.

**Why this priority**: This is the core pedagogical shift -- reversing the traditional "formula-first" order to "intuition-first." It directly addresses the user's request to start with concrete cases.

**Independent Test**: Can be tested by reviewing any module file and verifying that each major concept section begins with a "Situation concrète" or "Cas réel" block before the first formula appears.

**Acceptance Scenarios**:

1. **Given** a student opens Module 1 (Séquence 2: Intérêts simples et composés), **When** they read the opening of the section, **Then** they encounter a concrete financial decision scenario (e.g., savings account vs. term deposit) before seeing the formulas for simple and compound interest.
2. **Given** a student opens Module 3 (Séquence 2: VAN), **When** they read the opening, **Then** they encounter a realistic investment decision (e.g., "Should we buy this machine?") with concrete cash flows before the VAN formula is introduced.

---

### User Story 2 - Progressive Abstraction Ladder Within Each Section (Priority: P1)

Within each major concept section, the student experiences a clear progression: (1) Concrete narrative case -> (2) Numerical exploration with specific numbers -> (3) Pattern recognition / generalisation -> (4) Mathematical notation and formula -> (5) Formal definition -> (6) Worked example applying the formula -> (7) Intuition check / economic interpretation.

**Why this priority**: Ensures the "slowly move to abstract realm" requirement is structurally embedded, not just a one-time opening hook.

**Independent Test**: Can be tested by selecting any concept section (e.g., "Annuités constantes", "Duration", "TRI") and verifying the 7-step ladder exists in sequence.

**Acceptance Scenarios**:

1. **Given** the "Annuités constantes" section in Module 1, **When** a student reads it top-to-bottom, **Then** they encounter: a concrete savings goal story -> a numerical table showing year-by-year accumulation -> a "notice the pattern" prompt -> the general formula box -> the formal definition -> a worked example -> an economic interpretation callout.
2. **Given** the "Duration de Macaulay" section in Module 2, **When** a student reads it, **Then** they encounter: a bondholder's dilemma (when do I really get my money back?) -> a weighted-average timeline visual -> the general formula -> interpretation as "economic maturity."

---

### User Story 3 - Clear Explanations Accompany Every Formula (Priority: P2)

Every formula box is immediately followed by a plain-language explanation that answers: "What does this compute?", "Why does each term appear?", "What does the result mean in business terms?", and "What would happen if [key parameter] changed?"

**Why this priority**: The user explicitly requested "clear explanation" and the constitution (T-III) requires "every formula MUST be accompanied by a plain-language explanation of what it computes and why it matters."

**Independent Test**: Can be tested by checking each formula box in all three modules for the presence of a structured explanation block immediately after.

**Acceptance Scenarios**:

1. **Given** the VAN formula box in Module 3, **When** a student reads the following explanation, **Then** they find: a sentence stating "Cette formule calcule la valeur nette créée aujourd'hui par le projet", a bullet list explaining each symbol's economic role, and a "Si le taux k augmente..." intuition check.
2. **Given** the bond pricing formula in Module 2, **When** a student reads the explanation, **Then** they find a decomposition showing "Prix = Valeur actuelle des coupons + Valeur actuelle du nominal" with economic meaning for each component.

---

### User Story 4 - Visual/Geometric Intuition for Key Concepts (Priority: P2)

Concepts with geometric interpretations (duration as weighted average timeline, VAN as area under curve, convexity as curvature) include visual diagrams or interactive demonstrations that make the abstraction tangible.

**Why this priority**: Aligns with constitution principle T-VII (Visual and Geometric Intuition) and reinforces the concrete-to-abstract progression.

**Independent Test**: Can be tested by verifying that duration, VAN profile, and convexity sections include either a static diagram (Mermaid/ASCII timeline) or a Shinylive/OJS interactive demo.

**Acceptance Scenarios**:

1. **Given** the Duration section in Module 2, **When** a student views it, **Then** they see a timeline diagram showing cash flows as weighted blocks whose center of gravity represents Macaulay duration.
2. **Given** the VAN vs. taux graph in Module 3, **When** a student interacts with the demo, **Then** they can slide the discount rate and see the VAN curve cross zero at the TRI.

---

### User Story 5 - Consistent Pedagogical Structure Across All Three Modules (Priority: P3)

All three modules (Journée 1, 2, 3) follow the same "concrete -> numerical -> pattern -> formula -> definition -> example -> interpretation" template, so students build a reliable mental model of how to learn financial mathematics.

**Why this priority**: Consistency reduces cognitive load and makes the pedagogy itself a transferable skill.

**Independent Test**: Can be tested by comparing the structure of equivalent concept sections across modules (e.g., "Capitalisation" in M1 vs "Valorisation obligation" in M2 vs "VAN" in M3) and verifying parallel structure.

**Acceptance Scenarios**:

1. **Given** the three module files, **When** an auditor compares the section templates, **Then** they find a consistent sequence of callout types and heading patterns marking each rung of the abstraction ladder.

---

## Requirements

### Functional Requirements

- **FR-001**: Each major concept section in all three modules MUST begin with a "Situation concrète" or "Cas réel" narrative block presenting a relatable financial decision or scenario before any mathematical notation appears.
- **FR-002**: Each major concept section MUST follow a 7-step abstraction ladder: (1) Concrete case -> (2) Numerical exploration -> (3) Pattern recognition -> (4) Formula box -> (5) Formal definition -> (6) Worked example -> (7) Economic interpretation. **Exception**: Sequence 6 in each module (Cas pratique / Cas integrateur) follows a 3-step "Situation -> Application -> Synthese" pattern instead.
- **FR-003**: Every formula box MUST be immediately followed by a structured "Explication en langage clair" block covering: what it computes, role of each parameter, economic meaning of the result, and directional intuition (what happens if key variable changes).
- **FR-004**: Key concepts with geometric interpretations (Duration, VAN profile, Convexity, Annuity timeline) MUST include a visual diagram (Mermaid timeline, ASCII art, or static image) or an interactive Shinylive/OJS demonstration.
- **FR-005**: The "Règle d'or — La ligne du temps avant toute formule" principle (already present in Module 1) MUST be explicitly reinforced at the start of every module and before every major calculation section.
- **FR-006**: Each module MUST include at least one "Erreur fréquente" callout per major concept that contrasts the intuitive wrong answer with the correct reasoning, building metacognitive awareness. **Exception**: Synthesis sections (Séquence 6 in each module) are exempt from this requirement.
- **FR-007**: The glossary (glossaire.qmd) MUST be updated to include "Intuition économique" entries for each symbol using a standardized 3-field template: (1) **Ce que ça représente** (1 sentence), (2) **Pourquoi ça importe** (1 sentence, business context), (3) **Intuition clé** (1 sentence, directional or analogy). This applies to all 47+ symbols in the glossary.
- **FR-008**: The formulaire (formulaire.qmd) MUST be updated to include a one-sentence intuition reminder next to each formula (e.g., "Cette formule répond à : combien vaudra mon capital dans n périodes si je le place à i % ?").
- **FR-009**: Interactive demonstrations MUST be added for at least: capitalisation vs actualisation (M1) -- OJS; bond price-yield relationship (M2) -- OJS; VAN-TRI profile (M3) -- Shinylive; sensitivity analysis (M3) -- Shinylive. Technology choice justified per constitution T-IV: OJS for pure arithmetic; Shinylive for root-finding and scenario loops.
- **FR-010**: All changes MUST preserve existing canonical theory, worked examples, and exercises (Constitution T-I: Content Fidelity).

### Key Entities

- **Module**: A course day file (module-01.qmd, module-02.qmd, module-03.qmd) containing multiple concept sequences.
- **Concept Section**: A major topic within a module (e.g., "Intérêts composés", "VAN", "Duration") that must follow the abstraction ladder.
- **Formula Box**: A boxed mathematical formula with accompanying plain-language explanation.
- **Concrete Case**: A narrative financial scenario with specific numbers and a decision question.
- **Abstraction Ladder**: The 7-step pedagogical sequence from concrete to formal.
- **Glossary Entry**: A symbol definition including notation, formal definition, pronunciation, and economic intuition.
- **Interactive Demo**: A Shinylive-Python or OJS block enabling parameter exploration.

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: 100% of major concept sections across all three modules begin with a concrete case before any formula (verifiable by automated grep for "Situation concrète" or "Cas réel" preceding first formula box in each section).
- **SC-002**: 100% of formula boxes have an immediately following "Explication en langage clair" block with all four required components (what, parameters, meaning, directional intuition).
- **SC-003**: At least 4 new interactive demonstrations added (capitalisation/actualisation, bond price-yield, VAN-TRI, sensitivity) -- verifiable by counting `{shinylive-python}` or `{ojs}` blocks in the three modules.
- **SC-004**: Student feedback (post-course survey) shows >= 80% agreement with "The concrete examples helped me understand why the formulas work" (qualitative, measured next course delivery).
- **SC-005**: Time-to-first-correct-application on exercises decreases by >= 15% compared to previous cohort (quantitative, measured next course delivery).
- **SC-006**: All three modules render without errors via `quarto render` (technical validation).
- **SC-007**: Glossary and formulaire are updated and linked from module sidebars (structural completeness).

---

## Assumptions

- **Target audience**: Master 1 business school students with Licence-level math and basic Excel -- no advanced calculus or stochastic processes background.
- **Course scope**: 18 hours total (3 x 6h days), 35% theory, 30% exercises, 25% cases, 10% assessment -- no change to time allocation.
- **Language**: French (primary language of instruction for this course); English stubs may be added later per bilingual strategy (Constitution VI).
- **Technology**: Quarto with Shinylive extension for interactive demos; Mermaid for static diagrams; no new runtime dependencies.
- **Existing content fidelity**: All current theory, examples, exercises, and solutions must be preserved (Constitution T-I).
- **Sidebar/navigation**: No changes to `_quarto.yml` structure needed; only content within existing module files.
- **Freeze cache**: `_freeze/` will be updated as part of the render; must be committed alongside source changes.

---

## Clarifications

### Session 2026-10-11

- Q: What precisely counts as a "major concept section" in each module? -> A: Use existing Séquence headings in each module as the canonical list (Option A).
- Q: Should the 7-step ladder apply rigidly to all 15 sections, including synthesis cases? -> A: Full ladder for 13 concept-introduction sections (Séquences 2-5); Séquence 6 (cas pratique / cas intégrateur) uses lighter 3-step pattern (Option B).
- Q: Should synthesis sections (Séquence 6) also require "Erreur fréquente" callouts per FR-006? -> A: Only the 13 concept-introduction sections (Séquences 2-5) require "Erreur fréquente"; synthesis sections exempt (Option B).
- Q: For the 4 required interactive demos (FR-009), should they all use Shinylive, all OJS, or a mix? -> A: Mix by computational need: Shinylive for VAN-TRI and sensitivity (need root-finding, loops); OJS for capitalisation/actualisation and bond price-yield (simple arithmetic) (Option C).
- Q: What structure should each "Intuition économique" glossary entry follow for consistency? -> A: Standardized 3-field template per symbol: (1) Ce que ça représente, (2) Pourquoi ça importe, (3) Intuition clé (Option A).

## Edge Cases

- **Highly abstract concepts** (e.g., convexity, modified duration): May require two concrete cases -- one for the base concept (duration as weighted average time) and a second for the extension (convexity as curvature correction).
- **Formula-heavy sections** (e.g., amortisation table): The abstraction ladder may compress steps 2-3 into a single "construction numérique" table that simultaneously shows numbers and reveals pattern.
- **Backward compatibility**: Students who prefer formula-first reading must still be able to locate formulas quickly -- formula boxes remain visually prominent and indexed in formulaire.
- **Translation parity**: French content changes will require eventual English mirror updates (Constitution VI), but English stubs can be created in a follow-up.

---

**Definition: Major Concept Section**

A "major concept section" is defined as each top-level **Séquence** heading in the three module files (module-01.qmd, module-02.qmd, module-03.qmd). Based on current structure:

| Module | Séquences (Major Concept Sections) | Count |
|--------|-------------------------------------|-------|
| Module 1 (Journée 1) | Séquence 2: Intérêts simples et composés; Séquence 3: Actualisation et équivalence; Séquence 4: Taux proportionnels et équivalents; Séquence 5: Annuités constantes; Séquence 6: Cas pratique -- constituer un capital | 5 |
| Module 2 (Journée 2) | Séquence 2: Emprunt amortissable; Séquence 3: Autres modalités; Séquence 4: Coût réel du crédit; Séquence 5: Introduction aux obligations; Séquence 6: Sensibilité obligataire; Séquence 7: Étude de cas -- choisir un financement | 6 |
| Module 3 (Journée 3) | Séquence 2: VAN; Séquence 3: TRI; Séquence 4: Délai de récupération; Séquence 5: Analyse du risque; Séquence 6: Cas intégrateur | 5 |
| **Total** | | **16** |

**Classification (resolved during task generation)**: Module 2's Séquence 6
(*Sensibilité obligataire*) introduces new concepts (duration, convexity) and
US2 scenario 2 requires a full ladder for Duration, so it is a **concept**
section. Module 2's case study is Séquence 7, which is its **synthesis**
section. This yields:

- **13 concept sections** (7-step ladder + Erreur fréquente): M1 S2-S5,
  M2 S2-S6, M3 S2-S5.
- **3 synthesis sections** (3-step pattern, no Erreur fréquente): M1 S6,
  M2 S7, M3 S6.

Wherever this spec says "Séquence 6 (synthesis)", read "the synthesis
section of the module" (Séquence 7 for Module 2).

Requirements FR-001, FR-002, FR-006 and Success Criteria SC-001, SC-002 apply to these 16 sections.