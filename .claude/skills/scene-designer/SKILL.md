---
name: scene-designer
description: AI场景设计师 - 设计动画中的场景环境，建立世界观视觉基础。输出到全局共享目录，跨章节复用。当需要设计场景的视觉特征、光影设定、色彩规划时使用此技能。
---

# AI场景设计师 (Scene Designer)

## 角色定位
负责设计动画中的场景环境，建立世界观视觉基础，为AI背景生成提供精确的场景描述。

## 核心变更（v2）
- **输出位置变更**: 从 `output/chapter_XXX/03_scene_refs.md` 改为 `output/scene/[场景名].md`
- **全局共享**: 场景文件跨章节复用，不再每章重新生成
- **增量跳过**: 已存在的场景文件自动跳过，只处理新场景
- **视角方案变更**: 取消8视角卡，改为"定场镜头 + 平面图 + 关键角度"方案

## 前置依赖

### 必须读取
1. **分镜脚本**: `output/[章节编号]/storyboard.md`（获取本章场景列表）
2. **风格配置**: `works/[剧名]/style.json`（必须）

### 场景全景读取（非常重要）⭐

**为了避免场景设计片面化，必须读取更多章节以获取完整的场景信息：**

1. **同场景相关章节**: 使用 Grep 工具搜索场景关键词（地点名、建筑名）
   - 读取至少 20-30 个相关章节片段
   - 提取所有关于场景布局、建筑结构、家具陈设的描述

2. **场景元素清单**: 从多章节中收集以下信息
   - 建筑整体布局（几进院落、几间房）
   - 室外空间（院子、花园、围墙、大门）
   - 室内分区（正房、偏房、厢房、厨房等）
   - 固定家具（床、桌、椅、柜等）
   - 特殊元素（井、树、花架、走廊等）

### 风格配置读取

**必须先读取** `works/[剧名]/style.json`，使用以下字段：
- `scene_style.*` - 场景风格参数
- `color.*` - 全部色彩参数
- `lighting.*` - 全部光影参数
- `world_setting.*` - 世界观设定
- `prompts.image.*` - 图片提示词风格标签

## 工作流程

### 步骤1: 检查已有场景文件

对于分镜脚本中列出的每个场景：
1. 检查 `works/[剧名]/output/scene/[场景名].md` 是否已存在
2. **如果已存在 → 跳过该场景**
3. 如果不存在 → 执行场景设计流程

### 步骤2: 场景全景读取

对每个新场景：
1. 使用 Grep 搜索场景名在所有章节中的出现
2. 读取相关章节片段，提取布局、陈设、氛围等信息
3. 汇总为完整的场景画像

### 步骤3: 生成场景文件

每个场景输出一个独立文件到 `output/scene/[场景名].md`

## 输出路径

```
works/[剧名]/output/scene/[场景名].md
```

**示例：**
```
works/穿书后我攻略了奸臣首辅/output/scene/沈家小院.md
works/穿书后我攻略了奸臣首辅/output/scene/破旧草屋.md
works/穿书后我攻略了奸臣首辅/output/scene/京城大街.md
```

## 输出模板

```markdown
# 场景参考 - [场景名]

> **如何使用本文件**:
> 1. 本文件是场景设计参考，供 shot-builder 生成背景图片提示词使用
> 2. "AI提示词核心片段"可直接复制用于生成场景图
> 3. 定场镜头必须首先生成，后续所有场景图都需要上传定场镜头作为参考

---

## 基本信息
- **场景名称**: [场景名]
- **地点类型**: [室内/室外/半室外]
- **时代风格**: [现代/古代/未来/架空]
- **建筑风格**: [描述]

---

## 场景完整布局说明

> **重要**: 此部分综合了小说多个章节中对该场景的描述，确保场景设计完整准确。

### 建筑整体结构
- **类型**: [四合院/三合院/独栋/其他]
- **布局**: [几进院落/几间房]
- **主要建筑**: [正房、偏房、厢房等]

### 室外空间
- **院子**: [大小、地面材质、植物]
- **围墙**: [材质、高度、状态]
- **大门**: [位置、样式、状态]

### 室内分区
| 房间 | 功能 | 主要陈设 | 状态 |
|------|------|---------|------|
| [房间名] | [用途] | [家具列表] | [破旧/完好] |

---

## 场景平面示意图

> 示意图必须精准，千万不要出现左右排列的绘制成上下排列，生成后要再次对比原文确认。

```
[ASCII平面图]
```

---

## 光影与色彩设定

### 默认光影
- **主光源**: [方向、强度、颜色]
- **阴影风格**: [硬阴影/软阴影]

### 默认色彩
- **主色调**: [颜色]
- **辅助色**: [颜色]
- **整体色温**: [暖色/冷色/中性]

### 氛围元素
- **空气感**: [清晰/薄雾/浓雾]
- **粒子效果**: [尘埃/雨滴/雪花/无]

---

## 第一步：定场镜头（Establishing Shot）⭐

> **必须首先生成**，作为后续所有该场景图片的参考。
>
> 定场镜头是场景的"身份证"，后续所有该场景的图片都应上传此图作为参考。

**定场镜头提示词（详细版）**:
```
[STYLE_PREFIX - 从 style.json 获取],

[场景类型 - 如：ancient Chinese courtyard], [时代背景 - 如：Ming dynasty style],
[具体地点描述 - 如：exterior view of dilapidated rural residence],
[时间设定 - 如：late night], [天气状态 - 如：clear starry sky],

[主体结构描述 - 如：single-story wooden structure with curved roof tiles],
[细节元素描述 - 如：weathered wooden pillars, cracked stone steps, overgrown weeds],
[氛围元素 - 如：single bronze oil lamp glowing from inside window, casting warm light],

[主光源描述 - 如：moonlight from above, warm oil lamp glow from inside],
[阴影效果 - 如：soft shadows with high contrast between lit and dark areas],

[主色调 - 如：deep blue night sky], [辅助色 - 如：warm amber from lamp],
[情绪氛围 - 如：melancholic, desolate yet peaceful],

wide establishing shot, eye-level angle,
no people, empty scene, architectural focus,

[STYLE_SUFFIX - 从 style.json 获取],
[QUALITY_TAGS - 从 style.json 获取],

--ar 16:9
```

**负向提示词**:
```
[NEGATIVE_PROMPT - 从 style.json 获取],
people, characters, faces, figures, human silhouette,
modern elements, anachronistic objects, cars, electric lights
```

**保存为**: `[场景名]-定场镜头.png`

**用途**:
1. 作为场景的"身份证"上传到所有该场景的图片生成
2. 作为视频生成的场景参考图（5张参考图之一）

---

## 第二步：关键角度（供 shot-builder 使用）

根据分镜需要，提供以下常用角度的提示词片段：

### 室内全景（从门口看向内部）
```
[场景核心描述],
interior wide shot from doorway looking inward,
[光影和氛围],
```

### 角落特写（聚焦某个区域）
```
[场景核心描述],
close-up detail shot of [specific area],
[光影和氛围],
```

### 窗户视角（从窗外/窗内）
```
[场景核心描述],
view through window, [inside looking out / outside looking in],
[光影和氛围],
```

### 俯瞰视角
```
[场景核心描述],
aerial top-down view showing room layout,
[光影和氛围],
```

---

## 角色道具与场景元素的区分

**场景图中只应包含固定环境元素：**

| 类型 | 示例 | 是否出现在场景图中 |
|------|------|-------------------|
| 建筑结构 | 墙、门、窗、屋顶 | 是 |
| 固定家具 | 床/炕、柜子、桌子 | 是 |
| 环境道具 | 灯具、水缸、灶台 | 是 |
| 角色道具 | 轮椅、武器、随身物品 | **否** |
```

## 室内布局规范（重要）⭐⭐⭐

**室内布局必须符合现实逻辑：**

1. **床/炕的位置**: 必须靠墙放置
2. **家具布局**: 大件家具靠墙或靠窗放置，中央留出活动空间
3. **门窗位置**: 合理且不被家具遮挡

## 设计原则
- **一致性优先**: 同一场景在不同镜头中保持环境一致
- **功能明确**: 场景布局要服务于故事需要
- **氛围为王**: 光影和色彩要传达正确的情绪
