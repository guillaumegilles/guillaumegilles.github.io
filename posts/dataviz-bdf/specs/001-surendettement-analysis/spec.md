# Spécification : Analyse de l'inclusion financière des ménages français — Corrélation entre conditions économiques départementales et surendettement

**Branche** : `001-surendettement-analysis`

**Créée le** : 2026-05-20

**Statut** : Brouillon

---

## Résumé

Cette analyse étudie dans quelle mesure les conditions économiques locales — chômage, pauvreté, minimas sociaux, logement, structure démographique — permettent d'expliquer et de prédire les variations spatiales du surendettement des ménages en France métropolitaine à l'échelle des 96 départements. Le résultat livrable est un rapport Quarto reproductible, publié sur le site du projet, qui combine exploration des données, modélisation et cartographie.

---

## Questions de recherche

1. **Question principale** : Existe-t-il une corrélation statistiquement significative entre la précarité économique départementale (chômage, pauvreté, minimas sociaux) et le taux de dépôts de dossiers de surendettement à la Banque de France ?
2. **Question secondaire 1** : Quels indicateurs économiques sont les prédicteurs les plus robustes du surendettement une fois la multicolinéarité prise en compte ?
3. **Question secondaire 2** : Les conditions économiques passées (effet de décalage temporel, *lag* à t-1) expliquent-elles mieux le surendettement que les conditions contemporaines ?
4. **Question secondaire 3** : Peut-on construire un score composite de fragilité financière départementale fondé sur des données publiques, et ce score est-il cohérent avec la distribution observée du surendettement ?

---

## Scénarios utilisateurs & tests *(obligatoire)*

### Scénario 1 — L'analyste vérifie la cohérence des données sources (Priorité : P1)

Un·e analyste de données ouvre le rapport Quarto et souhaite vérifier que les jeux de données utilisés sont bien ceux publiés par les organismes officiels, sans aucune modification manuelle, et que la chaîne de traitement est traçable de bout en bout.

**Pourquoi cette priorité** : Sans intégrité et traçabilité des données, aucune conclusion analytique ne peut être validée. C'est le prérequis de toute la suite.

**Test indépendant** : Peut être testé indépendamment en inspectant uniquement la section « Sources de données » et les scripts d'acquisition — sans avoir besoin que les modèles soient finalisés.

**Scénarios d'acceptance** :

1. **Étant donné** que les scripts d'acquisition sont exécutés depuis zéro, **quand** l'analyste consulte la section sources du rapport, **alors** chaque tableau présente : le nom de la source, l'URL ou l'identifiant de série, l'année(s) couverte(s), et le nombre de départements disponibles.
2. **Étant donné** un jeu de données brut téléchargé, **quand** l'analyste compare le fichier brut au jeu analytique, **alors** aucune valeur n'a été modifiée manuellement et toute transformation est documentée dans un script versionné.
3. **Étant donné** que la couverture géographique est vérifiée, **quand** l'analyste consulte l'état des données, **alors** la proportion de départements avec au moins une donnée manquante par variable est explicitement affichée.

---

### Scénario 2 — Le lecteur explore les corrélations entre variables (Priorité : P1)

Un·e chercheur·se ou décideur·se politique consulte la section EDA du rapport pour comprendre quelles variables sont les plus fortement associées au taux de surendettement départemental.

**Pourquoi cette priorité** : La section EDA est le cœur analytique du rapport ; elle fonde la sélection des variables pour la modélisation et répond directement aux questions de recherche 1 et 2.

**Test indépendant** : Peut être testé indépendamment en produisant uniquement la matrice de corrélation et les distributions — avant même d'avoir des modèles de régression.

**Scénarios d'acceptance** :

1. **Étant donné** que le jeu analytique est constitué, **quand** le lecteur consulte la matrice de corrélation, **alors** toutes les variables listées en exigences fonctionnelles y figurent, avec le taux de surendettement comme variable cible, et les coefficients de corrélation sont affichés avec leur intervalle de confiance ou valeur p.
2. **Étant donné** que les distributions sont visualisées, **quand** le lecteur consulte les graphiques de distribution par département, **alors** chaque graphique comporte un titre descriptif, des axes labelisés avec unités, la source des données et une légende d'interprétation d'une phrase.
3. **Étant donné** que des données temporelles sont disponibles sur au moins deux années, **quand** le lecteur consulte la section tendances, **alors** un graphique de tendance temporelle est présenté pour le taux de surendettement et au moins deux variables explicatives.

---

### Scénario 3 — Le lecteur interprète les résultats de régression (Priorité : P2)

Un·e économiste ou analyste de politique publique souhaite comprendre quels prédicteurs restent significatifs dans un modèle multivarié, et si les effets de lag apportent un pouvoir explicatif supplémentaire.

**Pourquoi cette priorité** : La modélisation répond à la question de recherche 2 et 3 ; elle dépend de l'EDA (P1) mais constitue la valeur ajoutée analytique principale.

**Test indépendant** : Peut être testé indépendamment en comparant les modèles OLS avec et sans lag, en vérifiant la robustesse via VIF.

**Scénarios d'acceptance** :

1. **Étant donné** qu'un modèle OLS de base est estimé, **quand** le lecteur consulte les résultats, **alors** le tableau présente : coefficients, erreurs standard, p-valeurs, R², et un commentaire sur la significativité économique de chaque prédicteur.
2. **Étant donné** que la multicolinéarité est analysée, **quand** le lecteur consulte le diagnostic VIF, **alors** chaque variable du modèle final a un VIF inférieur à 10, ou une note explicite justifie le maintien d'une variable avec VIF élevé (ex. variable de contrôle indispensable).
3. **Étant donné** que les modèles avec et sans lag t-1 sont comparés, **quand** le lecteur consulte la comparaison, **alors** un tableau synthétique présente les deux spécifications côte-à-côte avec les mêmes métriques de qualité d'ajustement.
4. **Étant donné** qu'une ACP est réalisée si nécessaire pour traiter la multicolinéarité, **quand** le lecteur consulte les résultats, **alors** la proportion de variance expliquée par les composantes retenues est indiquée et la sélection est justifiée.

---

### Scénario 4 — Le lecteur consulte la cartographie départementale (Priorité : P2)

Un·e journaliste ou communicant·e de politique publique souhaite identifier visuellement les territoires les plus exposés au surendettement et à la fragilité financière composite.

**Pourquoi cette priorité** : Les cartes choroplèthes rendent les résultats accessibles à un public non spécialiste et constituent la vitrine visuelle du rapport.

**Test indépendant** : Peut être testé indépendamment en produisant uniquement les cartes — avant même que les modèles de régression soient finalisés.

**Scénarios d'acceptance** :

1. **Étant donné** que la carte du taux de surendettement est produite, **quand** le lecteur la consulte, **alors** les 96 départements métropolitains sont représentés, avec une échelle de couleur lisible, une légende, le titre, la source et l'année des données.
2. **Étant donné** que les cartes des variables explicatives clés sont produites, **quand** le lecteur les consulte, **alors** au moins 4 variables (chômage, taux de pauvreté, part RSA, part locataires) sont cartographiées au même niveau d'exigence visuelle.
3. **Étant donné** que le score composite de fragilité est calculé (chômage × 0,3 + pauvreté × 0,3 + RSA × 0,2 + logement × 0,2), **quand** le lecteur consulte la carte composite, **alors** la formule est explicitée dans la légende ou la note de carte, et une comparaison visuelle avec la carte de surendettement est possible.

---

### Scénario 5 — Le lecteur reproduit l'analyse depuis zéro (Priorité : P3)

Un·e analyste externe ou pair souhaitant reproduire les résultats exécute l'ensemble de la chaîne analytique depuis les données brutes jusqu'au rapport HTML/PDF final, sans intervention manuelle.

**Pourquoi cette priorité** : La reproductibilité est un principe fondamental du projet (Constitution II) mais ne bloque pas la lecture du rapport — c'est une exigence de qualité scientifique.

**Test indépendant** : Peut être testé indépendamment en suivant uniquement le `README` et en exécutant les scripts dans l'ordre documenté.

**Scénarios d'acceptance** :

1. **Étant donné** un environnement vierge avec les dépendances installées, **quand** l'analyste exécute les scripts dans l'ordre documenté, **alors** le rapport final est produit sans erreur et les chiffres clés sont identiques à la version de référence.
2. **Étant donné** que les sources de données changent de format ou d'URL, **quand** l'analyste consulte la documentation, **alors** une procédure de mise à jour des données est documentée avec les points de contrôle attendus.

---

### Cas limites

- Que se passe-t-il si une source de données officielle est temporairement indisponible ou a changé de format depuis la dernière exécution ?
- Comment le rapport traite-t-il les départements avec des valeurs manquantes sur une ou plusieurs variables (ex. données FICP incomplètes) ?
- Que se passe-t-il si les millésimes disponibles ne se chevauchent pas entre deux sources (ex. surendettement en N et chômage uniquement en N-2) ?
- Comment la carte choroplèthe gère-t-elle les départements d'Outre-mer (hors périmètre de l'analyse) ?
- Que se passe-t-il si le VIF de toutes les spécifications testées dépasse 10 pour plusieurs variables simultanément ?

---

## Exigences fonctionnelles *(obligatoire)*

### Acquisition et préparation des données

- **FR-001** : L'analyse DOIT intégrer les **dépôts de dossiers de surendettement** par département (Banque de France WebStat), exprimés en taux pour 1 000 ménages ou en nombre absolu avec la population de référence fournie.
- **FR-002** : L'analyse DOIT intégrer les **taux d'inscription au FICP et FCC** (Banque de France) par département, au moins pour l'année la plus récente disponible.
- **FR-003** : L'analyse DOIT intégrer le **taux de chômage localisé** par département (INSEE chômage localisé), avec au moins deux millésimes pour permettre l'analyse de lag.
- **FR-004** : L'analyse DOIT intégrer les indicateurs **FiLoSoFi** (INSEE) : revenu médian disponible par unité de consommation, taux de pauvreté (seuil 60 %), et indice de Gini, par département.
- **FR-005** : L'analyse DOIT intégrer les **bénéficiaires de minimas sociaux** par département : RSA, prime d'activité, ASS/ASPA (France Travail / DREES), exprimés en part de la population ou des ménages.
- **FR-006** : L'analyse DOIT intégrer les **indicateurs de logement** par département : part des locataires, part du logement social, taux d'effort au logement, taux de surpeuplement (données data.gouv.fr, DREES, ou INSEE).
- **FR-007** : L'analyse DOIT intégrer les **indicateurs socio-démographiques** : part des familles monoparentales, structure par âge (part des 25-54 ans actifs, part des 65+), part des ménages unipersonnels (DREES, INSEE RP).
- **FR-008** : L'ensemble des sources DOIT être accompagné de métadonnées documentées : organisme émetteur, URL ou identifiant de série, millésime(s) utilisé(s), unité de mesure, méthode de normalisation appliquée.
- **FR-009** : Les données brutes NE DOIVENT PAS être modifiées manuellement. Toute transformation DOIT être réalisée par un script versionné.
- **FR-010** : Le jeu analytique final DOIT couvrir les 96 départements de France métropolitaine. Les départements et régions d'outre-mer sont hors périmètre.

### Analyse exploratoire (EDA)

- **FR-011** : Le rapport DOIT présenter une **matrice de corrélation** entre toutes les variables et la variable cible (taux de surendettement), avec coefficients de corrélation de Pearson et/ou Spearman et indication de la significativité statistique.
- **FR-012** : Le rapport DOIT présenter les **distributions** de chaque variable (histogramme ou boxplot) avec identification des valeurs extrêmes.
- **FR-013** : Le rapport DOIT présenter une **analyse des tendances temporelles** du taux de surendettement et des principales variables explicatives, si au moins deux millésimes sont disponibles pour la même variable.
- **FR-014** : Le rapport DOIT afficher explicitement la **couverture des données manquantes** par variable et par département avant toute analyse.

### Modélisation

- **FR-015** : Le rapport DOIT présenter au moins un **modèle OLS** avec les prédicteurs minimaux suivants : taux de chômage, revenu médian, taux de pauvreté, part RSA, part locataires, familles monoparentales.
- **FR-016** : Le rapport DOIT tester et documenter les **effets de décalage temporel (lag t-1)** pour au moins le taux de chômage et le taux de pauvreté.
- **FR-017** : Le rapport DOIT inclure un **diagnostic VIF** pour chaque spécification de modèle retenue. Toute variable avec VIF ≥ 10 DOIT faire l'objet d'un commentaire explicite.
- **FR-018** : Si la multicolinéarité est rédhibitoire, le rapport DOIT documenter le recours à une **ACP** ou à une sélection de variables, avec justification et proportion de variance expliquée.
- **FR-019** : Tous les modèles DOIVENT présenter leurs résultats dans un tableau standardisé : coefficients, erreurs standard, p-valeurs, R² ajusté, nombre d'observations.

### Visualisation et cartographie

- **FR-020** : Le rapport DOIT produire une **carte choroplèthe** du taux de surendettement par département, pour chaque millésime disponible.
- **FR-021** : Le rapport DOIT produire des **cartes choroplèthes** pour au moins 4 variables explicatives clés (chômage, taux de pauvreté, part RSA, part locataires).
- **FR-022** : Le rapport DOIT produire une **carte du score composite de fragilité** calculé selon la formule : score = chômage × 0,3 + pauvreté × 0,3 + RSA × 0,2 + logement × 0,2. La formule et la normalisation des variables DOIVENT être explicitées.
- **FR-023** : Le rapport DOIT produire des **nuages de points** (scatter plots) illustrant la relation bivariate entre le taux de surendettement et chacune des variables explicatives clés.
- **FR-024** : **Chaque visualisation** (carte ou graphique) DOIT comporter : titre descriptif, axes/légende avec unités, mention de la source et de l'année, et une phrase de conclusion (caption).

### Livrable et reproductibilité

- **FR-025** : L'analyse complète DOIT être encapsulée dans un ou plusieurs **fichiers Quarto (`.qmd`)** dont le rendu produit le rapport final publié sur le site du projet.
- **FR-026** : Tous les chiffres, statistiques et résultats mentionnés dans le texte narratif du rapport DOIVENT être **générés programmatiquement** (aucune valeur saisie manuellement).
- **FR-027** : Le rapport DOIT être **reproductible de bout en bout** : un tiers disposant de l'environnement documenté et des scripts DOIT pouvoir régénérer le rapport identique sans intervention manuelle.

---

### Entités clés

- **Département** : unité géographique d'analyse (96 unités en France métropolitaine) ; identifié par son code INSEE à 2 chiffres.
- **Taux de surendettement** : variable cible ; nombre de dossiers déposés à la Banque de France rapporté à la population de référence du département (pour 1 000 ménages ou pour 1 000 habitants majeurs).
- **Indicateur économique départemental** : toute variable explicative issue des sources listées (FR-001 à FR-007), normalisée pour permettre la comparaison inter-départementale.
- **Millésime** : année de référence d'un jeu de données ; plusieurs millésimes d'une même variable permettent l'analyse temporelle et les effets de lag.
- **Score de fragilité composite** : indicateur synthétique calculé à partir de 4 variables normalisées selon la formule pondérée définie en FR-022.
- **Modèle OLS** : régression par moindres carrés ordinaires ; unité d'observation = département × millésime.

---

## Critères de succès *(obligatoire)*

### Résultats mesurables

- **SC-001** : L'ensemble des 7 sources de données listées (FR-001 à FR-007) est intégré dans le jeu analytique final, avec un taux de couverture ≥ 90 % des 96 départements métropolitains pour chaque variable.
- **SC-002** : La matrice de corrélation identifie au moins 3 variables présentant une corrélation statistiquement significative (p < 0,05) avec le taux de surendettement.
- **SC-003** : Le modèle OLS de base atteint un R² ajusté ≥ 0,40, indiquant qu'au moins 40 % de la variance inter-départementale du surendettement est expliquée par les prédicteurs retenus.
- **SC-004** : Le rapport produit au minimum 10 visualisations conformes aux exigences (titre + axes + source + caption) : au moins 6 cartes choroplèthes et 4 graphiques analytiques.
- **SC-005** : L'analyse de lag détermine si le chômage à t-1 explique significativement mieux le surendettement que le chômage contemporain (comparaison formelle de modèles avec critère AIC ou test de Wald).
- **SC-006** : Le rapport complet est reproductible depuis les données brutes jusqu'au HTML rendu, sans erreur, en suivant uniquement la documentation fournie dans le `README`.
- **SC-007** : La carte du score composite de fragilité et la carte du taux de surendettement montrent une concordance visuelle qualitativement commentée dans le rapport (coefficient de corrélation spatiale ou commentaire narratif fondé sur les données).

---

## Hypothèses et suppositions

- **H-01** : Les séries de surendettement de la Banque de France (WebStat) sont disponibles en téléchargement programmatique par département pour au moins les années 2018–2023. Si l'API WebStat change ou impose des restrictions, un miroir CSV sera documenté.
- **H-02** : Les données FiLoSoFi (INSEE) sont disponibles à l'échelle départementale pour au moins 3 millésimes, ce qui permet une analyse temporelle minimale.
- **H-03** : Les données FICP/FCC sont disponibles en open data ou via des tableaux statistiques publiés par la Banque de France ; elles ne nécessitent pas d'accès privilégié.
- **H-04** : Le périmètre géographique est limité aux **96 départements de France métropolitaine**. La Corse (2A, 2B) est incluse. Les DOM-TOM (971–976) sont exclus.
- **H-05** : Les données de population de référence pour le calcul des taux (ménages, habitants majeurs) sont issues des recensements INSEE et considérées stables à l'échelle de l'analyse.
- **H-06** : La pondération du score composite (chômage × 0,3 + pauvreté × 0,3 + RSA × 0,2 + logement × 0,2) est fixée a priori sur la base de la littérature existante sur les déterminants du surendettement ; elle n'est pas optimisée statistiquement dans cette version.
- **H-07** : L'analyse se limite à des modèles de régression linéaire (OLS) et à une ACP si nécessaire. Les modèles de régression spatiale (Moran, SAR/SLM) sont hors périmètre de cette version mais documentés comme perspectives.
- **H-08** : Le rapport final est publié en HTML via Quarto sur le site du projet. Un rendu PDF est une option de diffusion secondaire mais n'est pas un critère de succès de cette version.
- **H-09** : Les variables sont toutes disponibles au même niveau d'agrégation (département). Toute variable disponible uniquement à un niveau inférieur (commune, EPCI) nécessiterait une agrégation préalable documentée — ce cas n'est pas anticipé dans le périmètre actuel.
- **H-10** : Les années de référence des différentes sources ne sont pas nécessairement identiques. L'analyse principale utilisera le millésime le plus récent commun à toutes les sources (ou le plus proche avec interpolation documentée si nécessaire).
