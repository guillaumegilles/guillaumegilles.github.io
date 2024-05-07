---
# Foam YAML metadata
title: "📇 R"
type: Anki card
tags: [Anki, R]
# Foam template YAML metadata
---

## `R` est un langage compilé ou interprété ?

`R` est un langage de programmation interprété

## Avec quels langages de programmation, `R` est-il écrit (3) ?

Il est écrit en `C`, `Fortran` et `R`.

## Comment appelle-t-on les différents _type_ d’objet en R ?

**mode**

## Retouner le **mode** d'un objet R

`mode()` est une fonction `R` {base} qui retourne une chaîne de caractère
décrivant le mode d'encodage d'une donnée.

On peut facilement imaginer qu'il est nécessaire d'utiliser des _contenants_
différents si on veut conserver de la farine ou de l'eau. On utilise donc un
mode différent pour stocker un booléen et un nombre.

```r
> x <- "Hello, world!"
> mode(x)
[1] "character"
```

## Retourne le répertoire dans lequel la session `R` est exécutée

```r
> getwd()
```

## Modifier le répertoire de travail avec `R`

```r
> setwd("/home/skekcoon/r_projects")
```

## Sauvegarder une image, `.RData`, contenant les objets d’une session R

```r
> save.image()
```

## Charger une image, `.RDtata` de session R précédemment sauvegarder

```r
> load()
```

## Qu’elle est la fonction de R pour afficher l’aide ?

```r
> help(mean)
> ?mean
```

`?` est un alias de la fonction `help()`. Les résultats de ces deux lignes de R
sont identiques.

## Quel est l’opérateur en `R` pour créer un objet

```r
# Good
x <- 5

# Bad
x = 5
```

On peut également utilisé `->` ou `=`, mais `<-` est l’opérateur à privilégier.

## Insérer un commentaires dans un script `R`

```r
# this is a comment in R
```

Tout ce qui se trouve après le symbole `#` n’est pas interprété par `R`.

## Afficher la valeur d’un objet `R`

```r
> print(x)
[1] 5
```

Ou plus simplement :

```r
> x
[1] 5
```

## Lister les objects d’une session `R`.

```r
> objects()
```

Ou simplement, avec la fonction `ls()` :

```r
> ls()
```

La syntaxe de la fonction `ls()` est similaire à la commande `ls` de bash.

## Supprimer un objet d’une session `R`

```r
> rm(x)
```

Comme avec la fonction `ls()`, On retrouve la même similitude entre la fonction
`rm()` et la commande bash `rm`.

Pour supprimer plusieurs objets, ils sont passés en arguments les uns à la suite
des autres et séparés par des virgules.

```r
rm(x, y, data)
```
