---
id: bs98nac4jwaj2lw4jnuwndr
title: Do While Loop
desc: ''
updated: 1651608127480
created: 1651607718366
---

Une boucle `do while` avec `C` est similaire à une boucle [[c.while-loop]] **mais** les conditions sont vérifiées en dernier, plutôt qu’au début avec la boucle while.

```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Width: ");
    }
    while (n < 1)

    for (int i = 0; i < n; i++)
    {
        printf("?");
    }
    printf("\n");
}
```