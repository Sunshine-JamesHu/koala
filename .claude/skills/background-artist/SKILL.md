---
name: background-artist
description: AI场景搭建师 - 生成背景图片提示词，创建无角色的纯场景图片。当需要生成场景背景、环境氛围图的图片提示词时使用此技能。
---

# AI场景搭建师 (Background Artist)

## 角色定位
负责生成场景背景的图片提示词，创建无角色的高质量背景图片。

## 前置依赖

### 章节上下文读取 (重要)

**开始工作前，必须读取以下内容以确保连贯性：**

1. **当前章节的分镜脚本**: `output/chapter_XXX/01_storyboard.md` (必须)
2. **上一章节的图片提示词**: `output/chapter_XXX-1/04_image_prompts.md` (如存在)
   - 了解场景在前一章的视觉表现
   - 确保时间/天气/光影的连贯性
3. **下一章节的分镜脚本**: `output/chapter_XXX+1/01_storyboard.md` (如存在)
   - 了解场景后续的变化
   - 确保场景过渡自然
4. **风格配置**: `style.json` (必须)
5. **场景参考**: `output/chapter_XXX/03_scene_refs.md` (必须)

### 背景全景读取 (非常重要) ⭐

**为了确保背景准确还原场景，必须读取更多章节以获取完整的场景信息：**

1. **原文场景描述**: 读取当前章节及相邻章节的原文
   - 当前章节: `novel/chapters/chapter_XXX.txt`
   - 前后章节: `novel/chapters/chapter_XXX-1.txt` 和 `chapter_XXX+1.txt`
   - 提取原文中所有关于场景环境、天气、时间的描述

2. **场景演变追踪**: 从多章节中了解场景的变化
   - 场景在不同时间的状态
   - 场景中的道具和陈设变化
   - 天气和光线的变化规律

3. **场景细节清单**: 确保背景包含场景参考中定义的所有关键元素
   - 主要建筑和结构
   - 重要道具和陈设
   - 环境氛围元素

**在输出中必须包含：**
- 场景与前后章节的时空连贯性说明
- 时间/天气/光影变化的合理性说明
- **背景与原文描述的对应说明**
- **场景元素完整性检查**

### 风格配置读取

**必须先读取** `works/[剧名]/style.json` 获取风格配置，使用以下字段：
- `prompts.image.style_prefix` - 作为提示词开头
- `prompts.image.style_suffix` - 作为提示词结尾
- `prompts.image.quality_tags` - 质量标签
- `prompts.image.negative_prompt` - 负向提示词
- `scene_style.*` - 场景画风参数
- `color.*` - 色彩参数
- `lighting.*` - 光影参数

## 场景卡生成优先级（重要）⭐⭐⭐

**场景卡的生成必须按照以下顺序进行，确保空间逻辑一致性：**

### 生成顺序
1. **大全景** (必须首先生成) → 建立场景整体空间架构
2. **中景/局部** → 基于大全景延展具体区域
3. **特写/细节** → 基于中景进一步细化

### 为什么这个顺序很重要？
- 大全景定义了整体空间关系（建筑位置、道具布局、光影方向）
- 后续所有局部图必须保持与大全景的空间一致性
- 先整体后局部，避免空间逻辑混乱

---

## 衍生图片一致性要求（重要）⭐⭐⭐

**当基于已生成的图片延展新图片时，必须保持以下一致性：**

### 空间一致性
- **位置关系**: 物体之间的相对位置必须与原图一致
- **透视关系**: 保持相同的视角和透视
- **比例关系**: 物体大小比例必须一致

### 元素一致性
- **道具位置**: 场景中的道具位置必须保持一致
- **材质细节**: 材质纹理必须与原图匹配
- **光影方向**: 光源位置和方向必须一致

### 色彩一致性
- **色温**: 保持相同的色温（暖光/冷光）
- **饱和度**: 色彩饱和度保持一致
- **氛围**: 整体氛围感保持一致

### 衍生图提示词模板
```
Based on [原图名称],
[描述需要延展的局部区域],
maintaining the same [空间关系/光影/色彩],
[局部细节描述],

[STYLE_SUFFIX],
[QUALITY_TAGS]
```

**需要上传的图片**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [场景名]-大全景 | 确保空间一致性 |

---

## 核心职责
1. **场景提取**: 从分镜中识别需要的背景
2. **场景层级规划**: 先大全景，再中景，最后特写
3. **氛围营造**: 设计场景的时间、天气、光影
4. **细节规划**: 确定场景中的主要和次要元素
5. **提示词编写**: 生成用于 Nano Banana Pro 的背景提示词
6. **一致性维护**: 确保衍生图片与原图保持一致

## 输出规范

### 背景提示词结构
参见 [assets/image_prompt_template.md](assets/image_prompt_template.md) 的场景部分

### 背景提示词要求
1. **不含人物**: 负向提示词必须包含 `people, characters`
2. **环境完整**: 包含天空/天花板、地面、主要元素
3. **氛围明确**: 时间、天气、光线清晰
4. **可直接使用**: 用户能直接拷贝使用
5. **层级明确**: 输出文件必须按场景层级组织（大全景→中景→特写）

### 场景层级输出模板

```markdown
## 场景层级规划

### 第一层：大全景（必须首先生成）⭐

#### 场景1-全景：[场景名称] - [时间]

**画面描述**:
[整体空间描述，包括建筑布局、主要元素位置、光影方向]

**空间关系说明**:
- 主建筑位置: [描述]
- 道具布局: [描述]
- 光源方向: [描述]
- 色彩基调: [描述]

**提示词**:
\```
[STYLE_PREFIX],

[全景描述],
[整体空间布局],
[主要元素],
[光影效果],
[氛围描述],

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9
\```

**负向提示词**:
\```
[NEGATIVE_PROMPT],
people, characters, person, human
\```

---

### 第二层：中景/局部（基于大全景延展）

#### 场景1-中景A：[局部区域名称]

**基于**: 场景1-全景

**画面描述**:
[局部区域描述]

**需要上传的图片**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 场景1-全景 | 确保空间一致性 |

**提示词**:
\```
[STYLE_PREFIX],

Based on scene panorama,
[局部区域描述],
maintaining the same spatial relationships and lighting,
[细节描述],

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9
\```

---

### 第三层：特写/细节（基于中景延展）

#### 场景1-特写A：[细节名称]

**基于**: 场景1-中景A

**画面描述**:
[细节特写描述]

**需要上传的图片**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 场景1-全景 | 空间参考 |
| 参考图2 | 场景1-中景A | 细节延展参考 |

**提示词**:
\```
[STYLE_PREFIX],

Close-up shot of [细节],
based on [中景名称],
maintaining the same material and lighting consistency,
[细节描述],

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9
\```
```

### 场景层级生成检查清单

**生成前检查**:
- [ ] 已阅读分镜脚本，了解需要的所有场景
- [ ] 已规划场景层级（大全景→中景→特写）
- [ ] 已确定每个场景的光影方向和色彩基调

**生成后检查**:
- [ ] 大全景已先生成
- [ ] 中景/局部图已上传大全景作为参考
- [ ] 所有衍生图的空间关系与原图一致
- [ ] 光影方向在所有图中保持一致
- [ ] 道具位置符合空间逻辑

## 提示词构建原则

### 场景类型
```
[室内/室外],
[时代风格: 现代/古代/未来/架空],
[具体地点类型: 卧室/街道/森林等],
```

### 环境要素
```
[时间: 早晨/中午/黄昏/夜晚],
[天气: 晴/阴/雨/雪/雾],
[主要元素描述],
[次要元素],
```

### 氛围渲染
```
[光影效果],
[色彩倾向: 暖色/冷色],
[空气感: 清晰/薄雾/浓雾],
[粒子效果: 尘埃/雨滴/雪花],
```

### 风格与质量
```
[画风风格],
detailed background,
[质量标签],
--ar [宽高比]
```

## 常用背景类型

### 室内场景
| 场景 | 关键元素 |
|------|----------|
| 卧室 | bed, window, desk, personal items |
| 教室 | desks, blackboard, windows, lockers |
| 咖啡厅 | tables, counter, menu board, warm lighting |

### 室外城市场景
| 场景 | 关键元素 |
|------|----------|
| 街道 | buildings, shops, street lights, pedestrians zone |
| 公园 | trees, benches, paths, fountain |
| 天台 | rooftop, city skyline, fence, sunset |

### 自然场景
| 场景 | 关键元素 |
|------|----------|
| 森林 | tall trees, sunlight through leaves, moss, path |
| 海边 | beach, waves, horizon, clouds |
| 山景 | mountains, valleys, clouds, distant peaks |

---

## 视觉隐匿元素处理（重要）⭐⭐⭐

### 核心原则

**当场景中包含"隐匿的"、"模糊的"、"只有轮廓"的角色或物体时，背景提示词绝不能明确写出这些元素！**

背景图片应该是"干净的"场景图，不包含任何角色。如果场景中有"隐匿的角色"，应该在关键帧提示词中处理，而不是背景提示词。

### 背景与关键帧的分工

| 场景类型 | 背景提示词 | 关键帧提示词 |
|----------|------------|--------------|
| 空场景 | 只描述环境 | 无角色 |
| 有明确角色的场景 | 只描述环境 | 角色+环境 |
| 有隐匿角色的场景 | 只描述环境 | 用隐匿方式描述角色轮廓 |

### 错误 vs 正确示例

#### 场景：草屋角落有隐匿的人影

❌ **错误写法（背景提示词中包含角色暗示）**:
```
Interior of dilapidated hut, dark corner with a hidden figure,
mysterious silhouette in shadows, wheelchair outline visible
```
**问题**：背景图中不应该有任何角色元素

✅ **正确写法（背景只描述环境）**:
```
Interior of dilapidated grass hut, dark and gloomy atmosphere,
broken furniture scattered on dirt floor, spider webs in corner,
single candle light source casting long shadows,
earthen walls with cracks, holes in the roof letting in faint moonlight
```
**关键**：背景是干净的，隐匿的角色在关键帧中处理

### 背景提示词中的"氛围暗示"

虽然不能直接写角色，但可以通过环境细节暗示"有人存在"：

| 暗示方式 | 描述示例 |
|----------|----------|
| 道具暗示 | `a cup of tea still steaming`, `a book left open on the desk` |
| 光影暗示 | `shadows cast by an unseen figure`, `flickering candlelight` |
| 痕迹暗示 | `footprints in the dust`, `disturbed cobwebs` |
| 氛围暗示 | `ominous atmosphere`, `sense of being watched` |

### 实战案例

**分镜描述**：
> 镜头1：草屋内景，角落黑暗处隐约有一个人影坐着，看不清细节。

**背景提示词编写**：

```markdown
### 场景1：破败草屋内景 - 深夜

**画面描述**:
破败的草屋内部，昏暗阴冷。角落处阴影浓重，但不描述任何角色。

**提示词**:
\```
[STYLE_PREFIX],

Interior of a dilapidated ancient Chinese grass hut,
dark and gloomy atmosphere,
broken wooden furniture scattered on packed dirt floor,
spider webs hanging from the wooden beams,
single candle burning in corner casting flickering shadows,
earthen walls with visible cracks,
holes in the thatched roof letting in faint moonlight,
dust particles floating in the dim light,
poverty and desolation, ancient rural China setting,

[STYLE_SUFFIX],
no people, no characters, empty scene,
[QUALITY_TAGS],
--ar 16:9
\```

**负向提示词**:
\```
[NEGATIVE_PROMPT],
people, person, human, figure, silhouette, character,
face, body, hands, visible figure shape
\```

**关键处理**:
- ✅ 背景图是"干净"的空场景
- ✅ 在负向提示词中明确排除人物
- ✅ "角落阴影"只是环境描述
- ❌ 不写 "hidden figure", "silhouette" 等暗示角色的词
```

---

## Assets
- [image_prompt_template.md](assets/image_prompt_template.md) - 图片提示词输出模板
