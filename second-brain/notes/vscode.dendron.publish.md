---
id: bhwul5v3bvk3473txc9s3x1
title: "\U0001F4D1 Dendron Publish"
desc: Publier un site web avec Dendron
updated: 1697316355352
created: 1697315075187
---

1. Command [[vscode]] `>Dendron: Configure (yaml)`

```yaml
publishing:
    siteUrl: {https://www.guillaumegilles.com/}
```

## [[CLI|vscode.dendron#cli]]
Se positionner à la base du répertoire, dans lequel se trouve le fichier `dendron.code-workspace`.

### Initialiser le site grâce à [Next.JS](https://nextjs.org/)
```shell
$ npx dendron publish init
```

## Publié le site en local
```shell
$ npx dendron publish dev
```

- le site est accessible sur http://localhost:3000/
- `ctrl` + `e` dans le terminal pour arrêter le _preview_

## Exporter le site, une fois qu'il est prêt
```shell
$ npx dendron publish export
```