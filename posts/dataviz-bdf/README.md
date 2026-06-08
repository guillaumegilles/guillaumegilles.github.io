# dataviz-bdf — Inclusion financière des ménages français

Analyse de la corrélation entre les conditions économiques départementales
(chômage, pauvreté, minimas sociaux, logement, démographie) et le taux de
surendettement des ménages en France métropolitaine (96 départements).

**Périmètre** : 96 départements métropolitains | **Période** : 2018–2024 | **Sources** : BdF, INSEE, DREES

## Résultats

Consulter le rapport Quarto : `index.html` (après exécution du pipeline).

Le rapport comprend :
- Tableau des sources et couverture des données manquantes
- Analyse exploratoire : matrice de corrélations, distributions, tendances temporelles
- Modélisation OLS avec diagnostics VIF et comparaison des spécifications avec/sans lag t-1
- Cartographie choroplèthe : surendettement, évolution 2018–2021, variables explicatives, score de fragilité

## Installation

```bash
git clone https://github.com/guillaumegilles/dataviz-bdf.git
cd dataviz-bdf
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows (PowerShell)
pip install -r requirements.txt
```

**Prérequis** : Python ≥ 3.11, Quarto CLI ≥ 1.4, Git, connexion Internet (~250 Mo pour les données brutes).

## Données

Les données brutes (`data/raw/`) ne sont **pas versionnées** (`.gitignore`) afin de respecter les conditions
d'utilisation des sources et d'éviter l'archivage de fichiers volumineux dans le dépôt.
Le jeu analytique final (`data/processed/analytical_dataset.csv`) n'est pas non plus versionné.

Voir le [guide de démarrage rapide](specs/001-surendettement-analysis/quickstart.md) pour reproduire l'intégralité du pipeline.

> ⚠️ Si le téléchargement du chômage localisé INSEE échoue (protection anti-bot HTTP 500),
> télécharger manuellement depuis <https://www.insee.fr/fr/statistiques/2012804>
> et placer le fichier dans `data/raw/chomage/`.

## Exécution

Lancer les 5 commandes dans l'ordre depuis la racine du projet :

```bash
python scripts/01_download.py   # 1. Téléchargement BdF + INSEE + GeoJSON (~10-20 min)
python scripts/02_clean.py      # 2. Nettoyage et normalisation par source
python scripts/03_merge.py      # 3. Fusion → data/processed/analytical_dataset.csv
python scripts/04_validate.py   # 4. Validation couverture → data/processed/coverage_report.csv
quarto render index.qmd         # 5. Génération du rapport HTML (~2-5 min)
```

Ouvrir `index.html` dans un navigateur pour consulter le rapport.

## Mise à jour des données

Pour mettre à jour l'analyse avec un millésime plus récent :

1. Vérifier la disponibilité des nouvelles données sur les pages sources (BdF, INSEE, DREES)
2. Modifier la variable `YEAR_TARGET` dans `scripts/01_download.py`
3. Relancer les étapes 2 à 5 ci-dessus
4. Contrôler les points suivants :
   - `scripts/04_validate.py` s'exécute sans erreur fatale
   - `data/processed/analytical_dataset.csv` contient 96 lignes × 1 millésime minimum
   - La section « Sources » dans `index.qmd` reflète les nouveaux millésimes
5. **Note anti-bot chômage** : si le téléchargement TCRD échoue, le script affiche l'URL et attend un téléchargement manuel (voir `H-01` dans la spec)

## Structure

```
data/raw/                    # Sources brutes (gitignorées, ~250 Mo)
  bdf/                       # PDFs synthèses surendettement BdF
  filosofi/                  # FiLoSoFi INSEE (revenus, pauvreté)
  chomage/                   # TCRD chômage localisé INSEE
  rp/                        # Recensement population 2021
  minimas/                   # RSA, prime activité (DREES)
data/processed/              # Données nettoyées et jeu analytique final
  analytical_dataset.csv     # Jeu analytique principal (96 dép. × n années)
  coverage_report.csv        # Rapport de couverture des variables
data/geo/
  departements.geojson       # Contours simplifiés (gregoiredavid/france-geojson)
scripts/
  01_download.py             # Téléchargement de toutes les sources
  02_clean.py                # Nettoyage et normalisation par source
  03_merge.py                # Fusion et calcul du score de fragilité
  04_validate.py             # Validation du contrat de données
index.qmd                    # Rapport Quarto (source de vérité)
requirements.txt             # Dépendances Python pinnées
specs/                       # Spécifications et documentation technique
```

## Références

- [Constitution du projet](.specify/memory/constitution.md)
- [Spécification](specs/001-surendettement-analysis/spec.md)
- [Plan technique](specs/001-surendettement-analysis/plan.md)
- [Guide de démarrage rapide](specs/001-surendettement-analysis/quickstart.md)
- [Contrats de données](specs/001-surendettement-analysis/contracts/data-contracts.md)
