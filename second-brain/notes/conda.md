---
id: ssefc78lfujizt2mnyb1tpr
title: Conda
desc: >-
  Conda is an open-source package management system and environment management
  system
updated: 1709759283053
created: 1698095139017
---

Conda is an open-source package and environment management system that runs on
Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages
and their dependencies. It also easily creates, saves, loads, and switches
between environments on your local computer. It was created for Python programs,
but it can package and distribute software for any language.

## Miniconda

Miniconda is a free minimal installer for conda. It is a small bootstrap version
of Anaconda that includes only [conda](https://docs.conda.io/en/latest/),
Python, the packages they both depend on, and a small number of other useful
packages (like pip, zlib, and a few others). If you need more packages, use the
[[conda.install]] command to install from thousands of packages available by
default in Anaconda’s public repo, or from other channels, like conda-forge or
bioconda.

## [Installer miniconda](https://docs.anaconda.com/free/miniconda/)

### Linux

These four commands quickly and quietly install the latest 64-bit version of the
installer and then clean up after themselves. To install a different version or
architecture of Miniconda for Linux, change the name of the `.sh` installer in
the `wget` command.

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

After installing, initialize your newly-installed Miniconda. The following
commands initialize for bash and zsh shells:

```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

## Cheatcheet

### Quick Start

**Tip**: It is recommended to create a new environment for any new project or
workflow.

| Actions                                                            | conda commands                    |
| ------------------------------------------------------------------ | --------------------------------- |
| verify conda install and check version                             | `conda info`                      |
| update conda in base environment                                   | `conda update -n base conda`      |
| install latest anaconda distribution                               | `conda install anaconda=2022.05`  |
| create a new environment (**tip**: name environment descriptively) | `conda create --name ENVNAME`     |
| activate environment (do this before installing packages)          | `conda activate ENVNAME`          |

### Channels and Packages

**Tip**: Package dependencies and platform specifics are automatically resolved
when using conda.

| Actions                                                                         | conda commands                               |
| :------------------------------------------------------------------------------ | -------------------------------------------- |
| list installed packages                                                         | `conda list`                                 |
| list installed packages with source info                                        | `conda list --show-channel-urls`             |
| update all packages                                                             | `conda update --all`                         |
| install a package from specific channel                                         | `conda install -c CHANNELNAME PKG1 PKG2`     |
| install specific version of package                                             | `conda install PKGNAME=3.1.4`                |
| install a package from specific channel                                         | `conda install CHANNELNAME::PKGNAME`         |
| install package with AND logic                                                  | `conda install “PKGNAME>2.5,<3.2”`           |
| uninstall package                                                               | `conda uninstall PKGNAME`                    |
| view channel sources                                                            | `conda config --show-sources`                |
| add channel                                                                     | `conda config --add channels CHANNELNAME`    |
| set default channel for pkg fetching (targets first channel in channel sources) | `conda config --set channel_priority strict` |

### Working with conda environments

**Tip**: List environments at the beginning of your session. Environments with
an asterisk are active.

| Actions                             | conda commands                              |
| :---------------------------------- | ------------------------------------------- |
| list all environments and locations | `conda env list`                            |
| list all packages + source channels | `conda list -n ENVNAME --show-channel-urls` |
| install packages in environment     | `conda install -n ENVNAME PKG1 PKG2`        |
| remove package from environment     | `conda uninstall PKGNAME -n ENVNAME`        |
| update all packages in environment  | `conda update --all -n ENVNAME`             |

### Environement management

**Tip**: Specifying the environment name confines conda commands to that
environment.

| Actions                                 | conda commands                                   |
| :-------------------------------------- | ------------------------------------------------ |
| create environment with Python version  | `conda create -n ENVNAME python=3.10`            |
| clone environment                       | `conda create --clone ENVNAME -n NEWENV`         |
| rename environment                      | `conda rename -n ENVNAME NEWENVNAME`             |
| delete environment by name              | `conda remove -n ENVNAME --all`                  |
| list revisions made to environment      | `conda list -n ENVNAME --revisions`              |
| restore environment to a revision       | `conda install -n ENVNAME --revision NUMBER`     |
| uninstall package from specific channel | `conda remove -n ENVNAME -c CHANNELNAME PKGNAME` |

### Exporting environements

**Recommendation**: Name the export file “environment.” Environment name will be
preserved.

| Actions                               | conda commands                            |
| :------------------------------------ | ----------------------------------------- |
| cross-platform compatible             | `conda env export --from-history>ENV.yml` |
| platform + package specific           | `conda env export ENVNAME>ENV.yml`        |
| platform + package + channel specific | `conda list --explicit>ENV.txt`           |

### Importing environments

**Tip**: When importing an environment, conda resolves platform and package
specifics.

| Actions            | conda commands                               |
| :----------------- | -------------------------------------------- |
| from a `.yml` file | `conda env create -n ENVNAME --file ENV.yml` |
| from a `.txt` file | `conda create -n ENVNAME --file ENV.txt`     |

### Additional hints

| Actions                          | conda commands                  |
| :------------------------------- | ------------------------------- |
| get help for any command         | `conda COMMAND --help`          |
| get info for any package         | `conda search PKGNAME --info`   |
| run commands w/o user prompt     | `conda COMMAND ARG --yes`       |
| eg, installing multiple packages | `conda install PKG1 PKG2 --yes` |
| remove all unused files          | `conda clean --all`             |
| examine conda configuration      | `conda config --show`           |
