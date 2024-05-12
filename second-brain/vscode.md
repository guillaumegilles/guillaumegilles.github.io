---
title: VSCode
---

- [ ] [VS Code Tutorial – Become More Productive](https://www.youtube.com/watch?v=heXQnM99oAI)
- [ ] [VSCode, Faster](https://blog.zsa.io/vscode-tips/?mc_cid=f7de3b31dd)
- [ ] [Terminal Basics](https://code.visualstudio.com/docs/terminal/basics)
- [ ] [Data Science in Visual Studio Code](https://code.visualstudio.com/docs/datascience/overview)
- [ ] [Integrate with External Tools via Tasks](https://code.visualstudio.com/docs/editor/tasks#vscode)

## `setting.json`

le fichier de configuration de `VSCode` se trouve dans `~/.config/Code/User/setting.json`.

## User Interface

- **A**: Activity Bar
- **B**: Side Bar
- **C**: Editor Groups
- **D**: Panel
- **E**: Status Bar

![vscode-ui](/assets/images/vscode-ui.png)

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

## [[foam]] Panels

You can see a few panels on the left, including:

- `Outline`: this panel shows you the structure of the file based on the headings
- `Tag Explorer`: This shows you the tags in your workspace, see [[foam-tags]] for more information on tags

[//begin]: # "Autogenerated link references for markdown compatibility"
[vscode.dendron]: vscode.dendron.md "📑 Dendron"
[vscode.quarto]: vscode.quarto.md "Quarto"
[//end]: # "Autogenerated link references"
