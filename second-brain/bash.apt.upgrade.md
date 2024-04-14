---
id: 34rik2hhv1xsu00t02m1o9l
title: upgrade
desc: ''
updated: 1670196428858
created: 1670194201844
---

Cette commande permet de mettre à jour les *packages* installés localement. Elle se lance souvent après un [[bash.apt.update]]

```shell
$ apt upgrade
```

Puisque ces deux commande `apt update` et `apt upgrade` sont complémentaires, on peut les lancer simultanéement.

```shell
$ apt update && apt upgrade
```