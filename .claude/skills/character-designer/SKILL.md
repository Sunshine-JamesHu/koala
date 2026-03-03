---
name: character-designer
description: AI角色设计师 - 定义和维护角色视觉设定，为AI图片生成提供精确的角色描述。输出到全局共享目录，跨章节复用。当需要设计角色的外观特征、服装设定、表情库时使用此技能。
---

# AI角色设计师 (Character Designer)

## 角色定位
负责定义和维护角色视觉设定，确保角色在所有场景中保持外观一致性，为AI图片生成提供精确的角色描述。

## 核心变更（v2）
- **输出位置变更**: 从 `output/chapter_XXX/02_character_refs.md` 改为 `output/character/[角色名].md`
- **全局共享**: 角色文件跨章节复用，不再每章重新生成
- **增量跳过**: 已存在的角色文件自动跳过，只处理新角色

## 前置依赖

### 必须读取
1. **分镜脚本**: `output/[章节编号]/storyboard.md`（获取本章角色列表）
2. **风格配置**: `works/[剧名]/style.json`（必须）

### 角色全景读取（非常重要）⭐

**为了避免角色设计片面化，必须读取更多章节以获取完整的角色信息：**

1. **同角色相关章节**: 使用 Grep 工具搜索角色名字关键词
   - 读取至少 5-10 个相关章节片段
   - 提取所有关于角色外貌、服装、性格、背景的描述

2. **角色信息清单**: 从多章节中收集以下信息
   - **外貌描述**: 详细的五官、身材、发型描述
   - **服装演变**: 不同时期/场景的服装变化
   - **性格特征**: 通过对话和行为展现的性格
   - **背景故事**: 角色的来历、身份、经历
   - **关键道具**: 角色随身携带或使用的特殊物品

### 风格配置读取

**必须先读取** `works/[剧名]/style.json` 获取风格配置，使用以下字段：
- `character_style.proportion` - 人物比例
- `character_style.line` - 线条风格
- `character_style.coloring` - 上色方式
- `character_style.face_style` - 脸部风格
- `character_style.body_style` - 身体风格
- `visual_style.keywords` - 视觉风格关键词
- `prompts.image.*` - 图片提示词风格标签

## 工作流程

### 步骤1: 检查已有角色文件

对于分镜脚本中列出的每个角色：
1. 检查 `works/[剧名]/output/character/[角色名].md` 是否已存在
2. **如果已存在 → 跳过该角色**
3. 如果不存在 → 执行角色设计流程

### 步骤2: 角色全景读取

对每个新角色：
1. 使用 Grep 搜索角色名在所有章节中的出现
2. 读取相关章节片段，提取外貌、服装、性格等信息
3. 汇总为完整的角色画像

### 步骤3: 生成角色文件

每个角色输出一个独立文件到 `output/character/[角色名].md`

## 输出路径

```
works/[剧名]/output/character/[角色名].md
```

**示例：**
```
works/穿书后我攻略了奸臣首辅/output/character/辛影月.md
works/穿书后我攻略了奸臣首辅/output/character/沈清起.md
works/穿书后我攻略了奸臣首辅/output/character/霍奇.md
```

## 输出模板

```markdown
# 角色参考 - [角色名]

> **如何使用本文件**:
> 1. 本文件是角色设计参考，供 shot-builder 生成图片/视频提示词使用
> 2. "AI提示词核心片段"可直接复制用于生成角色图
> 3. 三视图必须首先生成，后续所有图片都需要上传三视图作为参考

---

## 基础信息
- **姓名**: [角色名]
- **年龄**: [年龄]
- **性别**: [性别]
- **身份**: [故事中的身份]
- **性格关键词**: [3-5个性格词]

## 外观特征

### 面部特征
- **脸型**: [描述]
- **眼睛**: [形状 + 颜色 + 特点]
- **发型**: [长度 + 颜色 + 样式]
- **肤色**: [肤色描述]

### 身体特征
- **身高**: [高/中/矮]
- **体型**: [纤细/标准/健壮]

## 服装设定
- **上衣**: [详细描述]
- **下装**: [详细描述]
- **鞋子**: [详细描述]
- **配饰**: [详细描述]
- **颜色搭配**: [主要颜色]

## 角色色卡
- **头发**: [HEX/颜色名]
- **眼睛**: [HEX/颜色名]
- **肤色**: [HEX/颜色名]
- **服装主色**: [HEX/颜色名]

## AI提示词核心片段

```
[角色名], [年龄] years old [性别],
[发型描述 - 英文], [眼睛描述 - 英文],
[体型], [身高],
wearing [服装描述 - 英文],
[风格关键词]
```

---

## 第一步：三视图（必须首先生成）⭐

**三视图提示词（可直接复制使用）**:
```
[STYLE_PREFIX],

Character reference sheet of [角色名],
[年龄] years old [性别],
[发型描述 - 详细英文],
[眼睛描述 - 详细英文],
[脸型描述],
[肤色描述],
[体型], [身高],
wearing [服装详细描述],

Three views: front view, side view, back view,
full body, standing in neutral pose,
white background, character design sheet,
consistent character design across all three views,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 3:1
```

**负向提示词**:
```
[NEGATIVE_PROMPT],
multiple characters, different outfits, inconsistent design,
dynamic pose, action pose, sitting, lying
```

---

## 第二步：情绪表情卡（在三视图基础上生成）⭐

**表情卡生成提示词（可直接复制使用）**:
```
[STYLE_PREFIX],

Expression sheet of [角色名],
[角色核心提示词，不含风格部分],

Six different expressions arranged in two rows:
Row 1: [表情1] ([英文]) | [表情2] ([英文]) | [表情3] ([英文])
Row 2: [表情4] ([英文]) | [表情5] ([英文]) | [表情6] ([英文])

same character, same outfit, consistent design,
white background, expression reference sheet,

[STYLE_SUFFIX],
[QUALITY_TAGS],
--ar 3:2
```

**需要上传的参考图**:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色名]-三视图 | 确保角色一致性 |

---

## 注意事项

### 必须保持一致的元素
- [元素1]
- [元素2]

### 常见错误提醒
- [错误1]: [如何避免]

### 生成顺序提醒
- 必须先生成三视图，再生成表情卡
- 后续生成必须上传三视图作为参考
- 不按顺序生成会导致角色不一致
```

## 设计原则
- **一致性优先**: 选择AI容易保持一致的特征
- **辨识度设计**: 与其他角色有明显区分
- **动画友好**: 服装不宜过于复杂

## 视觉隐匿处理指南

**当角色在画面中是"隐匿的"、"模糊的"、"只有轮廓"时，绝不能直接写出明确的物体名称！**

| 隐匿程度 | 英文关键词 |
|----------|-----------|
| 完全隐匿 | `ominous presence felt but not seen` |
| 极度隐匿 | `silhouette barely visible`, `faint outline in shadows` |
| 重度隐匿 | `vague shape in the dark`, `indistinct form` |
| 中度隐匿 | `partially obscured figure`, `half-hidden in shadows` |
| 轻度隐匿 | `figure shrouded in shadow`, `cloaked in darkness` |
