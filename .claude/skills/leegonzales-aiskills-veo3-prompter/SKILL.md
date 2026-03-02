---
name: veo3-prompter
description: Craft professional video prompts for Google Veo 3.1 using cinematic techniques, audio direction, and timestamp choreography. Use when generating AI videos, creating video prompts, or working with Veo 3.
---

# Veo 3.1 Video Prompter

Transform ideas into professional Veo 3.1 prompts using cinematic structure, audio direction, and multi-shot choreography.

## 前置依赖 (Koala2 项目)

**必须先读取** `works/[剧名]/style.json` 获取风格配置，使用以下字段：
- `prompts.video_veo.style_suffix` - 视频风格后缀
- `prompts.video_veo.cinematography` - 摄影风格关键词
- `prompts.video_veo.camera_style` - 镜头风格
- `visual_style.keywords` - 视觉风格关键词
- `lighting.*` - 光影参数

## When to Use

Invoke when user:
- Says "create a video prompt" or "generate a Veo prompt"
- Wants to "make a video of..." or "animate this..."
- Asks for help with "video generation" or "AI video"
- Needs "Veo 3" or "Veo 3.1" prompt assistance
- Wants to create "multi-shot" or "cinematic" video sequences

## Core Prompt Formula

**[Cinematography] + [Subject] + [Action] + [Context] + [Style & Audio]**

Every prompt should address these five elements for maximum control.

## Prompt Density: Finding the Sweet Spot

Prompts fail in two directions:
- **Too sparse:** Model fills gaps unpredictably, you lose creative control
- **Too dense:** Model can't execute all instructions, produces confused output

### The Priority Framework

**Tier 1 - MUST INCLUDE (model needs these):**
- Shot size (wide/medium/close-up)
- Subject identity (who/what is in frame)
- Primary action (what happens)
- One dominant mood/style word

**Tier 2 - SHOULD INCLUDE (significant impact):**
- Camera movement OR angle (pick one, not both)
- Lighting quality (natural/dramatic/soft)
- One audio layer (dialogue OR SFX OR ambient)
- Setting/environment

**Tier 3 - NICE TO HAVE (diminishing returns):**
- Secondary audio layers
- Specific lens type
- Color palette details
- Film stock/grain texture
- Background action

**Rule of thumb:** Include all Tier 1, most of Tier 2, and 1-2 from Tier 3.

### Density Comparison

**TOO SPARSE (model guesses too much):**
> "A professor talking about philosophy"

**TOO DENSE (model overloaded):**
> "Medium close-up shot at eye level with a 50mm lens at f/1.8 creating shallow depth of field with bokeh highlights, of a 52-year-old female professor with silver-streaked auburn hair pulled back in a loose bun, wearing an olive tweed jacket with leather elbow patches over a cream silk blouse with a small pearl brooch, standing in a contemporary lecture hall with tiered mahogany seating and brass fixtures visible in the soft background, natural diffused daylight streaming through floor-to-ceiling windows on the left side creating soft rembrandt lighting on her face with a gentle fill from reflected light on the right..."

**OPTIMAL (directed but breathable):**
> "Medium close-up of a professor in her 50s, tweed jacket, standing in a university lecture hall. She gestures while speaking: 'Kant asked one question: could everyone do this?' Warm natural window light from left, soft academic atmosphere. SFX: marker on whiteboard."

### Calibration Signals

**Signs your prompt is too sparse:**
- Results vary wildly between generations
- Key elements missing or wrong
- Mood/tone inconsistent with intent

**Signs your prompt is too dense:**
- Model ignores some instructions entirely
- Unnatural or frozen-looking motion
- Conflicting elements appear (e.g., both day and night)
- Audio doesn't match visual action

### Iteration Strategy

1. **Start with Tier 1 only** - generate test
2. **Add Tier 2 elements** that matter most to your vision
3. **Add ONE Tier 3 detail** if something specific is missing
4. **Remove any element the model consistently ignores**

See `references/prompt-calibration.md` for detailed examples and troubleshooting.

## Cinematography Elements

### Shot Composition
- Wide shot, medium shot, close-up, extreme close-up
- Single shot, two shot, over-the-shoulder shot
- High angle, low angle, eye level, worm's eye, bird's eye

### Camera Movement
- Dolly (in/out), tracking shot, crane shot
- Pan (left/right), tilt (up/down), zoom
- Steadicam, handheld, aerial, POV

### Lens & Focus
- Shallow depth of field, deep focus
- Wide-angle lens, telephoto, macro lens
- Soft focus, rack focus, bokeh

## Audio Direction

Veo 3.1 generates synchronized sound. Direct it explicitly:

**Dialogue** (use quotes):
> "A man says, 'The storm is coming.'"

**Sound Effects** (label with SFX):
> "SFX: Thunder rumbles in the distance, rain patters on glass"

**Ambient Noise**:
> "Ambient noise: busy café chatter, clinking cups, soft jazz"

**Music**:
> "A swelling orchestral score begins to play"

## Timestamp Prompting

For multi-shot sequences within one generation (max 8 seconds):

```
[00:00-00:02] Medium shot of a detective at his desk, lighting a cigarette.
SFX: Match strike, paper rustling.

[00:02-00:04] Close-up of his eyes narrowing as he reads a letter.
Ambient: Rain against the window.

[00:04-00:06] Reverse shot of a shadowy figure in the doorway.
A woman's voice: "You shouldn't have looked."

[00:06-00:08] Wide shot as the detective stands, reaching for his gun.
SFX: Chair scraping, thunder crack.
```

## Style Keywords

**Visual Aesthetic:**
- Photorealistic, cinematic, documentary, animation
- Retro (sepia, grainy film, 1980s vaporwave)
- Noir, epic fantasy, sci-fi, romantic, horror

**Mood & Lighting:**
- Warm golden hour, cool blue tones, moody shadows
- Harsh fluorescent, soft morning light, dramatic chiaroscuro
- Neon-lit, candlelit, overcast diffused

**Film Grain Tip:**
> Add "slightly grainy, film-like" to avoid overly clean AI look

## Output Formats

**Quick Prompt:** Single sentence for simple shots
**Structured Prompt:** Multi-line with all five elements
**Timestamp Sequence:** Choreographed multi-shot within 8s
**Storyboard Mode:** Multiple prompts for full narrative

## Example Prompts

**Action Shot:**
> "Tracking shot following a parkour athlete sprinting across rooftops at sunset, warm orange light, urban cityscape background, cinematic, shallow depth of field. SFX: footsteps on concrete, wind rushing past."

**Dialogue Scene:**
> "Medium two-shot in a dimly lit bar, a woman in red leans toward a man in a suit. She says quietly, 'I know what you did.' Ambient: jazz music, glasses clinking. Moody noir aesthetic, warm tungsten lighting."

**Nature Documentary:**
> "Slow-motion close-up of a hummingbird drinking from a flower, macro lens with shallow focus, lush green garden background, soft morning light. SFX: gentle buzzing, birdsong."

## Technical Specs

- **Duration:** 4, 6, or 8 seconds
- **Resolution:** 720p or 1080p
- **Aspect Ratio:** 16:9 (landscape) or 9:16 (portrait)
- **Frame Rate:** Configurable (default: 24 FPS)

## Advanced API Options

When using Veo through API (not Flow), these additional parameters are available:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `negativePrompt` | Elements to exclude from the video | - |
| `seed` | RNG seed for reproducible results (same prompt + seed = same video) | Random |
| `enhancePrompt` | Let the model rewrite your prompt for better results | false |
| `generateAudio` | Generate synchronized audio | true |
| `personGeneration` | Control person generation: `dont_allow` or `allow_adult` | - |
| `referenceImages` | Up to 3 asset images OR 1 style image for consistency | - |

### Negative Prompts

Explicitly exclude unwanted elements:
> "A forest at sunset" + negativePrompt: "people, animals, buildings"

### Seed for Consistency

Use the same seed to reproduce similar results:
> First generation: seed=12345 → video A
> Same prompt + seed=12345 → nearly identical video

Useful for:
- Iterating on a specific "look"
- Creating variations with controlled changes
- A/B testing different prompts

### 图片输入模式（重要）⭐

Veo 3.1 支持两种图片输入模式：

| 模式 | 图片数量 | 适用场景 | 说明 |
|------|----------|----------|------|
| **首尾帧模式** | 2张（首帧+尾帧） | 控制视频起点和终点 | 精确控制动作的开始和结束状态 |
| **多图模式** | 多张（最多3张资产图） | 多角色、复杂场景 | 配合 Nano Banana Pro 4×2 分镜图使用 |

### 首尾帧模式

**使用场景：**
- 需要精确控制视频起点和终点
- 单角色动作过渡
- 镜头衔接（用上一视频尾帧作首帧）

**图片要求：**
- First frame：控制视频开始画面
- Last frame：控制视频结束画面
- 最多上传 2 张图片

**示例：**
```
First frame: Previous shot's last frame
Last frame: Character standing up, determined expression

Medium shot, continuing from sitting position. She slowly rises,
her gaze fixed ahead. Camera dollies back slightly.
```

### 多图模式（配合 4×2 分镜图）⭐

**使用场景：**
- 多角色场景
- 复杂动作序列
- 需要保持角色一致性

**推荐：先在 Nano Banana Pro 生成 4×2 分镜图**

使用 Nano Banana Pro 生成一个 4×2 的 8 格分镜参考图，包含本视频所有关键帧，确保角色和风格一致性。

**4×2 Storyboard Prompt Template:**
```
[Visual style], 4×2 storyboard grid, 8 panels, comic layout,
Panel 1: [Frame 1 description - scene/character starting state]
Panel 2: [Frame 2 description - action A]
Panel 3: [Frame 3 description - action B]
Panel 4: [Frame 4 description - action C]
Panel 5: [Frame 5 description - reaction/transition]
Panel 6: [Frame 6 description - dialogue/interaction]
Panel 7: [Frame 7 description - climax action]
Panel 8: [Frame 8 description - ending state],
consistent character design, [style suffix]
```

**多图模式图片上传：**
```
Reference Images (up to 3 assets):
- Image 1: Character A reference
- Image 2: Character B reference
- Image 3: Scene/location reference
- Optional: 4×2 storyboard as style reference
```

**操作步骤：**
1. 先在 Nano Banana Pro 使用上述模板生成 4×2 分镜图
2. 在 Veo 3.1 中上传分镜图作为风格参考
3. 上传角色/场景图作为资产参考（最多3张）
4. 输入视频提示词生成

---

### Reference Images

Maintain visual consistency across shots using reference images:

**Asset References (up to 3):**
- Character appearances
- Locations/settings
- Props or products

**Style References (1):**
- Overall aesthetic
- Color palette
- Visual treatment
- **4×2 storyboard grid (recommended for complex scenes)**

## 跨镜头衔接 (Koala2 项目)

### 衔接输入格式

当处理镜头 N（N > 1）时，会收到以下衔接信息：

```yaml
continuity:
  previous_shot: 镜头编号
  first_frame_reference: 上一镜头尾帧前 1-2 秒的帧（作为首帧图片）
  last_2_seconds_action: 上一镜头最后2秒的动作描述
  ending_state:
    character_position: 角色位置
    character_facing: 角色朝向
    character_expression: 角色表情
    camera_position: 镜头位置
  transition_type: direct_continue | action_transition | emotion_shift | scene_change
```

### 衔接提示词模板

**直接延续型:**
```
Continuing from previous shot where [角色] was [上一镜头结尾动作].
[首帧图片作为 referenceImages 输入]
[当前镜头的完整动作描述]
```

**动作过渡型:**
```
Following [角色]'s [上一镜头结尾动作], the camera [运镜过渡].
Now [当前镜头的新动作].
```

**示例:**
```
# 镜头 2 - 衔接自镜头 1
Continuing from previous shot where the young woman was walking towards the ancient temple gate, her hand reaching for the door.
首帧图片: 镜头1 第6秒帧

Medium shot, she pushes open the heavy wooden door. Dust particles float in the beam of light entering through the gap. Her expression shifts from curiosity to awe as she steps inside. Camera slowly dollies forward following her movement. SFX: creaking door, echoing footsteps.

输出给下一镜头:
- 尾帧时间点: 第7秒
- 结尾动作: 她正踏入殿内，目光向上看
- 结尾位置: 殿门口内侧，面向殿内
```

## References

- `references/prompt-calibration.md` - Finding the right detail level
- `references/cinematography-glossary.md` - Full camera terms
- `references/prompt-examples.md` - 20+ categorized examples
- `references/advanced-workflows.md` - Image-to-video, first/last frame
