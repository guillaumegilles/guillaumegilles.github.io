---
id: j62uztgbxsypgx3isx81nm6
title: ggplot2
desc: ''
updated: 1684176948071
created: 1683145576885
---

## 

Le package `ggplot2` est inclu dans [[r.tidyverse]] et il remplace la fonction basique 
`plot()`de `R` dans la plupart des situations.

La syntaxe de `ggplot2` repose sur les éléments développés par *Leland Wilkinson* 
dans son livre [The Grammar of Graphics](https://link.springer.com/book/10.1007/0-387-28695-0). 
Le principe consiste à décomposer un graphique en couches :
1. Une couche pour le jeu de donnée, gâce à la fonction [[r.tidyverse.ggplot2.ggplot]] +
2. une couche pour le type de graphique qu’on souhaite, histograme, camambert, etc. : [[r.tidyverse.ggplot2.geom]] +
3. Une autre couche pour la ou les variable(s) à reprenter : [[r.tidyverse.ggplot2.aes]].


## modèle graphique

On utilise une recette simple pour construire des graphiques avec les *couches* 
`ggplot` nécessaire :

```{r}
ggplot(data = <DATA>) + 
  <GEOM_FUNCTION>(mapping = aes(<MAPPINGS>))
```

## références 

- https://ggplot2.tidyverse.org/
- @DataScience2e
- @hussonPourStatistiqueScience2018