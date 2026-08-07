---
name: video-reverse-prompt
description: Reverse-engineer supplied videos, clips, screenshots, or video descriptions into director-style AI video prompts. Use when the user asks for 视频反推提示词, 视频拆解, 逐秒分镜, 镜头语言分析, extracting prompts from a reference video, or producing Chinese prompts for AI video generation tools from existing footage.
---

# Video Reverse Prompt

## Workflow

1. Inspect the source before writing: read duration, resolution, frame rate, and visual evidence from the video or screenshots. If a video file is available, run `scripts/extract_video_evidence.py` to create evenly spaced frames.
2. Analyze from picture structure and timeline, not loose tag keywords. Anchor claims in visible evidence: camera height, shot size, composition, blocking, body mechanics, object movement, lighting direction, materials, and spatial relationships.
3. Divide the action into natural time ranges. Prefer 1-3 second ranges for short clips, and merge only when the camera and action remain continuous.
4. Separate what is visible from what is inferred. If dialogue cannot be heard or verified, write "无可辨识台词" rather than inventing lines.
5. Output in Chinese unless the user asks otherwise.

## Required Output Shape

### 1. 核心视觉架构（全局设定）

Include:

- 视觉风格: e.g. 写实电影摄影, 手机纪实视频, 赛博朋克3D渲染, 复古胶片.
- 基础光影: describe light source, direction, intensity, contrast, shadows, reflections.
- 色彩基调: describe dominant hues, saturation, contrast, warm/cool balance.
- 镜头质感: mention handheld/fixed, lens feel, motion blur, depth of field, compression, stabilization artifacts when visible.
- 场景空间: describe location layout, background layers, props, and scale.

### 2. 时间线动作分镜（逐秒拆解表）

Use a Markdown table with these columns:

| 时间段 | 机位与运镜 | 主体动作细节 | 环境与道具互动 | 每个人物的台词 |
| --- | --- | --- | --- | --- |

For 主体动作细节, specify:

- limb actions, weight shifts, head/eye direction, facial expression;
- clothing/hair/object physics when visible;
- exact interaction order between characters.

For 机位与运镜, specify:

- shot size: 特写, 近景, 中景, 全景, 俯拍, 仰拍;
- camera behavior: 固定, 手持轻晃, 推镜, 拉镜, 横移, 跟拍, 甩镜;
- composition: centered subject, thirds, foreground/background layering, negative space.

### 3. 最终中文生成提示词

Merge the analysis into one continuous prompt. Follow this grammar:

`[风格参数] [镜号][时间轴][景别与运镜][构图][画面主体与核心动作描述，角色之间的互动 + 谁说什么台词], [环境与背景细节], [光影与材质]`

Write concrete visual instructions. Avoid hollow adjectives such as "好看的", "完美的", "高级的", "震撼的", "电影级" unless they are translated into measurable visual details.

## Prompt Quality Rules

- Use visual, measurable language: position, direction, timing, texture, light source, shadow edge, material response.
- Keep identity and continuity stable across shots: clothing, body position, object placement, screen direction.
- Preserve the reference's actual camera logic unless the user asks for a creative remake.
- Do not add events, props, dialogue, or emotional beats that are not visible or explicitly supplied.
- If image or audio evidence is insufficient, mark the uncertainty briefly and continue with the best visible analysis.

## Script

Run:

```bash
python scripts/extract_video_evidence.py <video-path> --out-dir <output-dir> --frames 12
```

The script prints JSON metadata and writes evenly spaced JPEG frames. It uses `ffprobe`/`ffmpeg` when available, otherwise falls back to OpenCV if installed.
