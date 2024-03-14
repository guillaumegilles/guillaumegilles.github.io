---
id: ur1jux7mw8vlh6izzbt2b4g
title: pwd
desc: visualiser le répertoire dans lequel on se trouve
updated: 1680642099974
created: 1668160648908
---

`pwd` signifie **p**rint **w**orking **d**irectory. Cette commande permet d'*output* le répertoire (*directory*) dans lequel on se trouve. Dans l'exemple `/home/johndoe`

```shell
$ pwd
/home/johndoe
```

Now to the command itself. pwd is an abbreviation of ‘print working directory’. All it does is print out the shell’s current working directory. But what’s a working directory?

One important concept to understand is that the shell has a notion of a default location in which any file operations will take place. This is its working directory. If you try to create new files or directories, view existing files, or even delete them, the shell will assume you’re looking for them in the current working directory unless you take steps to specify otherwise. So it’s quite important to keep an idea of what directory the shell is “in” at any given time, after all, deleting files from the wrong directory could be disastrous. If you’re ever in any doubt, the pwd command will tell you exactly what the current working directory is.

---

## Références

- https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal