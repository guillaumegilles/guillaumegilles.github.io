---
id: 7nqyfcgf3qmz7da2ehh4ky1
title: R Markdown
desc: blabla.Rmd
updated: 1684739212552
created: 1670533091025
---

**R Markdown** est un format de fichier, `.rmd` qui permettant d’écrire le code `R` avec les bénéfices de la mise en page du [[markdown]]. Le résultat apporte un travail **reproductible** en combinant bloc de code `R`, l’exécution et les résultats avec les commentaires dans un seul document.

### Les blocs de coder

Pour créer un bloc de code en **R Markdown** on utilise la syntaxe **Markdown** en ajoutant `{r}` après les 3 accents graves.

Ce `{r}` peut contenir des options utiles pour la présentation du code :

- `echo = TRUE` : display code in output document ;
- `error = FALSE` : stop render when error occurs ;
- `eval = TRUE` : run code in chunk ;
- `include = TRUE` : include chunk in doc after running ;

#### Définir des options pour tout le document

Dans le premier bloc de code, souvent après l’en-tête en YAML, on peut définir des options qui s’appliqueront à l’ensemble du document.

```{r include=FALSE}
knitr::opts_chunk$set(message = FALSE)
```

#### Insérer du code dans le texte

On peut également insérer des bouts de code, sans utiliser des blocs de code, dans le texte `r <code>`. Le code est évaluer et le résultat apparaît en texte.

« Built with `r getRversion()` » --> "Built with 4.1.0"

### Autres avantages

En plus de cet avantage, on peut compiler le fichier R Markdown vers différents format d’output, [[html]], PDF, [reveal.js](https://bookdown.org/yihui/rmarkdown/revealjs.html), beamer, etc.

Ce fichier **R Markown** contient un en-tête en YAML contenant des métadonnées, dont le titre du fichier, le format de sortie, etc.

### Les raccourcis clavier :

- `Ctrl` + `Alt` + `i` : insère un bloc de code
- `Ctrl` + `Shift` + `k` : génère le fichier de sortie déféni dans les métadonnées YAML

https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf

## Références

- https://r-stat-sc-donnees.github.io/
- https://rmarkdown.rstudio.com/

