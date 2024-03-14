---
id: d3ovw0f6nw2aoexrdi2s201
title: Fusionner des branches avec Git
desc: ''
updated: 1645645060646
created: 1645644785557
---

Cette procédure est réalisée en trois étapes. La première, on se positionne sur la banche qui va recevoir la fusion grâce [[git.branch.checkout]].

```shell
git checkout nomDeLaBranche
```

La deuxième étape est de fusionner la branche désiré dans la branche dans laquelle on se trouve.

```shell
git merge nomDeLaBranche
```

Dernière étape *optionnelle* on peut supprimer la branche fusionnée, qui n'a plus d'utilité désormais, grâce à la commande :

```shell
git branch -d nomDeLaBranche
```
