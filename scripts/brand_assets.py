#!/usr/bin/env python3
"""Generate the ggilles.dev brand kit: gg monogram mark, category glyphs,
favicon, og-image, and one thumbnail per blog post.

Single source of truth for the visual identity. Re-run after changing the
palette below or after adding a post:

    .venv/bin/python scripts/brand_assets.py

Posts that already declare `image:` in their front matter are left untouched;
for all others an `image: assets/posts/<slug>.png` line is injected.
"""
import glob
import math
import os
import re

import yaml
from PIL import Image, ImageDraw, ImageFont

ROOT = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if "__file__" in globals() else os.getcwd())
BRAND = os.path.join(ROOT, "assets", "brand")
POSTS_IMG = os.path.join(ROOT, "assets", "posts")

# Palette — mirror of assets/custom.scss
SURFACE = (250, 249, 245)        # #FAF9F5
SURFACE_SUBTLE = (242, 240, 233) # #F2F0E9
BORDER = (224, 221, 210)         # #E0DDD2
BORDER_STRONG = (203, 199, 185)  # #CBC7B9
INK = (43, 43, 48)               # #2B2B30
INK_STRONG = (18, 18, 20)        # #121214
INK_DIM = (107, 107, 116)        # #6B6B74
ACCENT = (47, 93, 138)           # #2F5D8A

FD = "/usr/share/fonts/truetype/dejavu/"
F_SANS = FD + "DejaVuSans.ttf"
F_SANS_B = FD + "DejaVuSans-Bold.ttf"
F_MONO = FD + "DejaVuSansMono.ttf"
F_MONO_B = FD + "DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# ─── Mark: "gg" monogram with a sparkline underline ──────────────────

def draw_mark(size, letters=INK_STRONG, spark=ACCENT):
    """Transparent RGBA image with the gg mark."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fs = int(size * 0.58)
    f = font(F_MONO_B, fs)
    d.text((size * 0.50, size * 0.42), "gg", font=f, fill=letters, anchor="mm")
    # sparkline underline: dips then rises, ends on a data-point dot
    w = max(2, int(size * 0.045))
    pts = [
        (size * 0.16, size * 0.76),
        (size * 0.34, size * 0.70),
        (size * 0.50, size * 0.78),
        (size * 0.66, size * 0.64),
        (size * 0.84, size * 0.56),
    ]
    d.line(pts, fill=spark, width=w, joint="curve")
    r = w * 1.1
    d.ellipse([pts[-1][0] - r, pts[-1][1] - r, pts[-1][0] + r, pts[-1][1] + r], fill=spark)
    return img


# ─── Category glyphs: single-stroke line icons in ACCENT ─────────────

def _box(d, box, color, w):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=int((x1 - x0) * 0.08), outline=color, width=w)


def glyph_bell(box, color=ACCENT, w=None):
    """Gaussian curve on a baseline — stats."""
    x0, y0, x1, y1 = box
    s = x1 - x0
    w = w or max(3, int(s * 0.055))
    img = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = s * 0.10
    base = s - pad
    d.line([(pad, base), (s - pad, base)], fill=color, width=w)
    pts = []
    for i in range(200):
        x = -3 + 6 * i / 199
        y = math.exp(-x * x / 2)
        pts.append((pad + (x + 3) / 6 * (s - 2 * pad), base - y * (s - 2 * pad) * 0.92))
    d.line(pts, fill=color, width=w, joint="curve")
    return img


def glyph_candles(box, color=ACCENT, w=None):
    """Three candlesticks trending up — finance."""
    x0, y0, x1, y1 = box
    s = x1 - x0
    w = w or max(3, int(s * 0.05))
    img = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = s * 0.12
    body_w = (s - 2 * pad) / 3 * 0.45
    candles = [  # (wick_top, body_top, body_bottom, wick_bottom) in fractions of usable height
        (0.55, 0.62, 0.80, 0.88),
        (0.35, 0.42, 0.62, 0.70),
        (0.12, 0.20, 0.44, 0.52),
    ]
    top, bot = pad, s - pad
    for i, (wt, bt, bb, wb) in enumerate(candles):
        cx = pad + (i + 0.5) * (s - 2 * pad) / 3
        y_wt = top + wt * (bot - top)
        y_bt = top + bt * (bot - top)
        y_bb = top + bb * (bot - top)
        y_wb = top + wb * (bot - top)
        d.line([(cx, y_wt), (cx, y_wb)], fill=color, width=w)
        d.rectangle([cx - body_w / 2, y_bt, cx + body_w / 2, y_bb], fill=color)
    return img


def glyph_integral(box, color=ACCENT, w=None):
    """Integral sign — math. Rendered from the font for a correct shape."""
    x0, y0, x1, y1 = box
    s = x1 - x0
    img = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(F_SANS, int(s * 0.95))
    d.text((s * 0.5, s * 0.52), "\u222b", font=f, fill=color, anchor="mm")
    return img


def glyph_nodes(box, color=ACCENT, w=None):
    """Node graph — AI."""
    x0, y0, x1, y1 = box
    s = x1 - x0
    w = w or max(3, int(s * 0.05))
    img = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = s / 2
    r = s * 0.085
    nodes = [(s * 0.22, s * 0.30), (s * 0.78, s * 0.30), (s * 0.22, s * 0.74), (s * 0.78, s * 0.74)]
    for nx, ny in nodes:
        d.line([(c, c), (nx, ny)], fill=color, width=w)
    for nx, ny in nodes:
        d.ellipse([nx - r, ny - r, nx + r, ny + r], outline=color, width=w)
    d.ellipse([c - r, c - r, c + r, c + r], fill=color)
    return img


def glyph_terminal(box, color=ACCENT, w=None):
    """Terminal window with prompt — dev & web."""
    x0, y0, x1, y1 = box
    s = x1 - x0
    w = w or max(3, int(s * 0.05))
    img = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = s * 0.06
    _box(d, (pad, pad * 1.6, s - pad, s - pad), color, w)
    d.line([(pad, pad * 3.4), (s - pad, pad * 3.4)], fill=color, width=w)
    f = font(F_MONO_B, int(s * 0.30))
    d.text((s * 0.18, s * 0.62), ">_", font=f, fill=color, anchor="lm")
    return img


def glyph_spark(box, color=ACCENT, w=None):
    """Sparkline on a baseline — general."""
    x0, y0, x1, y1 = box
    s = x1 - x0
    w = w or max(3, int(s * 0.055))
    img = Image.new("RGBA", (int(s), int(s)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = s * 0.10
    base = s - pad
    d.line([(pad, base), (s - pad, base)], fill=color, width=w)
    frac = [(0.05, 0.62), (0.25, 0.50), (0.45, 0.68), (0.65, 0.38), (0.82, 0.46), (0.95, 0.22)]
    pts = [(pad + fx * (s - 2 * pad), base - fy * (s - 2 * pad) * 0.9) for fx, fy in frac]
    d.line(pts, fill=color, width=w, joint="curve")
    r = w * 1.1
    d.ellipse([pts[-1][0] - r, pts[-1][1] - r, pts[-1][0] + r, pts[-1][1] + r], fill=color)
    return img


GLYPHS = {
    "stats": ("STATS & PROBA", glyph_bell),
    "finance": ("FINANCE", glyph_candles),
    "math": ("MATH", glyph_integral),
    "ai": ("AI & ML", glyph_nodes),
    "dev": ("DEV & WEB", glyph_terminal),
    "notes": ("NOTES", glyph_spark),
}


# ─── Domain mapping from title + categories ──────────────────────────

DOMAIN_KEYWORDS = [
    ("finance", ["finance", "financial", "interest", "banque", "market", "marché",
                 "prix", "price", "électric", "electric", "bourse", "invest", "taux"]),
    ("ai", ["ai", "artificial intelligence", "intelligence", "learning", "statistic",
            "machine", "deep", "perceptron", "neural", "agent", "prompt", "token",
            "giskard", "model", "skill", "context", "llm"]),
    ("math", ["bessel", "math", "calculus", "mathematic", "proof", "theorem", "équation"]),
    ("dev", ["quarto", "github", "codespace", "web", "posse", "indieweb", "readme",
             "bash", "homelab", "home lab", "dev", "spec", "blog"]),
]


def domain_of(title, categories):
    text = ((title or "") + " " + " ".join(categories or [])).lower()
    for key, kws in DOMAIN_KEYWORDS:
        if any(k in text for k in kws):
            return key
    return "notes"


# ─── Text helpers ────────────────────────────────────────────────────

def spaced_text(d, xy, s, f, fill, spacing):
    x, y = xy
    for ch in s:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + spacing


def wrap(d, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ─── Composite images ────────────────────────────────────────────────

def make_favicon(size, path):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(size * 0.22)
    d.rounded_rectangle([1, 1, size - 2, size - 2], radius=r, fill=SURFACE,
                        outline=BORDER_STRONG, width=max(2, size // 32))
    mark = draw_mark(int(size * 0.78))
    img.paste(mark, ((size - mark.width) // 2, int(size * 0.10)), mark)
    img.save(path)


def make_og_image(path):
    W, H = 1920, 1440
    img = Image.new("RGB", (W, H), SURFACE)
    d = ImageDraw.Draw(img)
    m = 56
    d.rounded_rectangle([m, m, W - m, H - m], radius=44, outline=BORDER, width=5)
    mark = draw_mark(560)
    img.paste(mark, ((W - mark.width) // 2, int(H * 0.22)), mark)
    d = ImageDraw.Draw(img)
    d.text((W / 2, H * 0.60), "Guillaume Gilles", font=font(F_SANS_B, 128),
           fill=INK_STRONG, anchor="mm")
    d.text((W / 2, H * 0.71), "ggilles.dev  ·  math · finance · data · AI",
           font=font(F_MONO, 52), fill=ACCENT, anchor="mm")
    img.save(path, "JPEG", quality=92)


def make_thumbnail(slug, title, domain, path):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), SURFACE)
    d = ImageDraw.Draw(img)
    m = 30
    d.rounded_rectangle([m, m, W - m, H - m], radius=26, outline=BORDER, width=3)

    label, glyph_fn = GLYPHS[domain]
    f_lab = font(F_MONO, 30)
    spaced_text(d, (72, 62), label, f_lab, INK_DIM, spacing=5)

    # glyph on the right, vertically centered
    gs = 330
    gx, gy = W - 72 - gs, (H - gs) // 2
    g = glyph_fn((0, 0, gs, gs))
    img.paste(g, (gx, gy), g)

    # title bottom-left, wrapped
    f_t = font(F_SANS_B, 56)
    lines = wrap(d, title, f_t, 760)[:3]
    if len(lines) == 3 and d.textlength(" ".join(title.split()), font=f_t) > 760:
        lines[2] = lines[2].rstrip(".,;: ") + "…"
    lh = 68
    y = H - 70 - lh * len(lines)
    for line in lines:
        d.text((72, y), line, font=f_t, fill=INK_STRONG)
        y += lh

    # small mark bottom-right
    mark = draw_mark(92)
    img.paste(mark, (W - 72 - 92, H - 70 - 92), mark)
    img.save(path, "PNG")


# ─── Post scanning + front matter injection ──────────────────────────

def front_matter(text):
    # newline-agnostic so CRLF files keep their original line endings
    return re.match(r"^(---\r?\n)(.*?)(\r?\n---\r?\n)", text, re.S)


def main():
    os.makedirs(BRAND, exist_ok=True)
    os.makedirs(POSTS_IMG, exist_ok=True)

    # core brand files
    draw_mark(1024).save(os.path.join(BRAND, "mark.png"))
    make_favicon(64, os.path.join(BRAND, "favicon.png"))
    make_favicon(180, os.path.join(BRAND, "apple-touch-icon.png"))
    for key, (_, fn) in GLYPHS.items():
        fn((0, 0, 512, 512)).save(os.path.join(BRAND, f"glyph-{key}.png"))
    make_og_image(os.path.join(ROOT, "assets", "og-image.jpg"))
    print("brand kit -> assets/brand/, assets/og-image.jpg")

    files = sorted(glob.glob(os.path.join(ROOT, "posts", "*", "index.qmd"))
                   + glob.glob(os.path.join(ROOT, "posts", "*.qmd")))
    for f in files:
        with open(f, encoding="utf-8", newline="") as fh:
            text = fh.read()
        m = front_matter(text)
        if not m:
            print(f"  skip (no front matter): {f}")
            continue
        nl = "\r\n" if "\r\n" in m.group(1) else "\n"
        block = m.group(2)
        fm = yaml.safe_load(block) or {}
        slug = os.path.basename(os.path.dirname(f)) if os.path.basename(f) == "index.qmd" \
            else os.path.splitext(os.path.basename(f))[0]
        if fm.get("image") or re.search(r"(?m)^image:", block):
            print(f"  keep existing image: {slug} ({fm.get('image')})")
            continue
        title = fm.get("title") or slug.replace("-", " ").title()
        domain = domain_of(fm.get("title"), fm.get("categories"))
        out = os.path.join(POSTS_IMG, f"{slug}.png")
        make_thumbnail(slug, title, domain, out)
        rel = f"assets/posts/{slug}.png"
        new_block, n = re.subn(r"(?m)^(title:[^\r\n]*)(\r?\n)",
                               lambda mm: mm.group(1) + mm.group(2) + "image: " + rel + mm.group(2),
                               block, count=1)
        if n == 0:  # no title line, append at end of front matter
            new_block = block + nl + "image: " + rel
        with open(f, "w", encoding="utf-8", newline="") as fh:
            fh.write(text[:m.start(2)] + new_block + text[m.end(2):])
        print(f"  thumbnail: {slug} [{GLYPHS[domain][0]}] -> {rel}")


if __name__ == "__main__":
    main()
