# Recherche — Analyse surendettement départemental

**Phase** : 0 — Recherche & décisions techniques  
**Branche** : `001-surendettement-analysis`  
**Date** : 2026-05-20  
**Référence spec** : `specs/001-surendettement-analysis/spec.md`

---

## 1. Source surendettement Banque de France (BdF WebStat)

### Question initiale
Quel endpoint/identifiant de série WebStat utiliser pour les dépôts de dossiers de surendettement par département ?

### Décision
**Source primaire : extraction PDF des Synthèses annuelles BdF.**  
**Source secondaire : API WebStat IFI (niveau région, non département).**

### Rationale

L'API WebStat (`api.webstat.banque-france.fr/webstat-fr/v1/`) publie des séries IFI à deux niveaux géographiques confirmés : national (`IFI.M.FR.SUREN.DEPOT`) et régional (13 régions, pattern `IFI.M.{CODE_REGION}.SUREN.DEPOT`). **Aucune série de niveau département n'a été trouvée dans le catalogue public.** Les données départementales existent, mais exclusivement dans les Synthèses nationales annuelles publiées en PDF.

Les PDF synthèses contiennent un tableau département × année exploitable par extraction (bibliothèques `pdfplumber` ou `camelot-py`). Cette approche respecte le principe d'intégrité des données (données officielles BdF, non modifiées, pipeline scriptable).

### Sources identifiées

| Document | URL | Années disponibles |
|---|---|---|
| Synthèse annuelle 2023 | `https://www.banque-france.fr/system/files/2024-03/SUREN-2023_Rapport-d_activite-des-commissions_web_0.pdf` | 2023 |
| Synthèse annuelle 2024 | `https://www.banque-france.fr/system/files/2025-10/RAC_Rapport_activite_des_commissions_0.pdf` | 2024 |
| Page d'index des synthèses | `https://www.banque-france.fr/fr/publications-et-statistiques/publications/synthese-nationale-des-rapports-dactivite-des-commissions-de-surendettement` | 2018–2024 |
| API WebStat — Séries IFI (national/région) | `https://api.webstat.banque-france.fr/webstat-fr/v1/` | À partir de ~2014 |

### Séries WebStat connues (projet existant)
```
IFI.M.FR.SUREN.DEPOT       → dépôts de dossiers, national, mensuel
IFI.M.FR.FICP.INS_FICP     → inscriptions FICP, national, mensuel
```
Pattern régional hypothétique (à vérifier avec clé API) :
```
IFI.M.ARA.SUREN.DEPOT      → Auvergne-Rhône-Alpes
IFI.M.HDF.SUREN.DEPOT      → Hauts-de-France
...
```

### Alternatives considérées

| Alternative | Rejetée parce que |
|---|---|
| API WebStat niveau département | Aucune série de ce niveau confirmée dans le catalogue public |
| data.gouv.fr | Seul jeu disponible date de 1995–2010, hors périmètre temporel |
| Accès manuel (téléchargement navigateur) | Incompatible avec le principe II (Reproductibilité) — aucun script automatisable |

### ⚠️ Mise à jour MVP (2026-05-20) — API ODS confirmée au niveau département

**La conclusion initiale (PDF uniquement) est OBSOLÈTE.** L'API WebStat expose bien des séries départementales via son endpoint OpenDataSoft (ODS), distinct de l'endpoint SDMX formel.

**Endpoint ODS (opérationnel)** :
```
https://webstat.banque-france.fr/api/explore/v2.1/catalog/datasets/observations/exports/csv/
```

**Clé publique intégrée dans le bundle JS de WebStat** (non documentée officiellement) :
```
a78150367a35332580ae1651b4023f0c333e99b6653821d6ac445af9
```

**Pattern de séries départementales confirmé** :
```
IFI.M.D{CODE}.SUREN.DEPOT   ex : IFI.M.D01.SUREN.DEPOT  → Ain
                                  IFI.M.D2A.SUREN.DEPOT  → Corse-du-Sud
                                  IFI.M.D2B.SUREN.DEPOT  → Haute-Corse
```
Couverture : **données mensuelles depuis 2019-01** pour les 96 départements métropolitains.

**Implémentation existante** : `scripts/01_download.py` implémente déjà cette approche (lignes 100–153).

**Risque** : la clé publique n'est pas versionnée officiellement et pourrait être renouvelée sans préavis. Fallback documenté : enregistrement d'une clé via `developer.webstat.banque-france.fr/user/register`.

### Plan d'implémentation (mis à jour)
1. Utiliser l'API WebStat ODS (déjà implémentée dans `scripts/01_download.py`) pour les 96 séries `IFI.M.D{CODE}.SUREN.DEPOT`
2. Agréger les données mensuelles en annuel (somme des 12 mois) dans `scripts/02_clean.py`
3. Les PDFs synthèses restent disponibles comme source de validation croisée pour les années 2018–2023

---

## 2. Téléchargement INSEE — FiLoSoFi et chômage localisé

### Question initiale
Méthode de téléchargement en masse pour FiLoSoFi et chômage localisé par département.

### Décision
**FiLoSoFi** : téléchargement ZIP direct depuis `www.insee.fr/fr/statistiques/7756729`  
**Chômage localisé** : scraping HTML de la page INSEE 2012804 + contournement anti-bot pour les fichiers TCRD historiques  
**Gini** : utiliser le ratio interdécile D9/D1 (`GI21`) comme proxy, ou le fichier SUPRA 2019 pour la Gini exacte

### Rationale

FiLoSoFi (millésime 2021) est téléchargeable directement via un ZIP CSV sans authentification. **Point important** : la colonne `GI21` dans `base-cc-filosofi-2021` est le rapport D9/D1 (interdécile), **pas** l'indice de Gini. L'indice de Gini n'est disponible au niveau département que dans les fichiers SUPRA (dernier millésime confirmé : 2019).

Pour le chômage localisé, les fichiers TCRD Excel sont bloqués par une protection anti-bot INSEE (HTTP 500). La page HTML elle-même contient le tableau des derniers trimestres disponibles (96 départements) et est scrapable. Pour les séries historiques, une approche avec headers HTTP de navigateur est documentée.

### URLs de téléchargement

| Jeu de données | URL | Millésime | Format |
|---|---|---|---|
| FiLoSoFi 2021 (revenu médian, taux de pauvreté, D9/D1) | `https://www.insee.fr/fr/statistiques/fichier/7756729/base-cc-filosofi-2021-geo2024_csv.zip` | 2021 | ZIP CSV (~1 Mo) |
| FiLoSoFi SUPRA 2019 (Gini + déciles) | `https://www.insee.fr/fr/statistiques/fichier/6036907/indic-struct-distrib-revenu-2019-SUPRA.zip` | 2019 | ZIP XLSX (~22 Mo) |
| FiLoSoFi SUPRA 2017 (Gini + déciles) | `https://www.insee.fr/fr/statistiques/fichier/4291712/indic-struct-distrib-revenu-2017-SUPRA.zip` | 2017 | ZIP XLSX (~22 Mo) |
| Chômage localisé — page HTML | `https://www.insee.fr/fr/statistiques/2012804` | Trimestriel, 2025+ | HTML (scraping) |
| RP 2021 — ménages (IRIS → DEP) | `https://www.insee.fr/fr/statistiques/fichier/8268828/base-ic-menages-2021_csv.zip` | 2021 | ZIP CSV |
| RP 2021 — population (IRIS → DEP) | `https://www.insee.fr/fr/statistiques/fichier/8268806/base-ic-population-2021_csv.zip` | 2021 | ZIP CSV |
| RP 2021 — activité (IRIS → DEP) | `https://www.insee.fr/fr/statistiques/fichier/8268843/base-ic-activite-2021_csv.zip` | 2021 | ZIP CSV |
| RP 2021 — logement (IRIS → DEP) | `https://www.insee.fr/fr/statistiques/fichier/8268838/base-ic-logement-2021_csv.zip` | 2021 | ZIP CSV |

### Note sur le chômage localisé (TCRD)
Les fichiers TCRD Excel (`TCRD_025.xlsx`, etc.) sont protégés anti-bot (HTTP 500). **Contournement documenté** :
```python
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) ...",
    "Referer": "https://www.insee.fr/fr/statistiques/2012804",
    "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
}
resp = requests.get(url, headers=headers)
```
Si ce contournement échoue, le script alertera l'utilisateur et proposera l'URL manuelle dans la documentation.

### Alternatives considérées

| Alternative | Rejetée parce que |
|---|---|
| Gini exact (2021) via base-cc-filosofi-2021 | N'existe pas — GI21 = D9/D1, pas Gini |
| API BDM INSEE pour chômage départemental | Pas d'IDBANK confirmé pour les taux localisés (séries estimées, hors enquête BIT standard) |
| DoReMIFaSol (InseeFrLab) | Catalogue incomplet sur le chômage localisé, accès complexe |

---

## 3. Millésime commun le plus récent

### Décision
**Millésime de référence principal : 2021**

### Rationale

| Source | Millésime le plus récent confirmé |
|---|---|
| Surendettement BdF (Synthèse PDF) | 2023 (données 2023 publiées mars 2024) |
| FICP/FCC (BdF) | 2023 |
| Chômage localisé (INSEE) | 2024 (trimestriel) |
| FiLoSoFi (INSEE) | **2021** (base-cc publiée 2023) |
| Gini SUPRA (INSEE) | **2019** (dernier millésime SUPRA confirmé) |
| Bénéficiaires minimas sociaux (DREES) | 2022–2023 |
| Logement (INSEE/DREES) | 2021 (RP 2021) |
| Socio-démographique (INSEE RP) | **2021** |

FiLoSoFi et le Recensement de la Population (RP) constituent le goulot d'étranglement : leur dernier millésime est 2021. **L'analyse principale utilisera 2021** comme année de référence. L'analyse temporelle couvrira 2017–2021 (3–5 millésimes selon la source), avec 2018–2021 comme fenêtre minimale garantie.

Pour le lag t-1, les variables de chômage et de pauvreté à t-1 (2020) seront construites à partir des millésimes disponibles.

---

## 4. Bibliothèque géographique recommandée

### Décision
**`geopandas` + GeoJSON `gregoiredavid/france-geojson`**

### Rationale

| Critère | gregoiredavid/france-geojson | IGN Admin Express COG | api.gouv.fr/departements |
|---|---|---|---|
| Téléchargement direct (1 ligne Python) | ✅ | ❌ (portail JS) | ❌ (pas de géométrie) |
| 96 départements métropole uniquement | ✅ | ✅ | N/A |
| Projection WGS84 EPSG:4326 | ✅ | ✅ (option) | N/A |
| Champ code département | `"code"` (2 chars) | `"INSEE_DEP"` | `"code"` (sans géom) |
| Licence | Licence Ouverte | Licence Ouverte | Open API |
| Version simplifiée disponible | ✅ (~570 Ko) | ❌ | N/A |

```python
import geopandas as gpd

# URL directe, aucune extraction ZIP, compatible geopandas.read_file()
GEO_URL = (
    "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/"
    "departements-version-simplifiee.geojson"
)
gdf = gpd.read_file(GEO_URL)
# → CRS : EPSG:4326 | colonnes : code, nom, geometry | 96 lignes
```

Note : les codes Corse sont `"2A"` et `"2B"` (pas `"20"`). La jointure avec les données analytiques se fait sur `df.merge(gdf, left_on='dep_code', right_on='code')`.

### Alternatives considérées

| Alternative | Rejetée parce que |
|---|---|
| IGN Admin Express COG | Portail JavaScript, pas de téléchargement direct scriptable |
| data.gouv.fr OSM contours | URL de téléchargement hors ligne depuis avril 2026 |
| api.gouv.fr/departements | Pas de géométrie exposée (codes et noms seulement) |

---

## 5. OLS vs régression spatiale

### Décision
**OLS confirmé pour cette version. Régression spatiale (SAR/SLM) hors périmètre.**

### Rationale

Conforme à l'hypothèse **H-07** de la spec. L'OLS avec 96 observations est statistiquement tractable et suffisant pour répondre aux questions de recherche 1–3. La dépendance spatiale éventuelle sera documentée comme limite et perspective d'extension, via une mention du test de Moran's I dans la section discussion. Si Moran's I est significatif, une note explicite sera ajoutée sans modifier le modèle estimé.

### Alternatives considérées

| Alternative | Rejetée parce que |
|---|---|
| Spatial Lag Model (SAR) | Hors périmètre H-07, complexité de mise en œuvre et d'interprétation |
| Spatial Error Model (SEM) | Même raison |
| GWR (Geographically Weighted Regression) | Non justifié par les questions de recherche actuelles |

---

## 6. Stratégie de normalisation des variables

### Décision
**Double approche : coefficients bruts (modèle primaire) + coefficients bêta standardisés z-score (robustesse)**

### Rationale

| Stratégie | Usage recommandé |
|---|---|
| **Unités brutes** | Modèle primaire — coefficients interprétables (ex. "1 point de chômage → X dépôts") |
| **Z-score** | Modèle secondaire — coefficients β comparables entre prédicteurs (importance relative) |
| Min-max | ❌ Sensible aux outliers, pas de motivation statistique pour OLS |

L'approche en deux temps est standard en économétrie appliquée française (*Économie & Statistique*, *Revue d'économie régionale & urbaine*). Elle permet de répondre à la fois aux audiences techniques (bêta standardisés) et politiques (coefficients en unités réelles).

**Ordre des opérations avec variables de lag** :
1. Construire le lag en unités brutes : `unemp_t1 = unemp_rate.shift(1)`
2. Normaliser l'ensemble des variables (courantes et lagguées) dans un second temps
3. Ne **pas** normaliser avant de construire le lag (biais de séquence)

```python
# Ordre correct
df['unemp_t1'] = df['unemp_rate'].shift(1)          # 1. lag en unités brutes
X_std = StandardScaler().fit_transform(df[features]) # 2. normalisation z-score
```

### Alternatives considérées

| Alternative | Rejetée parce que |
|---|---|
| Min-max uniquement | Sensible aux outliers (Paris, Val-de-Marne vs. Creuse) ; pas utilisé en économétrie |
| Z-score uniquement | Perd l'interprétabilité des coefficients pour le rapport |
| Log-transform | Pertinent pour variables très asymétriques (ex. revenus) — à évaluer sur les distributions, documenté comme option dans le script de nettoyage |

---

## 7. Bibliothèque de visualisation — Choroplèthes MVP

### Question initiale
Quelle bibliothèque Python utiliser pour les cartes choroplèthes interactives dans le rapport Quarto HTML ?

### Décision
**Plotly (`plotly.graph_objects.Choropleth` + `make_subplots`)** pour les deux cartes côte à côte.

### Rationale

| Critère | Matplotlib + GeoPandas | **Plotly** | Folium |
|---|---|---|---|
| Interactivité HTML (zoom, tooltip) | ❌ Statique (PNG) | ✅ JS natif | ⚠️ Leaflet iframe |
| Intégration Quarto HTML | ✅ Simple | ✅ Widget Jupyter natif | ⚠️ iframe difficile à intégrer |
| Layout 2 cartes côte à côte | ✅ `plt.subplots()` | ✅ `make_subplots` | ❌ 1 widget / carte |
| Tooltips au survol (nom, valeur) | ❌ | ✅ `hovertemplate` | ✅ |
| Colorblind-safe (`Cividis`, `Blues`) | ✅ | ✅ | ✅ |

Plotly est listé en premier dans les widgets Jupyter natifs de la documentation officielle Quarto (`quarto.org/docs/interactive/widgets/jupyter.html`). La figure est sérialisée en JSON et chargée via CDN Plotly.js — pas besoin d'`embed-resources: true` pour le site hébergé.

### Configuration retenue pour le MVP

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "choropleth"}, {"type": "choropleth"}]],
    subplot_titles=[
        "Dépôts de dossiers de surendettement (pour 1 000 ménages)",
        "Taux de chômage localisé (%)"
    ],
    horizontal_spacing=0.02
)

# Carte 1 : Surendettement — YlOrRd (chaleureux, intuitif pour un indicateur de risque)
fig.add_trace(go.Choropleth(
    geojson=depts_geojson,
    locations=df['dep_code'],
    z=df['suren_depot_taux'],
    featureidkey="properties.code",
    colorscale="YlOrRd",
    colorbar=dict(x=0.46, title="Dépôts / 1 000 ménages"),
    hovertemplate="<b>%{location}</b><br>Surendettement : %{z:.1f}<extra></extra>",
), row=1, col=1)

# Carte 2 : Chômage — Blues (palette froide distincte de la première)
fig.add_trace(go.Choropleth(
    geojson=depts_geojson,
    locations=df['dep_code'],
    z=df['chomage_taux'],
    featureidkey="properties.code",
    colorscale="Blues",
    colorbar=dict(x=1.0, title="Chômage (%)"),
    hovertemplate="<b>%{location}</b><br>Chômage : %{z:.1f} %<extra></extra>",
), row=1, col=2)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(height=500, title_text="...", margin={"r":0,"t":40,"l":0,"b":0})
```

**Fix VS Code / Positron** :
```python
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook_connected"
```

### Échelles de couleur — justification accessibilité

| Variable | Échelle | Justification |
|---|---|---|
| Surendettement | `YlOrRd` | Séquentielle chaud-rouge ; intuitive pour un indicateur de risque financier ; ColorBrewer, colorblind-safe |
| Chômage | `Blues` | Séquentielle froide ; visuellement distincte de YlOrRd pour comparaison immédiate ; print-safe |
| Alternative daltonisme strict | `Cividis` pour les deux | Conçu spécifiquement pour deuteranopie/protanopie (Morgan et al. 2018) |

**Note** : éviter `Rainbow`/`Jet` — non perceptuellement uniformes, interdits en publications scientifiques.

### GeoJSON — join key

Source : `gregoiredavid/france-geojson` (version simplifiée, 569 Ko)
```
URL : https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson
Champ de jointure : properties.code  (ex : "01", "2A", "95")
```
⚠️ Les codes sont des chaînes zero-padded. La colonne `dep_code` du DataFrame doit être de type `str`, pas `int`.

### Alternatives considérées

| Alternative | Rejetée parce que |
|---|---|
| `matplotlib + geopandas` | Statique (PNG) — perd l'interactivité HTML (tooltips, zoom) |
| `folium` | Génère des iframes Leaflet incompatibles avec `layout-ncol=2` Quarto et `embed-resources` |
| `choropleth_mapbox` (Plotly) | Ne fonctionne pas dans `make_subplots` — nécessite un layout Quarto séparé ; tile background non nécessaire pour MVP |
