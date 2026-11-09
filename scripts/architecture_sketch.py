#!/usr/bin/env python3
"""Generate an architectural pen-sketch with watercolor washes, in the style
of illustrarch-style concept sketches, but in the ggilles.dev palette.

Technique: loose multi-pass ink strokes with overshoot at corners, faint
construction lines, diagonal hatching + scribble shading on dark faces,
warm amber wash on sunlit surfaces, cool steel-blue wash on glass/shadow,
paper grain. Output: assets/brand/architecture-sketch.jpg (1200x630).

    .venv/bin/python scripts/architecture_sketch.py
"""
import math
import os

import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter

ROOT = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if "__file__" in globals() else os.getcwd())
OUT = os.path.join(ROOT, "assets", "brand", "architecture-sketch.jpg")

W, H = 1200, 630

# Palette — paper white + brand accents
PAPER = np.array([253, 252, 248], dtype=float)
INK = np.array([52, 52, 60], dtype=float)          # soft black pen
INK_FAINT = np.array([150, 150, 158], dtype=float)  # pencil construction
ACCENT = np.array([47, 93, 138], dtype=float)       # steel blue wash
AMBER = np.array([183, 121, 31], dtype=float)      # warm sun wash
GRAY = np.array([120, 122, 130], dtype=float)       # neutral wash
GREEN = np.array([46, 125, 79], dtype=float)       # tree wash

rng = np.random.default_rng(20260623)


# ─── low-level helpers ───────────────────────────────────────────────

def new_canvas():
    img = np.zeros((H, W, 3))
    img[:] = PAPER
    grain = gaussian_filter(rng.standard_normal((H, W)), sigma=60) * 3.0
    fine = gaussian_filter(rng.standard_normal((H, W)), sigma=0.8) * 1.6
    for c in range(3):
        img[:, :, c] += grain + fine
    return img


def poly_mask(poly, blur=1.0):
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(list(poly), fill=255)
    return gaussian_filter(np.asarray(m, dtype=float) / 255.0, sigma=blur)


def composite(canvas, mask, color, alpha):
    a = np.clip(mask * alpha, 0, 1)[..., None]
    return canvas * (1 - a) + color * a


def wash(canvas, poly, color, alpha, blur=2.5, passes=5, jitter=2.0):
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    for _ in range(passes):
        pts = [(x + rng.uniform(-jitter, jitter), y + rng.uniform(-jitter, jitter))
               for x, y in poly]
        d.polygon(pts, fill=255)
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=blur)
    gran = gaussian_filter(rng.standard_normal((H, W)), sigma=10) * 0.5
    return composite(canvas, mask * (1 + gran * 0.3), color, alpha)


def _stroke_pts(p0, p1, jitter, overshoot):
    """Subdivided jittered polyline with random overshoot past both ends."""
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy) or 1.0
    ux, uy = dx / length, dy / length
    o0 = rng.uniform(0, overshoot)
    o1 = rng.uniform(0, overshoot)
    n = max(2, int(length / 14))
    pts = []
    for i in range(n + 1):
        t = i / n
        px = x0 + dx * t - ux * o0
        py = y0 + dy * t - uy * o0
        if 0 < i < n:
            px += rng.uniform(-jitter, jitter)
            py += rng.uniform(-jitter, jitter)
        pts.append((px, py))
    last = (x1 + ux * o1, y1 + uy * o1)
    pts[-1] = last
    return pts


def ink_line(canvas, p0, p1, color=INK, alpha=0.8, width=2, passes=3,
             jitter=1.2, overshoot=7.0):
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    for _ in range(passes):
        pts = _stroke_pts(p0, p1, jitter, overshoot)
        w = max(1, int(width + rng.uniform(-0.8, 0.8)))
        d.line(pts, fill=255, width=w, joint="curve")
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=0.5)
    return composite(canvas, mask, color, alpha)


def ink_curve(canvas, pts, color=INK, alpha=0.8, width=2, passes=3, jitter=1.2):
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    for _ in range(passes):
        jpts = [(x + rng.uniform(-jitter, jitter), y + rng.uniform(-jitter, jitter))
                for x, y in pts]
        d.line(jpts, fill=255, width=max(1, int(width)), joint="curve")
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=0.5)
    return composite(canvas, mask, color, alpha)


def hatch(canvas, poly, angle_deg, spacing, color=INK, alpha=0.5, width=1,
          jitter=1.0, length_jitter=0.25):
    """Diagonal hatching clipped to a polygon."""
    mask = poly_mask(poly, blur=0.8)
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    ang = math.radians(angle_deg)
    dx, dy = math.cos(ang), math.sin(ang)
    px, py = -math.sin(ang), math.cos(ang)
    cx = W / 2
    cy = H / 2
    diag = math.hypot(W, H)
    n = int(diag / spacing)
    for i in range(-n, n):
        ox, oy = cx + px * i * spacing, cy + py * i * spacing
        L = diag * (1 - abs(rng.uniform(0, length_jitter)))
        p0 = (ox - dx * L / 2 + rng.uniform(-jitter, jitter),
              oy - dy * L / 2 + rng.uniform(-jitter, jitter))
        p1 = (ox + dx * L / 2 + rng.uniform(-jitter, jitter),
              oy + dy * L / 2 + rng.uniform(-jitter, jitter))
        d.line([p0, p1], fill=255, width=width)
    h = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=0.4)
    return composite(canvas, h * mask, color, alpha)


def scribble_shade(canvas, poly, color=INK, alpha=0.55, n=260, seg=26):
    """Random short strokes inside a polygon — dense pen scribble."""
    mask = poly_mask(poly, blur=0.8)
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    for _ in range(n):
        x = rng.uniform(min(xs), max(xs))
        y = rng.uniform(min(ys), max(ys))
        if mask[int(y), int(x)] < 0.4:
            continue
        a = rng.uniform(0, 2 * math.pi)
        L = rng.uniform(seg * 0.3, seg)
        d.line([(x, y), (x + math.cos(a) * L, y + math.sin(a) * L)],
               fill=255, width=1)
    s = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=0.5)
    return composite(canvas, s * mask, color, alpha)


def pencil_line(canvas, p0, p1, alpha=0.16):
    return ink_line(canvas, p0, p1, color=INK_FAINT, alpha=alpha, width=1,
                    passes=1, jitter=2.5, overshoot=0)


def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def tree(canvas, x, ground_y, scale=1.0):
    top = ground_y - 90 * scale
    canvas = ink_line(canvas, (x, ground_y), (x + rng.uniform(-4, 4), top),
                      alpha=0.7, width=2, passes=2, overshoot=2)
    # scribble foliage: overlapping jittered loops
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    cx, cy, r = x, top - 22 * scale, 34 * scale
    for _ in range(9):
        rr = r * rng.uniform(0.7, 1.15)
        bbox = [cx - rr + rng.uniform(-6, 6), cy - rr * 0.8 + rng.uniform(-6, 6),
                cx + rr + rng.uniform(-6, 6), cy + rr * 0.8 + rng.uniform(-6, 6)]
        d.arc(bbox, start=rng.uniform(0, 180), end=rng.uniform(180, 360),
              fill=255, width=2)
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=0.6)
    canvas = composite(canvas, mask, INK, 0.55)
    blob = [(cx - r, cy - r * 0.8), (cx + r, cy - r * 0.8), (cx + r, cy + r * 0.8), (cx - r, cy + r * 0.8)]
    canvas = wash(canvas, blob, GREEN, 0.16, blur=6, passes=3, jitter=5)
    return canvas


def figure(canvas, x, ground_y, s=1.0):
    h = 26 * s
    canvas = ink_curve(canvas, [(x, ground_y - h * 0.72), (x + rng.uniform(-1, 1), ground_y - h * 0.68)],
                       alpha=0.75, width=2, passes=2, jitter=0.8)
    ImageDraw  # noqa
    layer = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(layer)
    d.ellipse([x - 3 * s, ground_y - h - 3 * s, x + 3 * s, ground_y - h + 3 * s], outline=255, width=2)
    mask = gaussian_filter(np.asarray(layer, dtype=float) / 255.0, sigma=0.5)
    canvas = composite(canvas, mask, INK, 0.75)
    canvas = ink_line(canvas, (x, ground_y - h * 0.7), (x + rng.uniform(-1, 1), ground_y - h * 0.25),
                      alpha=0.75, width=2, passes=2, overshoot=1)
    canvas = ink_line(canvas, (x, ground_y - h * 0.25), (x - 4 * s, ground_y), alpha=0.75, width=2, passes=2, overshoot=1)
    canvas = ink_line(canvas, (x, ground_y - h * 0.25), (x + 4 * s, ground_y), alpha=0.75, width=2, passes=2, overshoot=1)
    return canvas


# ─── the sketch ──────────────────────────────────────────────────────

def main():
    img = new_canvas()

    # faint construction lines (long pencil strokes across the scene)
    img = pencil_line(img, (120, 250), (1120, 195))
    img = pencil_line(img, (90, 420), (1140, 385))
    img = pencil_line(img, (330, 120), (330, 600))
    img = pencil_line(img, (930, 120), (930, 590))
    img = pencil_line(img, (200, 560), (1050, 520))

    # ── building geometry ──
    # lower volume: front face + right side face
    A = (300, 395)   # lower-left front
    B = (840, 365)   # lower-right front (corner)
    C = (840, 505)   # bottom-right front
    D = (300, 535)   # bottom-left front
    E = (1010, 320)  # back-right top of side face
    F = (1010, 460)  # back-right bottom
    # upper volume: cantilevered slab with gently curved top
    U0 = (390, 235)          # upper-left front
    U1 = (960, 205)          # upper-right front
    V1 = (1080, 165)         # back-right top (side face)
    V0 = (520, 175)          # back-left top
    # curve control for the top front edge
    ctrl = (675, 150)
    top_front = bezier(U0, ctrl, U1, 36)
    top_back = bezier(V0, (800, 120), V1, 36)
    bot_front = bezier((390, 330), (675, 305), (960, 300), 36)   # underside front edge
    side_bot = [(960, 300), (1080, 258)]
    side_top = [(U1[0], U1[1]), (V1[0], V1[1])]

    ground = 560

    # ground shadow wash (soft, to the lower right)
    shadow_poly = [(300, 535), (840, 505), (1120, 500), (1150, 545),
                   (900, 585), (420, 600)]
    img = wash(img, shadow_poly, GRAY, 0.30, blur=8, passes=4, jitter=6)
    img = wash(img, shadow_poly, ACCENT, 0.10, blur=10, passes=3, jitter=8)

    # ground perspective lines
    for x0 in range(80, 1180, 130):
        img = pencil_line(img, (x0, 630), (x0 + 260, ground - 30), alpha=0.10)
    for yy in [ground - 8, ground + 8, ground + 24, ground + 46]:
        img = pencil_line(img, (60, yy + 6), (1160, yy - 14), alpha=0.13)

    # ── washes: sunlit warm faces, cool glass/shadow faces ──
    lower_front = [A, B, C, D]
    lower_side = [B, E, F, C]
    upper_front = top_front + [(960, 300), (390, 330)]
    upper_side = side_top + [(1080, 258), (960, 300)]
    img = wash(img, lower_front, AMBER, 0.16, blur=3, passes=5, jitter=2.5)
    img = wash(img, lower_side, ACCENT, 0.22, blur=3, passes=5, jitter=2.5)
    img = wash(img, upper_front, ACCENT, 0.30, blur=3, passes=6, jitter=2.5)   # glass band
    img = wash(img, upper_side, INK_FAINT, 0.25, blur=3, passes=5, jitter=2.5)

    # roof slab of lower volume (warm concrete)
    roof = [A, B, E, (460, 360)]
    img = wash(img, roof, AMBER, 0.28, blur=2.5, passes=5, jitter=2)
    # underside of cantilever (dark)
    img = wash(img, [(390, 330), (960, 300), (1080, 258), (520, 292)], GRAY, 0.45,
               blur=3, passes=5, jitter=2.5)

    # ── hatching: shaded side faces, under-cantilever, entrance ──
    img = hatch(img, lower_side, 115, 7, alpha=0.35)
    img = hatch(img, upper_side, 115, 6, alpha=0.4)
    img = scribble_shade(img, [(960, 300), (1080, 258), (1080, 330), (960, 360)],
                         alpha=0.5, n=180)
    img = hatch(img, [(390, 330), (960, 300), (1080, 258), (520, 292)], 100, 5,
                color=INK, alpha=0.5)

    # entrance: dark opening + steps
    door = [(560, 420), (760, 408), (760, 505), (560, 515)]
    img = wash(img, door, INK, 0.55, blur=2, passes=4, jitter=1.5)
    img = scribble_shade(img, door, alpha=0.5, n=200, seg=20)
    for i in range(1, 6):
        y0 = 515 + i * 9
        img = ink_line(img, (545 - i * 6, y0), (775 + i * 6, y0 - i * 2),
                       alpha=0.6, width=2, passes=2, overshoot=4, jitter=1.5)

    # ── ink outlines (loose, overshooting) ──
    for p0, p1 in [(A, B), (B, C), (C, D), (D, A),      # lower front
                   (B, E), (E, F), (F, C),                # lower side
                   (A, (460, 360)), ((460, 360), E),     # roof
                   (B, (840, 340))]:
        img = ink_line(img, p0, p1, alpha=0.85, width=2.4, passes=3, overshoot=9)
    img = ink_curve(img, top_front, alpha=0.9, width=2.6, passes=3, jitter=1.4)
    img = ink_curve(img, top_back, color=INK_FAINT, alpha=0.4, width=1.6, passes=2, jitter=1.6)
    img = ink_curve(img, bot_front, alpha=0.85, width=2.4, passes=3, jitter=1.4)
    for p0, p1 in [((390, 235), (390, 330)), ((960, 205), (960, 300)),
                   ((1080, 165), (1080, 258)), side_bot[0:1] + side_bot[1:2],
                   (U1, V1), (V1, (1080, 258))]:
        img = ink_line(img, p0, p1, alpha=0.85, width=2.4, passes=3, overshoot=8)

    # glass mullions on upper front band
    for i in range(1, 22):
        t = i / 22
        x = 390 + (960 - 390) * t
        y_top = top_front[int(t * 36)][1]
        y_bot = bot_front[int(t * 36)][1]
        img = ink_line(img, (x, y_top + 2), (x + 6 * (1 - t), y_bot - 2),
                       color=INK, alpha=0.45, width=1.4, passes=1, jitter=1.0, overshoot=2)
    # a couple of reflection strokes on the glass
    img = ink_line(img, (450, 260), (700, 240), color=PAPER, alpha=0.5, width=3, passes=2, jitter=2, overshoot=10)
    img = ink_line(img, (560, 315), (880, 290), color=PAPER, alpha=0.4, width=2, passes=2, jitter=2, overshoot=10)

    # columns under the cantilever
    for cx in [880, 950, 1020]:
        img = ink_line(img, (cx, 300 + (cx - 960) * -0.2), (cx + 8, ground - 6),
                       alpha=0.8, width=2.2, passes=2, overshoot=5)
    # column shadows
    img = hatch(img, [(860, 505), (1060, 490), (1120, 540), (900, 560)], 60, 9,
                color=GRAY, alpha=0.3)

    # window grid on lower front
    for i in range(1, 10):
        t = i / 10
        x = 300 + (840 - 300) * t
        y_top = 395 + (365 - 395) * t
        y_bot = 535 + (505 - 535) * t
        img = ink_line(img, (x, y_top + 14), (x, 415 + (395 - 415) * t),
                       alpha=0.35, width=1.2, passes=1, jitter=1.0, overshoot=1)
    img = ink_line(img, (310, 415), (835, 386), alpha=0.4, width=1.4, passes=2, overshoot=6)

    # ── surroundings ──
    img = tree(img, 190, ground, 1.15)
    img = tree(img, 245, ground + 4, 0.8)
    img = tree(img, 1120, ground - 4, 0.9)
    img = figure(img, 700, 545, 1.0)
    img = figure(img, 735, 548, 0.85)
    # birds
    for bx, by in [(180, 120), (230, 100), (285, 130)]:
        img = ink_curve(img, [(bx - 7, by), (bx, by - 4), (bx + 7, by)],
                        alpha=0.6, width=1.6, passes=1, jitter=0.7)
    # cloud scribbles
    for cx, cy, s in [(880, 80, 1.0), (150, 200, 0.7)]:
        img = ink_curve(img,
                        bezier((cx - 60 * s, cy), (cx, cy - 22 * s), (cx + 60 * s, cy), 16),
                        color=INK_FAINT, alpha=0.3, width=1.4, passes=2, jitter=2)

    # signature scribble, bottom right
    sig = bezier((1085, 600), (1105, 585), (1150, 598), 14)
    img = ink_curve(img, sig, alpha=0.7, width=1.8, passes=2, jitter=1.0)
    img = ink_curve(img, bezier((1100, 605), (1125, 590), (1160, 603), 12),
                    alpha=0.5, width=1.4, passes=1, jitter=1.2)

    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.save(OUT, "JPEG", quality=92)
    print("wrote", OUT, out.size)


if __name__ == "__main__":
    main()
