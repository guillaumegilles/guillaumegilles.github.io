# Shiny server

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
