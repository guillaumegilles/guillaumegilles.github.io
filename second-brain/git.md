---
id: 5Ax3lCkb2jvrPjs7ZRu7n
title: Git
desc: Une présentation de Git
updated: 1709533243214
created: 1645474431427
---

## Outil de gestion de versions centralisés

[Git](https://git-scm.com/) est un outil de _versioning_, c'est-à-dire qu'il permet d'enregistrer les différentes versions d'un projet au fil de son existence. C'est un logiciel de _gestion de versions centralisé_. En anglais, on appelle cet outil un **V**ersion **C**ontrol **S**ystrem (VCS). Cet outil est très pratique pour collaborer sur un projet, car il permet de centralier les fichiers sur un serveur et de créer un copie locale sur chaque machine travaillant sur le projet. Dès qu'un changement est validé dans le répertoire source du serveur, ce changement est envoyé à tous les fichiers locaux des autres machines.

1. **Déclarer son identité:**

   La première chose à faire est configurer son identité, grâce à la [[bash]]
   [[git.config]].

2. **Initialiser un répertoire locale:**

   Après avoir configurer Git, on doit initialiser un répertoire, en locale, sur
   notre machine afin de travailler avec Git: [[git.init]]

### comment annuler l’initialisation d'un répertoire

Pour annuler un répertoire initialiser avec Git, on supprime le fichier `.git` à la racine du répertoire, grâce à la commande [[bash#rm-remove]].

```shell
$ rm -rf .git
```

## 3. `git add`

Avant un `commit` on doit sélectionner les fichiers locaux à indexer grâce à la ligne de commande `git add` :

```shell
git add filename.bla
```

### Comment indexer tous les fichiers créés et modifiés

On peut indexer tous les fichiers créés et modifiés, simplement, grâce à la commande :

```shell
$ git add .
```

### Indexer tous les fichiers d’un dossier

Pour ce faire, on se positionne sur le dossier en question dans le shell, et on saisit la commande :

```shell
$ git add * --v
```

`-v` ou `--verbose` permet de lister tous les fichiers ajoutés à l’index

## 4. `git commit`

L'enregistrement se déroule en deux étapes. La première est de [[git#3-git-add]]. La deuxième étape, on **commit** ces fichiers grâce à la ligne de commande :

```shell
$ git commit -m "texte de commantaire"
```

L'option `-m "commentaire"` permet d'ajouter un commentaire au commit pour lui donner plus d'explication et facilliter la compréhension par les autres contributeurs.

- # Getting a Git Repository

  You typically obtain a Git repository in one of two ways:

  You can take a local directory that is currently not under version control, and turn it into a Git repository, or

  You can clone an existing Git repository from elsewhere.

  In either case, you end up with a Git repository on your local machine, ready for work.

  2. A distance :
  1. [[git.remote]] ;
     1. [[git.pull]]
     2. [[git.push]]

  …or create a new repository on the command line

  ```shell
  echo "# s3-e20-predict-co2-emissions-in-rwanda" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin git@github.com:guillaumegilles/s3-e20-predict-co2-emissions-in-rwanda.git
  git push -u origin main
  ```

  …or push an existing repository from the command line

  ```shell
  git remote add origin git@github.com:guillaumegilles/s3-e20-predict-co2-emissions-in-rwanda.git
  git branch -M main
  git push -u origin main
  ```

- ## Références
- https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

### Initialiser le répertoire locale

##### Getting a Git Repository

You typically obtain a Git repository in one of two ways:

You can take a local directory that is currently not under version control, and turn it into a Git repository, or

You can clone an existing Git repository from elsewhere.

In either case, you end up with a Git repository on your local machine, ready for work.

1. En local :
   1. [[git.init]] ;
   2. [[git.add]] ;
   3. [[git.commit]]
2. A distance :
   1. [[git.remote]] ;
      1. [[git.pull]]
      2. [[git.push]]

---

## Références

- https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

---
