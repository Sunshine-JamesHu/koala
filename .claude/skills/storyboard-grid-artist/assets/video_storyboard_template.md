# 视频分镜参考图模板

> **模板说明**: 本模板用于为每个视频生成独立的分镜参考图提示词

---

## 文件头部

```markdown
# 视频分镜参考图 - 第[X]章 [章节名]

> **使用说明**:
> - 本文件包含每个视频的独立分镜参考图提示词
> - 在生成视频前，先生成对应的分镜参考图
> - 将分镜参考图上传到视频生成工具作为参考

---

## 分镜参考图总览

| 视频编号 | 视频名称 | 时长 | 格数 | 对应位置 |
|----------|----------|------|------|----------|
| V01 | [名称] | 8秒 | 6格 | 第X章 Veo |
| V02 | [名称] | 8秒 | 6格 | 第X章 Veo |
| K01 | [名称] | 10秒 | 8格 | 第X章 可灵 |
| K02 | [名称] | 5秒 | 4格 | 第X章 可灵 |
```

---

## 单个视频分镜参考图模板

### 8秒视频 - 6格布局

```markdown
### [V01/V02/...] 分镜参考图 - [视频名称]（8秒）

**用途**: 作为 [视频编号] 的参考图上传到 AI 视频生成工具

**布局**: 6格分镜（2行×3列）

**镜头概览**:
| 格子 | 时间点 | 内容概要 | 景别 |
|------|--------|----------|------|
| 1 | 0-1.3秒 | [开场动作] | [景别] |
| 2 | 1.3-2.6秒 | [发展动作] | [景别] |
| 3 | 2.6-4秒 | [转折动作] | [景别] |
| 4 | 4-5.3秒 | [高潮动作] | [景别] |
| 5 | 5.3-6.6秒 | [收尾动作] | [景别] |
| 6 | 6.6-8秒 | [结尾状态] | [景别] |

**提示词**:
\```
[STYLE_PREFIX],

IMPORTANT: This is a storyboard reference image for a SINGLE CONTINUOUS VIDEO SHOT. All 6 panels depict the SAME scene with SAME characters in a CONTINUOUS time flow of 8 seconds. Maintain PERFECT SPATIAL CONSISTENCY across all panels: character positions must flow logically from panel to panel, scene layout (door position, furniture, background elements) remains IDENTICAL in every panel, light source direction (moonlight from window, candlelight from corner) stays CONSTANT across all 6 panels. This is NOT 6 separate illustrations but ONE continuous action broken into 6 key moments.

6 panel storyboard grid layout for video reference, 2 rows by 3 columns,
consistent character design across all panels,

Panel 1 (top-row-1): [Shot type], [Character] [detailed action with start-middle-end states, at least 100 words describing WHO/WHAT/WHERE/WHEN], [precise position in scene: left/center/right, distance from key scene elements], [expression and eye direction], [costume fabric texture and hair movement details], [scene environment with specific light source position], [camera angle and lens effect], [emotional tone of beginning], [this is the opening moment of the sequence]

Panel 2 (top-row-2): [Shot type], [Character] [action developing from Panel 1's end state, cause-effect chain clearly shown, at least 100 words], [position transition: moving from X to Y], [expression shift from previous], [costume dynamics in motion], [scene with same lighting setup], [camera movement], [building emotion], [continuing from Panel 1 where character was at position X]

Panel 3 (top-row-3): [Shot type], [Character] [action mid-point progression, at least 100 words], [new spatial relationship to scene elements], [expression evolution], [visual texture details], [same environment maintained], [camera technique], [mood development], [continuing the flow from Panel 2]

Panel 4 (bottom-row-1): [Shot type], [Character] [action approaching climax or major turning point, at least 100 words], [critical position in scene], [expression at peak intensity], [detailed costume action], [scene with dramatic lighting from same sources], [camera at most dynamic], [peak tension], [the payoff moment building from Panels 1-3]

Panel 5 (bottom-row-2): [Shot type], [Character] [action resolution beginning, aftermath of climax, at least 100 words], [position after climax moment], [expression transitioning from peak], [costume settling from motion], [scene atmosphere shifting], [camera stabilizing], [emotion processing], [consequence of Panel 4's action]

Panel 6 (bottom-row-3): [Shot type], [Character] [final frozen moment, complete resolution, at least 100 words], [final position in scene], [final expression holding], [costume at rest], [scene atmosphere resolved], [camera fixed on final composition], [emotional landing point], [the conclusive image that sums up the entire 8-second sequence]

unified art style across all panels, consistent character design, smooth action flow between panels, narrative continuity, spatial consistency maintained, same scene across all panels, continuous time flow,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9

需要严格按照 一行三个镜头图片，两行。这种排列方式去输出
\```

**负向提示词**:
\```
[NEGATIVE_PROMPT],
inconsistent style, mismatched characters, different art styles between panels,
bad anatomy, bad hands, missing fingers, extra limbs
\```

**需要上传的参考图**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色A]-三视图 | 角色一致性 |
| 参考图2 | [角色B]-三视图 | 角色一致性（如有） |
| 参考图3 | [场景名]-主图 | 场景一致性 |

---
```

### 10秒视频 - 8格布局

```markdown
### [K01/K02/...] 分镜参考图 - [视频名称]（10秒）

**用途**: 作为 [视频编号] 的参考图上传到 AI 视频生成工具

**布局**: 8格分镜（2行×4列）

**镜头概览**:
| 格子 | 时间点 | 内容概要 | 景别 |
|------|--------|----------|------|
| 1 | 0-1.25秒 | [开场动作] | [景别] |
| 2 | 1.25-2.5秒 | [发展动作] | [景别] |
| 3 | 2.5-3.75秒 | [转折动作] | [景别] |
| 4 | 3.75-5秒 | [推进动作] | [景别] |
| 5 | 5-6.25秒 | [高潮动作] | [景别] |
| 6 | 6.25-7.5秒 | [收尾动作] | [景别] |
| 7 | 7.5-8.75秒 | [结尾动作] | [景别] |
| 8 | 8.75-10秒 | [定格状态] | [景别] |

**提示词**:
\```
[STYLE_PREFIX],

IMPORTANT: This is a storyboard reference image for a SINGLE CONTINUOUS VIDEO SHOT. All 8 panels depict the SAME scene with SAME characters in a CONTINUOUS time flow of 10 seconds. Maintain PERFECT SPATIAL CONSISTENCY across all panels: character positions must flow logically from panel to panel, scene layout (door position, pillars, furniture, background elements) remains IDENTICAL in every panel, light source direction (moonlight angle from window, candlelight position in corner) stays CONSTANT across all 8 panels. This is NOT 8 separate illustrations but ONE continuous action broken into 8 key moments. Each panel is a frame from the same video, not independent artworks.

8 panel storyboard grid layout for video reference, 2 rows by 4 columns,
consistent character design across all panels,

Panel 1 (top-row-1): [Shot type], [Character] [detailed action with start-middle-end states, at least 100 words describing the opening moment: WHO is in the frame, WHAT are they doing, WHERE exactly in the scene, WHEN in the emotional arc], [precise position in scene: left/center/right third of frame, X meters from door/pillar/window], [expression and eye direction with micro-details], [costume fabric texture, folds, and hair movement details], [scene environment with specific light source positions marked], [camera angle, height, and lens effect], [emotional tone of beginning], [this is the opening moment that establishes everything]

Panel 2 (top-row-2): [Shot type], [Character] [action developing from Panel 1's end state, cause-effect chain clearly visible, at least 100 words], [position transition: character has moved from position X toward position Y], [expression shift showing reaction to previous moment], [costume dynamics showing ongoing motion], [same scene with identical lighting setup], [camera movement if any], [building emotion from opening], [continuing directly from Panel 1 where character was doing X at position Y]

Panel 3 (top-row-3): [Shot type], [Character] [action mid-point progression, momentum building, at least 100 words], [new spatial relationship to fixed scene elements], [expression evolution showing emotional journey], [visual texture details of motion], [same environment strictly maintained], [camera technique enhancing drama], [mood development], [the story continues from Panel 2's endpoint]

Panel 4 (top-row-4): [Shot type], [Character] [action approaching climax, tension building toward peak, at least 100 words], [critical position in scene relative to key elements], [expression intensifying with anticipation], [detailed costume in maximum motion], [scene with dramatic lighting from same fixed sources], [camera at most dynamic angle], [peak tension before release], [building to the climax that will pay off in Panel 5]

Panel 5 (bottom-row-1): [Shot type], [Character] [action at CLIMAX or major turning point, the KEY MOMENT of entire sequence, at least 100 words with maximum detail], [climax position: exactly where in scene this peak occurs], [peak emotional expression frozen at height of drama], [maximum visual detail of costume, hair, environment at this decisive instant], [scene at most dramatic with same lighting sources], [camera at most dynamic composition], [emotional explosion/turning point], [THE moment everything has been building toward from Panels 1-4]

Panel 6 (bottom-row-2): [Shot type], [Character] [action resolution BEGINNING, immediate aftermath of climax, at least 100 words], [position after climax moment, showing physical result], [expression transitioning from peak to processing], [costume settling from intense motion], [scene atmosphere shifting but same space], [camera stabilizing after climax], [emotion processing what just happened], [the first breath after the climax in Panel 5]

Panel 7 (bottom-row-3): [Shot type], [Character] [action winding down, consequences becoming clear, at least 100 words], [settling position in scene], [expression resolving toward final state], [visual quieting after drama], [environment settling to new equilibrium], [camera resting on meaningful composition], [mood conclusion forming], [the denouement following Panel 5's climax and Panel 6's aftermath]

Panel 8 (bottom-row-4): [Shot type], [Character] [final frozen moment, complete resolution, the IMAGE THAT SUMS UP EVERYTHING, at least 100 words], [final position in scene that feels like natural endpoint], [final expression holding the emotional conclusion], [costume at rest, hair settled], [scene atmosphere fully resolved], [camera fixed on final composition that feels complete], [emotional landing point the audience will remember], [the conclusive image that encapsulates the entire 10-second journey from Panel 1 to now]

unified art style across all panels, consistent character design, smooth action flow between panels, narrative continuity, spatial consistency strictly maintained, same scene across all panels, continuous time flow, cinematic progression, single video broken into 8 frames,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9

需要严格按照 一行四个镜头图片，两行。这种排列方式去输出
\```

**负向提示词**:
\```
[NEGATIVE_PROMPT],
inconsistent style, mismatched characters, different art styles between panels,
bad anatomy, bad hands, missing fingers, extra limbs
\```

**需要上传的参考图**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色A]-三视图 | 角色一致性 |
| 参考图2 | [角色B]-三视图 | 角色一致性（如有） |
| 参考图3 | [场景名]-主图 | 场景一致性 |

---
```

### 5秒视频 - 4格布局

```markdown
### [K0X/V0X] 分镜参考图 - [视频名称]（5秒）

**用途**: 作为 [视频编号] 的参考图上传到 AI 视频生成工具

**布局**: 4格分镜（2行×2列）

**镜头概览**:
| 格子 | 时间点 | 内容概要 | 景别 |
|------|--------|----------|------|
| 1 | 0-1.25秒 | [开场动作] | [景别] |
| 2 | 1.25-2.5秒 | [发展动作] | [景别] |
| 3 | 2.5-3.75秒 | [高潮动作] | [景别] |
| 4 | 3.75-5秒 | [结尾状态] | [景别] |

**提示词**:
\```
[STYLE_PREFIX],

IMPORTANT: This is a storyboard reference image for a SINGLE CONTINUOUS VIDEO SHOT. All 4 panels depict the SAME scene with SAME characters in a CONTINUOUS time flow of 5 seconds. Maintain PERFECT SPATIAL CONSISTENCY across all panels: character positions must flow logically from panel to panel, scene layout remains IDENTICAL in every panel, light source direction stays CONSTANT across all 4 panels. This is NOT 4 separate illustrations but ONE continuous action broken into 4 key moments.

4 panel storyboard grid layout for video reference, 2 rows by 2 columns,
consistent character design across all panels,

Panel 1 (top-row-1): [Shot type], [Character] [detailed action with start-middle-end states, at least 100 words describing WHO/WHAT/WHERE/WHEN], [precise position in scene: left/center/right, distance from key scene elements], [expression and eye direction with details], [costume fabric texture and hair movement], [scene environment with specific light source positions], [camera angle and lens effect], [emotional tone of beginning], [the opening that establishes the sequence]

Panel 2 (top-row-2): [Shot type], [Character] [action developing from Panel 1's end state, cause-effect chain, at least 100 words], [position transition from X to Y], [expression shift], [costume dynamics in motion], [same scene with identical lighting], [camera movement if any], [building emotion], [continuing from Panel 1 where character ended at position X]

Panel 3 (bottom-row-1): [Shot type], [Character] [action at CLIMAX or turning point, at least 100 words], [climax position in scene], [peak emotional expression], [maximum visual detail], [scene at most dramatic with same light sources], [camera at most dynamic], [emotional explosion], [THE key moment everything builds toward]

Panel 4 (bottom-row-2): [Shot type], [Character] [final frozen moment, complete resolution, at least 100 words], [final position in scene], [final expression holding conclusion], [costume at rest], [scene atmosphere resolved], [camera fixed on final composition], [emotional landing point], [the conclusive image that sums up the entire 5-second sequence]

unified art style across all panels, consistent character design, smooth action flow between panels, narrative continuity, spatial consistency maintained, same scene across all panels, continuous time flow,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9

需要严格按照 一行两个镜头图片，两行。这种排列方式去输出
\```

**负向提示词**:
\```
[NEGATIVE_PROMPT],
inconsistent style, mismatched characters, different art styles between panels,
bad anatomy, bad hands, missing fingers, extra limbs
\```

**需要上传的参考图**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色]-三视图 | 角色一致性 |
| 参考图2 | [场景名]-主图 | 场景一致性 |

---
```

---

## 描述要素清单

### 每格必须包含的要素

1. **角色** (Character)
   - 角色名称
   - 关键外观特征（发型、服装颜色）

2. **位置** (Position)
   - 画面中的位置（左侧/中央/右侧）
   - 与环境的关系（靠墙/中央/门口等）

3. **动作** (Action)
   - 正在进行的动作
   - 动作的起始/中间/结束状态

4. **表情** (Expression)
   - 面部表情描述
   - 眼神方向

5. **场景** (Scene)
   - 环境简述
   - 光线状态

6. **景别** (Shot Type)
   - 远景/中景/近景/特写

### 英文关键词参考

| 中文 | 英文 |
|------|------|
| 远景 | wide shot / establishing shot |
| 全景 | full shot |
| 中景 | medium shot |
| 中近景 | medium close-up |
| 近景 | close-up |
| 特写 | extreme close-up |
| 仰拍 | low angle |
| 俯拍 | high angle / overhead shot |
| 平视 | eye level |

---

## 文件尾部

```markdown
---

## 使用流程

1. **生成分镜图片**: 将每个视频的提示词复制到 Nano Banana Pro
2. **保存图片**: 保存为 [视频编号]-分镜参考.png
3. **上传到视频工具**:
   - Veo: 作为 Reference Images 上传
   - 可灵: 作为风格参考上传
4. **生成视频**: 输入视频提示词，使用分镜图作为视觉参考

---

*由 AI分镜拼图师 生成*
```
