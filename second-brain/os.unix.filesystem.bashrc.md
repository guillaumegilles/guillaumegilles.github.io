---
id: r8f6db8pd7a6i1cf0hhrytv
title: ~/.bashrc
desc: Qu’est-ce que le fichier ~/.bashrc
updated: 1669048390340
created: 1668372941770
---

Le fichier `~/.bashrc` est un script exécuté à l’ouverture de session d’un utilisateur. Il contient la configuration du terminal permettant de modifier les caractères, les couleurs, l’historique du shell, les alias, etc.

### Modifier le prompt

Pour modifier l’affichage du [[sh.prompt]], on peut modifier la variable `PS1` du fichier `~/.bashrc` en utilisant les caractères [[cs.nw.communication.ascii]] et des [caractères spéciaux](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Controlling-the-Prompt) :

```bash
PS1="\[\033[1;32m\]\342\224\200\$[\[\033[1;37m\]\u\[\033[01;32m\]@\[\033[01;34m\]\h\[\033[1;32m\]]\342\224\200[\[\033[1;37m\]\w\[\033[1;32m\]]\n\[\033[1;32m\]\342\224\224\342\224\200\342\224\200\342\225\274 [\[\e[01;33m\]$(date +%D-%r)\[\e[01;32m\]]\\$ \[\e[0m\]"
```

- `\[`…`\]` permet de saisir des caractères non « imprimables » ;
- `\033[1;32m` est la séquence pour modifier la couleur ;
- `$(date +%D-%r)` est la séquence pour afficher la date.

Après la modification, il ne reste plus qu’à « rafraichir » le fichier `~/.bashrc` avec la commande [[sh.source]].

## Références

-  https://www.digitalocean.com/community/tutorials/bashrc-file-in-linux
-  https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Controlling-the-Prompt