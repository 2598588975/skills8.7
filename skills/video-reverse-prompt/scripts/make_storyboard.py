#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def load_font(size):
    candidates = [
        Path(r"C:\Windows\Fonts\msyh.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
        Path("/System/Library/Fonts/PingFang.ttc"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def main():
    parser = argparse.ArgumentParser(description="Create a timestamped storyboard from evidence JSON.")
    parser.add_argument("evidence_json")
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="逐秒截图分镜故事板")
    parser.add_argument("--columns", type=int, default=3)
    args = parser.parse_args()

    evidence_path = Path(args.evidence_json).expanduser().resolve()
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    files = [Path(path) for path in evidence.get("frames", [])]
    times = [float(value) for value in evidence.get("timestamps", [])]
    metadata = evidence.get("metadata") or {}
    if not files or len(files) != len(times):
        raise SystemExit("Evidence JSON must contain matching frames and timestamps.")

    columns = max(1, args.columns)
    rows = int(math.ceil(len(files) / columns))
    page_width = 1800
    margin, gap, header_height = 70, 34, 150
    cell_width = (page_width - 2 * margin - (columns - 1) * gap) // columns
    frame_height, caption_height = 610, 74
    cell_height = frame_height + caption_height
    page_height = header_height + rows * cell_height + max(0, rows - 1) * gap + margin

    canvas = Image.new("RGB", (page_width, page_height), "#f4f5f7")
    draw = ImageDraw.Draw(canvas)
    draw.text((margin, 45), args.title, fill="#16181d", font=load_font(54))
    duration_value = metadata.get("duration")
    duration_text = f"{float(duration_value):.2f}s" if duration_value is not None else "?s"
    info = f"{metadata.get('width', '?')}×{metadata.get('height', '?')} | {metadata.get('fps', '?')}fps | {duration_text}"
    draw.text((page_width - margin, 72), info, fill="#555b66", font=load_font(24), anchor="ra")
    caption_font = load_font(30)
    duration = float(metadata.get("duration") or times[-1])

    for index, (path, start) in enumerate(zip(files, times)):
        row, column = divmod(index, columns)
        x = margin + column * (cell_width + gap)
        y = header_height + row * (cell_height + gap)
        source = Image.open(path).convert("RGB")
        fitted = ImageOps.contain(source, (cell_width, frame_height), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (cell_width, frame_height), "#111318")
        tile.paste(fitted, ((cell_width - fitted.width) // 2, (frame_height - fitted.height) // 2))
        canvas.paste(tile, (x, y))
        draw.rectangle((x, y, x + cell_width, y + cell_height), outline="#b8bdc7", width=2)
        draw.rectangle((x, y + frame_height, x + cell_width, y + cell_height), fill="#ffffff")
        end = times[index + 1] if index + 1 < len(times) else duration
        label = f"{index:02d} | {start:g}s–{end:.2f}s" if index + 1 == len(times) else f"{index:02d} | {start:g}s–{end:g}s"
        draw.text((x + 18, y + frame_height + 18), label, fill="#1c2028", font=caption_font)

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, quality=96)
    print(output)


if __name__ == "__main__":
    main()
