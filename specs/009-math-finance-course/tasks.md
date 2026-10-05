# Tasks: Cours de Mathématiques Financières (M1)

**Input**: Design documents from `specs/009-math-finance-course/`
**Branch**: `009-math-finance-course`
**Date**: 2026-10-04

**Prerequisites**: plan.md ✅ · spec.md ✅ · research.md ✅ · data-model.md ✅ · contracts/ ✅ · quickstart.md ✅

**Tests**: Not explicitly requested — no test tasks generated.

**Organization**: Tasks are grouped by user story to enable independent
implementation and testing of each story increment.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no in-flight dependencies)
- **[Story]**: User story this task belongs to (US1–US5)
- Exact file paths included in every task description

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the French course directory and shared configuration file.

- [x] T001 Create directory `fr/teaching/mathematics-finance/`
- [x] T002 Create `fr/teaching/mathematics-finance/_metadata.yml` with content `lang: fr` so all pages in the directory inherit the French language declaration without per-file repetition

**Checkpoint**: Directory exists and `_metadata.yml` is in place.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Register both course variants in the site navigation and fix the
pre-existing constitution violations on the English page. No user story can render
correctly in the sidebar until this phase is complete.

**⚠️ CRITICAL**: Complete before any user story work begins.

- [x] T003 Refactor `teaching/mathematical-finance/index.qmd` into a proper English stub: replace existing French course-plan content with (a) `lang: en` and `title: "Financial Mathematics"` in front-matter, (b) a `.callout-note` block linking to the French counterpart at `fr/teaching/mathematics-finance/index.qmd`, and (c) a "Full English version coming soon" notice — preserving `image.jpg` reference. See contract in `specs/009-math-finance-course/contracts/page-structure.md` (Contract 5).
- [x] T004 Add two new sidebar blocks to `_quarto.yml` immediately after the existing `fr-mathematical-fundamentals` block: (a) `id: en-mathematics-finance`, title "Financial Mathematics", listing `teaching/mathematical-finance/index.qmd`; (b) `id: fr-mathematics-finance`, title "Mathématiques financières", listing `fr/teaching/mathematics-finance/index.qmd`, the three modules, and a `**Ressources**` section with `glossaire.qmd` and `formulaire.qmd`. See exact YAML in `specs/009-math-finance-course/contracts/url-structure.md`.
- [x] T005 Run `quarto render teaching/mathematical-finance/index.qmd --quiet` and confirm exit code 0 — validates the EN stub renders and the sidebar picks up the file.

**Checkpoint**: Both sidebar blocks are active; EN stub renders without error;
`_quarto.yml` lists all 7 course pages even though most don't exist yet (render
will fail until they are created — that is expected at this stage).

---

## Phase 3: User Story 1 — Syllabus (Priority: P1) 🎯 MVP

**Goal**: A student can navigate to `/fr/teaching/mathematics-finance/` and find
the complete course syllabus — objectives, three-day architecture, and bibliography.

**Independent Test**: `quarto render fr/teaching/mathematics-finance/index.qmd --quiet`
exits 0; the rendered page shows "Bibliographie recommandée" with ≥ 5 references
each having author, title, edition, and publisher.

### Implementation for User Story 1

- [x] T006 [US1] Create `fr/teaching/mathematics-finance/index.qmd` as the course syllabus with the following structure (see Contract 1 in `specs/009-math-finance-course/contracts/page-structure.md`):
  - Front-matter: `title: "Mathématiques financières"`, `lang: fr`, `date-modified: today`, `abstract` with the course guiding question
  - Section **Description du cours**: fil directeur ("Comment comparer, valoriser et arbitrer des flux financiers qui interviennent à des dates différentes ?"), public (M1 école de commerce), volume horaire (18 h / 3 journées), niveau requis (licence math + Excel), format pédagogique (35 % conceptuel / 30 % exercices / 25 % cas / 10 % évaluation)
  - Section **Compétences visées**: two subsections — Compétences techniques (13 items from spec source) and Compétences managériales (6 items)
  - Section **Architecture du cours**: markdown table with 3 rows — Journée / Problématique centrale / Principaux thèmes / Production attendue — linking each journée to its module page
  - Section **Bibliographie recommandée**: 5 references from `specs/009-math-finance-course/research.md` (Devolder/Fox/Vaguener 3e éd. Pearson 2018; Quiry/Le Fur Vernimmen Dalloz 2025; Berk/DeMarzo adapt. fr. 6e éd. Pearson 2024; Parienté Pearson 2016; Brealey/Myers/Allen 14e éd. McGraw-Hill 2023) — each with author(s), *title in italics*, edition, publisher, year
- [x] T007 [US1] Run `quarto render fr/teaching/mathematics-finance/index.qmd --quiet` and confirm exit code 0. Open `docs/fr/teaching/mathematics-finance/index.html` and verify: bibliography section present, architecture table renders, page title correct, `lang="fr"` in rendered `<html>` tag.

**Checkpoint**: US1 fully functional — syllabus renders, sidebar shows "Mathématiques financières" with `index.qmd` as first entry.

---

## Phase 4: User Story 2 — Module 01, Journée 1 (Priority: P1)

**Goal**: A student can read the full Day 1 content — compound interest,
actualization, rate conversion, annuities — work through exercises with collapsible
solutions, and interact with the OJS capitalization/actualization demo.

**Independent Test**: `quarto render fr/teaching/mathematics-finance/module-01.qmd --quiet`
exits 0; rendered page contains at least one OJS demo, at least one collapsible
derivation, and exercises at all three difficulty levels.

### Implementation for User Story 2

- [x] T008 [US2] Create `fr/teaching/mathematics-finance/module-01.qmd` — Journée 1 : Valeur temps de l'argent et suites de flux. Required front-matter: `title: "Journée 1 — Valeur temps de l'argent"`, `lang: fr` (inherited via `_metadata.yml`), `date-modified`. Follow the mandatory section structure from Contract 2 in `specs/009-math-finance-course/contracts/page-structure.md`. Required content per sequence:
  - **Séquence 1 — Introduction et diagnostic** (30 min): choix entre 10 000 € / 11 000 € / 12 500 €; discussion préférence pour le présent, coût d'opportunité, inflation, risque; mini-quiz descriptif (no code)
  - **Séquence 2 — Intérêts simples et composés** (1 h): formules $C_n = C_0(1+ni)$ et $C_n = C_0(1+i)^n$; comparaison des deux régimes; exemple numérique 20 000 € / 4 % / 5 ans; `.callout-caution collapse="true"` with step-by-step derivation of compound interest from first principles; `.callout-warning` for common errors (T-VI required)
  - **Séquence 3 — Actualisation et équivalence financière** (1 h): formules $V_0 = V_n/(1+i)^n$ et $a_n = (1+i)^{-n}$; exemple décisionnel 48 000 € vs 52 000 € à 5 %; discussion on why the discount rate is never neutral
  - **Séquence 4 — Taux proportionnels et taux équivalents** (1 h): formule $i_m = i_a/12$ vs $i_m = (1+i_a)^{1/12}-1$; taux annuel effectif $(1+i_p)^m - 1$; exemple 0,5 % mensuel → 6,17 % annuel; activité binômes (comparer trois offres de placement)
  - **Séquence 5 — Annuités constantes** (1 h 15): valeur acquise $V_n = A(1+i)^n-1)/i$ et valeur actuelle $V_0 = A(1-(1+i)^{-n})/i$; annuités de début de période (factor $(1+i)$); annuités différées (two-step); perpétuité $V_0 = A/i$; perpétuité croissante $V_0 = A_1/(i-g)$; `.callout-tip` with "ligne du temps avant toute formule"
  - **Séquence 6 — Cas pratique** (1 h): entreprise souhaite constituer 500 000 € en 8 ans à 3,5 % — calcul de l'annuité constante ($A = V_n \times i/((1+i)^n-1)$); questions subsidiaires (début de période; taux à 2 %; versements de 50 000 €)
  - **Séquence 7 — Synthèse** (45 min): carte mentale textuelle reliant capitalisation / actualisation / taux / périodicité / annuités / VA / VC; erreurs fréquentes (.callout-warning)
  - **Démonstration interactive OJS** (after Séquence 3 or at start of Séquence 6): embed the OJS skeleton from `specs/009-math-finance-course/research.md` (Demo 1 — capitalisation vs actualisation); sliders for C0, i, n; bar chart comparing capitalised and present values at each period
  - **Exercices Niveau 1** (application directe): at least 2 exercises with `.callout-caution collapse="true"` solutions — e.g., (a) calculate $C_5$ with simple and compound interest for given C0/i, (b) convert monthly rate to effective annual rate
  - **Exercices Niveau 2** (problème contextualisé): at least 1 exercise — e.g., compare two savings offers with different periodicities
  - **Exercices Niveau 3** (étude de cas): at least 1 case study — e.g., plan to build a capital reserve with structured recommendation
- [x] T009 [US2] Run `quarto render fr/teaching/mathematics-finance/module-01.qmd --quiet` and confirm exit code 0. Spot-check rendered HTML: (a) OJS sliders visible, (b) at least one `.callout-caution` with `collapse` button, (c) formulas $C_n$, $V_0$, $a_n$ render correctly, (d) all three exercise levels present.

**Checkpoint**: US2 fully functional — Journée 1 renders independently; OJS demo interactive; solutions collapsible.

---

## Phase 5: User Story 3 — Module 02, Journée 2 (Priority: P2)

**Goal**: A student can read the Day 2 content on loans, amortization tables, actuarial
cost, and bond valuation; interact with the bond-price vs rate OJS demo; and work
through exercises.

**Independent Test**: `quarto render fr/teaching/mathematics-finance/module-02.qmd --quiet`
exits 0; rendered page contains a structured amortization table example, bond valuation
formula, Macaulay duration formula, and the OJS bond-price demo.

### Implementation for User Story 3

- [x] T010 [US3] Create `fr/teaching/mathematics-finance/module-02.qmd` — Journée 2 : Emprunts, coût du financement et obligations. Required front-matter: `title: "Journée 2 — Emprunts et obligations"`, `date-modified`. Required content per sequence:
  - **Séquence 1 — Réactivation des acquis** (30 min): correction du travail intersession; quiz sur les annuités; erreurs fréquentes (confusion capitalisation/actualisation, oubli de conversion du taux, décalage de période, confusion début/fin de période)
  - **Séquence 2 — Emprunt amortissable à annuités constantes** (1 h 15): formule $C_0 = A(1-(1+i)^{-n})/i$ donc $A = C_0 i/(1-(1+i)^{-n})$; structure d'une échéance: $I_t = CRD_{t-1} \times i$, $Am_t = A - I_t$, $CRD_t = CRD_{t-1} - Am_t$; tableau type (6 columns: Période / Capital initial / Intérêts / Amortissement / Annuité / CRD) with numeric example; lecture économique (intérêts élevés en début, amortissement croissant); `.callout-caution collapse="true"` derivation of the annuity formula from the present value of annuities (T-VI)
  - **Séquence 3 — Autres modalités de remboursement** (1 h): (A) amortissement constant $Am = C_0/n$, annuité décroissante; (B) emprunt in fine $I_t = C_0 i$, flux terminal $C_0 i + C_0$; (C) différé partiel et différé total; tableau comparatif (Modalité / Avantage / Inconvénient)
  - **Séquence 4 — Coût réel du crédit et taux actuariel** (1 h): limite du taux nominal (frais de dossier, commission, assurance, garantie); principe actuariel — taux $r$ tel que montant net reçu = $\sum CF_t/(1+r)^t$; exemple 100 000 € avec 2 000 € de frais → base 98 000 €; fonctions Excel (VAN, TRI, TAUX, VPM, VA, VC) avec conventions de signe
  - **Séquence 5 — Introduction aux obligations** (1 h): vocabulaire (valeur nominale, coupon, taux facial, maturité, rendement actuariel, prime/décote); formule de valorisation $P_0 = C(1-(1+r)^{-n})/r + N/(1+r)^n$; relation inverse prix/taux (4 cas: $r$ monte/descend; taux facial = / > taux marché); zéro-coupon $P_0 = N/(1+r)^n$
  - **Séquence 6 — Sensibilité obligataire** (45 min): duration de Macaulay $D_M = \sum t \cdot CF_t/(1+r)^t / P_0$; duration modifiée $D^* = D_M/(1+r)$; approximation $\Delta P/P \approx -D^* \Delta r$; interprétation ($D^* = 4$ → baisse de ~4 % pour +1 pp de taux); limite (relation non linéaire, convexité évoquée)
  - **Séquence 7 — Étude de cas** (1 h): PME finance 600 000 € — trois solutions (annuités constantes / amortissement constant / in fine avec frais); demandé: tableaux d'amortissement, coût total, taux actuariel, analyse trésorerie, recommandation
  - **Démonstration interactive OJS** (after Séquence 5): embed Demo 2 skeleton from `specs/009-math-finance-course/research.md` — sliders for C (coupon), N (nominal), n (maturity), r0 (reference rate); line chart of P0 vs r; red dot at reference rate; dashed line at N; status label (prime/décote/au pair)
  - **Exercices N1/N2/N3** with `.callout-caution collapse="true"` solutions: N1 — calculate amortization table row by row for a 3-period loan; N2 — compare annuités constantes vs in fine for a given scenario; N3 — étude de cas financement multi-critères
- [x] T011 [US3] Run `quarto render fr/teaching/mathematics-finance/module-02.qmd --quiet` and confirm exit code 0. Spot-check: amortization table visible, bond pricing formula renders, OJS sliders present.

**Checkpoint**: US3 functional — Journée 2 renders independently with bond-price demo.

---

## Phase 6: User Story 4 — Module 03, Journée 3 (Priority: P2)

**Goal**: A student can read Day 3 content on cash-flow construction, NPV, IRR, and
risk analysis; interact with the VAN/TRI OJS demo; and work through a full investment
recommendation exercise.

**Independent Test**: `quarto render fr/teaching/mathematics-finance/module-03.qmd --quiet`
exits 0; rendered page contains NPV formula with decision rule, IRR limitations
section, OJS VAN/TRI demo, and a 4-step integrative case.

### Implementation for User Story 4

- [x] T012 [US4] Create `fr/teaching/mathematics-finance/module-03.qmd` — Journée 3 : Choix d'investissement, VAN, TRI et incertitude. Required front-matter: `title: "Journée 3 — Choix d'investissement"`, `date-modified`. Required content per sequence:
  - **Séquence 1 — Construction des flux de trésorerie** (1 h): principe (flux différentiels ≠ résultat comptable); flux initial (acquisition + installation + formation + cession ancien + ΔBFR + fiscal); flux d'exploitation ($= résultat d'exploitation après impôt + dotations$ or $= EBE - impôt théorique - \Delta BFR - investissements$); flux terminal (revente + fiscal + récupération BFR + coûts de fermeture); pièges (charges non décaissées, BFR oublié, double-comptage investissement, intérêts dans flux, valeur résiduelle omise, coûts irrécupérables)
  - **Séquence 2 — Valeur actuelle nette** (1 h): formule $VAN = -I_0 + \sum_{t=1}^n CF_t/(1+k)^t$; règle de décision (VAN > 0 / = 0 / < 0); interprétation économique (VAN de 120 000 € → rembourse + rémunère + surplus); indice de profitabilité $IP = VA_{flux}/I_0 = 1 + VAN/I_0$; `.callout-caution collapse="true"` derivation linking NPV to annuities formula (T-VI)
  - **Séquence 3 — Taux de rentabilité interne** (1 h): définition $0 = -I_0 + \sum CF_t/(1+r)^t$; règle de décision TRI > taux exigé; 4 limites — (1) plusieurs TRI possibles si flux multi-signes, (2) absence de TRI, (3) conflit VAN-TRI (taille / durée / calendrier), (4) hypothèse de réinvestissement irréaliste; message central: en cas de conflit VAN/TRI pour projets mutuellement exclusifs, la VAN prime
  - **Séquence 4 — Délai de récupération et comparaison de projets** (45 min): délai simple (flux cumulés); délai actualisé (flux actualisés cumulés); intérêt (liquidité, simplicité, risque élevé) et limites (ignore flux post-délai, ignore valeur temps, mesure non directe de valeur, seuil arbitraire); comparaison de projets de durées différentes: annuité équivalente $AE = VAN \times k/(1-(1+k)^{-n})$
  - **Séquence 5 — Analyse du risque** (1 h 15): (A) analyse de sensibilité uni-variée (volume, prix, coût variable, I0, BFR, valeur résiduelle, taux d'actualisation); (B) valeur seuil (VAN = 0 → prix minimal, volume minimal, I0 maximal, taux critique); (C) analyse par scénarios (pessimiste / central / optimiste); espérance $E(VAN) = \sum p_s VAN_s$; (D) mesures de dispersion: $Variance = \sum p_s(VAN_s - E(VAN))^2$, $\sigma(VAN) = \sqrt{Variance}$; (E) limites (même VAN espérée ≠ même risque; examiner scénario défavorable, amplitude, probabilité de VAN < 0)
  - **Séquence 6 — Cas intégrateur** (1 h 15): automatisation logistique — données (I0 = 850 000 €, installation = 50 000 €, ΔBFR = 40 000 €, durée = 5 ans, économies annuelles, maintenance, valeur résiduelle, taux); 4 étapes groupes — modélisation (chronologie + flux initial + flux annuels + flux terminal) → évaluation (VAN + TRI + délai simple + délai actualisé + IP) → risque (sensibilité économies, hausse I0, retard, 3 scénarios, variable critique) → recommandation (1 page: crée-t-il de la valeur ? facteur de risque principal ? hypothèse à sécuriser ? décision ?)
  - **Séquence 7 — Évaluation finale** (30 min): questions individuelles portant sur conversion de taux, actualisation, annuités, emprunt, obligation, VAN et TRI; question de synthèse "Pourquoi une décision financière ne peut-elle pas être fondée sur un indicateur unique ?"; grille de décision collective (8 étapes)
  - **Démonstration interactive OJS** (after Séquence 3 or 4): embed Demo 3 skeleton from `specs/009-math-finance-course/research.md` — fixed cash flows array, slider for k (discount rate), line chart VAN(k), red dot at TRI (zero crossing), blue dot at current k, display of current VAN and TRI values
  - **Exercices N1/N2/N3** with collapsible solutions: N1 — calculate NPV and IRR for a simple 3-year project; N2 — compare two mutually exclusive projects of different lengths using equivalent annuity; N3 — integrative investment case with sensitivity analysis and written recommendation
- [x] T013 [US4] Run `quarto render fr/teaching/mathematics-finance/module-03.qmd --quiet` and confirm exit code 0. Spot-check: NPV formula renders, OJS VAN/TRI demo present, IRR limitations section present.

**Checkpoint**: US4 functional — Journée 3 renders independently; OJS VAN/TRI demo interactive.

---

## Phase 7: User Story 5 — Glossaire (Priority: P3)

**Goal**: A student can look up any symbol or term from the course and find its
notation, French definition, and (for Greek letters) pronunciation.

**Independent Test**: `quarto render fr/teaching/mathematics-finance/glossaire.qmd --quiet`
exits 0; rendered page contains ≥ 30 symbol entries and all symbols from the data model.

### Implementation for User Story 5

- [x] T014 [P] [US5] Create `fr/teaching/mathematics-finance/glossaire.qmd` with:
  - Front-matter: `title: "Glossaire — Mathématiques financières"`, `date-modified`
  - Section **Symboles mathématiques**: markdown table with columns Notation / Nom / Définition / Prononciation / Module(s); minimum 30 entries covering all symbols from `specs/009-math-finance-course/data-model.md` (Entity 3): $C_0$, $C_n$, $i$, $n$, $V_0$, $V_n$, $a_n$, $i_m$, $i_a$, $i_p$, $m$, $A$, $Am_t$, $I_t$, $CRD_t$, $P_0$, $C$ (coupon), $N$ (nominal), $r$, $D_M$, $D^*$, $\Delta r$, $I_0$, $CF_t$, $k$, $VAN$, $TRI$, $IP$, $AE$, $E(VAN)$, $\sigma(VAN)$, $p_s$, $g$
  - Section **Termes financiers**: definition list or table for at least: Actualisation, Annuité, Amortissement, BFR (besoin en fonds de roulement), Capitalisation, Convexité, Coupon, CRD (capital restant dû), Duration, Emprunt in fine, Équivalence financière, Flux différentiel, Intérêts composés, Intérêts simples, Obligation, Perpétuité, Prime / Décote, Taux actuariel, Taux équivalent, Taux proportionnel, Valeur acquise, Valeur actuelle, VAN, TRI
- [x] T015 [US5] Run `quarto render fr/teaching/mathematics-finance/glossaire.qmd --quiet` and confirm exit code 0. Count symbol entries — must be ≥ 30.

**Checkpoint**: US5 functional — glossaire renders; all module symbols covered.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Formulaire de référence, full site render, navigation audit.

- [x] T016 [P] Create `fr/teaching/mathematics-finance/formulaire.qmd` with front-matter `title: "Formulaire — Mathématiques financières"`, `date-modified`, and all 10 essential formulas from `specs/009-math-finance-course/data-model.md` (Entity 4) in display LaTeX with their names: Capitalisation / Actualisation / Taux équivalent / Valeur acquise d'annuités / Valeur actuelle d'annuités / Annuité d'un emprunt / Prix d'une obligation / Valeur actuelle nette / Taux de rentabilité interne / Annuité équivalente
- [x] T017 Run `quarto render fr/teaching/mathematics-finance/formulaire.qmd --quiet` and confirm exit code 0; verify all 10 formulas render correctly.
- [x] T018 Run full site render `quarto render` from project root and confirm exit code 0. This validates that `_quarto.yml` sidebar entries all resolve to existing files and no cross-links are broken.
- [x] T019 [P] Navigation audit (quickstart.md Steps 5–6): open `docs/fr/teaching/mathematics-finance/index.html` in a browser or via `quarto preview`; click each sidebar entry; confirm correct pages load; confirm `**Ressources**` section groups glossaire and formulaire.
- [x] T020 [P] OJS demo functional audit (quickstart.md Step 7): in browser, open each of module-01, module-02, module-03; move each demo slider and confirm the chart updates in real time; confirm status labels and value displays update correctly.
- [x] T021 [P] Symbol coverage cross-check: scan module-01, module-02, module-03 for all `$...$` notation used; confirm each is present in `glossaire.qmd`; add any missing entries.
- [x] T022 Commit `_freeze/` and `docs/` directories alongside all `.qmd` source files and `_quarto.yml` edits in a single commit (constitution Principle III — reproducible rendering).

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
  └─► Phase 2 (Foundational) — BLOCKS all user stories
        ├─► Phase 3 (US1 Syllabus P1) — MVP
        │     └─► Phase 4 (US2 Module 01 P1) — extends MVP
        │           ├─► Phase 5 (US3 Module 02 P2)
        │           └─► Phase 6 (US4 Module 03 P2)
        └─► Phase 7 (US5 Glossaire P3) — parallel with US2–US4
              └─► Phase 8 (Polish) — depends on all stories complete
```

### User Story Dependencies

- **US1 (P1)**: Requires Phase 2 (Foundational) complete. No other story dependency.
- **US2 (P1)**: Requires Phase 2 complete. Independent of US1 (different file), but
  logically delivers after US1 (navigation makes sense with syllabus first).
- **US3 (P2)**: Requires Phase 2 complete. Independent of US1/US2 (different file).
  Can be worked in parallel with US2 once Phase 2 is done.
- **US4 (P2)**: Requires Phase 2 complete. Independent of US1/US2/US3 (different file).
  Can be worked in parallel once Phase 2 is done.
- **US5 (P3)**: Requires Phase 2 complete. Can be started in parallel with US2–US4
  (different file), but final symbol coverage check (T021) requires US2–US4 complete.

### Within Each User Story

- Content writing task (T006/T008/T010/T012/T014/T016) → render validation (T007/T009/T011/T013/T015/T017)
- All content tasks work on separate files — no write conflicts.

### Parallel Opportunities

- **T001, T002**: Sequential (T002 needs directory from T001)
- **T003, T004**: Both target different parts of the project; T003 edits one `.qmd`, T004 edits `_quarto.yml` — can be parallelized
- **T008, T010, T012, T014**: All different files — can all be parallelized after Phase 2
- **T016, T019, T020, T021**: All marked [P] — can be parallelized in Polish phase

---

## Parallel Example: All Modules (after Phase 2)

```
# All three day-modules are independent files — parallel execution possible:
Task T008: Write module-01.qmd (Journée 1 — valeur temps de l'argent)
Task T010: Write module-02.qmd (Journée 2 — emprunts et obligations)
Task T012: Write module-03.qmd (Journée 3 — VAN, TRI et risque)
Task T014: Write glossaire.qmd
```

---

## Implementation Strategy

### MVP First (US1 + US2 Only)

1. Complete **Phase 1**: Setup (`_metadata.yml`, directory)
2. Complete **Phase 2**: Foundational (EN stub, `_quarto.yml` sidebar blocks)
3. Complete **Phase 3**: US1 — syllabus `index.qmd`
4. Complete **Phase 4**: US2 — module-01 Journée 1
5. **STOP and VALIDATE**: `quarto render` exits 0; Journée 1 fully accessible from
   syllabus; OJS demo interactive; exercises collapsible.
6. Deploy/preview if ready — students can access 33 % of the course content.

### Incremental Delivery

1. Setup + Foundational → infrastructure ready (T001–T005)
2. Add US1 Syllabus → course entry point live (T006–T007)
3. Add US2 Module 01 → first teaching day live (T008–T009) — MVP!
4. Add US3 Module 02 → second teaching day live (T010–T011)
5. Add US4 Module 03 → complete course live (T012–T013)
6. Add US5 Glossaire → reference resource live (T014–T015)
7. Polish → formulaire, full render, audits (T016–T022)

### Single-Agent Strategy

Work sequentially in priority order: Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8.
Each phase is independently renderable; stop and validate at each checkpoint.

---

## Notes

- `[P]` tasks = different files, no in-flight dependencies — safe to parallelize
- `[USN]` label maps every task to its user story for traceability
- All module pages are independently renderable after Phase 2 (Foundational) is complete
- OJS demo skeletons are in `specs/009-math-finance-course/research.md` — copy and adapt
- Page structure contracts are in `specs/009-math-finance-course/contracts/page-structure.md`
- URL and sidebar YAML are in `specs/009-math-finance-course/contracts/url-structure.md`
- Validation steps are detailed in `specs/009-math-finance-course/quickstart.md`
- Constitution compliance: all 14 checklist items pass (see `specs/009-math-finance-course/plan.md`)
