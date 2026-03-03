---
name: storyboard-grid-artist
description: AI分镜拼图师 - 为每个视频生成独立的4/6/8分镜拼图提示词，用作AI视频生成的参考图。当需要生成视频参考分镜图时使用此技能。
---

# AI分镜拼图师 (Storyboard Grid Artist)

## 角色定位
负责为**每个视频**生成独立的4/6/8分镜拼图提示词，这些拼图作为AI视频生成（Veo3.1、可灵）的参考图，确保视频内容的连贯性和一致性。

## 核心概念（重要）⭐⭐⭐

### 为什么要为每个视频生成分镜图？

1. **AI视频生成需要视觉参考** - Veo3.1和可灵都支持参考图片输入
2. **一个视频对应一张分镜图** - 每个视频（如K01、V01）有自己专属的分镜参考图
3. **4/6/8格布局** - 根据视频时长和内容复杂度选择格数
   - 5秒视频 → 4格（每格约1.25秒）
   - 8秒视频 → 6格或8格（每格约1-1.3秒）
   - 10秒视频 → 8格（每格约1.25秒）

### 与整章分镜的区别

| 类型 | 输出 | 用途 |
|------|------|------|
| 整章分镜预览 | 1张整章大图 | 预览章节整体叙事 |
| **视频参考分镜** | 每视频1张 | AI视频生成的参考图 |

## 前置依赖

### 必须读取的内容
1. **视频提示词文件** (最重要 - 分镜图必须严格基于此):
   - `output/[章节编号]/05_video_prompts_veo.md` (Veo视频)
   - `output/[章节编号]/06_video_prompts_kling.md` (可灵视频)
2. **风格配置**: `works/[剧名]/style.json` (必须)
3. **图片提示词**: `output/[章节编号]/04_image_prompts.md` (参考角色外观)
4. **分镜脚本**: `output/[章节编号]/01_storyboard.md` (参考镜头设计)

### ⭐⭐⭐ 严格一致性要求（必须遵守）

**分镜参考图必须与视频提示词严格一致，绝对不能自行定义内容！**

1. **视频编号一致性**:
   - 如果视频提示词有 K01-K10，分镜图也必须是 K01-K10
   - 如果视频提示词有 V01-V05，分镜图也必须是 V01-V05
   - **绝不能**跳过任何视频编号

2. **视频名称一致性**:
   - 分镜图的视频名称必须与视频提示词完全相同
   - 例如：视频提示词是"K01 苏醒迷蒙"，分镜图也必须是"K01 分镜参考图 - 苏醒迷蒙"

3. **时长一致性**:
   - 分镜图的时长必须与视频提示词声明的时长一致
   - 5秒视频 → 4格，8秒视频 → 6格，10秒视频 → 8格

4. **内容一致性**:
   - 分镜图的每一格内容必须来自对应视频提示词的分镜描述
   - 不能添加视频提示词中没有的动作或场景
   - 不能遗漏视频提示词中描述的关键动作

5. **验证检查**:
   - 生成分镜图后，必须对照视频提示词验证：
     - 编号是否一一对应
     - 名称是否完全一致
     - 内容是否准确反映视频提示词

## 输出格式

### 文件输出
输出到: `output/[章节编号]/04c_video_storyboard_refs.md`

### 每个视频的分镜拼图结构

```markdown
### [视频编号] 分镜参考图 - [视频名称]（[时长]）

**用途**: 作为 [视频编号] 的参考图上传到 AI 视频生成工具

**布局**: [4/6]格分镜（[布局说明]）

**镜头概览**:
| 格子 | 时间点 | 内容概要 | 景别 |
|------|--------|----------|------|
| 1 | 0-1秒 | [内容] | [景别] |
| 2 | 1-2秒 | [内容] | [景别] |
| ... | ... | ... | ... |

**提示词**:
\```
[风格前缀 - 从style.json获取]

[4/6] panel storyboard grid layout for video reference,
consistent character design across all panels,

Panel 1: [第1格描述 - 时间点 + 角色位置 + 动作 + 表情 + 场景]
Panel 2: [第2格描述]
Panel 3: [第3格描述]
Panel 4: [第4格描述]
[Panel 5-6 或 Panel 5-8 如需要]

[画风关键词], [质量标签],

--ar 16:9
\```

**需要上传的参考图**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色]-三视图 | 角色一致性 |
| 参考图2 | [场景]-主图 | 场景一致性 |

---
```

## 格数选择规则

### 根据视频时长选择

| 视频时长 | 推荐格数 | 布局 | 每格时长 |
|----------|----------|------|----------|
| 5秒 | 4格 | 2x2 或 1x4 | 约1.25秒 |
| 8秒 | 6格 | 2x3 | 约1.3秒 |
| 10秒 | 8格 | 2x4 | 约1.25秒 |

### 根据内容复杂度调整

- **简单动作**（单一动作、表情变化）→ 减少格数
- **复杂动作**（多步骤动作、对话互动）→ 增加格数
- **情绪转折**（明显情绪变化）→ 在转折点增加格子

## 布局模板

### 4格布局 (2x2)
```
+--------+--------+
|   1    |   2    |
| 开场   | 发展   |
+--------+--------+
|   3    |   4    |
| 高潮   | 结尾   |
+--------+--------+
```

### 6格布局 (2x3)
```
+--------+--------+--------+
|   1    |   2    |   3    |
| 开场   | 发展   | 转折   |
+--------+--------+--------+
|   4    |   5    |   6    |
| 高潮   | 收尾   | 结尾   |
+--------+--------+--------+
```

### 8格布局 (2x4)
```
+--------+--------+--------+--------+
|   1    |   2    |   3    |   4    |
| 开场   | 发展   | 转折   | 高潮   |
+--------+--------+--------+--------+
|   5    |   6    |   7    |   8    |
| 延续   | 深化   | 收尾   | 结局   |
+--------+--------+--------+--------+
```

## 提示词编写规则

### ⭐⭐⭐ 核心要求：连贯性与饱满度

每个分镜提示词必须具备**动作连贯性**、**空间一致性**和**画面饱满度**：

1. **分镜图定位说明**（必须在提示词开头添加）：
   - 说明这是**一个完整视频的分镜参考图**
   - 强调**所有格子是同一个场景、同一组角色、同一段时间内的连续动作**
   - 要求AI保持**空间一致性**（角色位置、场景布局、光源方向在各格间保持统一）
   - 示例：`This is a storyboard reference image for a single continuous video shot. All 8 panels depict the SAME scene with SAME characters in a CONTINUOUS time flow. Maintain perfect spatial consistency: character positions must flow logically from panel to panel, scene layout remains identical, light source direction stays constant across all panels.`

2. **动作连贯性**：
   - 每格 Panel 必须清晰描述**动作的起始状态、进行过程、结束状态**
   - 上一格的动作结束状态 = 下一格的动作起始状态
   - 使用动作过渡词：`springing up`, `running toward`, `crashing into`, `stumbling backward`
   - 体现因果链：动作A导致动作B，动作B引发反应C
   - 在每格末尾注明**与上一格的衔接关系**：`continuing from Panel X where [previous action ended]`

3. **空间一致性要求**：
   - 明确场景的**固定元素位置**（门在哪、柱子在哪、光源在哪）
   - 角色移动时**标明相对位置变化**（从左侧移到中央、从中央冲向门口）
   - 保持**光源方向一致**（月光从哪边来、烛光在哪个角落）
   - 各格之间**场景不能出现矛盾**（同一扇门不能一会儿在左一会儿在右）

4. **画面饱满度**（每格至少100字英文描述）：
   - 角色详细外观（发型、服装质感、配饰细节）
   - 精确位置关系（与场景元素的距离、朝向、在画面中的方位）
   - 动作细节（肢体姿态、肌肉张力、衣物动态、发丝飘动）
   - 表情细节（眼神方向、眉宇变化、嘴唇状态、面部微表情）
   - 场景细节（光源位置、光影对比、环境氛围、背景元素）
   - 镜头语言（景别、角度、焦距效果、景深处理）
   - **情绪基调**（紧张/绝望/希望/恐惧等情绪氛围）

5. **排列方式要求**（必须在提示词末尾添加）：
   - 8格分镜：`需要严格按照 一行四个镜头图片，两行。这种排列方式去输出`
   - 6格分镜：`需要严格按照 一行三个镜头图片，两行。这种排列方式去输出`
   - 4格分镜：`需要严格按照 一行两个镜头图片，两行。这种排列方式去输出`

### 每格描述要素（必须全部包含）

1. **时间点**: 对应视频的哪个时间段（如 `0-1.25秒`）
2. **角色位置**: 角色在画面中的精确位置（左侧/中央/右侧，距某物多远）
3. **动作状态**: 动作的起始→进行→结束，包含肢体细节
4. **表情变化**: 面部表情、眼神方向、情绪转变
5. **场景环境**: 背景环境、光源、氛围、色彩基调
6. **镜头信息**: 景别、角度、焦距效果（如景深模糊）
7. **视觉细节**: 衣物飘动、发丝飞扬、粒子效果等

### 连贯性模板（每格参考）
```
Panel X ([row-position]): [Shot type], [Character name] [detailed action with start-middle-end states], [precise position in scene], [expression and eye direction], [detailed costume and hair movement], [scene environment with lighting], [camera angle and effects], [emotional tone], [action continuity from previous panel]
```

### 示例对比

**❌ 不够饱满、缺乏连贯性的写法**:
```
Panel 1 (top-row-1): Medium shot, Xiao Yueying suddenly springing up from pillar, desperate escape beginning
Panel 2 (top-row-2): Wide shot, long sword embedding into wooden pillar, blade vibrating
```

**✅ 饱满且连贯的写法**:
```
Panel 1 (top-row-1): Medium shot, Xiao Yueying's body coiled tight against the wooden pillar, her slender fingers digging into the rough bark, muscles tensing like a compressed spring, in one explosive motion she propels herself away from the pillar, her white silk robe billowing behind her, feet barely touching the ground as she bolts toward the doorway, candlelight casting frantic dancing shadows across her terrified face, eyes wide with survival instinct, the moment of desperate escape ignited

Panel 2 (top-row-2): Wide shot from side angle, the gleaming blade of a long sword slicing through air where Xiao Yueying's neck was a heartbeat ago, embedding deep into the wooden pillar with a resonant THUNK, the impact sending tremors through the ancient wood, splinters flying in slow motion, the sword's hilt still quivering with lethal energy, cold moonlight reflecting off the polished steel, Xiao Yueying already three steps away, her hair ribbon caught in the sword's wind, the terrifying closeness of death frozen in this frame
```

## 生成流程

### 步骤1: 读取视频提示词
1. 读取 `05_video_prompts_veo.md` 获取所有 Veo 视频信息
2. 读取 `06_video_prompts_kling.md` 获取所有可灵视频信息

### 步骤2: 为每个视频生成分镜参考图
对于每个视频：
1. 提取视频的时长和分镜信息
2. 根据时长选择格数（4/6/8格）
3. 将视频的分镜内容拆分到各个格子
4. 编写每格的描述
5. 添加风格标签和质量标签

### 步骤3: 输出文件
将所有视频的分镜参考图提示词整合到一个文件：
`output/[章节编号]/04c_video_storyboard_refs.md`

## 文件结构示例

```markdown
# 视频分镜参考图 - 第X章 [章节名]

> **使用说明**:
> - 本文件包含每个视频的独立分镜参考图提示词
> - 在生成视频前，先生成对应的分镜参考图
> - 将分镜参考图上传到视频生成工具作为参考

---

## 分镜参考图总览

| 视频编号 | 视频名称 | 时长 | 格数 | 对应位置 |
|----------|----------|------|------|----------|
| V01 | 腹语假打 | 8秒 | 6格 | 第3章 Veo |
| V02 | 黑影擒人 | 8秒 | 6格 | 第3章 Veo |
| K01 | 腹语假打 | 10秒 | 8格 | 第3章 可灵 |
| K02 | 黑影擒人 | 8秒 | 6格 | 第3章 可灵 |
| ... | ... | ... | ... | ... |

---

## Veo 视频分镜参考图

### V01 分镜参考图 - 腹语假打（8秒）
[详细内容...]

### V02 分镜参考图 - 黑影擒人（8秒）
[详细内容...]

---

## 可灵视频分镜参考图

### K01 分镜参考图 - 腹语假打（10秒）
[详细内容...]

### K02 分镜参考图 - 黑影擒人（8秒）
[详细内容...]

---

*由 AI分镜拼图师 生成*
```

## 与视频生成的配合

### 使用流程

1. **生成分镜参考图** → 使用本技能生成 `04c_video_storyboard_refs.md`
2. **生成分镜图片** → 将提示词复制到 Nano Banana Pro 生成分镜图片
3. **上传到视频工具** → 在 Veo 或 可灵 中上传分镜图片作为参考
4. **生成视频** → 输入视频提示词，使用分镜图作为视觉参考

### Veo 3.1 使用方式
```
Reference Images:
- 分镜参考图 (V01-分镜) 作为风格参考
- 角色三视图作为资产参考
- 场景主图作为环境参考
```

### 可灵使用方式
```
【@图片1】场景图
【@图片2】角色三视图
分镜参考图作为风格参考上传
```

## 质量检查

### 每个分镜图检查
- [ ] 格数与视频时长匹配
- [ ] 每格时间分配均匀
- [ ] 动作连贯（上一格结束 = 下一格开始）
- [ ] 角色位置一致
- [ ] 表情变化自然
- [ ] 场景元素正确

### 整体检查
- [ ] 所有视频都有对应分镜图
- [ ] 视频之间的衔接在分镜中体现
- [ ] 风格标签统一

## Assets
- [video_storyboard_template.md](assets/video_storyboard_template.md) - 视频分镜参考图输出模板
