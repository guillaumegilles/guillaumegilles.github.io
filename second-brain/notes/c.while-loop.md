---
id: v4vesxqlvugx6nprtzqwir2
title: while loop
desc: ''
updated: 1697431366936
created: 1651607994315
---

Pour générer une boucle ´while´ avec `C`, la syntaxe est la suivante :
```c
while (true)
{
    printf("meow\n");
}
```

Si on souhaite créer une boucle de 3, une solution simple est :
```c
int counter = 0;
while (counter < 3)
{
    printf("meow\n");
    counter += 1;
}
```