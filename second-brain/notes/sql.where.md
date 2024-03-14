---
id: 8pqdvhe2bc9ub5cw53to7fx
title: Where
desc: Filtrer des requêtes SQL
updated: 1655126747197
created: 1655108851496
---

On peut filtrer des requêtes SQL avec le mot-clé `WHERE` 

```sql
SELECT *
FROM students
WHERE major = 'Biology';
```

Cette requête permet de sélectionner toutes les colonnes de la table `students` en filtrant ceux qui ont choisi `Biology` pour matière principale.

> la syntexte des textes doit être accompagné di ' ' comme 'Biologie' Pour les valeurs numériques ce n’est pas nécessaire

```sql
SELECT *
FROM students
WHERE year = 1;
```

