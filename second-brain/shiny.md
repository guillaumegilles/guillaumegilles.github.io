# Shiny

[Shiny](https://shiny.posit.co/) is a framework to build web app in [[r]] and
[[python]]. It possible to add [[css]] and [javascript]] elements to further
customize the layout.


- [Shiny for Python](https://shiny.rstudio.com/py/docs/overview.html)
- [Shinylive](https://shiny.posit.co/py/docs/shinylive.html)

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
