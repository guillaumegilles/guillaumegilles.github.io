---
id: 4t6gnog0jcidyuakuv4l33h
title: read.table()
desc: créer un data frame depuis un fichier contenant une matrice de données
updated: 1684330627858
created: 1683148602864
---

## syntaxe

Un fichier contenant [[une matrice de données|ds.data.import]] peut-être importé dans une session `R` grâce à la fonction `read.table()`

```r
> tablo <- read.table("file",
                        sep = ";",
                        header = TRUE,
                        dec = ",",
                        row.names = 1,
                        na.string = ".")
```

L’[[r.object]] créé, dans ce cas, `tablo` est donc un [[r.ds.data-frame]]. On peut le vérifier avec la fonction grâce à la fonction [[r.base.mode]].

Les [[r.dt]] des variables sont *devinés* ma fonction d’importation, il est conseillé de vérifier les type de données des varaibles avec la fonction [[r.base.summary]].

## arguments
- `"file"` : le fichier à importer :
  - on peut utiliser un [[os.absolute-path]] : `"~/Dropbox/dendron-pkm/notes/assets/file.csv"` ;
  - un [[chemin est relatif|os.relative-path]] à la session R en cours : `"./assets/file.csv"` ;
  - une [[url]] : `"https://r-stat-sc-donnees.github.io/decathlon.csv"` ;
- `sep = ";"` : indique le caractère qui sépare les colonnes, ici `;`. Pour un espace, on indique `" "` et une tabulation `"\t"` ;
- `header = TRUE` : indique si oui ou non, la première ligne contient les noms des colonnes ;
- `dec = ","` : spécifie le caractère utilisé pour la décimale ; 
- `row.names = 1` : indique que la colonne `1` dans ce cas n’est pas une variable mais l’identifiant des individus, cf. lignes ;
- `na.string = "."` : indique le caractère utilisé pour les valeurs manquantes du jeu de données