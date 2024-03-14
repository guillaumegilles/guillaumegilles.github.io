---
id: 7n6qjjltbhexg6qzz35tntr
title: Open
desc: Lire et écrire du texte avec Python
updated: 1653662668370
created: 1653643997743
---

Pour lire et/ou écrire du texte avec Python, on peut utiliser la fonction `open()`

```python
# Read the entire file as a single string
with open ('somefile.txt', 'rt') as f:
    data = f.read()
```

@beazley_python_2013, p. 141