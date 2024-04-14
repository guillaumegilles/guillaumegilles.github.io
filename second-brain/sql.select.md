---
id: a26cdl3mu0cg9u8gyn669rt
title: Select
desc: Selectionner des éléments d’une table dans une requête SQL
updated: 1655325282913
created: 1655063308219
---

Pour sélectionner des éléments dans une table SQL, la syntaxe est simple :

```sql
SELECT name 
FROM users;
```

- *SELECT* est le mot-clé utilisé pour déterminer la colonne qu’on souhaite consulter dans la table ;
- *FROM* est la table dans laquelle on fait la requête.

Cette requête permet de sélectionner la colonne des noms (*name*) dans la table *users*.

> Les **mots-clés du langage SQL s’écrivent en capitale** pour être plus lisible.

> À la fin d’une ligne, le point-virgule `;` n’est pas obligatoire, mais il s’agit d’**une bonne pratique qu’on doit suivre**.

## Sélectionner plusieurs éléments

Pour séléctionner plusieurs éléments d’une table, on utilise la virgule `,` comme séparateur :

```sql
SELECT name, email
FROM users;
```

## Sélectionner toute une table

Pour sélectioner toutes les colonnes d’une table, il est fastidieux de les lister les une à la suite des autres avec des `,`. Une manière plus simple est d’utiliser l’astérix `*`

```sql
SELECT *
FROM stock;
```

