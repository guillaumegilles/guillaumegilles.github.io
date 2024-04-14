---
id: odv1wgmwh8vwnyf8tayqhrc
title: git remote
desc: ''
updated: 1700427364270
created: 1645645154537
---

## Adding a remote repository

To add a new remote, use the `git remote add` command on the terminal, in the directory your repository is stored at. The git remote add command takes two arguments:

1. A remote name, for example, origin
2. A remote URL, for example, https://github.com/OWNER/REPOSITORY.git

For example:

```shell
$ git remote add origin https://github.com/OWNER/REPOSITORY.git
# Set a new remote

$ git remote -v
# Verify new remote
> origin  https://github.com/OWNER/REPOSITORY.git (fetch)
> origin  https://github.com/OWNER/REPOSITORY.git (push)
```

https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories

On peut parfois vouloir [[git.remote.remove]].

## Les status du dépot distant

On peut vérifier les _ponts_ existants pour un répertoire local en utilisant la commande :

```shell
git remote
```

Pour **vérifier les adresses URL** des _ponts_, on peut ajouter le tag `-v` dans la ligne de commande :

```shell
git remote -v
```

## Changer l'URL d'un remote Git repository

Lorsqu'on créé un pont entre un répertoire local et un dépôt local, on doit assigner l'adresse URL de ce dépôt distant. On peut modifier cette adresse URL, grâce à la ligne de commande :

```shell
git remote set-url origin https://github.com/guillaumegilles/nouvelle-url
```
