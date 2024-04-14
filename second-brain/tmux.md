---
id: 5ofrkszore30cppyh41cszn
title: Tmux
desc: ""
updated: 1697917359238
created: 1697917016628
---

## Installation

[Github repo](https://github.com/tmux/tmux)

```shell
$ brew install tmux
```

## Les raccourcis claviers

Dans tmux Prefix, par défaut : `Ctrl + b`

## Session

### Créer une nouvelle session

```bash
$ tmux new -s session-name
```

### Liste des sessions actives

```shell
$ tmux ls
```

Ou, dans une session :

```shell
<prefix> spa
```

### Rejoindre une session existante

```shell
$ tmux attach -t session-name
```

### Détacher une session

```shell
$ tmux detach
```

## Window

### Nouvelle fenêtre

```shell
<prefix> c
```

### Fenêtre suivante

```shell
<prefix> n
```

### Fenêtre précédente

      ``` shell
      <prefix> p
      ```
    - ### Lister toutes les fenêtres

      ``` shell
      <prefix> w
      ```
    - ### Renommer une fenêtre

      ``` shell
      <prefix> ,
      ```
    - ### Trouver une fenêtre

      ``` shell
      <prefix> f
      ```
    - ### Tuer une fenêtre

      ``` shell
      <prefix> &
      ```

- ## Terminer (_pane_)
  - ### Division verticale

    ```shell
    <prefix> %
    ```

  - ### Division horizontale

    ```shell
    <prefix> “
    ```

  - ### Supprimer une division

    ```shell
    exit
    ```

    Ou

    ```shell
    <prefix> x
    ```
- ## Configuration

  Le fichier de configuration de Tmux se trouve `~/.tmux.conf`
