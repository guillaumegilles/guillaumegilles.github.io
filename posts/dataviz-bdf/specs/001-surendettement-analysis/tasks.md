# Tâches : Analyse surendettement départemental

**Branche** : `001-surendettement-analysis`  
**Input** : Documents de conception dans `specs/001-surendettement-analysis/`  
**Référence** : [plan.md](./plan.md) · [spec.md](./spec.md) · [data-model.md](./data-model.md) · [contracts/data-contracts.md](./contracts/data-contracts.md)

---

## 📍 Statut actuel — ✅ Toutes les phases terminées

| Phase | Scénario | Statut | Tâches |
|---|---|---|---|
| 1 — Setup | — | ✅ **Terminée** | T001–T004 |
| 2 — Fondations | Pipeline de données | ✅ **Terminée** | T005–T017 |
| 3 — US1 | Traçabilité des sources | ✅ **Terminée** | T018–T020 |
| 4 — US2 | Exploration (EDA) | ✅ **Terminée** | T021–T023 |
| 5 — US3 | Modélisation OLS | ✅ **Terminée** | T024–T028 |
| 6 — US4 | Cartographie | ✅ **Terminée** | T029–T034 |
| 7 — US5 | Reproductibilité | ✅ **Terminée** | T035–T037 |
| 8 — Polish | Finalisation | ✅ **Terminée** | T038–T042 |

**Prérequis validés :**
- `data/processed/analytical_dataset.csv` ✅ (96 × 5 années × ~25 colonnes)
- `data/processed/coverage_report.csv` ✅
- `data/geo/departements.geojson` ✅
- `index.qmd` ✅ (sections sources + couverture + EDA complètes)

**Démarrage Phase 5 + 6 (parallèle possible)** :
- Phase 5 (US3 — OLS) : T024 → T025 → T026 → T027/T028 [P]
- Phase 6 (US4 — Carto) : T029 → T030 → T031/T032/T034 [P] → T033

---

## Format : `[ID] [P?] [Story?] Description`

- **[P]** : Parallélisable (fichiers différents, pas de dépendance incomplète)
- **[Story]** : Scénario utilisateur de référence (US1 à US5)
- Chemins de fichiers exacts inclus dans chaque description

---

## Phase 1 : Setup (infrastructure projet)

**Objectif** : Créer la structure de répertoires, l'environnement Python et les fichiers de configuration de base.

- [x] T001 Créer la structure de répertoires du projet : `data/raw/bdf/`, `data/raw/filosofi/`, `data/raw/chomage/`, `data/raw/rp/`, `data/raw/minimas/`, `data/processed/`, `data/geo/`, `scripts/`
- [x] T002 Créer `requirements.txt` avec versions pinnées : pandas≥2.0, geopandas≥0.14, matplotlib≥3.8, plotly≥5.18, statsmodels≥0.14, scikit-learn≥1.4, requests≥2.31, pdfplumber≥0.10, openpyxl≥3.1, pyarrow≥14.0
- [x] T003 [P] Créer `.gitignore` en ajoutant `data/raw/` et `data/processed/analytical_dataset.csv` (données brutes non versionnées)
- [x] T004 [P] Créer `data/processed/dep_ref.csv` — table de référence 96 départements : colonnes `dep_code`, `dep_nom`, `reg_code` (codes INSEE métropole, incluant `2A`/`2B` Corse)

**Point de contrôle** : Structure de répertoires prête, dépendances installables via `pip install -r requirements.txt`

---

## Phase 2 : Fondations (prérequis bloquants)

**Objectif** : Scripts d'acquisition et de nettoyage fonctionnels produisant des fichiers intermédiaires valides. Ces fondations DOIVENT être complètes avant tout travail sur les scénarios utilisateurs.

**⚠️ CRITIQUE** : Aucun scénario utilisateur ne peut démarrer avant la fin de cette phase.

### Acquisition des données (script 01)

- [x] T005 Créer `scripts/01_download.py` — bloc BdF : télécharger les PDFs synthèses surendettement 2018–2023 dans `data/raw/bdf/synthese_{annee}.pdf` via URLs directes banque-france.fr (6 fichiers)
- [x] T006 [P] Compléter `scripts/01_download.py` — bloc FiLoSoFi : télécharger et décompresser `base-cc-filosofi-2021-geo2024_csv.zip` et `indic-struct-distrib-revenu-2019-SUPRA.zip` dans `data/raw/filosofi/`
- [x] T007 [P] Compléter `scripts/01_download.py` — bloc chômage : télécharger les fichiers TCRD Excel chômage localisé INSEE avec headers anti-bot (`User-Agent`, `Referer`) dans `data/raw/chomage/` ; afficher un avertissement et l'URL manuelle si HTTP 500
- [x] T008 [P] Compléter `scripts/01_download.py` — bloc RP 2021 : télécharger et décompresser les 4 bases infracommunales (ménages, population, logement, activité) dans `data/raw/rp/`
- [x] T009 [P] Compléter `scripts/01_download.py` — bloc minimas sociaux : télécharger RSA, prime d'activité, ASS/ASPA depuis DREES/France Travail dans `data/raw/minimas/`
- [x] T010 [P] Compléter `scripts/01_download.py` — bloc GeoJSON : télécharger `departements-version-simplifiee.geojson` depuis `gregoiredavid/france-geojson` dans `data/geo/departements.geojson`

### Nettoyage par source (script 02)

- [x] T011 Créer `scripts/02_clean.py` — bloc BdF : extraire tableaux PDF avec `pdfplumber`, jointure noms → codes via `dep_ref.csv`, produire `data/processed/surendettement.csv` (colonnes : `dep_code`, `annee`, `suren_depot_nb`, `source_url`, `source_millesime`) ; assertion 96 lignes par année
- [x] T012 [P] Compléter `scripts/02_clean.py` — bloc FiLoSoFi : filtrer lignes département (`CODGEO` longueur 2 ou pattern `^[0-9]{2}$|^2[AB]$`), renommer `MED21`→`revenu_median_uc`, `TP6021`→`taux_pauvrete`, `GI21`→`interdecile_d9d1`, produire `data/processed/filosofi.csv` ; charger SUPRA 2019 pour `gini`, produire `data/processed/filosofi_gini.csv`
- [x] T013 [P] Compléter `scripts/02_clean.py` — bloc chômage : sélectionner 96 départements métropolitains (exclure DOM 971–976), agréger trimestres → moyenne annuelle, produire `data/processed/chomage.csv` (colonnes : `dep_code`, `annee`, `chomage_taux`, `source_url`, `source_millesime`)
- [x] T014 [P] Compléter `scripts/02_clean.py` — bloc RP 2021 : `groupby('DEP').sum()` sur chaque base IC ; calculer `part_locataires`, `part_hlm`, `part_familles_mono`, `part_menages_1pers`, `part_25_54`, `part_65plus`, `taux_surpeuplement` ; produire `data/processed/rp_menages.csv`, `rp_logement.csv`, `rp_population.csv`
- [x] T015 [P] Compléter `scripts/02_clean.py` — bloc minimas sociaux : calculer `rsa_taux`, `prime_activite_taux`, `ass_aspa_taux` en part de population de référence (RP), produire `data/processed/minimas_sociaux.csv`

### Fusion et validation (scripts 03 & 04)

- [x] T016 Créer `scripts/03_merge.py` : joindre tous les fichiers intermédiaires sur `(dep_code, annee)`, construire les lags t-1 **en unités brutes** (`chomage_taux_t1`, `taux_pauvrete_t1`) avant toute normalisation, calculer `score_fragilite` = `chomage_z×0,3 + taux_pauvrete_z×0,3 + rsa_taux_z×0,2 + part_locataires_z×0,2` (z-scores des 4 composantes), exporter `data/processed/analytical_dataset.csv` (schéma complet conforme à `contracts/data-contracts.md` §2)
- [x] T017 Créer `scripts/04_validate.py` : vérifier les invariants du contrat de sortie (`dep_code.nunique()==96`, `suren_depot_taux.notna().all()`, couverture ≥ 90 % par variable), afficher les avertissements pour `gini` (comportement attendu : 20,8 % couverte), produire `data/processed/coverage_report.csv`

**Point de contrôle** : `python scripts/04_validate.py` s'exécute sans erreur fatale ; `analytical_dataset.csv` existe avec ≥ 96 lignes et 25 colonnes

---

## Phase 3 : Scénario US1 — Traçabilité des sources (Priorité : P1) 🎯 MVP

**Objectif** : Permettre à un·e analyste de vérifier que chaque jeu de données provient d'une source officielle non modifiée, avec une chaîne de traitement traçable de bout en bout.

**Test indépendant** : Exécuter `python scripts/04_validate.py` et vérifier que `coverage_report.csv` est produit avec une ligne par variable ; consulter la section « Sources » de `index.qmd` et vérifier que chaque tableau présente nom, URL, millésime et nombre de départements.

- [x] T018 [US1] Ajouter une section « Sources de données » dans `index.qmd` : tableau des 7 sources (nom, URL/identifiant série, millésime(s) utilisé(s), nombre de départements couverts) généré programmatiquement depuis `coverage_report.csv` (FR-008)
- [x] T019 [US1] Ajouter la section « Couverture des données manquantes » dans `index.qmd` : tableau et/ou heatmap des valeurs manquantes par variable et par département, généré depuis `data/processed/coverage_report.csv` (FR-014) — titre, source, caption obligatoires (FR-024)
- [x] T020 [P] [US1] Vérifier que `data/raw/` est bien dans `.gitignore` et que `data/processed/analytical_dataset.csv` n'est pas versionné ; documenter ce choix dans `README.md` section « Données »

**Point de contrôle** : Section « Sources » rendue dans `index.qmd` ; couverture affichée ; aucun fichier brut commité

---

## Phase 4 : Scénario US2 — Exploration des corrélations (Priorité : P1)

**Objectif** : Permettre à un·e chercheur·se de comprendre quelles variables sont associées au taux de surendettement, via matrice de corrélation, distributions et tendances temporelles.

**Test indépendant** : Exécuter `quarto render index.qmd` après avoir complété uniquement la Phase 3 + cette phase ; vérifier que la matrice de corrélation s'affiche et que chaque figure respecte le contrat FR-024 (titre + axes + source + caption).

- [x] T021 [US2] Implémenter la matrice de corrélation dans `index.qmd` : Pearson **et** Spearman entre toutes les variables et `suren_depot_taux`, avec p-values (statsmodels ou scipy) ; heatmap `coolwarm` avec annotations, titre, source, caption (FR-011, FR-024)
- [x] T022 [P] [US2] Implémenter les distributions dans `index.qmd` : histogrammes + boxplots pour chaque variable clé (6 variables du modèle minimal + variable cible), identification des valeurs extrêmes, titre/axe/source/caption par figure (FR-012, FR-024)
- [x] T023 [P] [US2] Implémenter les tendances temporelles dans `index.qmd` : graphique en lignes pour `suren_depot_taux` + `chomage_taux` + `taux_pauvrete` sur 2017–2021 (si ≥ 2 millésimes disponibles), axe X = années, axe Y avec unité, source, caption (FR-013, FR-024)

**Point de contrôle** : Rendu Quarto produit ≥ 3 figures conformes FR-024 dans la section EDA ; matrice identifie ≥ 3 variables avec p < 0,05 (SC-002)

---

## Phase 5 : Scénario US3 — Modélisation OLS (Priorité : P2)

**Objectif** : Permettre à un·e économiste d'interpréter quels prédicteurs restent significatifs dans un modèle multivarié et si les effets de lag améliorent le pouvoir explicatif.

**Test indépendant** : Vérifier que le tableau OLS de base affiche R² ajusté ≥ 0,40 (SC-003) et que le diagnostic VIF est présent pour chaque spécification.

- [x] T024 [US3] Implémenter le modèle OLS de base dans `index.qmd` : prédicteurs = `chomage_taux`, `revenu_median_uc`, `taux_pauvrete`, `rsa_taux`, `part_locataires`, `part_familles_mono` ; Y = `suren_depot_taux` ; tableau standardisé coefficients + SE + p-values + R² ajusté + N (FR-015, FR-019)
- [x] T025 [US3] Implémenter le diagnostic VIF dans `index.qmd` : calculer VIF pour chaque prédicteur de chaque spécification avec `statsmodels.stats.outliers_influence.variance_inflation_factor` ; tableau VIF par modèle, commentaire explicite si VIF ≥ 10 (FR-017)
- [x] T026 [US3] Implémenter les modèles avec lag t-1 dans `index.qmd` : modèles avec `chomage_taux_t1` et `taux_pauvrete_t1` en remplacement des variables contemporaines ; tableau comparatif côte-à-côte (spéc. sans lag / avec lag) avec AIC et test de Wald ; conclusion sur SC-005 (FR-016)
- [x] T027 [P] [US3] Implémenter le modèle z-score dans `index.qmd` : réestimer le modèle de base avec toutes les variables normalisées en z-score ; présenter les coefficients bêta standardisés pour comparaison de l'importance relative des prédicteurs (research.md §6)
- [x] T028 [P] [US3] Implémenter l'ACP conditionnelle dans `index.qmd` : si VIF ≥ 10 pour ≥ 2 variables simultanément, appliquer `sklearn.decomposition.PCA`, présenter variance expliquée par composante, justifier les composantes retenues (FR-018)

**Point de contrôle** : Rendu Quarto produit tableaux OLS + VIF + comparaison lag ; R² ajusté ≥ 0,40 vérifié (SC-003) ; aucun VIF non commenté ≥ 10

---

## Phase 6 : Scénario US4 — Cartographie départementale (Priorité : P2)

**Objectif** : Permettre à un·e journaliste ou décideur de visualiser les disparités territoriales du surendettement et de la fragilité composite sur des cartes choroplèthes lisibles.

**Test indépendant** : Vérifier que la carte du taux de surendettement 2021 s'affiche avec les 96 départements, une légende colorblind-safe, et une caption d'une phrase.

- [x] T029 [US4] Charger le GeoDataFrame dans `index.qmd` : `geopandas.read_file("data/geo/departements.geojson")`, jointure avec `analytical_dataset.csv` sur `dep_code`/`code`, vérifier les 96 lignes et les codes Corse `2A`/`2B`
- [x] T030 [US4] Produire la carte choroplèthe du `suren_depot_taux` 2021 dans `index.qmd` : palette `YlOrRd`, légende avec unité ("Dépôts pour 1 000 ménages"), titre, source BdF 2021, caption — Corse visible, DOM exclus (FR-020, FR-024)
- [x] T031 [P] [US4] Produire la carte d'évolution surendettement 2018–2021 dans `index.qmd` : variation absolue ou relative du taux entre 2018 et 2021, palette divergente `RdYlBu_r`, titre, source, caption (FR-020, FR-024)
- [x] T032 [P] [US4] Produire les cartes des 4 variables explicatives clés dans `index.qmd` : `chomage_taux`, `taux_pauvrete`, `rsa_taux`, `part_locataires` — millésime 2021, palette `viridis`, conformité FR-024 complète pour chacune (FR-021)
- [x] T033 [US4] Produire la carte du `score_fragilite` dans `index.qmd` : palette divergente `RdYlBu_r`, formule pondérée explicitée dans la légende ou note de carte, caption incluant le coefficient de corrélation spatiale entre score et taux de surendettement (FR-022, SC-007)
- [x] T034 [P] [US4] Produire les scatter plots bivariés dans `index.qmd` : `suren_depot_taux` vs. `chomage_taux`, `taux_pauvrete`, `rsa_taux`, `part_locataires` — axe X et Y labelisés avec unités, droite de régression, source, caption (FR-023, FR-024)

**Point de contrôle** : Rendu Quarto produit ≥ 6 cartes + ≥ 4 graphiques analytiques conformes FR-024 (SC-004) ; comparaison visuelle score/surendettement commentée (SC-007)

---

## Phase 7 : Scénario US5 — Reproductibilité (Priorité : P3)

**Objectif** : Permettre à un·e analyste externe de reproduire l'intégralité de l'analyse depuis les données brutes jusqu'au rapport HTML, sans intervention manuelle.

**Test indépendant** : Suivre `quickstart.md` depuis un environnement vierge (nouveau virtualenv) et vérifier que `quarto render index.qmd` s'exécute sans erreur et produit un fichier `index.html`.

- [x] T035 [US5] Mettre à jour `README.md` : section « Installation » avec commandes `git clone`, `python -m venv`, `pip install -r requirements.txt` ; section « Données » expliquant que `data/raw/` est gitignorée ; section « Exécution » listant les 5 commandes dans l'ordre (scripts 01→04 + quarto render) (SC-006)
- [x] T036 [P] [US5] Valider `specs/001-surendettement-analysis/quickstart.md` contre l'état réel du projet : vérifier que chaque commande documentée fonctionne, mettre à jour les URLs et noms de fichiers si nécessaire
- [x] T037 [P] [US5] Documenter la procédure de mise à jour des données dans `README.md` section « Mise à jour » : variables `YEAR_TARGET` dans `01_download.py`, liste des points de contrôle, note sur l'anti-bot chômage INSEE (H-01 de la spec)

**Point de contrôle** : `README.md` suffisant pour reproduire l'analyse sans consulter d'autres fichiers ; SC-006 vérifiable

---

## Phase 8 : Polish & finalisation transversale

**Objectif** : Intégration finale, cohérence narrative du rapport, et validation de bout en bout.

- [x] T038 [P] Rédiger l'introduction et la problématique dans `index.qmd` (section existante) : mettre à jour le texte avec les résultats réels (R², corrélations, lag significatif ou non), références à la littérature BdF/ECB documentées dans `research.md`
- [x] T039 [P] Rédiger la section « Conclusion » dans `index.qmd` : répondre aux 4 questions de recherche de la spec, mentionner les limites (Gini 2019 uniquement, OLS sans correction spatiale, Moran's I si significatif), lister les perspectives (régression spatiale SAR/SLM)
- [x] T040 Valider le rendu complet : exécuter `quarto render index.qmd` et vérifier que (a) le rendu s'achève en < 5 min, (b) aucun chunk Python ne produit d'erreur, (c) le nombre total de figures ≥ 10 est atteint, (d) tous les chiffres clés dans le texte sont générés programmatiquement (SC-006, FR-026)
- [x] T041 [P] Vérifier la conformité FR-024 sur toutes les figures : parcourir `index.qmd` et confirmer que chaque figure a titre + axes/légende + source + caption ; corriger les manquants
- [x] T042 [P] Ajouter les métadonnées YAML Quarto dans `index.qmd` : `author`, `date`, `format: html` avec table des matières, `execute: cache: true` pour accélérer les re-rendus

---

## Dépendances et ordre d'exécution

### Dépendances entre phases

```
Phase 1 (Setup)
    │
    ▼
Phase 2 (Fondations) ◄─── BLOQUE TOUTES LES PHASES SUIVANTES
    │
    ├──▶ Phase 3 (US1 — Sources) ─────────────┐
    │                                          │
    ├──▶ Phase 4 (US2 — EDA)                   │
    │        (dépend de Phase 3 complète)       │
    │                                          │
    ├──▶ Phase 5 (US3 — Modélisation OLS)       │
    │        (dépend de Phase 4 complète)       │
    │                                          │
    ├──▶ Phase 6 (US4 — Cartographie)           │
    │        (dépend de Phase 3 complète)       │ ◄── Peut être parallèle avec Phase 5
    │                                          │
    └──▶ Phase 7 (US5 — Reproductibilité)      │
             (dépend de Phases 3, 4, 5, 6)     │
                                               ▼
                                        Phase 8 (Polish)
```

### Dépendances entre scénarios

| Scénario | Dépend de | Peut démarrer après |
|---|---|---|
| **US1 (P1)** — Sources | Phase 2 complète | Phase 2 |
| **US2 (P1)** — EDA | US1 complète | Phase 3 |
| **US3 (P2)** — Modélisation | US2 complète | Phase 4 |
| **US4 (P2)** — Cartographie | US1 complète | Phase 3 (parallèle avec US2/US3) |
| **US5 (P3)** — Reproductibilité | US1+US2+US3+US4 complètes | Phase 7 |

### Au sein de chaque phase

- T005–T010 (téléchargements) : parallélisables entre eux après T001–T004
- T011–T015 (nettoyage par source) : parallélisables entre eux après T005–T010
- T016 (fusion) dépend de T011–T015
- T017 (validation) dépend de T016

### Opportunités de parallélisme

- **Scripts 01** : T006, T007, T008, T009, T010 peuvent s'exécuter simultanément (sources indépendantes)
- **Scripts 02** : T012, T013, T014, T015 peuvent s'exécuter simultanément (fichiers distincts)
- **Cartographie** (Phase 6) : T031, T032, T034 sont indépendants entre eux

---

## Exemple de parallélisme — Phase 2 (nettoyage)

```bash
# Lancer simultanément après que 01_download.py est terminé :
Tâche A : "Bloc BdF dans scripts/02_clean.py → data/processed/surendettement.csv"
Tâche B : "Bloc FiLoSoFi dans scripts/02_clean.py → data/processed/filosofi.csv"
Tâche C : "Bloc chômage dans scripts/02_clean.py → data/processed/chomage.csv"
Tâche D : "Bloc RP dans scripts/02_clean.py → data/processed/rp_menages.csv, rp_logement.csv, rp_population.csv"
Tâche E : "Bloc minimas dans scripts/02_clean.py → data/processed/minimas_sociaux.csv"
```

---

## Stratégie d'implémentation

### MVP (Scénario US1 + US2 uniquement)

1. Compléter **Phase 1** : structure du projet
2. Compléter **Phase 2** : pipeline de données valide (scripts 01–04)
3. Compléter **Phase 3** (US1) : section sources dans `index.qmd`
4. Compléter **Phase 4** (US2) : EDA dans `index.qmd`
5. **STOP et VALIDATION** : `quarto render index.qmd` produit un rapport avec matrice de corrélation et distributions
6. Démo possible à ce stade

### Livraison incrémentale

1. Setup + Fondations → Pipeline fonctionnel (SC-001 vérifiable)
2. US1 + US2 → Rapport EDA publié (SC-002 vérifiable)
3. US3 → Modèles OLS ajoutés (SC-003, SC-005 vérifiables)
4. US4 → Cartes ajoutées (SC-004, SC-007 vérifiables)
5. US5 + Polish → Rapport reproductible complet (SC-006 vérifiable)

---

## Résumé

| Phase | Scénario | Tâches | Tâches [P] | Statut | Livrable |
|---|---|---|---|---|---|
| 1 — Setup | — | T001–T004 | T003, T004 | ✅ Terminée | Structure + requirements.txt |
| 2 — Fondations | — | T005–T017 | T006–T010, T012–T015 | ✅ Terminée | `analytical_dataset.csv` valide |
| 3 — US1 | Sources (P1) | T018–T020 | T020 | ✅ Terminée | Section sources dans index.qmd |
| 4 — US2 | EDA (P1) | T021–T023 | T022, T023 | ✅ Terminée | Matrice corr. + distributions + tendances |
| **5 — US3** | **OLS (P2)** | **T024–T028** | **T027, T028** | 🔲 **Prochaine étape** | Tableaux OLS + VIF + lag |
| **6 — US4** | **Cartographie (P2)** | **T029–T034** | **T031, T032, T034** | 🔲 **Parallèle avec US3** | ≥ 6 cartes + ≥ 4 graphiques |
| 7 — US5 | Reproductibilité (P3) | T035–T037 | T036, T037 | 🔲 Après US3+US4 | README complet |
| 8 — Polish | — | T038–T042 | T038, T039, T041, T042 | 🔲 En dernier | Rapport final rendu |
| **Total** | | **42 tâches** | **21 [P]** | **23/42 ✅** | |

---

## Notes

- `[P]` = fichiers distincts ou blocs indépendants, pas de dépendances non résolues
- `[USn]` = traçabilité vers le scénario utilisateur dans `spec.md`
- Chaque phase constitue un incrément livrable et testable indépendamment
- Pas de tests unitaires (hors périmètre — validation via `04_validate.py` et rendu Quarto)
- Commiter après chaque phase ou groupe logique de tâches
- S'arrêter à tout point de contrôle pour valider le scénario de manière autonome
