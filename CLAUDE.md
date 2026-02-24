# 考拉动漫 - AI小说漫剧生成项目

## 项目简介

考拉动漫是一个使用 AI 将小说转换为漫剧视频的项目。支持多部小说的并行开发，每部作品独立管理。

## 目录结构

```
koala/
├── works/                           # 作品总目录
│   └── {novel_name}/                # 具体小说项目
│       ├── novel/                   # 小说原文
│       │   ├── chapters/            # 章节拆分
│       │   │   └── chapter_XXX.txt
│       │   ├── outline.md           # 大纲
│       │   └── metadata.json        # 元数据
│       │
│       ├── scripts/                 # 分镜剧本
│       │   └── episode_XXX/         # 按集组织
│       │       ├── storyboard.json  # 分镜配置
│       │       ├── shots/           # 分镜图
│       │       └── dialogue.json    # 对话文本
│       │
│       ├── assets/                  # 资源文件夹
│       │   ├── characters/          # 角色资源
│       │   │   └── {角色名}/
│       │   │       ├── front.png        # 主视图（正面）
│       │   │       ├── views.png        # 四视图设计图
│       │   │       ├── expressions/     # 表情
│       │   │       └── poses/           # 姿态
│       │   │
│       │   ├── props/               # 道具
│       │   │   └── {道具名}/
│       │   │       └── *.png        # 三视图
│       │   │
│       │   ├── scenes/              # 场景背景
│       │   │   ├── outdoor/
│       │   │   └── indoor/
│       │   │
│       │   ├── audio/               # 音频
│       │   │   ├── bgm/             # 背景音乐
│       │   │   ├── sfx/             # 音效
│       │   │   └── voice/           # 配音
│       │   │
│       │   └── styles/              # 风格参考
│       │       └── color_palette.json
│       │
│       ├── output/                  # 视频输出
│       │   ├── episodes/            # 完整剧集
│       │   ├── clips/               # 片段
│       │   └── previews/            # 预览
│       │
│       ├── cache/                   # 缓存/中间文件
│       │
│       └── project.json             # 项目配置
│
├── templates/                       # 模板文件夹
│   ├── project.json                 # 项目配置模板
│   ├── storyboard.json              # 分镜模板
│   └── color_palette.json           # 色板模板
│
└── tools/                           # 工具脚本
```

## 核心文件说明

### project.json - 项目配置
```json
{
  "name": "小说名称",
  "title": "显示标题",
  "author": "原作者",
  "video": { "resolution": "1920x1080", "fps": 24 },
  "style": { "artStyle": "anime" },
  "chapters": { "total": 100, "adapted": 10 },
  "episodes": { "total": 20, "completed": 2 }
}
```

### storyboard.json - 分镜脚本
每个镜头包含：
- `type`: 场景类型 (scene/action/dialogue/narration)
- `duration`: 时长（秒）
- `scene`: 场景信息（位置、时间、天气）
- `camera`: 镜头（角度、运动）
- `characters`: 角色（名称、位置、表情、动作）
- `dialogue/narration`: 台词/旁白
- `sfx/bgm`: 音效/背景音乐

## 工作流程

1. **准备阶段**
   - 在 `works/` 下创建项目文件夹
   - 复制 `templates/project.json` 并配置
   - 将小说按章节拆分到 `novel/chapters/`

2. **资源准备**
   - 设计角色三视图存入 `assets/characters/`
   - 准备道具图存入 `assets/props/`
   - 收集/生成场景背景到 `assets/scenes/`

3. **剧本制作**
   - 根据章节创建分镜脚本 `scripts/episode_XXX/storyboard.json`
   - 生成分镜图到 `scripts/episode_XXX/shots/`

4. **视频生成**
   - AI 根据分镜生成片段到 `output/clips/`
   - 合成完整剧集到 `output/episodes/`

5. **预览与发布**
   - 预览版本放 `output/previews/`
   - 最终版本放 `output/episodes/`

## 命名规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 章节 | `chapter_XXX.txt` | chapter_001.txt |
| 剧集 | `episode_XXX` | episode_001 |
| 镜头 | `shot_XXX.png` | shot_001.png |
| 片段 | `clip_XXX.mp4` | clip_001.mp4 |
| 角色/道具 | 中文名/英文名 | 萧炎、xuanheave_sword |

## 开发环境

本项目使用 [uv](https://docs.astral.sh/uv/) 作为Python包管理工具。

**重要规则：所有Python脚本的执行均需要在uv环境中处理。**

```bash
# 安装依赖
uv sync

# 运行脚本
uv run python <script.py>

# 示例
uv run python .claude/skills/text-to-image/text_to_image.py --prompt "测试"
```

## 注意事项

- `cache/` 目录可随时清理，存储 AI 生成的临时文件
- `assets/` 中的资源应保持一致性风格
- 每个项目独立的 `project.json` 管理项目级配置
- 使用 `templates/` 中的模板快速创建新项目
- **所有Python脚本必须使用 `uv run` 执行**
