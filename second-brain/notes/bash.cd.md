---
id: kyy1r9422nrpwugfqvhvfz4
title: cd
desc: Se déplacer dans l'arborescence grâce au terminal
updated: 1671102109573
created: 1668162223585
---

La commande `cd` signifie **c**hange **d**irectory, elle permet de se " déplacer " dans l'arborescence de dossiers d'un système. Les déplacements se font à l'aide des [[os.absolute-path]] ou des [[os.relative-path]].

```shell
$ cd /home/guillaume
```

Cette commande permet d'accéder au répertoire `/guillaume` situé dans le `/home`. Par faciliter la navigation dans les différents répertoire, il exsite plusieurs raccourcis.

### Accéder au répertoire parent

```shell
$ cd ..
```

Ce raccourci, `..`, permet de remonter d'un cran dans l'arborescence, au répertoire parent dans lequel on se trouve.

```shell
$ cd /home/guillaume
$ cd ../..
```

Avec cette commande, je me positionne dans un premier temps dans le répertoire `/home/guillaume`, puis la deuxième commande remonte d'un cran à `/home` puis d'un deuxième à `/`.

### Accéder au *root*

```shell
$ cd /
```

Le raccourcis *slash*, `/`, permet d'accéder directement au répertoire *root*.

### Accéder au *home*

```shell
$ cd ~
```

Ce raccourci, `~` permet d'aller directement dans le répertoire *home*.

### Faire référence au répertoire actuel

```shell
$ cd .
```

`.` permet de faire référence au répertoire dans lequel on se trouve. Dans cet exemple, l'éxécution de la commande, on se retrouve dans le même répertoire, on a finalement pas « bouger ».

## Références

- https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal
- https://www.youtube.com/watch?v=kjUQ2c9AFLw&list=PLDKPqJOyp99TvAvB27Z8bzrkuSBrGPY9X&index=3