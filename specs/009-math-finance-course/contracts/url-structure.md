# Contract: URL Structure — Mathématiques financières (M1)

**Feature**: `009-math-finance-course`
**Type**: URL contract
**Date**: 2026-10-04

## URL Map

| Source file | Rendered URL | Sidebar ID |
|-------------|--------------|------------|
| `teaching/mathematical-finance/index.qmd` | `/teaching/mathematical-finance/` | `en-mathematics-finance` |
| `fr/teaching/mathematics-finance/index.qmd` | `/fr/teaching/mathematics-finance/` | `fr-mathematics-finance` |
| `fr/teaching/mathematics-finance/module-01.qmd` | `/fr/teaching/mathematics-finance/module-01.html` | `fr-mathematics-finance` |
| `fr/teaching/mathematics-finance/module-02.qmd` | `/fr/teaching/mathematics-finance/module-02.html` | `fr-mathematics-finance` |
| `fr/teaching/mathematics-finance/module-03.qmd` | `/fr/teaching/mathematics-finance/module-03.html` | `fr-mathematics-finance` |
| `fr/teaching/mathematics-finance/glossaire.qmd` | `/fr/teaching/mathematics-finance/glossaire.html` | `fr-mathematics-finance` |
| `fr/teaching/mathematics-finance/formulaire.qmd` | `/fr/teaching/mathematics-finance/formulaire.html` | `fr-mathematics-finance` |

## EN ↔ FR Parity Links

| EN URL | FR URL |
|--------|--------|
| `/teaching/mathematical-finance/` | `/fr/teaching/mathematics-finance/` |
| (no EN module pages yet) | `/fr/teaching/mathematics-finance/module-01.html` |
| (no EN module pages yet) | `/fr/teaching/mathematics-finance/module-02.html` |
| (no EN module pages yet) | `/fr/teaching/mathematics-finance/module-03.html` |

Note: Module-level EN ↔ FR links will be added when full EN course pages exist.
The stub EN `index.qmd` links to the FR `index.qmd` as its parity counterpart.

## Sidebar Registration in `_quarto.yml`

```yaml
#--- EN --- Mathematics Finance
- id: en-mathematics-finance
  title: "Financial Mathematics"
  contents:
    - teaching/mathematical-finance/index.qmd

#--- FR --- Mathematics Finance
- id: fr-mathematics-finance
  title: "Mathématiques financières"
  contents:
    - fr/teaching/mathematics-finance/index.qmd
    - fr/teaching/mathematics-finance/module-01.qmd
    - fr/teaching/mathematics-finance/module-02.qmd
    - fr/teaching/mathematics-finance/module-03.qmd
    - section: "**Ressources**"
      contents:
        - fr/teaching/mathematics-finance/glossaire.qmd
        - fr/teaching/mathematics-finance/formulaire.qmd
```

## Constraints

- All URLs are deterministic and static (no query strings, no dynamic routing).
- The `docs/` directory must contain the rendered HTML counterparts of all
  source `.qmd` files after `quarto render`.
- No page in `fr/teaching/mathematics-finance/` may be rendered without a
  corresponding sidebar entry (constitution Principle II).
