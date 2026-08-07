---
name: openstoryline-video-editor
description: "Use when the user wants a FireRed OpenStoryline-style video editing agent workflow: natural-language video editing, storyline planning, rough cuts, transition design, subtitle imitation, speech rough cut, reusable style profiles, clip sequencing, or human-in-the-loop editing plans. This is a local wrapper for FireRedTeam/FireRed-OpenStoryline and its bundled OpenStoryline skills; do not assume the runtime is installed unless explicitly configured."
---

# OpenStoryline Video Editor

Source repository: https://github.com/FireRedTeam/FireRed-OpenStoryline

Use this wrapper when the user is thinking like an editor rather than only a prompt writer. It converts natural-language intent into a timeline plan, edit decisions, style profile, and QC pass. It is especially useful after clips or images already exist.

## When To Use

- The user asks how to assemble, edit, restructure, subtitle, transition, or repurpose video clips.
- The user wants a reusable editing style, rough cut workflow, subtitle imitation, or speech-based cut plan.
- The request mentions OpenStoryline, FireRed, natural-language video editing, storyline editing, style skills, or clip orchestration.
- The user has several generated shots and needs continuity, pacing, or sequence repair.

If the user only needs still-image generation or first-draft video prompts, use image or Seedance-oriented skills first.

## Workflow

1. Inventory the material: clips, images, audio, dialogue, length, aspect ratio, and target platform.
2. Identify the edit intent: romance tension, reveal, ad conversion, narrative clarity, rhythm repair, subtitle style, or transition polish.
3. Build a storyline timeline: opening hook, continuity bridge, emotional turn, key shot order, and ending beat.
4. Define style profile: pacing, shot duration range, color mood, subtitle position, transition types, sound bed, and silence strategy.
5. Convert the plan into edit instructions: trim points, shot order, B-roll use, dialogue placement, cutaway moments, music and ambience.
6. Add human review checkpoints where ambiguity matters: character identity, line delivery, object continuity, gaze direction, and background geography.
7. For install/run requests, inspect upstream documentation and environment first; do not claim OpenStoryline tools are callable until configured.

## Bundled Upstream Skill Ideas

- Install and use OpenStoryline.
- AI transition editing.
- Profile style skill creation.
- Default editing workflow.
- Speech rough cut.
- Subtitle imitation.

## Output Pattern

For editing tasks, output:

1. Material assumptions.
2. Storyline or timeline table.
3. Edit decision list.
4. Style profile.
5. Subtitle and audio notes.
6. QC checklist.

When working on dialogue scenes, preserve eyeline, camera axis, background geography, and light direction before improving decorative style.
