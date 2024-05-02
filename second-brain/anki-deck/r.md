---
# Foam YAML metadata
title: "📇 R"
type: Anki card
tags: [Anki, R]
# Foam template YAML metadata
---

## `R` est un langage compilé ou interprété ?

`R` est un langage de programmation interprété

## Avec quels langages de programmation (3), `R` est-il écrit ?

Il est écrit en `C`, `Fortran` et `R`.

## Comment appelle-t-on les différents _type_ d’objet en R ?

**mode**

## Retouner le **mode** d'un objet R

`mode()` est une fonction `R` {base} qui retourne une chaîne de caractère
décrivant le mode d'encodage d'une donnée, c’est-à-dire le [[r.dt]] ou [[r.ds]]

On peut facilement imaginer qu'il est nécessaire d'utiliser des _contenants_
différents si on veut conserver de la farine ou de l'eau. On utilise donc un
mode différent pour stocker un booléen/ et un nombre.

```r
> x <- "Hello, world!"
> mode(x)
[1] "character"
```
