# Tasks: 3-Day Lecture Slide Deck for the Financial Analysis Course

**Input**: Design documents from `specs/014-financial-analysis-slides/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/slide-deck-format.md, contracts/day-plans.md, quickstart.md

**Tests**: The spec did not ask for automated tests. Validation means renders, static grep checks and timing sums ([quickstart.md](quickstart.md)). These are included as checkpoint and polish tasks, not as TDD tasks.

**Organization**: All three deck files are shared across stories. Each story adds one layer to them:

| Story | Layer |
|---|---|
| US1 | Structure: agenda, objectives, block sections, exercise briefs, recap |
| US2 | Content from the original deck, corrected and up to date |
| US3 | Content from the other folder files |
| US4 | Site integration for revision |

Within a story, tasks on different deck files are marked [P].

**Paths**: Shorthand used below:
- `FR` = `fr/teaching/financial-analysis`
- `EN` = `teaching/financial-analysis`
- `SPEC` = `specs/014-financial-analysis-slides`

## Format: `[ID] [P?] [Story] Description`

---

## Phase 1: Setup (shared infrastructure)

- [ ] T001 Create `FR/slides/_metadata.yml` with exactly this content: `format: revealjs` with `theme: ../../../../assets/dark-slides.scss`, `slide-number: true`, `progress: true`, `controls: true`, `transition: slide`, `fig-align: center`. Copy the comment header from `fr/teaching/mathematical-fundamentals/slides/_metadata.yml` and do **not** set `lang:` (contract §1).
- [ ] T002 [P] Create `EN/slides/_metadata.yml`, identical to T001 except `theme: ../../../assets/dark-slides.scss` (contract §1).
- [ ] T003 Create minimal decks `FR/slides/jour-1.qmd`, `FR/slides/jour-2.qmd` and `FR/slides/jour-3.qmd`. Each gets the front matter from contract §2 (`title: "Jour N — …"` using the day titles from `SPEC/contracts/day-plans.md`, `subtitle: "Analyse financière et stratégique · INSEEC MSc"`, `footer: "[Retour au cours 📖](../index.qmd)"`, `date-modified: 2026-10-18`, no `format:`, no `lang:`, no `date: today`) and one placeholder `## Programme de la journée` slide.
- [ ] T004 Smoke-render per quickstart §1: run `quarto render FR/slides/jour-1.qmd --quiet` and check that `docs/fr/teaching/financial-analysis/slides/jour-1.html` is a RevealJS deck, not a plain HTML page.

---

## Phase 2: Foundational (blocking prerequisites)

**Purpose**: Set up the evidence base every content task depends on: the coverage map, resolved facts and case data.

- [ ] T005 Create `SPEC/coverage-map.md` with the six sections from data-model.md "CoverageMap":
  - Original slides: 102 rows, numbered 1–102 with the slide titles from the PPTX, destination column empty.
  - Source files: one row per file currently in `FR/`, including `modules/`, `exercices/`, PDFs, DOCX, PPTX, ODP, MP4 and images. Get the list with `find fr/teaching/financial-analysis -type f`.
  - Definitions, Verified facts, Exercises, Quest mapping.
- [ ] T006 Copy research.md Part B rows F1–F14 into the "Verified facts" section of `SPEC/coverage-map.md`. Use columns `id | value | publisher | date | url | checked_on | status`, with `status` restricted to `verified` / `fallback` / `todo`.
- [ ] T007 [P] Resolve F9 (intégration proportionnelle under ANC 2020-01). Read Livre II, Titre II of https://www.anc.gouv.fr/files/anc/files/1_Normes_fran%C3%A7aises/recueil/REGLT-2020_01-VERSION-RECUEIL2026.pdf and record the article number and the verdict in `SPEC/coverage-map.md`.
- [ ] T008 [P] Resolve F11 (cote X threshold in months). Check the current BdF cotation reference on banque-france.fr. If it can't be confirmed, set status `fallback` and use the value from the 2022 guide (20 mois) with its date. Record in `SPEC/coverage-map.md`.
- [ ] T009 [P] Resolve F6. Find the latest BdF *Cotation — chiffres clés* PDF (data at 31/12/2024 or later) on banque-france.fr. Record the total and the count per cote for the 22 grades in `SPEC/coverage-map.md`. If only the 31/12/2023 edition exists (325 105 firms), keep it as `verified` with that date.
- [ ] T010 [P] Resolve F13 (IFRS 18: effective 1 Jan 2027, replaces IAS 1). Cite the IFRS Foundation page URL in `SPEC/coverage-map.md`.
- [ ] T011 [P] Find the official URL of the BdF video "C'est quoi la Banque de France" (BdF YouTube channel or banque-france.fr) and add it as F15 in `SPEC/coverage-map.md`. If none is found, record title and publisher only, per the spec edge case.
- [ ] T012 [P] Retrieve the Lectra SA 2016 social accounts (bilan + compte de résultat, in K€) from the *Rapport financier 2016*, "Comptes de la société mère" (research A8). Save them as Markdown tables in `SPEC/case-data-lectra-2016.md` with the source URL and page.
- [ ] T013 [P] Search the Klarsen/Actiplay investor archive for the ConcoursMania SA 2016 social accounts. If found, save them as tables in `SPEC/case-data-concoursmania-2016.md`. If not, build tables from the figures in `CORRIGE CAS PRATIQUE ANALYSE FINANCIERE - ELEMENTS DE BASE.docx` that reconcile with the key, and mark the file `fallback` with a note for the slide (FR-017a).
- [ ] T014 Reconcile T012 and T013 against the answer-key totals in `CORRIGE CAS PRATIQUE … ELEMENTS DE BASE.docx`. The totals are VA, EBE, RE, RCAI, RN, CAF, FRNG, BFR and TN, for example LECTRA FRNG 69 282 / BFR 20 430 / TN 48 853 and CONCOURSMANIA FRNG 1 959 / BFR −749 / TN 2 705. Record each gap, including the known off-by-2/3 mismatches, in the "Exercises" section of `SPEC/coverage-map.md`.
- [ ] T015 Fill the "Definitions" section of `SPEC/coverage-map.md` with one row per ratio/aggregate, following research A6:
  - rentabilité économique = REX net d'IS / actif économique
  - marge commerciale ratio = MC / CA HT
  - BFR = BFRE + BFRHE
  - délai clients includes EENE
  - taux d'endettement = endettement financier retraité / FP retraités
  - RNR ≈ ¾ RCAI
  - CAFr = ¾ RCAI + dotations nettes d'exploitation
  - CAF ≠ FCF

  Each row lists the rejected variants with their sources (`COURS M1`, `LES RATIOS`, `M1 FIN Démarche`, PPT slide 85).
- [ ] T016 Recompute the CP2 and CP3 answer-key figures at 25 % (CP2: RCAI retraité 9 128 × ¾ = 6 846 instead of 6 085; CP3: redo the payback-on-RNR variants). Write them to `SPEC/answer-keys-25pct.md`, an internal instructor file, and set `key_tax_convention` for each exercise in `SPEC/coverage-map.md`.

**Checkpoint**: Every F-row has status `verified` or `fallback`, the case data exists, and the definitions are fixed. Deck content work can start.

---

## Phase 3: User Story 1 — The instructor delivers each course day from the deck (Priority: P1) 🎯 MVP

**Goal**: Each deck has the full teaching structure: agenda with timings, objectives, a section slide per block, exercise briefs, recap and preview. The day can be run in time even before the content layers are complete.

**Independent Test**: Open each deck in presentation mode. Check that the agenda lists every block from `contracts/day-plans.md`, that non-optional minutes add up to 360, that the 3–6 objectives are there, that every exercise has a brief, and that there is a recap and preview (spec US1 scenarios 1, 3, 4, 5).

- [ ] T017 [P] [US1] In `FR/slides/jour-1.qmd`:
  - Write `## Programme de la journée` as a table `Horaire | Bloc | Durée | Activité / quête` with blocks 1.0–1.9 from `contracts/day-plans.md`. Non-optional minutes must total 360. The schedule is 9:00–12:00 / 13:30–16:30.
  - Write `## Objectifs` with 3–6 measurable verbs.
  - Add one `# Bloc 1.N — <titre>` section slide per block, with `::: notes` `Durée : N min`.
- [ ] T018 [P] [US1] Same as T017 for `FR/slides/jour-2.qmd` with blocks 2.0–2.11.
- [ ] T019 [P] [US1] Same as T017 for `FR/slides/jour-3.qmd` with blocks 3.0–3.10.
- [ ] T020 [P] [US1] In `FR/slides/jour-1.qmd`, add exercise briefs as `::: {#exr-temple-bilans-n1}`, `::: {#exr-concoursmania-lectra-a}` and `::: {#exr-concoursmania-lectra-b}`. Each brief gives task, data location, team format and duration (60/45/30 min), contains **no solution**, and is followed by `::: notes` naming the answer key: `modules/01-temple-bilans-enseignant.qmd` and `CORRIGE CAS PRATIQUE ANALYSE FINANCIERE - ELEMENTS DE BASE.docx` (FR-021).
- [ ] T021 [P] [US1] In `FR/slides/jour-2.qmd`, add exercise briefs `#exr-archives-consolidees` (60 min, key: "à rédiger", see T046), `#exr-cp1-swot` (30 min) and `#exr-cp2-rnr` (30 min). The CP1 and CP2 notes point to `Cas pratiques d'analyse financière corrigé.docx`. CP2 also points to `SPEC/answer-keys-25pct.md`, and its slide states the 25 % convention.
- [ ] T022 [P] [US1] In `FR/slides/jour-3.qmd`, add exercise briefs `#exr-cp3-fonds-propres` (60 min) and `#exr-cp4-endettement` (45 min). The notes name `Cas pratiques d'analyse financière corrigé.docx` and, for CP3, also `SPEC/answer-keys-25pct.md`.
- [ ] T023 [P] [US1] In `FR/slides/jour-1.qmd`, add `# Récapitulatif` with `## Ce qu'il faut retenir` (4–6 bullets) and `## Demain` (Day 2 preview).
- [ ] T024 [P] [US1] Same as T023 for `FR/slides/jour-2.qmd`, with a Day 3 preview.
- [ ] T025 [P] [US1] Same as T023 for `FR/slides/jour-3.qmd`, with `## Examen et suite` instead of `## Demain`. Briefly describe the exam format from `FR/exercices/examen-1h.qmd` and `examen-final.qmd` and include the course-feedback prompt (SC-007).
- [ ] T026 [US1] Render all three decks (quickstart §2) and check timing sums (quickstart §4).

**Checkpoint**: Three runnable day skeletons, each with agenda, briefs and recap.

---

## Phase 4: User Story 2 — Content from the original deck is kept, corrected and up to date (Priority: P2)

**Goal**: All still-valid content of `inseec-analyse-financiere.pptx` (parts 2–3) is in the decks. Image-only slides are rebuilt, facts are current and the tax convention is consistent.

**Independent Test**: Every row 1–102 of the coverage map's "Original slides" section has a destination or a drop reason. A spot check of 10 facts matches the "Verified facts" section (spec US2 scenarios 1–6).

- [ ] T027 [P] [US2] Block 2.1 in `FR/slides/jour-2.qmd`:
  - Condense PPT slides 3–21 into **at most 5** text slides: 3 missions, Eurosystème, why the BdF rates companies.
  - Link the video from F14 (and F15 if found) as plain `https://` links. Never use `<iframe>`.
  - Add `::: aside` sources (FR-007, FR-022).
- [ ] T028 [P] [US2] Block 2.2 in `FR/slides/jour-2.qmd`, rebuilding PPT 22–39:
  - Cotation vs notation, « à dire d'expert », information sources.
  - Cote d'activité table A–N, X, with **seuil 1 250 K€ since 12/01/2025** (F1) and X from F11.
  - Cote de crédit table with the 22 grades and labels from the *5 questions* PDF, eligibility 1+ to 4+ (F3).
  - A `:::: {.columns}` then-now slide labelling the old 3++…9 scale "échelle avant 2022".
  - A `xychart-beta` of one-year default rates per grade (F4), with total 1,75 % / 3,22 % / 3,68 % (F5).
  - Legal basis L.141-6, OEEC since 19/06/2007, ICAS/ECAF.
  - Indicateur dirigeant 000/060 rules, and one FIBEN slide.
  - Every figure slide has an `::: aside` source (FR-008, FR-010, FR-013, FR-014).
- [ ] T029 [P] [US2] Block 2.3 in `FR/slides/jour-2.qmd`, rebuilding PPT 41–47 and 60–61:
  - Notion de groupe, enjeux, particularités, documentation, entretien de cotation.
  - Consolidation thresholds **30 M€ / 60 M€ / 250, exercices à compter du 1/1/2025** (F7).
  - **ANC 2020-01** replacing CRC 99-02 (F8).
  - The méthodes table (IG / IP / MEE / non consolidé), with the IP wording per F9.
  - SCI focus (3 conditions).
  - "offre au public" replaces "appel public à l'épargne".
- [ ] T030 [P] [US2] Block 2.5 in `FR/slides/jour-2.qmd`, rebuilding PPT 49–56:
  - Step 1 objectives.
  - A Markdown 2×2 SWOT grid rebuilt from the Séminaire PDF text (strengths: diversification, niche, brevets, partenariats; etc.).
  - A mermaid `flowchart` group organigramme (holding → filiales, frein 1 between entities, replacing PPT 52).
  - Legal, economic and financial organisation, each ending with "→ degré d'intégration …".
  - Faits marquants, and the choice of debt aggregate (brut / net).
- [ ] T031 [P] [US2] Block 2.8 in `FR/slides/jour-2.qmd` from PPT 58–61: objectives, quality and transparency checks, consolidation scope checks, methods vs real control, CAC certification.
- [ ] T032 [P] [US2] Block 2.9 in `FR/slides/jour-2.qmd` from PPT 63–66:
  - Recurring vs non-recurring items.
  - A `.callout-tip` formula RNR ≈ ¾ × RCAI, followed by a "Ce que mesure…" sentence.
  - A `.callout-caution` **derivation** RNR = RCAI × (1 − 25 %), with a note to use the actual tax charge when losses or deferred tax distort it (T-VI, FR-011).
  - Trends by group profile, organic vs scope vs FX, point mort.
- [ ] T033 [P] [US2] Block 3.1 in `FR/slides/jour-3.qmd`, rebuilding PPT 68–78:
  - FP as a residual.
  - `.callout-tip` FPNR = FP − écart d'acquisition élargi − IDA − écarts de conversion positifs.
  - Goodwill decomposition as a table (replacing image PPT 70).
  - `.callout-caution` **derivation** of the 10 × RNR cap on écart d'acquisition élargi.
  - Impôts différés with the two worked examples from PPT 73–74 rebuilt as tables and **recomputed at 25 %**: provision 120 K€ ⇒ IDA 30 K€, not 40 K€. Redo the dérogatoire example from 34,4 % to 25 %.
  - Treatment rules (2-year horizon for loss carryforwards).
  - Écarts de conversion, minoritaires, retraites.
- [ ] T034 [P] [US2] Block 3.3 in `FR/slides/jour-3.qmd` from PPT 79–84:
  - Debt components: titres hybrides (3 treatments), comptes courants d'associés (neutralisation conditions).
  - Hors-bilan as two lists (systematic vs depending on risk).
  - Trésorerie disponible (pre-allocated or captive cash).
  - Taux d'endettement = endettement financier retraité / FP retraités.
- [ ] T035 [P] [US2] Block 3.5 in `FR/slides/jour-3.qmd` from PPT 85: `.callout-tip` CAFr = ¾ × RCAI + dotations nettes d'exploitation. This **corrects the ⅔ in PPT 85**, and the correction goes in the coverage map. Add capacité de remboursement = endettement retraité / CAFr, and coverage of the N+1 / N+2 maturities.
- [ ] T036 [P] [US2] Block 3.6 in `FR/slides/jour-3.qmd` from PPT 87–93:
  - Objectives, then one slide per phase: static (FRNG, FRNG/BFR, TN/FP, ΔTN/FP), dynamic (FTA/CA), prospective (FTD = FTA − investissements de maintien − dividendes; Ressources N+k − échéances MLT N+k > 0) and financial risks.
  - The final 2×2 verdict matrix (horizon × marges de manœuvre → cote 5+ to 6 / at most 4 / eligible) as a Markdown table, replacing PPT 93.
- [ ] T037 [P] [US2] Block 3.7 in `FR/slides/jour-3.qmd` from PPT 96–101:
  - 4 phases: financial cote (primary cote 3–6 segmented → **map to the current 22-grade scale**, `TODO: à vérifier` only if unresolved), qualitative profile grid rebuilt as a table (replacing PPT 99), perspective, subsidiaries.
  - Rule: FP < ½ capital ⇒ at best 5+. Confirm this against GUIDE (2022) and record the result in the coverage map.
- [ ] T038 [P] [US2] In `FR/slides/jour-1.qmd` block 1.0, add a mermaid `flowchart` of the six BdF steps (replacing the 7 repeated agenda slides). Reuse it in `FR/slides/jour-2.qmd` and `jour-3.qmd`, highlighting the current step through a text label, not CSS.
- [ ] T039 [US2] Fill the "Original slides" section of `SPEC/coverage-map.md`:
  - Rows 1–102 → `jour-N / bloc / slide` or `dropped: <reason>`, following contracts/day-plans.md "deliberately dropped".
  - Log the corrections: ⅔ → ¾, old scale → 22 grades, 750 K€ → 1 250 K€, 24/48/250 → 30/60/250, CRC 99-02 → ANC 2020-01, 34,4 %/33⅓ % → 25 %.

**Checkpoint**: Days 2–3 carry the full BdF method with current facts. US2 is independently verifiable through the coverage map.

---

## Phase 5: User Story 3 — Material from the other course files fills the gaps (Priority: P3)

**Goal**: Day 1 fundamentals, exercise data, focus boxes, then-now slides and quest input blocks, all sourced from the folder.

**Independent Test**: Every block in `contracts/day-plans.md` has a source in the coverage map. Every exercise has readable data and a named key. Every folder file has a verdict (spec US3 scenarios 1–4).

- [ ] T040 [P] [US3] Block 1.1 in `FR/slides/jour-1.qmd` from `COURS M1.pdf` §I: flux réels/monétaires, partie double, bilan and compte de résultat structure (table), sources of information. Cite **ANC 2014-03 (PCG)**, not "PCG 1987".
- [ ] T041 [P] [US3] Block 1.3 in `FR/slides/jour-1.qmd`:
  - The SIG cascade as a table, with each formula as written in `Élément sde base …docx`.
  - The crédit-bail retraitement worked example (VO 500 000, redevance 100 000, VR 100 000, 5 ans ⇒ dotation 80 000, intérêts 20 000) with `. . .` step reveals.
  - Personnel extérieur and subventions retraitements.
  - SIG ratios table with the T015 definitions.
- [ ] T042 [P] [US3] Block 1.4 in `FR/slides/jour-1.qmd`: CAF méthode soustractive (from EBE) and additive (from RN) in a `:::: {.columns}` slide, plus a slide "CAF ≠ free cash flow" that corrects the `M1 FIN Démarche` error.
- [ ] T043 [P] [US3] Block 1.6 in `FR/slides/jour-1.qmd`:
  - A two-column bilan fonctionnel diagram (Markdown table: emplois stables | ressources stables; actif / passif d'exploitation; HE; trésorerie).
  - Reclassification rules: valeurs brutes, amortissements → ressources propres, EENE, CBC.
  - The Iris crédit-bail example (150 000 / 4 ans / VR 50 000 ⇒ +25 000 ressources propres, +125 000 dettes financières).
  - `.callout-tip` FRNG, BFR = BFRE + BFRHE, TN = FRNG − BFR, each with a prose sentence.
  - BFR in days.
- [ ] T044 [P] [US3] Block 1.8 in `FR/slides/jour-1.qmd`:
  - `.callout-tip` ROCE = REX net d'IS / actif économique, and ROE = RN / CP.
  - `.callout-caution` **derivation** ROE = ROCE + (ROCE − i) × D/CP, step by step (T-VI).
  - An `xychart-beta` line of ROE vs ROCE for D/CP = 0, 0.5, 1 and 2 with i = 4 % (T-VII).
  - DuPont (RN/CA × CA/Actif × Actif/CP) and effet ciseau.
  - The deck's single `.callout-warning`: mixing net/gross results or ROCE before and after tax.
- [ ] T045 [P] [US3] In `FR/slides/jour-1.qmd`, put the CONCOURSMANIA/LECTRA 2016 data from `SPEC/case-data-lectra-2016.md` and `SPEC/case-data-concoursmania-2016.md` into the `#exr-concoursmania-lectra-a/b` slides as `{.smaller}` tables, with `::: aside` sources. If T013 fell back, add the fallback sentence (FR-017a).
- [ ] T046 [US3] Write the missing instructor keys in `SPEC/answer-keys-25pct.md`: the CONCOURSMANIA/LECTRA ratio and credit-appreciation part (EBE/CA, RCAI/CA, RN/CA, EF/FP, FP/TB, EF/CAF, intérêts/EBE, FRNG/BFR, TN/FP) and a short key for the shortened Archives consolidées (Q2) exercise from `FR/modules/02-archives-consolidees.qmd`. Update the "Exercises" section of the coverage map (depends on T014).
- [ ] T047 [P] [US3] In `FR/slides/jour-2.qmd`, add data/context slides for `#exr-cp1-swot` (granulats group context) and `#exr-cp2-rnr` (hotel-TV group: CA 50 807, RCAI 4 528, RNC 772, plus the listed annex items), taken from `Cas pratiques d'analyse financière énoncé.docx`.
- [ ] T048 [P] [US3] In `FR/slides/jour-3.qmd`, add data slides for `#exr-cp3-fonds-propres` (ultra-frais dairy group, N-2 to N) and `#exr-cp4-endettement` from `Cas pratiques d'analyse financière énoncé.docx`, as `{.smaller}` or `{.scrollable}` tables.
- [ ] T049 [P] [US3] In `FR/slides/jour-2.qmd`, add a focus box in block 2.5: `> **Focus — Entreprises françaises (2020)**` with gross debt 87,6 % vs net 55,5 % of GDP and dette nette/EBE 2,7×, plus the lesson. Cite *Lettre Vernimmen n° 190, juillet 2021* in `::: aside`.
- [ ] T050 [P] [US3] In `FR/slides/jour-3.qmd`:
  - Block 3.3: a then-now IFRS 16 `:::: {.columns}` slide (leases 82,7 Md€ = 12,5 % of FP for 80 groups, end-2016; source BdF *Actualités comptables*, 23/03/2018) and `> **Focus — Orpéa (2022)**` (dette nette/EBE 3,7× retraité vs 11,4×; *Lettre Vernimmen n° 206, mars 2023*). Add the deck's single `.callout-warning`: post-IFRS 16 EBE combined with debt excluding leases.
  - Block 3.6: `> **Focus — Casino (2023)**` (dette > 6× EBE since 2019, negative FCF since 2017; *Lettre Vernimmen n° 210, juillet 2023*).
- [ ] T051 [P] [US3] In `FR/slides/jour-2.qmd` block 2.8, add a then-now IFRS 5 slide on N-1 restatements (AREVA revenue 5,6 → 1,6 Md€, source BdF *Actualités comptables* 2018).
- [ ] T052 [P] [US3] In `FR/slides/jour-2.qmd` block 2.6, add the Business Model Canvas input block (3–5 slides): quest goal, the 9 blocks as a table, the link to SWOT, and `[Quête 5](../modules/05-cartographes-modele-eco.qmd)` (FR-003a).
- [ ] T053 [P] [US3] In `FR/slides/jour-3.qmd`, add input blocks 3.8 (regulatory watch, Q7: CSRD per F12, IFRS 16, IFRS 18 per F13, AMF; link `../modules/07-veilleurs-marche.qmd`) and 3.9 (ESG, Q9: DPEF → CSRD, ESG channels to ratios, RSE criteria in cotation; link `../modules/09-gardiens-extra-financier.qmd`), each 3–5 slides (FR-003a, FR-019).
- [ ] T054 [P] [US3] In `FR/slides/jour-1.qmd` block 1.2, add the Temple des Bilans level-1 data (bilan, CR and tableau de flux from `FR/modules/01-temple-bilans.qmd` "Niveau 1") as `{.scrollable}` tables, or a link to that page if the tables exceed 2 slides.
- [ ] T055 [US3] Fill the "Source files" and "Quest mapping" sections of `SPEC/coverage-map.md`:
  - Every folder file gets `used` / `partly used` / `not used` + reason. For example: Séminaire = duplicate; `10356_a_path_towards_autonomous_mach.pdf` = irrelevant (misplaced AI paper); 2017/2018 BdF old-scale docs = historical; `Exam INSEEC.*` = out of scope.
  - Map Q1–Q9 to their blocks. Flag Q6 → 3.7 and Q8 → 3.6 as optional pointers for user review (FR-020, FR-003a).

**Checkpoint**: All three decks are content-complete.

---

## Phase 6: User Story 4 — Students revise with the same deck after class (Priority: P4)

**Goal**: Students can reach the decks from the site in two clicks or fewer, every block links to its reference page, and an English stub exists.

**Independent Test**: From `/fr/teaching/financial-analysis/`, open each deck in two clicks or fewer. Every relative link in the decks resolves. The EN stubs link to the FR decks (spec US4 scenarios 1–3).

- [ ] T056 [P] [US4] End every block in `FR/slides/jour-1.qmd` with a `## Pour aller plus loin` slide linking its reference page. Targets: `../modules/formules.qmd`, `../modules/performances.qmd`, `../modules/structure-fi.qmd`, `../modules/01-temple-bilans.qmd`, `../modules/04-arenes-rentabilite.qmd` (FR-024).
- [ ] T057 [P] [US4] Same for `FR/slides/jour-2.qmd`. Targets: `../modules/banque-france.qmd`, `../modules/banque-france-cotation.qmd`, `../modules/02-archives-consolidees.qmd`, `../modules/05-cartographes-modele-eco.qmd`, `../modules/performances.qmd`.
- [ ] T058 [P] [US4] Same for `FR/slides/jour-3.qmd`. Targets: `../modules/structure-fi.qmd`, `../modules/liquidite.qmd`, `../modules/03-detective-diagnostic.qmd`, `../modules/06-conseil-sages.qmd`, `../modules/07-veilleurs-marche.qmd`, `../modules/08-architectes-strategie.qmd`, `../modules/09-gardiens-extra-financier.qmd`.
- [ ] T059 [P] [US4] Create the EN stubs `EN/slides/jour-1.qmd`, `jour-2.qmd` and `jour-3.qmd` per contract §6. Use the titles "Day N — …", a "Translation in progress" slide and a link `/fr/teaching/financial-analysis/slides/jour-N.html`.
- [ ] T060 [US4] Edit `_quarto.yml`:
  - Add the `fr-financial-analysis` sidebar block from contract §7, with `fr/teaching/financial-analysis/index.qmd` first and then the **Diapositives** section with the 3 FR decks.
  - Repair the EN block `id: inseec-finane` to list `teaching/financial-analysis/index.qmd` and a `**Slides**` section with the 3 EN stubs (Constitution II).
- [ ] T061 [US4] In `FR/index.qmd`, add a `## Diapositives` subsection after "Plan des séances" under `# Séances`, as a 3-row table `Jour | Thème | Lien` linking `slides/jour-1.qmd`, `slides/jour-2.qmd` and `slides/jour-3.qmd`. Make no other change (contract §8).
- [ ] T062 [US4] Render `FR/index.qmd`, the 3 decks and the 3 stubs, then run the link check from quickstart §5. Every target must exist under `docs/`.

**Checkpoint**: Decks are published and navigable in both languages.

---

## Phase 7: Polish & cross-cutting concerns

- [ ] T063 [P] Run the static checks from quickstart §3 on `FR/slides/jour-*.qmd`. Each deck needs ≥ 1 `callout-caution`, ≤ 1 `callout-warning` and zero `TODO: à vérifier`, with no `<iframe|<details|style=|date: today>` and the expected `{#exr-` counts (Day 1: 3, Day 2: 3, Day 3: 2). Fix any violations.
- [ ] T064 [P] Check that every slide in `FR/slides/jour-*.qmd` with a year-dependent figure or rebuilt third-party content has an `::: aside` source, and that every formula is followed by a "Ce que mesure…" sentence (FR-013, US4-3).
- [ ] T065 [P] Check that every `::: notes` block in `FR/slides/jour-*.qmd` contains only durations, key filenames and optional hints. **No solutions or numeric answers** (FR-021).
- [ ] T066 Do the visual check from quickstart §6 at 1920×1080 and 1366×768. Add `{.smaller}` or `{.scrollable}` where tables overflow (SC-004).
- [ ] T067 Do the final coverage audit from quickstart §7. Every one of the 102 original slides and every folder file has a row, no fact has `todo`, and 10 figures are spot-checked against their sources. Update the `SPEC/checklists/requirements.md` notes.
- [ ] T068 Full render with `quarto render` (post-render hook included). Confirm it exits 0 and no `_freeze/` entries changed.
- [ ] T069 Instructor dry run of each day with only the deck and the named answer keys (quickstart §8, SC-001). Adjust block minutes in the agendas if a day is off by more than 15 min.

---

## Dependencies & Execution Order

### Phase dependencies
- **Setup (T001–T004)**: no dependencies.
- **Foundational (T005–T016)**: depends on Setup. T014 depends on T012 and T013. T006 depends on T005. T007–T011 write into the T005 file, so append to separate sections.
- **US1 (T017–T026)**: depends on Setup. T021 and T022 reference `SPEC/answer-keys-25pct.md` (T016), but that file can be written afterwards.
- **US2 (T027–T039)**: depends on Foundational (facts F1–F15, definitions) and US1 (block section slides exist).
- **US3 (T040–T055)**: depends on Foundational (case data, definitions) and US1. T045 depends on T012–T014. T046 depends on T014.
- **US4 (T056–T062)**: depends on US1. It can run in parallel with US2 and US3. T062 is best run after US2 and US3 so all links exist.
- **Polish (T063–T069)**: depends on all stories.

### Story dependencies
- US1 is independent once Setup is done, and it is the MVP.
- US2 and US3 both write into the same three deck files, but into **different blocks**. They can run in parallel if each worker owns a deck file (see below), not a story.
- US4 is independent of US2 and US3, except for the final link check.

### Within each story
- Tasks marked [P] touch different deck files, or different blocks of one file that one worker can do sequentially.
- The safest split is one worker per deck file.

---

## Parallel Example

```text
# Foundational research (all independent web/file lookups):
T007 ANC 2020-01 IP  |  T008 cote X  |  T009 chiffres clés  |  T010 IFRS 18
T011 video URL       |  T012 Lectra 2016  |  T013 ConcoursMania 2016

# US1, one worker per deck:
Worker A: T017 → T020 → T023   (jour-1)
Worker B: T018 → T021 → T024   (jour-2)
Worker C: T019 → T022 → T025   (jour-3)

# US2 + US3 combined, one worker per deck:
Worker A (jour-1): T038, T040–T045, T054
Worker B (jour-2): T027–T032, T047, T049, T051, T052
Worker C (jour-3): T033–T037, T048, T050, T053
```

---

## Implementation Strategy

### MVP (User Story 1)
1. Phase 1 Setup, then Phase 2 Foundational (facts and case data are needed by every later layer).
2. Phase 3 US1: three day skeletons with agendas totalling 360 min, briefs and recaps. **Stop and validate**: render, timing sums, and run one day as a dry run.

### Incremental delivery
1. US2 (Days 2–3 reach teachable BdF content), then validate against the coverage map.
2. US3 (Day 1 fundamentals, case data, focus boxes, input blocks), and the decks become content-complete.
3. US4 (sidebar, syllabus links, EN stubs), and the decks are published.
4. Polish, then the dry run.

### Notes
- Day 1 depends mostly on US3. To teach Day 1 early, do T040–T046 right after US1.
- Commit after each task or block. Never commit answer keys into public deck files.
- `SPEC/answer-keys-25pct.md` and `SPEC/case-data-*.md` live under `specs/`, which is not rendered to the public site.
