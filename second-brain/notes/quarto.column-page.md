---
id: l83m6eg6d8yyzru6b4um4gl
title: "Utiliser toute la largeur de la page web"
desc: ""
updated: 1704127685625
created: 1704122489553
---

## Page Column

If you need even more space for your content, you can use the `.column-page` class to make the content much wider, though stopping short of extending across the whole document[^1]. For example, to create a wider image, you could use:

[1]: https://quarto.org/docs/authoring/article-layout.html#page-column

```dot
:::{.column-page}
![](images/elephant.jpg)
:::
```

For computational output, you can specify the page column in your code cell options. For example:

```r
#| column: page

knitr::kable(
  mtcars[1:6, 1:10]
)
```

## Screen Inset

If you’d like a full width appearance, but would like to retain a margin, you can use inset or inset-shaded modifiers on the column. For example[^2]:

[2]: https://quarto.org/docs/authoring/article-layout.html#screen-inset

```dot
::: {.column-screen-inset}
![A full screen image](/image.png)
:::
```

The inset-shaded modifier results in a block spanning the full width but wrapped with a lightly shaded background. For example:

```{r}
#| column: screen-inset-shaded

library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
```