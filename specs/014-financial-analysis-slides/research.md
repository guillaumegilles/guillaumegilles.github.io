# Phase 0 Research: Financial Analysis Slide Decks

**Date**: 2026-10-18

There are two parts. Part A covers the technical decisions. Part B is the log
of facts checked against current official sources (FR-014a). Part B seeds
`coverage-map.md`.

## Part A: Technical decisions

### A1. Deck location and naming
- **Decision**: Put the decks in `fr/teaching/financial-analysis/slides/jour-1.qmd`, `jour-2.qmd` and `jour-3.qmd`, with a local `slides/_metadata.yml` (`format: revealjs`, theme `../../../../assets/dark-slides.scss`, slide numbers, progress, controls). Put the EN stubs at `teaching/financial-analysis/slides/jour-N.qmd`, with their own `_metadata.yml` using the same theme (relative path `../../../assets/dark-slides.scss`).
- **Rationale**: This copies the working pattern in `fr/teaching/mathematical-fundamentals/slides/`. `fr/teaching/_metadata.yml` warns that mixing `format.html` and RevealJS in one directory produces broken output. Mirrored paths keep the language switcher working (Constitution VI).
- **Alternatives**: Putting the decks at the course root as `jour-N-slides.qmd`, which risks the dual render and clutters an already crowded folder. A single deck was rejected by clarification Q2.

### A2. Diagrams and charts
- **Decision**: Use Quarto's bundled Mermaid 11.12.0 (verified at `/opt/quarto/share/formats/html/mermaid/mermaid.min.js`):
  - `flowchart` for the six-step method, group organigrammes and the consolidation decision tree
  - `xychart-beta` for the distribution of firms by cote and for the ROE vs ROCE leverage line
  - `quadrantChart` or a 2×2 table for the liquidity verdict (horizon × marges de manœuvre)
  - Markdown tables for every grid (SWOT, consolidation methods, cote scales, SIG cascade, goodwill decomposition, qualitative-profile grid)
- **Rationale**: Mermaid renders client-side from text, with no Python execution, no `_freeze/` entries and no third-party requests. It also rebuilds the image-only content (FR-008, FR-022).
- **Alternatives**: Matplotlib via Python, which needs execution and freeze and is heavier. OJS Plot, which may load libraries from a CDN (privacy) and is not needed for static charts. Screenshots, which FR-008 and FR-022 forbid.

### A3. Markup for slide roles (no new CSS)
- **Decision**:
  - Definitions go in `.callout-note`, formulas in `.callout-tip` and derivations in `.callout-caution`.
  - Each deck has at most one `.callout-warning`, for its most common mistake.
  - Unresolved facts get `.callout-important` with "TODO: à vérifier".
  - Exercise briefs use `::: {#exr-slug name="…"}`.
  - Focus boxes are plain Markdown blockquotes that start with **Focus**.
  - Sources go in `::: aside`.
  - Speaker notes (`::: notes`) carry the timing, the answer-key filename and optional-block hints.
  - Dense slides use the built-in `.smaller` or `.scrollable` classes.
- **Rationale**: This follows Constitution V without editing `assets/dark-slides.scss`. Speaker notes keep instructor prompts out of the projected view. Notes are visible in the public HTML, so they contain no solutions (FR-021).

### A4. Videos
- **Decision**: Link, never embed. "Qu'est-ce que la cotation ? | Banque de France" is at https://www.youtube.com/watch?v=VHvdDBbcSn4 (found via search on 2026-10-18). The "C'est quoi la BDF" video still needs its official URL. If none is found, the slide gives the title and publisher (spec edge case).
- **Rationale**: FR-022 and Constitution IV (no third-party embeds).

### A5. Tax-rate convention
- **Decision**: Use 25 % throughout: RNR ≈ ¾ × RCAI and CAFr = ¾ × RCAI + dotations nettes d'exploitation. Each slide says to use the actual tax charge when it is known or when losses or deferred tax distort the rate.
- **Rationale**: The French corporate tax rate has been 25 % since 2022 (CGI art. 219). The original deck already uses ¾ for RNR but ⅔ for CAFr (C1). The keys for CP2 and CP3 use ⅔, so they must be recomputed or flagged in the coverage map (spec edge case).

### A6. One definition per ratio (C6)
- **Decision**: The canonical source is `fr/teaching/financial-analysis/modules/formules.qmd`. Where it is silent, COURS M1 (PCG, BdF Centrale des bilans) wins over LES RATIOS. Specific choices:
  - Rentabilité économique = REX net d'IS / actif économique.
  - Marge commerciale ratio = MC / CA HT.
  - BFR = BFRE + BFRHE.
  - Délai clients includes EENE.
  - Taux d'endettement = endettement financier retraité / FP retraités. The deck explains its link to the simple gearing ratio.
  - Each choice is logged in the coverage map.
- **Rationale**: The course formula sheet already governs the web pages, so the slides stay consistent with them (spec 013, FR-025).

### A7. Day timings
- **Decision**: Each day has 360 min of non-optional content, scheduled 9:00–12:00 and 13:30–16:30. The detailed budgets are in [contracts/day-plans.md](contracts/day-plans.md). Long quests (2 h or more) run as shortened in-class versions, with the full version marked optional.
- **Rationale**: Clarification Q5. Quest durations in the syllabus add up to about 19 h, so trimming is needed.

### A8. Case data for CONCOURSMANIA / LECTRA (FR-017a)
- **Finding**:
  - **Lectra**: Lectra publishes its *Rapport financier 2016*, which includes the *comptes de la société mère* (states p. 154), at https://www.lectra.com/fr/investisseurs/information-financiere/publications/rapports-financiers-annuels?year=2016. The AGM dossier is at https://www.lectra.com/sites/default/files/2021-06/20170428_dossierdactionnaires_agoe.pdf.
  - **ConcoursMania**: The 2016 group press release is online (https://www.klarsen.com/uploads/ALGCM-R%C3%A9sultats-annuels-2016-30-mars-2017.pdf). It shows consolidated figures (RCAI −115,9 K€; RN −473,2 K€). These do **not** match the answer key (RCAI −421; RN −812), so the key is based on the **SA social accounts**, which have not been located yet.
- **Decision**: Retrieve Lectra SA from the Rapport financier 2016. Search the Klarsen/Actiplay investor archive for the ConcoursMania SA 2016 accounts. If they are not found, apply the spec fallback: keep the figures that reconcile with the key and state it on the slide. Every gap is recorded in the coverage map.
- **Risk**: Medium. ConcoursMania (now Klarsen) may only have its social accounts at the greffe, which is paid access.

### A9. Quests without a lecture block
- **Decision**:
  - The FR-003a input blocks are BMC (Q5) on Day 2, regulatory watch (Q7) on Day 3 and ESG/CSRD (Q9) on Day 3.
  - The pointers are Q1 → Day 1 états financiers, Q2 → Day 2 consolidation, Q3 → Day 3 synthesis (optional) and Q4 → Day 1 rentabilité.
  - Q6 → Day 3 cotation decision, as an optional pointer.
  - Q8 → Day 3 liquidité prospective, also as an optional pointer.
- **Rationale**: Q6 and Q8 also lack a full block. The spec allows pointers "where one fits", so the coverage map flags both for the user's review.

## Part B: Verified-fact log (FR-014a)

All checks were made on 2026-10-18. "Folder value" is the value in the course folder or the original deck.

| # | Fact | Folder value | Current value | Source |
|---|------|--------------|---------------|--------|
| F1 | Seuil de cotation (CA) | ≥ 750 K€ | **1 250 K€ since 12 Jan 2025** (the 750 K€ threshold had been unchanged for more than 40 years) | BdF, *Évaluation des performances 2024*, Sept 2025, encadré 1 — https://www.banque-france.fr/system/files/2025-12/FR_Eval_performances_cotation_2025_VClean.pdf |
| F2 | Horizon de la cotation | "3 ans" / "1 à 3 ans" | "un à trois ans" (official page). 3 years is the reference for default statistics | BdF, *Comprendre la cotation et l'indicateur dirigeant* — https://www.banque-france.fr/fr/a-votre-service/entreprises/comprendre-cotation-indicateur-dirigeant; Eval. perf. 2024 |
| F3 | Échelle de cote de crédit | 3++ … 9, P, 0 (deck slide 26, `assets/cote-credit.png`) | 22 positions: 1+, 1, 1-, 2+, 2, 2-, 3+, 3, 3-, 4+, 4, 4-, 5+, 5, 5-, 6+, 6, 6-, 7, 8, P, 0. Eligible: 1+ to 4+ | BdF *Guide de référence* (01/2022) and *5 questions* (11/2021), in the folder |
| F4 | Taux de défaut à 1 an, current scale (firms rated 31/12/2023, observed 2024) | old-scale rates only | 1+ 0,00 % · 1 0,02 % · 1- 0,02 % · 2+ 0,06 % · 2 0,03 % · 2- 0,10 % · 3+ 0,22 % · 3 0,18 % · 3- 0,30 % · 4+ 0,51 % · 4 1,26 % · 4- 1,90 % · 5+ 2,82 % · 5 5,21 % · 5- 3,89 % · 6+ 5,63 % · 6 8,17 % · 6- 15,03 % · 7 20,02 % · 8 27,42 % · **total 1,75 %** (339 191 firms) | Eval. perf. 2024, annexe 2 ("Reproduction autorisée avec mention de la source") |
| F5 | Taux de défaut global | — | 1,75 % at 1 yr · 3,22 % at 2 yrs · 3,68 % at 3 yrs | Eval. perf. 2024, §2.1 |
| F6 | Number of rated firms | 250 000–308 348 | 325 105 at 31/12/2023 (BdF *Chiffres clés*, 01/2024). The edition at 31/12/2024 or later still needs a check | https://www.banque-france.fr/system/files/2024-01/Fiben-cotation-chiffres-cles.pdf |
| F7 | Mandatory consolidation thresholds | 24 M€ bilan / 48 M€ CA / 250 salariés | **30 M€ / 60 M€ / 250** ("grand groupe", art. L.233-17 and D.230-2 C. com.) for years from 1 Jan 2025. 24/48/250 applied up to 31/12/2024 | Décret 2024-152; CNCC EJ 2024-30 and EJ 2024-14 |
| F8 | Consolidation rules | CRC 99-02 | **ANC 2020-01** (abrogates CRC 99-02; years opened from 1 Jan 2021) | ANC 2020-01, art. 1 |
| F9 | Intégration proportionnelle (French GAAP) | "normes françaises uniquement" | Still available under ANC 2020-01 for contrôle conjoint (secondary source). Removed under IFRS 11 since 2013 | Phacet glossary (secondary). **TODO: confirm in the ANC 2020-01 text** (Livre II, Titre II) |
| F10 | Corporate tax rate | 33⅓ % (keys) / 25 % (deck RNR) | 25 % standard rate | CGI art. 219 (rate since 2022) |
| F11 | X cote d'activité (latest accounts too old) | 20 / 21 / 23 months | **TODO: confirm** on the current BdF reference guide. The 2022 guide says 20 months and the 04/2022 flyer says 23 months | — |
| F12 | Extra-financial reporting | DPEF | CSRD, transposed by ordonnance 2023-1142 | Décret 2023-1394 (cited in Décret 2024-152) |
| F13 | IFRS 18 | — | Replaces IAS 1. Mandatory "résultat opérationnel" subtotal and disclosed performance measures. Effective 1 Jan 2027 | IFRS Foundation. **TODO: cite the IASB page during implementation** |
| F14 | BdF video | `.mp4` files in the folder | "Qu'est-ce que la cotation ? \| Banque de France" — https://www.youtube.com/watch?v=VHvdDBbcSn4 | YouTube (BdF channel) |

Open items (F6 latest edition, F9, F11, F13, the C'est quoi la BDF video URL
and the ConcoursMania SA accounts) are implementation tasks. They must be
resolved, or turned into the documented fallbacks, before publishing (SC-003).
