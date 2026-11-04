# Data Model: Fictitious Consolidated Accounts (French GAAP)

The "data" is the fictitious group's financial statements. There is no
database: the single source of truth is the generator's parameter file
(`scripts/financial-analysis/dataset_params.*`), and every published
artifact (Excel, PDF, markdown tables, corrigé) is derived from it. Entities
below map to parameter blocks, workbook sheets, and page sections.

## Groupe

| Field | Rule |
|---|---|
| nom | "Groupe AUBÉPINE" (fixed, R4) |
| forme / SIREN | SA, SIREN fictif à 9 chiffres non attribué (verified at implementation) |
| secteur, siège, cotation | Agro-industriel, France, non coté |
| exercices publiés | exactement N-2, N-1, N (Q2 decision) |
| disclaimer | "Données fictives — usage pédagogique uniquement" on every page and file (FR-006) |

## Entité (mère + filiales + associé)

| Field | Rule |
|---|---|
| nom, forme | AUBÉPINE SA (mère); AUBÉPINE NORD SAS, AUBÉPINE SUD SAS, VERGER Export SARL; TERROIR PARTENAIRES SA (associé) |
| % contrôle / % intérêt | NORD 75%, SUD 80%, VERGER 60%, TERROIR 30% |
| méthode d'intégration | IG for filiales (contrôle exclusif), MEE for TERROIR (R2) |
| date d'acquisition, prix des titres | Fixed per entité; drive the écart d'acquisition |

## PosteComptable (per exercice, per entité agrégée)

| Field | Rule |
|---|---|
| libellé | PCG modèle normal (actif immobilisé, circulant, capitaux propres, dettes, etc.) |
| montant (k€) | Entier; signes normalisés (charges négatives au CR) |
| exercice | N-2, N-1 ou N |

**Validation rules (checked by `--check`, FR-003 / SC-001):**

- Bilan: total actif = total passif, for every entity-agrégée and every year.
- CR: résultat net = produits − charges; the bilan's capitaux propres move
  by résultat net − dividendes, year over year.
- Flux: variation de trésorerie du tableau des flux = Δ disponibilités +
  Δ concours bancaires courants between two bilans.
- Consolidation identity: consolidated poste = Σ entités − éliminations
  (documented in the annexe), for every line of bilan and CR.

## OpérationIntragroupe

| Field | Rule |
|---|---|
| type | vente (avec marge en stock), prêt, créance/dette, dividende |
| montant (k€), exercice | Documented in the annexe (FR-004) |
| entités concernées | Both sides named (mère ↔ filiale) |
| traitement | Éliminée en consolidation; MEE associate's intragroup ops only
  affect the quote-part |

## ÉcartAcquisition / IntérêtsMinoritaires

| Field | Rule |
|---|---|
| écart d'acquisition | prix des titres − % contrôle × capitaux propres à l'acquisition;
  presented as an actif immobilisé incorporel in the consolidated bilan |
| minoritaires (bilan) | (1 − % contrôle) × capitaux propres filiale at closing, per year |
| minoritaires (résultat) | (1 − % contrôle) × résultat net filiale, per year |

## AnnexeNote

Sections of the annexe page: principes comptables (CRC 99-02, IG/MEE),
périmètre, écarts d'acquisition, opérations intragroupe, intérêts
minoritaires, événements postérieurs à la clôture (fictitious).

## VarianteEtudiant

| Field | Rule |
|---|---|
| seed | Student ID (string) |
| postes modifiés | Fixed documented list (R5): CA VERGER, stock AUBÉPINE NORD,
  marge intragroupe, dividende NORD |
| règle | Deterministic shift from seed; all dependent statements re-derived;
  variant MUST still pass every validation rule above |
| publicité | Assignment page states variants exist (FR-009); no hidden text |

## Artifact (published file)

| Field | Rule |
|---|---|
| Excel | One workbook `<groupe>-consolide.xlsx`, sheets: Bilan, Compte de
  résultat, Annexe, Flux, Périmètre — one column per exercice (see contracts/) |
| PDF | `<groupe>-consolide.pdf`, same content, presentation format |
| pages | 6 FR pages under `donnees/` + 6 EN stubs; tables generated from the
  same parameters (R3) |
| corrigé | `enseignant/corrige-aubepine.qmd`, figures generated from the same
  parameters; diff vs published = empty (SC-004) |
