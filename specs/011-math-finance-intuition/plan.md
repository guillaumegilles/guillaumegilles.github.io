# Implementation Plan: Mathematical Finance Intuition-First Pedagogy

**Branch**: `011-math-finance-intuition` | **Date**: 2026-10-11 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/011-math-finance-intuition/spec.md`

## Summary

Transform the existing 3-module Mathematical Finance course (18 hours, Master 1 level) from a traditional "formula-first" pedagogy to an "intuition-first" approach. Each of the 15 major concept sections (5 per module, defined by Séquence headings) will be restructured to follow a concrete-to-abstract progression: concrete financial scenario → numerical exploration → pattern recognition → formula → definition → worked example → economic interpretation. Key deliverables: (1) 13 concept sections get full 7-step ladder; 3 synthesis sections get 3-step pattern; (2) every formula box gets a 4-component plain-language explanation; (3) 4 new interactive demos (2 OJS, 2 Shinylive); (4) glossary updated with 47+ standardized "Intuition économique" entries (3-field template); (5) formulaire updated with one-sentence intuition reminders; (6) "Erreur fréquente" callouts added to 13 concept sections; (7) "Règle d'or" timeline principle reinforced throughout. All changes preserve existing canonical content (Constitution T-I).

## Technical Context

**Language/Version**: Quarto Markdown (.qmd) with embedded LaTeX math; Shinylive Python (for interactive demos requiring root-finding/loops); Observable JS (OJS) for pure arithmetic demos; Mermaid for static diagrams

**Primary Dependencies**: Quarto (core), quarto-ext/shinylive (Shinylive extension), Observable JS runtime (via CDN), Mermaid.js (via Quarto)

**Storage**: File-based (`.qmd` source files in `fr/teaching/mathematical-finance/`); rendered HTML in `docs/`; computational cache in `_freeze/`

**Testing**: `quarto render` (must exit 0 for all 3 modules); visual inspection of rendered HTML; manual verification of interactive demos; grep-based validation of structural requirements (concrete case openings, formula explanations, callout patterns)

**Target Platform**: Static site served via GitHub Pages (`docs/` directory); no server-side logic

**Project Type**: Educational content / static site (teaching materials)

**Performance Goals**: Page load < 3s on 3G; interactive demo response < 500ms for OJS, < 2s for Shinylive (cold start); `quarto render` completes in < 60s for all 3 modules

**Constraints**: 
- No new runtime dependencies beyond existing Quarto/Shinylive/OJS/Mermaid stack
- Must preserve all existing theory, examples, exercises (Constitution T-I)
- French language only for this iteration (English stubs deferred per Constitution VI)
- No changes to `_quarto.yml` sidebar structure
- `_freeze/` cache must be committed alongside source changes
- Line width: prose wrapped at 80 chars in `.qmd` files

**Scale/Scope**: 
- 3 module files (~2,000 lines each)
- 15 major concept sections (5 per module)
- ~47 glossary symbols to update
- 10 formulas in formulaire to annotate
- 4 new interactive demos
- ~13 "Erreur fréquente" callouts to add
- ~13 "Règle d'or" reinforcements

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify the following before proceeding:

- [x] **I. Content-First** — All new pages are backed by `.qmd` source files; no direct HTML in `docs/`. (Only modifying existing `.qmd` files)
- [x] **II. Navigation registered** — Every new teaching page is listed in the correct `website.sidebar` block in `_quarto.yml`. (No new pages; only modifying existing module files already registered)
- [x] **III. Reproducible** — `_freeze/` entries are committed; any deleted freeze entries are intentional. (Will commit updated `_freeze/` after render)
- [x] **IV. Privacy-First** — No tracking scripts, cookies, or fingerprinting introduced by this feature. (Shinylive/OJS/Mermaid are privacy-safe; no analytics added)
- [x] **V. Styling contained** — All CSS/SCSS changes are in `assets/dark.scss`; no inline styles; no `<style>` blocks. (No styling changes planned; using native Quarto callouts)
- [x] **VI. Bilingual parity** — Every new page has both an EN and FR `.qmd` counterpart. Untranslated pages render a stub with a "translation in progress" notice — not a 404 or a missing nav entry. `lang:` front matter set on all files. (French-only course; English stubs deferred per Assumptions)

*For teaching pages only:*
- [x] **T-I. Content Fidelity** — Canonical theory, examples, and exercises preserved. (FR-010 explicitly requires this)
- [x] **T-II. Pedagogical Structure** — Theory → examples → exercises order maintained. (Abstraction ladder embeds this: theory/formula → worked example → exercises unchanged)
- [x] **T-III. Audience language** — Plain language; every formula has a prose explanation. (FR-003 requires 4-component explanation for every formula)
- [x] **T-IV. Interactive demos** — Priority concepts have Shinylive Python or OJS interactive demos; gaps marked with TODO callout. (FR-009 specifies 4 demos with technology justification per T-IV)
- [x] **T-V. Glossary** — New symbols added to the course `glossary.qmd`. (FR-007 updates all 47+ symbols with intuition entries)
- [x] **T-VI. Proof** — Each session includes at least one collapsible formal proof. (Existing proofs preserved; no new concepts requiring new proofs)
- [x] **T-VII. Visual intuition** — Geometric interpretation surfaced where applicable. (FR-004 requires diagrams/demos for Duration, VAN profile, Convexity, Annuity timeline)
- [x] **T-VIII. Course syllabus** — `index.qmd` exists at course root, is first sidebar entry, contains Recommended Literature section. (Existing index.qmd unchanged; already compliant)

## Project Structure

### Documentation (this feature)

```text
specs/011-math-finance-intuition/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (N/A - no external interfaces)
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
fr/teaching/mathematical-finance/
├── index.qmd                 # Course syllabus (unchanged)
├── module-01.qmd             # Journée 1 - 5 Séquences (major rewrite)
├── module-02.qmd             # Journée 2 - 5 Séquences (major rewrite)
├── module-03.qmd             # Journée 3 - 5 Séquences (major rewrite)
├── glossaire.qmd             # Glossary - 47+ symbols to update with intuition template
├── formulaire.qmd            # Formula reference - 10 formulas to annotate
└── _freeze/                  # Computational cache (auto-updated on render)

docs/fr/teaching/mathematical-finance/
├── module-01.html            # Rendered output
├── module-02.html
├── module-03.html
├── glossaire.html
├── formulaire.html
└── _freeze/                  # Committed cache

assets/
└── dark.scss                 # Styling (no changes planned)
```

**Structure Decision**: Single-project Quarto site. Feature modifies existing teaching content files in place. No new directories or external interfaces.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | All constitution checks pass | N/A |

---

## Phase 0: Research

*Generate `research.md` resolving all NEEDS CLARIFICATION and documenting best practices.*

### Research Tasks

| Task | Description | Output |
|------|-------------|--------|
| R1 | Research best practices for "concrete-to-abstract" pedagogy in financial mathematics education | Pedagogical patterns for sequencing |
| R2 | Document OJS vs Shinylive tradeoffs for each of the 4 required demos | Technology justification per demo (T-IV compliance) |
| R3 | Define standardized "Intuition économique" 3-field template with examples | Template for glossary updates (FR-007) |
| R4 | Define "Explication en langage clair" 4-component structure with examples | Template for formula explanations (FR-003) |
| R5 | Document "Erreur fréquente" callout pattern with financial math examples | Pattern for metacognitive callouts (FR-006) |
| R6 | Review existing module files to map current structure to target abstraction ladder | Gap analysis per section |

### Research Output: `research.md`

Will contain decisions, rationale, and alternatives for each research task.

---

## Phase 1: Design & Contracts

*Generate `data-model.md`, `quickstart.md`, and (if applicable) `contracts/`.*

### Data Model (`data-model.md`)

Entities derived from spec:

1. **Module** — Course day file
   - Fields: `id` (01/02/03), `title`, `sequences` (list of Sequence)
   - Relationships: contains 5 Sequences

2. **Sequence** — Major concept section (Séquence 2-6)
   - Fields: `number` (2-6), `title`, `type` (concept|synthesis), `ladder_steps` (7 or 3), `concrete_case`, `formula_boxes` (list), `erreur_frequente` (bool), `interactive_demo` (optional)
   - Relationships: belongs to Module; contains FormulaBoxes, ConcreteCase, InteractiveDemo

3. **FormulaBox** — Boxed mathematical formula with explanation
   - Fields: `id`, `latex`, `explanation` (4 components: what, parameters, meaning, directional_intuition), `sequence_id`
   - Validation: explanation must have all 4 components

4. **ConcreteCase** — Narrative financial scenario
   - Fields: `id`, `narrative`, `decision_question`, `specific_numbers`, `sequence_id`
   - Validation: must appear before first FormulaBox in sequence

5. **GlossaryEntry** — Symbol definition with intuition
   - Fields: `symbol`, `name`, `definition`, `pronunciation`, `modules`, `intuition` (3 fields: ce_que_ca_represente, pourquoi_ca_importe, intuition_cle)
   - Validation: intuition has all 3 fields

6. **FormulaireEntry** — Formula reference with intuition reminder
   - Fields: `id`, `latex`, `description`, `intuition_reminder` (1 sentence), `symbols`
   - Validation: intuition_reminder present

7. **InteractiveDemo** — Parameter exploration widget
   - Fields: `id`, `title`, `technology` (OJS|Shinylive), `concepts` (list), `sequence_id`, `justification` (T-IV rationale)
   - Validation: technology matches computational need

### Contracts

No external interfaces (APIs, CLIs, libraries). This is a content-only feature. Contracts directory will contain a single file documenting the internal "pedagogical contract" — the abstraction ladder template that each concept section must follow.

`contracts/pedagogical-contract.md` — Defines the required structure for concept sections (7-step ladder) and synthesis sections (3-step pattern), including required callout types and heading hierarchy.

### Quickstart Validation Guide (`quickstart.md`)

Prerequisites:
- Quarto installed (`quarto --version`)
- Python 3.11+ with Shinylive dependencies (for Shinylive demos)
- Node.js (for OJS demos, via CDN)
- Git (for `_freeze/` commit)

Validation Steps:
1. `cd fr/teaching/mathematical-finance`
2. `quarto render module-01.qmd --quiet` → verify exit 0
3. `quarto render module-02.qmd --quiet` → verify exit 0
4. `quarto render module-03.qmd --quiet` → verify exit 0
5. `grep -n "Situation concrète\|Cas réel" module-0*.qmd` → verify 13+ matches (one per concept section)
6. `grep -n "Explication en langage clair" module-0*.qmd` → verify matches formula box count
7. `grep -n "Erreur fréquente" module-0*.qmd` → verify 13+ matches
8. `grep -n "shinylive-python\|ojs" module-0*.qmd` → verify 4+ demo blocks
9. `grep -n "Ce que ça représente\|Pourquoi ça importe\|Intuition clé" glossaire.qmd` → verify 47+ symbol entries have all 3 fields
10. `grep -n "intuition" formulaire.qmd` → verify 10 formulas have reminders
11. Open rendered HTML in browser → verify interactive demos load and respond

Expected Outcomes:
- All 3 modules render without errors
- Structural grep checks pass (counts match requirements)
- Interactive demos functional in browser
- Glossary and formulaire updated completely

---

## Phase 1 Design Complete

Ready for `/speckit-tasks` to generate implementation task breakdown.