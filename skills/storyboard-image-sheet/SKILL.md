---
name: storyboard-image-sheet
description: Create or refine one-image AI video storyboard sheets from a scene script, character identity boards, shot notes, or Chinese prompts. Use when the user asks for 故事板, 分镜图, AI视频故事板, 手绘线稿分镜, one storyboard image, panel-by-panel visual planning, captions under each frame, or a prompt that clearly shows character positions, shot size, actions, camera movement, arrows, and visual focus without making a polished poster.
---

# Storyboard Image Sheet

## Core Use

Turn a scene script and one or more character identity boards into a single storyboard sheet for AI video planning. Prefer a clean hand-drawn line-art storyboard, not a finished poster, key visual, cinematic still, or polished comic page.

If the user asks for an actual image, build a complete image-generation prompt and use the available image generation tool. If the storyboard is meant to support AI video generation, also provide a detailed shot-note table outside the image. If the user only asks for a prompt, return the image prompt, the panel caption list, and the video shot-note table.

## Workflow

1. Extract the input:
   - Character A/B identity: age, gender presentation, role, costume, hairstyle, key props, facial features, posture, and relationship.
   - Scene goal: what changes from start to end, who leads the action, who reacts, and the emotional turn.
   - Location and time: interior/exterior, weather, light source, key background elements, moving environment elements.

2. Choose panel count:
   - Default to 6 panels in one sheet for a normal scene.
   - Use 4 panels for a short simple beat.
   - Use 8 panels only if the scene has multiple clear action turns.

3. Structure each panel:
   - Show character positions clearly: left/right, foreground/background, distance, orientation, eyeline.
   - Specify shot size: 远景, 全景, 中景, 近景, 特写, 过肩, 俯拍, 仰拍.
   - Specify action: body movement, hand action, expression, object interaction.
   - Specify camera movement: 推, 拉, 摇, 移, 跟拍, 环绕, 固定镜头, 手持轻晃.
   - Add arrows for motion: solid arrows for character movement, dashed arrows for camera movement, small repeated arrows for environment movement.
   - Mark the visual focus: use simple circles, frame boxes, or focus marks around faces, hands, props, or impact points.

4. Require captions:
   - Add a short Chinese caption below every panel.
   - Format each caption as: `景别｜人物动作｜镜头运动`.
   - Keep captions concise so they fit inside the panel footer.
   - Also provide the caption list outside the image prompt when text legibility matters.
   - Do not place dialogue balloons, speech bubbles, subtitles, or floating text inside the image area when the storyboard may be used as an AI video reference. Put dialogue in the external shot notes instead.
   - Keep the image footer short; put richer text in the external shot notes, not inside the generated image.

5. Reduce anatomy risk:
   - For hand or ring close-ups, prefer clear simplified storyboard hands over detailed photorealistic fingers.
   - Avoid multiple overlapping hands, tangled fingers, hidden thumbs, or extreme cropped hand piles.
   - Show one controlling hand and one wrist/hand in a readable side view when depicting force.
   - Keep the ring separated from the fingers enough to remain readable; circle it as a prop focus if needed.

## Image Prompt Template

Use this template and replace bracketed fields:

```text
根据以下剧情脚本和人物身份板，生成一张 AI 视频故事板分镜图。画面是一张完整的 storyboard sheet，白纸背景，黑色和灰色铅笔手绘线稿，清晰分格，不是精修海报，不是电影剧照，不是漫画成稿。

画幅：[横版16:9 / A3分镜纸 / 竖版按用户要求]，布局：[默认2行3列，共6格；或4格/8格]。每一格都有清楚边框、分镜编号、简短中文说明栏。每格下方中文说明格式为“景别｜人物动作｜镜头运动”。

人物身份保持一致：
角色A：[身份、外貌、服装、关键道具、性格状态]
角色B：[身份、外貌、服装、关键道具、性格状态]

剧情核心：[一句话概括场景冲突或情绪转折]
场景环境：[地点、时间、光线、天气、关键物件]

每格内容：
1. [景别]：角色位置[左/右/前/后]，角色动作[具体动作]，镜头[运动方式]，画面重点[脸/手/道具/空间关系]，用箭头标注[人物/镜头/环境运动]。说明：[景别｜人物动作｜镜头运动]
2. [景别]：...
3. [景别]：...
4. [景别]：...
5. [景别]：...
6. [景别]：...

视觉要求：专业导演分镜草图，线条干净，人物比例简化但可辨认，空间透视清楚，动作姿态明确，镜头运动箭头清楚，环境运动箭头清楚，重要道具用圈线标注。画面重点是调度、动作和镜头，不追求精修质感。

避免：精修海报、厚涂插画、彩色商业KV、复杂背景压过人物、无分格、无说明栏、人物身份混乱、文字过长、中文乱码、镜头运动缺失、箭头缺失、每格构图重复、画面内对话框、气泡对白、字幕漂浮在分镜画面里、异常手、额外手指、手指粘连、手部交叠过多。
```

## Panel Writing Rules

Before generating the final prompt, create a compact panel plan:

```text
1. 全景｜A从门口进入，B在桌旁回头｜镜头缓慢推入
2. 过肩中景｜A看向B手中的道具，B微微后退｜镜头向右横移
3. 特写｜B握紧道具，手指发抖｜固定镜头
4. 双人中景｜A伸手制止，B躲开｜手持跟拍
5. 近景｜两人对视，情绪僵住｜镜头轻推
6. 远景｜B转身离开，A停在原地｜镜头缓慢拉远
```

Use concrete visual verbs. Avoid vague words like “电影感很强” unless tied to a visible action, shot, or lighting choice.

## Video-Reference Cleanups

If a generated storyboard will be fed into an AI video model, make the image itself clean:

- Keep dialogue, voiceover, sound design, and exact lines outside the image as separate shot notes.
- Remove speech bubbles, dialogue boxes, floating subtitles, and long text inside panels.
- Keep only panel numbers, arrows, simple focus circles, and optional footer captions.
- For difficult anatomy beats such as grabbing a wrist or putting on a ring, use a medium close-up or prop insert with simplified hands instead of a dense interlocked-finger macro.

For live-action video references:

- Treat hand-drawn storyboard sheets as blocking/camera references, not style references.
- Treat photoreal reference boards as look-development documents for humans; avoid feeding dense collage boards directly to video models.
- Prefer separate clean inputs: one high-resolution character identity image, one environment/style reference, one clean storyboard panel, and one detailed text prompt per shot.
- If only one image reference is allowed, use a clean single-shot keyframe or a clean storyboard panel; avoid all-in-one boards with maps, icons, labels, palettes, tiny photos, and UI lines.
- Add this instruction to video prompts: `参考图只用于构图、人物站位和运镜，不继承分镜线稿、箭头、边框、文字、拼贴版式或低清噪点。`

## External Video Shot Notes

For AI video generation, output a separate detailed note for each panel after the image or prompt. Use this structure:

```text
05｜15-19s
画面：断崖礼台中全景，诺亚从左后方把莉娅推到仪式中央，宾客半圆围住她，长桌和银烛形成压迫中心。
人物：莉娅踉跄、抗拒、低头稳住身体；诺亚靠近她肩后，动作克制但强硬；宾客静默注视。
运镜：镜头从左向右轻摇，同时缓慢拉远，露出宾客包围和悬崖边缘。
动态：海风吹动长裙、斗篷和烛火，远处海浪闪光。
声音/对白：诺亚低声“微笑。今晚之后，我家的债就清了。”对白只写在这里，不进入画面。
负面：不要气泡对白，不要画内字幕，不要现代婚礼，不要过度精修。
```

Keep these notes concrete enough to become video prompts. Include:

- Timecode and shot number
- Scene/framing
- Character blocking and action
- Camera movement
- Environmental motion
- Sound/dialogue/voiceover
- Continuity constraints and negative prompts

## Output Shape

When answering the user, keep the response practical:

1. Provide the finished image-generation prompt.
2. Provide the panel caption list.
3. Provide external detailed video shot notes when the storyboard is intended for AI video generation.
4. If an image was generated, show the image and mention that image text should stay short; use the external shot notes for exact dialogue and detailed video prompting.
