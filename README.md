# ggilles.dev

> Personal website of Guillaume Gilles — regional economist, lecturer, and
> cybersecurity practitioner.

**Live site:** <https://ggilles.dev>

Built with [Quarto](https://quarto.org) and deployed to
[GitHub Pages](https://pages.github.com). The site is an open notebook: CTF
writeups, security research, and dev experiments alongside course materials for
students.

---

## Contents

| Section | Description |
|---------|-------------|
| [Blog](/posts/) | CTF writeups, security research, and dev experiments |
| [Teaching](/teaching/) | Course materials for statistics, financial analysis, and AI |
| [About](/about.qmd) | Professional background and links (also synced to GitHub profile README) |

### Teaching courses

| Course | Institution | Level |
|--------|-------------|-------|
| [Probabilités & Statistiques](teaching/statistics-probability/) | ESSCA | Undergraduate |
| [Mathematical Analysis](teaching/mathematical-analysis/) | ESSCA | Undergraduate |
| [Financial Analysis](teaching/financial-analysis/) | INSEEC MSc | Graduate |
| [AI Guide](teaching/ai/) | — | Self-study |

---

## Tech Stack

- **[Quarto](https://quarto.org)** — static site generator; renders `.qmd`
  files to HTML (and GFM for the profile README)
- **GitHub Pages** — hosting; Quarto outputs to `docs/`, which GitHub Pages
  serves directly from the `main` branch
- **[Cloudflare Workers](https://workers.cloudflare.com)** (`worker/`) — edge
  function powering the AI chat widget on the homepage
- **[Cloudflare AI](https://developers.cloudflare.com/workers-ai/)** — runs
  `@cf/meta/llama-3.1-8b-instruct` to answer questions about Guillaume's
  background
- **Python** (`requirements.txt`) — used in computational notebooks:
  `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `shiny`, `shinylive`
- **[Hypothesis](https://web.hypothes.is/)** — collaborative annotation on
  course pages

---

## Project Structure

```
.
├── _quarto.yml              # Site configuration (nav, sidebar, theme)
├── index.qmd                # Homepage with AI chat widget
├── about.qmd                # About page → also auto-synced to GitHub profile README
├── blog.qmd                 # Blog listing page
├── teaching.qmd             # Teaching index page
│
├── posts/                   # Blog posts (CTF writeups, dev experiments, …)
├── teaching/
│   ├── statistics-probability/
│   ├── mathematical-analysis/
│   ├── financial-analysis/
│   └── ai/
│
├── assets/                  # Theme (dark.scss), favicon, OG image, profile photo
├── scripts/
│   └── update-profile-readme.sh  # Post-render: syncs about.qmd → GitHub profile
├── worker/
│   ├── index.js             # Cloudflare Worker (AI chat backend)
│   └── wrangler.toml        # Worker deployment config
│
├── docs/                    # Quarto build output (served by GitHub Pages)
├── requirements.txt         # Python dependencies for computational content
└── .devcontainer/           # Dev container for GitHub Codespaces
```

---

## Local Development

### Prerequisites

- [Quarto CLI](https://quarto.org/docs/get-started/) ≥ 1.5
- Python ≥ 3.11 (for computational notebooks)

### Setup

```bash
# Clone the repo
git clone https://github.com/guillaumegilles/guillaumegilles.github.io.git
cd guillaumegilles.github.io

# Install Python dependencies
python -m pip install -r requirements.txt

# Start the preview server (live reload)
quarto preview
```

The site will be available at `http://localhost:4848` with hot-reload on save.

### Build

```bash
quarto render
```

Output is written to `docs/`. The post-render script
(`scripts/update-profile-readme.sh`) also fires and attempts to sync the
GitHub profile README — it gracefully skips the push if SSH keys are not
configured.

### GitHub Codespaces

Open this repo in a Codespace — the dev container installs Quarto and Python
dependencies automatically and runs `quarto preview` on startup.

---

## Deployment

### Website (GitHub Pages)

Pushing to `main` deploys automatically. GitHub Pages serves the `docs/`
directory on the custom domain `ggilles.dev` (configured via `CNAME`).

### AI Chat Worker (Cloudflare Workers)

The homepage chat widget talks to a Cloudflare Worker at
`https://resume-chat.resume-chat.workers.dev`. To deploy or update the worker:

```bash
cd worker
npx wrangler deploy
```

The worker uses Cloudflare AI (Llama 3.1 8B Instruct) and is CORS-locked to
`https://ggilles.dev`.

### GitHub Profile README

`about.qmd` doubles as the GitHub profile README. After every `quarto render`,
`scripts/update-profile-readme.sh` renders `about.qmd` to GFM Markdown and
pushes the result to the
[`guillaumegilles/guillaumegilles`](https://github.com/guillaumegilles/guillaumegilles)
profile repository via SSH.

---

## Freeze

Quarto's `freeze: auto` feature caches the output of computationally expensive
cells. Cached results live in `_freeze/` and are committed to the repository so
that contributors without the Python dependencies can still build the site.

---

## License

[GPL-3.0](LICENSE) — course content and blog posts are © Guillaume Gilles.
