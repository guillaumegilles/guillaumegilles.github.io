---
id: i6dxokh7y4by7t4zmrqgwv2
title: server
desc: le bloc backend d’une appli shiny
updated: 1682365000724
created: 1682364544963
---

La partie back-end est initialiser grâce la syntaxe suivante :

```r
server <- function(input, output, session) {

}
```

Des fonctions peuvent être ajoutées au server pour retourner le résultat de calcul r, comme `renderPrint()`, `renderTable`, etc.

```r
server <- function(input, output, session) {
    output$summary <- renderPrint({
        dataset <- get(input$dataset, "package:datasets")
        summary(dataset)
    })
    
    output$table <- renderTable({
        dataset <- get(input$dataset, "package:datasets")
        dataset
    })   
}
```

## références

  @wickhamMasteringShinyBuild2021