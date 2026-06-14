#!/usr/bin/env python3
"""Render a Fangye vertical steps card from a JSON spec."""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


W = 1080
BG = (250, 249, 245)
DARK = (37, 62, 47)
MUTED = (108, 123, 109)
GREEN = (110, 145, 112)
LIGHT_GREEN = (232, 241, 231)
LINE = (190, 214, 190)
ORANGE = (219, 120, 39)


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
    ]
    index = 0 if weight == "regular" else 1
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size, index=index)
    return ImageFont.load_default()


def wrap_cn(text: str, width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines():
        if not paragraph:
            lines.append("")
            continue
        lines.extend(textwrap.wrap(paragraph, width=width, break_long_words=True, replace_whitespace=False))
    return lines


def rounded(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], radius: int, outline=None, fill=None, width: int = 2):
    draw.rounded_rectangle(xy, radius=radius, outline=outline, fill=fill, width=width)


def render(spec: dict, out: Path) -> None:
    steps = spec.get("steps", [])
    card_h = int(spec.get("card_height", 178))
    gap = int(spec.get("gap", 58))
    top = 74
    first_card_y = 360
    bottom = 130
    height = first_card_y + len(steps) * card_h + max(0, len(steps) - 1) * gap + bottom
    im = Image.new("RGB", (W, height), BG)
    d = ImageDraw.Draw(im)

    title_font = font(56, "bold")
    subtitle_font = font(29)
    chip_font = font(26)
    tag_font = font(25)
    heading_font = font(36, "bold")
    body_font = font(25)
    num_font = font(30)

    d.text((78, top), spec["title"], fill=DARK, font=title_font)
    if spec.get("subtitle"):
        d.text((78, top + 76), spec["subtitle"], fill=MUTED, font=subtitle_font)

    chip_x = 78
    for idx, chip in enumerate(spec.get("chips", [])):
        color = GREEN if idx == 0 else ORANGE
        tw = d.textlength(chip, font=chip_font)
        box = (chip_x, top + 136, chip_x + int(tw) + 74, top + 196)
        rounded(d, box, 29, outline=color, fill=None, width=2)
        d.text((chip_x + 37, top + 150), chip, fill=color, font=chip_font)
        chip_x = box[2] + 84

    line_x = 155
    y = first_card_y
    for idx, step in enumerate(steps, start=1):
        if idx < len(steps):
            d.line((line_x, y + 16, line_x, y + card_h + gap - 12), fill=GREEN, width=6)
            tri_y = y + card_h + gap - 32
            d.polygon([(line_x - 17, tri_y), (line_x + 17, tri_y), (line_x, tri_y + 36)], fill=GREEN)
        d.ellipse((line_x - 34, y + 28, line_x + 34, y + 96), outline=GREEN, width=6, fill=BG)
        num = str(idx)
        nw = d.textlength(num, font=num_font)
        d.text((line_x - nw / 2, y + 43), num, fill=GREEN, font=num_font)

        card = (220, y, W - 70, y + card_h)
        rounded(d, card, 22, outline=LINE, fill=(255, 255, 252), width=2)
        tag = step.get("tag", "")
        tag_box = (254, y + 30, 404, y + 78)
        rounded(d, tag_box, 23, fill=LIGHT_GREEN)
        d.text((286, y + 39), tag, fill=GREEN, font=tag_font)
        d.text((464, y + 28), step["heading"], fill=DARK, font=heading_font)
        body_lines = wrap_cn(step.get("body", ""), 24)[:2]
        for line_i, line in enumerate(body_lines):
            d.text((464, y + 84 + line_i * 32), line, fill=MUTED, font=body_font)
        y += card_h + gap

    if spec.get("logo", True):
        cx, cy = W - 126, height - 66
        d.ellipse((cx - 14, cy - 24, cx + 14, cy + 4), fill=(139, 170, 126))
        d.ellipse((cx + 22, cy + 2, cx + 50, cy + 30), fill=(139, 170, 126))
        d.line((cx - 3, cy + 28, cx + 41, cy - 18), fill=(105, 136, 101), width=5)

    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=95)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", help="Path to JSON spec")
    parser.add_argument("-o", "--output", required=True, help="Output PNG path")
    args = parser.parse_args()
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    render(spec, Path(args.output))


if __name__ == "__main__":
    main()
