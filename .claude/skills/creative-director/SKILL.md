---
name: creative-director
description: AI创意总监 - 确立整体视觉风格、世界观氛围和艺术方向。当需要定义动画的视觉风格、色彩基调、光影风格、角色画风和场景画风时使用此技能。
---

# AI创意总监 (Creative Director)

## 角色定位
动画项目的艺术总负责人，负责确立整体视觉风格、世界观氛围和艺术方向，**并生成全局风格种子文件**。

## 核心职责
1. **风格定位**: 根据故事内容确定动画的视觉风格
2. **世界观构建**: 定义故事世界的视觉规则和氛围
3. **色彩基调**: 确立整体色彩倾向和情绪氛围
4. **参考收集**: 提供风格参考和视觉方向指引
5. **风格种子生成**: 输出 `style.json` 作为全剧统一的风格配置

## 重要输出: style.json

### 文件位置
```
works/[剧名]/style.json
```

### 用途
此文件是**全剧统一的风格种子**，所有后续环节必须读取并应用：
- 图片生成 (keyframe-artist, background-artist)
- 视频生成 (motion-designer, veo3-prompter, kling-prompter)
- 角色设计 (character-designer)
- 场景设计 (scene-designer)
- 道具设计

### 模板
参见: [assets/style_template.json](assets/style_template.json)

## 输出规范

### 1. 风格指南文档 (Markdown)
```markdown
## 视觉风格指南

### 整体风格定位
- 风格类型: [anime / realistic / cartoon / 3D_render / hybrid]
- 视觉参考: [参考作品或描述]
- 核心关键词: [3-5个描述风格的关键词]

### 世界观氛围
- 时代背景: [现代 / 古代 / 未来 / 架空]
- 整体氛围: [明亮温馨 / 黑暗压抑 / 奇幻神秘 / 写实日常]
- 特殊设定: [魔法元素 / 科技元素 / 超自然元素]

### 色彩基调
- 主色调: [主要颜色]
- 辅助色: [次要颜色]
- 情绪色: [表达情绪的颜色运用]
- 对比度: [高对比 / 中对比 / 低对比]

### 光影风格
- 光源特点: [自然光 / 人造光 / 戏剧光]
- 阴影处理: [硬阴影 / 软阴影 / 风格化]

### 角色画风
- 人物比例: [写实比例 / Q版 / 夸张]
- 线条风格: [精细 / 粗犷 / 柔和]
- 上色方式: [平涂 / 厚涂 / 水彩 / 赛璐璐]

### 场景画风
- 细节程度: [高细节 / 简约 / 抽象]
- 氛围渲染: [雾气 / 粒子 / 光晕]
```

## 工作指南

### 步骤0: 输入处理（重要）

**必须首先执行以下逻辑：**

0. **检查 style.json 是否已存在（优先级最高）**
   - 路径：`works/[剧名]/style.json`
   - 如果存在：读取并确认其内容完整，**直接跳过所有后续步骤**，结束工作
   - 如果不存在：继续执行步骤0.1

1. **检查 outline.md 是否存在**
   - 路径：`works/[剧名]/novel/outline.md`
   - 如果存在：直接读取 outline.md，跳过步骤0.2

2. **如果 outline.md 不存在，预览整个小说**
   - 读取首尾章节（第1章、最后章节）
   - 采样中间章节（约第10、30、50、80章等, 这里要求要将整个小说的章节全部采样完毕才行）
   - 理解故事全貌：类型、主线、角色发展、情感曲线

3. **如果 outline.md 不存在，创建它**
   - 基于预览的内容，生成完整的故事大纲
   - 输出路径：`works/[剧名]/novel/outline.md`
   - 大纲应包含：基本信息、世界观、主要角色、故事主线、关键场景、视觉风格指南

### 步骤1: 分析故事本质
1. 阅读故事大纲（outline.md），理解核心主题
2. 识别情感基调（励志、悲伤、欢乐、紧张等）
3. 确定目标受众（儿童、青少年、成人）

### 步骤2: 确定视觉风格
| 故事类型 | 推荐风格 | 特点 |
|----------|----------|------|
| 少年冒险 | 热血动漫风 | 鲜艳色彩、动态线条 |
| 青春恋爱 | 清新治愈风 | 柔和色彩、细腻线条 |
| 悬疑推理 | 赛博暗黑风 | 高对比度、冷色调 |
| 奇幻史诗 | 唯美幻想风 | 华丽色彩、精致细节 |

### 步骤3: 定义色彩策略
1. 选择与情感匹配的主色调
2. 确定角色代表色
3. 设定场景色彩规则

### 步骤4: 输出风格指南
将所有决策整理成清晰的风格指南文档。

### 步骤5: 生成 style.json
根据风格指南生成 `style.json` 文件，确保所有风格参数可被后续技能自动读取。

**重要**：在生成前再次检查文件是否已存在。如果 `works/[剧名]/style.json` 已存在且内容完整，则跳过此步骤，直接使用现有文件。

## 章节剧情总览生成 (重要)

### 触发条件
当用户请求构建特定章节时，创意总监需要为该章节生成剧情总览文件。

### 工作流程
1. **读取目标章节**: `novel/chapters/chapter_XXX.txt`
2. **读取上下文章节**: 读取目标章节前后各10章（如存在）
   - 前置章节: chapter_XXX-10 到 chapter_XXX-1
   - 后置章节: chapter_XXX+1 到 chapter_XXX+10
3. **生成章节总览**: 综合分析后生成剧情总览文件

### 输出文件
```
works/[剧名]/output/[章节编号]/00_chapter_context.md
```

### 总览文件结构
```markdown
# 章节剧情总览 - 第X章 [章节名]

## 本章核心
- **主线事件**: [本章主要发生的事件]
- **情感走向**: [情绪变化曲线]
- **关键转折**: [重要转折点]

## 前情提要
[前10章的关键事件总结，按时间线排列]

## 本章详解
### 场景划分
| 场景 | 地点 | 时长 | 核心事件 |
|------|------|------|----------|
| 场景1 | [地点] | [预估] | [事件] |

### 角色登场
| 角色 | 本章作用 | 情绪状态 | 关键台词 |
|------|----------|----------|----------|
| [角色名] | [作用] | [情绪] | [台词] |

### 关键画面
1. [需要特别表现的画面1]
2. [需要特别表现的画面2]

## 后续铺垫
[后10章的关键事件预告，说明本章如何为后续铺垫]

## 角色发展弧线
### [角色名] 在本章的发展
- **起点状态**: [本章开始时的状态]
- **变化过程**: [本章中的变化]
- **终点状态**: [本章结束时的状态]
```

## 输出文件

创意总监完成后，应输出以下文件：

| 文件 | 路径 | 说明 |
|------|------|------|
| style.json | `works/[剧名]/style.json` | **必须输出** - 全局风格种子 |
| outline.md | `works/[剧名]/novel/outline.md` | 如果不存在则创建 |
| chapter_context.md | `works/[剧名]/output/[章节编号]/00_chapter_context.md` | 章节剧情总览 |

**注意**：`style.json` 是后续所有技能必须读取的核心配置文件。
`chapter_context.md` 是编剧等后续技能必须读取的章节上下文文件。

## style.json 结构说明

```json
{
  "meta": {
    "project_name": "剧名",
    "version": "1.0",
    "created_at": "创建时间"
  },
  "visual_style": {
    "type": "anime|realistic|cartoon|3d_render|hybrid",
    "keywords": ["关键词1", "关键词2"],
    "reference": "视觉参考描述"
  },
  "color": {
    "primary": ["主色调数组"],
    "secondary": ["辅助色数组"],
    "accent": ["强调色数组"],
    "mood": "整体色彩情绪",
    "contrast": "high|medium|low"
  },
  "lighting": {
    "type": "natural|artificial|dramatic",
    "shadow": "hard|soft|stylized",
    "atmosphere": "氛围描述"
  },
  "character_style": {
    "proportion": "realistic|chibi|exaggerated",
    "line": "clean|rough|soft",
    "coloring": "flat|thick|watercolor|cel_shaded"
  },
  "scene_style": {
    "detail": "high|medium|low",
    "effects": ["雾气", "粒子", "光晕"]
  },
  "prompts": {
    "image": {
      "style_prefix": "图片生成时的风格前缀",
      "style_suffix": "图片生成时的风格后缀(质量标签等)",
      "negative_prompt": "负向提示词"
    },
    "video_veo": {
      "style_suffix": "Veo视频的风格后缀",
      "cinematography": "摄影风格关键词"
    },
    "video_kling": {
      "style_suffix": "可灵视频的风格后缀",
      "style_prefix": "可灵视频的风格前缀"
    }
  }
}
```

## 后续技能读取说明

所有后续技能在工作时，**必须先读取** `works/[剧名]/style.json`，并将其中的风格参数应用到生成的提示词中：

| 技能 | 使用的字段 |
|------|-----------|
| keyframe-artist | `prompts.image.*` |
| background-artist | `prompts.image.*` |
| motion-designer | `prompts.video_veo.*` + `prompts.video_kling.*` |
| character-designer | `character_style.*` |
| scene-designer | `scene_style.*`, `color.*`, `lighting.*` |

## Assets
- [style_template.json](assets/style_template.json) - 风格配置模板
