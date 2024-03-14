---
id: hjh1n4mv49k837lmm6oxx5x
title: ~/.profile
desc: À quoi sert le fichier ~/.profile
updated: 1668437269524
created: 1668436221485
---

Traditionnellement, lorsqu’on se connecte à une session Unix, le système charge un seul programme, le [[os.unix.shell]]. Le shell par défaut, le **Bourne shell** lit les commandes à partir du fichier `~/.profile`

Bash is a Bourne-like shell. It reads commands from `~/.bash_profile` when it is invoked as the login shell, and if that file doesn't exist, it tries reading `~/.profile` instead.


### Quelles sont les différences entre `~/.profile` et [[~/.bashrc|os.unix.filesystem.bashrc]]

You can invoke a shell directly at any time, for example by launching a terminal emulator inside a GUI environment. If the shell is not a login shell, it doesn't read ~/.profile. When you start bash as an interactive shell (i.e., not to run a script), it reads ~/.bashrc (except when invoked as a login shell, then it only reads ~/.bash_profile or ~/.profile.

Aussi :

> `~/.profile` is the place to put stuff that applies to your whole session, such as programs that you want to start when you log in (but not graphical programs, they go into a different file), and environment variable definitions.

> ~/.bashrc is the place to put stuff that applies only to bash itself, such as alias and function definitions, shell options, and prompt settings. (You could also put key bindings there, but for bash they normally go into ~/.inputrc.)

## Références

- https://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile/183980#183980