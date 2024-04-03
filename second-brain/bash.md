# Bash

Pour exécuter un programme dans le terminal, on peut utiliser plusieurs méthodes :

1. la première, on saisit le nom du programme dans le [[bash.pwd]] ou on se trouve :

```bash
./hello
```

---

## Prompt

Dans une interface en ligne de commandes, le prompt est l'indicateur textuel que l'ordinateur est en attente d'une commande de la part de l'utilisateur. Il est très généralement représenté par `$`, et parfois par `>>>`.

```bash
$ pwd
/home/johndoe
$
```

The second thing to understand is that when you run a command any output it produces will usually be printed directly in the terminal, then you’ll be shown another prompt once it’s finished. Some commands can output a lot of text, others will operate silently and won’t output anything at all. Don’t be alarmed if you run a command and another prompt immediately appears, as that usually means the command succeeded. If you think back to the slow network connections of our 1970s terminals, those early programmers decided that if everything went okay they may as well save a few precious bytes of data transfer by not saying anything at all.

### Références

- https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal

---

During the formative years of the computer industry, one of the early operating systems was called Unix. It was designed to run as a multi-user system on mainframe computers, with users connecting to it remotely via individual terminals. These terminals were pretty basic by modern standards: just a keyboard and screen, with no power to run programs locally. Instead they would just send keystrokes to the server and display any data they received on the screen. There was no mouse, no fancy graphics, not even any choice of colour. Everything was sent as text, and received as text. Obviously, therefore, any programs that ran on the mainframe had to produce text as an output and accept text as an input.

Compared with graphics, text is very light on resources. Even on machines from the 1970s, running hundreds of terminals across glacially slow network connections (by today’s standards), users were still able to interact with programs quickly and efficiently. The commands were also kept very terse to reduce the number of keystrokes needed, speeding up people’s use of the terminal even more. This speed and efficiency is one reason why this text interface is still widely used today.

Shell stands for the command-line interpreter. A shell is a program that processes commands and outputs the results. A shell is a layer that sits on top of the kernel: 1) It interprets and processes the commands entered by the user. Unlike users, the shell has access to the kernel. Users can only gain access to the kernel by using a shell and entering commands (i.e. running programs). System calls are used by programs to gain access to kernel functionality. The system API is made up of all system calls.

Le shell est une interface système sous la forme de **C**ommand **L**ine **I**terface (CLI). Il permet d'intérargir avec le système d'expoitation, **O**perating **S**ystem (OS), de la machine. Simplement le shell est un programme qui reçoit des instructions sous formes de textes et qui les passent au système d'exploitation.

Pour mieux comprendre, on peut imaginer une noix, avec une coquille et un fruit. On peut schématiser le système d'exploitation avec cette noix. En anglais, _shell_ désigne la coquille. Pour manger le fruit, qu'on appelle _kernel_, il faut d'abord s'occuper de la coquille, du _shell_.

![Shell Logo](/assets/images/shell.jpg)

Peut-on accéder au kernel de l'OS grâce à autre chose que le shell ?

Oui ! L'[[interface graphique utilisateur]].

- Gather information on a system
  - [[Display CPU information|sh.lscpu]]
  -

## Supprimer un fichier : `rm` _remove_

Dans le shell, la commande pour supprimer un fichier est `rm` pour _remove_.

```shell
rm hello
```

To remove an empty directory, use the -d (directory) option. You can use wildcards (\* and ?) in directory names just as you can with filenames.

```shell
rm -d directory
```

Providing more than one directory name deletes all of the specified empty directories.

```shell
rm -d directory1 directory2 /path/to/directory3
```

To delete directories that are not empty, use the -r (recursive) option. To be clear, this removes the directories and all files and sub-directories contained within them.

```shell
rm -r directory1 directory2 directory3
```

If a directory or a file is write-protected, you will be prompted to confirm the deletion.
To delete directories that are not empty and to suppress these prompts, use the -r (recursive) and -f (force) options together.

```shell
rm -rf directory
```

Care is required here. Making a mistake with the `rm -rf` command could cause data loss or system malfunction.

---

## `apt`

    - `apt` is a command-line utility for installing, updating, removing, and otherwise managing deb packages on Ubuntu, Debian and related Linux distributions.
    - `apt install` permet d'installer un **package**. Une de forces de cette commande est l'auto-completion permettant de trouver le nom d'un **package** en utilisant la touche « tab ».
      ```shell
      $ apt install [package]
      ```
    - `apt remove ` permet de supprimer un package présent localement sur une machine.
      ```shell
      $ apt remove [package]
      ```
    - `apt search` pour chercher un **package** dans la liste des packages disponibles.
      ```shell
      $ apt search [package]
      ```
    - `apt update` pour identifier les packages pour lesquels une mise-à-jour et/ou une nouvelle versions existent. Pour procéders à la mise-à-jour, on doit utiliser la commande `apt upgrade`.
      ```shell
      $ apt update
      ```
    - `apt upgrade` pour mettre à jour les **packages** installés localement. Elle se lance souvent après un `apt update`.
      ```shell
      $ apt upgrade
      ```
      Puisque ces deux commande `apt update` et `apt upgrade` sont complémentaires, on peut les lancer simultanément.
      ```shell
      $ apt update && apt upgrade
      ```

- ## `neofetch`

  - Neofetch is a command-line system information tool written in `bash 3.2+`. Neofetch displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.
  - ### Installation avec [[Homebrew]]

    ```shell
    $ brew install neofetch
    ```

- ## Retourne la version

  ```shell
  which pip
  ```

- ## Localiser un fichier

  ```shell
  whereis conda
  ```

- ```shell
  echo $SHELL
  ```
- ## Déplacer ou renommer des fichiers
  - On peut utiliser la commande [[mv]]

> You can abbreviate many frequently used command options that are preceded by 2 dashes (`--`) to just 1 dash and the first letter of the option. So `--name` and `--envs` can be written as `-n` and `-e` respectively.
> provenant de la doc `conda`.
