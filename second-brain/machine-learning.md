---
id: dqwd0ge7mm5a2f4vjxgrx9m
title: "\U0001F5FA modélisation : machine learning"
desc: MOC pour le machine learning
updated: 1698006177182
created: 1680186749042
---

> Machine learning is a completely new programming paradigm.
> Now instead of given explicit instruction you program with examples and the machine learning algorithm finds patterns in your data and tursn them into these instructions.
> No more handcrafting of recipes.
> Machine learning's model is jsut a fancy word for recipe.
> Cassie Kozyrskov

## une branche de l’intelligence artificielle

les algorithmes de machine learning sont _construits sur des règles mathématiques_.
Pour schématiser, ces algorithmes permettent de _construire des modèles prédictifs_.

> Field of study that gives computers the ability to learn without being
> explicitly programmed
>
> --- Arthur Samuel (1959)

### [[ds.ml.notation]]

### critère(s) d’erreur

- [[ds.ml.sl.reg.cost-function]]

### sur-apprentissage

- [[ds.ml.cross-validation]]

## Est-ce que tous les algorithmes de machine learning ont un risque de sur-apprentissage ?

Oui, sauf RF = l’élagage / out of bag

---

## Flux de travail

### analyse exploratoire des données

1.  [[ds.data.import]]

### exporter les résultats

### manipuler les variables

#### changer le type de données

- [[r.dt]]
-

#### découpage en classes

#### niveau des facteurs

### manipuler les individus

#### importer les données

#### manipuler les données

- transformation des variables qualitatives en `factor`

```r
df$chas <- as.factor(df$chas)
```

- Normalisation des variables qualitatives (centrer-réduire)

on utilise la fonction `scale()` dans ca cas

- traitement des données manquantes
- supprimer rapidement une colonne d’un data set

```r
don$heure <- NULL
```

#### clustering

##### Classification non supervisé _clustering_

- K-means
- [[ds.cah]]

```{r}
# hclust requière la matrice de distance, on utilise donc la `dist()`
cah <- dist(df)

cah_single <- hclust(cah, method = "single")
cah_ward <- hclust(cah, method = "ward.D2")
cah_complete <- hclust(cah, method = "complete")
cah_average <- hclust(cah, method = "average")

# plot(as.dendrogram(chaS))
# plot(sort(chaS$height,dec=T)[1:30],type="h")
# abline(h=1.2)
# don$single <- cutree(chaS,h=1.2)
# plot(sort(chaW$height,dec=T)[1:20],type="h")
# don$ward <- cutree(chaW,k=6)
# plot(sort(chaM$height,dec=T)[1:20],type="h")
# don$compl <- cutree(chaM,k=6)
# plot(sort(chaA$height,dec=T)[1:30],type="h")
# abline(h=3.5)
# don$ave <- cutree(chaA,h=3.5)
```

`cutree()` est la fonction pour découper le dendograme en k classe selon lcoude observé dans le graphique auparavant ;

- DBSCAN, modèles de mélange, auto-encodeurs
- cartes de Kohonen (SOM : Self Organizing Maps)

###### Réduction de dimension _dimension reduction_

- ACP Analyse en Composantes Principales (_PCA_)

```r
medical %>%
  PCA()
```

- AFC
- ACM

### modélisation

#### Modèle linéaire généralisé

- régression linéaire
- régression de Poisson
- régression logistique

#### Méthodes régularisés

- Ridge
- Lasso
- Elasticnet
- Lars.

> Pouvez-vous indiquer les différences entre ridge, lasso et elasticnet ?

Ridge, Lasso et Elastic Net sont des modèles de régression linéaire pénalisée.

- Ridge : la régression ridge ajoute une **pénalité proportionnelle à la somme**
  **des carrés des coefficients** (norme L2) à la fonction de perte des moindres
  carrés ordinaires (MCO). L'objectif est de réduire les coefficients vers zéro
  sans les éliminer complètement.

- Lasso : la régression Lasso, similaire à la régression ridge, ajoute une
  pénalité à la fonction de perte. Cependant, au lieu de la somme des coefficients
  au carré, elle utilise la **somme des valeurs absolues des coefficients**
  (norme L1). La régression Lasso effectue une sélection des caractéristiques en
  ramenant certains coefficients à exactement zéro, les éliminant ainsi du modèle.

- Elastic Net est une combinaison de Ridge et de Lasso.

#### Méthodes bayésiennes.

#### Méthodes splines

- régression spline
- GAM

I D’autres méthodes : analyse discriminante linéaire, PLS,
méthodes à directions révélatrice (index model ).

#### Méthodes de moyennage local

- plus proches voisins
- noyau de lissage
- CART.

#### Méthodes d’agrégation

- bagging (dont random forests),
- gradient boosting.

##### Méthodes à noyau

- SVM (et SVR).

#### Réseaux de neurones

- DNN
- CNN
- RNN

![](assets/ml_scikit_learn_map.png)

### comparaison des résultats

## référence

- [[ml.workflow.template.qmd]]
