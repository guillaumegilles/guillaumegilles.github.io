---
id: 4ia1bvc0cq3tpm16sacv2eg
title: shiny
desc: les bases d’une application shiny
updated: 1704147347919
created: 1680277162438
---

- [Mastering Shiny](https://mastering-shiny.org/index.html)
- [Shiny for Python](https://shiny.rstudio.com/py/docs/overview.html)

Shiny est un package de R pour construire des applications interactives. Il est tout à fait possible des éléments intéractif dans un document `html`. Les briques web, tels que `CSS`et  `JavaScript` peuvent être incorporé dans les app shiny pour encore plus de dynamisme.

Pour utiliser le package, [[il suffit de le charger|r.package]].

une app shiny se compose de 2 éléments fondamentaux :

1. une partie [[UI|r.shiny.ui]] pour le _frontend_ ;
2. et une partie _backend_, le [[server|r.shiny.server]]
3. pour finir, le script doit inclure la fonction `shinyApp(ui, server)` afin de combiner les 2 briques `ui` + `server`.

## runApp()

pour lancer l’application shiny, on utilise la fonction `runApp()`.

```r
shiny::runApp()
```

L’app se lance sur l’url : http://127.0.0.1:2827

- `http://127.0.0.1` est l’url IPv4 par défaut pour faire tourner l’app ;
- `3827` est un port aléatoire.

Pour arrêter l’app, on utilise le raccourci `Ctrl + c`.

## Référence

@wickhamMasteringShinyBuild2021
