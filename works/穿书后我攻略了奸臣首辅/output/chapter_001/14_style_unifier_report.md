# 风格统一检查报告 - 第1章 你自尽吧

> **审核范围**: 第1章所有提示词文件
> **审核日期**: 2025-03-01
> **审核结果**: 通过（A級）

---

## 项目风格卡

### 画风定位
- **类型**: 3D Animation / Chinese Donghua
- **参考**: 《魔道祖师》3D动画 + 《天官赐福》国漫渲染
- **渲染引擎**: Unreal Engine 5, Octane Render

### 必用标签
```
风格前缀: 3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景
风格后缀: masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
```

---

## 角色一致性检查

### 辛月影（女主）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 核心描述 | ✅ 一致 | "Xin Yueying, 20 years old female" |
| 发型描述 | ✅ 一致 | "two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle" |
| 眼睛描述 | ✅ 一致 | "beautiful almond-shaped eyes" |
| 服装描述 | ✅ 一致 | "worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color" |
| 体型描述 | ✅ 一致 | "petite and slender body" |

**一致性评分**: A

**核心描述模板**（已验证在所有文件中一致）:
```
Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes, long thick eyelashes,
delicate oval face, slightly upturned nose, fair porcelain skin,
petite and slender body,
wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color
```

---

### 沈清起（男主）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 核心描述 | ✅ 一致 | "Shen Qingqi, 25 years old male" |
| 发型描述 | ✅ 一致 | "long black hair tied back in ancient Chinese style" |
| 眼睛描述 | ✅ 一致 | "narrow phoenix eyes" |
| 肤色描述 | ✅ 一致 | "pale almost bloodless skin" |
| 服装描述 | ✅ 一致 | "dark blue-black ancient Chinese scholar robe" |
| 轮椅描述 | ✅ 一致 | "sitting in worn wooden wheelchair" |

**一致性评分**: A

**核心描述模板**（已验证在所有文件中一致）:
```
Shen Qingqi, 25 years old male,
long black hair tied back in ancient Chinese style,
narrow phoenix eyes, thin lips, pale almost bloodless skin,
handsome and refined face with sharp defined features,
tall and slender body, sitting in worn wooden wheelchair,
wearing dark blue-black ancient Chinese scholar robe,
cold and gloomy aura
```

---

### 霍齐（配角）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 核心描述 | ✅ 一致 | "Huo Qi, 28 years old male" |
| 面部特征 | ✅ 一致 | "full beard, round bull-like eyes" |
| 肤色描述 | ✅ 一致 | "bronze skin weathered from outdoor labor" |
| 体型描述 | ✅ 一致 | "burly and muscular body, tall and strong frame" |
| 服装描述 | ✅ 一致 | "coarse cloth ancient Chinese laborer clothes, brown and earth tones" |

**一致性评分**: A

---

## 场景一致性检查

### 破败草屋·卧房

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 场景类型 | ✅ 一致 | "dilapidated ancient Chinese cottage bedroom" |
| 时间设定 | ✅ 一致 | "late night" |
| 光源设定 | ✅ 一致 | 青灯(暖黄) + 月光(冷白) |
| 地面材质 | ✅ 一致 | "mud floor" |
| 主要道具 | ✅ 一致 | 轮椅、碎瓷、土炕、青灯 |

**关键环境元素一致性**:
- 青灯: "single flickering blue oil lamp (qingdeng)" ✅
- 月光: "moonlight streaming through torn window paper" ✅
- 碎瓷: "scattered broken porcelain pieces" ✅
- 轮椅: "worn wooden wheelchair" ✅

---

## 画风一致性检查

### 图片提示词检查

| 文件 | 风格前缀 | 风格后缀 | 状态 |
|------|----------|----------|------|
| 04_image_prompts.md | ✅ 正确 | ✅ 正确 | 通过 |
| 04b_background_prompts.md | ✅ 正确 | ✅ 正确 | 通过 |
| 04c_storyboard_grid_prompts.md | ✅ 正确 | ✅ 正确 | 通过 |

### 视频提示词检查

| 文件 | 风格设定 | 摄影术语 | 状态 |
|------|----------|----------|------|
| 06_video_prompts_veo.md | ✅ 正确 | ✅ 正确 | 通过 |
| 07_video_prompts_kling.md | ✅ 正确 | ✅ 正确 | 通过 |

### 质量标签检查

**所有文件必须包含的质量标签**:
```
masterpiece, best quality, 8k resolution, highly detailed
```
| 检查项 | 状态 |
|--------|------|
| 图片提示词包含质量标签 | ✅ 通过 |
| 视频提示词包含质量标签 | ✅ 通过 |

---

## 负向提示词检查

### 标准负向提示词

**图片通用负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly,
bad anatomy, bad proportions, bad hands, missing fingers, extra fingers,
modern elements, western style, electric lights, cars, buildings,
2d flat, sketch, line art, text, watermark, signature,
photo realistic, plastic look
```

**背景专用负向提示词**:
```
people, characters, faces, figures, human shape, silhouette, person
```

| 检查项 | 状态 |
|--------|------|
| 图片负向提示词完整 | ✅ 通过 |
| 背景负向提示词排除人物 | ✅ 通过 |

---

## 色彩一致性检查

### 主色调验证

| 色彩元素 | 规定值 | 实际使用 | 状态 |
|----------|--------|----------|------|
| 主色调 | 青灰色 | cold blue-grey dominant | ✅ |
| 辅助色 | 昏黄色 | warm yellow candlelight accent | ✅ |
| 高光色 | 月白色 | pale moonlight highlights | ✅ |
| 强调色 | 血红色 | crimson red (场景6) | ✅ |

### 光源色温验证

| 光源 | 规定色温 | 实际描述 | 状态 |
|------|----------|----------|------|
| 青灯 | 暖黄 2800-3200K | warm yellow candlelight | ✅ |
| 月光 | 冷白 9000-12000K | cold pale moonlight | ✅ |

---

## 视觉隐匿元素检查

### 黑暗中的沈清起

| 检查项 | 要求 | 实际 | 状态 |
|--------|------|------|------|
| 轮椅剪影 | 不明确写"wheelchair" | 使用"seated figure silhouette" | ✅ 正确 |
| 人物描述 | 只描述轮廓 | "silhouette barely visible" | ✅ 正确 |
| 病娇亮相 | 月光揭示 | "moonlight illuminating his face" | ✅ 正确 |

---

## 文件间交叉检查

### 图片→视频一致性

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 角色描述一致 | ✅ | 关键帧与视频使用相同角色描述 |
| 场景描述一致 | ✅ | 背景与视频场景元素匹配 |
| 光影设定一致 | ✅ | 图片与视频光源描述一致 |

### 视频→特效一致性

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 特效与场景匹配 | ✅ | 特效设计符合场景光源设定 |
| 特效关键词一致 | ✅ | Veo和可灵特效描述协调 |

---

## 发现的问题

### 已修正问题
无

### 待关注事项

1. **可灵提示词格式**
   - 状态: 已注意到并使用正确的中文格式
   - 建议: 保持"主体描述 + 运动描述 + 场景描述"的结构

2. **视频衔接链**
   - 状态: 已正确建立"上一个分镜→输出给下一分镜"机制
   - 建议: 生成时确保按顺序使用尾帧作为下一视频首帧

---

## 统一化建议

### 推荐使用的固定模板

**角色描述模板**（直接复制使用）:
```
[角色核心描述 - 从02_character_refs.md复制]
```

**场景描述模板**（直接复制使用）:
```
[场景核心描述 - 从03_scene_refs.md复制]
```

**风格标签模板**（所有提示词必须包含）:
```
前缀: 3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,
后缀: , masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
```

---

## 检查结果汇总

| 检查类别 | 状态 | 评分 |
|----------|------|------|
| 角色一致性 | ✅ 通过 | A |
| 场景一致性 | ✅ 通过 | A |
| 画风一致性 | ✅ 通过 | A |
| 色彩一致性 | ✅ 通过 | A |
| 质量标准 | ✅ 通过 | A |
| 负向提示词 | ✅ 通过 | A |

### 综合评级: A（优秀）

**结论**: 第1章所有提示词的风格统一性检查通过，可直接用于生成。建议在后续章节中继续保持相同的角色描述和风格标签模板。

---

*由 AI风格统一师 生成*
