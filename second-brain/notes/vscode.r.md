---
id: 88kzv3d84rvg1hrszlv65h8
title: Working with R in VSCode
desc: ''
updated: 1705564273618
created: 1704749811616
---

The [R extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)
for Visual Studio Code supports extended syntax highlighting, code completion, linting,
formatting, interacting with R terminals, viewing data, plots, workspace variables, help
pages, managing packages and working with R Markdown documents.

## [Getting Started](https://github.com/REditorSupport/vscode-R#getting-started)

1. [Install R](https://cloud.r-project.org/) (>= 3.4.0) on your system. For Windows users,
   Writing R Path to the registry is recommended in the installation.
2. Install `[languageserver](https://github.com/REditorSupport/languageserver)` in R.

```R
install.packages("languageserver")
```

3. Install the [R extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r).
4. Create an R file and start coding.

## Enhance the experience of using R in VS Code:

1. [radian](https://github.com/randy3k/radian): A modern R console that corrects many
   limitations of the official R terminal and supports many features such as syntax
   highlighting and auto-completion.

   To Install it globally

   ```bash
   pip install -U radian
   ```

   Or if you don't have root privilege, you may want to install it only for yourself:

   ```bash
   pip install --user radian
   ```

   You may run `[[bash.which]] radian` to see where your `radian` executable is located.
   Then the following VS Code settings should be updated to properly use `radian` as the
   default terminal. If your `radian` is installed only for user:

   ```json
   {
   "r.bracketedPaste": true,
   "r.rterm.linux": "/home/user/.local/bin/radian"
   }
   ```

2. [VSCode-R-Debugger](https://github.com/ManuelHentschel/VSCode-R-Debugger): A VS Code extension
   to support R debugging capabilities.It depends on vscDebugger.

   - Install VSCode-R-Debugger extension in VS Code.
   - Install vscDebugger package via

   ```R
   remotes::install_github("ManuelHentschel/vscDebugger")
   ```

3. [httpgd](https://github.com/nx10/httpgd): An R package to provide a graphics device that
   asynchronously serves SVG graphics via HTTP and WebSockets. It enables the plot viewer
   based on httpgd in VS Code.

   - Install `httpgd` from CRAN/r-universe

     ```R
     install.packages("httpgd", repos = c("https://nx10.r-universe.dev", "https://cran.r-project.org"))
     ```

   - Enable `r.plot.useHttpgd` in VS Code settings.

## [Features](https://github.com/REditorSupport/vscode-R?tab=readme-ov-file#features)

- [Code Completion](https://code.visualstudio.com/docs/languages/r#_code-completion-intellisense)
  The R extension supports code completion and many other code editing features thanks to the R
  language server. The completion shows the available functions and variables in the scope and
  the current R workspace along with the documentation from packages or provided as comments.
- [Linting](https://code.visualstudio.com/docs/languages/r#_linting)
  Linting is a feature that checks the code for warnings and potential errors. R code linting
  is provided by `lintr` package. You can customize it by choosing from the list of available
  linters via the configuration file.
- [Workspace viewer](https://code.visualstudio.com/docs/languages/r#_workspace-viewer)
  The workspace viewer is located in the side bar in VS Code and contains the packages in use and
  global variables in the active R session. Select the R icon in the Activity bar and the workspace
  viewer and help pages viewer will show up. It is a convenient way to view the R workspace, preview
  existing R objects, find help topics, and read help pages interactively.
- [Debugging](https://code.visualstudio.com/docs/languages/r#_debugging)
  The R debugging capabilities are provided by R Debugger extension. It supports debugging R
  code or an R project by launching a new R process or attaching to a running one. When a
  [[vscode.breakpoint]] is hit, you can view or alter the variables of the currently selected
  stack frame, or evaluate an expression in the debug console in the stack frame.
- [R Markdown support](https://github.com/REditorSupport/vscode-R/wiki/R-Markdown)
