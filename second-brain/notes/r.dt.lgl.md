---
id: cejp9jqexeq4kkokldu3u2k
title: logical
desc: "les booléens, TRUE ou FALSE"
updated: 1684257493448
created: 1684234604996
---

les booléens. `TRUE`ou `FALSE` sont des types de données *logical*, abbréviées 
`lgl`.

```{r}
> x <- TRUE
> mode(x)
[1] "logical"
```

On peut tester l’appartenance au [[mode|r.dt]] `logical` grâce à la fonction 
[[r.base.is-logical]]


```{r}
> is.logical(x)
[1] FALSE
```

## références

@hussonPourStatistiqueScience2018