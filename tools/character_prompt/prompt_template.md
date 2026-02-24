# 角色三视图 Prompt 模板

## 使用说明

1. 复制 `character_template.json` 到角色目录，重命名为 `character.json`
2. 填写角色特征信息
3. 使用下方的 Prompt 模板，替换 `{变量}` 部分
4. 在 AI 绘图工具中使用生成的 Prompt

---

## 三视图基础 Prompt（通用）

```
Character reference sheet, full body turnaround design, three-view drawing:
front view, side view (left), side view (right), back view,
same character in different angles, white background,
professional character design sheet, clean line art,
consistent character appearance across all views,
{art_style}, high quality, detailed.

Character description:
{gender}, {age} years old appearance, {height}, {body_type} body.
{face_shape} face, {skin_tone} skin.
{eye_description}, {eyebrow_description}.
{nose_description}, {lip_description}.
{hair_description}.

Outfit:
{clothing_description}, {color_scheme}.
{accessories_description}.
{shoes_description}.

Personality & vibe:
{personality_keywords}, {overall_vibe}.
{posture_description}.

{special_features}

Style: {art_base}, {color_tone}, {reference_style}.
```

---

## 完整 Prompt 示例

### 正面图 Prompt

```
Character design, front view, full body,
{gender}, {age} years old, {detailed_appearance},
{clothing}, {accessories},
standing straight, arms at sides,
white background, {art_style}, high quality,
front facing camera, symmetrical composition.
```

### 侧面图 Prompt（左/右）

```
Character design, side view ({left/right}), full body,
{gender}, {age} years old, {detailed_appearance},
{clothing}, {accessories},
standing straight, profile view,
white background, {art_style}, high quality,
side facing camera, showing {hair_side} profile.
```

### 背面图 Prompt

```
Character design, back view, full body,
{gender}, {age} years old, {back_hair_description},
{clothing_back_view}, {accessories_back_view},
standing straight, back to camera,
white background, {art_style}, high quality,
rear view, showing full back design.
```

---

## 表情图 Prompt 模板

```
Character expression sheet, {character_name},
multiple facial expressions on white background,
expressions: happy, sad, angry, surprised, neutral, embarrassed,
same character, consistent design,
head shots only, {art_style},
expressive eyes, detailed facial features.
```

---

## 变量说明

| 变量 | 说明 | 示例 |
|------|------|------|
| `{art_style}` | 整体画风 | anime, realistic, semi-realistic |
| `{gender}` | 性别 | male, female |
| `{age}` | 外观年龄 | young adult, 24 years old |
| `{height}` | 身高 | tall, 175cm, slender |
| `{body_type}` | 体型 | slender, athletic, muscular |
| `{skin_tone}` | 肤色 | pale, fair, tan, dark |
| `{hair_description}` | 发型描述 | long black hair, flowing |
| `{clothing}` | 服装描述 | ancient Chinese robe, blue and white |
| `{color_scheme}` | 配色 | cool tones, warm palette |
| `{personality_keywords}` | 性格词 | elegant, mysterious, cold |

---

## 画质增强词（可选添加）

```
masterpiece, best quality, highly detailed,
8k resolution, sharp focus, professional artwork,
intricate details, clean lines, vivid colors.
```

## 负面词（Negative Prompt 参考）

```
low quality, bad anatomy, worst quality,
deformed, disfigured, missing limbs,
extra limbs, blurry, watermark, signature,
text, logo, cropped, out of frame.
```
