---
id: zablrncdzrx5y77azc3f0ru
title: "\U0001F5FA data science"
desc: MOC pour la science des données
updated: 1698992646501
created: 1684401234633
---

## Quelle est la différence entre erreur d’estimation et erreur de prévision ?

Une **erreur d’estimation** est une erreur lors de la phase d’entraînement du modèle. (biais) ; alors que l’**erreur de prévision**, c’est une erreur du modèle pendant la phase de test (variance).

## [[ds.data.import]]

## statistiques descriptives univariées

- [[stat.descri.univariate]]
- distribution empiriques
- tendance centrale, dispersion et forme

## statistiques descriptives bivariées

- distributions conditionnelles
- corrélations
- tableau de contingence

## statistiques descriptives temporelles

- graphiques
- correction des variations saisonnières

## [[ds.eda]]

- [[ds.ml.ul.dimension-reduction]] _dimension reduction_
- [[ds.ml.ul.cluster]] _clustering_

## Statistique décisionnelle _inférentielle_

- estimation ponctuelle
- estimation par intervalle de confiance
- test d’hypothèse
- [Initiez-vous à la statistique inférentielle | Openclassrooms](https://openclassrooms.com/fr/courses/4525306-initiez-vous-a-la-statistique-inferentielle)

## [[machine-learning]]

### [[supervised-learning]]

#### [[ds.ml.sl.reg]]

#### [[ds.ml.sl.class]]

## traitement du langage

- [[nlp]]
- LLM

## [[time-serie]]

---- EXAM certification DS ENSAE

---

title: "exam"
author: "Guillaume Gilles"
date: "2023-05-22"
output:
html_document:
toc: TRUE # table of content true
toc_depth: 3 # up to three depths of headings
toc_float: TRUE # table of content follow the navigation up & down
number_sections: TRUE # if you want number sections at each table header

---

## séparer les données en `training set` et `test set`

Avec `initial_split` on sépare le dataset en 2, d’un côté, le jeu
d’entraînement `vin_train` et de l’autre, le jeu de test, `vin_train`.

```{r}
set.seed(789)
vin_split <- initial_split(vin, strata = quality)
vin_train <- training(vin_split)
vin_test <- testing(vin_split)

vin_split
```

## Modèlisation

Pour la modélisation, j’utilise tidymodels.

### définir un workflow

Dans un premier temps, je défini un _workflow_ qui va me permettre de spécifier
la variable à prédire, `quality` à partir de quelles variables potentiellement
explicatives, toutes mon cas, `~ .`

```{r}
vin_wf <- workflow() %>%
  add_formula(quality ~ .)

vin_wf
```

### régression logistique

La régression logistique est un modèle de régression statistique utilisé pour les
problèmes de classification. La fonction mathématique associée attribue tout
nombre réel à une valeur comprise entre 0 et 1.

Premier modèle, la régression logistique. Je défini les spécificités du modèle
`glm_spec` pour ajouter ensuite le _worflow_ précédement initialisé.

```{r}
glm_spec <- logistic_reg() %>%
  set_engine("glm")

glm_spec

glm_wf <- vin_wf %>%
  add_model(glm_spec)

glm_wf
```

### ridge

la régression ridge ajoute une **pénalité proportionnelle à la somme**
**des carrés des coefficients** (norme L2) à la fonction de perte des moindres
carrés ordinaires (MCO). L'objectif est de réduire les coefficients vers zéro
sans les éliminer complètement.

Je fais de même pour le ridge…

Attention, cette fois, il faut spécifier la problématique de prédiction, soit
`regression`, ou `classification` dans ce cas, puisque ridge et d’autre algorithmes,
lasso, K-NN, forêts aléatoires, XGBosst, SVM, etc. peuvent traiter les 2 problématiques.

```{r}
ridge_spec <- logistic_reg(penalty = tune(), mixture = 0) %>%
  set_engine("glmnet") %>%
  set_mode("classification") %>%
  set_args(maxit = 10000)

ridge_spec

ridge_wf <- vin_wf %>%
  add_model(ridge_spec)

ridge_wf
```

### lasso

la régression Lasso, similaire à la régression ridge, ajoute une
pénalité à la fonction de perte. Cependant, au lieu de la somme des coefficients
au carré, elle utilise la **somme des valeurs absolues des coefficients**
(norme L1). La régression Lasso effectue une sélection des caractéristiques en
ramenant certains coefficients à exactement zéro, les éliminant ainsi du modèle.

```{r}
lasso_spec <- logistic_reg(penalty = tune(), mixture = 1) %>%
  set_engine("glmnet") %>%
  set_mode("classification") %>%
  set_args(maxit = 10000)

lasso_spec

lasso_wf <- vin_wf %>%
  add_model(lasso_spec)

lasso_wf
```

### K-NN

Algorithme d'apprentissage automatique **non paramétrique**, il repose sur l'idée
que les points de données appartenant à la même classe ou catégorie sont
généralement proches les uns des autres.

```{r}
knn_spec <- nearest_neighbor(
  mode = "classification",
  engine = "kknn",
  weight_func = "rectangular")

knn_spec

knn_wf <- vin_wf %>%
  add_model(knn_spec)

knn_wf
```

### random forest

Le principe des forêts aléatoire est de constituer à l’aide de la technique du
_bootstrapping_ une forêt d’arbres avec un faible biais et une grande variance.
En faisant la moyenne de ces arbres, on réduit la variance, tout en conservant
un biais faible.

```{r}
rf_spec <- rand_forest() %>%
  set_mode("classification") %>%
  set_engine("ranger")

rf_spec

rf_wf <- vin_wf %>%
  add_model(rf_spec)

rf_wf
```

### XGBoost

L'idée principale de XGBoost est d'entraîner itérativement une séquence de modèles
faibles, chacun d'entre eux tentant de corriger les erreurs commises par les
modèles précédents. Les modèles sont entraînés de manière croissante, ce qui
signifie que chaque nouveau modèle est entraîné pour minimiser les erreurs des
modèles précédents.

```{r}
xgb_spec <- boost_tree(trees = 100, tree_depth = 6) %>%
  set_engine("xgboost") %>%
  set_mode("classification")

xgb_spec

xgb_wf <- vin_wf %>%
  add_model(xgb_spec)

xgb_wf
```

### Support Vector Machine

Avec SVM on essaie de faire passer un _hyperplan_ dans un espace multidimensionnel
pour séparer en 2 classes. Ensuite, les points sont classés selon s’ils sont sur
le côté positif ou négatif de l’hyperplan.

```{r}
svm_spec <- svm_linear() %>%
  set_engine('LiblineaR') %>%
  set_mode("classification")

svm_spec

svm_wf <- vin_wf %>%
  add_model(svm_spec)

svm_wf
```

## fit avec `fit_resamples()`

Il est temps d’entraîner les modèles initialement définis, grâce à la fonction
`fit_resample()` du package **tune**.

### régression logistique

les objets `glm_res$.metrics[[2]]` et `glm_res$.predictions[[2]]` permettent de
vérifier l’accuracy ainsi que l’aire sous la courbe ROC et les différentes
prédictions dans le bloc numéro 2 de la validation croisée.

```{r}
glm_res <- fit_resamples(
  object = glm_wf,
  resamples = folds_train,
  control = control_resamples(save_pred = TRUE)
  )

glm_res$.metrics[[2]]
glm_res$.predictions[[2]]
```

### Ridge

```{r}
# ridge_res <- fit_resamples(
#   object = ridge_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
#   )
```

### Lasso

```{r}
# lasso_res <- fit_resamples(
#   object = lasso_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
#   )
```

### K-NN

```{r}
# knn_res <- fit_resamples(
#   object = knn_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
# )
```

### random forest

```{r}
rf_res <- fit_resamples(
  object = rf_wf,
  resamples = folds_train,
  control = control_resamples(save_pred = TRUE)
  )
```

### XGBoost

```{r}
xgb_res <- fit_resamples(
  object = xgb_wf,
  resamples = folds_train,
  control = control_resamples(save_pred = TRUE)
  )
```

### SVM

```{r}
# svm_res <- fit_resamples(
#   object = svm_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
#   )
```

## Évaluation des modèles

Maintenant que tous les modèles sont entraînés, on peut évaluer les performances
de chacun et choisir le modèles que l’on préfère.

```{r}
collect_metrics(glm_res)
# collect_metrics(ridge_res)
# collect_metrics(lasso_res)
# collect_metrics(knn_res)
collect_metrics(rf_res)
collect_metrics(xgb_res)
# collect_metrics(svm_res)
```

### matrice de confusion

Le meilleur modèle (entre ceux qui fonctionnent…) est la **random forest**.

Il s’agit de la matrice de confusion sur le modèle de la forêt aléatoire.

```{r}
rf_res %>%
  conf_mat_resampled()
```

## il est temps de réaliser la prédiction final sur le `test set`

```{r}
vin_final <- rf_wf %>%
  last_fit(vin_split)

vin_final
```

Les performances et les prédictions du modèle final avec une forêt aléatoire.

```{r}
collect_metrics(vin_final)
```

```{r}
collect_predictions(vin_final) %>%
  conf_mat(quality, .pred_class)
```

## Les éléments qui manque :

1. plussieurs de mes modèles ne fonctionne pas à cause d’une erreur dans le code que je n’arrive pas à résoudre à temps…
2. Je n’ai pas fais le _feature engineering_, comme mettre les variable au carré, au cube, etc.
3.
