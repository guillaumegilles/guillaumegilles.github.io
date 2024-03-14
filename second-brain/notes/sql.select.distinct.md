---
id: 4iaw1k386uyakb3bz8dd4ky
title: Distinct
desc: Éviter les doublons dans une requête SQL
updated: 1655066713855
created: 1655066498993
---

Lorsqu’on [[sélectionne|sql.select]] une colonne, la requête renvoie tous les éléments, y compris les doublons. Pour éviter ça on peut utiliser le mot-clé `DISTINCT` :

```sql
SELECT DISTINCT country
FROM subscribers;
```