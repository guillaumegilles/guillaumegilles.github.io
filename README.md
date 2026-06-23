# ggilles.dev

![License](https://img.shields.io/github/license/guillaumegilles/guillaumegilles.github.io)
![Stars](https://img.shields.io/github/stars/guillaumegilles/guillaumegilles.github.io?style=social)
![Issues](https://img.shields.io/github/issues/guillaumegilles/guillaumegilles.github.io)

> Personal website combining a blog, teaching course materials, and an AI-powered résumé chat.

---

## ✨ Features

- **Blog** — articles on data science, AI, and software engineering
- **Teaching** — course materials for statistics, financial analysis, maths, and AI
- **AI Worker** — Cloudflare-hosted chat widget that answers questions about the résumé

---

## 📸 Demo

🔗 [ggilles.dev](https://ggilles.dev)

---

## 🚀 Getting Started

### Prerequisites

- [Quarto](https://quarto.org) 1.x or higher
- Python 3.12 or higher
- Node.js (for the Cloudflare Worker)

### Installation

```bash
git clone https://github.com/guillaumegilles/guillaumegilles.github.io.git
cd guillaumegilles.github.io
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running locally

```bash
quarto preview
```

Open [http://localhost:4321](http://localhost:4321) in your browser.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Site generator | [Quarto](https://quarto.org) |
| Styling | Custom SCSS (`assets/dark.scss`) |
| Comments | [Giscus](https://giscus.app) |
| Edge Worker | Cloudflare Workers (AI résumé chat) |
| Deployment | GitHub Pages (`docs/` directory) |

---

## 🗺 Roadmap

- [ ] Expand teaching materials (AI & dev course)
- [ ] Improve Cloudflare Worker AI responses
- [ ] Add more blog posts

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## 📄 License

Distributed under the GPL-3.0 License. See [LICENSE](LICENSE) for more information.

---

## 🌟 Stargazers

Thanks to everyone who has starred this project!

[![Stargazers](https://reporoster.com/stars/guillaumegilles/guillaumegilles.github.io)](https://github.com/guillaumegilles/guillaumegilles.github.io/stargazers)
