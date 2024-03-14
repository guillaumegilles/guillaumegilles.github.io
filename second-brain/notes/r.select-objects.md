---
id: ewy4cthzr35bx1psg0ryn7e
title: Select Objects
desc: ""
updated: 1708981467599
created: 1708981440190
---

[Sélectionnez des éléments dans les objets R](https://openclassrooms.com/fr/courses/4525256-initiez-vous-au-langage-r-pour-analyser-vos-donnees/exercises/3501)

## Quels sont les deux grands principes dans la sélection d'éléments au sein d'un objet R ?

- [x] La sélection par position ou indice

- [ ] La sélection par arguments

- [x] La sélection par conditions

- [ ] La sélection par opérateurs

> Les deux grands principes de sélection via R sont, (1) la sélection par indice ou position et (2) la sélection par condition.

## Quelles affirmations sont vraies concernant la sélection dans un vecteur ?

- [x] L'opérateur de sélection est [ ]

- [x] On peut employer des indices négatif au sein de l'opérateur de sélection

- [ ] On ne peut pas sélectionner dans un vecteur via une condition

> L'opérateur de sélection est bien `[ ]` et on peut sélectionner via des indices négatifs ! En revanche, comme on peut sélectionner via des indices négatifs, si `n` correspond au nombre d'éléments du vecteur, ces derniers doivent être des entiers entre `-n` et `n`, à l'exception du 0 ! On peut également sélectionner dans un vecteur via une condition : c'est une des grandes forces de R !

## Quel est l'affichage correspondant à l'exécution du code suivant ?

````r

x = c(1, 3, 4, 5, 10)

x[-c(1:4)]

```r



```r

10

````

> La sélection par indice négatif prend tous les éléments, sauf les indices spécifiés. Or ici, l'opérateur ` :` indique que nous sélectionnons tous les indices de 1 à 4, donc au final on sélectionne tout, sauf les éléments de 1 à 4. Il ne reste donc que le dernier `10`.

## Soit une matrice m. Que permet de sélectionner le code suivant :

```r

m[ ,c(i, 10)]

```

- [ ] Il permet de sélectionner un élément à la ligne i et la colonne 10

- [x] Il permet de sélectionner l'ensemble des éléments des colonnes i et 10

- [ ] Il permet de sélectionner l'ensemble des éléments des lignes i et 10

- [ ] Il permet de sélectionner les éléments i et 10 de notre matrice

> Ici notre code permet (1) de sélectionner toutes les lignes, car l'emplacement pour sélectionner des lignes (avant la virgule) est laissé vide et (2) de sélectionner les colonnes i et 10. Ainsi, on sélectionne l'ensemble des éléments des colonnes i et 10, peu importe la valeur de i.

## Soit une matrice `m` ayant 10 lignes et 4 colonnes. Quel code permet de sélectionner une "sous-matrice" contenant les lignes 2 à 5, de la 3ème colonne ?

```r

m[2:5, 3, drop=F]

```

> Les deux codes permettant de sélectionner les lignes 2 à 5, de la 3ème colonne sont `m[2:5, 3, drop=F]` et `m[2:5, 3]`. Or, comme nous souhaitons conserver le format matrice (et non avoir un résultat sous forme de vecteur), la première écriture est donc la plus adéquate !

## Quelles affirmations parmi les suivantes sont vraies concernant la sélection dans une liste ?

- [ ] On peut accéder à l'objet R correspondant au second élément d'une liste L via l'écriture : L[2]

- [x] Si on connait le nom d'un élément de la liste, on peut y accéder via l'opérateur $

- [ ] On peut sélectionner des éléments d'une liste via une sélection par index (ou indice)

- [ ] Le résultat d'une sélection au sein d'une liste sera forcément une autre liste

> L'écriture `L[2]` permet d'accéder au second élément de la liste et non l'objet correspondant. Pour ce faire, on utilisera l'écriture `[[ ]]`, soit : `L[[2]]`. On peut sélectionner via l'opérateur `$`, si on connait le nom associé à un élément au sein d'une liste. Mais on peut très bien sélectionner les différents éléments via des indices, `L[c(1:3)]` par exemple. En revanche, le résultat d'une sélection n'est pas forcément une liste. Lorsqu'on sélectionne par exemple l'objet correspondant à un élément, le résultat sera du type de l'objet en question, qui n'est pas forcément une liste ! Par exemple, avec le code ci-dessous, on sélectionne un vecteur classique de caractères :

```r

x <- c("a", "a", "b", "c")

X <- matrix(1:8, ncol=4)

maliste <- list(a=x, b=X)

maliste$a # vecteur

```

## Soit la liste suivante :

```r

x <- c(1:10)

X <- matrix(1:8, ncol=4)

y <- c(T, T, T, F, F)

z <- matrix(c("A", "B", "C", "D"), ncol=2)



maliste <- list(comp1=x, comp2=X, comp3=y, element4=z)

```

Quel(s) code(s) permet d'accéder à l'objet associé au nomcomp3, c'est à dire un vecteur de booléen ?

- [ ] maliste['comp3']

- [ ] maliste[3]

- [x] maliste[[3]]

- [x] maliste$comp3

> `maliste[3]` et `maliste['comp3']` permettent juste d'accéder à l'élément et non à ce qu'il contient. Les codes corrects pour faire ce que l'on cherche à faire sont donc `maliste[[3]]` et `maliste$comp3`.

## Quelles affirmations parmi les suivantes sont vraies concernant les dataframes ?

- [x] On peut sélectionner un élément via son numéro de ligne et son numéro de colonne

- [x] On peut sélectionner selon une condition

- [ ] On peut sélectionner dans un data.frame via l'opérateur `%`

- [ ] Le résultat d'une sélection sur un data.frame est forcément un autre data.frame

> La sélection dans les dataframes peut se faire comme la sélection dans les matrices ou comme la sélection dans les listes. Ainsi, on peut très bien sélectionner via l'indice ligne/colonne (comme avec une matrice) ou via une condition (comme avec une liste). On peut également sélectionner une colonne en particulier si on connait le nom qui y est associé, via l'opérateur `$`. Lorsque l'on sélectionne une seule colonne, le résultat sera par exemple un vecteur : donc le résultat d'une sélection sur un dataframe n'est pas forcément un data.frame.

## Soit le dataframe `df` suivant, représentant la température mesurée dans 3 villes différentes, sur deux jours :

```r

temp = c(20, 21, 17.5, 32, 30, 25)

jour = c('Lu', 'Lu', 'Lu', 'Ma', 'Ma', 'Ma')





df = data.frame(temp, jour, lieu)

```

Quel code permet de sélectionner les villes qui ont eu une température strictement supérieure à 20°C, le lundi ?

- [ ] `df[df$jour = 'Lu' & df$temp > 20, 'lieu']`

- [ ] `df[df$jour == 'Lu' & df$temp >= 20, 'lieu']`

- [ ] `df$lieu[df$jour == 'Lu' and df$temp > 20]`

- [x] `df$lieu[df$jour == 'Lu' & df$temp > 20]`

> Analysons code par code :

- `df[df$jour = 'Lu' & df$temp > 20, 'lieu']` contient une erreur. En effet, l'opérateur d'égalité dans une condition est `==`

- `df[df$jour == 'Lu' & df$temp >= 20, 'lieu']` ce code est quasiment juste, sauf qu'il sélectionne les villes pour lesquelles les températures sont supérieurs ou égales à 20. Hors nous voulons juste celles supérieurs. L'écriture correcte serait : `df[df$jour == 'Lu' & df$temp > 20, 'lieu']`

- `df$lieu[df$jour == 'Lu' and df$temp > 20]` contient une erreur : le mot clé `and ` n'existe pas en R, l'opérateur correspondant est `&`

- `df$lieu[df$jour == 'Lu' & df$temp > 20]` est correcte et fait bien ce que nous recherchons ici.

## Reprenons le dataframe df présenté question précédente. Que fait le code suivant :

```r

df[df$jour != 'Ma' & df$temp == max(df$temp[df$jour == 'Lu']), 'lieu']

```

- [ ] Il permet de sélectionner la température maximale observée sur le mardi

- [ ] Il permet de sélectionner le lieu de la température maximale observée sur un autre jour que mardi

- [ ] Il permet de sélectionner un lieu qui a eu une température égale à la maximale observé le lundi

- [x] Il permet de sélectionner tous les lieux qui ont eu une température égale à la maximale observé le lundi, sur un autre jour que le mardi

> Décomposons le code pour bien comprendre. Il y a ici deux conditions :

- la première `df$jour != 'Ma'` va sélectionner toutes les lignes dont le jours est différent de Mardi

- la seconde `df$temp == max(df$temp[df$jour == 'Lu'])` va sélectionner toutes lignes qui ont l'exacte même température que la maximale enregistrée le Lundi

- Étant donné qu'il y a l'opérateur `&` qui correspond au `ET` logique, la sélection doit valider la première et la seconde condition. Ainsi, on prend toutes les lignes différentes de Mardi, qui ont l'exacte même température que la maximale enregistrée le Lundi

- La fin de la sélection indique qu'on ne prend que la colonne Lieu.

Finalement, ce code permet donc de sélectionner tous les lieux qui ont eu une température égale à la maximale observé le lundi, sur un autre jour que le mardi.

# Localisez les données manquantes

## Résumé

Vous avez vu dans ce chapitre comment, à partir des fonctions `is.na()` et `which()`, identifier les NA qui viendraient à se trouver dans un de vos dataframes pour pouvoir les retirer de votre étude.

## Identifier les NA au sein d’un dataframe

Le décompte des individus manquants est spécifié variable par variable. Plaçons-nous dans le cas où le statisticien devrait savoir repérer les individus possédant une valeur manquante. Sa première tâche est de connaître l’identifiant, ou le numéro de ces individus. Pour cela, il suffit d’utiliser la fonction `is.na()`.

```r

ozR <- ozoneNA[1:4,1:7]

ozR

#     maxO3   T9  T12  T15 Ne9 Ne12 Ne15

# 601    87 15.6 18.5 18.4   4    4    8

# 602    82 17.0 18.4 17.7   5    5    7

# 603    NA   NA   NA 19.5   2    5    4

# 604    NA 16.2   NA 22.5   1   NA    0



is.na(ozR)

#     maxO3    T9   T12   T15   Ne9  Ne12  Ne15

# 601 FALSE FALSE FALSE FALSE FALSE FALSE FALSE

# 602 FALSE FALSE FALSE FALSE FALSE FALSE FALSE

# 603  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE

# 604  TRUE FALSE  TRUE FALSE FALSE  TRUE FALSE

```

À la question `is.na()`, R retourne un booléen. Ils prennent donc la valeur `NA ` dans le vecteur variable. Si nous souhaitons éliminer les individus qui possèdent au moins une valeur manquante, il faut d’abord repérer les valeurs manquantes. Nous souhaitons donc connaître les couples ligne/colonne des individus présentant une valeur manquante. Nous pouvons utiliser l’argument `arr.ind` (pour « array indices ») de la fonction `which()

```r

which(is.na(ozR),arr.ind=TRUE)

#     row col

# 603   3   1

# 604   4   1

# 603   3   2

# 603   3   3

# 604   4   3

# 604   4   6

```

La première donnée manquante correspond à la ligne 3 et la colonne 1, puis la suivante à la ligne 4 et la colonne 1...

> La fonction `which()` permet de ressortir les indices des éléments d’un objet (vecteur, dataframe, etc.) satisfaisant une condition donnée. Ici, par exemple, elle nous permet de ressortir l’ensemble des indices des éléments qui sont des NA, dans notre dataframe.

Pour enlever les individus qui admettent au moins un `NA`, il faut donc récupérer les indices des lignes qui se trouvent dans la colonne 1 du résultat :

```r

indligneNA <- which(is.na(ozR),arr.ind=TRUE)[, 1]

indligneNA

# 603 604 603 603 604 604

#   3   4   3   3   4   4



ozRsansNa <- ozR[-indligneNA, ]

```
