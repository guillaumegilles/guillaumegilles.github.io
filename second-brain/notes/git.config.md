---
id: VHoehcal4ELrTaVik63IC
title: Git config
desc: Configuration initiale de Git
updated: 1709533099630
created: 1645476929584
---

### Saisir son nom et addresse email

C'est une étape préalable pour travailler avec [[git]] en local sur une machine car `git` utilise ces informations dans chaque commit.

```shell
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

### Définir le nom de la branche locale par défaut

Par défaut Git will créer une branche appelée, _master_. Depuis la version 2.28 de Git, on peut sélectionner le nom de la branche initiale avec la commande suivante :

```shell
$ git config --global init.defaultBranch main
```

### Consulter les paramètres de Git init

Pour vérifier les informations saisies on peut utiliser la ligne de commande suivante :

```shell
$ git config --list
```

##### Checking Your Settings

If you want to check your configuration settings, you can use the git config --list command to list all the settings Git can find at that point:

$ git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
...
You may see keys more than once, because Git reads the same key from different files ([path]/etc/gitconfig and ~/.gitconfig, for example). In this case, Git uses the last value for each unique key it sees.

You can also check what Git thinks a specific key’s value is by typing git config <key>:

$ git config user.name
John Doe

## Références

- [Getting Started - First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
