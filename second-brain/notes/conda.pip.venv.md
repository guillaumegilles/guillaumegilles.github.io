---
id: fwl5yvf167e7fq9nrzyfmpg
title: Conda vs Pip vs Venv
desc: ""
updated: 1709757538773
created: 1709757272404
---

## `Conda` vs. `pip` vs. `venv` commands

If you have used [[python.pip]] and [[python.venv]] in the past, you can use
`conda` to perform all of the same operations. `pip` is a [[python.package]]
manager and `venv` is an [[virtual-environment]] manager. `conda` is both.

| Task                                 | Conda package and environment manager command       |
| ------------------------------------ | --------------------------------------------------- |
| Install a package                    | conda install $PACKAGE_NAME                         |
| Update a package                     | conda update --name $ENVIRONMENT_NAME $PACKAGE_NAME |
| Update package manager               | conda update conda                                  |
| Uninstall a package                  | conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME |
| Create an environment                | conda create --name $ENVIRONMENT_NAME python        |
| Activate an environment              | conda activate $ENVIRONMENT_NAME \*                 |
| Deactivate an environment            | conda deactivate                                    |
| Search available packages            | conda search $SEARCH_TERM                           |
| Install package from specific source | conda install --channel $URL $PACKAGE_NAME          |
| List installed packages              | conda install --channel $URL $PACKAGE_NAME          |
| Create requirements file             | conda list --export                                 |
| List all environments                | conda info --envs                                   |
| Install other package manager        | conda install pip                                   |
| Install Python                       | conda install python=x.x                            |
| Update Python                        | conda update python \*                              |

1. `conda activate` only works on conda 4.6 and later versions. For conda
   versions prior to 4.6, type:

   - Windows: `activate`
   - Linux and macOS: `source activate`

2. `conda update python` updates to the most recent in the series, so any Python
   2.x would update to the latest 2.x and any Python 3.x to the latest 3.x.
