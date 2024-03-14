---
id: 5lp16f034vlq4u5darll7nu
title: Minecraft
desc: ''
updated: 1697399172800
created: 1697377414152
---

Pour implémenter de nouveaux mods, voici les étapes à suivre :

## Prérequis

### S'assurer que [Java](https://www.oracle.com/java/) est installé en local
Grâce à la commande [[shell]]
```shell
$ java -version
```

Si ce n'est pas le cas, on peut rapidement l'installer avec [[homebrew]]
```shell
$ brew install java
```

### S'asurer que [Maven](https://maven.apache.org/)
Grâce à la commande [[shell]]
```shell
$ mvn -v
```

Si ce n'est pas le cas, on peut rapidement l'installer avec [[homebrew]]
```shell
$ brew install maven
```

### [[vscode]] extensions
1. [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
2. [Gradle for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-gradle)

## Installer NeoForged
1. Télécharger le fichier `.jar` sur le site [NeoForged](https://neoforged.net/) correpondant à la version de Minecraft.
2. cloner le répertoire [[git]] [MDK](https://github.com/neoforged/MDK) dans le répertoire local du mod et hop !

## Références
- [website](https://neoforged.net/)
- [NeoForged documentation - Getting Starded](https://docs.neoforged.net/docs/gettingstarted/)
- [GitHub](https://github.com/neoforged)
