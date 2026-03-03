---
name: creative-director
description: AI创意总监 - 确立整体视觉风格、生成故事大纲和全局风格种子。当需要定义动画的视觉风格、色彩基调、光影风格时使用此技能。
---

# AI创意总监 (Creative Director)

## 角色定位
动画项目的艺术总负责人，负责确立整体视觉风格并生成全局风格种子文件。

## 核心职责
1. **故事大纲**: 检查/创建 `outline.md`
2. **风格种子**: 生成 `style.json` 作为全剧统一的风格配置

## 输出文件

| 文件 | 路径 | 说明 |
|------|------|------|
| style.json | `works/[剧名]/style.json` | **必须输出** - 全局风格种子 |
| outline.md | `works/[剧名]/novel/outline.md` | 如果不存在则创建 |

---

## 工作流程

### 步骤0: 检查已有文件（优先级最高）

1. **检查 style.json 是否已存在**
   - 路径：`works/[剧名]/style.json`
   - 如果存在且内容完整：**直接跳过所有后续步骤**，结束工作
   - 如果不存在：继续执行

2. **检查 outline.md 是否存在**
   - 路径：`works/[剧名]/novel/outline.md`
   - 如果存在：直接读取，跳过步骤1
   - 如果不存在：执行步骤1

### 步骤1: 创建故事大纲（如不存在）

1. 读取首尾章节（第1章、最后章节）
2. 采样中间章节（约第10、30、50、80章等，要将整个小说的章节全部采样完毕）
3. 理解故事全貌：类型、主线、角色发展、情感曲线
4. 输出 `works/[剧名]/novel/outline.md`

**大纲应包含：**
- 基本信息（类型、时代背景、目标受众）
- 世界观设定
- 主要角色列表（姓名、身份、简要描述）
- 故事主线
- 关键场景
- 视觉风格建议

### 步骤2: 分析故事本质

1. 阅读故事大纲，理解核心主题
2. 识别情感基调（励志、悲伤、欢乐、紧张等）
3. 确定目标受众

### 步骤3: 确定视觉风格

| 故事类型 | 推荐风格 | 特点 |
|----------|----------|------|
| 少年冒险 | 热血动漫风 | 鲜艳色彩、动态线条 |
| 青春恋爱 | 清新治愈风 | 柔和色彩、细腻线条 |
| 悬疑推理 | 赛博暗黑风 | 高对比度、冷色调 |
| 奇幻史诗 | 唯美幻想风 | 华丽色彩、精致细节 |
| 古代宫廷 | 中国风水墨 | 淡雅色彩、意境渲染 |
| 武侠仙侠 | 东方幻想风 | 飘逸线条、仙气色彩 |

### 步骤4: 定义色彩策略

1. 选择与情感匹配的主色调
2. 确定角色代表色
3. 设定场景色彩规则

### 步骤5: 生成 style.json

根据风格指南生成 `style.json` 文件。
模板参见: `assets/style_template.json`

**重要**：在生成前再次检查文件是否已存在。

---

## style.json 结构说明

```json
{
  "meta": {
    "project_name": "剧名",
    "version": "2.0",
    "created_at": "创建时间"
  },
  "visual_style": {
    "type": "anime|realistic|cartoon|3d_render|hybrid",
    "keywords": ["关键词1", "关键词2"],
    "reference": "视觉参考描述"
  },
  "world_setting": {
    "era": "古代|现代|未来|架空",
    "atmosphere": "整体氛围",
    "special_elements": []
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
    "coloring": "flat|thick|watercolor|cel_shaded",
    "face_style": "",
    "body_style": ""
  },
  "scene_style": {
    "detail": "high|medium|low",
    "effects": ["雾气", "粒子", "光晕"],
    "depth_rendering": "",
    "background_style": ""
  },
  "prompts": {
    "image": {
      "style_prefix": "图片生成时的风格前缀",
      "style_suffix": "图片生成时的风格后缀",
      "quality_tags": "masterpiece, best quality, highly detailed, 4k",
      "negative_prompt": "low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, text, watermark, signature"
    },
    "video_kling": {
      "style_prefix": "可灵视频的风格前缀",
      "style_suffix": "可灵视频的风格后缀",
      "quality_tags": "高质量, 精致细节, 流畅动作"
    }
  },
  "voice_settings": {
    "角色名": {
      "voice_type": "音色描述",
      "tone": "语调特点"
    }
  },
  "aspect_ratio": {
    "image": "16:9",
    "video": "16:9"
  }
}
```

## 后续技能读取说明

所有后续技能在工作时，**必须先读取** `works/[剧名]/style.json`：

| 技能 | 使用的字段 |
|------|-----------|
| storyboard-writer | `visual_style.*`, `world_setting.*` |
| character-designer | `character_style.*`, `visual_style.keywords`, `prompts.image.*` |
| scene-designer | `scene_style.*`, `color.*`, `lighting.*`, `prompts.image.*` |
| shot-builder | `prompts.video_kling.*`, `prompts.image.*`, `voice_settings.*` |
| reviewer | 全部字段 |

## Assets
- assets/style_template.json - 风格配置模板
