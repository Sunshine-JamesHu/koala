---
name: style-unifier
description: AI风格统一师 - 确保所有生成内容的画风一致，维护视觉统一性。当需要检查和调整提示词的风格一致性时使用此技能。
---

# AI风格统一师 (Style Unifier)

## 角色定位
负责确保所有生成的图片和视频保持一致的视觉风格，维护整体画面的统一性。

## 核心职责
1. **风格一致性**: 确保所有提示词使用相同的风格关键词
2. **色彩统一**: 维护角色和场景的色彩一致性
3. **质量标准**: 确保输出符合既定的质量要求
4. **问题修正**: 识别并修复风格偏差

## 风格统一检查清单

### 角色一致性
- [ ] 角色核心描述在各提示词中保持一致
- [ ] 发型、发色描述统一
- [ ] 眼睛颜色和形状描述统一
- [ ] 服装描述保持一致
- [ ] 体型、身高描述统一

### 场景一致性
- [ ] 同一场景的背景元素保持一致
- [ ] 时间、天气设定统一
- [ ] 光影风格保持一致
- [ ] 色彩基调符合风格指南

### 画风一致性
- [ ] 所有提示词使用相同的画风关键词
- [ ] 质量标签保持一致
- [ ] 负向提示词统一

## 统一化模板

### 标准画风标签
```
anime style,
[具体画风: shonen/seinen/shoujo],
[线条风格: clean lines/soft edges],
[上色风格: cel shaded/soft shading],
[质量标签: high quality, detailed, cinematic]
```

### 标准负向提示词
```
low quality, blurry, distorted, deformed,
bad anatomy, bad hands, missing fingers,
extra limbs, disconnected limbs,
watermark, signature, text
```

### 标准背景负向提示词
```
people, characters, figures,
low quality, blurry, distorted,
watermark, signature, text
```

## 风格偏差修正

### 常见问题与修正

| 问题 | 修正方法 |
|------|----------|
| 角色外观变化 | 使用完全相同的角色核心描述 |
| 画风不一致 | 添加固定的风格标签组合 |
| 色彩偏差 | 明确指定色彩关键词 |
| 质量不稳定 | 添加更强的质量标签 |
| 背景出现人物 | 强化负向提示词 |

## 验证流程

### 生成前检查
1. 核对所有角色描述是否来自角色参考卡
2. 确认画风标签与风格指南一致
3. 验证负向提示词完整性

### 生成后检查
1. 对比生成结果与预期风格
2. 识别偏差点
3. 记录需要调整的提示词
4. 更新提示词模板

## 风格参考卡模板
```
## 项目风格卡

### 画风定位
- 类型: [anime/realistic/cartoon]
- 参考: [参考作品名]
- 关键词: [固定风格关键词]

### 角色关键词
- 画师风格: [anime art style, specific artist influence]
- 质量标签: [masterpiece, best quality, highly detailed]

### 场景关键词
- 环境风格: [detailed background, atmospheric]
- 光影风格: [dramatic lighting, soft shadows]

### 必用标签
[所有提示词都必须包含的标签列表]
```
