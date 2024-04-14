---
id: byjsk59zqbi8bqq0ouysu2s
title: Workspace Types
desc: Code or Native Workspace
updated: 1709819326568
created: 1708372890396
---

[Workspace Types](https://wiki.dendron.so/notes/c4cf5519-f7c2-4a23-b93b-1c9a02880f6b/)

Dendron recognizes two types of [[workspaces|vscode,workspace]], **Code** and
**Native**. When you initialize your workspace with the Initialize Workspace
command, you get a Code workspace. Code workspaces include a
`dendron.code-workspace` file which sets up vaults and recommends installing
some useful extensions. Code workspaces are great when you are setting up a
knowledge base.

Native workspaces on the other hand is created with a `dendron.yml` and don't
have a `dendron.code-workspace` file. They are useful when you are writing notes
or documentation, and you want to keep your notes as part of a project rather
than a separate knowledge base.
