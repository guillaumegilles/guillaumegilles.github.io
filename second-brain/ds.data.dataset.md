---
id: ld3tpb1cym5x0gux49fu3us
title: jeu de données
desc: "dataset ou data matrix"
updated: 1697486802237
created: 1667594180715
---

## jeu de données / dataset / data matrix

les données sont, le plus souvent, stockées dans des fichiers `.txt` ou `.csv` 
sous la forme d’une matrice de données *data matrix*. C’est un tableau à double 
entrée dans lequelle on retrouve notre jeu de données.

Les lignes du tableau représentent les **individus** ou **observations** 
(*samples*) ; alors que les  colonnes représentent les **caractéristiques** 
(*features*) propres à ces observations, les **variables**.

| Sepal length (cm) | Sepal width (cm) | Petal length (cm) | Petal width (cm) | Iris Type  |
|:-----------------:|:----------------:|:-----------------:|:----------------:|:----------:|
|        6          |       3.4        |       4.5         |      1.6         | versicolor |
|       5.7         |       3.8        |       1.7         |      0.8         | setosa     |
|       6.5         |       3.2        |       3.9         |      1.4         | virginica  |
|       ...         |       ...        |       ...         |      ...         | setosa     |
|       ...         |       ...        |       ...         |      ...         | …          |

Dans ce jeu de données, `Sepal length`, `Sepal width`, `Petal length` et 
`Petal width` sont des [[ds.data.cont]] ; alors que `Iris Type` est une 
[[ds.data.cat]].

## Jeu de données déséquilibrées

metric = choisir le F1 score

## Doit’on centrer-réduire, mise à l’echelle, pour tous les modèles

= diapo 25 du pdf de Fei sur tidymodels

Oui pour tous, sauf pour les forêts et les RF