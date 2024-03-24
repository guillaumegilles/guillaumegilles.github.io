---
id: 5lg6g70xnudmy8dp4lbxnfb
title: $PATH
desc: ''
updated: 1668437512007
created: 1668434073545
---

`$PATH` est une variable [[bash]] déféni par [[os.unix.sh.bash]] contenant les répertoires dans lesquels se trouvent les programmes exécutable d’un sytème Unix. Elle permet d’indiquer au système où chercher ces fichiers exécutable lorsqu’on entre une commande dans un terminal. 

### Lire la variable $PATH

```shell
$ echo "$PATH"
```

Si on souhaite une lecture plus lisible

```shell
$ echo "${PATH//:/$'\n'}"
```

### Ajouter un fichier dans la variable $PATH

On retrouve cette variable `$PATH` dans le fichier [[~/.profile|os.unix.filesystem.profile]]. On peut donc modifier cette variable en éditant ce fichier. Par exemple :

```shell
# Set PATH to also include ~/.emacs.d/bin
PATH=$PATH:~/.emacs.d/bin
```

> `PATH=$PATH` est la syntaxe pour ajouter le `$PATH` par défaut à la variable `PATH`.

> Dans la syntaxe ci-dessus, les deux-points `:`, permettent de séparer les répertoires à ajouter, un peu comme les virgules d’une phrases.


## Références

- https://www.cyberciti.biz/faq/how-to-add-to-bash-path-permanently-on-linux/
- https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path