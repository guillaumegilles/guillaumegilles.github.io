# Guide de démarrage rapide — Analyse surendettement départemental

**Branche** : `001-surendettement-analysis`  
**Date** : 2026-05-20  
**Temps estimé** : 30–45 min (première exécution, téléchargements inclus)

---

## Prérequis système

- Python 3.11 ou supérieur
- Quarto CLI ≥ 1.4 (voir [quarto.org/docs/get-started](https://quarto.org/docs/get-started/))
- Git
- Connexion Internet (pour les téléchargements de données)
- 500 Mo d'espace disque libre

---

## Étape 1 — Cloner le dépôt et créer l'environnement Python

```bash
# Cloner le dépôt
git clone https://github.com/guillaumegilles/dataviz-bdf.git
cd dataviz-bdf

# Créer et activer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows (PowerShell)

# Installer les dépendances
pip install -r requirements.txt
```

**Contenu de `requirements.txt`** (versions pinnées) :
```
pandas>=2.0,<3.0
geopandas>=0.14,<1.0
matplotlib>=3.8,<4.0
plotly>=5.18,<6.0
statsmodels>=0.14,<1.0
scikit-learn>=1.4,<2.0
requests>=2.31,<3.0
pdfplumber>=0.10,<1.0
openpyxl>=3.1,<4.0
pyarrow>=14.0,<16.0
jupyter>=1.0,<2.0
```

---

## Étape 2 — Télécharger les données brutes

```bash
python scripts/01_download.py
```

Ce script télécharge automatiquement les sources suivantes dans `data/raw/` :

| Source | Destination | Taille estimée |
|---|---|---|
| Synthèses PDF surendettement BdF (2018–2023) | `data/raw/bdf/` | ~30 Mo |
| FiLoSoFi 2021 CSV (INSEE) | `data/raw/filosofi/` | ~5 Mo |
| FiLoSoFi SUPRA 2019 XLSX (Gini) | `data/raw/filosofi/` | ~22 Mo |
| Chômage localisé TCRD (INSEE) | `data/raw/chomage/` | ~2 Mo |
| RP 2021 — ménages, population, logement | `data/raw/rp/` | ~200 Mo |
| Bénéficiaires RSA/prime activité (DREES) | `data/raw/minimas/` | ~5 Mo |
| GeoJSON départements | `data/geo/` | ~600 Ko |

**Durée estimée** : 10–20 min selon la connexion.

> **Note sur le chômage localisé** : Si le téléchargement du fichier TCRD Excel échoue (protection anti-bot INSEE), le script affichera un avertissement et indiquera l'URL manuelle. Dans ce cas, télécharger manuellement depuis `https://www.insee.fr/fr/statistiques/2012804` et placer le fichier dans `data/raw/chomage/`.

---

## Étape 3 — Nettoyer et normaliser les données par source

```bash
python scripts/02_clean.py
```

Ce script produit un fichier CSV nettoyé par source dans `data/processed/` :

| Entrée | Sortie | Opérations |
|---|---|---|
| PDFs BdF | `surendettement.csv` | Extraction tabulaire PDF, jointure codes INSEE |
| `base-cc-filosofi-2021.csv` | `filosofi.csv` | Filtrage lignes département, renommage colonnes |
| `filosofi_supra_2019.xlsx` | `filosofi_gini.csv` | Extraction indice de Gini |
| TCRD chômage | `chomage.csv` | Sélection 96 départements, agrégation trimestrielle → annuelle |
| Bases IC RP 2021 | `rp_menages.csv`, `rp_logement.csv`, `rp_population.csv` | Agrégation IRIS → département (`groupby('DEP').sum()`) |
| RSA / prime activité | `minimas_sociaux.csv` | Calcul taux / population de référence |

---

## Étape 4 — Fusionner et construire le jeu analytique

```bash
python scripts/03_merge.py
```

Ce script :
1. Joint tous les fichiers intermédiaires sur `(dep_code, annee)`
2. Calcule les variables dérivées (lags t-1, taux normalisés, score de fragilité)
3. Exporte `data/processed/analytical_dataset.csv`

**Sortie attendue** :
```
✅ Fusion réussie : 480 lignes × 25 colonnes (96 départements × 5 années)
   Couverture par variable :
     suren_depot_taux : 100.0%
     chomage_taux     :  97.9%
     taux_pauvrete    : 100.0%
     ...
```

---

## Étape 5 — Valider la couverture des données

```bash
python scripts/04_validate.py
```

Ce script vérifie les invariants du jeu analytique et produit `data/processed/coverage_report.csv`. Il affiche :
- Nombre de lignes et colonnes
- Taux de couverture par variable (% de valeurs non manquantes)
- Avertissements si couverture < 90 % pour une variable
- Statistiques descriptives de base (min, max, médiane)

```
📊 Rapport de couverture — analytical_dataset.csv
────────────────────────────────────────────────────
Dimensions : 480 lignes × 25 colonnes
Départements couverts : 96/96
Années couvertes : 2017, 2018, 2019, 2020, 2021

Variable                  Couverture   Min      Max      Médiane
──────────────────────────────────────────────────────────────────
suren_depot_taux          100.0%       1.2      18.4     5.7
chomage_taux               97.9%       3.1      17.2     7.4
...
⚠️ gini : couverture = 20.8% (millésime 2019 uniquement — comportement attendu)
```

---

## Étape 6 — Générer le rapport Quarto

```bash
quarto render index.qmd
```

Ouvre `index.html` dans votre navigateur pour consulter le rapport complet.

**Durée estimée** : 2–5 min (calculs Python + rendu HTML).

> **Note** : Si le rendu échoue avec une erreur de mémoire sur les bases RP volumineuses, vérifier que Python dispose d'au moins 2 Go de RAM disponible.

---

## Structure du projet après exécution complète

```
dataviz-bdf/
├── data/
│   ├── raw/                    # Sources brutes (gitignorées)
│   │   ├── bdf/                # PDFs synthèses surendettement
│   │   ├── filosofi/           # FiLoSoFi ZIP/XLSX
│   │   ├── chomage/            # TCRD chômage localisé
│   │   ├── rp/                 # Bases infracommunales RP 2021
│   │   └── minimas/            # RSA, prime activité
│   ├── processed/              # Jeux nettoyés et jeu analytique final
│   │   ├── surendettement.csv
│   │   ├── filosofi.csv
│   │   ├── chomage.csv
│   │   ├── rp_menages.csv
│   │   ├── rp_logement.csv
│   │   ├── rp_population.csv
│   │   ├── minimas_sociaux.csv
│   │   ├── analytical_dataset.csv   ← jeu analytique principal
│   │   └── coverage_report.csv      ← rapport de couverture
│   └── geo/
│       └── departements.geojson     ← contours simplifiés
├── scripts/
│   ├── 01_download.py
│   ├── 02_clean.py
│   ├── 03_merge.py
│   └── 04_validate.py
├── index.qmd                    ← rapport Quarto principal
├── requirements.txt             ← dépendances pinnées
└── README.md
```

---

## Résolution des problèmes courants

| Problème | Solution |
|---|---|
| `ModuleNotFoundError: geopandas` | Vérifier que l'environnement virtuel est activé (`source .venv/bin/activate`) |
| Erreur PDF extraction (pdfplumber) | Vérifier que le PDF n'est pas protégé par mot de passe ; mettre à jour `pdfplumber` |
| Téléchargement TCRD bloqué (HTTP 500) | Télécharger manuellement sur `https://www.insee.fr/fr/statistiques/2012804` |
| `quarto: command not found` | Installer Quarto CLI depuis `https://quarto.org/docs/get-started/` |
| `CRS error` dans geopandas | Vérifier que le fichier GeoJSON est en EPSG:4326 (voir `data/geo/departements.geojson`) |
| Rendu Quarto > 5 min | Augmenter la RAM Python ou utiliser `quarto render --cache` |

---

## Mise à jour des données

Pour mettre à jour l'analyse avec un millésime plus récent :

1. Vérifier la disponibilité de nouvelles données sur les pages sources
2. Modifier les URLs dans `scripts/01_download.py` (variables `YEAR_TARGET`)
3. Relancer les étapes 2 à 6
4. Documenter le changement de millésime dans la section « Sources » de `index.qmd`
