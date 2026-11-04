# Research: Fictitious Consolidated Accounts (French GAAP)

All unknowns from the Technical Context of [plan.md](plan.md) are resolved
below. No open NEEDS CLARIFICATION remains (the three spec-level questions
were answered by the owner on 2026-11-04 and are recorded in spec.md).

## R1 — How are downloadable files (Excel/PDF) served on this site?

**Finding**: Quarto copies any file that sits next to a `.qmd` source (and any
path listed under `project.resources`) into `docs/` at render time. The site
already ships PDFs/PNGs this way inside `fr/teaching/financial-analysis/`
(e.g. the Banque de France PDFs), and `_quarto.yml` lists only `CNAME` and
`assets/giscus-neutral-light.css` as global resources.

**Decision**: Put the generated Excel/PDF under
`fr/teaching/financial-analysis/donnees/fichiers/` next to the dataset pages
and link them with relative paths (`fichiers/<groupe>-N.xlsx`). No change to
`project.resources`.

**Rationale**: Zero config, follows the existing pattern, keeps the dataset
self-contained in the course tree.

**Alternatives considered**: global `project.resources` entry (unnecessary —
it would expose the files site-wide and couple the course to the root
config); generating files into `docs/` directly (forbidden by Principle I —
`docs/` is generated output only).

## R2 — Which French-GAAP reference framework for the statements?

**Finding**: "Normes françaises" for consolidated accounts = PCG art.
L. 233-16 et suivants + règlement CRC 99-02 (comptes consolidés), with the
bilan and compte de résultat "modèle normal" of règlement ANC 2014-03, and
the tableau des flux de trésorerie (méthode indirecte) per CRC 99-02/PCG.
Integration methods: intégration globale (contrôle exclusif), mise en
équivalence (influence notable); coentreprises historically via intégration
proportionnelle under CRC 99-02.

**Decision**: Build the dataset on intégration globale for controlled
subsidiaries + mise en équivalence for one 30% associate; no coentreprise in
v1 (keeps the annexe simple). The annexe states the méthodes comptables
appliquées, as a real annexe would.

**Rationale**: Covers the two methods the course teaches; a coentreprise can
be added in the IFRS version later.

**Alternatives considered**: including a coentreprise with intégration
proportionnelle now (more complete but heavier annexe and more elimination
rules to verify; deferred to the IFRS pass).

## R3 — How is internal consistency (FR-003, SC-001) guaranteed?

**Finding**: The existing Q2 mini-group hard-codes figures in markdown and
even contains a deliberate anomaly for students to find. For a 3-year,
multi-entity dataset, hand-written tables would drift.

**Decision**: **Single-source generation.** One parameter file holds every
figure; `scripts/financial-analysis/generate-dataset.py` derives all
statements (bilan, CR, annexe, flux, goodwill, minoritaires) from it by
construction — each bilan balances because the generator computes one side
from the other; the `--check` mode re-reads the generated Excel and asserts
all invariants (bilan = passif, résultat ties, flux ties to Δ trésorerie,
consolidé = somme des postes après éliminations). The markdown tables in
the `.qmd` pages are emitted by the same script, so pages and Excel can
never diverge.

**Rationale**: Consistency by construction + machine check beats manual
proofreading at this scale; the generator also produces the teacher key and
the seeded variants (R5) for free.

**Alternatives considered**: hand-written markdown + a separate checker
(checker would flag but not prevent drift; two sources of truth); a Python
block inside the `.qmd` with `freeze: auto` (would couple rendering to the
`.venv` and touch `_freeze/` — rejected to keep Principle III untouched).

## R4 — What does the fictitious group look like?

**Decision** (owner confirmed "nouveau groupe industriel", 2026-11-04):

- **Groupe AUBÉPINE SA** — fictitious agro-industrial group, SIREN fictif
  à 9 chiffres non attribué (verified not to match a real company at
  implementation time), siège in France, not listed.
- Parent: **AUBÉPINE SA**.
- Subsidiaries (intégration globale): **AUBÉPINE NORD SAS** (75%),
  **AUBÉPINE SUD SAS** (80%), **VERGER Export SARL** (60%, export /
  foreign-currency flavor for the annexe).
- Associate (mise en équivalence): **TERROIR PARTENAIRES SA** (30%).
- 3 exercices: N-2, N-1, N. Figures in k€. Intragroup operations documented
  in the annexe: ventes intragroupe with marge en stock, prêt intragroupe,
  dividendes, créance/dette.

**Rationale**: 3 IG subsidiaries + 1 MEE exercises every method the course
teaches, stays small enough to verify by hand in the corrigé, and gives the
case studies a coherent narrative (growth + export + one associate).

**Alternatives considered**: reusing STRATFIN (rejected by owner — kept as
the Q2 intro workshop only); a listed group (adds IFRS/EURONEXT flavor,
deferred); a foreign subsidiary with full currency translation (too heavy
for French GAAP v1, candidate for the IFRS version).

## R5 — How do seeded per-student variants work (FR-009)?

**Decision**: `generate-dataset.py --seed <student-id> --out <dir>` shifts a
fixed, documented list of figures (CA of one subsidiary, stock level, taux
de marge intragroupe, dividende) by a deterministic pseudo-random amount
derived from the seed, then re-derives all dependent statements so the
variant still balances. The base (seed 0) is the published dataset. The
assignment page states openly that individual variants exist.

**Rationale**: Two students submitting identical numbers is detectable
because variants differ; transparency keeps it ethical (no hidden
instructions — SC-005).

**Alternatives considered**: hidden prompt injection in the HTML (rejected —
deceptive toward students using AI legitimately, and booby-traps the page
for any AI reader; see spec.md Context); no variants at all (leaves
copy-paste undetectable).

## R6 — Where do the dataset pages live and how are they registered?

**Decision**: `fr/teaching/financial-analysis/donnees/` with pages `index`
(presentation, périmètre, disclaimer, AI-use note, OJS demo), `bilan-consolide`,
`compte-de-resultat`, `annexe`, `flux-tresorerie`, `telechargements`; a new
sidebar section **"Fil rouge — Groupe AUBÉPINE"** in the
`fr-financial-analysis` block, and mirrored EN stubs + section in
`en-financial-analysis` (`teaching/financial-analysis/donnees/`).

**Rationale**: Principle II — only `_quarto.yml` registers navigation; the
`donnees/` subdirectory keeps the red thread visually grouped; EN stubs
satisfy Principle VI.

**Alternatives considered**: a single mega-page (harder to navigate,
violates the page-per-topic pattern of the course); a new top-level course
(rejected — it is a dataset of the existing course, not a new course).

## R7 — Where does the teacher key live?

**Decision**: `fr/teaching/financial-analysis/enseignant/corrige-aubepine.qmd`
(all figures, ratios, and the variant list), listed in the existing
"Instructor" sidebar section. The generator's parameter file remains the
ultimate source of truth; the corrigé is generated/checked against it
(SC-004: diff recomputed vs published = empty).

**Rationale**: Follows the existing `enseignant/` convention; keeps
student-facing pages clean.

**Alternatives considered**: key only in the repo, no page (inconsistent with
the course's instructor pages); key in a separate repo (breaks single-source
of truth).

## R8 — How is the visible AI-use policy worded and where?

**Decision**: Plain prose (not a callout — roles are reserved, Principle V) on
`donnees/index.qmd` and `evaluation.qmd`: the dataset is fictitious teaching
material; per-student variants exist for graded work; submitted work must
match the student's own variant and show the working file; oral restitutions
apply. No hidden text, no prompt injection (SC-005).

**Rationale**: Transparent, enforceable, consistent with the oral
restitutions already built into the quests.

**Alternatives considered**: a callout block (violates the callout-role
table); hidden canary text (rejected, see spec.md Context).
