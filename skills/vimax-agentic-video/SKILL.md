---
name: vimax-agentic-video
description: "Use when the user wants a ViMax-style agentic video-generation workflow: turning concepts, novels, scripts, short-drama hooks, or visual references into a coordinated director, screenwriter, producer, and video-generator plan with story beats, scene structure, shot lists, asset needs, model routing, and quality checks. This local wrapper is based on HKUDS/ViMax; the upstream repo had no native Codex SKILL.md, so do not assume ViMax is installed unless explicitly set up."
---

# ViMax Agentic Video

Source repository: https://github.com/HKUDS/ViMax

Use this wrapper for agentic end-to-end video planning. It is best for projects that need more than one prompt: scripts, short dramas, connected clips, character consistency, environment consistency, and generation strategy.

## When To Use

- The user asks to process a story, title, plot, or one-minute drama into script plus video-generation plan.
- The user wants a director/screenwriter/producer style breakdown.
- The request needs a hook, beat structure, character arcs, shot sequencing, and generation-ready prompts.
- The user references ViMax, agentic video generation, or all-in-one AI video agents.

For a single Seedance prompt, use Seedance-specific skills after the plan is formed.

## Agent Roles

- Director: defines visual language, blocking, lens distance, rhythm, and emotional continuity.
- Screenwriter: builds hook, conflict, reveal, dialogue, and payoff.
- Producer: tracks assets, character references, location plates, continuity risks, runtime, and clip count.
- Video generator: converts each scene into prompt-ready shots with timing, motion, light, and constraints.
- Reviewer: checks whether the result can actually be generated without identity drift, background mismatch, or unclear camera direction.

## Workflow

1. Extract the core promise: genre, relationship, secret, immediate conflict, and final beat.
2. Build a one-minute structure: 0-5s hook, 5-15s setup, 15-35s escalation, 35-50s reveal, 50-60s cliffhanger or emotional turn.
3. Define character locks: face, age range, wardrobe, posture, expression baseline, speech pattern.
4. Define space locks: location, light direction, camera axis, props, background continuity.
5. Convert beats into shots: timecode, shot size, camera, action, micro-expression, dialogue, sound, generation notes.
6. Route to specialized skills for final prompt rendering when useful: Seedance storyboard, script-to-shot, micro-expression control, or image prompt director.
7. Add a QC pass: hook clarity, dialogue economy, identity continuity, background stability, and motion feasibility.

## Output Pattern

For a script request, output:

1. Logline.
2. One-minute beat sheet.
3. Dialogue script.
4. Shot-by-shot video script with timecodes.
5. Prompt-ready generation blocks.
6. Short comparison note if multiple processing methods are requested.

Keep the first five seconds visually decisive: conflict in frame, one irreversible line or action, and a question the viewer needs answered.
