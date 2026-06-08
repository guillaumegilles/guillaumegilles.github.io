# Modèle de données — Analyse surendettement départemental

**Phase** : 1 — Conception  
**Branche** : `001-surendettement-analysis`  
**Date** : 2026-05-20  
**Dépend de** : `research.md`

---

## Vue d'ensemble

Le modèle analytique est un **panel département × millésime** (données de coupe transversale enrichies de quelques années pour l'analyse temporelle et les effets de lag). L'unité d'observation finale est `(dep_code, annee)`.

```
┌─────────────────────────────────────────────────────────────────┐
│  7 sources brutes (CSV / PDF / HTML)                            │
│    BdF · INSEE FiLoSoFi · INSEE Chômage · INSEE RP              │
│    DREES · France Travail · geo.api.gouv.fr                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │ scripts/01_download.py
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  data/raw/   (fichiers bruts, gitignorés, non modifiés)         │
└──────────────────────────────┬──────────────────────────────────┘
                               │ scripts/02_clean.py
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  data/processed/  (fichiers nettoyés par source)                │
│   surendettement.csv · filosofi.csv · chomage.csv               │
│   rsa.csv · logement.csv · socio_demo.csv · ficp.csv            │
└──────────────────────────────┬──────────────────────────────────┘
                               │ scripts/03_merge.py
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  data/processed/analytical_dataset.csv  (modèle analytique)    │
│   96 × N_annees lignes · ~25 colonnes                           │
└──────────────────────────────┬──────────────────────────────────┘
                               │ scripts/04_validate.py
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  data/processed/coverage_report.csv  (rapport couverture)       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Schéma du jeu de données analytique

### Table principale : `analytical_dataset.csv`

Clé primaire : `(dep_code, annee)`  
Granularité : département × année (96 départements × 2017–2021 = jusqu'à 480 lignes)

#### Identifiants géographiques

| Colonne | Type | Description | Source |
|---|---|---|---|
| `dep_code` | `str(2)` | Code INSEE département (`"01"` à `"95"`, `"2A"`, `"2B"`) | INSEE |
| `dep_nom` | `str` | Nom du département | INSEE |
| `reg_code` | `str(2)` | Code INSEE région (optionnel, pour agrégation) | INSEE |
| `annee` | `int` | Année de référence (ex. `2021`) | Calculé |

#### Variable cible

| Colonne | Type | Unité | Source | FR |
|---|---|---|---|---|
| `suren_depot_taux` | `float` | Dépôts pour 1 000 ménages | BdF Synthèse PDF | FR-001 |
| `suren_depot_nb` | `int` | Nombre absolu de dossiers déposés | BdF Synthèse PDF | FR-001 |

Note : `suren_depot_taux = suren_depot_nb / (nb_menages / 1000)`. La population de ménages de référence est issue du RP INSEE.

#### Chômage (FR-003)

| Colonne | Type | Unité | Source |
|---|---|---|---|
| `chomage_taux` | `float` | Taux de chômage BIT localisé (%) | INSEE TCRD |
| `chomage_taux_t1` | `float` | `chomage_taux` à t-1 (lag 1 an) | Calculé |

#### FiLoSoFi — revenus et pauvreté (FR-004)

| Colonne | Type | Unité | Source |
|---|---|---|---|
| `revenu_median_uc` | `float` | Revenu médian disponible par UC (€/an) | INSEE FiLoSoFi `MED21` |
| `taux_pauvrete` | `float` | Taux de pauvreté au seuil de 60 % (%) | INSEE FiLoSoFi `TP6021` |
| `taux_pauvrete_t1` | `float` | `taux_pauvrete` à t-1 | Calculé |
| `interdecile_d9d1` | `float` | Rapport D9/D1 (proxy inégalités) | INSEE FiLoSoFi `GI21` |
| `gini` | `float` | Indice de Gini (si disponible) | INSEE SUPRA 2019 — peut être `NaN` pour autres années |

#### Minimas sociaux (FR-005)

| Colonne | Type | Unité | Source |
|---|---|---|---|
| `rsa_taux` | `float` | Allocataires RSA / population 15–64 ans (%) | DREES / France Travail |
| `prime_activite_taux` | `float` | Bénéficiaires prime d'activité / population active (%) | DREES / France Travail |
| `ass_aspa_taux` | `float` | Allocataires ASS+ASPA / demandeurs d'emploi (%) | France Travail |

#### Logement (FR-006)

| Colonne | Type | Unité | Source |
|---|---|---|---|
| `part_locataires` | `float` | Part des ménages locataires (%) | INSEE RP `P21_RP_LOC / P21_RP` |
| `part_hlm` | `float` | Part du logement social HLM (%) | INSEE RP `P21_RP_LOCHLMV / P21_RP` |
| `taux_surpeuplement` | `float` | Taux de surpeuplement des résidences principales (%) | INSEE RP ou DREES |
| `taux_effort_logement` | `float` | Taux d'effort médian au logement (%) | DREES / données data.gouv.fr |

#### Socio-démographique (FR-007)

| Colonne | Type | Unité | Source |
|---|---|---|---|
| `part_familles_mono` | `float` | Part des familles monoparentales / ensemble familles (%) | INSEE RP `C21_FAMMONO / (C21_FAMMONO + C21_COUPAENF)` |
| `part_25_54` | `float` | Part de la population âgée de 25 à 54 ans (%) | INSEE RP |
| `part_65plus` | `float` | Part de la population âgée de 65 ans et plus (%) | INSEE RP |
| `part_menages_1pers` | `float` | Part des ménages unipersonnels (%) | INSEE RP `C21_MENPSEUL / C21_MEN` |

#### FICP / FCC (FR-002)

| Colonne | Type | Unité | Source |
|---|---|---|---|
| `ficp_taux` | `float` | Taux d'inscription au FICP pour 1 000 habitants majeurs | BdF OIB / Synthèse |
| `fcc_taux` | `float` | Taux d'inscription au FCC pour 1 000 habitants majeurs | BdF OIB / Synthèse |

Note : Si non disponibles au niveau département, ces colonnes seront renseignées à `NaN` avec une note dans les métadonnées.

#### Score composite de fragilité (FR-022)

| Colonne | Type | Description |
|---|---|---|
| `score_fragilite` | `float` | Score = `chomage_z×0,3 + taux_pauvrete_z×0,3 + rsa_taux_z×0,2 + part_locataires_z×0,2` (z-scores) |

Calculé dans `scripts/03_merge.py` après normalisation z-score des 4 composantes.

#### Variables de normalisation

| Colonne | Type | Description |
|---|---|---|
| `nb_menages` | `int` | Nombre de ménages du département (RP INSEE) |
| `population` | `int` | Population municipale (RP INSEE) |
| `population_majeurs` | `int` | Population de 18 ans et plus |

---

## Conventions de nommage

- **snake_case** partout
- Suffixe `_taux` → proportion ou taux (%)
- Suffixe `_nb` → comptage absolu
- Suffixe `_z` → variable normalisée z-score (moyenne 0, écart-type 1)
- Suffixe `_t1` → variable décalée d'un an (lag = 1)
- Suffixe `_uc` → par unité de consommation (équivalent adulte)
- Préfixe `suren_` → variable liée au surendettement
- Préfixe `ficp_` / `fcc_` → variables d'incidents de crédit
- Les codes de source INSEE dans les colonnes intermédiaires conservent les noms d'origine (`MED21`, `TP6021`, `GI21`, etc.) pour la traçabilité, puis sont renommés avant export dans le jeu analytique

---

## Relations entre sources

```
BdF PDF (suren_depot_nb)
        │
        │ normalisation par nb_menages (RP)
        ▼
analytical_dataset  ←── INSEE FiLoSoFi (revenu, pauvreté, D9/D1)
        │           ←── INSEE TCRD (chomage)
        │           ←── INSEE RP (logement, socio-démographique, nb_menages)
        │           ←── DREES / France Travail (RSA, prime activité)
        │           ←── BdF OIB (ficp, fcc — si disponible)
        │
        └── data/geo/departements.geojson  (jointure spatiale pour les cartes)
```

---

## Gestion des données manquantes

### Stratégie par type de variable

| Cas | Traitement |
|---|---|
| Département absent d'une source pour 1 année | `NaN` — documenté dans `coverage_report.csv` |
| Variable FICP/FCC indisponible au niveau département | Colonne entière `NaN` + note dans métadonnées |
| Gini absent pour millésimes ≠ 2019 | `NaN` — utiliser `interdecile_d9d1` comme proxy dans les modèles |
| Chevauchement de millésimes incomplet (ex. suren 2021, RSA 2022) | Utiliser le millésime le plus proche, documenter le décalage dans `FR-008` |
| VIF élevé dû à multicolinéarité | ACP ou sélection de variables (documentée cf. FR-017, FR-018) |

### Critère de couverture (SC-001)
Toute variable avec couverture < 90 % des 96 départements (soit < 87 départements avec valeur non manquante) déclenche un **avertissement** dans `04_validate.py` et est signalée dans la section « Couverture des données » du rapport Quarto.

### Imputation
**Pas d'imputation statistique** dans cette version. Les valeurs manquantes restent `NaN`. Si le taux de manquants est > 10 % pour une variable, une note explicite figure dans le rapport.

---

## Transitions d'état du pipeline

```
raw/         → processed/   (02_clean.py)
  TÉLÉCHARGÉ       NETTOYÉ
  
processed/   → analytical_dataset.csv   (03_merge.py)
  NETTOYÉ          FUSIONNÉ + CALCULÉ (lags, score fragilité)
  
analytical   → rapport Quarto            (index.qmd)
  FUSIONNÉ         ANALYSÉ + VISUALISÉ
```

---

## Fichiers intermédiaires (data/processed/)

| Fichier | Clé | Variables principales |
|---|---|---|
| `surendettement.csv` | `(dep_code, annee)` | `suren_depot_nb` |
| `filosofi.csv` | `(dep_code, annee)` | `revenu_median_uc`, `taux_pauvrete`, `interdecile_d9d1`, `gini` |
| `chomage.csv` | `(dep_code, annee, trimestre)` | `chomage_taux` — agrégé annuellement par moyenne des 4 trimestres |
| `rp_menages.csv` | `(dep_code, annee)` | `nb_menages`, `part_menages_1pers`, `part_familles_mono`, `population` |
| `rp_logement.csv` | `(dep_code, annee)` | `part_locataires`, `part_hlm`, `taux_surpeuplement` |
| `rp_population.csv` | `(dep_code, annee)` | `part_25_54`, `part_65plus`, `population_majeurs` |
| `minimas_sociaux.csv` | `(dep_code, annee)` | `rsa_taux`, `prime_activite_taux`, `ass_aspa_taux` |
| `ficp_fcc.csv` | `(dep_code, annee)` | `ficp_taux`, `fcc_taux` |

Chaque fichier intermédiaire inclut une colonne `source_url` et `source_millesime` pour la traçabilité (FR-008).

---

## Variables du modèle OLS de base (FR-015)

| Variable | Rôle | Signe attendu (littérature) |
|---|---|---|
| `chomage_taux` | Prédicteur principal | `+` |
| `revenu_median_uc` | Prédicteur | `–` |
| `taux_pauvrete` | Prédicteur | `+` |
| `rsa_taux` | Prédicteur | `+` |
| `part_locataires` | Prédicteur | `+` |
| `part_familles_mono` | Prédicteur | `+` |
| `suren_depot_taux` | Variable dépendante (Y) | — |
