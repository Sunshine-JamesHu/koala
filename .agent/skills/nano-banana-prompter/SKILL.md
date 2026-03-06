---
name: nano-banana-prompter
description: An advanced prompt generation guide and assistant for Nano Banana Pro. Use this skill when you need to write, refine, or structure high-quality prompts for Nano Banana Pro to generate images, UI designs, character sheets, or photography. It includes best practices for JSON-based prompts, structured markdown prompts, camera settings, lighting, and text rendering.
---

# Nano Banana Prompter

## Overview

This skill provides the best practices and templates for writing highly effective, professional-grade prompts for **Nano Banana Pro**. Nano Banana Pro thrives on extreme detail, structured formatting, and precise technical specifications (camera parameters, lighting conditions, etc.).

## Prompt Generation Rules

1. All prompt text **MUST be in English**.
2. All prompts **MUST** include the full art style block from `global_assets/style.json` verbatim.
3. Character descriptions **MUST** reference the corresponding `characters/*.json` four-view data.
4. Scene descriptions **MUST** reference the corresponding `scenes/*.json` layout and angles.
5. **角色四视图的绝对画幅控制 (Strict 4-View Layout)**: To ensure stability and prevent the AI from generating 3 or 5 views, character sheet prompts **MUST explicitly define the layout as a horizontal side-by-side lineup**. Always start the prompt with: `A professional character design sheet of [Name], [Description]. EXACTLY 4 distinct views arranged horizontally side-by-side on a clean neutral background. From left to right: 1) Large detailed facial close-up bust, 2) Front full body, 3) Back full body, 4) Side profile full body.`
6. **角色四视图归属角色目录**: Character design sheet prompts are generated into the character's own directory (`global_assets/characters/` or `chapters/[XX]/characters/`) as a `[name]_prompt.md` file. The `04_prompts.md` only **references** them, never repeats the full prompt.
7. **场景空镜不含角色私有道具**: Scene base images must NEVER include character-bound props (e.g., wheelchair belongs to Shen Qingqi, not to the room). Only fixed architectural elements belong in scene bases.
8. **角色姿态的绝对精确描述 (Explicit Pose Definitions)**: When a character is not standing, you **MUST explicitly define their anatomical posture**. Avoid vague terms like "lying on the floor". Instead use: `lying prone on her stomach`, `lying supine on his back`, `lying on her right side propped up on her elbow`, `curled in a fetal position`, `kneeling on both knees`. This ensures the AI understands exactly how the body intersects with the environment.
9. **绝对的光源与空间透视控制 (Absolute Spatial & Lighting Continuity)**: Pay strict attention to where light sources and props are placed in the scene definition. If an oil lamp is defined as sitting on a wooden table, **it must remain on the table in all shots**. Do not write "dim oil lamp nearby" on the floor, or "backlight from oil lamp" if the table is in front of the character. Specify the light direction based on the actual 3D layout of the room.

## Output File Structure (04_prompts.md)

The final output file for the human operator **MUST** follow this exact 3-part structure:

---

### Part 1: 操作总览 (Quick Start Checklist)

A table at the very top of the file summarizing ALL images to generate in order. This lets the operator see the full workload at a glance.

```markdown
# [Novel Name] - 第[X]章 生图清单

## 📌 全局风格 (Global Style)
> 以下英文风格段落必须附加在**每一条**提示词的末尾。请先复制保存备用。

```text
[PASTE THE EXACT CONTENT of art_style + color_palette.description + texture + lighting.default_quality from style.json here, verbatim, as one continuous block.]
```

## ✅ 生图清单

| # | 文件名 | 类型 | 垫图 | 状态 |
|---|--------|------|------|------|
| 1 | 辛月影_四视图.jpg | 角色 | 无 | ☐ |
| 2 | 破落农舍_全景.jpg | 场景 | 无 | ☐ |
| 3 | C01_S01_Shot01.jpg | 分镜 | 角色图+场景图 | ☐ |
| 4 | C01_S01_Shot02.jpg | 分镜 | ← Shot01 | ☐ |
| ... | ... | ... | ... | ☐ |

> 操作员可以在"状态"列打勾来跟踪进度。
```

---

### Part 2: 基准图 (Reference Images)

Generate scene bases BEFORE any storyboard shots. Character sheets are **NOT written here** — they live in the character directory. This section only contains:

**A) 角色引用 (Character References — link only, no prompt)**
```markdown
---
### 👤 角色: [Name]
> 📂 四视图提示词 → `global_assets/characters/[name]_prompt.md`
> 生成后保存为: `[name]_四视图.jpg` 供后续垫图使用
---
```

**B) 场景空镜 (Scene Bases — full prompt)**

> ⚠️ 场景空镜**绝不包含**角色私有道具（如：轮椅属于沈清起角色，不属于房间）。只包含固定的建筑/家具。

```markdown
---
### 🏞️ REF-XX: [Scene Name] - [Angle]
> **类型**: 场景空镜 | **垫图**: 无需
> **来源**: `scenes/[name].json` → Angle [X]

```text
[The full English prompt. Extract FIXED layout from scene JSON.
Do NOT include character-bound props (wheelchairs, weapons, etc.)
Include the FULL style block at the end.

Negative prompt: [negative terms here]]
```
---
```

---

### Part 3: 分镜连载 (Storyboard Shots)

Each shot is a compact card. The format is designed for fast scanning and one-click copy:

```markdown
---
### 🎬 #[N] `C01_S01_Shot01.jpg`
> **景别**: 远景 | **角度**: 俯拍 | **镜头**: 35mm
> **垫图**: 📌 请上传 `破落农舍_全景.jpg` + `辛月影_四视图.jpg`
> **过渡**: ← 硬切 (Hard Cut)

```text
[Concise, detailed English prompt.
Subject: ...
Environment: ...
Lighting: ...
Camera: ...
Continuous action: ... (if applicable)

(FULL STYLE BLOCK from style.json, verbatim)

Negative prompt: 2D, smiling, bright sunlight, modern clothing, text, watermark]
```
---
```

## Key Design Principles of This Format

1. **One-glance planning**: The checklist table lets the operator plan their entire session.
2. **Copy-paste efficiency**: Each prompt is in a single `text` code block, **including negative prompts at the end**. Just click "copy".
3. **Style block consistency**: The global style is shown once at the top but MUST be pasted into every individual prompt's `text` block by the Agent.
4. **Base image clarity**: The `垫图` line is the very first thing the operator sees per card.
5. **Progress tracking**: ☐ checkboxes in the overview table.
6. **Compact cards**: Metadata (shot size, angle, lens) is in a single `>` quote line, not mixed into the prompt text.

## Keyframe Density Rule
You must generate enough prompts to cover EVERY key action and transition. If a character walks across a room and picks up a sword, break it down:
1. Wide shot: Character walking.
2. Medium shot: Character reaching for the sword.
3. Extreme Close-up: Hand grabbing the hilt.

When generating prompts from a storyboard, if the shots are too sparse, **you must actively insert more keyframes** to make the animation fluid.

## Character & Image Consistency
- Explicitly state: `[CRITICAL: Maintain precise facial features from the uploaded character reference sheet.]`
- For continuous actions: `Continuous action sequence, exact same pose and clothing as the reference image, progressing the movement slightly.`
- For same-scene shots: `Exact same background layout as reference image.`
