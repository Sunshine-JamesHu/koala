# 尾帧图片提示词模板

## 文件命名
`shot_XXX/last_frame.md`

---

# 尾帧图片提示词 - [镜头编号]

> **用途**: 作为视频的尾帧钉定图，定义视频的结束画面。
>
> **重要**:
> - 可灵支持尾帧钉定，视频将演变到这张图片结束
> - **此图也将作为下一个镜头（shot_XXX+1）的首帧参考**

---

## 连续性信息

| 属性 | 值 |
|------|-----|
| 当前镜头 | shot_XXX |
| 下一镜头 | shot_XXX+1 |
| 衔接方式 | 本尾帧 → 下一首帧 |

---

## 场景信息

| 属性 | 值 |
|------|-----|
| 场景名称 | [场景名] |
| 时间设定 | [如：深夜] |
| 光线变化 | [如有变化请描述] |
| 氛围基调 | [如：从压抑转为紧张] |

---

## 角色最终状态

| 属性 | 值 |
|------|-----|
| 角色名称 | [角色名] |
| 最终位置 | [动作结束后的位置] |
| 最终姿态 | [如：站立，面向门口] |
| 最终表情 | [如：震惊中带着觉醒] |
| 服装状态 | [如有变化请描述] |

---

## 构图设计

| 属性 | 值 |
|------|-----|
| 景别 | [如：close-up] |
| 角度 | [如：eye level] |
| 焦点 | [如：眼睛，瞳孔反射] |
| 景深 | [如：极浅，只有眼睛清晰] |

---

## 需要上传的参考图

| 顺序 | 图片 | 来源 | 用途 |
|------|------|------|------|
| 1 | shot_XXX_first_frame.png | 本镜头首帧 | 确保连续性 |
| 2 | [角色名]-表情卡.png | output/character/ | 表情一致性 |

---

## 完整提示词（直接复制使用）

```
[STYLE_PREFIX - 从 style.json 获取],

[场景核心描述 - 与首帧保持一致或有演变],
[时间设定 - 与首帧保持一致],
[光线变化 - 如有变化请描述],

[角色核心描述 - 与首帧保持一致],
[最终位置 - 如：now standing in center of room],
[最终姿态 - 如：facing the doorway, body tense],
[最终表情 - 如：expression of shocked awakening, eyes wide with realization],
[如有服装变化请描述],

[构图信息 - 如：close-up on face, eye level],
[景深处理 - 如：extremely shallow depth of field, only eyes in sharp focus],
[特殊效果 - 如：subtle light reflection in pupils],

[STYLE_SUFFIX - 从 style.json 获取],
[QUALITY_TAGS - 从 style.json 获取],

--ar 16:9
```

---

## 负向提示词

```
[NEGATIVE_PROMPT - 从 style.json 获取],
multiple characters, different outfits, modern elements,
bright lighting, calm expression, outdoor scene
```

---

## 保存为

`shot_XXX_last_frame.png`

---

## 输出给下一镜头

| 属性 | 值 |
|------|-----|
| 尾帧时间点 | 第[X]秒 |
| 结尾动作 | [描述] |
| 结尾位置 | [描述] |
| 结尾表情 | [描述] |
| 画面状态 | [描述] |

**下一镜头首帧应参考本尾帧的画面状态**

---

## 质量检查清单

- [ ] 提示词以风格前缀开头
- [ ] 提示词以风格后缀+质量标签结尾
- [ ] 场景与首帧保持一致（或合理演变）
- [ ] 角色与首帧保持一致
- [ ] 最终状态清晰定义
- [ ] 比例设置为 16:9
- [ ] 输出信息已填写（供下一镜头使用）

---

*生成时间: [时间戳]*
*关联文件: video_prompt.md, first_frame.md, shot_XXX+1/first_frame.md*
