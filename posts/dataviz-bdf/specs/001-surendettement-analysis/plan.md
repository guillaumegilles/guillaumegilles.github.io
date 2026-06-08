# Plan d'implémentation — MVP Choroplèthes Surendettement & Chômage

**Branche** : `001-surendettement-analysis` | **Date** : 2026-05-20 | **Spec** : `specs/001-surendettement-analysis/spec.md`

**Input** : Spécification de la feature dans `specs/001-surendettement-analysis/spec.md`

---

## Résumé

MVP centré sur la **visualisation cartographique** de deux variables : le nombre de dépôts de dossiers de surendettement (BdF WebStat ODS) et le taux de chômage localisé (INSEE), l'un et l'autre représentés par des **cartes choroplèthes** au niveau départemental avec intensité de couleur proportionnelle à la valeur. Le livrable est un rapport Quarto HTML interactif (`index.qmd`) avec deux cartes côte à côte par Plotly, conforme au Scénario 4 et aux exigences FR-001, FR-003, FR-020, FR-021, FR-024.

Cette première version MVP permet de valider :
- la chaîne de données de bout en bout (téléchargement → nettoyage → fusion → visualisation)
- la qualité visuelle des cartes (Constitution IV)
- la reproductibilité du pipeline (Constitution II)

Les analyses EDA, modélisation OLS, score composite et comparaisons temporelles sont hors périmètre du MVP mais tracées dans les specs pour implémentation ultérieure.

---

## Technical Context

**Language/Version** : Python 3.11

**Primary Dependencies** :
- `pandas >= 2.0` — manipulation de données tabulaires
- `geopandas >= 0.14` — jointure spatiale (optionnel pour MVP, utilisé pour validation)
- `plotly >= 5.18` — cartes choroplèthes interactives (Quarto HTML natif)
- `requests >= 2.31` — téléchargement API BdF ODS + INSEE
- `openpyxl >= 3.1` — lecture des fichiers XLS/XLSX INSEE (chômage)
- `pyarrow >= 14.0` — sérialisation Parquet des datasets intermédiaires

**Storage** :
- `data/raw/` — fichiers bruts téléchargés (CSV, XLS, GeoJSON) — non modifiés, gitignorés
- `data/processed/` — fichiers nettoyés par source + `analytical_dataset_mvp.csv`
- `data/geo/` — `departements.geojson` (gregoiredavid/france-geojson, version simplifiée)

**Testing** : `scripts/04_validate.py` — validation de couverture, cohérence des codes département, absence de NaN sur les variables MVP

**Target Platform** : HTML statique via Quarto CLI ≥ 1.4, publié sur le site du projet

**Project Type** : rapport d'analyse de données — pipeline ETL scriptable + document Quarto

**Performance Goals** : aucun temps de réponse en ligne — rapport généré offline, temps de rendu Quarto < 5 min pour le MVP

**Constraints** :
- Données publiques uniquement (BdF WebStat, INSEE) — aucun accès privilégié
- 96 départements de France métropolitaine (DOM-TOM hors périmètre — FR-010)
- Aucune modification manuelle des données brutes (Constitution I)
- Valeurs dans le rapport générées programmatiquement (Constitution II)

**Scale/Scope** : MVP = 96 départements × 1 année de référence (2021 ou millésime commun le plus récent) × 2 variables

---

## Constitution Check

*GATE : Vérifié avant Phase 0, re-vérifié après Phase 1.*

| Principe | Statut | Note |
|---|---|---|
| **I. Data Integrity First** | ✅ PASS | Données BdF via API WebStat ODS (script `01_download.py`), INSEE via téléchargement direct. Aucune modification manuelle. Lineage documentée dans `data-model.md`. |
| **II. Reproducibility** | ✅ PASS | Pipeline complet via 4 scripts versionnés (`01_download.py` → `04_validate.py`), `requirements.txt` avec versions pinnées, `quickstart.md` documenté. |
| **III. Transparent Methodology** | ✅ PASS | Choix de Plotly (vs matplotlib) documenté dans `research.md §7`. Échelles de couleur choisies (YlOrRd / Blues, colorblind-safe) justifiées. Jointure sur `properties.code` de gregoiredavid/france-geojson documentée. |
| **IV. Visualization Clarity** | ✅ PASS | Chaque carte devra comporter : titre descriptif, légende avec unités, mention de la source+année, phrase de conclusion (caption) — cf. FR-024. Contrôlé à la revue du rendu Quarto. |
| **V. Scope Discipline** | ✅ PASS | MVP limité à 2 variables (surendettement + chômage), niveau département, 1 millésime. Toute extension doit passer par une nouvelle spec ou une clarification de celle-ci. |

**Post-Phase 1 re-check** : ✅ Aucune violation détectée après conception. Le modèle de données MVP (`analytical_dataset_mvp.csv`) et les contrats de visualisation sont cohérents avec les 5 principes.

---

## Project Structure

### Documentation (this feature)

```text
specs/001-surendettement-analysis/
├── plan.md              # Ce fichier
├── research.md          # Décisions techniques (sources, libs, visualisation)
├── data-model.md        # Schéma du jeu analytique complet
├── quickstart.md        # Guide de démarrage (reproduire le pipeline)
├── contracts/
│   └── data-contracts.md  # Contrats de format CSV + schéma choroplèthe
└── tasks.md             # Généré par /speckit.tasks (non créé ici)
```

### Source Code (repository root)

```text
data/
├── raw/                    # Données brutes gitignorées
│   ├── surendettement_bdf.csv       # API BdF WebStat ODS (01_download.py)
│   ├── chomage_insee.xls            # INSEE TCRD (01_download.py)
│   └── departements.geojson         # gregoiredavid/france-geojson (01_download.py)
├── processed/              # Données nettoyées et fusionnées
│   ├── surendettement.csv           # 02_clean.py
│   ├── chomage.csv                  # 02_clean.py
│   ├── analytical_dataset_mvp.csv   # 03_merge.py (MVP : 96 lignes × ~8 colonnes)
│   └── coverage_report.csv          # 04_validate.py
└── geo/
    └── departements.geojson         # copie locale (01_download.py)

scripts/
├── 01_download.py          # Téléchargement BdF ODS + INSEE + GeoJSON
├── 02_clean.py             # Nettoyage et normalisation par source
├── 03_merge.py             # Fusion → analytical_dataset_mvp.csv
└── 04_validate.py          # Vérification couverture 96 départements

index.qmd                   # Rapport Quarto — cartes choroplèthes MVP
requirements.txt            # Dépendances pinnées
README.md                   # Documentation principale
```

**Structure Decision** : Pipeline ETL en 4 scripts séquentiels, un seul rapport Quarto (`index.qmd`). Pas de sous-package Python — scripts autonomes appelables en ligne de commande. Conforme aux conventions du projet existant.

---

## Complexity Tracking

> Aucune violation constitutionnelle à justifier pour le MVP.
