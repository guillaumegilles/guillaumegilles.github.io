---
id: 56g8icc7qdsdgtl998cxg6u
title: Git LFS
desc: "Git Large File System"
updated: 1700169006710
created: 1700168970919
---

- [GitHub](https://github.com/git-lfs/git-lfs?utm_source=gitlfs_site&utm_medium=installation_link&utm_campaign=gitlfs#installing)
- [website](https://git-lfs.com/)

## installation

## Getting Started

1. set up Git LFS for your user account by running:

```shell
git lfs install
```

You only need to run this once per user account.

2. In each Git repository where you want to use Git LFS, select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime.

````shell
git lfs track "*.psd"

3. Now make sure .gitattributes is tracked:

```shell
git add .gitattributes
````

Note that defining the file types Git LFS should track will not, by itself, convert any pre-existing files to Git LFS, such as files on other branches or in your prior commit history. To do that, use the `git lfs migrate` command, which has a range of options designed to suit various potential use cases.

There is no step four. Just commit and push to GitHub as you normally would; for instance, if your current branch is named main:

```shell
git add file.psd
git commit -m "Add design file"
git push origin main
```

## git lfs migrate

- https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc?utm_source=gitlfs_site&utm_medium=doc_man_migrate_link&utm_campaign=gitlfs
