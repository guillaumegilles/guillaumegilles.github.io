---
id: zr8ulct6orohue6usk926r2
title: "R"
desc: langage de programmation R
updated: 1711636760102
created: 1669667999458
tags: anki
---

`R` est un langage de programmation interprété et un logiciel libre destiné aux
statistiques et à la science des données. Il fait partie de la liste des paquets
GNU3 et est écrit en `C`, `Fortran` et `R`.

Le langage R est largement utilisé par les statisticiens, les data miners, data
scientists pour le développement de logiciels statistiques et l'analyse des
données.

`R` fournit un langage de commande très souple et ouvert : il est possible de
connecter R avec d’autres langages comme C, Fortran, Java, JavaScript, Python…
il est aussi possible d’appeler des fonctions R depuis Matlab, Excel, etc. De
plus, des connectiques pour tous les types de bases de données existent : RMySQL
ou ROracle, pour ne citer que les plus connus.

- [The tidyverse style guide](https://style.tidyverse.org/syntax.html?q=comment#comments)

## `R` est un langage compilé ou interprété ?

`R` est un langage de programmation interprété

## Avec quels langages de programmation (3), `R` est-il écrit ?

Il est écrit en `C`, `Fortran` et `R`.

## Comment appelle-t-on les différents _type_ d’objet en R ?

**mode**

## Retouner le **mode** d'un objet R

`mode()` est une fonction `R` {base} qui retourne une chaîne de caractère décrivant le mode d'encodage d'une donnée, c’est-à-dire le [[r.dt]] ou [[r.ds]]

On peut facilement imaginer qu'il est nécessaire d'utiliser des _contenants_ différents si on veut conserver de la farine ou de l'eau. On utilise donc un mode différent pour stocker un booléen/ et un nombre.

```R
> x <- "Hello, world!"
> mode(x)
```

1. les nombres, on parle de [[r.dt.num]] ;
2. les nombres complexes, on parle de [[r.dt.complex]] ;
3. les caractères, on parle de [[r.dt.chr]] ;
4. les booléen, on parle de [[r.dt.lgl]] ;
5. les données vides, on parle de [[r.dt.null]]

- Packages

to load a package use this method ~rpart::~ exemple avec le package rpart

###### --------------------------------------------------------------

title: Les fonctions levels et order dans R
type: star
tags: #R #code

---

> # Scinder la note en 2
>
> - levels
>   \_- order

## levels()

## order()

The R order function returns a permutation of the order of the elements of a vector. The syntax with summarized descriptions of the arguments is as follows:

```r
order(x, # Sequence of s of the same length
      decreasing = FALSE, # Whether to sort in increasing or decreasing order
      na.last = TRUE,     # Whether to put NA values at the beginning or at the end
      method = c("auto", "shell", "radix")) # Method to be used. Defaults to auto
```

Définition
Les facteurs sont des vecteurs un peu particuliers, facilitant la manipulation de données qualitatives (qu’elles soient numériques ou caractères). En effet, en plus de stocker les différents éléments comme un vecteur classique, il stocke également l’ensemble des différentes modalités possibles dans un attribut accessible via la commande `levels`
Ils forment une classe d’objets et bénéficient de traitements particuliers lors de leur manipulation et lors de l’utilisation de certaines fonctions. Les facteurs peuvent être **non ordonnés** (homme, femme) ou **ordonnés** (niveaux de ski).
Création de facteur
Il y a 2 possibilités, la fonction `factor()` et `

```R
Y <- c("M", "F", "F", "M", "F")
y
# [1] "M" "F" "F" "M" "F"

yf <- factor(y)
yf
# [1] M F F M F
# Levels: F M
```

Il est possible de « regarder » les attributs de `yf`

```R
attributes(yf)
# $levels
# [1] "F" "M"
# $class
# [1] "factor"

levels(yf)
# [1] "F" "M"

nlevels(yf)
# [1] 2
```

Les `levels` correspondent aux modalités du facteur `yf`. Il est possible de les modifier :

```R
levels(yf) <- c("Femme","Homme")
yf
# [1] Homme Femme Femme Homme Femme
# Levels: Femme Homme
```

Ainsi, on modifie le facteur original comprenant les modalités F et H, elles deviennent respectivement Femme et Homme.

### Il est possible de modifier ces levels dès la création de la fonction `factor` avec l’argument `labels`

---

Et à présent, un exemple avec la fonction `as.factor()` :

```R
salto <- c(1:5,5:1)
salto
# [1] 1 2 3 4 5 5 4 3 2 1

salto.f <- as.factor(salto)
salto.f
# [1] 1 2 3 4 5 5 4 3 2 1
# Levels: 1 2 3 4 5
```

                              La fonction `ordered()`

La focntion `ordered()` permet de créer des facteurs **ordonnés** :

```R
niveau <- ordered(c("débutant", "débutant", "champion", "champion", "moyen", "moyen", "moyen", "champion"), levels = c("débutant", "moyen", "champion"))

niveau
# [1] débutant débutant champion champion moyen moyen moyen
# [8] champion
# Levels: débutant < moyen < champion
```

Les facteurs ont certains avantages, mais aussi certaines **contraintes de manipulation**. En effet, par exemple, il n’est pas possible de modifier ou d’ajouter un élément si celui-ci n’est pas dans la liste des `levels` . Il faut d’abord modifier les modalités possibles via la fonction `levels()` avant de pouvoir ajouter un nouvel élément. Pour vous affranchir des contraintes liées à l’utilisation des facteurs, vous pouvez à tout moment repasser sur un vecteur classique en utilisant les fonctions correspondantes : `as.numeric()` pour des numériques, `as.character()` pour des caractères, etc.

                              Utilisez des facteurs pour représenter la réalité

Lors de vos analyses statistiques, vous allez être confronté à de nombreuses variables qualitatives codées différemment :

- sous forme de vecteurs de caractères (comme des stations météo, etc.) ;
- sous forme de vecteurs numériques (comme des CSP où chaque numéro correspond à une catégorie particulière, par exemple 1 : ouvriers ; 2 : cadres ; etc.).

Les facteurs vont nous permettre de mieux faire comprendre à R que nous manipulons des variables qualitatives. Prenons l’exemple d’une variable `X` comportant des numériques :

```R
X <- c(rep(10,3),rep(12,2),rep(13,4))
X
# [1] 10 10 10 12 12 13 13 13 13
```

Il existe deux méthodes classiques pour savoir si un objet de type vecteur est une variable quantitative ou une variable qualitative sans afficher la totalité du vecteur. La première consiste à interroger R sur le type :

```R
is.factor(X)
# [1] FALSE

is.numeric(X)
# [1] TRUE
```

La seconde consiste à effectuer un résumé de la variable ( summary ). Quand il s’agit d’une variable quantitative, le minimum, le maximum, les quartiles et la moyenne sont affichés. Par contre, pour un facteur, le nombre d’observations pour les six premiers niveaux de la variable qualitative est donné :

```R
summary(X)
# Min.   1st Qu.  Median   Mean   3rd Qu.  Max.
# 10.00  10.00    12.00    11.78  13.00    13.00
```

De manière évidente, il s’agit bien ici d’une variable quantitative. La fonction `summary()` est particulièrement pratique pour déterminer les types au sein de tableaux de données (dataframe) issus d’une étape d’importation. En effet, le résumé est proposé variable par variable et il permet de repérer rapidement les éventuelles erreurs de type pour les variables.

Le passage en facteur se fait simplement en utilisant la fonction `factor()` :

```R
Xqual <- factor(X)
Xqual
# [1] 10 10 10 12 12 13 13 13 13
# Levels: 10 12 13

summary(Xqual)
# 10 12 13
# 3  2  4
```

L’affichage d’un facteur permet clairement de le distinguer d’un numérique par la présence des niveaux `levels` en fin d’affichage. Il en est de même pour le résumé fourni par `summary`.

                              Conversion d’un facteur en nnumérique

Le passage de facteur en numérique se fait en deux étapes. D’abord, il faut transforme le facteur en vecteur de type caractère, puis on transforme ce dernier en numérique. Si l’on transforme directement le facteur en numérique, les niveaux sont recodés dans l’ordre (le premier niveau sera 1, le deuxième 2, etc.) :

```R
## conversion avec recodage des modalités
as.numeric(Xqual)
# [1] 1 1 1 2 2 3 3 3 3

## conversion sans recodage des modalités : 2 étapes
provisoire <- as.character(Xqual)
provisoire
# [1] "10" "10" "10" "12" "12" "13" "13" "13" "13"

as.numeric(provisoire)
# [1] 10 10 10 12 12 13 13 13 13
```

# matrice

_Vidéo_ :

Matrice = objet monotype
Tous les éléments de la matrice sont de même modes. Une matrices de numériques, une matrices de caractères, une matrice de booléens.

On peut concaténer 2 matrices ensemble avec la fonction `cbind()`. Pour cela, il faut que les 2 matrices aient le même nombre de lignes. On peut également utiliser la fonction `rbind()`, dans ce cas, il faut que les matrice aient le même nombre de colonnes.

_Cours_ :

Les matrices - équivalentes aux matrices en mathématiques - peuvent être vues comme des tableaux de valeurs, à double entrée. Une matrice est donc définie par son nombre de lignes et de colonnes. Ce sont des objets monotypes, c’est-à-dire de même type pour tous ses éléments. Chaque valeur de la matrice peut être repérée par son numéro de ligne et son numéro de colonne. Les deux attributs intrinsèques d’un objet R sont la **longueur** `length`, qui correspond ici au nombre total d’éléments de la matrice, et le mode `mode` , qui correspond ici au mode des éléments de cette matrice. Les matrices possèdent également l’attribut de dimension `dim`, qui retourne le nombre de lignes et le nombre de colonnes.

## En résumé

- Les **matrices** sont des sortes de **tableaux monotypes à deux dimensions** où chaque élément est identifié par son **numéro de ligne** et son **numéro de colonne**.
- Vous pouvez **créer** une matrice soit à partir d’un objet existant (vecteur notamment), soit en définissant directement les éléments via la fonction `matrix()`.
- Vous pouvez réaliser de nombreuses **opérations d’algèbre linéaire** via différents opérateurs ou fonctions.
- Il existe plusieurs fonctions permettant d’accéder aux **dimensions** (nombre de lignes, nombre de colonnes, etc.) et/ou de **concaténer** des matrices.

## Création d’une matrice

Voici les principales façons de créer une matrice. La plus utilisée est la fonction `matrix` qui prend en arguments le vecteur d’éléments et les dimensions - nombre de lignes ou de colonnes - de la matrice. Par défaut, R range les valeurs dans une matrice par colonne. Pour ranger les éléments par ligne, on utilise l’argument `byrow` :

```R
x <- matrix(c(1:6), nrow = 2, ncol = 3, byrow = TRUE)
x
#      [,1] [,2] [,3]
# [1,]    1    2    3
# [2,]    4    5    6

y <- matrix(1:2, ncol = 1)
y
#      [,1]
# [1,]    1
# [2,]    2

z <- matrix(3:1, ncol = 3)
z
#      [,1] [,2] [,3]
# [1,]    3    2    1
```

Lorsque la longueur du vecteur est différente du nombre d’éléments de la matrice, R remplit toute la matrice. Si le vecteur est trop grand, il prend les premiers éléments, si le vecteur est trop petit, R le répète :

```R
m <- matrix(1:4, nrow = 3, ncol = 3)
m
#      [,1] [,2] [,3]
# [1,]    1    4    3
# [2,]    2    1    4
# [3,]    3    2    1
```

> Dans tous les cas, un message d’avertissement (Warning message) sera émis au moment de l’exécution de la ligne de code. De façon globale, les messages d’avertissement ne sont pas à prendre à la légère. Cela signifie généralement que R a fait quelque chose (comme compléter une matrice même s’il manque des éléments), mais que ce quelque chose ne correspond pas forcément à ce vous attendiez initialement.

Il est possible de remplir une matrice d’un élément unique sans avoir à créer le vecteur des éléments :

```R
un <- matrix(1, nrow = 2, ncol = 4)
un
#      [,1] [,2] [,3] [,4]
# [1,]    1    1    1    1
# [2,]    1    1    1    1
```

Un vecteur n’est pas considéré par R comme une matrice. Il est cependant possible de **transformer** un vecteur en une matrice **unicolonne** avec la fonction `as.matrix` :

```R
x <- seq(1, 10, by = 2)
x
# [1] 1 3 5 7 9

as.matrix(x)
#      [,1]
# [1,]    1
# [2,]    3
# [3,]    5
# [4,]    7
# [5,]    9
```

Il est bien évidemment possible de créer une matrice de caractères :

```R
matrix(c("A", "B", "C", "A"), ncol = 2)
#      [,1] [,2]
# [1,] "A"  "C"
# [2,] "B"  "A"
```

## Opérations entre matrices

Comme avec des matrices classiques, il est possible d’effectuer différentes opérations sur et avec des matrices. Considérons les deux matrices `m` et `n` suivantes :

```R
m <- matrix(1:4, ncol = 2)
m
#      [,1] [,2]
# [1,]    1    3
# [2,]    2    4

n <- matrix(3:6, ncol = 2, byrow = T)
n
#      [,1] [,2]
# [1,]    3    4
# [2,]    5    6
```

Vous pouvez additionner deux matrices de **même dimension** :

```R
m + n
#      [,1] [,2]
# [1,]    4    7
# [2,]    7   10
```

Ou calculer le produit entre deux matrices, lorsque le **nombre de lignes de la première est égal au nombre de colonnes de la deuxième**.

```R
# Produit élément par élément
m*n
#      [,1] [,2]
# [1,]    3   12
# [2,]   10   24
```

Et vous pouvez y appliquer toute une série d’**opérations mathématiques**, qui vont s’effectuer élément par élément :

```R
# Sinus élément par élément
sin(m)

# Exponentielle élément par élément

exp(m)

# Puissance quatrième élément par élément

m^4
```

Le tableau suivant donne les principales fonctions utiles en algèbre linéaire que vous pouvez également utiliser :

Fonction Description
X%_%Y produit (matriciel) de matrices
t(X) transposition d’une matrice
diag(5) matrice identité d’ordre 5
diag(vec) matrice diagonale avec les valeurs du vecteur `vec` dans la diagonale
crossprod(X, Y) produit croisé (t(X)%_%Y)
det(X) déterminant de la matrice X
svd(X) décomposition en valeurs singulières
eigen(X) diagonalisation d’une matrice
solve(X) inversion de matrice
solve(A, b) résolution de système linéaire
chol(Y) décomposition de Cholesky
qr(Y) décomposition QR

## Autres fonctions utiles

Nous présentons dans ce paragraphe quelques fonctions utiles pour manipuler vos matrices :

### Dimensions : `dim()`, `nrow()`, `ncol()` donnent respectivement la dimension, le nombre de lignes et de colonnes de X.

```R
X <- matrix(1:6, ncol = 3)
X
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6

ncol(X)
# [1] 3

nrow(X)
# [1] 2

dim(X)
# [1] 2 3
```

Ces fonctions renvoient NULL si X est un vecteur.

### Concaténation : par colonne avec la fonction `cbind()`, par ligne avec la fonction `rbind()`.

```R
cbind(c(1, 2), c(3, 4))
#      [,1] [,2]
# [1,]    1    3
# [2,]    2    4
```

### La fonction `apply()` permet d’appliquer une fonction choisie aux lignes (MARGIN=1) ou aux colonnes (MARGIN=2) de la matrice. Par exemple :

```R
# Sommes par colonne

apply(X, MARGIN = 2, sum)
# [1] 3 7 11

# Moyennes par ligne

apply(X, 1, mean)
# [1] 3 4
```

# Liste

La liste est un objet R hétéroclite, elle peut contenir :
• Vecteurs de caractères ;
• Vecteurs de numériques ;
• Des matrices ;
• Des listes

Lors de vos analyses statistiques, vous risquez d’être confronté à la gestion de plusieurs données de **types différents** et potentiellement de **longueurs différentes**. Bien entendu, vous pourriez stocker tous ces éléments dans autant de vecteurs/variables/facteurs en fonction de vos besoins. Mais ne serait-il pas plus pratique d’avoir un seul objet permettant de stocker tous ces différents objets ? C’est ce à quoi correspondent les **listes**.

Une liste est un ensemble ordonné d’objets qui n’ont pas toujours le même mode ou la même longueur. Les différents objets sont appelés des composantes et peuvent être associés à un nom spécifique (un peu comme une variable). Les listes ont les deux **attributs** des vecteurs (_length_ et _mode_) et l’attribut supplémentaire **names**. Les listes sont des objets indispensables, car toutes les fonctions qui retournent plusieurs objets le font sous la forme d’une liste.

## Création de listes

La fonction de base pour créer une liste est la fonction `list()` :

```R
maliste <- list(c("A","B","C","A"),matrix(1:4,2,2))
maliste
# [[1]]
# [1] "A" "B" "C" "A"

# [[2]]
#      [,1] [,2]
# [1,]    1    3
# [2,]    2    4
```

Cette liste contient bien 2 objets et c’est bien une liste, comme nous pouvons le voir ci-dessous :

```R
length(maliste)
# [1] 2

mode(maliste)
# [1] "list"

is.list(maliste)
# [1] TRUE
```

Comme dit plus tôt, vous pouvez nommer les composantes de la liste, c’est-à-dire associer un nom à chaque objet de la liste pour pouvoir y accéder plus facilement via l’opérateur `$`. Ceci est faisable via la fonction `names()` :

```R
names(maliste) # pas de nom actuellement, la fonction retourne un NULL
# NULL

names(maliste) <- c("vec","mat")
names(maliste)
# [1] "vec" "mat"
```

Il est également possible de créer une liste en partant d’une liste vide.

```R
li <- list()
li
# list()

li[[1]] <- 1:4
li
# [[1]]
# [1] 1 2 3 4

li$nouv <- matrix(1:4,nrow=2)
li
# [[1]]
# [1] 1 2 3 4

# $nouv
#      [,1] [,2]
# [1,]    1    3
# [2,]    2    4
```

Comme la première composante n’a pas de nom, on retrouve `[[1]]` dans l’affichage de la liste puis la composante `nouv`.

```R
names(li)
# [1] "" "nouv"
```

et les attributs de cette liste sont les noms.

## Fonctions utiles applicables aux listes

Comme les objets d’une liste n’ont pas forcément le même type, il n’est pas possible de faire des calculs entre plusieurs listes. Néanmoins, il existe quelques fonctions valides et utiles :

- `lapply()` applique une fonction (comme la moyenne, la variance, etc.) successivement à chacune des composantes.
- `unlist()` crée un seul vecteur contenant tous les éléments de la liste. Les éléments d’un vecteur étant nécessairement du même mode, il faut faire attention à la conversion automatique pratiquée par R.
- `c(liste1,liste2)` concatène deux listes.

## En résumé

- Une liste est un **ensemble ordonné d’objets** qui n’ont pas toujours le même _mode_ ou la même _longueur_.
- Il est possible d’associer un nom à un objet spécifique de la liste.
- Plusieurs fonctions permettent d’effectuer une action sur chaque élément d’une liste.

# Quizz #1

## Q1 - Concernant les vecteurs, quelles affirmations parmi les suivantes sont vraies ?

- [] Les vecteurs peuvent contenir plusieurs types

> Les vecteurs sont monotypes, ils ne peuvent donc contenir qu'un seul type donné.

- [x] La longueur d'un vecteur peut être obtenue via la fonction `length()`

Si vous avez un vecteur `a`, il suffit d'utiliser la fonction `length()` pour obtenir sa taille.

- [] `seq` permet de créer un vecteur en répétant plusieurs fois un ou plusieurs éléments

`seq` permet de générer une séquence de nombre également répartis dans un intervalle donné. La fonction pour répéter un ou plusieurs éléments un certain nombre de fois est `rep`.

- [x] `c()` permet de créer un vecteur en spécifiant les différents éléments de ce dernier

> `c` permet de créer un vecteur en spécifiant les éléments à l'intérieur. Si par exemple je veux créer le vecteur 1, 2, 3 : `a <- c(1, 2, 3)`.

## Q2 - Quel sera le résultat affiché dans la console suite à l'exécution des lignes suivantes :

```R
x <- c(rep(10, times = 3), seq(1, 5, by = 1), 1, 2, 3)
x
```

Décomposons l'instruction :

- `c(rep(10, times = 3)` va répéter l'entier 10 trois fois, le début sera donc `10, 10, 10`
- `seq(1, 5, by = 1)` va créer une séquence de 1 à 5, par 1. La suite sera donc `1, 2, 3, 4, 5`
- `1, 2, 3` correspondra simplement à `1, 2, 3` à la suite.
  Mis bout à bout, on obtient : `10, 10, 10, 1, 2, 3, 4, 5, 1, 2, 3`

## Q3 - Concernant les facteurs, quelles affirmations parmi les suivantes sont vraies ?

- [x] Les facteurs sont des vecteurs particuliers pour des données qualitatives
- [ ] Les facteurs ne peuvent contenir qu'une seule modalité
- [x] Les différentes valeurs possibles d'un facteur peuvent être obtenues via la fonction `levels()`
- [ ] Il n'est pas possible d'ordonner les niveaux d'un facteurs

> Les facteurs sont des vecteurs permettant la manipulation de données qualitatives. Par conséquence, ils prennent en compte plusieurs modalités d'une variable qualitative. Les différentes modalités peuvent d'ailleurs être obtenus via la fonctions `levels()`. Il est tout à fait possible d'ordonner un facteur, via la fonction `ordered()`.

## Q4 - La fonction pour transformer un vecteur en facteur est :

La fonction pour transformer un vecteur existant en facteur est `as.factor()`

## Q5 - Concernant les matrices, quelles affirmations parmi les suivantes sont vraies ?

- [x] Une matrice ne peut contenir qu'un seul type
- [x] On peut accéder à un élément d'une matrice via son indice de ligne et de colonne
- [] La fonction `length` permet d'avoir le nombre de lignes et de colonnes d'une matrice
- [x] Il est possible de créer une matrice de caractères

> Une matrice peut être vue comme une sorte de tableau, on peut donc accéder à un élément via son numéro de ligne/colonne. Elle ne peut contenir qu'un seul type, qui peut être numérique, caractère, booléen, etc... Pour avoir les dimensions de la matrice (nombres de lignes et de colonnes), il faut utiliser la fonction `dim`.

Q6 - Quel sera le résultat affiché dans la console suite à l'exécution des lignes suivantes :

```r
m <- matrix(1, nrow = 3, ncol = 3)
vec <- c(1, 2, 3)
m[1, 3] = 3
m <- m + diag(vec)
t(m)
```

```R
     [,1]  [,2]  [,3]
[1,]    2     1     1
[2,]    1     3     1
[3,]    3     1     4
```

> Évaluons ligne par ligne :

1. On crée une matrice 3x3, remplie par des 1
2. On crée un vecteur `vec` contenant les valeurs 1, 2 et 3
3. On remplace la valeur située à la première ligne et à la troisième colonne de `m``par 3
4. on ajoute à `m` une matrice dont la diagonale a les valeurs de `vec`

À ce stade, la matrice stockée dans `m` est :

```R
     [,1]  [,2]  [,3]
[1,]    2     1     3
[2,]    1     3     1
[3,]    1     1     4
```

Dans la dernière ligne, on prend la transposée de cette matrice. Ainsi, l'affichage final est bien :

```R
    [,1]  [,2]  [,3]
[1,]    2     1     1
[2,]    1     3     1
[3,]    3     1     4
```

## Q7 - Concernant les liste, quelles affirmations parmi les suivantes sont vraies ?

- [] Une liste ne peut contenir qu'un seul type

> Une liste peut contenir plusieurs types.

- [] Si j'utilise la fonction `length()` sur la liste suivante : `list(c("A", "B", "C", "A"), matrix(1:4, 2, 2))`. Celle-ci renverra bien la valeur 8.

> Dans l'exemple donné, la fonction `length()` renverra bien 2, car il y a uniquement deux objets : un vecteur et une matrice.

- [x] Lorsqu'ils sont nommés, on peut accéder aux différents objets contenus dans une liste via l'opérateur `$`

> Lorsqu'ils sont nommés, on peut accéder aux différents objets contenus dans une liste via l'opérateur `$`

- [x] On peut accéder aux différents objets d'une liste via leurs indices

> On peut accéder aux différents objets d'une liste via leurs indices

## Q8 - Concernant les dataframes, quelles affirmations parmi les suivantes sont vraies ?

- [x] Les dataframes sont des listes particulières dont les composantes sont de même taille

> Les dataframes sont des listes particulières dont les composantes sont de même taille.

- [] Les modes des différentes composantes d'un dataframe doivent être tous identiques

> Les modes des différentes composantes d'un dataframe peuvent être différents. Il faut voir un dataframe comme un tableau de données. Ainsi, on peut avoir une colonne représentant des valeurs quantitatives, une autre représentant une variable qualitative, etc...

- [x] On peut créer un dataframe à partir d'un tableau de données externe (.txt, .csv, etc...)

> On peut créer un dataframe à partir d'un tableau de données externe (.txt, .csv, etc...) via la fonction `read.table` que nous verrons prochainement.

- [] Il n'est pas possible de transformer une matrice en dataframe

> Il est possible de transformer une matrice en dataframe via la fonction `as.data.frame`

---

Lorsqu'on utilise des packages avec R, il est important d'appeler les fonctions du package avec le code suivant : `package::function`

```r
dplyr::select
# Permet d'utiliser la fonction select du package dplyr
```

Ainsi, il n'y a pas de collusion entre différentes fonctions possédant le même nom dans divers packages. Cette situation ne peut pas arriver si on utilise un seul package, mais il est rare de n'utiliser q'un seul package. Aussi, on préférera appeler la fonction avec son package.

---

🌅 Note créée le : 11-06-2021
📑 Note éditée le :

---

title: Modèle macroéconomique FR BDF
type: protostar
tags: #economy #mathematics

---

## Qu’est-ce qu’un modèle ?

> faire le lien avec mes notes de formation data science de l’ENSAE

https://www.youtube.com/watch?v=qH_ltaEpQdE

https://www.banque-france.fr/sites/default/files/media/2021/07/02/methodologie_projections_macro_bdf.pdf

https://publications.banque-france.fr/le-modele-fr-bdf-et-une-evaluation-des-effets-de-la-politique-monetaire-en-france

https://www.banque-france.fr/sites/default/files/medias/documents/818334_rdb68_fr_v7.pdf#search=mod%C3%A8le%20mapi%20inflation

- présentation outil DPCM

---

title: Comment sélectionner un élément dans R

# Familiarisez-vous avec la sélection d'éléments

En statistique, les données constituent le point de départ de toute analyse. Il est en effet très courant d’avoir à sélectionner une partie de nos données, soit en sélectionnant manuellement un sous-échantillon (par exemple les 30 premières lignes), soit selon une condition donnée (par exemple uniquement les femmes, ou les personnes de moins de 25 ans, etc.). Il est donc obligatoire de maîtriser les opérations de sélection simples que nous présentons ici.

## En résumé

Il existe deux façons de sélectionner des éléments au sein d’un objet en R : soit via une sélection par position (ou indice), soit via une sélection par condition.

Les conditions peuvent être construites en utilisant des opérateurs de comparaisons et/ou des opérateurs logiques.

## Principes de sélections

Il y a deux grands principes dans la sélection d’éléments d’un objet R :

- la sélection par **position** : il faut indiquer un ou plusieurs vecteurs de positions (ou d’indices), des éléments à sélectionner ;

- la sélection par **condition** : il faut indiquer une condition (qui pourra être construite via différents opérateurs de comparaison et des opérateurs logiques) et ne seront sélectionnés que les éléments satisfaisant cette condition.

Dans tous les cas, la sélection s’opère avec l’opérateur de sélection [ ].

### La sélection par condition

Nous reviendrons un peu plus en détail dans les chapitres suivants sur la sélection par position, mais pour celle par condition, vous allez avoir besoin d’utiliser des opérateurs de comparaison pour construire vos conditions. Comme le nom le suggère, les opérateurs de comparaison sont utilisés pour comparer deux valeurs. Il y en a six principaux :

- `==` égal à (deux valeurs sont exactement pareilles)

- `!=` différent de

- `<` inférieur à

- `<=` inférieur ou égal

- `>` supérieur à

- `>=` supérieur ou égal

Voici quelques exemples avec des valeurs numériques :

```R

2 == 2 # -> TRUE

2 == 3 # -> FALSE

4 != 4 # -> FALSE

4!= 5 # -> TRUE

1 < 2 # -> TRUE

1 < 1 # -> FALSE

1 <= 1 # -> TRUE

3 > 4 # -> FALSE

5 > 4 # -> TRUE

5 >= 4 # -> TRUE

```

Et à présent un exemple simple avec un vecteur :

```R

x <- -2:5

x > 0

# [1] FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE  TRUE

```

On voit bien que le résultat est un vecteur de booléen, indiquant pour chaque élément si la condition est vraie ou non.

Parfois, vous allez avoir besoin de conditions plus élaborées, ou la condition va être le résultat de la combinaison de plusieurs expressions. C’est là qu’interviennent les **opérateurs logiques**.

Ces opérateurs vont vous permettre de mixer plusieurs valeurs booléennes : des valeurs booléennes spécifiques ou des résultats d’expression. Il y en a 3 :

- `&` : l’opérateur ET. Le résultat final est vrai seulement lorsque toutes les conditions sont vraies. Par exemple : le résultat de `condition1 & condition2` sera TRUE seulement si `condition1` est vraie ET `condition2` est également vraie.

- `|` : l’opérateur OU. Le résultat final est vrai lorsque au moins une des conditions est vraie. Par exemple : le résultat de `condition1  | condition2` sera TRUE si `condition1` est vraie OU `condition2` est vraie.

- `!` : l’opérateur N’EST PAS. Cela inverse simplement le résultat de la condition donnée. Par exemple, le résultat de `!(condition)` est vrai lorsque `condition` est faux.

Quelques exemples d’utilisation de ces opérateurs :

```R

TRUE & TRUE # TRUE

TRUE & FALSE # FALSE

FALSE & FALSE # FALSE

TRUE | FALSE # TRUE

TRUE | TRUE # TRUE

FALSE | FALSE # FALSE

!TRUE # FALSE

!FALSE # TRUE

```

---

# R

## Sélection dans un vecteur

### En résumé

Il est possible de sélectionner au sein d’un vecteur selon :

- Un **vecteur d’entiers positifs** : dans ce cas, les entiers correspondent aux indices des éléments à sélectionner ;
- Un **vecteur d’entiers négatifs** : dans ce cas, les entiers correspondent aux indices des éléments à exclure du résultat final ;
- Une **condition** : dans ce cas, le résultat sera constitué de l’ensemble des éléments du vecteur initial qui satisfont cette condition.

---

La sélection au sein d’un vecteur s’opère avec l’**opérateur de sélection** `[ ]` et un vecteur de sélection pouvant être un vecteur d’entiers positifs, d’entiers négatifs ou de logiques :

```R
x[vecteurdeselection]
```

## Sélection par position

La sélection la plus naturelle est la sélection par des vecteurs d’**entiers positifs**. Les entiers sont les **indices** des éléments à sélectionner et doivent être compris entre 1 et la longueur du vecteur considéré (obtenue via la fonction `length()`). La longueur du vecteur d’indices peut être quelconque :

```R
x <- c(2,-1,15)
x[2] # donne le deuxième élément de x
# [1] -1

x[c(1,3)] # donne les premier et troisième éléments de x
# [1] 2 15

x[c(3,1,2,2,1)]
# [1] 15 2 -1 -1 2
```

Une autre méthode consiste à enlever les éléments du vecteur que l’on ne souhaite pas conserver : c’est la sélection par des vecteurs d’**entiers négatifs**. Le vecteur d’indices indique les indices des éléments à exclure du résultat final :

```R
x[-2] # ne donne pas le deuxième élément de x
# [1] 2 15
```

**??????** Une autre façon de procéder consiste à sélectionner des éléments du vecteur en fonction de leur valeur ou d’autres éléments provenant d’autres objets R. Cela conduit à la sélection par des vecteurs de logiques.

## Sélection par condition

Cette sélection permet l’extraction d’éléments particuliers que l’on sait caractériser par une périphrase ou par une condition logique :

- L’élément de sgenre masculin (M);
- L’élément qui possède une valeur inférieure à 5 et (ou) supérieure ou égale à 12.

Prenons par exemple les éléments de `x` qui sont positifs.

```r
x[x>0]
# [1] 2 15

x[!(x<0)]
# [1] 2 15
```

Cependant, aucun élément n’est à la fois inférieur à 5 et supérieur à 12, la fonction retourne
alors l’ensemble vide avec `integer(0)` :

```r
x[(x<5) & (x>=12)]
# numeric(0)
```

On peut aussi sélectionner les valeurs d’un vecteur à partir des valeurs d’un autre vecteur de même longueur :

```R
T <- c(23, 28, 24, 32)
O3 <- c(80, 102, 87, 124)
O3[T>25]
# [1] 102 124
```

#########

# Sélection dans un dataframe

Tout comme la création, la sélection dans les dataframes est à mi-chemin entre la sélection dans les matrices et celle dans les listes. Commençons par créer un dataframe :

```R
x <- c("A","B","C",rep("D",3))
y <- 1:6
z <- c(seq(10,45,length=5),-10)
mondf <- data.frame(x,y,z)
mondf
#   x y      z
# 1 A 1  10.00
# 2 B 2  18.75
# 3 C 3  27.50
# 4 D 4  36.25
# 5 D 5  45.00
# 6 D 6 -10.00
```

## En résumé

Le dataframe étant un objet à mi-chemin entre une liste et une matrice, il partage les façons de sélectionner de ces deux types :

- Vous pouvez sélectionner selon un **indice** ou un **vecteur d’indice**, sur les lignes, les colonnes ou les deux en même temps.
- Vous pouvez sélectionner en précisant le nom associé à la colonne d’un dataframe.
- Vous pouvez sélectionner selon une condition qui ne va conserver que les lignes qui satisfont ladite condition.
- Et il est tout à fait possible de mixer ces différentes méthodes pour arriver à une sélection bien précise !

## Sélection par position

Comme avec les matrices, il est possible de spécifier des lignes et/ou colonnes à sélectionner. Voici un exemple avec une sélection des 4 premières lignes et des colonnes 2 et 3 :

```R
mondf[1:4,2:3]
#   y     z
# 1 1 10.00
# 2 2 18.75
# 3 3 27.50
# 4 4 36.25
```

Nous pouvons, tout comme avec une liste, sélectionner via un nom associé à une colonne au sein du dataframe :

```R
mondf$z
# [1] 10.00 18.75 27.50 36.25 45.00 -10.00

mondf["z"]
#        z
# 1  10.00
# 2  18.75
# 3  27.50
# 4  36.25
# 5  45.00
# 6 -10.00
```

Il est également possible de pouvoir mixer les deux. Par exemple ici, nous sélectionnons les lignes 2 à 4 de la colonne `x` :

```R
mondf$x[2:4]
# [1] B C D
# Levels: A B C D
```

> Notez ici que le vecteur de caractères a été automatiquement modifié en **facteur** par R lors de la création du dataframe. Si jamais vous souhaitez éviter cela, vous devrez préciser l’argument `stringsAsFactors = FALSE` lors de la création du dataframe !

## Sélection par conditions

Même s’il arrive de sélectionner par indice, il est généralement plus courant de devoir sélectionner selon une condition. Par exemple, la ligne suivante permet de sélectionner toutes les lignes qui satisfont la condition spécifiée :

```R
mondf[mondf$y>4,]
#   x y   z
# 5 D 5  45
# 6 D 6 -10

mondf[(mondf$y>4)|(mondf$z>17),]
#   x y      z
# 2 B 2  18.75
# 3 C 3  27.50
# 4 D 4  36.25
# 5 D 5  45.00
# 6 D 6 -10.00

mondf[(mondf$y>4)&(mondf$z>17),]
#   x y   z
# 5 D 5  45
```

Vous noterez que, lors de la construction de vos conditions, il est indispensable de repréciser l’association `dataframe$colonne`, même si le nom associé à une colonne d’un dataframe est forcément unique. Vous pouvez également préciser une ou plusieurs colonnes en particulier :

```R
mondf[mondf$y>4,1:2] # équivalent à
mondf[mondf$y>4,c('x','y')]
#   x y
# 5 D 5
# 6 D 6
```

######

######

# Sélection dans une liste

Pour extraire une composante de la liste, on peut toujours le faire en indiquant la position de l’élément que l’on souhaite extraire.

## En résumé

Il existe différentes façons de sélectionner au sein d’une liste :

- soit c’est une sélection par **position**. Cependant, il faut bien être vigilant à la différence entre une sélection via `[ ]` qui renverra une sous-liste de la liste originale et une sélection via `[[ ]]` qui renverra l’objet stocké dans la liste à laquelle on essaie d’accéder ;
- soit c’est une sélection par nom, où l’on peut accéder à une sous-liste ou un objet spécifique en utilisant le nom qui y est associé au sein de la liste.

## Sélection par position

Les `[[ ]]` permettent de retourner l’élément de la liste. Il faut faire la distinction entre :

- `maliste[1]` qui retourne une sous-liste composée de l’élément 1 de la liste initiale. `length(maliste[1])` vaut donc 1.
- `maliste[[1]]` qui retourne l’objet R qui compose l’élément 1 de la liste. `length(maliste[[1]])` retourne la longueur de l’objet stocké en premier dans la liste `maliste`.

Commençons par créer une liste de 4 éléments.

```R
x <- c("a","a","b","c")
X <- matrix(1:8,ncol=4)
y <- c(T,T,T,F,F)
z <- matrix(c("A","B","C","D"),ncol=2)

maliste <- list(comp1=x,comp2=X,comp3=y,element4=z)
maliste
# $comp1
# [1] "a" "a" "b" "c"
#
# $comp2
#      [,1] [,2] [,3] [,4]
# [1,]    1    3    5    7
# [2,]    2    4    6    8
#
# $comp3
# [1]  TRUE  TRUE  TRUE FALSE FALSE
#
# $element4
#      [,1] [,2]
# [1,] "A"  "C"
# [2,] "B"  "D"
```

Voyons à présent les différences notables entre la sélection avec l’opérateur `[ ]` et celle avec l’opérateur `[[ ]]` au sein de notre liste de 4 objets :

```R
maliste[2] #retourne une liste
# $comp2
#      [,1] [,2] [,3] [,4]
# [1,]    1    3    5    7
# [2,]    2    4    6    8

length(maliste[2])
# [1] 1

maliste[[2]] #extrait le second élément de la liste
#      [,1] [,2] [,3] [,4]
# [1,]    1    3    5    7
# [2,]    2    4    6    8

length(maliste[[2]])
# [1] 8
# puisqu’il y a 8 éléments dans la composante 2 de maliste.
```

## Sélection par nom

Lorsque vous souhaitez sélectionner au sein d’une liste en utilisant directement le nom d’un des objets qu’elle contient, vous pouvez l’écrire de deux façons :

- soit de façon similaire à une sélection par position en précisant le nom entre quotes,
- soit via l’opérateur `$`.

Par exemple :

```R
maliste["comp2"]
# $comp2
#      [,1] [,2] [,3] [,4]
# [1,]    1    3    5    7
# [2,]    2    4    6    8

maliste[["comp2"]]
#      [,1] [,2] [,3] [,4]
# [1,]    1    3    5    7
# [2,]    2    4    6    8

maliste$comp2
#      [,1] [,2] [,3] [,4]
# [1,]    1    3    5    7
# [2,]    2    4    6    8
```

> Notez bien ici encore une fois la différence entre l’opérateur `[ ]` qui renvoie une sous-liste et l’opérateur `[[ ]]` qui renvoie l’objet que l’on souhaite sélectionner.

Il est possible d’extraire plusieurs éléments d’une même liste, ce qui crée une sous-liste. Noter qu’ici l’on utilise `[ ]` et non `[[ ]]` :

```R
maliste[c(1,3)]
# $comp1
# [1] "a" "a" "b" "c"
#
# $comp3
# [1]  TRUE  TRUE  TRUE FALSE FALSE
```

######

Tags : #r #matrice
Résumé :

Il est possible de sélectionner au sein d’une matrice selon
un entier positif ou un vecteur d’entiers positifs : pour pouvoir sélectionner en particulier une ligne ou une colonne. Un cas particulier est de spécifier un numéro de ligne et de colonne dans le cas où vous souhaiteriez ne sélectionner qu’un seul élément bien identifié ;

un entier négatif ou un vecteur d’entiers négatifs : pour exclure du résultat final les éléments dont les indices sont représentés par les entiers ;

une condition : définie soit sur les lignes, soit sur les colonnes, voire les deux en même temps.

---

# Sélection dans une matrice

L’emplacement d’un élément dans une matrice est en général donné par le numéro de sa ligne `i` et de sa colonne `j`. Ainsi, pour sélectionner l’élément `(i, j)` de la matrice `m`, il faut écrire : `m[i,j]`. Cependant, il est rare de ne sélectionner qu'un seul élément dans une matrice. On sélectionne plus souvent une ou plusieurs lignes et/ou colonnes.

## Sélection par indices

Le premier cas est la sélection par des entiers positifs : `m[i,]`. On retourne la ligne `i` sous la forme d’un vecteur. Pour conserver la structure de matrice il faut ajouter l’argument `drop` : `m[i, , drop=F]`. donne la ligne `i` sous la forme d’une matrice uniligne et non plus d’un vecteur, ce qui permet de conserver le nom de la ligne.

Il est possible de sélectionner plusieurs fois la même ligne et/ou colonne grâce à la synthaxe : `m[,c(2,2,1)]`. Cette synthaxe retourne aucune ligne, ainsi que deux fois la seconde colonne, puis une fois la première colonne : c’est donc une matrice à trois colonnes.

Tout comme avec les vecteurs, il est possible de faire une selection avec des entiers négatifs, pour éliminer des éléments :

```r
# La matrice, m, sans sa première ligne

m[-1,]

# Les deux premières lignes de la matrice m, privée de sa première colonne

m[1:2,-1]
```

## Sélection par conditions

On peut également sélectionner selon une condition, définie soit sur les lignes, soit sur les colonnes, voire les deux en même temps !

```r
X <- matrix(1:12,nrow=3,ncol=4)
X
#      [,1] [,2] [,3] [,4]
# [1,]    1    4    7   10
# [2,]    2    5    8   11
# [3,]    3    6    9   12
```

L’instruction suivante retourne uniquement les colonnes de X pour lesquelles la valeur sur la première ligne est strictement supérieure à 2 :

```r
X[,X[1,]>2]
#      [,1] [,2] [,3]
# [1,]    4    7   10
# [2,]    5    8   11
# [3,]    6    9   12
```

C’est donc une matrice, alors que l’instruction suivante retourne un vecteur contenant les valeurs de X supérieures à 2 :

```r
X[X>2]
# [1]  3  4  5  6  7  8  9 10 11 12
```

L’instruction suivante quant à elle remplace les valeurs de X inférieures à 5 par des NA

```r
X[X<5] <- NA
#      [,1] [,2] [,3] [,4]
# [1,]   NA   NA    7   10
# [2,]   NA    5    8   11
# [3,]   NA    6    9   12
```

########
