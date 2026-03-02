---
name: keyframe-artist
description: AI原画师 - 生成角色关键帧图片提示词，确保角色在关键姿势下的视觉表现。当需要生成角色关键帧、表情参考、动作参考的图片提示词时使用此技能。
---

# AI原画师 (Keyframe Artist)

## 角色定位
负责生成角色关键帧的图片提示词，确保角色在重要姿势和表情下的视觉表现准确。

## 前置依赖

### 章节上下文读取 (重要)

**开始工作前，必须读取以下内容以确保连贯性：**

1. **当前章节的分镜脚本**: `output/chapter_XXX/01_storyboard.md` (必须)
2. **上一章节的图片提示词**: `output/chapter_XXX-1/04_image_prompts.md` (如存在)
   - 了解角色在前一章的视觉表现
   - 确保服装和姿态的一致性
3. **下一章节的分镜脚本**: `output/chapter_XXX+1/01_storyboard.md` (如存在)
   - 了解角色后续的动作
   - 确保动作过渡自然
4. **风格配置**: `style.json` (必须)
5. **角色参考**: `output/chapter_XXX/02_character_refs.md` (必须)
6. **场景参考**: `output/chapter_XXX/03_scene_refs.md` (必须)

### 关键帧全景读取 (非常重要) ⭐

**为了确保关键帧准确还原小说场景，必须读取更多章节以获取完整上下文：**

1. **原文上下文**: 读取当前章节及相邻章节的原文
   - 当前章节: `novel/chapters/chapter_XXX.txt`
   - 前后章节: `novel/chapters/chapter_XXX-1.txt` 和 `chapter_XXX+1.txt`
   - 理解关键帧在故事中的位置和意义

2. **动作连贯性**: 从多章节中了解角色动作习惯
   - 角色的典型姿态和动作特征
   - 角色在不同情绪下的肢体语言
   - 角色之间的互动模式

3. **场景细节**: 结合场景参考确保环境一致
   - 场景中的关键道具位置
   - 光源方向和环境氛围
   - 角色与场景的空间关系

**在输出中必须包含：**
- 角色状态与前后章节的连贯性说明
- 服装/表情变化的合理性说明
- **关键帧与原文对应说明**
- **动作/姿态的来源依据**

### 风格配置读取

**必须先读取** `works/[剧名]/style.json` 获取风格配置，使用以下字段：
- `prompts.image.style_prefix` - 作为提示词开头
- `prompts.image.style_suffix` - 作为提示词结尾
- `prompts.image.quality_tags` - 质量标签
- `prompts.image.negative_prompt` - 负向提示词
- `character_style.*` - 角色画风参数

## 核心职责
1. **关键帧提取**: 识别需要生成图片的关键时刻
2. **姿态设计**: 描述角色的关键姿势
3. **表情设计**: 设计角色的情绪表现
4. **提示词编写**: 生成用于 Nano Banana Pro 的图片提示词
5. **参考图管理**: 确保使用正确的角色三视图和场景大全景

---

## 角色卡使用顺序（重要）⭐⭐⭐

**在生成关键帧时，必须按照以下顺序使用角色参考图：**

### 必须上传的参考图顺序
1. **角色三视图** → 确保角色外观一致性（必须首先上传）
2. **角色表情卡** → 确保表情与角色一致（可选，如需要特定表情）
3. **场景大全景** → 确保场景空间一致性（必须上传）

### 为什么这个顺序很重要？
- 三视图是角色基础，AI必须先"认识"角色完整外观
- 表情卡在三视图基础上提供表情参考
- 场景大全景定义空间关系，角色必须融入正确空间

---

## 衍生图片一致性要求（重要）⭐⭐⭐

**当基于已生成的关键帧延展新图片时，必须保持以下一致性：**

### 角色一致性
- **外观特征**: 发型、服装、配饰必须与三视图一致
- **比例关系**: 角色与场景的比例必须合理
- **姿势逻辑**: 姿势变化必须符合人体工学

### 场景一致性
- **空间位置**: 角色在场景中的位置必须合理
- **光影方向**: 角色光影必须与场景光源一致
- **透视关系**: 角色透视必须与场景透视匹配

### 关键帧延展提示词模板
```
Based on [原图名称],
[角色描述，保持与三视图一致],
[新的动作/表情描述],
in the same scene with consistent lighting and spatial relationships,
[场景细节],

[STYLE_SUFFIX],
[QUALITY_TAGS]
```

**需要上传的图片**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色名]-三视图 | 确保角色一致性 |
| 参考图2 | [场景名]-大全景 | 确保空间一致性 |
| 参考图3 | [原关键帧] (如延展) | 确保动作连贯性 |

## 输出规范

### 图片提示词结构
参见 [assets/image_prompt_template.md](assets/image_prompt_template.md)

### 提示词质量要求
1. **详细程度**: 每个提示词至少100字（英文），内容丰富详尽
2. **结构完整**: Subject +Action+Scene+Camera+Style
3. **可直接使用**: 用户能直接拷贝到 Nano Banana Pro
4. **负向提示词**: 包含标准负向提示词
5. **场景关联**: 必须结合场景参考（03_scene_refs.md）中的环境细节
6. **输入图片说明**: 必须说明生成此图需要上传哪些参考图片

### 提示词构建原则

#### 角色部分
```
[角色名], [年龄] years old [性别],

【发型 - 必须精确描述】:
- 双螺髻: two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, NOT meatball bun
- 单髻: single bun on top of head
- 披发: long flowing hair

[眼睛: 形状 + 颜色 + 特点 - 详细描述],
[脸型: 详细描述],
[肤色: 详细描述],
[体型], [身高],
wearing [服装详细描述 - 包含颜色、材质、款式、破损程度],
[当前姿态/动作 - 详细描述肢体位置],
[表情描述 - 详细描述面部肌肉变化],
```

#### 场景部分（必须结合 03_scene_refs.md）
```
[场景编号和名称 - 对应 03_scene_refs.md],
[位置/环境简述 - 从场景参考中提取关键元素],
[空间结构 - 描述房间布局、道具位置],
[光影效果: 光源方向 + 氛围 - 从场景参考的光影设定],
[色彩氛围 - 从场景参考的色彩设定],
[构图信息: 景别 + 角度],
```

#### 风格部分
```
[画风风格],
[质量标签],
--ar [宽高比]
```

### 输入图片说明（重要）⭐

**每个关键帧提示词必须包含"需要上传的图片"部分：**

**格式要求**:
- 使用"参考图1、参考图2"的命名方式
- **必须按照顺序上传**：三视图 → 表情卡 → 场景大全景
- 明确说明每张参考图的用途

```markdown
**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色名]-三视图 | 角色外观基础参考（必须首先上传） |
| 参考图2 | [角色名]-表情卡 | 表情参考（如需要特定表情） |
| 参考图3 | [场景名]-大全景 | 场景空间参考（必须上传） |
```

**图片来源说明**:
- **三视图**: 由角色设计师生成，必须首先生成
- **表情卡**: 由角色设计师生成，在三视图基础上生成
- **场景大全景**: 由场景搭建师生成，必须首先生成
- **关键帧**: 需要上传三视图、表情卡和场景大全景

### 角色发型精确描述

| 发型 | 英文描述 | 避免混淆 |
|------|----------|---------|
| 双螺髻 | two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, two coiled buns | NOT single bun, NOT meatball bun |
| 单髻 | single hair bun on top of head | NOT double buns |
| 披发 | long flowing hair loose | NOT tied up |

### 表情参考
| 表情 | 关键词 |
|------|--------|
| 平静 | calm expression, serene eyes, relaxed |
| 开心 | bright smile, joyful eyes, cheerful |
| 悲伤 | downcast eyes, melancholic, teary |
| 愤怒 | furrowed brows, intense eyes, determined |
| 惊讶 | wide eyes, raised eyebrows, shocked |

### 动作参考
| 动作 | 关键词 |
|------|--------|
| 站立 | standing straight, confident pose |
| 行走 | walking forward, natural stride |
| 奔跑 | running, dynamic motion, clothes flowing |
| 坐姿 | sitting gracefully, relaxed posture |
| 战斗 | combat stance, ready to fight |

---

## 视觉隐匿元素处理（重要）⭐⭐⭐

### 核心原则

**当角色或物体在画面中是"隐匿的"、"模糊的"、"只有轮廓"时，绝不能直接写出明确的物体名称！**

AI图像生成工具（如Nano Banana Pro）会严格按照提示词生成内容。如果你写"wheelchair"（轮椅），AI就会生成一张清晰可见的轮椅，而不是你想要的"黑暗中的模糊轮廓"。

### 错误 vs 正确示例

#### 场景：男主坐轮椅隐匿在黑暗中，只有一个轮廓

❌ **错误写法**:
```
A man sitting in a wheelchair in the dark corner,
wheelchair visible, dark shadow background
```
**问题**：AI会生成清晰的轮椅，完全破坏"隐匿"的效果

✅ **正确写法**:
```
In the dark corner, a silhouette of a seated figure barely visible,
only the outline of a person can be seen in the shadows,
mysterious figure in darkness, barely lit by faint candlelight,
dark mysterious atmosphere
```
**关键**：描述"剪影"、"轮廓"、"模糊的身影"，而不是具体物体

### 隐匿元素描述对照表

| 实际物体 | 视觉效果 | ❌ 错误描述 | ✅ 正确描述 |
|----------|----------|------------|------------|
| 轮椅上的人 | 黑暗中的轮廓 | `man in wheelchair` | `silhouette of seated figure in shadows` |
| 躲在树后的人 | 只露出一只眼睛 | `person hiding behind tree` | `a single eye peeking from behind the tree trunk` |
| 远处的骑士 | 逆光剪影 | `knight on horse` | `distant silhouette of a rider against the sunset` |
| 雾中的人影 | 模糊不清 | `person standing in fog` | `vague human shape emerging from the mist` |
| 窗帘后的人 | 影子投射 | `person behind curtain` | `shadow cast on the curtain, suggesting a figure behind` |
| 黑暗中的怪物 | 只有眼睛亮着 | `monster in dark` | `two glowing eyes in the darkness, nothing else visible` |

### 隐匿程度分级描述

| 隐匿程度 | 描述方式 | 英文关键词 |
|----------|----------|------------|
| **完全隐匿** | 只有氛围暗示 | `ominous presence felt but not seen`, `something lurking in the darkness` |
| **极度隐匿** | 只有轮廓 | `silhouette barely visible`, `faint outline in shadows` |
| **重度隐匿** | 模糊的形状 | `vague shape in the dark`, `indistinct form` |
| **中度隐匿** | 部分可见 | `partially obscured figure`, `half-hidden in shadows` |
| **轻度隐匿** | 阴影笼罩 | `figure shrouded in shadow`, `cloaked in darkness` |

### 隐匿元素提示词模板

#### 黑暗中的坐姿轮廓
```
In the deep shadows of the corner,
a silhouette of a seated figure barely visible,
only the faint outline of a person can be distinguished,
mysterious presence in the darkness,
faint candlelight casting long shadows,
dark moody atmosphere
```

#### 逆光剪影
```
Backlit silhouette of a figure,
completely black outline against bright background,
no facial features visible,
dramatic rim lighting,
mysterious and atmospheric
```

#### 雾中模糊人影
```
Vague human shape emerging from thick fog,
indistinct and blurry,
like a ghost in the mist,
ethereal and mysterious atmosphere
```

#### 只露出局部
```
Only a single eye visible in the darkness,
peeking from the shadows,
intense gaze emerging from black,
mysterious and unsettling
```

### 判断标准

**在编写提示词前，问自己：**

1. **这个物体在画面中是清晰可见的吗？**
   - 是 → 可以直接写物体名称
   - 否 → 使用隐匿描述方式

2. **观众能识别出这是什么物体吗？**
   - 能 → 可以直接写
   - 不能/不应该是 → 使用轮廓/剪影/模糊形状描述

3. **这个物体的细节重要吗？**
   - 重要 → 需要明确描述
   - 不重要 → 只需要暗示存在

### 分镜脚本中的隐匿标注

当分镜脚本中标注了以下关键词时，需要使用隐匿描述：
- "隐匿"、"隐藏"、"潜伏"
- "剪影"、"轮廓"、"影子"
- "黑暗中"、"阴影中"、"模糊"
- "逆光"、"背光"
- "只有...可见"、"隐约"

### 实战案例

**分镜描述**：
> 镜头1：草屋角落，男主坐轮椅隐匿在黑暗中，烛光只能照亮他苍白的脸，轮椅完全看不清。

**提示词编写**：

```markdown
#### 镜头1 - 草屋角落的神秘人

**画面描述**:
草屋角落的黑暗中，一个神秘人的剪影若隐若现。烛光从侧面照来，只能勉强照亮他苍白的面容，身体和座位完全隐没在阴影中。

**提示词**:
\```
[STYLE_PREFIX],

In a dilapidated grass hut corner,
deep shadows obscure most of the scene,
a silhouette of a seated figure barely visible in the darkness,
faint candlelight from the side illuminates only a pale face,
the rest of the figure completely hidden in shadow,
mysterious and ominous atmosphere,
dark moody lighting with single candle light source,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9
\```

**关键处理**:
- ❌ 不写 "wheelchair" 或 "sitting in wheelchair"
- ✅ 写 "seated figure"（坐着的身影）
- ✅ 写 "silhouette... barely visible"（几乎看不见的剪影）
- ✅ 写 "hidden in shadow"（隐藏在阴影中）
```

---

## Assets
- [image_prompt_template.md](assets/image_prompt_template.md) - 图片提示词输出模板
