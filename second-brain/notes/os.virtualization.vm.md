---
id: 0r1qtgcj6a4tidkhiy5eqht
title: virtual machine
desc: Description des machines virtuelles
updated: 1680638319866
created: 1668267383535
---

La virtualisation du hardware permet de rendre le matériel informatique indépendant de ces composants informatique, grâce à une couche logicielle, **hypervisor**. L'hypervisor est un environnement étanche, de la machine sur lequel il est installé.

Les meilleurs exemples de la virtualization du hardware sont les ***Virtual Machine*, VM**. Les VM sont indépendante les unes des autres et elles ne peuvent pas s'influencer entre elles. L'hypervisor gère les ressources matérielles de chaque VM selon les besoins.

![Virtual Machine](assets/images/virtualization_stack_showing.jpg)

Les VM sont donc des machines virtuelles se compartant exactement de la même façon qu'une machine "physique" tant qu niveau hardware que software. Les VM, **guest** peuvent tourner sur une ou plusieurs machines physiques, les **hosts**. Du point de vue applications, elles se comportentes commme si elles étaient installées sur une véritable machine physique.

Malgrès les baisses de performances induite par la couche de *virtualization* de l'*hypervisor*, les avantages de VM sont nombreux :

1. Les applications et services des VM n’interfère pas entre elles
2. Indépendance complète entre le *guest* et le harware + OS du *host*
3. Les VM peuvent être dupliquer simplement en les copiant
4. Les ressources hardawre sont alloués dynamiquement par l'*hypervisor*
5. Meilleure utilisation des ressources hardaware d'une machine
6. Une gestion simplifié des environnements virtuels

---

## Références

- https://academy.hackthebox.com/module/87/section/881
- https://en.wikipedia.org/wiki/Hypervisor