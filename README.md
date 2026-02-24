# 考拉动漫

考拉动漫是一个使用 AI 为小说生成漫剧视频的项目。支持多部小说的并行开发，每部作品独立管理。

## 快速开始

### 1. 创建新项目

```bash
# 复制示例项目模板
cp -r works/.example works/你的小说名

# 编辑项目配置
vim works/你的小说名/project.json
```

### 2. 准备小说原文

将小说按章节拆分，放入 `novel/chapters/` 目录：

```
novel/
├── chapters/
│   ├── chapter_001.txt    # 第一章
│   ├── chapter_002.txt    # 第二章
│   └── ...
├── outline.md             # 故事大纲
└── metadata.json          # 元数据（作者、字数等）
```

### 3. 准备角色资源

为每个主要角色创建主视图和四视图设计图：

```
assets/characters/萧炎/
├── front.png          # 主视图（正面立绘）
├── views.png          # 四视图设计图（正面+左侧+右侧+背面在一张图中）
├── expressions/       # 表情变体
│   ├── happy.png
│   ├── angry.png
│   ├── sad.png
│   └── ...
└── poses/             # 常用姿态
    ├── standing.png
    └── fighting.png
```

### 4. 准备道具和场景

```
assets/
├── props/                 # 重要道具（贯穿剧情的）
│   └── 玄重尺/
│       ├── front.png
│       └── detail.png
│
└── scenes/                # 场景背景
    ├── outdoor/           # 室外
    │   ├── forest.png
    │   └── mountain.png
    └── indoor/            # 室内
        ├── hall.png
        └── room.png
```

### 5. 制作分镜剧本

在 `scripts/` 目录按剧集组织：

```
scripts/episode_001/
├── storyboard.json    # 分镜配置（镜头、台词、时长等）
└── shots/             # 分镜图（可 AI 生成）
    ├── shot_001.png
    └── shot_002.png
```

`storyboard.json` 定义每个镜头的详细信息：

```json
{
  "episode": 1,
  "title": "第一集 少年萧炎",
  "shots": [
    {
      "id": "shot_001",
      "duration": 5.0,
      "scene": { "location": "萧家大院" },
      "camera": { "angle": "long" },
      "characters": [{ "name": "萧炎", "expression": "sad" }],
      "dialogue": { "speaker": "萧炎", "text": "三十年河东..." }
    }
  ]
}
```

### 6. 准备音频资源

```
assets/audio/
├── bgm/                    # 背景音乐
│   ├── tense.mp3
│   └── emotional.mp3
├── sfx/                    # 音效
│   ├── sword_clash.wav
│   └── wind.wav
└── voice/                  # 配音
    └── episode_001/
        ├── shot_001.wav
        └── shot_002.wav
```

### 7. 生成视频

输出目录结构：

```
output/
├── episodes/               # 完整剧集（最终发布）
│   ├── episode_001.mp4
│   └── episode_002.mp4
├── clips/                  # 单个镜头片段
│   └── episode_001/
│       ├── clip_001.mp4
│       └── clip_002.mp4
└── previews/               # 预览版（快速查看效果）
    └── episode_001_preview.mp4
```

## 目录说明

| 目录 | 用途 | 是否必需 |
|------|------|----------|
| `novel/chapters/` | 存放拆分好的章节原文 | 是 |
| `novel/outline.md` | 故事大纲、角色设定 | 建议 |
| `scripts/` | 分镜剧本，按剧集组织 | 是 |
| `assets/characters/` | 角色设计图、表情、姿态 | 是 |
| `assets/props/` | 重要道具图 | 按需 |
| `assets/scenes/` | 场景背景图 | 是 |
| `assets/audio/` | BGM、音效、配音 | 是 |
| `output/` | 生成的视频 | 自动生成 |
| `cache/` | AI 中间文件，可清理 | 自动生成 |

## 模板文件

`templates/` 目录提供配置模板：

- `project.json` - 项目基础配置（分辨率、风格等）
- `storyboard.json` - 分镜脚本结构模板
- `color_palette.json` - 全局配色方案

## 工作流程

```
小说原文 → 章节拆分 → 分镜剧本 → 资源准备 → AI生成 → 视频合成
    ↓          ↓          ↓          ↓          ↓         ↓
 novel/   chapters/  scripts/   assets/    cache/   output/
```

1. **原文处理**：将小说拆分为章节文件
2. **剧本改编**：根据章节编写分镜脚本
3. **资源准备**：角色/道具/场景/音频
4. **AI 生成**：根据分镜生成画面和片段
5. **视频合成**：组合片段、添加音频，输出成片

## 多项目管理

每个小说独立一个文件夹，互不干扰：

```
works/
├── 斗破苍穹/
│   ├── project.json
│   ├── novel/
│   └── ...
├── 遮天/
│   ├── project.json
│   └── ...
└── 完美世界/
    └── ...
```
