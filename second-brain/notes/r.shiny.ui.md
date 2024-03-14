---
id: 0fohpe7797ye0g2qzbk2llm
title: shiny UI
desc: fonction pour initialiser une page web responsive
updated: 1682365430963
created: 1682363748418
---

le premier bloc dêune app shiny est d’initialiser la page web avec la fonction `fluidPage()`.

```r
ui <- fluidPage(
  "Hello, world!"
)
```

Les arguments de cette fonction permettent de configurer la page, en incluant des éléments d’ui, comme `selectInput`, ou `verbatimTextOutput`par exemple :

```r
ui <- fluidPage(
    selectInput("dataset", label = "Dataset", choices = ls("package:datasets")),
    verbatimTextOutput("summary"),
    tableOutput("table")
)
```

## les 3 types de fonctions dans l’ui

- `layout functions` : règle la structure visuelle de la page web ;
- `input controls` : contrôle les **inputs** disponibles pour l’utilisateur ;
- `output controls` : contrôle les **outputs** disponibles pour l’utilisateur.

Toutes ces fonctions sont des encapsulations de code [[html]], on peut le vérifier en tapant ces fonctions dans la console, le retour est le code `html`généré par la fonction.


## références

- @wickhamMasteringShinyBuild2021