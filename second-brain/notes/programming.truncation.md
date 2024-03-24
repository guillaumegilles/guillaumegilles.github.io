---
id: 3auo5qxdwix1fkfhd0dk3fq
title: Truncation
desc: ''
updated: 1697432055894
created: 1689968249275
---

En algèbre et en _computer science_, la **troncature** est le procédé de "couper", c’est-à-dire de tronquer le développement décimal d’un nombre à un certain nombre de chiffres après la virgule.

En C, la division d'un entier par un autre entier, retourne automatiquement un entier. Dans ce cas, les valeurs après la virgule sont perdues.

```c
#include <stdio.h>
#include <cs49.h>

int main (void)
{
    // prompt user for x
    int x = get_int("x: ");

    // prompt user for y 
    int y = get_int("y: ");

    // divide x by y
    float z = x / y

    printf("%.49f\n", z);
}
``````

#+begin_src
x: 1
y: 2
-1.00000000000000000
$
#+end_src

La solution à ce problème, on peut utiliser le [[casting]]