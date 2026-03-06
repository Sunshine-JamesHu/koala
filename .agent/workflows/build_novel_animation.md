---
description: Pipeline to build novel animation storyboards and prompts
---

# 构建小说动画分镜工作流

当用户输入指令 `构建 @[文件名]` 或 `构建 [小说名] [章节号]` 时，触发该工作流。该工作流旨在将原始小说文本转化为可以直接用于 Nano Banana Pro 生成动画分镜图片的提示词资产。

**前置操作**：
1. 本工作流强依赖于项目的目录结构。
2. 小说名默认为用户提供的文件名（去除后缀）或者用户指定的名称。
3. 章节默认在 `novels/[Novel_Name]/chapters/` 下生成一个新的流水号文件夹（例如 `chapter_001`）。如果源文件已经标明了章节，则使用该章节名。

> [!NOTE]
> 请 Agent 在执行过程中主动创建缺失的文件夹结构。

## 执行步骤

### Step 1: 读取并生成全局大纲 (Outline)
- **动作**: 读取提供的源文件内容。
- **思考**: 提取该小说的整体故事大纲、核心冲突。
- **输出**: 将大纲写入 `f:\Projects\koala3\novels\[Novel_Name]\outline.md`。如果已存在，则追加或跳过（视用户意图）。

### Step 2: 提取本章核心元素 (Elements)
- **动作**: 基于本章原文，提取出场角色、场景、关键道具。
- **⚠️ 铁律：一切细节必须来源于原文**：
  - 任何角色外貌、场景布局、道具描写，**必须从原始小说文本中提取**，严禁凭空臆造。
  - 如果当前章节信息不足（例如场景只提了一笔），**必须主动阅读前后多个章节**来综合补全细节。
  - 遇事不决就回去读原文，读一章不够就多读几章。
- **思考**: 
  - 判断哪些元素是贯穿全书的，哪些是本章特有的。如果该小说是首次构建，则在此阶段创建并初始化一部小说的全局美术设定 `style.json`。
  - **【重要】场景架构规范 (Scene Architecture JSON + MD)**：对于每一个新出现的关键大场景，必须结合多章的综合描述，在 `global_assets/scenes/` 目录下同时生成：
    - `[Scene_Name].json`：供 Agent 程序读取的结构化数据，包含运镜角度定义、空间坐标、材质信息。
    - `[Scene_Name].md`：**供人工查阅的可视化文档**，必须包含 ASCII 平面图、建筑细节表格、预设机位表格、光线方向说明，以及空间约束警告。
    - **场景层级引用 (Parent Scene)**：子场景（如：卧室内部）必须在 JSON 中通过 `parent_scene` 字段引用它所在的父场景（如：沈家小院整体布局），以确保子场景的门窗朝向、光照方向与院落总体结构完全自洽。Agent 需要先生成或读取父场景 JSON，再基于其空间约束来定义子场景的布局。
  - **【重要】角色结构规范 (Character Architecture JSON)**：为每一个新出场的角色生成具有“四视图特征”的独立 JSON，保证人物外观绝对一致。
    - **主角/核心贯穿角色 (Main Characters)** （如女主辛月影、男主沈清起）：保存在全局 `global_assets/characters/[Character_Name].json`。
    - **配角/本章特有角色 (Supporting Characters)** （如屠户老王、龙套）：保存在本章局部 `chapters/[章号]/characters/[Character_Name].json`，避免污染全局资产。
- **输出**: 
  - 将本章信息概览写入 `chapters/[章号]/01_elements.md`。
  - 创建并保存上述 Scene JSONs 和 Character JSONs 到对应目录。

### Step 3: 编剧与统筹生成剧本 (Scriptwriter)
- **动作**: 调用 `scriptwriter-planner` Skill 的能力。
- **输入**: 结合全局大纲、本章原文以及提取的角色设定。
- **要求**: 将小说文本转化为专业的剧本格式，剔除冗长旁白，外化内心戏，切分为具体场次。
- **输出**: 将剧本写入 `f:\Projects\koala3\novels\[Novel_Name]\chapters\[章号]\02_script.md`。

### Step 4: 分镜师撰写分镜表 (Director & Photographer)
- **动作**: 调用 `director-photographer` Skill 的能力。
- **输入**: 读取 `02_script.md` 的内容。
- **要求**: 按照至少“1秒1图”的节奏，细化每一个动作的景别、角度、转场过渡提示。生成一个 Markdown 的分镜表格。
- **输出**: 将分镜表写入 `f:\Projects\koala3\novels\[Novel_Name]\chapters\[章号]\03_storyboard.md`。

### Step 5: 生成生图提示词 (Prompter)
- **动作**: 调用 `nano-banana-prompter` Skill 的能力。
- **输入**: 读取 `03_storyboard.md` 的每一个镜头描述和过渡提示，`01_elements.md` 的角色特征，以及极其重要的 `global_assets/style.json`。
- **要求**: 
  1. **基准图生成原则 (Reference Images Priority)**：在开始写具体镜头之前，如果有新的关键角色登场，必须先生成**“角色四视图 (Character Design Sheet)”**；如果有新的关键大场景，先生成**“场景基准图 (Scene Environment Base)”**。
  2. **高密度关键帧拆解**：为表格中**每一行 (每1秒的镜头)** 生成一个独立的、可直接复制用来生图的 Nano Banana Pro 提示词。如果分镜表太简略，必须主动拆分关键帧动作。
  3. 提示词文本**必须是纯英文**，用一个专门的 Markdown Code Block 包裹（` ```text `）。
  4. 必须单独、醒目地写出**“垫图说明”**：明确告诉用户“请垫入该角色的四视图”、“请垫入场景基准图”或“请垫入上一帧 Shot”。以保证绝对的一致性。
  5. 必须融合 `style.json` 中定义的美术风格。

### Step 6: 准备工作区 (Workspace Ready)
- **动作**: 创建一个空的 `images` 文件夹以供用户手动存放生图结果。
`f:\Projects\koala3\novels\[Novel_Name]\chapters\[章号]\images\`
- **完成反馈**: 使用 `notify_user` 告知用户构建完成，并提供 `04_prompts.md` 的链接，让用户开始“傻瓜式”复制生图。
