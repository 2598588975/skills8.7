#!/usr/bin/env python3
import argparse
import json
import math
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_binary(name):
    override = os.environ.get(f"{name.upper()}_PATH")
    if override and Path(override).expanduser().is_file():
        return str(Path(override).expanduser())
    found = shutil.which(name)
    if found:
        return found
    if sys.platform == "win32":
        candidates = [
            Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Topaz Labs LLC" / "Topaz Video" / f"{name}.exe",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Links" / f"{name}.exe",
        ]
        for candidate in candidates:
            if candidate.is_file():
                return str(candidate)
    return None


def run_json(command):
    try:
        process = subprocess.run(command, check=True, capture_output=True, text=True, encoding="utf-8")
        return json.loads(process.stdout)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def parse_rate(value):
    if not value or value == "0/0":
        return None
    try:
        if "/" in value:
            numerator, denominator = value.split("/", 1)
            return float(numerator) / float(denominator)
        return float(value)
    except (ValueError, ZeroDivisionError):
        return None


def probe_with_ffprobe(video, ffprobe):
    if not ffprobe:
        return None
    data = run_json([
        ffprobe, "-v", "error", "-show_entries",
        "format=duration:stream=index,codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels",
        "-of", "json", str(video),
    ])
    if not data:
        return None
    streams = data.get("streams") or []
    video_stream = next((stream for stream in streams if stream.get("codec_type") == "video"), {})
    audio_stream = next((stream for stream in streams if stream.get("codec_type") == "audio"), {})
    duration = (data.get("format") or {}).get("duration")
    return {
        "width": int(video_stream["width"]) if video_stream.get("width") else None,
        "height": int(video_stream["height"]) if video_stream.get("height") else None,
        "fps": parse_rate(video_stream.get("avg_frame_rate")),
        "duration": float(duration) if duration else None,
        "video_codec": video_stream.get("codec_name"),
        "audio_codec": audio_stream.get("codec_name"),
        "sample_rate": int(audio_stream["sample_rate"]) if audio_stream.get("sample_rate") else None,
        "channels": audio_stream.get("channels"),
        "backend": "ffprobe",
    }


def probe_with_opencv(video):
    try:
        import cv2
    except Exception:
        return None
    capture = cv2.VideoCapture(str(video))
    if not capture.isOpened():
        return None
    fps = capture.get(cv2.CAP_PROP_FPS) or None
    frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT) or None
    metadata = {
        "width": int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) or 0) or None,
        "height": int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0) or None,
        "fps": float(fps) if fps else None,
        "duration": float(frame_count / fps) if frame_count and fps else None,
        "video_codec": None,
        "audio_codec": None,
        "sample_rate": None,
        "channels": None,
        "backend": "opencv",
    }
    capture.release()
    return metadata


def even_timestamps(duration, count):
    if not duration or duration <= 0:
        return [0.0]
    count = max(1, count)
    if count == 1:
        return [min(duration / 2, max(duration - 0.05, 0.0))]
    start = min(0.2, duration * 0.05)
    end = max(duration - min(0.2, duration * 0.05), start)
    return [start + (end - start) * index / (count - 1) for index in range(count)]


def second_timestamps(duration):
    if not duration or duration <= 0:
        return [0.0]
    return [float(second) for second in range(int(math.floor(duration)) + 1)]


def extract_ffmpeg(video, output_dir, times, max_width, ffmpeg):
    if not ffmpeg:
        return None
    files = []
    scale = f"scale='min({max_width},iw)':-2"
    for index, timestamp in enumerate(times):
        destination = output_dir / f"frame_{index:03d}_{timestamp:.2f}s.jpg"
        command = [
            ffmpeg, "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{timestamp:.3f}",
            "-i", str(video), "-frames:v", "1", "-vf", scale, "-q:v", "2", str(destination),
        ]
        try:
            subprocess.run(command, check=True)
            files.append(str(destination))
        except (OSError, subprocess.CalledProcessError):
            return None
    return files


def extract_opencv(video, output_dir, times, max_width):
    try:
        import cv2
    except Exception as exc:
        raise RuntimeError("Install FFmpeg or opencv-python to extract video frames.") from exc
    capture = cv2.VideoCapture(str(video))
    if not capture.isOpened():
        raise RuntimeError(f"Could not open video: {video}")
    files = []
    for index, timestamp in enumerate(times):
        capture.set(cv2.CAP_PROP_POS_MSEC, max(timestamp, 0.0) * 1000)
        ok, frame = capture.read()
        if not ok:
            continue
        height, width = frame.shape[:2]
        if width > max_width:
            ratio = max_width / float(width)
            frame = cv2.resize(frame, (max_width, max(1, int(height * ratio))))
        destination = output_dir / f"frame_{index:03d}_{timestamp:.2f}s.jpg"
        cv2.imwrite(str(destination), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 92])
        files.append(str(destination))
    capture.release()
    return files


def main():
    parser = argparse.ArgumentParser(description="Extract metadata and evidence frames from a video.")
    parser.add_argument("video")
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--frames", type=int, default=12)
    parser.add_argument("--per-second", action="store_true")
    parser.add_argument("--max-width", type=int, default=960)
    parser.add_argument("--json", dest="json_path")
    args = parser.parse_args()

    video = Path(args.video).expanduser().resolve()
    output_dir = Path(args.out_dir).expanduser().resolve()
    if not video.is_file():
        raise SystemExit(f"Video not found: {video}")
    output_dir.mkdir(parents=True, exist_ok=True)

    ffmpeg = find_binary("ffmpeg")
    ffprobe = find_binary("ffprobe")
    metadata = probe_with_ffprobe(video, ffprobe) or probe_with_opencv(video)
    if not metadata:
        raise SystemExit("Could not read video metadata. Install FFmpeg or opencv-python.")
    times = second_timestamps(metadata.get("duration")) if args.per_second else even_timestamps(metadata.get("duration"), args.frames)
    files = extract_ffmpeg(video, output_dir, times, args.max_width, ffmpeg)
    if files is None:
        files = extract_opencv(video, output_dir, times, args.max_width)

    result = {"video": str(video), "metadata": metadata, "timestamps": times, "frames": files}
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_path:
        json_path = Path(args.json_path).expanduser().resolve()
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

