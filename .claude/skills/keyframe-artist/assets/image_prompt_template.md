# 图片提示词模板

> 此模板用于生成图片提示词输出文件

---

# 图片生成提示词 - [章节名/编号]

> **使用说明**:
> - 将"提示词"内容直接复制到 Nano Banana Pro
> - 负向提示词用于避免常见问题
> - 图片比例根据需要调整 --ar 参数

---

## 角色关键帧

### [角色名] 系列提示词

#### 镜头 [镜头编号] - [描述]

**图片用途**: [关键帧/表情参考/动作参考]

**画面描述**:
[简要描述这个画面要表现什么]

**提示词**:
```
[角色核心描述],
[当前姿态/动作],
[表情描述],
[服装状态],
[位置/环境简述],
[光影效果],
[构图信息],
[画风风格],
[质量标签],
--ar [宽高比]
```

**负向提示词**:
```
low quality, blurry, distorted, deformed,
bad anatomy, bad hands, missing fingers,
extra limbs, disconnected limbs
```

**参考信息**:
- 场景: [对应场景编号]
- 情绪: [情绪关键词]
- 光源: [主光源方向]

---

## 角色表情参考卡

### [角色名] - 基础表情

#### 平静
```
[角色名], [基础外观],
calm expression, neutral face,
serene eyes, relaxed mouth,
[服装], [风格标签]
```

#### 开心
```
[角色名], [基础外观],
happy expression, bright smile,
joyful eyes, cheerful face,
[服装], [风格标签]
```

#### 悲伤
```
[角色名], [基础外观],
sad expression, downcast eyes,
slightly frowning, melancholic,
[服装], [风格标签]
```

#### 愤怒
```
[角色名], [基础外观],
angry expression, furrowed brows,
intense eyes, determined look,
[服装], [风格标签]
```

#### 惊讶
```
[角色名], [基础外观],
surprised expression, wide eyes,
raised eyebrows, shocked face,
[服装], [风格标签]
```

---

## 场景背景

### 场景 [编号]: [场景名] - [变体]

**画面描述**:
[简要描述这个背景要表现什么]

**提示词**:
```
[场景类型],
[时间] [天气],
[主要元素描述],
[次要元素],
[氛围元素],
[光影效果],
[色彩倾向],
[构图信息],
[画风风格],
[质量标签],
--ar [宽高比]
```

**负向提示词**:
```
people, characters, text, watermark,
low quality, blurry, distorted
```

**使用场景**:
- 镜头: [对应镜头编号]
- 景别: [远景/中景/近景]
- 合成说明: [与角色的关系]

---

## 使用指南

### 图片生成顺序
1. 先生成角色表情参考卡（保持角色一致性）
2. 再按镜头顺序生成关键帧
3. 生成场景背景
4. 使用生成的图片作为视频生成的参考

### 保持一致性的技巧
- 始终使用相同的角色核心描述
- 保持画风标签一致
- 使用相同的负向提示词
- 相同场景使用相同的背景描述

---

## 视觉隐匿元素处理指南（重要）⭐

### 核心原则

**当角色或物体在画面中是"隐匿的"、"模糊的"、"只有轮廓"时，绝不能直接写出明确的物体名称！**

### 隐匿元素对照表

| 实际物体 | 视觉效果 | ❌ 错误描述 | ✅ 正确描述 |
|----------|----------|------------|------------|
| 轮椅上的人 | 黑暗中的轮廓 | `man in wheelchair` | `silhouette of seated figure in shadows` |
| 躲在树后的人 | 只露出一只眼睛 | `person hiding behind tree` | `a single eye peeking from behind the tree trunk` |
| 远处的骑士 | 逆光剪影 | `knight on horse` | `distant silhouette of a rider against the sunset` |
| 雾中的人影 | 模糊不清 | `person standing in fog` | `vague human shape emerging from the mist` |

### 隐匿程度描述关键词

| 隐匿程度 | 英文关键词 |
|----------|------------|
| 完全隐匿 | `ominous presence felt but not seen`, `something lurking in the darkness` |
| 极度隐匿 | `silhouette barely visible`, `faint outline in shadows` |
| 重度隐匿 | `vague shape in the dark`, `indistinct form` |
| 中度隐匿 | `partially obscured figure`, `half-hidden in shadows` |
| 轻度隐匿 | `figure shrouded in shadow`, `cloaked in darkness` |

### 实战示例：草屋角落的隐匿人影

**分镜描述**：草屋角落，男主坐轮椅隐匿在黑暗中，烛光只能照亮他苍白的脸。

**关键帧提示词**：
```
[STYLE_PREFIX],

In the dark corner of a dilapidated grass hut,
a silhouette of a seated figure barely visible in the shadows,
only a pale face faintly illuminated by candlelight from the side,
the rest of the figure completely hidden in darkness,
mysterious and ominous atmosphere,
dark moody lighting with single candle light source,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 16:9
```

**关键处理**：
- ❌ 不写 "wheelchair" 或 "sitting in wheelchair"
- ✅ 写 "seated figure"（坐着的身影）
- ✅ 写 "silhouette... barely visible"（几乎看不见的剪影）
- ✅ 写 "hidden in darkness"（隐藏在黑暗中）

---

## 图片清单

| 编号 | 类型 | 用途 | 状态 |
|------|------|------|------|
| [编号] | [角色/场景] | [对应镜头] | [待生成/已生成] |
