---
name: generative-media-skills
description: Use when the user wants to plan, adapt, or operationalize workflows inspired by SamurAIGPT/Generative-Media-Skills for broad AI image, video, audio, product ad, UGC, social media, YouTube Shorts, thumbnail, storyboard, clipping, or multimodal generative-media tasks. This is a local wrapper skill; it helps choose and translate upstream recipe families without assuming muapi credentials or upstream dependencies are installed.
---

# Generative Media Skills

Source repository: https://github.com/SamurAIGPT/Generative-Media-Skills

This local wrapper keeps the useful idea of the upstream project: a broad recipe library for AI media production. Use it to turn a user request into a practical media workflow, prompt pack, or production checklist while keeping the output platform-neutral unless the user names a target tool.

## When To Use

- The user asks for AI image, AI video, music, voice, clipping, social media, product ad, UGC, short-form video, thumbnail, or campaign-style creative production.
- The user wants to compare or combine media-generation workflows across tools.
- The user asks for a reusable production system rather than a single prompt.
- The user references Generative-Media-Skills, muapi, or broad multimodal AI media skill packs.

Prefer a more specific local skill when the request is clearly only Seedance prompting, reverse video prompt analysis, micro-expression control, image prompt writing, or storyboard board design.

## Workflow

1. Classify the request by output type: image, video, edit, audio, social, product/ad, or workflow.
2. Pick the smallest useful recipe family rather than loading a whole production stack.
3. Produce a compact production brief with objective, format, references, subject, scene, timing, camera, prompt, asset needs, and validation notes.
4. If the user asks to run an upstream workflow, state the required credentials and dependencies before making any runtime claims.
5. When the user is building short drama assets, route the idea into script, character identity, location plate, shot list, generation prompt, and consistency checks.

## Recipe Families

- Visual: still image prompts, style exploration, product visuals, thumbnails, character or scene references.
- Motion: text-to-video, image-to-video, Seedance-style clips, transitions, camera language, action continuity.
- Edit: AI clipping, rough cut, repurposing, subtitles, highlights, social cutdowns.
- Social: YouTube Shorts, Instagram posts, UGC ads, campaign packages, hook-first formats.
- Workflow: repeatable pipelines, asset inventory, shot tracking, prompt versioning, QC.

## Output Pattern

For creative planning, output:

1. Goal and target format.
2. Required inputs or reference assets.
3. Scene or asset plan.
4. Generation prompts or editing instructions.
5. Consistency controls.
6. Quality checks and iteration notes.

Keep language concrete: shot scale, timing, subject placement, light direction, material behavior, dialogue, and edit rhythm. Avoid vague quality tags.
