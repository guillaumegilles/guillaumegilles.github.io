---
id: hfs7t1e24xnnffiq18ma7cb
title: del()
desc: ''
updated: 1648248722206
created: 1648248722206
---

La fonction `del()` permet de supprimer un objet, une données.

## Listes

Elle est utile, lorsqu’on [[manipule|py.dt.list.manipulation]] des listes pour supprimer des élémets de cette liste. Attention

```python
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
```

SiIl est recomandé de

del(areas[10]); del(areas[11])

del(areas[-4:-2])
