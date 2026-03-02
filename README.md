# Koala2 - AI动画制作系统

从小说到AI动画提示词的自动化生成工具。

## 核心功能

输入小说章节，自动生成：
1. **图片提示词** → 用于 Nano Banana Pro
2. **视频提示词** → 用于 Veo3.1 Fast (8秒) 或 可灵动画 (5秒/10秒)

## 快速开始

### 使用方式

```
构建 @novel/chapters/0001.txt
```
或
```
为 @novel/chapters/0001.txt 生成完整提示词
```

### 输出内容

系统会自动生成以下文件：

| 文件 | 内容 | 用途 |
|------|------|------|
| `00_user_guide.md` | 用户操作手册 | 总览和操作步骤 |
| `01_storyboard.md` | 分镜脚本 | 镜头划分和内容 |
| `02_character_refs.md` | 角色参考 | 角色视觉设定 |
| `03_scene_refs.md` | 场景参考 | 场景视觉设定 |
| `04_image_prompts.md` | 图片提示词 | 生成参考图片 |
| `05_video_prompts_veo.md` | Veo视频提示词 | Veo3.1 视频生成 |
| `06_video_prompts_kling.md` | 可灵视频提示词 | 可灵动画视频生成 |

## 目录结构

```
koala2/
├── CLAUDE.md                    # AI协调者指令
├── config.md                    # 全局配置
├── VideoGenerationPromptGuide.md # 视频提示词指南
│
├── .claude/skills/              # AI角色技能
│   ├── creative-director/       # AI创意总监
│   ├── scriptwriter/            # AI编剧
│   ├── character-designer/      # AI角色设计师
│   ├── scene-designer/          # AI场景设计师
│   ├── storyboard-artist/       # AI分镜师
│   ├── keyframe-artist/         # AI原画师
│   ├── background-artist/       # AI场景搭建师
│   ├── motion-designer/         # AI动作设计师
│   ├── inbetween-artist/        # AI中间画师
│   ├── effects-artist/          # AI特效师
│   ├── style-unifier/           # AI风格统一师
│   ├── sound-designer/          # AI音效设计师
│   ├── music-composer/          # AI配乐师
│   ├── voice-director/          # AI配音导演
│   ├── colorist/                # AI调色师
│   ├── art-supervisor/          # AI艺术监督
│   └── story-supervisor/        # AI剧情监督
│
└── works/                       # 作品目录
    └── [剧名]/
        ├── novel/
        │   ├── outline.md       # 故事大纲
        │   └── chapters/        # 章节原文
        ├── output/              # 生成的提示词
        └── assets/              # 生成的素材
```

## AI角色团队

### 核心链路（前期创意）
| 角色 | 职责 |
|------|------|
| AI创意总监 | 确定视觉风格、世界观设定 |
| AI编剧 | 将小说转化为分场剧本 |
| AI角色设计师 | 设计角色外观、表情库 |
| AI场景设计师 | 设计场景环境、色彩基调 |
| AI分镜师 | 将剧本转化为分镜头脚本 |

### 制作链路（提示词生成）
| 角色 | 职责 |
|------|------|
| AI原画师 | 生成角色关键帧图片提示词 |
| AI场景搭建师 | 生成背景图片提示词 |
| AI动作设计师 | 生成视频提示词（Veo+可灵） |
| AI中间画师 | 生成补间动画提示词 |
| AI特效师 | 设计光影、粒子、魔法特效 |
| AI风格统一师 | 确保画面风格一致 |

### 后期链路
| 角色 | 职责 |
|------|------|
| AI音效设计师 | 设计环境音、动作音效 |
| AI配乐师 | 设计背景音乐 |
| AI配音导演 | 设计角色配音指导 |
| AI调色师 | 设计色彩方案和调色指南 |

### 监督链路
| 角色 | 职责 |
|------|------|
| AI艺术监督 | 审核画面质量、风格一致性 |
| AI剧情监督 | 审核故事逻辑、情感表达 |

## 视频工具支持

| 工具 | 时长 | 特点 |
|------|------|------|
| Veo3.1 Fast | 8秒/片段 | 适合中等长度镜头、流畅动作 |
| 可灵动画 | 5秒或10秒/片段 | 5秒适合快速动作、10秒适合完整场景 |

## 使用流程

1. **准备小说** - 在 `works/[剧名]/novel/` 下放置 `outline.md` 和章节文件
2. **运行构建** - 使用 `构建 @novel/chapters/XXXX.txt` 命令
3. **生成图片** - 使用提示词在 Nano Banana Pro 生成参考图
4. **生成视频** - 使用提示词在 Veo 或 可灵生成视频
5. **整合输出** - 按顺序拼接视频片段

## 提示词质量要求

- 每个提示词至少 50 字
- 包含：Subject + Action + Scene + Camera + Style
- 可直接拷贝使用，无需二次修改
- 遵循视频生成工具的安全规范

## 许可证

MIT License
