---
id: t5dhk0pxcjbtu1358qqmtsb
title: Venv
desc: ""
updated: 1708464691433
created: 1700088651244
---

The `venv` module supports creating lightweight [[virtual-environment]], each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.[^1]

When used from within a virtual environment, common installation tools such as [[python.pip]] will install Python packages into a virtual environment without needing to be told to do so explicitly.

A virtual environment is (amongst other things):

- Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.
- Contained in a directory, conventionally either named `venv` or `.venv` in the project directory, or under a container directory for lots of virtual environments, such as `~/.virtualenvs`.
- Not checked into source control systems such as Git.
- Considered as disposable -- it should be simple to delete and recreate it from scratch. You don't place any project code in the environment

## Creating virtual environments

Creation of virtual environments is done by executing the command `venv`:

```bash
python3 -m venv .venv
```

```powershell
python -m venv .venv
```

Running this command creates the target directory (creating any parent directories that don’t exist already) and places a `pyvenv.cfg` file in it with a home key pointing to the Python installation from which the command was run (a common name for the target directory is .venv). It also creates a bin (or Scripts on Windows) subdirectory containing a copy/symlink of the Python binary/binaries (as appropriate for the platform or arguments used at environment creation time). It also creates an (initially empty) lib/pythonX.Y/site-packages subdirectory (on Windows, this is Lib\site-packages). If an existing directory is specified, it will be re-used.

## Activate virtual environment

`<venv>` must be replaced by the path to the directory containing the virtual environment.

POSIX (MacOS and Linux)

```bash
source <venv>/bin/activate
```

Windows

```powershell
PS C:\> <venv>\Scripts\Activate.ps1
```

## `.venv/lib` directory

List of all packages installed inside the virtual environment.

[^1]: https://docs.python.org/fr/3/library/venv.html
