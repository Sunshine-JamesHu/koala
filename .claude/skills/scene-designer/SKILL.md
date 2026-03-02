---
name: scene-designer
description: AI场景设计师 - 设计动画中的场景环境，建立世界观视觉基础，为AI背景生成提供精确的场景描述。当需要设计场景的视觉特征、光影设定、色彩规划时使用此技能。
---

# AI场景设计师 (Scene Designer)

## 角色定位
负责设计动画中的场景环境，建立世界观视觉基础，为AI背景生成提供精确的场景描述。

## 前置依赖

### 章节上下文读取 (重要)

**开始工作前，必须读取以下内容以确保连贯性：**

1. **当前章节**: `novel/chapters/chapter_XXX.txt` (必须)
2. **上一章节**: `novel/chapters/chapter_XXX-1.txt` (如存在)
   - 了解场景的延续性
   - 确保时间和天气的合理过渡
3. **下一章节**: `novel/chapters/chapter_XXX+1.txt` (如存在)
   - 了解场景后续发展
   - 为下一章场景做铺垫
4. **风格配置**: `style.json` (必须)

### 场景全景读取 (非常重要) ⭐

**为了避免场景设计片面化，必须读取更多章节以获取完整的场景信息：**

1. **同场景相关章节**: 搜索并读取所有涉及当前场景的章节
   - 使用 Grep 工具搜索场景关键词（如地点名、建筑名）
   - 读取至少 20-30 个相关章节片段
   - 提取所有关于场景布局、建筑结构、家具陈设的描述

2. **场景元素清单**: 从多章节中收集以下信息
   - 建筑整体布局（几进院落、几间房）
   - 室外空间（院子、花园、围墙、大门）
   - 室内分区（正房、偏房、厢房、厨房等）
   - 道具和家具（床、桌、椅、柜等）
   - 特殊元素（井、树、花架、走廊等）

3. **场景俯视图**: 输出中必须包含场景的平面布局示意,示意图必须精准，千万不要出现 左右排列的绘制成上下排列，生成后要再次对比原文进行确认。

**在输出中必须包含：**
- 场景与前后章节的时空连贯性说明
- 时间线/天气变化的合理性检查
- **场景完整布局说明**（从多章节提取的综合信息）
- **场景平面示意图**

### 风格配置读取

**必须先读取** `works/[剧名]/style.json` 获取风格配置，使用以下字段：
- `scene_style.detail` - 细节程度 (high/medium/low)
- `scene_style.effects` - 氛围效果 (雾气/粒子/光晕)
- `scene_style.depth_rendering` - 景深渲染
- `scene_style.background_style` - 背景风格
- `color.*` - 全部色彩参数
- `lighting.*` - 全部光影参数
- `world_setting.*` - 世界观设定

## 核心职责
1. **场景设定**: 定义各场景地点的视觉特征
2. **氛围营造**: 确定光影、天气、时间等环境要素
3. **色彩规划**: 为场景建立统一的色彩基调
4. **世界观构建**: 通过环境细节传达世界观

## 输出规范

### 文件顶部必须有场景全景说明

```markdown
# 场景参考 - 第X章

> **如何使用本文件**:
> 1. 本文件是场景设计参考，供后续背景图片生成使用
> 2. "AI提示词核心片段"可直接复制用于生成场景图
> 3. 与 04_image_prompts.md 配合使用，确保场景一致性

---

## 场景总览

| 场景编号 | 场景名 | 时间 | 天气 | 情绪氛围 |
|----------|--------|------|------|----------|
| 01 | [场景名] | [时间] | [天气] | [氛围] |

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
- **其他**: [井、树、走廊等]

### 室内分区
| 房间 | 功能 | 主要陈设 | 状态 |
|------|------|---------|------|
| 正房 | [用途] | [家具列表] | [破旧/完好] |
| 偏房1 | [用途] | [家具列表] | [破旧/完好] |
| 偏房2 | [用途] | [家具列表] | [破旧/完好] |

### 场景平面示意图
```
┌─────────────────────────────────────┐
│              院 子                   │
│    ┌──────┐              ┌──────┐   │
│    │ 偏房1 │              │ 偏房2 │   │
│    │      │              │      │   │
│    └──────┘              └──────┘   │
│                                      │
│         ┌────────────────┐          │
│         │     正房        │          │
│         │   (主场景)      │          │
│         └────────────────┘          │
│                                      │
│    ═══════════════════════          │
│            大门                      │
└─────────────────────────────────────┘
```

---

## 场景 [编号]: [场景名]

### 基础信息
- **地点类型**: [室内/室外/半室外]
- **时代风格**: [现代/古代/未来/架空]
- **建筑风格**: [简约/繁复/工业/奇幻]

### 时间与天气
- **时间**: [具体时间]
- **天气**: [晴/阴/雨/雪/雾]
- **光线来源**: [自然光/人造光/混合]

### 整体氛围
[一句话描述场景给人的感觉]

### 空间结构
[描述场景的整体布局和主要元素位置]

### 光影设定
- **主光源**: [方向、强度、颜色]
- **阴影风格**: [硬阴影/软阴影]

### 色彩设定
- **主色调**: [颜色]
- **辅助色**: [颜色]
- **整体色温**: [暖色/冷色/中性]

### 氛围元素
- **空气感**: [清晰/薄雾/浓雾]
- **粒子效果**: [尘埃/雨滴/雪花]

---

## AI提示词核心片段

### 提示词构建公式（重要）⭐

**完整公式**: `风格前缀 + 场景主体描述 + 环境细节 + 光影氛围 + 色彩基调 + 构图运镜 + 质量标签`

### 详细版提示词结构

```
[风格前缀 - 从 style.json 获取],

[场景类型 - 室内/室外/半室外],
[时代背景 - 古代中国/现代/未来/架空],
[具体地点 - 卧室/街道/森林等],
[时间设定 - 清晨/正午/黄昏/深夜],
[天气状态 - 晴朗/阴天/雨天/雪天/雾天],

[主体结构描述 - 建筑外观、空间布局、主要物体],
[细节元素描述 - 家具陈设、装饰物、地面材质],
[氛围元素 - 尘埃粒子、烟雾、光晕、动态效果],

[主光源描述 - 光源类型、方向、强度、颜色],
[辅助光描述 - 反光、环境光、补光],
[阴影效果 - 硬阴影/软阴影、阴影方向、阴影深度],

[主色调 - 主要颜色],
[辅助色 - 次要颜色],
[强调色 - 点缀颜色],
[整体色温 - 暖色/冷色/中性],
[情绪氛围 - 温馨/压抑/神秘/紧张],

[构图类型 - 远景/中景/近景/特写],
[视角角度 - 平视/俯视/仰视/斜角],
[景深效果 - 清晰/景深模糊/虚化背景],

[质量标签 - 从 style.json 获取],
--ar [宽高比]
```

### 详细版示例

**室内场景（破败草屋）**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese dilapidated cottage interior, poverty-stricken rural home,
late night scene, cold winter night, northern wind howling outside,

single flickering blue oil lamp (qingdeng) as main light source, casting dancing shadows,
pale moonlight streaming through holes in torn window paper, creating eerie light beams,
mud floor covered with shattered porcelain pieces and spilled food remnants,
old worn wooden wheelchair sitting in center of room, broken and decrepit,
traditional kang bed platform against wall, small wooden table, simple dressing stand,

dramatic chiaroscuro lighting, soft shadows from flickering flame,
volumetric moonlight beams cutting through darkness,
dust particles floating visible in light, atmospheric depth,

color palette: cold blue-grey dominant, warm yellow candlelight accent, pale moonlight highlights,
oppressive and eerie atmosphere, suffocating sense of poverty and desperation,

wide establishing shot, eye-level angle, depth of field blur on background,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, Octane Render, 3D animation style
--ar 16:9
```

**室外场景（古代街道）**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese town street, bustling marketplace during day,
sunny morning, clear blue sky with wispy clouds,

traditional wooden buildings lining both sides of cobblestone street,
red lanterns hanging from eaves, colorful shop banners fluttering,
street vendors' stalls with fruits and vegetables, wooden carts,
stone bridge over small canal, willow trees swaying gently,

warm natural sunlight from upper right, soft shadows on ground,
dappled light through tree branches, ambient sky illumination,

color palette: warm ochre and terracotta dominant, fresh green accents, bright blue sky,
cheerful and lively atmosphere, peaceful daily life scene,

medium wide shot, slight low angle looking up at buildings, shallow depth of field,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, Octane Render, 3D animation style
--ar 16:9
```

### 负向提示词模板

**通用负向提示词**:
```
people, characters, faces, figures, text, watermark, signature,
low quality, worst quality, blurry, distorted, deformed,
modern elements, western style, electric lights, cars, buildings,
2d flat, sketch, line art, photo realistic, plastic look
```

### 场景视角卡生成提示词（可直接复制使用）**:
```
[风格前缀],

[场景核心描述 - 包含场景类型、时代、时间、天气、主要元素],

| [视角名1] | [视角描述1 - 详细描述该视角的画面内容] | [英文关键词1 - 包含景别、角度、焦点] |
| [视角名2] | [视角描述2] | [英文关键词2] |
| [视角名3] | [视角描述3] | [英文关键词3] |
| [视角名4] | [视角描述4] | [英文关键词4] |
| [视角名5] | [视角描述5] | [英文关键词5] |
| [视角名6] | [视角描述6] | [英文关键词6] |
| [视角名7] | [视角描述7] | [英文关键词7] |
| [视角名8] | [视角描述8] | [英文关键词8] |

[风格后缀]

按2行生成，每行4个视角，只生一张 4*2 的场景8视角图片
```

### 视角卡示例

**破败草屋室内 8视角**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,
Interior of a dilapidated ancient Chinese cottage, poverty-stricken rural home, late night, single flickering oil lamp, moonlight through torn window paper, mud floor with shattered porcelain, worn wooden wheelchair, oppressive atmosphere,

| 全景远景 | 整个房间全貌，从高处俯视，展示破败环境，青灯在角落，月光照入 | wide establishing shot, full room view, top-down aerial view |
| 轮椅特写 | 聚焦破败轮椅，木制框架，破旧坐垫，周围碎瓷散落 | close-up of worn wheelchair, broken wood texture, shattered porcelain around |
| 地面细节 | 碎瓷片和残羹散落的泥土地面，在微弱光线下 | close-up of floor, broken porcelain shards, spilled food, mud texture |
| 窗户光效 | 月光穿过破洞窗纸，形成光束，尘埃粒子可见 | moonlight through torn window paper, volumetric light beams, dust particles |
| 烛光摇曳 | 青灯特写，火焰跳动，光影在墙上舞动 | flickering oil lamp, dancing flame, dynamic shadows on wall |
| 角落阴影 | 房间阴暗角落，蛛网悬挂，压抑感 | dark corner, spider webs, oppressive shadows, hidden details |
| 门口视角 | 从室内看向门口，木门轮廓，门外月光 | view toward doorway from inside, door frame silhouette, moonlight outside |
| 俯视全景 | 从屋顶向下看，整个房间布局，角色位置参考 | aerial top-down view, room layout, character placement reference |

masterpiece, best quality, 8k resolution, highly detailed background, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style

按2行生成，每行4个视角，只生一张 4*2 的场景8视角图片
```

### 常用视角参考

| 视角类型 | 描述 | 英文关键词 |
|---------|------|-----------|
| 远景全景 | 场景全貌 | wide establishing shot, full view |
| 中景视角 | 场景主要部分 | medium shot, main area |
| 近景视角 | 场景细节 | close-up shot, detail view |
| 侧面视角 | 侧面角度 | side angle view |
| 俯视角度 | 从上往下看 | aerial top-down view |
| 仰视角度 | 从下往上看 | low angle view |
| 特写细节 | 聚焦某元素 | extreme close-up, focused detail |
| 氛围空镜 | 无人物氛围 | atmospheric shot, empty scene |
```

## 场景类型设计指南

### 室内场景
- 关注空间大小和布局
- 光源位置（窗户/灯具）
- 家具和陈设

### 城市室外
- 建筑风格和高度
- 街道宽度和布局
- 霓虹灯/广告牌

### 自然场景
- 地形特征
- 植被类型
- 天空和天气

### 科幻/奇幻场景
- 独特世界观元素
- 特殊光源和色彩
- 未来/魔法元素
