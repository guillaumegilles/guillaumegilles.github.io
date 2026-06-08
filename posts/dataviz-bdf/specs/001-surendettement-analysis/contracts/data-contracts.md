# Contrats de données — Analyse surendettement départemental

**Phase** : 1 — Conception  
**Branche** : `001-surendettement-analysis`  
**Date** : 2026-05-20  
**Dépend de** : `research.md`, `data-model.md`

---

## 1. Contrats d'entrée — Sources brutes

Ces contrats définissent le format attendu de chaque source à l'entrée du pipeline. Si une source ne respecte pas ces contrats, `scripts/02_clean.py` doit lever une exception explicite et arrêter le traitement.

### 1.1 Synthèses annuelles BdF — Surendettement (FR-001)

**Fichiers** : `data/raw/bdf/synthese_{annee}.pdf`  
**Format** : PDF (extraction tabulaire via `pdfplumber`)

| Champ attendu dans le tableau PDF | Type | Description |
|---|---|---|
| Nom du département | `str` | Ex. `"Ain"`, `"Val-de-Marne"`, `"Corse-du-Sud"` |
| Nombre de dossiers déposés | `int` | Comptage annuel brut |
| Rang national (optionnel) | `int` | Non utilisé dans l'analyse |

**Invariants** :
- Exactement 96 lignes de données (France métropolitaine uniquement)
- Valeurs numériques de dépôts > 0 pour tous les départements
- Aucune ligne `NaN` sur la colonne de comptage
- Correspondance nom → code INSEE via table de référence `data/processed/dep_ref.csv`

**Validation dans `02_clean.py`** :
```python
assert len(df_suren) == 96, f"Attendu 96 départements, obtenu {len(df_suren)}"
assert df_suren['depot_nb'].notna().all(), "Valeurs manquantes dans les dépôts"
```

---

### 1.2 FiLoSoFi — base-cc (INSEE, FR-004)

**Fichier** : `data/raw/filosofi/base-cc-filosofi-{annee}.csv`  
**Source** : `https://www.insee.fr/fr/statistiques/fichier/7756729/base-cc-filosofi-2021-geo2024_csv.zip`

| Colonne INSEE | Colonne analytique | Type | Unité |
|---|---|---|---|
| `CODGEO` | Filtre → `dep_code` | `str(2-5)` | Code INSEE commune/EPCI/DEP |
| `LIBGEO` | `dep_nom` | `str` | Nom |
| `MED{yy}` | `revenu_median_uc` | `float` | €/an par UC |
| `TP60{yy}` | `taux_pauvrete` | `float` | % ménages sous seuil 60% |
| `GI{yy}` | `interdecile_d9d1` | `float` | Ratio D9/D1 (≥ 1.0) |

**Filtrage** : Conserver uniquement les lignes où `CODGEO` est un code département à 2 caractères (`len == 2` ou match `^[0-9]{2}$|^2[AB]$`).

**Invariants** :
- `MED{yy}` : valeur entre 10 000 et 40 000 €/an (plage France métropolitaine)
- `TP60{yy}` : valeur entre 0 et 50 %
- `GI{yy}` ≥ 1.0 (ratio interdécile toujours ≥ 1)
- 96 lignes après filtrage sur les codes département

---

### 1.3 FiLoSoFi SUPRA — Gini (INSEE, FR-004)

**Fichier** : `data/raw/filosofi/filosofi_supra_{annee}.xlsx`  
**Source** : `https://www.insee.fr/fr/statistiques/fichier/6036907/indic-struct-distrib-revenu-2019-SUPRA.zip`

| Colonne | Type | Description |
|---|---|---|
| Code géographique | `str` | Filtre sur codes département |
| Indice de Gini | `float` | Valeur entre 0.25 et 0.50 pour les départements français |

**Note** : Millésime 2019 uniquement pour la Gini. Pour les autres années, `gini = NaN`.

---

### 1.4 Chômage localisé (INSEE, FR-003)

**Fichier** : `data/raw/chomage/tcrd_{edition}.xlsx` OU données scrapées  
**Source** : `https://www.insee.fr/fr/statistiques/2012804` (page HTML) ou fichier TCRD

| Colonne attendue | Type | Description |
|---|---|---|
| Code ou nom département | `str` | Identifiant de l'unité géographique |
| Taux de chômage BIT (%) | `float` | Trimestriel ou annuel |
| Période | `str`/`int` | Trimestre ou année |

**Invariants** :
- 96 départements métropolitains + éventuellement 4 DOM (à exclure)
- `chomage_taux` : valeur entre 2 % et 25 %
- Agrégation annuelle = moyenne des 4 trimestres disponibles

---

### 1.5 Recensement de la Population — Bases infracommunales (INSEE RP 2021, FR-006, FR-007)

**Fichiers** :
```
data/raw/rp/base-ic-menages-2021.csv     (ménages, familles monoparentales)
data/raw/rp/base-ic-population-2021.csv  (structure par âge)
data/raw/rp/base-ic-activite-2021.csv    (activité — si nécessaire)
data/raw/rp/base-ic-logement-2021.csv    (logement, statut occupation)
```

| Colonne source (ménages) | Signification |
|---|---|
| `DEP` | Code département (2 chars) — clé d'agrégation |
| `C21_MEN` | Nombre total de ménages |
| `C21_MENPSEUL` | Ménages unipersonnels |
| `C21_FAMMONO` | Familles monoparentales |
| `C21_COUPAENF` | Couples avec enfants |

| Colonne source (logement) | Signification |
|---|---|
| `DEP` | Code département |
| `P21_RP` | Résidences principales |
| `P21_RP_LOC` | Résidences principales en location |
| `P21_RP_LOCHLMV` | Locataires HLM vides |

| Colonne source (population) | Signification |
|---|---|
| `DEP` | Code département |
| `P21_POP` | Population totale |
| `P21_POP3044` | Population 30–44 ans |
| `P21_POP4559` | Population 45–59 ans |
| `P21_POP6074` | Population 60–74 ans |
| `P21_POP75P` | Population 75 ans et plus |

**Agrégation** : `df.groupby('DEP').sum()` sur les colonnes numériques.

---

### 1.6 Minimas sociaux — RSA, Prime d'activité, ASS/ASPA (FR-005)

**Fichiers** : `data/raw/minimas/rsa_{annee}.csv`, `prime_activite_{annee}.csv`, `ass_aspa_{annee}.csv`  
**Sources** : DREES (data.drees.solidarites-sante.gouv.fr), France Travail (open.datafrance travail.gouv.fr)

| Champ attendu | Type | Description |
|---|---|---|
| Code département | `str(2)` | Code INSEE |
| Nombre d'allocataires | `int` | Valeur en fin de trimestre ou moyenne annuelle |
| Période | `str` | Année ou trimestre de référence |

**Invariants** :
- Couverture ≥ 90 % des 96 départements
- Valeurs numériques > 0

---

### 1.7 Géométries départementales (Cartographie)

**Fichier** : `data/geo/departements.geojson`  
**Source** : `https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson`

| Propriété GeoJSON | Type | Description |
|---|---|---|
| `code` | `str(2)` | Code INSEE département (`"01"` à `"2B"`) |
| `nom` | `str` | Nom du département |
| `geometry` | `Polygon/MultiPolygon` | Contour simplifié |

**Invariants** :
- Exactement 96 features (France métropolitaine, sans DOM)
- CRS : EPSG:4326 (WGS84)
- Codes Corse : `"2A"`, `"2B"` (non `"20"`)

---

## 2. Contrat de sortie — Jeu analytique

**Fichier** : `data/processed/analytical_dataset.csv`

### Schéma minimal garanti

| Colonne | Type | Nullable | Contrainte |
|---|---|---|---|
| `dep_code` | `str(2)` | Non | `^[0-9]{2}$\|^2[AB]$`, 96 valeurs uniques par année |
| `dep_nom` | `str` | Non | Non vide |
| `annee` | `int` | Non | Entre 2017 et 2023 inclus |
| `suren_depot_nb` | `int` | Non | > 0 |
| `suren_depot_taux` | `float` | Non | Entre 0 et 50 (pour 1 000 ménages) |
| `chomage_taux` | `float` | Oui (max 10 % NaN) | Entre 2.0 et 25.0 |
| `revenu_median_uc` | `float` | Oui (max 10 % NaN) | Entre 10 000 et 40 000 |
| `taux_pauvrete` | `float` | Oui (max 10 % NaN) | Entre 0.0 et 50.0 |
| `rsa_taux` | `float` | Oui (max 10 % NaN) | Entre 0.0 et 20.0 |
| `part_locataires` | `float` | Oui (max 10 % NaN) | Entre 0.0 et 100.0 |
| `part_familles_mono` | `float` | Oui (max 10 % NaN) | Entre 0.0 et 50.0 |
| `nb_menages` | `int` | Non | > 0 |
| `score_fragilite` | `float` | Oui | Calculé uniquement si toutes les 4 composantes non-NaN |

### Colonnes optionnelles (présentes si données disponibles)

| Colonne | Nullable | Condition |
|---|---|---|
| `gini` | Oui | Disponible pour millésime 2019 uniquement |
| `interdecile_d9d1` | Oui | FiLoSoFi disponible |
| `ficp_taux` | Oui | Si séries BdF accessibles au niveau département |
| `fcc_taux` | Oui | Si séries BdF accessibles au niveau département |
| `chomage_taux_t1` | Oui | Si millésime t-1 disponible |
| `taux_pauvrete_t1` | Oui | Si millésime t-1 disponible |

### Encodage et format

- Encodage : UTF-8
- Séparateur : virgule (`,`)
- Décimale : point (`.`)
- Valeurs manquantes : chaîne vide (standard pandas `to_csv`)
- Pas de colonne d'index en première position
- En-têtes en snake_case anglicisé

### Validation de sortie (`scripts/04_validate.py`)

```python
# Règles de validation minimales
assert df['dep_code'].nunique() == 96          # 96 départements
assert df['suren_depot_taux'].notna().all()    # variable cible complète
assert (df['suren_depot_taux'] > 0).all()      # sanity check
assert df.groupby('annee')['dep_code'].nunique().eq(96).all()  # couverture par année
coverage = df.notna().mean()
warnings = coverage[coverage < 0.90]
if len(warnings) > 0:
    print(f"⚠️ Couverture < 90% pour : {list(warnings.index)}")
```

---

## 3. Contrat de visualisation (FR-024)

Toute visualisation produite dans `index.qmd` doit satisfaire les quatre critères suivants sans exception.

### 3.1 Structure obligatoire de chaque figure

```python
# Modèle de conformité pour chaque chart/map
{
    "title": str,           # Titre descriptif (obligatoire, non vide)
    "axes": {               # Pour les graphiques XY
        "x_label": str,     # Libellé + unité (ex. "Taux de chômage (%)")
        "y_label": str      # Libellé + unité (ex. "Taux de surendettement (‰)")
    },
    "legend": str,          # Pour les cartes : label de l'échelle de couleur
    "source": str,          # Attribution (ex. "Source : Banque de France, 2021")
    "caption": str          # Phrase de conclusion (1 phrase, non vide)
}
```

### 3.2 Cartes choroplèthes (≥ 6 requises — FR-020, FR-021, FR-022)

| Champ | Requis | Exemple |
|---|---|---|
| Titre | ✅ | `"Taux de surendettement par département (2021)"` |
| Échelle de couleur | ✅ | Divergente ou séquentielle, colorblind-safe (ex. `viridis`, `RdYlBu`) |
| Légende (colorbar) | ✅ | Unité sur la légende (ex. `"Dépôts pour 1 000 ménages"`) |
| Source + année | ✅ | Dans le caption ou annotation |
| Corse visible | ✅ | Codes `"2A"`, `"2B"` présents dans le GeoDataFrame |
| DOM exclus | ✅ | Filtrer `dep_code not in ["971","972","973","974","976"]` |
| Caption (1 phrase) | ✅ | Ex. `"Les Hauts-de-France et la Normandie affichent les taux les plus élevés."` |

### 3.3 Graphiques analytiques (≥ 4 requis — FR-023)

| Type | Champs requis |
|---|---|
| Scatter plot (bivarié) | Titre, axe X labelisé + unité, axe Y labelisé + unité, source, caption |
| Matrice de corrélation | Titre, légende des valeurs, p-values indiquées, source, caption |
| Distribution (histogramme / boxplot) | Titre, axe X avec unité, valeurs aberrantes identifiées, source, caption |
| Tendance temporelle | Titre, axe X = années, axe Y avec unité, source, caption |

### 3.4 Palettes recommandées

| Usage | Palette | Raison |
|---|---|---|
| Cartes séquentielles (taux) | `viridis` ou `YlOrRd` | Lisible en N&B, colorblind-safe |
| Cartes divergentes (résidus, score fragilité) | `RdYlBu_r` | Centre à zéro identifiable |
| Corrélation (heatmap) | `coolwarm` symétrique | Convention standard |
| Scatter plots | `tab10` (catégoriel) | Discernabilité maximale |

---

## 4. Contrat de visualisation MVP — Double choroplèthe (⚠️ Périmètre MVP)

Contrat spécifique à la **première version MVP** : deux cartes choroplèthes côte à côte, surendettement et chômage.

### 4.1 Schéma de la figure MVP

```python
# Contrat : figure Plotly make_subplots(rows=1, cols=2)
{
    "library": "plotly >= 5.18",
    "layout": "make_subplots(rows=1, cols=2, specs=[[choropleth, choropleth]])",
    "geojson": "data/geo/departements.geojson",  # gregoiredavid/france-geojson simplifié
    "featureidkey": "properties.code",            # join key : str 2 chars, ex. "01", "2A"
    "map_1": {
        "variable": "suren_depot_taux",
        "colorscale": "YlOrRd",
        "colorbar_title": "Dépôts / 1 000 ménages",
        "hover_template": "<b>{dep_nom}</b><br>Surendettement : {val:.1f}<extra></extra>"
    },
    "map_2": {
        "variable": "chomage_taux",
        "colorscale": "Blues",
        "colorbar_title": "Chômage (%)",
        "hover_template": "<b>{dep_nom}</b><br>Chômage : {val:.1f} %<extra></extra>"
    },
    "shared_layout": {
        "fitbounds": "locations",   # zoom automatique sur la France
        "visible": False,           # fond de carte masqué (outline only)
        "height": 500,
        "margin": {"r": 0, "t": 40, "l": 0, "b": 0}
    },
    "title_required": True,          # ex. "Surendettement et chômage par département (2021)"
    "caption_required": True,        # 1 phrase de conclusion dans le Quarto cell output
    "source_attribution_required": True  # "Source : Banque de France / INSEE, 2021"
}
```

### 4.2 Dataset d'entrée pour le MVP

**Fichier** : `data/processed/analytical_dataset_mvp.csv`

| Colonne | Type | Nullable | Description |
|---|---|---|---|
| `dep_code` | `str(2)` | Non | Code INSEE (`"01"`–`"95"`, `"2A"`, `"2B"`) |
| `dep_nom` | `str` | Non | Nom du département |
| `annee` | `int` | Non | Année de référence (2021 pour le MVP) |
| `suren_depot_nb` | `int` | Non | Dépôts de dossiers (absolu, source BdF ODS) |
| `suren_depot_taux` | `float` | Non | Dépôts pour 1 000 ménages (calculé) |
| `chomage_taux` | `float` | Non | Taux de chômage localisé annuel moyen (%) |
| `nb_menages` | `int` | Non | Ménages (RP INSEE 2021, dénominateur) |

**Contraintes minimales MVP** :
```python
assert len(df) == 96                          # exactement 96 départements
assert df['dep_code'].is_unique               # pas de doublons
assert df['suren_depot_taux'].notna().all()   # variable cible complète
assert df['chomage_taux'].notna().all()       # variable explicative complète
assert (df['suren_depot_taux'] > 0).all()
assert df['chomage_taux'].between(2.0, 25.0).all()
```
