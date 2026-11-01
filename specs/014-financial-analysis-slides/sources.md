# Source Inventory: Financial Analysis Slide Deck

**Reviewed**: 2026-10-18
**Folder**: `fr/teaching/financial-analysis/` (74 tracked files)
**Purpose**: Evidence base for `spec.md`. Lists every source, what it contributes to the deck, and the conflicts the deck must resolve. Text was extracted with `pdftotext`, `pandoc` and `python-pptx`; image-only slides were inspected visually.

## 1. Primary source — `inseec-analyse-financiere.pptx` (102 slides; `.odp` and `.pdf` are exports of the same deck)

| Part | Slides | Content | Form |
|------|--------|---------|------|
| Title, agenda | 1–2 | "Analyse financière — Guillaume Gilles, Analyste financier"; 3-part agenda | Text |
| 1. Découvrir la Banque de France | 3–21 | BdF institutional deck: 3 missions (stratégie monétaire, stabilité financière, services à l'économie), history 1800 → 2017, key figures, network in France/Europe/international, RSE, gouvernance, contacts | **Image only** (screenshots of an official BdF presentation, figures ~2017–2018) |
| 2. La cotation Banque de France | 22–39 | Intérêt de la cotation; history (1982 FIBEN, 2010, 2014, 2016); cote d'activité table (A–N, X); cote de crédit table (**old scale 3++ … 9, P, 0**); cotation vs notation; « à dire d'expert »; fondements juridiques (L.141-6 CMF, OEEC, ICAS); what the cotation considers; information sources; distribution chart; indicateur dirigeant (000 / 060) | Text + 7 image slides |
| 3. Analyse des comptes consolidés | 40–101 | Notion de groupe, enjeux, seuils de consolidation (24 M€ / 48 M€ / 250), particularités, documentation, entretien de cotation, then **the 6 steps**: (1) environnement / SWOT / organisation juridique-économique-financière; (2) examen critique, méthodes de consolidation table, SCI; (3) performances, RNR; (4) structure financière: FPNR, écart d'acquisition élargi (10× RNR rule), impôts différés (2 worked examples, image), écarts de conversion, minoritaires, retraites, titres hybrides, comptes courants, hors bilan, trésorerie disponible, CAFr; (5) liquidité: 4 phases + final risk matrix; (6) décision de cotation: 4 phases, profil qualitatif grid (image) | Mostly text; tables as native tables |
| Breaks | 56, 66, 78, 84, 94 | "Photo by Helloquence" interlude / "Cas pratique" slide — placeholders for exercises with no exercise content | Image |
| Close | 102 | Merci — BdF / INSEEC logos | Image |

Speaker notes exist on 4 slides only (26, 31, 58, 59), e.g. OEEC default-rate ceilings (cote 3 = 0,10 %, 4+ = 0,40 %, 4 = 1,50 %).

**Gaps in the primary deck**: no fundamentals (bilan, CR, SIG, CAF, bilan fonctionnel, FRNG/BFR/TN), no rentabilité / effet de levier, no tableau de flux, no exercises, no learning objectives, no day structure, no recap slides, no ESG/CSRD despite the syllabus.

## 2. Supporting sources

| File | Type / vintage | Use in deck | Verdict |
|------|----------------|-------------|---------|
| `Séminaire INSEEC - M2 Banque d'affaire….pptx/.pdf` | Earlier version of the primary deck (99 slides, ~2018–19) | Only new item: SWOT content of the image on primary slide 50; idea of a final "Étude de cas" | Duplicate |
| `COURS M1.pdf` | Lecture notes (K. Ravon, 2020), PCG; parts 1–2 only | Day-1 fundamentals: flux, bilan, CR, SIG, retraitements Centrale des bilans (crédit-bail…), CAF (2 methods), bilan fonctionnel, FRNG/BFR/TN, ratios de structure & rotation; Iris crédit-bail example | Core (Day 1) |
| `LES RATIOS.pdf` | Ratio handout, PCG | Ratio families, DuPont | Supporting (some definitions conflict — §4) |
| `Élément sde base de l'analyse financière.docx` | Formula sheet, PCG | SIG, CAF, bilan fonctionnel | Core reference |
| `M1 FIN Démarche de lanalyse financière.pdf` | 1-page plan for consolidated analysis (IFRS view) | EBITDA/EBIT, cash-flow, bilan économique, sectoral info | Supporting (contains FCF = CAF error) |
| `CAS PRATIQUE … ELEMENTS DE BASE.docx` + `CORRIGE …` | Case CONCOURSMANIA / LECTRA 2016, with key | Day-1/2 exercise: SIG, CAF, FRNG, BFR, TN | Core exercise (source statements missing from the énoncé; ratio/appreciation part of the key missing) |
| `Cas pratiques d'analyse financière` (énoncé `.docx`, `.pdf`, corrigé `.docx`; copies also in `exercices/`) | 4 BdF-style cases with key: CP1 SWOT (granulats), CP2 RNR (hotel TV), CP3 FPNR (ultra-frais), CP4 endettement retraité | Day-2/3 exercises aligned with steps 1, 3, 4 | Core exercises (key uses 2/3 tax rate) |
| `Exam INSEEC.pdf/.odt/.docx` | Exam, two variants, no key | Not slide content; exam-briefing slide only | Out of scope (mixes two companies; annex 2 image-only) |
| `exercices/examen-1h.qmd`, `examen-final.qmd` | Current exams (SOLSTICE, VERIDIAN) | Exam-briefing slide only | Out of scope |
| `2017-Entreprises-Le-systeme-de-cotation…pdf`, `BdF cotation.pdf` (2018), `BdF chiffres clés … 2018.pdf`, `BdF évaluation des performances de cotation.pdf` (2018) | BdF documents on the **old scale** | "Before 2022" comparison; how default rates are measured | Outdated for the scale |
| `Banque de France – Entreprises_guide-fiben-ref-cotation.pdf` (01/2022) | Official reference guide, **current 22-position scale** | Authoritative source for cotation slides | Core |
| `…_5questions_cotation.pdf` (11/2021), `…_cotation.pdf` (04/2022) | BdF flyers, current scale with labels | Cote d'activité and cote de crédit tables | Core |
| `…_2022_cotation_chiffres_cles.pdf` | Distribution at 31/12/2022 (308 348 firms) | Distribution chart | Core |
| `…_code_conduite_cotation.pdf` (02/2023) | Ethics, governance, legal basis | 1–2 slides on independence and confidentiality | Supporting |
| `…_bulletin…196…etude-4.pdf` (2014) | ECAF / ICAS / OEEC framework | Legal & Eurosystem framework | Supporting (figures outdated) |
| `…_fiben-segmentation-entrep.pdf`, `Modules FIBEN.docx`, `Diaporama_visites_FIBEN.pdf` (~2023) | FIBEN modules, segmentation, 2022 changes | 1 slide on FIBEN | Supporting |
| `BdF indicateur dirigeant.pdf` (2019) | 000 / 060 rules | Indicateur dirigeant slide | Supporting |
| `5_Les_actualites_comptables_2017.pptx` (BdF, March 2018) | Accounting news 2017 | IFRS 16 (leases = 12,5 % of equity of 80 groups), IFRS 5, IAS 12 — as "then vs now" | Mostly outdated |
| `Vernimmen_lettre_numero_190/206/210.pdf` (2021, 2023) | Newsletters | Focus boxes: gross vs net debt (dette nette/EBE 2,7×), **Orpéa** and IFRS 16 (3,7× vs 11,4×), **Casino** and the 6× dette/EBE threshold, EV vs equity value, inflation | Supporting (case material) |
| `Cest quoi la BDF.mp4` (2 min 23), `La cotation Banque de France.mp4` (1 min 18) | Short BdF videos | Embedded in Day 1 opening | Supporting |
| Images: `Bilan fonctionnel.png`, `cotation2possibilites.png`, `assets/cote-activite.png`, `assets/cote-credit.png`, `helloquence-…jpg`, `image.jpg` | Figures | Reusable; `cote-credit.png` must be checked against the current scale | Supporting |
| `10356_a_path_towards_autonomous_mach.pdf` | Y. LeCun AI position paper (2022) | None | Irrelevant — misplaced file |

## 3. Course pages already in the folder (web reference)

- `index.qmd` — syllabus: 3 days / 9 gamified quests (Q1 Temple des Bilans … Q9 Gardiens de l'Extra-Financier), 6-step method table, RNCP competencies, XP levels, bibliography.
- `modules/01…09-*.qmd` — the 9 quests (briefs, data, deliverables; Q1 has a teacher sheet).
- `modules/banque-france*.qmd`, `performances.qmd`, `structure-fi.qmd`, `liquidite.qmd`, `formules.qmd` — theory pages for steps 3–6 and formula sheet.
- Top-level drafts: `05-structure-fi.qmd`, `analyse-performance.qmd`, `guide-reference.qmd`, `indicateur-dirigreant.qmd` (French, partial duplicates of `modules/`); `financial-stability.qmd`, `monetary-strategy.qmd`, `society-services.qmd`, `preface.qmd` (English text in the French folder; `society-services.qmd` is empty).

## 4. Conflicts the deck must resolve

1. **Tax rate in RNR / CAFr**: primary deck uses RNR = ¾ × RCAI (25 %) but CAFr = RCAI × **⅔** + dotations; Séminaire and CP2/CP3 keys use ⅔ (33,33 %). Current French CIT rate is 25 %.
2. **Cote de crédit scale**: primary deck slide 26 and `assets/cote-credit.png` show the **old scale (3++ … 9)**; since 2022 the scale has 22 positions (1+ … 6-, 7, 8, P, 0), eligible grades 1+ to 4+. The same code means different things on the two scales (e.g. 4+ "assez forte" vs "bonne +").
3. **Default rates**: only old-scale default rates are available in the folder; none for the current scale.
4. **Cote X threshold**: 20, 21 or 23 months depending on the document. **Horizon**: "3 ans" vs "1 à 3 ans".
5. **Firm counts**: 250 000 / 260 000 / ~270 000 / 308 348 depending on vintage.
6. **Ratio definitions differ between sources**: rentabilité économique (REX net d'IS / actif économique vs RN / actif total), marge commerciale (MC / CA vs ventes / coût d'achat), CAF (full method vs RN + dotations), BFR (BFRE + BFRHE vs global), délais clients/fournisseurs, taux d'endettement (brut, net, retraité), capacité de remboursement thresholds.
7. **Regulatory references are dated**: CRC 99-02 (replaced by ANC 2020-01), "appel public à l'épargne", intégration proportionnelle under French GAAP, consolidation thresholds, PCG 1987, DPEF (now CSRD) — to verify and update.
8. **Primary deck vs syllabus**: the deck covers BdF + the 6 steps; the published syllabus is organised as 9 quests over 3 days including rentabilité, Business Model Canvas, listed vs unlisted valuation, regulatory watch, financial planning and ESG, none of which the deck covers.
9. **Institutional slides 3–21** are image-only snapshots of ~2017 BdF material (figures such as staff numbers and history up to 2017).
