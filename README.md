# guillaumegilles.github.io

Personal website — live at **[ggilles.dev](https://ggilles.dev)**.

Regional economist by day, CTF player by night, and teacher in between.
The site hosts [blog posts & CTF writeups](https://ggilles.dev/blog),
[projects](https://ggilles.dev/projects), and
[course materials](https://ggilles.dev/teaching) for statistics and financial
analysis classes.

## Tech stack

| Layer | Tool |
|---|---|
| Static site generator | [Quarto](https://quarto.org/) |
| Styling | Custom SCSS (light + dark theme) |
| Hosting | GitHub Pages (`docs/` output dir) |
| AI chat widget | Cloudflare Worker (`worker/`) |

## Project structure

```
.
├── _quarto.yml          # site-wide configuration
├── index.qmd            # home page
├── blog.qmd             # blog listing
├── projects.qmd         # projects listing
├── teaching.qmd         # teaching listing
├── posts/               # blog posts & CTF writeups
├── projects/            # project pages
├── teaching/            # course materials (stats, financial analysis)
├── assets/              # SCSS themes, favicon, colour palette
├── worker/              # Cloudflare Worker for AI resume chat
├── about/               # About page, résumé, and GitHub profile README (see below)
└── docs/                # rendered output (deployed to GitHub Pages)
```

## Getting started

1. Install [Quarto](https://quarto.org/docs/get-started/).

2. Clone the repo:

   ```sh
   git clone git@github.com:guillaumegilles/guillaumegilles.github.io.git
   cd guillaumegilles.github.io
   ```

3. Preview locally (auto-reloads on save):

   ```sh
   quarto preview
   ```

4. Build the site:

   ```sh
   quarto render
   ```

   Output lands in `docs/`, which GitHub Pages serves directly.

## About page & GitHub profile README

`about/index.qmd` is the single source of truth for both the site's About page
and the GitHub profile README. It is rendered in two formats:

- **HTML** — by `quarto render` as part of the normal site build.
- **GitHub Flavored Markdown** — by the `Makefile` inside `about/`, which writes
  `about/README.md`. That file is what GitHub displays on the
  [guillaumegilles](https://github.com/guillaumegilles) profile page.

To regenerate the GitHub profile README after editing `about/index.qmd`:

```sh
cd about/
make readme
```

## AI chat widget

The home page includes a chat widget backed by a Cloudflare Worker that
answers questions about Guillaume's background using an LLM.

To deploy your own:

```sh
cd worker/
wrangler deploy
```

Then replace the `WORKER_URL` placeholder in `index.qmd` with the URL
printed by `wrangler deploy`.

## Color palette

![Color palette](assets/color-palette.png)

## License

Source code is licensed under [GPL-3.0](LICENSE).
Content (posts, course materials) is © Guillaume Gilles — all rights reserved
unless otherwise noted.
