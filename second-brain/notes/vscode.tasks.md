---
id: gn28c419o6ojwean84fk0zb
title: Tasks
desc: ''
updated: 1708371247061
created: 1708371227831
---

https://code.visualstudio.com/Docs/editor/tasks

You can create a VS Code task using the .runOptions.runOn == "folderOpen" option to install them when opening the workspace.

Create (or update) file in .vscode/tasks.json with the following. This example assumes jq is installed and the code CLI command is available.

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Install All Recommended Extensions",
      "type": "shell",
      "command": "jq -r '.recommendations[]' ./.vscode/extensions.json | xargs -L 1 code --install-extension",
      "runOptions": {
        "runOn": "folderOpen"
      },
      "presentation": {
        "reveal": "silent"
      }
    }
  ]
}
```
