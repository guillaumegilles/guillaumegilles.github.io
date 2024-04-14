---
id: wuy46pupz3g66medso128m0
title: Poetry
desc: Python packaging and dependency management made easy
updated: 1708979690846
created: 1708287137863
---

> [Poetry](https://python-poetry.org/docs/) is a tool for **dependency management** and **packaging** in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

Poetry requires Python 3.8+. It is multi-platform and the goal is to make it work equally well on Linux, macOS and Windows.

> Install poetry sur la base et pas sur le venv ??
> --- pas certain de comprendre ce que cela signifie

## poetry init

Generate the pyproject.toml file

## poetry install

Create a [[virtual environment]] and install python packages from the pyporject.toml file

## poetry env info

Display information about the virtual environment

## poetry env info -p

Get only the path

## poetry config virtualenvs.in-project true

Create the virtual environment inside the project directory
=> create a .venv with binaries, librairies (dependencies)

> this create a `~/.config/pypoetry/config.toml` file to store poetry configuration

## poetry add <package names>

Add the package to the pyproject.toml

## poetry remove <package names>

## poetry env list

List virtual environment

## poetry shell

Activate the virtual environment

## deactivate

Deactivate the virtual environment

- [Andy Mutaschak](https://andymatuschak.org/)
