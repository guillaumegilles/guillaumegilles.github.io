---
id: fzc34uepjaxwppm7nvugras
title: Container
desc: ''
updated: 1668269359448
created: 1668269345424
---

Un *container* est un ensemble de processus tournant sur une seule machine *host* comprennant une application complète, avec sa configuration et ses dépendances. Cette application est "enpaquetée" dans un format réutilisable. À l'inverse d'une [[cs.infosec.virtualization.vm]], un *container* ne possède pas d'[[os]] et de [[kernel]]. Les *containers* sont des *virtualization* d'application.

### Principales différences entre *container* et *VM*

| Virtual Machine | Container |
|:------:|:-----:|
|Contain applications and the complete operating system | Contain applications and only the necessary operating system components such as libraries and binaries|
| A hypervisor such as VMware ESXi provides virtualization | The operating system with the container engine provides its own virtualization |
| Multiple VMs run in isolation from each other on a physical server | Several containers run isolated from each other on one operating system |


## Références

- https://academy.hackthebox.com/module/87/section/882