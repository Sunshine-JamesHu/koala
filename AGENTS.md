# 🚀 自动化小说转动画工作流 (Novel-to-Animation Pipeline)

当前项目是一个专门用于将"小说文本"批量转换为"Nano Banana Pro 生图提示词"的自动化动画分镜流水线。

## 📁 目录结构

```
f:\Projects\koala3\
├── 📁 novels/[Novel_Name]/
│   ├── 📁 source/chapters/       # 原始小说章节文本 (.txt)
│   ├── 📄 outline.md             # 全书故事大纲
│   ├── 📁 global_assets/
│   │   ├── 📄 style.json         # 全局美术风格 (3D UE5 东画风)
│   │   ├── 📁 characters/        # 全局常驻角色设定 (含分类子目录)
│   │   │   └── 📁 main_cast/     # 如主角团、核心配角
│   │   │       ├── 📄 [name].json       # 角色四视图物理描述 (供Agent读)
│   │   │       └── 📄 [name]_prompt.md  # 角色四视图生图提示词 (供人工用)
│   │   └── 📁 scenes/            # 全局常驻场景设定 (含分类子目录)
│   │       └── 📁 shen_residence/# 按照地理位置/建筑群分类
│   │           ├── 📄 [name].json       # 场景结构定义 (供Agent读)
│   │           └── 📄 [name].md         # 场景可视化文档 (供人工用)
│   └── 📁 chapters/[chapter_NNN]/
│       ├── 01_elements.md        # 本章出场元素
│       ├── 02_script.md          # 剧本文本
│       ├── 03_storyboard.md      # 摄影分镜表
│       ├── 04_prompts.md         # 最终生图清单 (操作员直接复制用)
│       ├── 05_storytelling.md    # 有声小说/推文图文解说稿 (带网感旁白)
│       ├── images/               # 生成的图片存放
│       └── characters/           # 本章配角JSON (可选)
├── scripts/                      # 可执行脚本 (仅限JavaScript)
├── .agent/
│   ├── skills/                   # AI技能定义
│   │   ├── scriptwriter-planner/ # 编剧统筹
│   │   ├── director-photographer/# 导演分镜师
│   │   └── nano-banana-prompter/ # 生图提示词生成器
│   └── workflows/
│       └── build_novel_animation.md  # 一键构建工作流
└── CLAUDE.md                     # 本文件
```

## 🤖 核心指令

**触发**: `构建 @[文件名]` 或 `构建 [小说名] [章节号]`

执行以下 6 步流水线 (详见 `.agent/workflows/build_novel_animation.md`):

1. **大纲提取** → `outline.md`
2. **元素沉淀** → `01_elements.md` + 角色/场景 JSON+MD
3. **编剧改写** → `02_script.md` (调用 `scriptwriter-planner` 技能)
4. **分镜设计** → `03_storyboard.md` (调用 `director-photographer` 技能)
5. **提示词生成** → `04_prompts.md` (调用 `nano-banana-prompter` 技能)
6. **有声书/推文解说稿** → `05_storytelling.md` (用于短视频制作，包含画面描述与网感旁白)
7. **工作区准备** → 创建 `images/` 文件夹

## 📏 铁律

### 数据来源
- **一切细节必须来源于原文**，严禁凭空臆造
- 如果当前章节信息不足，**必须主动阅读前后多个章节**综合补全
- 遇事不决就回去读原文，一章不够就多读几章

### 资产归属
- **角色四视图提示词** → 存放在角色目录 `*_prompt.md`，`04_prompts.md` 只做链接引用
- **场景空镜** → 不含角色私有道具（轮椅属沈清起，不属于房间）
- **主角/贯穿角色** JSON → `global_assets/characters/`
- **配角/章节角色** JSON → `chapters/[章号]/characters/`
- **场景** → 同时生成 `.json` (供Agent) + `.md` (供人工，含ASCII布局图+生图提示词)
- **子场景** 必须通过 `parent_scene` 引用父场景，确保空间自洽

### 提示词格式
- 所有提示词**必须纯英文**
- **Negative prompt 合并在 text 代码块末尾**，不单独分行，方便一键复制
- 每条提示词**必须内嵌完整的 `style.json` 风格段**
- `04_prompts.md` 采用三段式结构：✅ 生图清单表 → 👤🏞️ 基准图引用 → 🎬 分镜卡片

### 文件管理
- **严禁乱放文件**：所有产出按章节放入 `novels/[Novel_Name]/chapters/`
- **脚本语言唯一性**：仅限 JavaScript
- **强制字符编码**：所有脚本读写文件、所有生成产出，**必须显式指定使用 UTF-8 编码**（如 Node.js 中的 `fs.readFileSync('...', 'utf8')`），严禁出现因系统默认编码造成的中文乱码（如“坐轮??男主”）。
- **强制 Skill 调用**：执行任务时必须参考 `.agent/skills/` 中的准则

### 脚本使用
- `scripts/` 目录下存储本项目需要使用的所有脚本
- 脚本语言**必须为 JavaScript**

