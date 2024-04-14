---
id: vnzr1vz3rvuhb55qxb0qx9h
title: Vector
desc: ""
updated: 1708980995471
created: 1708980890755
---

[Utilisez les vecteurs](https://openclassrooms.com/fr/courses/4525256-initiez-vous-au-langage-r-pour-analyser-vos-donnees/6250872-utilisez-les-vecteurs)

Le vecteur est une sorte de tableau d’une ligne (ou une colonne) pouvant stocker plusieurs valeurs appelées composantes, coordonnées ou éléments. C’est un objet monotype : tous les éléments d’un vecteur sont donc du même type. Tout comme chaque objet, on peut obtenir l’attribut longueur (correspondant au nombre d’éléments contenus dans un vecteur) via la fonction length .

Les vecteurs numériques

Les vecteurs numériques vont permettre de représenter numériquement toutes les séries de nombres que vous pourrez rencontrer lors de vos analyses : relevés météorologiques, notes d’une classe, taille de différentes fleurs, etc. De façon générale, ils vont permettre de représenter toutes vos variables quantitatives.

Il existe différentes méthodes pour construire un vecteur, que vous pouvez utiliser en fonction de vos besoins :

    Construction par l’opérateur séquence  :. Ce dernier permet de créer un vecteur allant de la première valeur à la deuxième, par pas de 1.

· 1:6

· # [1] 1 2 3 4 5 6

    Construction par la fonction  seq  , qui va créer un vecteur contenant l’ensemble des valeurs de a  à  b  , soit répartis également si l’on utilise l’argument  length  , soit selon un pas donné via l’argument  by  . Par exemple :

· seq(1,6,by=0.5)

· # [1] 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0

·

· seq(1,6,length=5)

· # [1] 1.00 2.25 3.50 4.75 6.00

    Construction par la fonction collecteur  c  . Cette dernière permet de construire un vecteur en citant explicitement l’ensemble des valeurs que l’on stocke à l’intérieur.

· x <- c(1, 4, 10) # vecteur de numériques à 3 éléments

· x

· # [1] 1 4 10

·

· y <- seq(1,10,by=2) # vecteur à 7 éléments

· y

· # [1] 1 3 5 7 9

·

· z <- c(x,y)

· z

· # [1] 1 4 10 1 3 5 7 9

    Construction par la fonction  rep  , qui va répéter un objet (valeur seule, vecteur, etc.) un nombre de fois fixé.

· rep(1,4)

· # [1] 1 1 1 1

·

· rep(c(1,2),each=3)

· # [1] 1 1 1 2 2 2

Les vecteurs de caractères

Les vecteurs de caractères vont eux représenter toutes les séries d’informations textuelles comme : les noms de stations météo, les noms des élèves, les espèces de fleurs, etc. De façon globale, ils permettront de représenter des variables qualitatives.

Il est possible de créer des vecteurs de caractères de la même façon que des vecteurs numériques, en utilisant les fonctions c ou rep . Par exemple :

x <- c("bonjour","hello","hej")

x

# [1] "bonjour" "hello" "hej"

x <- rep(c("rouge","jaune","bleu"),times=2)

x

# [1] "rouge" "jaune" "bleu" "rouge" "jaune" "bleu"

rep(c("rouge","jaune","bleu"),each=2)

# [1] "rouge" "rouge" "jaune" "jaune" "bleu" "bleu"

rep(c("rouge","jaune","bleu"),times=c(1,4,2))

# [1] "rouge" "jaune" "jaune" "jaune" "jaune" "bleu" "bleu"

Il est également possible de créer un vecteur numérique pour ensuite le convertir en un vecteur de chaînes de caractères de même longueur, via la fonction format (voir aussi la fonction toString ).

Création par concaténation

Une autre façon de procéder, pour créer un vecteur de caractères, est de manipuler différents objets R et de les concaténer (c’est-à-dire les mettre bout à bout) ou d’en extraire une partie. Pour la concaténation, on utilise la fonction paste :

nom <- paste(rep("ind",10),1:10,sep=".")

# [1] "ind.1" "ind.2" "ind.3" "ind.4" "ind.5" "ind.6" "ind.7" "ind.8"

# [9] "ind.9" "ind.10"

paste(c("X","Y"),1:5,sep=".",collapse="+")

# [1] "X.1+Y.2+X.3+Y.4+X.5"

L’argument collapse permet de concaténer l’ensemble des éléments d’un vecteur en un seul, délimités par le caractère passé en argument. Par exemple, ci-dessus, le résultat correspond à l’ensemble des valeurs du vecteur mises bout à bout, entrecoupées par le caractère + .

Pour l’extraction, on utilise la fonction substr .

substr("freerider",5,9)

# [1] "rider"

Cela extrait de "freerider" les caractères en position 5 à 9 ce qui donne "rider".

Vecteurs logiques

Les vecteurs logiques sont un peu particuliers en pratique. Ils peuvent représenter des vecteurs binaires (pluie ou beau temps, présence ou non d’une maladie, etc.), mais peuvent aussi être le résultat d’une fonction appliquée à un autre vecteur (comme avec la fonction is.na vue précédemment).

Les vecteurs de booléens sont en général générés grâce à des opérateurs logiques : > , >= , < , <= , == , != , etc. Ils peuvent aussi être générés par les fonctions seq , rep et c . Ils permettent des sélections complexes ou des opérations de conditions.

Prenons l’exemple suivant :

1>0

# [1] TRUE

Cette commande retourne un vecteur logique de longueur 1 qui est TRUE, puisque 1 est plus grand que 0. De façon similaire, la commande :

> x>13

retourne un vecteur logique de même longueur que x . Ses éléments ont la valeur TRUE quand l’élément correspondant satisfait la condition (ici strictement supérieur à 13) et la valeur FALSE s’il ne la satisfait pas. Lors d’opérations arithmétiques, les logiques sont transformées en numériques avec la convention selon laquelle les FALSE sont transformés en 0 et les TRUE en 1.

Voyons cela sur un exemple. Nous créons un objet test qui est le vecteur de logiques (FALSE,FALSE,TRUE), puis nous calculons le produit suivant :

x <- c(-1,0,2)

test <- x>1

(1+x^2)\*(x>1)

# [1] 0 0 5

On peut aussi utiliser les fonctions all ou any . La fonction all renvoie TRUE si tous les éléments satisfont la condition et FALSE sinon. La fonction any renvoie TRUE dès que l’un des éléments satisfait la condition, FALSE sinon.

all(x>1)

# [1] FALSE

any(x>1)

# [1] TRUE

En résumé

Un vecteur permet de pouvoir stocker plusieurs éléments d’un même type. On peut ainsi avoir :

    Des vecteurs de numériques
    Des vecteurs de caractères
    Des vecteurs logiques

Il existe plusieurs façons de créer un vecteur, soit via l’opérateur :, soit via une fonction adéquate. Vous pouvez convertir un vecteur d’un type à un autre, en utilisant la fonction adéquate.

Dans le prochain chapitre, nous verrons un peu plus en détails un cas particulier de vecteur : les facteurs.
