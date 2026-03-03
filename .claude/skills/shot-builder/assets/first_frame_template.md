# 首帧图片提示词模板

## 文件命名
`shot_XXX/first_frame.md`

---

# 首帧图片提示词 - [镜头编号]

> **用途**: 作为视频的首帧钉定图，定义视频的开场画面。
>
> **重要**: 可灵支持首帧钉定，视频将从这张图片开始演变。

---

## 场景信息

| 属性 | 值 |
|------|-----|
| 场景名称 | [场景名] |
| 时间设定 | [如：深夜] |
| 光线条件 | [如：昏暗，仅有油灯] |
| 氛围基调 | [如：压抑、紧张] |

---

## 角色信息

| 属性 | 值 |
|------|-----|
| 角色名称 | [角色名] |
| 位置 | [在场景中的位置] |
| 姿态 | [如：蜷缩在角落] |
| 表情 | [如：惊恐、迷茫] |
| 服装状态 | [如：破旧单薄] |

---

## 构图设计

| 属性 | 值 |
|------|-----|
| 景别 | [如：medium shot] |
| 角度 | [如：slightly high angle] |
| 焦点 | [如：角色面部] |
| 景深 | [如：浅景深，背景虚化] |

---

## 需要上传的参考图

| 顺序 | 图片 | 来源 | 用途 |
|------|------|------|------|
| 1 | [角色名]-三视图.png | output/character/ | 角色外观一致性 |
| 2 | [场景名]-定场镜头.png | output/scene/ | 场景环境一致性 |

---

## 完整提示词（直接复制使用）

```
[STYLE_PREFIX - 从 style.json 获取],

[场景核心描述 - 如：interior of dilapidated ancient Chinese cottage, night time],
[时间设定 - 如：late night, dark and gloomy],
[光线来源 - 如：single bronze oil lamp flickering with weak warm yellow light],

[角色核心描述 - 如：Xin Yueying, 20 years old Chinese woman],
[位置姿态 - 如：curled up in corner of the room],
[表情状态 - 如：terrified and confused expression, wide fearful eyes],
[服装描述 - 如：wearing tattered grey peasant robe],

[构图信息 - 如：medium shot, slightly high angle looking down at her],
[景深处理 - 如：shallow depth of field, background softly blurred],
[光影效果 - 如：chiaroscuro lighting, strong shadows cast by the lamp],

[STYLE_SUFFIX - 从 style.json 获取],
[QUALITY_TAGS - 从 style.json 获取],

--ar 16:9
```

---

## 负向提示词

```
[NEGATIVE_PROMPT - 从 style.json 获取],
multiple characters, different outfits, modern elements,
bright lighting, happy expression, outdoor scene
```

---

## 保存为

`shot_XXX_first_frame.png`

---

## 质量检查清单

- [ ] 提示词以风格前缀开头
- [ ] 提示词以风格后缀+质量标签结尾
- [ ] 包含场景描述
- [ ] 包含角色描述
- [ ] 包含构图信息
- [ ] 包含光影效果
- [ ] 比例设置为 16:9

---

*生成时间: [时间戳]*
*关联文件: video_prompt.md, last_frame.md*
