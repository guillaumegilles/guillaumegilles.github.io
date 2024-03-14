---
id: 38043e0mcmmrmlhkfhs7il1
title: geom()
desc: ''
updated: 1684176898140
created: 1684156573712
---

La fonction `geom()` ajoute une *couche* pour représenter graphiquement les 
données. Il existe différentes fonction, selon le type de variables.

```{r}
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))
```

## 1 varaible quantitative

- `geom_area()`
- `geom_density()`
- `geom_dotplot()`
- `geom_freqpoly()`
- `geom_histogram()`
- `geom_qq()`
  
## 1 variable qualitative

- `geom_bar()`
  
## 2 variables quantitatives

- `geom_point()` pour créer un nuage de points
- `geom_quantile()`
- `geom_rug()`
- `geom_smooth()`
  
## 2 variables, l’une qualitative, l’autre quantitative

- `geom_col()`
- `geom_boxplot()`
- `geom_dotplot()`
- `geom_violon()`

## 2 variables qualitatives

- `geom_count()`
- `geom_jitter()`