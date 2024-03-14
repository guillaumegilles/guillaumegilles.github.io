---
id: onp7payt72bcmuzwlg10666
title: Dbscan
desc: ''
updated: 1697486300220
created: 1697486292430
---

```{r}
# donAL <- pivot_longer(don,cols=c("single","ward","compl","ave"),
#                       names_to = "indice")
# 
# ggplot(donAL,aes(x=V1,y=V2,col=as.factor(value)))+
#   geom_point()+facet_grid(rows = vars(indice))
# 
# 
# library(dbscan)
# kNNdistplot(don[,1:2],k=3)
# abline(h=0.21)
# tmpdb <- dbscan(don[,1:2],eps=0.21)
# names(tmpdb)
# table(tmpdb$cluster)
# ggplot(don,aes(x=V1,y=V2))+
#   geom_point(color=ifelse(tmpdb$cluster==0,"pink",
#                           as.factor(tmpdb$cluster)))
```