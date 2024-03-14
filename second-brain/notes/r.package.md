---
id: hc7mb1lhbon984hhkvxk3yp
title: package
desc: "gestion des packages de R"
updated: 1684441095943
created: 1671012845765
---

Un [package](https://www.rstudio.com/products/rpackages/) est un ensemble de 
programmes R qui permet d’augmenter les fonctionnalités de R. Un **package** est 
généralement dévolu à des méthodes particulières ou à un domaine d’applications.

## pour installer un package sur une machine

```r
install.package("tidyverse")  # pour installer le package tidyverse
```

## on peut vérifier si un package est installer

```r
packageVersion("tidyverse")
```

## charger le package dans un script r

```r
library(tidyverse)
```

## lister les packages installé sur la machine

```{r}
> installed.packages()
```

## Références

- https://posit.co/products/open-source/rpackages/