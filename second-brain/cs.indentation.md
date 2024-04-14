---
id: sihvj6gkuln8e2xzg95b9rl
title: indentation
desc: ''
updated: 1689974745241
created: 1647855501491
---

L’indentation est utilisé dans deux objectifs :

### En language de balisage…

…comme HTML, l’indentation apporte une meilleure visibilité à la lecture du code par les développeurs.

```html
<!DOCTYPE html>
<html>
    <head>
        <p>Title</p>
    </head>
    <body>
        <p>Hello World!</p>
    </body>
</html>
```

### En language de progrmation…

…l’indentation, permet de séparer des blocs de code.

```python
x = int(input('Enter an integer: '))
if x % 2 == 0:
    print('')       # un premier bloc de code
    print('Even')   # il est exécuté si x % 2 == 0 retourne TRUE
else:  
    print('')       # deuxième bloc de code exécuté, seulement si
    print('Odd')    # x % 2 == 0 retourne FALSE
print('Done with conditional')
```
