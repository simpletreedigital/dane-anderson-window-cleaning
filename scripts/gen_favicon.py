"""Render the A-frame peeling wave logo mark as a favicon / app icon PNG.
Drawn at 4x supersample then downsampled for clean anti-aliasing (no SVG rasterizer available)."""
from PIL import Image, ImageDraw
import math

SCALE = 4
SIZE = 512 * SCALE

NAVY = (11, 61, 92, 255)
SKY = (79, 184, 214, 255)
WHITE = (255, 255, 255, 255)
CORAL = (255, 107, 74, 255)

def pt(x, y):
    return (x * SCALE, y * SIZE // 512 // SCALE * SCALE) if False else (x * SCALE, y * SCALE)

def bezier_points(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts

def path_to_polygon(segments):
    poly = []
    cur = segments[0]
    poly.append(cur)
    for seg in segments[1:]:
        kind = seg[0]
        if kind == 'L':
            cur = seg[1]
            poly.append(cur)
        elif kind == 'C':
            pts = bezier_points(cur, seg[1], seg[2], seg[3])
            poly.extend(pts[1:])
            cur = seg[3]
    return poly

img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

cx, cy, r = 256, 256, 240

def S(x, y):
    return (x * SCALE, y * SCALE)

# Background circle badge
draw.ellipse([S(cx - r, cy - r), S(cx + r, cy + r)], fill=NAVY)

# Small coral "sun" accent, upper left, partially behind wave
draw.ellipse([S(150, 120), S(210, 180)], fill=CORAL)

# A-frame peeling wave body (sky blue), coordinates in 0-512 icon space
wave_segments = [
    (40, 400),
    ('C', (95, 300), (150, 190), (235, 105)),
    ('C', (265, 78), (315, 60), (345, 92)),
    ('C', (368, 118), (345, 148), (300, 142)),
    ('C', (268, 138), (248, 168), (282, 200)),
    ('C', (345, 260), (420, 330), (462, 400)),
    ('L', (40, 400)),
]
wave_poly = path_to_polygon(wave_segments)
wave_poly_s = [S(x, y) for (x, y) in wave_poly]
draw.polygon(wave_poly_s, fill=SKY)

# Darker navy shading along the trough (right underside of the curl) for depth
shade_segments = [
    (300, 142),
    ('C', (268, 138), (248, 168), (282, 200)),
    ('C', (345, 260), (420, 330), (462, 400)),
    ('L', (400, 400)),
    ('C', (365, 320), (310, 255), (262, 205)),
    ('C', (245, 178), (262, 152), (300, 142)),
]
shade_poly = [S(x, y) for (x, y) in path_to_polygon(shade_segments)]
draw.polygon(shade_poly, fill=(8, 46, 69, 255))

# White foam lip curling over the peak
foam_segments = [
    (235, 105),
    ('C', (265, 78), (315, 60), (345, 92)),
    ('C', (368, 118), (345, 148), (300, 142)),
    ('C', (280, 139), (262, 132), (250, 118)),
    ('C', (243, 110), (238, 108), (235, 105)),
]
foam_poly = [S(x, y) for (x, y) in path_to_polygon(foam_segments)]
draw.polygon(foam_poly, fill=WHITE)

# A few foam droplets flicking off the lip
for (fx, fy, fr) in [(360, 105, 9), (378, 128, 6), (352, 145, 5)]:
    draw.ellipse([S(fx - fr, fy - fr), S(fx + fr, fy + fr)], fill=WHITE)

# Downsample for clean anti-aliasing
final = img.resize((512, 512), Image.LANCZOS)
final.save("/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/images/logos/dane-anderson-wave-icon.png")

for size in (512, 192, 64, 32):
    final.resize((size, size), Image.LANCZOS).save(
        f"/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/images/favicon-{size}.png"
        if size != 64 else
        "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/images/favicon.png"
    )

print("wrote favicon.png + favicon-{512,192,32}.png + logos/dane-anderson-wave-icon.png")
