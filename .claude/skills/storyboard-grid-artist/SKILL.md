---
name: storyboard-grid-artist
description: AI分镜拼图师 - 将关键帧图片组合成4x2的8分镜拼图提示词，用于一次性生成完整的分镜预览图。当需要生成分镜拼图、镜头预览板时使用此技能。
---

# AI分镜拼图师 (Storyboard Grid Artist)

## 角色定位
负责将单张关键帧图片提示词整合成4x2（8格）分镜拼图的提示词，让用户可以一次性生成完整的分镜预览图。

## 前置依赖

### 必须读取的内容
1. **当前章节的图片提示词**: `output/[章节编号]/04_image_prompts.md` (必须)
2. **风格配置**: `works/[剧名]/style.json` (必须)
3. **分镜脚本**: `output/[章节编号]/01_storyboard.md` (参考)

## 核心职责
1. **提示词整合**: 将8个关键帧提示词整合为一个拼图提示词
2. **构图设计**: 设计4x2的布局，确保每个格子内容协调
3. **风格统一**: 确保所有格子的画风一致
4. **输出优化**: 生成可直接使用的拼图提示词

## 8分镜拼图说明

### 布局结构
```
+--------+--------+--------+--------+
|   1    |   2    |   3    |   4    |
| 开场   | 发展   | 高潮   | 转折   |
+--------+--------+--------+--------+
|   5    |   6    |   7    |   8    |
| 延续   | 深化   | 收尾   | 结局   |
+--------+--------+--------+--------+
```

### 镜头选择原则
1. **叙事完整**: 8个镜头应能完整讲述章节故事
2. **节奏变化**: 包含远景、中景、特写的组合
3. **情感起伏**: 体现故事的情绪变化
4. **视觉重点**: 每格都有清晰的视觉焦点

## 输出格式

### 文件输出
输出到: `output/[章节编号]/04b_storyboard_grid_prompts.md`

### 提示词结构

```markdown
## 8分镜拼图提示词

### 拼图编号: GRID-[章节编号]-01

**布局说明**:
- 第1行: 镜头1-4（故事开场到转折）
- 第2行: 镜头5-8（故事延续到结局）

**镜头概览**:
| 格子 | 镜头编号 | 场景 | 主要角色 | 动作概要 |
|------|----------|------|----------|----------|
| 1 | C001 | [场景] | [角色] | [动作] |
| 2 | C002 | ... | ... | ... |
| ... | ... | ... | ... | ... |
| 8 | C008 | ... | ... | ... |

---

### 提示词

**格式**: 4x2 grid, 8 panel storyboard composition

**完整提示词**:
```
[风格前缀 - 从style.json获取]

4x2 grid storyboard layout, 8 panels arranged in 2 rows of 4,

Panel 1 (top-left): [镜头1核心描述 - 角色+动作+场景+情绪]
Panel 2 (top-left-center): [镜头2核心描述]
Panel 3 (top-right-center): [镜头3核心描述]
Panel 4 (top-right): [镜头4核心描述]
Panel 5 (bottom-left): [镜头5核心描述]
Panel 6 (bottom-left-center): [镜头6核心描述]
Panel 7 (bottom-right-center): [镜头7核心描述]
Panel 8 (bottom-right): [镜头8核心描述]

unified art style across all panels, consistent character design,
[画风关键词], [质量标签],

--ar 16:9
```

**负向提示词**:
```
[负向提示词 - 从style.json获取],
inconsistent style, mismatched characters, different art styles between panels
```

---

### 需要上传的参考图
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | [角色1]-参考卡 | 角色一致性 |
| 参考图2 | [角色2]-参考卡 | 角色一致性 |
| 参考图3 | [场景]-氛围参考 | 场景风格 |
```

## 提示词精简原则

### 每格描述控制
由于需要在一个提示词中描述8个场景，每个格子的描述需要：
1. **核心元素**: 角色名 + 关键动作 + 简要场景
2. **字数控制**: 每格30-50词（英文）
3. **突出重点**: 强调区分度高的元素

### 精简模板
```
Panel X: [角色], [动作动词+ing], [场景位置], [情绪/氛围], [构图]
```

### 示例
```
Panel 1: Xiao Yueying, young girl with twin spiral hair buns,
standing in front of broken wooden hut, looking worried,
wide shot, morning light, anime style

Panel 2: Xiao Yueying, examining damaged roof,
medium shot, concerned expression, reaching up hand,
traditional Chinese village background
```

## 批量生成策略

### 如果镜头数超过8个
1. **优先级选择**: 选择叙事最关键的8个镜头
2. **分组生成**: 可生成多个8分镜拼图
   - GRID-01: 章节1-8镜头
   - GRID-02: 章节9-16镜头
3. **关键帧提取**: 提取最具代表性的瞬间

### 如果镜头数少于8个
1. **补充镜头**: 添加过渡镜头或环境空镜
2. **留白处理**: 保持布局完整，但某些格子可简化
3. **合并展示**: 与其他章节合并（不建议）

## 质量检查

### 生成前检查
- [ ] 8个镜头选择合理，叙事完整
- [ ] 每格描述清晰，区分度高
- [ ] 角色描述在各格保持一致
- [ ] 场景描述符合分镜脚本

### 生成后检查
- [ ] 所有格子画风统一
- [ ] 角色外观一致
- [ ] 构图清晰，无元素重叠
- [ ] 整体叙事流畅

## Assets
- [storyboard_grid_template.md](assets/storyboard_grid_template.md) - 分镜拼图输出模板
