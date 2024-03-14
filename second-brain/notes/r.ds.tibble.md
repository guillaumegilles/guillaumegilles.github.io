---
id: nf6fk6t1bjaehba5xi3ckes
title: tibble
desc: les data frames du package dplyr
updated: 1683577599464
created: 1683575578145
---

Le [[r.package]] [[r.tidy.dplyr]] offre une nouvelle structure de données, le `tibble`. Un `tibble` se comporte presque comme un [[r.ds.data-frame]] à quelques exceptions :

- les lignes d’un `tibble` n’ont pas de nom ;
- la structure de données du `tibble` conservé lorsqu’on extrait une unique colonne.

Ces choix reposent sur trois idées principales :

1. les `tibbles` sont analogue à des tables dans une base de donées. Les lignes n’y ont pas de *nom* ;
2. une fcontion doit toujours retourner le même type d’objet (*structure de données*)
3. l’affichage ne doit pas être trop long, car on utilise de plus en plus de gros volume de données

## références

@hussonPourStatistiqueScience2018