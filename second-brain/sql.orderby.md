---
id: cayumdzuh2tcgzdbl53wzz5
title: Order by
desc: Arranger les requêtes SQL
updated: 1655405696216
created: 1655066729914
---

On peut classer les éléments d’une requête en fonction d’une colonne avec le mot-clé `ORDER BY`

```sql
SELECT *
FROM patients
ORDER BY name;
```

Si on désire que les résultats de la requête soient arrangés par ordre ascendant ou descendant, on peut utiliser les mots-clés `ASC` ou `DESC` respectivement :

```sql
SELECT *
FROM patients
ORDER BY name ASC;
```

> Par défaut, SQL utilise l’ordre ascendant, `ASC` pour arranger les requêtes.

Pour les arranger par ordre descendant :

```sql
SELECT *
FROM patients
ORDER BY name DESC;
```
