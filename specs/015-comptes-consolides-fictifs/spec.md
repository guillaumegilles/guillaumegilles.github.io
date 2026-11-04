# Feature Specification: Fictitious Consolidated Accounts (French GAAP) — Course Red Thread

**Feature Branch**: `015-comptes-consolides-fictifs`

**Created**: 2026-11-04

**Status**: Draft

**Input**: User description: "Créer des comptes consolidés complets mais fictifs pour le cours de [financial analysis] afin de servir de fil rouge pour mes études de cas. Les comptes doivent être en normes françaises, on verra plus tard pour une version IFRS."

## Context

`fr/teaching/financial-analysis/` already teaches consolidation in Quest 2
(`modules/02-archives-consolidees.qmd`) with a deliberately simplified
mini-group (STRATFIN HOLDING, PHOENIX SA 80%, ORION SARL 60%) whose accounts
are hand-built for one 100-minute workshop. The rest of the course (Quests
3–9, BdF methodology pages, exams) works on real French companies or
scattered case files (`exercices/Cas pratiques...docx`).

What is missing is a single, coherent, **complete** set of fictitious
consolidated accounts — full French-GAAP statements over several years —
that every case study in the course can refer back to ("fil rouge"). This
feature creates that dataset and publishes it on the site.

**Explicitly out of scope**: embedding hidden prompt-injection instructions
in the published HTML to make students' generative-AI tools return wrong
answers. That mechanism was requested and rejected: it is deceptive toward
readers (including students using AI legitimately), it cannot be consented
to, and it booby-traps the page for any AI tool that reads it. The
anti-AI-copy measures adopted instead are transparent and documented (see
FR-009 and SC-005): a visible AI-use policy, per-student seeded data
variants, working-file requirements, and oral restitutions.

## Clarifications

### Session 2026-11-04

- Q: Extend the existing STRATFIN mini-group of Quest 2 or create a new
  group? → A: **New fictitious industrial group** (3–4 subsidiaries,
  possibly one mise en équivalence and one foreign subsidiary). STRATFIN
  stays as the simplified introductory workshop of Quest 2.
- Q: Which statement set and how many years? → A: **Bilan + compte de
  résultat (modèle normal) + annexe + tableau des flux de trésorerie, for
  3 years (N-2, N-1, N)** — enough for ratios and trend analysis.
- Q: Published consolidated statements only, or also individual accounts to
  rebuild the consolidation? → A: **Published consolidated statements
  only**; the annexe documents the intragroup operations for analysis, but
  no per-entity individual accounts are published.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Student accesses the complete fictitious consolidated accounts (Priority: P1)

A student opens the course site and finds a dedicated page for the
fictitious group: full consolidated balance sheet, income statement, notes
(annexe), and cash-flow statement for several fiscal years, downloadable as
Excel and PDF, clearly watermarked "données fictives à but pédagogique".

**Why this priority**: The dataset is the backbone of the case studies;
without it nothing else in the course can reference a common set of
accounts.

**Independent Test**: From the course sidebar, reach the dataset page in
at most 2 clicks and download every statement without missing file or
broken link.

**Acceptance Scenarios**:

1. **Given** the course site, **When** the student navigates the
   financial-analysis sidebar, **Then** a clearly labelled entry leads to
   the fictitious-group dataset page.
2. **Given** the dataset page, **When** the student downloads the Excel
   file, **Then** it contains bilan, compte de résultat, annexe and tableau
   des flux for each published year.
3. **Given** any published page or file of the dataset, **When** a student
   reads it, **Then** a visible disclaimer states the figures are fictitious
   and for teaching only.

---

### User Story 2 - Instructor reuses the same group across all case studies (Priority: P1)

The instructor references the same fictitious group in Quests 2–9, the BdF
ratio pages and the exams, so students meet one coherent company throughout
the course instead of a new dataset per exercise.

**Why this priority**: The "fil rouge" is the point of the feature; a
dataset used in only one quest is a failure.

**Independent Test**: Grep every quest/exam page for the group name and
confirm each case study that needs accounts links to the dataset.

**Acceptance Scenarios**:

1. **Given** the course modules, **When** a case study needs financial
   statements, **Then** it links to the fictitious-group dataset instead of
   inventing new figures.
2. **Given** the dataset, **When** the instructor prepares Quest 3
   (diagnostic), **Then** the consolidated accounts published there are
   exactly those of the dataset (no divergence).

---

### User Story 3 - Student works from the dataset at the required depth (Priority: P2)

The student analyses the published consolidated statements (bilan, compte
de résultat, annexe, tableau des flux) and the notes documenting the
intragroup operations; per-entity individual accounts are not published, so
the quest focuses on analysis of the consolidated statements, not on
rebuilding the consolidation (decision of 2026-11-04).

**Why this priority**: Determines whether the dataset supports a full
consolidation-building exercise or only ratio analysis.

**Independent Test**: Perform the quest's task using only the published
dataset and confirm every needed figure is present and labelled.

**Acceptance Scenarios**:

1. **Given** the dataset, **When** a student computes the Banque de France
   ratios (performance, structure, liquidité) for each published year,
   **Then** all inputs are available and the ratios are computable without
   gaps.
2. **Given** the consolidation quest, **When** the student performs the
   eliminations, **Then** all intragroup operations (sales, loans,
   dividends, margin in inventory) are documented with amounts.

---

### User Story 4 - Teacher has a complete answer key (Priority: P2)

The instructor has a teacher-only version with every computed figure:
eliminations, goodwill, minority interests, consolidated statements, and
all ratios, so grading is mechanical and consistent.

**Why this priority**: A fictitious dataset is only useful if the teacher
can verify it; errors in the key would propagate to every case study.

**Independent Test**: Recompute every published figure from the key and
confirm exact equality with the published statements.

**Acceptance Scenarios**:

1. **Given** the teacher key, **When** the consolidations are recomputed,
   **Then** the resulting bilan and compte de résultat match the published
   consolidated statements line by line.
2. **Given** the teacher key, **When** a ratio is recomputed for any
   published year, **Then** it matches the value quoted in the quest
   solutions.

---

### User Story 5 - Transparent per-student data variants deter AI copy-paste (Priority: P3)

For graded individual work, the teacher can generate a seeded variant of
the dataset per student (a few key figures shifted deterministically from a
student ID), with a visible notice on the assignment that variants exist.
Two students submitting identical AI-generated numbers are detectable
because their variants differ. No hidden instruction is embedded anywhere in
the published pages.

**Why this priority**: Supports academic integrity without deceptive
mechanisms; lower priority because the pedagogical core is the dataset
itself.

**Independent Test**: Generate two variants with different seeds and confirm
(i) they differ in exactly the seeded figures and (ii) each variant still
balances and remains internally consistent.

**Acceptance Scenarios**:

1. **Given** a student seed, **When** the variant generator runs, **Then**
   the output differs from the base dataset only in the designated
   figures, and the bilan still balances.
2. **Given** the assignment page, **When** a student reads it, **Then** a
   visible note states that individual variants exist and that submitted
   work must match the student's own variant.

### Edge Cases

- A published bilan that does not balance, or a compte de résultat whose
  result does not flow into capitaux propres: every published year must be
  checked by an automated consistency script before release.
- Consolidated figures that drift from the sum of individual accounts minus
  eliminations: the teacher key must reconcile them exactly.
- Missing comparatives: ratios and trend analyses need prior years, so the
  dataset must include enough years for every ratio used in the course.
- A student using a generative-AI tool on the page must never encounter
  hidden instructions: published HTML/markdown must be free of prompt
  injection (verified by inspection, see SC-005).
- English course pages: follow the site convention of labelled stubs linking
  to the French pages.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The feature MUST define one new fictitious industrial group
  (name, fictitious SIREN, sector, listing status) with a parent company and
  3–4 subsidiaries, each with a stated percentage of control and integration
  method (intégration globale / mise en équivalence), possibly including one
  foreign subsidiary. The existing STRATFIN mini-group remains the
  simplified Quest 2 workshop and is not modified.
- **FR-002**: The feature MUST publish complete French-GAAP (PCG, règlement
  CRC 99-02, consolidation CRC 2000-01/99-02) consolidated statements for
  **3 fiscal years (N-2, N-1, N)**: bilan (modèle normal), compte de résultat
  (par nature, modèle normal), annexe (principes, périmètre, écarts
  d'acquisition, opérations intragroupe, intérêts minoritaires) and tableau
  des flux de trésorerie.
- **FR-003**: All published statements MUST be internally consistent:
  each bilan balances, each compte de résultat result ties to the bilan, the
  cash-flow statement ties to the change in trésorerie, and comparatives
  are coherent year over year. Consistency MUST be verifiable by an
  automated check.
- **FR-004**: Intragroup operations (sales with margin in inventory, loans,
  receivables/payables, dividends) MUST be documented in the annexe with
  amounts sufficient to understand and analyse the eliminations. Per-entity
  individual accounts MUST NOT be published (published consolidated
  statements only, per the 2026-11-04 decision).
- **FR-005**: The dataset MUST be published on the site as dedicated pages
  under `fr/teaching/financial-analysis/` (e.g. a `cas-<groupe>/` section),
  registered in the matching sidebar of `_quarto.yml`, with downloadable
  Excel and PDF files; English pages under `teaching/financial-analysis/`
  MUST be labelled stubs linking to the French pages.
- **FR-006**: Every published page and file MUST carry a visible
  "données fictives — usage pédagogique uniquement" disclaimer.
- **FR-007**: A teacher-only answer key MUST exist under the course
  `enseignant/` area with all eliminations, goodwill, minority interests,
  consolidated statements and ratios, reproducing every published figure.
- **FR-008**: Existing quest and exam pages that need accounts MUST link to
  the dataset (fil rouge), starting with the consolidation quest and the
  diagnostic quest.
- **FR-009**: A seeded variant generator MUST be provided (script producing
  per-student Excel variants), used only with a visible notice on the
  assignment. The published pages MUST NOT contain any hidden prompt
  injection or instruction aimed at readers' AI tools.
- **FR-010**: An IFRS version of the dataset is explicitly OUT OF SCOPE for
  this feature and reserved for a later feature.

### Key Entities *(include if feature involves data)*

- **Groupe fictif**: parent company + subsidiaries; key attributes: name,
  fictitious SIREN, sector, percentage of control per subsidiary, integration
  method.
- **États financiers publiés**: bilan, compte de résultat, annexe, tableau
  des flux — per fiscal year, with comparatives.
- **Opérations intragroupe**: sales, loans, receivables/payables, dividends,
  margin in inventory — each with amount and counterpart entity.
- **Écarts d'acquisition / Intérêts minoritaires**: computed per subsidiary
  at acquisition and at each closing.
- **Variante par étudiant**: seed + list of shifted figures; derived from the
  base dataset, still internally consistent.
- **Corrigé enseignant**: full computation trail reproducing every published
  figure.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of published statements pass the automated consistency
  checks (balanced bilans, tied results, coherent comparatives) for every
  published year.
- **SC-002**: At least the consolidation quest, the diagnostic quest and
  the BdF ratio pages reference the same dataset; the dataset page is
  reachable from the course sidebar in ≤ 2 clicks.
- **SC-003**: A student can compute the full set of Banque de France ratios
  (performance, structure financière, liquidité) for every published year
  using only the downloadable dataset, with zero missing inputs.
- **SC-004**: The teacher answer key reproduces 100% of the published
  figures exactly (verified by diffing recomputed vs. published statements).
- **SC-005**: Inspection confirms 0 hidden instructions or prompt-injection
  content in any published HTML/markdown; the only anti-AI-copy measures are
  the visible policy, seeded variants and oral/working-file requirements.

## Assumptions

- "Normes françaises" means French GAAP as codified in the PCG with
  règlements CRC 99-02 (comptes consolidés) and CRC 2000-01; modèle normal
  of the bilan and compte de résultat; intégration globale for controlled
  subsidiaries, mise en équivalence for significant influence.
- The dataset is published in French first; English pages are stubs linking
  to the French version (site-wide convention).
- Downloadable files are Excel (working data) and PDF (presentation);
  sources remain `.qmd` per the site constitution.
- The existing simplified STRATFIN exercise in Quest 2 stays as the
  introductory workshop; the new industrial group is the red thread for the
  case studies (confirmed 2026-11-04).
- Figures are in k€ unless the chosen group size justifies M€.
- The seeded variant generator is a small script (e.g. Python in the
  project `.venv`), not a web service.
