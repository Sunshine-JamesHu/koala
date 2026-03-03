# 9分镜组合图提示词模板

## 文件命名
`shot_XXX/storyboard_grid.md`

---

# 9分镜组合图提示词 - [镜头编号]

> **用途**: 作为视频的动作参考图，展示整个视频的动作分解。
>
> **重要**: 可灵支持参考图输入，9分镜组合图能让AI理解视频的完整动作流程。

---

## 布局说明

**3x3 网格布局（9格）**

```
+-----------+-----------+-----------+
|     1     |     2     |     3     |
|   开场    |   发展    |   转折    |
|  0-[X]秒  | [X]-[X]秒 | [X]-[X]秒 |
+-----------+-----------+-----------+
|     4     |     5     |     6     |
|   高潮    |   延续    |   深化    |
| [X]-[X]秒 | [X]-[X]秒 | [X]-[X]秒 |
+-----------+-----------+-----------+
|     7     |     8     |     9     |
|   收尾    |   结局    |   定格    |
| [X]-[X]秒 | [X]-[X]秒 | [X]-[X]秒 |
+-----------+-----------+-----------+
```

---

## 镜头概览表

| 格子 | 时间点 | 内容概要 | 景别 | 情绪 |
|------|--------|----------|------|------|
| 1 | 0-[X]秒 | [开场内容] | [景别] | [情绪] |
| 2 | [X]-[X]秒 | [发展内容] | [景别] | [情绪] |
| 3 | [X]-[X]秒 | [转折内容] | [景别] | [情绪] |
| 4 | [X]-[X]秒 | [高潮内容] | [景别] | [情绪] |
| 5 | [X]-[X]秒 | [延续内容] | [景别] | [情绪] |
| 6 | [X]-[X]秒 | [深化内容] | [景别] | [情绪] |
| 7 | [X]-[X]秒 | [收尾内容] | [景别] | [情绪] |
| 8 | [X]-[X]秒 | [结局内容] | [景别] | [情绪] |
| 9 | [X]-[X]秒 | [定格内容] | [景别] | [情绪] |

---

## 连贯性要求 ⭐⭐⭐

**每个分镜提示词必须具备动作连贯性、空间一致性和画面饱满度：**

1. **分镜图定位说明**（必须在提示词开头添加）:
   - 所有格子是同一个场景、同一组角色、同一段时间内的连续动作
   - 保持空间一致性（角色位置、场景布局、光源方向在各格间保持统一）

2. **动作连贯性**:
   - 每格 Panel 必须清晰描述动作的起始状态、进行过程、结束状态
   - 上一格的动作结束状态 = 下一格的动作起始状态
   - 体现因果链：动作A导致动作B，动作B引发反应C

3. **空间一致性**:
   - 明确场景的固定元素位置（门在哪、光源在哪）
   - 角色移动时标明相对位置变化
   - 保持光源方向一致

4. **画面饱满度**（每格至少50字英文描述）:
   - 角色详细外观
   - 精确位置关系
   - 动作细节
   - 表情细节
   - 场景细节
   - 情绪基调

---

## 需要上传的参考图

| 顺序 | 图片 | 来源 | 用途 |
|------|------|------|------|
| 1 | shot_XXX_first_frame.png | 本镜头首帧 | 确保风格一致 |
| 2 | [角色名]-三视图.png | output/character/ | 角色一致性 |

---

## 完整提示词（直接复制使用）

```
[STYLE_PREFIX - 从 style.json 获取],

3x3 grid storyboard layout, 9 panels arranged in 3 rows of 3,

This is a storyboard reference image for a single continuous video shot.
All 9 panels depict the SAME scene with SAME characters in a CONTINUOUS time flow.
Maintain perfect spatial consistency: character positions must flow logically from panel to panel,
scene layout remains identical, light source direction stays constant across all panels.

Panel 1 (top-left): [详细描述 - 时间点 + 角色位置 + 动作 + 表情 + 场景 + 情绪]
Panel 2 (top-center): [详细描述 - 动作连贯，衔接Panel 1]
Panel 3 (top-right): [详细描述 - 动作连贯，衔接Panel 2]
Panel 4 (middle-left): [详细描述 - 动作连贯，衔接Panel 3]
Panel 5 (middle-center): [详细描述 - 动作连贯，衔接Panel 4]
Panel 6 (middle-right): [详细描述 - 动作连贯，衔接Panel 5]
Panel 7 (bottom-left): [详细描述 - 动作连贯，衔接Panel 6]
Panel 8 (bottom-center): [详细描述 - 动作连贯，衔接Panel 7]
Panel 9 (bottom-right): [详细描述 - 动作连贯，衔接Panel 8，应与尾帧画面一致]

consistent character design across all panels,
same character appearance in every panel,
unified art style across all panels,
cohesive color palette and lighting,
clean panel divisions with thin borders,

[STYLE_SUFFIX - 从 style.json 获取],
[QUALITY_TAGS - 从 style.json 获取],

--ar 16:9
```

---

## 负向提示词

```
[NEGATIVE_PROMPT - 从 style.json 获取],
inconsistent art style between panels,
different character designs in each panel,
varying quality across panels,
cluttered composition,
overlapping panel content
```

---

## 保存为

`shot_XXX_storyboard_grid.png`

---

## 质量检查清单

- [ ] 提示词以风格前缀开头
- [ ] 提示词以风格后缀+质量标签结尾
- [ ] 包含连贯性定位说明
- [ ] 每格描述至少50字
- [ ] 动作连贯（上一格结束 = 下一格开始）
- [ ] 空间一致（场景元素位置不变）
- [ ] Panel 9 与尾帧画面一致
- [ ] 比例设置为 16:9

---

*生成时间: [时间戳]*
*关联文件: video_prompt.md, first_frame.md, last_frame.md*
