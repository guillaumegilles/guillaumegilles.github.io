---
id: dYXeOxFn6K1TdSZTxB3ks
title: Branch
desc: ''
updated: 1645819956553
created: 1645568632495
---

## Qu'est-ce qu'une branches dans Git

Une branche est une copie du répertoire distant. On peut travailler en toute sérénité sur la copie locale. Pour créer une branche locale on utilise la ligne de commande :

```shell
git branch nomDeLaBranche
```

> La ligne de commande `git branch` permet de lister toutes les branches d'un projet.

## Renommer une branche

Il est possible de renommer, facilement, une branche, grâce à la ligne de commande :

```shell
git branch -m <oldname> <newname>
```

Si on se trouve déjà sur la branche à renommer, on peut utiliser la commande :

```shell
git branch -m <newname>
```
