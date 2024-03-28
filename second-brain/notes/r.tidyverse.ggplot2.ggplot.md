---
id: 5rom50yfsifaq39d69v1rxm
title: ggplot()
desc: ''
updated: 1684671386013
created: 1684156141528
---

Avec `ggplot` on commence un graphique avec la fonction `ggplot()`permettant de 
tracer un système de coordonnées dans lequel on peut ajouter des « couches », 
[[r.tidyverse.ggplot2.aes]], [[r.tidyverse.ggplot2.geom]], etc.

Le premier argument à spécifier est le jeu de données

```{r}
ggplot(data = mpg)
```

Une syntaxe plus appropriée au [[r.tidyverse]] est :

```{r}
mpg %>%
    ggplot()
```

## références

@DataScience2e