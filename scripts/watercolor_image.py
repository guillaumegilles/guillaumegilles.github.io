#!/usr/bin/env python3
"""Generate a watercolor-style building illustration in the site palette.

Simulated watercolor on paper: layered translucent washes with jittered
edges, edge pooling (darkened rims), granulation, and a paper grain.
Output: assets/brand/watercolor-building.jpg (1200x630, like post cards).

    .venv/bin/python scripts/watercolor_image.py
"""
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.ndimage import gaussian_filter

ROOT = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if "__file__" in globals() else os.getcwd())
OUT = os.path.join(ROOT, "assets", "brand", "watercolor-building.jpg")

W, H = 1200, 630

# Palette — mirror of assets/custom.scss
SURFACE = np.array([250, 249, 245], dtype=float)       # #FAF9F5 paper
ACCENT = np.array([47, 93, 138], dtype=float)          # #2F5D8A steel blue
AMBER = np.array([183, 121, 31], dtype=float)          # #B7791F
INK_DIM = np.array([107, 107, 116], dtype=float)       # #6B6B74
BORDER_STRONG = np.array([203, 199, 185], dtype=float) # #CBC7B9

rng = np.random.default_rng(20260623)


def paper_base():
    """Paper background with smooth tonal variation + fine grain."""
    img = np.zeros((H, W, 3))
    img[:] = SURFACE
    # broad tonal clouds
    for scale, amp in [(90, 5.0), (28, 2.5), (7, 1.2)]:
        n = gaussian_filter(rng.standard_normal((H, W)), sigma=scale) * amp
        for c in range(3):
            img[:, :, c] += n
    return img


def wash(canvas, poly_pts, color, alpha, passes=7, jitter=2.5, blur=1.6):
    """Layered translucent fill with irregular edges + granulation."""
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    for _ in range(passes):
        pts = [(x + rng.uniform(-jitter, jitter), y + rng.uniform(-jitter, jitter))
               for x, y in poly_pts]
        d.polygon(pts, fill=255)
    mask = np.asarray(layer, dtype=float) / 255.0
    mask = gaussian_filter(mask, sigma=blur)
    # granulation: mottled darker/lighter patches inside the wash
    gran = (gaussian_filter(rng.standard_normal((H, W)), sigma=14) * 0.35
            + gaussian_filter(rng.standard_normal((H, W)), sigma=1.2) * 0.65)
    a = np.clip(mask * alpha * (1.0 + gran * 0.45), 0, 1)[..., None]
    return canvas * (1 - a) + color * a  # composite wash


def edge_pooling(canvas, poly_pts, color, strength=0.5, blur=1.2, rim=5.0):
    """Darkened rim where the wash dries — classic watercolor edge."""
    layer = Image.new("L", (W, H), 0)
    ImageDraw.Draw(layer).polygon(poly_pts, fill=255)
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=blur)
    edge = np.clip(mask - gaussian_filter(mask, sigma=rim), 0, 1)
    a = np.clip(edge * strength, 0, 1)[..., None]
    return canvas * (1 - a) + color * a


def soft_rect(canvas, box, color, alpha, blur=2.0, passes=4, jitter=1.5):
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = box
    for _ in range(passes):
        d.rounded_rectangle(
            [x0 + rng.uniform(-jitter, jitter), y0 + rng.uniform(-jitter, jitter),
             x1 + rng.uniform(-jitter, jitter), y1 + rng.uniform(-jitter, jitter)],
            radius=(x1 - x0) * 0.15, fill=255)
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=blur)
    a = np.clip(mask * alpha, 0, 1)[..., None]
    return canvas * (1 - a) + color * a


def main():
    img = paper_base()

    # sky: faint cool gradient from the top
    grad = np.linspace(1.0, 0.0, H) ** 1.6
    sky = (grad * 0.14)[:, None, None]
    img = img * (1 - sky) + ACCENT * sky

    # pale sun, top right
    sun = soft_rect(img, (905, 75, 1005, 175), AMBER, 0.30, blur=18, passes=8, jitter=6)
    img = sun
    core = soft_rect(img, (935, 105, 975, 145), AMBER, 0.35, blur=8, passes=6, jitter=4)
    img = core

    # ── buildings (back to front) ────────────────────────────────
    left_bld = [(235, 320), (430, 305), (430, H), (235, H)]
    right_bld = [(725, 270), (905, 285), (905, H), (725, H)]
    main_bld = [(415, 185), (725, 185), (725, H), (415, H)]

    blue_gray = (ACCENT * 0.55 + INK_DIM * 0.45)
    light_blue = (ACCENT * 0.55 + SURFACE * 0.45)

    img = wash(img, left_bld, blue_gray, 0.50)
    img = edge_pooling(img, left_bld, INK_DIM * 0.8, 0.45)

    img = wash(img, right_bld, light_blue, 0.55)
    img = edge_pooling(img, right_bld, ACCENT * 0.8, 0.4)

    img = wash(img, main_bld, ACCENT, 0.62, passes=9, jitter=3.0, blur=1.8)
    img = edge_pooling(img, main_bld, ACCENT * 0.55, 0.55, rim=6.0)

    # roof details: penthouse box + antenna with signal arcs
    img = wash(img, [(470, 150), (610, 150), (610, 185), (470, 185)], ACCENT * 0.8, 0.7)
    d = ImageDraw.Draw(Image.fromarray(img.astype(np.uint8)))
    ant_x, ant_top = 640, 105
    d.line([(ant_x, 185), (ant_x, ant_top)], fill=tuple((ACCENT * 0.7).astype(int)), width=4)
    for r, al in [(22, 0.55), (38, 0.35), (54, 0.2)]:
        arc = Image.new("L", (W, H), 0)
        ImageDraw.Draw(arc).arc([ant_x - r, ant_top - r, ant_x + r, ant_top + r],
                                start=-60, end=60, fill=255, width=4)
        m = gaussian_filter(np.asarray(arc, dtype=float) / 255.0, sigma=1.5) * al
        img = img * (1 - m[..., None]) + ACCENT * m[..., None]

    # windows on the main tower: paper-colored cutouts, a few darker
    cols, rows = 6, 9
    x0, x1 = 445, 695
    y0, y1 = 215, 600
    for i in range(cols):
        for j in range(rows):
            wx0 = x0 + i * (x1 - x0) / cols + 7
            wx1 = x0 + (i + 1) * (x1 - x0) / cols - 7
            wy0 = y0 + j * (y1 - y0) / rows + 6
            wy1 = y0 + (j + 1) * (y1 - y0) / rows - 6
            if rng.random() < 0.18:
                img = soft_rect(img, (wx0, wy0, wx1, wy1), INK_DIM, 0.45, blur=1.2, passes=2)
            else:
                img = soft_rect(img, (wx0, wy0, wx1, wy1), SURFACE, 0.85, blur=1.0, passes=3)

    # a few windows on the side buildings
    for bx0, bx1, by0, by1, n in [(255, 410, 340, 600, 8), (745, 885, 300, 600, 8)]:
        for _ in range(n):
            wx0 = rng.uniform(bx0, bx1 - 30)
            wy0 = rng.uniform(by0, by1 - 34)
            img = soft_rect(img, (wx0, wy0, wx0 + 22, wy0 + 26), SURFACE, 0.6, blur=1.2, passes=2)

    # door
    img = soft_rect(img, (545, 560, 595, H), SURFACE, 0.9, blur=1.5, passes=4)

    # ground wash + horizon stroke
    ground = Image.new("L", (W, H), 0)
    ImageDraw.Draw(ground).rectangle([0, 596, W, H], fill=255)
    gm = gaussian_filter(np.asarray(ground, dtype=float) / 255.0, sigma=6)
    img = img * (1 - gm[..., None] * 0.25) + BORDER_STRONG * (gm[..., None] * 0.25)
    stroke = Image.new("L", (W, H), 0)
    ImageDraw.Draw(stroke).line([(0, 598), (W, 594)], fill=255, width=3)
    sm = gaussian_filter(np.asarray(stroke, dtype=float) / 255.0, sigma=1.5)
    img = img * (1 - sm[..., None] * 0.5) + INK_DIM * (sm[..., None] * 0.5)

    # final paper grain over everything
    grain = gaussian_filter(rng.standard_normal((H, W)), sigma=0.8) * 2.2
    img += grain[..., None]

    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")
    out = out.filter(ImageFilter.UnsharpMask(radius=1, percent=30, threshold=3))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.save(OUT, "JPEG", quality=92)
    print("wrote", OUT, out.size)


if __name__ == "__main__":
    main()
