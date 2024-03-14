---
id: 8etnr0vomotgmro2p0119cb
title: VSCode / VSCodium
desc: Microsoft open source IDE
updated: 1708462416876
created: 1684330226265
---

## `setting.json`

le fichier de configuration de `VSCode` se trouve dans `~/.config/Code/User/setting.json`.

## User Interface

![vscode-ui](/assets/vscode-ui.png)

## Command Palette

| keybindings    | functions                                                                              |
| :------------- | :------------------------------------------------------------------------------------- |
| `Ctrl+Shift+P` | Show All Command: afficher la `command palette`                                        |
| `Ctrl+P`       | will let you navigate to any file or symbol by typing its name                         |
| `Ctrl+P` + `?` | `?` into the input field to get a list of available commands you can execute from here |
| `Ctrl+T`       | Go to Symbol in workspace                                                              |
| `Ctrl+G`       | will let you navigate to a specific line in a file                                     |
| `Ctrl+Tab`     | Vwill cycle you through the last set of files opened                                   |
| `Ctrl+Shift+O` | will let you navigate to a specific symbol in a file                                   |

## Racourcis clavier Custom

| keybindings       | functions                    |
| :---------------- | :--------------------------- |
| `Ctrl+K` `J`      | Focus on Terminal View       |
| `Ctrl+K` `PageUp` | View: Toggle Maximized Panel |

## généraux

| keybindings     | functions                                                                           |
| :-------------- | :---------------------------------------------------------------------------------- |
| `Ctrl+→` or `←` | move word by word                                                                   |
| `Ctrl+D`        | Add Selection to the Next Find Match (repeat multiple time to select more than one) |
| `Ctrl+Tab`      | afficher les _tabs_ ouvertes                                                        |
| `Ctrl+PgUp`     | accéder à la _tab_ suivante                                                         |
| `Ctrl+PgDown`   | accéder à la _tab_ précédente                                                       |
| `F5`            | exécuter le code                                                                    |

## Navigation

| keybindings       | functions                                |
| :---------------- | :--------------------------------------- |
| `Ctrl+ ,`         | accéder au _setting_ de VSCode           |
| `Ctrl+K` `Ctrl+S` | accéder au _keyboard shortcut_ de VSCode |
| `Ctrl+Tab`        | afficher les _tabs_ ouvertes             |
| `Ctrl+PgUp`       | accéder à la _tab_ suivante              |
| `Ctrl+PgDown`     | accéder à la _tab_ précédente            |
| `F5`              | exécuter le code                         |

## Éditer le texte

| keybindings                  | functions                                                        |
| :--------------------------- | :--------------------------------------------------------------- |
| `Ctrl+Space`                 | Trigger Suggest (invoque _IntelliSense_)                         |
| `Shift`+`Alt`+`Up` or `Down` | copier une ligne de texte pour l'ajouter au dessus ou en dessous |
| `Alt+Up` or `Down`           | déplacer la ligne ves le bas ou le haut                          |
| `Ctrl+/`                     | Toggle _comment_                                                 |
| `F2`                         | _rename refactoring_                                             |
| `Shift`+`Alt`+`f`            | _format_ le document entier                                      |
| `Cmd`+`k` `Cmd`+`f`          | _format_ la sélection                                            |

## tabs

| keybindings          |                   functions                    |
| :------------------- | :--------------------------------------------: |
| `ctrl+k shift+enter` |    _pin/unpin_ une la fenêtre active, _tab_    |
| `ctrl+w`             |        fermer la fenêtre active, _tab_         |
| `Ctrl+k w`           | fermer **toutes** les fenêtres actives, _tabs_ |

## [[vscode.dendron]]

| keybindings  |                    functions                     |
| :----------- | :----------------------------------------------: |
| `Ctrl+K` `V` | Toggle Preview: afficher la fenêtre de _preview_ |
| `Ctrl+K` `S` |             créer une _scratch note_             |

## [[vscode.quarto]]

| keybindings           |                functions                 |
| :-------------------- | :--------------------------------------: |
| `Cmd`+`Shift`+`I`     | Insérer une cellule de code. _code cell_ |
| `Cmd`+`Shift`+`K`     |   Execute the Quarto: Preview command    |
| `Cmd`+`Enter`         |     Execute the **current line(s)**      |
| `Cmd`+`Shift`+`Enter` |       Execute the **current cell**       |
| `Cmd`+`Alt`+`P`       |      Execute the **previous cells**      |

## Tasks

[Integrate with External Tools via Tasks](https://code.visualstudio.com/docs/editor/tasks#vscode)

## [Remote Repositories](https://code.visualstudio.com/blogs/2021/06/10/remote-repositories)

## [Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

## [Terminal Basics](https://code.visualstudio.com/docs/terminal/basics)

Hi everyone!

I’ve been thinking to create a website, and more pricesly a blog, for a while now. I’ve never crossed the line of hypothesis until now, by fear of being judged. Expressing one’s thoughts on the web is intimidating and daunting. But I supposed the desire to have a place of my own to talk about thing that resonnate to me and pet projects I am working on is a stronger driving force than lack of self confidence.

As an aspirying machine learning engineer, blog posts are great opportunities to showcase your work. According to Chip Huyen, it is a great place to demonstrate “examples that convinced me of a candidate’s expertise in certain technology [...] a blog post that covers in-depth detail about X that made our team go: Whoa, they really know about X.” [@huyenWhatWeLook2023]

For David Robinson, a blog is the best advice for someone wanted to start a data science career. It helps to:

1. **Practice analyzing data and communicating about it**: it can be easily resumed to "practice makes perfect" or in French: "C'est en forgeant qu'on devient forgeron".
2. **Create a portfolio of your work and skills**: after spending hours and nights practicing your data science craft, a blog is a valuable medium to share your work. This piece of advice works well for established data scientists as well.
3. **Get feedback and evaluation**: creating a community and interacting with an audience helps individuals to reach for better. [@robinsonAdviceAspiringData2017]
