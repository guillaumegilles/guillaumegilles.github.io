---
id: k8mvaqj92m50kiie2vdof6l
title: CAH
desc: Classification Ascendante Hiérarchique
updated: 1697485987093
created: 1697485925039
---

```r
medical %>%
  hclust(method = "single")
```

```r
donM <- dist(don)
chaS <- hclust(donM,method = "single")
chaW <- hclust(donM,method = "ward.D2")
chaM <- hclust(donM,method = "complete")
chaA <- hclust(donM,method = "average")
plot(as.dendrogram(chaS))
plot(sort(chaS$height,dec=T)[1:30],type="h")
abline(h=1.2)
don$single <- cutree(chaS,h=1.2)
plot(sort(chaW$height,dec=T)[1:20],type="h")
don$ward <- cutree(chaW,k=6)
plot(sort(chaM$height,dec=T)[1:20],type="h")
don$compl <- cutree(chaM,k=6)
plot(sort(chaA$height,dec=T)[1:30],type="h")
abline(h=3.5)
don$ave <- cutree(chaA,h=3.5)
```