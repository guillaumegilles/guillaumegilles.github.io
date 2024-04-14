---
id: 99jq839wa4kos1ve0udvf2y
title: data frame
desc: la structure de données des data frames
updated: 1683402677554
created: 1683317192602
---

Le data frame est l’objet classique en statistique. Le data frame est une [[r.ds.list]] de [[r.dt.vector]] de même longueur, il s’agit donc d’une liste *particulière*.

Cours :

Les data frames sont des listes particulières dont les **composantes** sont de même *longueur*, mais les *modes* peuvent être différents. C’est d’ailleurs l’*objet privilégié en analyse statistique* : en effet, un **tableau de données** est constitué de variables quantitatives et/ou qualitatives mesurées sur les mêmes individus.

## Créer un data frame

Les principales manières de créer un dataframe consistent à utiliser les fonctions :

- `data.frame()` qui permet de concaténer des vecteurs de même taille et éventuellement de modes différents ;
- [[r.utils.read-table]] qui permet d’importer un tableau de données provenant d’un fichier externe (csv, txt, etc.) ;
- `as.data.frame()` pour la conversion explicite d’un objet à deux dimensions (comme une matrice).

Considérons les deux vecteurs `x` et `y` suivants :

```R
x <- c("A","B","C","A")
y <- 1:4
```

On peut utiliser ces derniers pour créer un dataframe assemblant ces deux vecteurs :

```R
mondf <- data.frame(x,y)
mondf
#   x y
# 1 A 1
# 2 B 2
# 3 C 3
# 4 A 4

length(mondf)
# [1] 2

attributes(mondf)
# $names
# [1] "x" "y"
# 
# $row.names
# [1] 1 2 3 4
# 
# $class
# [1] "data.frame"
```

Il est possible de transformer une matrice en dataframe en utilisant la fonction `as.data.frame()`. Il est aussi possible de faire le contraire en utilisant la fonction `data.matrix`.

## Visualisation d’un dataframe

La fonction `str` permet d’avoir un résumé rapide de chaque colonne du dataframe, de son type, etc. :

```R
str(mondf)
# 'data.frame':   4 obs. of  2 variables:
#  $ x: Factor w/ 3 levels "A","B","C": 1 2 3 1
#  $ y: int  1 2 3 4
```

Vous pouvez également avoir une visualisation un peu plus agréable de votre dataframe via la commande `View()` :

```R
View(mondf)
```

Cette visualisation permet également d’effectuer plusieurs opérations rapides sur le dataframe (qui n’impactent néanmoins pas le dataframe initial, elles modifient juste l’affichage de ce dernier dans la fenêtre `View` comme :

* Trier le dataframe selon une colonne définie ;
* Filtrer les valeurs d’une colonne définie.

## En résumé

* Vous pouvez créer un dataframe à partir d’un objet à deux dimensions déjà existant (comme une matrice) ou via l’importation d’un fichier externe (csv, txt, etc.).
* Il est possible d’afficher un dataframe dans une fenêtre externe, pour faciliter sa visualisation.

## références

@matzner-loberInitiezvousAuLangage