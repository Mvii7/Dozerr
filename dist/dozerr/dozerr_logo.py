# SPDX-FileCopyrightText: Copyright 2026 Dozerr contributors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Dozerr's mark: a D whose flat edge is a bulldozer blade, with speed lines, on a dark tile.

The source of dist/dozerr.ico, dist/dozerr.icns (the macOS app icon), dist/dozerr.bmp and
dist/dozerr.png (the 256 px icon the Qt theme and the About box use) and
dist/dozerr/dozerr_banner.png (the mark with the name, for the readme);
needs only Pillow:
    python dist/dozerr/dozerr_logo.py [output folder for a preview sheet]
Drawn in a unit square at 8x and scaled down, so the edges stay smooth. 16 and 24 px leave out the
speed lines (they vanish that small) and fill the tile with the D.
"""

import math
import os
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(HERE)

TILE_TOP = (52, 54, 60)
TILE_BOTTOM = (22, 23, 26)
YELLOW = (255, 196, 0)
YELLOW_DIM = (176, 134, 0)

# The D: flat left edge at x 0.30, round on the right (centre 0.44, 0.50, radius 0.30), with the
# counter cut out of it; three blade teeth on the flat edge.
D_LEFT, D_TOP, D_BOTTOM, D_ARC_START = 0.30, 0.20, 0.80, 0.44
COUNTER_LEFT, COUNTER_TOP, COUNTER_BOTTOM, COUNTER_ARC_START = 0.42, 0.34, 0.66, 0.46
TEETH_Y = (0.30, 0.50, 0.70)
TEETH_HALF_HEIGHT = 0.055
TEETH_DEPTH = 0.11
SPEED_LINES_Y = (0.38, 0.50, 0.62)


def arc(cx, cy, radius, start, end, steps=48):
    return [(cx + radius * math.cos(math.radians(start + (end - start) * i / steps)),
             cy + radius * math.sin(math.radians(start + (end - start) * i / steps)))
            for i in range(steps + 1)]


def d_polygon(left, top, bottom, arc_start):
    mid = (top + bottom) / 2
    radius = (bottom - top) / 2
    return [(left, top), (arc_start, top)] + arc(arc_start, mid, radius, -90, 90) + \
        [(arc_start, bottom), (left, bottom)]


def gradient(size, top, bottom):
    """A vertical gradient image (RGB) from top to bottom."""
    column = Image.new('RGB', (1, size))
    for y in range(size):
        t = y / max(1, size - 1)
        column.putpixel((0, y), tuple(round(a + (b - a) * t) for a, b in zip(top, bottom)))
    return column.resize((size, size))


def render(size, simple=None, tile=True):
    simple = size <= 24 if simple is None else simple
    scale = 8
    big = size * scale
    # The small sizes centre the D and make it larger: the speed lines are gone.
    zoom, shift = (1.14, 0.035) if simple else (1.0, 0.0)

    def point(p):
        return ((0.5 + (p[0] + shift - 0.5) * zoom) * big, (0.5 + (p[1] - 0.5) * zoom) * big)

    image = Image.new('RGBA', (big, big), (0, 0, 0, 0))
    if tile:
        mask = Image.new('L', (big, big), 0)
        inset = 0 if size <= 24 else round(big * 0.02)
        ImageDraw.Draw(mask).rounded_rectangle((inset, inset, big - 1 - inset, big - 1 - inset),
                                               radius=round(big * 0.22), fill=255)
        image.paste(gradient(big, TILE_TOP, TILE_BOTTOM), (0, 0), mask)
    letter = Image.new('L', (big, big), 0)
    draw = ImageDraw.Draw(letter)
    draw.polygon([point(p) for p in d_polygon(D_LEFT, D_TOP, D_BOTTOM, D_ARC_START)], fill=255)
    for y in TEETH_Y:
        draw.polygon([point((D_LEFT, y - TEETH_HALF_HEIGHT)), point((D_LEFT, y + TEETH_HALF_HEIGHT)),
                      point((D_LEFT - TEETH_DEPTH, y))], fill=255)
    draw.polygon([point(p) for p in d_polygon(COUNTER_LEFT, COUNTER_TOP, COUNTER_BOTTOM,
                                              COUNTER_ARC_START)], fill=0)
    image.paste(Image.new('RGBA', (big, big), YELLOW), (0, 0), letter)
    if not simple:
        lines = Image.new('L', (big, big), 0)
        draw = ImageDraw.Draw(lines)
        for i, y in enumerate(SPEED_LINES_Y):
            draw.rounded_rectangle((big * 0.80, big * (y - 0.012), big * (0.90 - i * 0.02),
                                    big * (y + 0.012)), radius=big * 0.012, fill=255)
        image.paste(Image.new('RGBA', (big, big), YELLOW_DIM), (0, 0), lines)
    return image.resize((size, size), Image.LANCZOS)


FONT_CANDIDATES = (
    'DejaVuSans-Bold.ttf', 'arialbd.ttf', 'Arial Bold.ttf', 'LiberationSans-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    'C:/Windows/Fonts/arialbd.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
)


def load_font(size):
    from PIL import ImageFont
    for name in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def render_banner(width=1600, height=400):
    """The mark with the name beside it, on a dark panel that reads on light and dark pages."""
    scale = 2
    w, h = width * scale, height * scale
    panel = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    gradient = Image.new('RGBA', (w, h))
    px = gradient.load()
    for y in range(h):
        t = y / (h - 1)
        color = tuple(round(TILE_TOP[i] + (TILE_BOTTOM[i] - TILE_TOP[i]) * t) for i in range(3))
        for x in range(w):
            px[x, y] = color + (255,)
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=int(h * 0.16), fill=255)
    panel.paste(gradient, (0, 0), mask)
    icon_size = int(h * 0.72)
    icon = render(256).resize((icon_size, icon_size), Image.LANCZOS)
    left = int(h * 0.14)
    panel.alpha_composite(icon, (left, (h - icon_size) // 2))
    draw = ImageDraw.Draw(panel)
    font = load_font(int(h * 0.46))
    text = 'Dozerr'
    box = draw.textbbox((0, 0), text, font=font)
    text_x = left + icon_size + int(h * 0.10)
    text_y = (h - (box[3] - box[1])) // 2 - box[1]
    draw.text((text_x, text_y), text, font=font, fill=YELLOW)
    return panel.resize((width, height), Image.LANCZOS)


def write_bmp(image, path):
    """32-bit BI_RGB bottom-up BMP with alpha in the fourth byte, like dist/eden.bmp (the CLI's
    SDL window icon, compiled in by yuzu_cmd's CMakeLists)."""
    import struct
    w, h = image.size
    rows = []
    for y in range(h - 1, -1, -1):
        row = bytearray()
        for x in range(w):
            r, g, b, a = image.getpixel((x, y))
            row += bytes((b, g, r, a))
        rows.append(bytes(row))
    pixels = b''.join(rows)
    header = struct.pack('<2sIHHI', b'BM', 54 + len(pixels), 0, 0, 54)
    info = struct.pack('<IiiHHIIiiII', 40, w, h, 1, 32, 0, len(pixels), 0, 0, 0, 0)
    with open(path, 'wb') as f:
        f.write(header + info + pixels)


def main():
    sizes = [16, 24, 32, 48, 64, 128, 256]
    frames = [render(s) for s in sizes]
    ico = os.path.join(DIST, 'dozerr.ico')
    frames[-1].save(ico, format='ICO', sizes=[(s, s) for s in sizes], append_images=frames[:-1])
    png = os.path.join(DIST, 'dozerr.png')
    render(256).save(png, optimize=True)
    bmp = os.path.join(DIST, 'dozerr.bmp')
    write_bmp(frames[-1], bmp)
    icns_frames = [render(s) for s in (16, 32, 64, 128, 256, 512)]
    icns = os.path.join(DIST, 'dozerr.icns')
    icns_frames[-1].save(icns, format='ICNS', append_images=icns_frames[:-1])
    banner = os.path.join(HERE, 'dozerr_banner.png')
    render_banner().save(banner, optimize=True)
    print(banner)
    print(icns)
    print(ico)
    print(png)
    print(bmp)
    if len(sys.argv) > 1:  # preview: every size at 1x and 4x, on light and dark
        sheet = Image.new('RGBA', (1500, 620), (240, 240, 240, 255))
        sheet.paste((32, 32, 36, 255), (0, 310, 1500, 620))
        x = 10
        for s, f in zip(sizes, frames):
            for y0 in (10, 320):
                sheet.alpha_composite(f, (x, y0))
                if s <= 64:
                    sheet.alpha_composite(f.resize((s * 4, s * 4), Image.NEAREST), (x, y0 + 270 - s * 4))
            x += max(s, s * 4 if s <= 64 else s) + 12
        out = os.path.join(sys.argv[1], 'dozerr_preview.png')
        sheet.save(out)
        print(out)


if __name__ == '__main__':
    main()
