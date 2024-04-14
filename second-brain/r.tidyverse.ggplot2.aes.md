---
id: 0lyisfv28n4mdfzh1v51quq
title: aes()
desc: ''
updated: 1684176875158
created: 1684156474147
---

Chaque focntion `geom()` prend un argument `mapping` sous la forme de la fonction 
`aes()`, *aesthetics* pour représenter les varaibles. Les paramètres de la fonction 
servent à configurer les formes, la taille, etc.

```{r}
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))
```

## références

- @hussonPourStatistiqueScience2018
- @DataScience2e



Each geom function in ggplot2 takes a mapping argument. This defines how variables in your dataset are mapped to visual properties. The mapping argument is always paired with aes(), and the x and y arguments of aes() specify which variables to map to the x and y axes. ggplot2 looks for the mapped variables in the data argument, in this case, mpg.