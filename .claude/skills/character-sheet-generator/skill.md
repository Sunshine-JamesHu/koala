# character-sheet-generator

根据小说角色描述，生成 AI 绘图可用的三视图 Prompt，并调用 text-to-image skill 生成图片。

## 触发条件

当用户请求：
- 为角色生成三视图
- 生成角色设计图
- 创建角色 Prompt
- 绘制角色参考图

## 工作流程

### 1. 收集角色信息

首先确认或收集以下信息：

```
角色名称：
角色定位：主角/配角/反派
性别：

【外貌特征】
- 年龄（外观）：
- 身高体型：
- 肤色：
- 脸型：
- 眼睛：
- 眉毛：
- 鼻子：
- 嘴唇：
- 发型发色：

【服装】
- 风格：古代/现代/奇幻
- 主要服装：
- 配色：
- 配饰：
- 鞋履：

【性格气质】
- 关键词：
- 整体感觉：
- 姿态特点：

【特殊设定】
- 特殊外貌：
- 随身道具：
- 备注：

【画风】
- 基础风格：anime/realistic/semi-realistic
- 参考风格：
- 色调：
```

### 2. 生成 Prompt

根据收集的信息，按以下模板生成 Prompt：

#### 三视图合一 Prompt

```
Character reference sheet, full body turnaround design, three-view drawing:
front view, side view (left), side view (right), back view,
same character in different angles, white background,
professional character design sheet, clean line art,
consistent character appearance across all views,
{art_style}, high quality, detailed.

Character description:
{gender}, {age} years old, {height}, {body_type}.
{face_features}, {skin_tone} skin.
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

#### 正面图 Prompt

```
Character design, front view, full body,
{gender}, {age} years old, {detailed_appearance},
{clothing}, {accessories},
standing straight, arms at sides,
white background, {art_style}, high quality,
front facing camera, symmetrical composition.
```

#### 侧面图 Prompt（左/右）

```
Character design, side view ({left/right}), full body,
{gender}, {age} years old, {detailed_appearance},
{clothing}, {accessories},
standing straight, profile view,
white background, {art_style}, high quality,
side facing camera, showing {hair_side} profile.
```

#### 背面图 Prompt

```
Character design, back view, full body,
{gender}, {age} years old, {back_hair_description},
{clothing_back_view}, {accessories_back_view},
standing straight, back to camera,
white background, {art_style}, high quality,
rear view, showing full back design.
```

#### 表情图 Prompt

```
Character expression sheet, {character_name},
multiple facial expressions on white background,
expressions: happy, sad, angry, surprised, neutral, embarrassed,
same character, consistent design,
head shots only, {art_style},
expressive eyes, detailed facial features.
```

### 3. 画质增强词

根据需要添加：

```
masterpiece, best quality, highly detailed,
8k resolution, sharp focus, professional artwork,
intricate details, clean lines, vivid colors.
```

### 4. 负面词

```
low quality, bad anatomy, worst quality,
deformed, disfigured, missing limbs,
extra limbs, blurry, watermark, signature,
text, logo, cropped, out of frame.
```

## 调用方式

生成 Prompt 后，使用 Bash 工具调用 text-to-image skill：

```bash
uv run python .claude/skills/text-to-image/text_to_image.py \
  --prompt "完整的Prompt文本" \
  --output "works/{项目名}/assets/characters/{角色名}" \
  --filename "{图片类型}"
```

## 输出格式

为每个角色创建以下文件：

| 图片类型 | 文件名 | 存放路径 |
|---------|--------|---------|
| 正面图 | `front.png` | `{项目}/assets/characters/{角色名}/` |
| 左侧图 | `side_l.png` | `{项目}/assets/characters/{角色名}/` |
| 右侧图 | `side_r.png` | `{项目}/assets/characters/{角色名}/` |
| 背面图 | `back.png` | `{项目}/assets/characters/{角色名}/` |
| 表情集 | `expressions.png` | `{项目}/assets/characters/{角色名}/` |

## 生成顺序

1. 先生成三视图合一图（character_sheet.png）作为主要参考
2. 然后依次生成：front.png → side_l.png → side_r.png → back.png
3. 最后生成表情集（可选）：expressions.png

## 示例

### 输入

```
角色：辛月影
- 24岁女性，175cm，九头身
- 肌肤似雪，五官精致如建模
- 长发及腰，乌黑如墨
- 古代服饰，淡青色襦裙
- 沙雕腹黑，机智狡黠
```

### 输出 prompt（正面图）

```
Character design, front view, full body,
female, 24 years old, 175cm tall, slender nine-head body proportion,
oval face, flawless model-like beauty, snow-white skin,
beautiful almond eyes with dark bright pupils,
willow-leaf eyebrows, elegant nose, cherry lips,
long raven black hair in ancient Chinese updo,
pale cyan ancient Chinese ruqun dress, moon-white sleeves,
wooden hairpin, sachet at waist, embroidered shoes,
standing straight, elegant posture,
white background, Chinese ancient anime style,
masterpiece, best quality, highly detailed.
```

## 注意事项

1. **一致性**：同一角色的多个 Prompt 保持描述一致
2. **特殊状态**：如轮椅、残疾等特殊设定需在所有 Prompt 中体现
3. **画风统一**：确保同一项目的角色使用相同画风
4. **文化适配**：古代背景使用古风描述词，现代背景使用现代词
