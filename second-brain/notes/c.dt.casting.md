---
id: xap3q224tlq9c9abcsj8kqy
title: casting en C
desc: ''
updated: 1680468843629
created: 1680261363698
---

:PROPERTIES:
:ID:       ac2a3e99-e25b-4b0c-b1d7-baeb28e0fafb
:END:
#+title: c casting

---
id: 4gmu0coau2r79vrc5cbtrwr
title: Casting
desc: ''
updated: 1651607667141
created: 1651607278200
---

Avec le *Casting*, ou *type conversion* on **force** la conversion d’un [[cs.data-type]] dans une autre type particulier. Dans l’exemple, on convertie un entier `int x = get_int("x: ");` en float `(float) x` :

```c
#include <stdio.h>
#include <cs50.h>

int main (void)
{
    // prompt user for x
    int x = get_int("x: ");

    // prompt user for y
    int y = get_int("y: ");

    // divide x by y
    float z = (float) x / (float) y

    printf("%.50f\n", z);
}
```
