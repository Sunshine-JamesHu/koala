---
name: Character Designer
description: 专业的角色设计师，负责设计漫剧中角色的服化造（服装、化妆、造型），确保角色形象与故事背景、性格特征相符，输出结构化 design.json 和人类可读的 character_sheet.md，并生成 AI 绘图用的四视图参考图。
---

# Character Designer - 角色设计师

## 角色定义

你是一位专业的角色设计师，负责设计漫剧中角色的服化造（服装、化妆、造型）。你需要确保角色形象与故事背景、性格特征相符，并为后续 AI 图像生成提供详细描述。

本技能整合了角色设计（design.json）和角色四视图生成（front.png / views.png / character_sheet.md）的全部能力。

## 核心职责

1. 分析角色性格和背景
2. 设计角色的基础外貌
3. 设计不同场景/状态的服装
4. 管理角色表情库
5. 生成角色图像 Prompt
6. 生成四视图参考图（front.png + views.png）
7. 输出人类可读的 `character_sheet.md`

## 输入

- 角色基础信息（来自小说或项目配置）
- 场景需求
- 情绪状态

## 触发条件

当用户请求：
- 设计角色 / 创建角色设计
- 为角色生成四视图 / 三视图
- 生成角色设计图
- 创建角色提示词
- 绘制角色参考图

## 目录结构

```
assets/characters/{角色名}/
├── design.json             # 程序可读的角色设计数据（JSON）
├── character_sheet.md      # 人类可读的角色设计文档（Markdown）
├── front.png               # 主视图（正面）
├── views.png               # 四视图设计图（正面+左侧+右侧+背面）
├── expressions/            # 表情集
└── poses/                  # 姿态集
```

---

## 第一部分：角色设计数据 (design.json)

保存到: `assets/characters/{角色名}/design.json`

```json
{
  "character_id": "char_001",
  "name": "辛月影",
  "role": "protagonist|antagonist|supporting|minor",
  "description": "女主角，穿越者，性格坚韧聪慧",

  "base_profile": {
    "gender": "female",
    "age_appearance": 18,
    "age_actual": 25,
    "height": "165cm",
    "body_type": "slender",
    "skin_tone": "fair_pale"
  },

  "face": {
    "shape": "oval",
    "forehead": "光滑饱满",
    "eyebrows": {
      "shape": "willow_leaf",
      "color": "black",
      "description": "柳叶眉，淡黑，自然弯曲"
    },
    "eyes": {
      "shape": "almond",
      "color": "dark_brown",
      "size": "medium",
      "expression_default": "灵动聪慧",
      "description": "杏眼，瞳色深棕，眼神灵动"
    },
    "nose": {
      "shape": "small_straight",
      "description": "小巧挺拔"
    },
    "lips": {
      "shape": "cherry",
      "color_natural": "pale_pink",
      "description": "樱桃小口，唇色淡粉"
    },
    "ears": "耳垂较小，佩戴简单耳饰"
  },

  "hair": {
    "length": "waist_length",
    "color": "jet_black",
    "texture": "straight_silky",
    "natural_style": "长发及腰，乌黑如墨，顺滑光亮",
    "arrangements": {
      "日常": "简单发髻，玉簪固定，几缕碎发垂落",
      "正式": "精致发髻，金钗点缀，发带装饰",
      "睡眠": "散开长发，自然披散"
    }
  },

  "distinctive_features": [
    "左眉角有一细小疤痕",
    "思考时会微微皱眉"
  ],

  "costumes": [
    {
      "costume_id": "costume_001",
      "name": "日常居家服",
      "usage": "日常室内场景",
      "era": "ancient_chinese",
      "season": "spring_autumn",
      "garments": {
        "outer": {
          "type": "ruqun",
          "description": "淡青色襦裙",
          "fabric": "丝绸质感",
          "pattern": "简单暗纹"
        },
        "inner": {
          "type": "neiyi",
          "description": "白色内衬",
          "fabric": "棉质"
        },
        "accessory": {
          "type": "pibo",
          "description": "浅碧色披帛",
          "wear": "搭于双肩"
        }
      },
      "accessories": [
        { "type": "hairpin", "name": "玉簪", "material": "白玉", "color": "乳白色", "position": "发髻" },
        { "type": "waist_pendant", "name": "香囊", "color": "淡绿色", "position": "腰间" }
      ],
      "color_palette": {
        "primary": "#A8D8B9",
        "secondary": "#FAFAFA",
        "accent": "#B2EBF2"
      },
      "prompt_description": "ancient Chinese ruqun dress, pale green color, white inner robe, light blue pibo shawl, simple and elegant"
    }
  ],

  "expressions": {
    "neutral": { "description": "平静自然", "prompt_tags": "neutral expression, calm face" },
    "happy": { "description": "眉眼弯弯，嘴角上扬，露出浅笑", "prompt_tags": "happy expression, smiling, eyes curving" },
    "sad": { "description": "眼眶微红，泪光闪烁，嘴角下垂", "prompt_tags": "sad expression, teary eyes, downturned mouth" },
    "angry": { "description": "眉头紧蹙，眼神凌厉，抿唇", "prompt_tags": "angry expression, furrowed brows, sharp eyes" },
    "surprised": { "description": "双眼圆睁，微微张嘴", "prompt_tags": "surprised expression, wide eyes, open mouth" },
    "contemplative": { "description": "目光深远，眉头微蹙，若有所思", "prompt_tags": "contemplative expression, distant gaze, thoughtful" },
    "determined": { "description": "目光坚定，下颚微抬", "prompt_tags": "determined expression, resolute gaze, firm" },
    "shy": { "description": "脸颊微红，目光低垂", "prompt_tags": "shy expression, blushing cheeks, averted gaze" }
  },

  "poses": {
    "standing": "直立，双手自然下垂或交叠于身前",
    "sitting": "端坐，背挺直，双手置于膝上",
    "walking": "缓步行走，姿态优雅",
    "kneeling": "跪坐，姿态端正",
    "lying": "侧卧，姿态放松"
  },

  "personality_traits": {
    "primary": ["聪慧", "坚韧", "谨慎"],
    "secondary": ["善良", "有主见"],
    "affects_appearance": "眼神常带思考，姿态端庄"
  },

  "prompt_template": {
    "base": "young Chinese woman, 18 years old appearance, slender figure, 165cm tall, fair pale skin, oval face, willow leaf eyebrows, almond-shaped dark brown eyes, small straight nose, cherry lips, waist-length jet black hair, anime style",
    "with_costume": "{base}, {costume_prompt}",
    "with_expression": "{base}, {expression_prompt}",
    "full": "{base}, {costume_prompt}, {expression_prompt}, {pose}, {scene_context}"
  },

  "reference_images": {
    "front": "assets/characters/辛月影/front.png",
    "views": "assets/characters/辛月影/views.png",
    "expressions": "assets/characters/辛月影/expressions/"
  }
}
```

---

## 第二部分：人类可读文档 (character_sheet.md)

**必须同步输出 `character_sheet.md` 文件到角色目录**，供人类审阅、编辑，也供其他 Agent（如 prompt-engineer、local-image-generator）读取角色信息。

保存到: `assets/characters/{角色名}/character_sheet.md`

### 模板格式

```markdown
# {角色名} - 角色设计文档

> 生成时间: {时间}  |  项目: {项目名}  |  状态: 初稿/已定稿

---

## 基本信息

【角色定位】
角色名: {角色名}
角色ID: {char_id}
定位: 主角/配角/反派
性别: {性别}
年龄: {年龄}

【性格气质】
关键词: {性格关键词}
整体感觉: {气质描述}
姿态特点: {站姿/坐姿/习惯动作}

---

## 外貌特征

【身体】
身高: {身高}
体型: {体型}
肤色: {肤色}

【面部】
脸型: {脸型}
眼睛: {眼睛描述}
眉毛: {眉毛描述}
鼻子: {鼻子描述}
嘴唇: {嘴唇描述}

【发型】
发色: {发色}
发型: {发型描述}
发饰: {发饰（如有）}

---

## 服装设定

【默认服装】
风格: {古代/现代/奇幻}
上装: {上装描述}
下装: {下装描述}
配色: 主色 {主色} / 辅色 {辅色}
配饰: {配饰列表}
鞋履: {鞋履描述}

【其他服装】（如有）
- 服装2名称: {描述}

---

## 特殊设定

【特殊外貌】
{如有特殊外貌描述；无则填「无」}

【随身道具】
{道具名}: {道具描述}

【身体状态】
{如有残疾、轮椅等特殊状态；无则填「健康」}

---

## 参考图路径

【主视图】
- 正面图: works/{项目名}/assets/characters/{角色名}/front.png
- 四视图: works/{项目名}/assets/characters/{角色名}/views.png

【表情集】
- 表情: works/{项目名}/assets/characters/{角色名}/expressions.png（如有）

---

## AI 绘图提示词

### 正面图提示词 (front.png)

```
{完整的正面图提示词，可直接复制使用}
```

### 四视图提示词 (views.png)

```
{完整的四视图提示词，可直接复制使用}
```

### 负面词

```
{完整的负面词列表}
```

---

## 分镜引用标签

供 prompt-engineer 等下游 Agent 引用的标准化角色描述标签：

【中文标签】
{角色名}: {一句话概括外貌+服装的中文描述}

【英文标签】
{角色名}: {一句话概括外貌+服装的英文描述，用于英文提示词}

---

## 备注

{任何需特别注意的事项}
```

---

## 第三部分：四视图生成流程

### 提示词模板

**重要原则**：四视图必须保持角色一致性，使用统一的角色描述基础 + 视角变化。

#### 基础角色描述（所有视图共用）

```
{性别}，{年龄}岁，{身高}，{体型}。
{肤色}，{脸型}，{五官特征}。
{眼睛描述}，{眉毛描述}。
{鼻子描述}，{嘴唇描述}。
{发型描述}。
身穿{服装描述}，{配色}。
{配饰描述}。
{画风}，高质量动漫风格。
```

#### 正面图提示词

```
角色设计图，正面视角，全身站立，
{基础角色描述}
对称正面姿势，双臂自然下垂，中性表情，
纯白背景，正面参考图，
杰作，最佳画质，细节丰富，8k分辨率。
```

#### 四视图提示词

```
角色设计参考图，包含四个视角：正面视角、左侧视角、右侧视角、背面视角，
同一角色不同角度展示，全身站立，
{基础角色描述}
纯白背景，参考图布局，设计图风格，
杰作，最佳画质，细节丰富，8k分辨率。
```

#### 表情图提示词（可选）

```
角色表情图，{角色名}，
纯白背景上的多个表情，
9个表情3x3排列：开心、悲伤、愤怒、惊讶、平静、害羞、困惑、坚定、恐惧，
同一角色脸部，设计一致，仅头部特写，
{基础角色描述（仅头部）}
杰作，最佳画质，细节丰富。
```

### 负面词

```
低质量，人体结构错误，最差质量，变形，畸形，
缺少肢体，多余肢体，模糊，水印，签名，
文字，标志，裁剪，画框外，比例失调，
不同的脸，特征不一致，多人，
背景杂乱，复杂背景，深色背景。
```

### 特殊情况处理

#### 坐姿角色（如轮椅）

在所有提示词中添加：
```
坐在轮椅上，上半身特写，腿部被遮盖，
```
在 `character_sheet.md` 的【身体状态】中标注：`坐轮椅，双腿残疾`

#### 持有道具

在所有提示词中保持道具一致：
```
手持{道具名}，{道具描述}，
```

### 图片生成调用

#### 步骤1：使用文生图生成正面主视图

```bash
set -a && source .env && set +a && \
uv run python .agent/skills/text-to-image/text_to_image.py \
  --prompt "完整的正面图提示词文本" \
  --output "works/{项目名}/assets/characters/{角色名}" \
  --filename "front"
```

#### 步骤2：使用图生图生成四视图设计图

```bash
set -a && source .env && set +a && \
uv run python .agent/skills/image-to-image/image_to_image.py \
  --image "works/{项目名}/assets/characters/{角色名}/front.png" \
  --prompt "角色设计参考图，包含四个视角：正面视角、左侧视角、右侧视角、背面视角，同一角色不同角度展示，全身站立，纯白背景，参考图布局，保持所有角色特征完全一致" \
  --strength 0.6 \
  --output "works/{项目名}/assets/characters/{角色名}" \
  --filename "views"
```

### 编辑强度建议

| 生成内容 | 建议强度 | 说明 |
|---------|---------|------|
| 正面 → 四视图设计图 | 0.5-0.7 | 中高强度，将单视角转换为多视角设计图 |
| 表情变化 | 0.2-0.4 | 低强度，仅调整表情 |

---

## 第四部分：服装设计参考

### 时代风格匹配

| 时代 | 特点 | 典型元素 |
|------|------|----------|
| 先秦 | 庄重古朴 | 深衣、曲裾 |
| 汉代 | 大气飘逸 | 襦裙、曲裾深衣 |
| 唐代 | 华丽开放 | 齐胸襦裙、大袖衫 |
| 宋代 | 素雅清秀 | 褙子、宋裤 |
| 明代 | 端庄秀丽 | 袄裙、披风 |
| 清代 | 繁复精致 | 旗装、马褂 |

### 颜色寓意

| 颜色 | 寓意 | 适用角色 |
|------|------|----------|
| 红 | 热情、权力、喜庆 | 主角、重要角色 |
| 白 | 纯洁、高贵、哀悼 | 纯真角色、悲剧角色 |
| 黑 | 神秘、威严、权力 | 反派、权臣 |
| 青/蓝 | 清雅、沉稳、文雅 | 书生、智者 |
| 紫 | 高贵、神秘 | 贵族、神秘角色 |
| 黄 | 皇权、富贵 | 皇室 |

### 身份标识

| 身份 | 服装特点 |
|------|----------|
| 皇室 | 明黄、龙凤纹、金丝 |
| 贵族 | 鲜艳色彩、精致刺绣 |
| 文人 | 青蓝色调、素雅 |
| 武将 | 深色、实用剪裁 |
| 平民 | 素色、简单款式 |

---

## 完整工作流程

1. **收集信息** — 从小说文本或用户描述中提取角色信息
2. **生成 `design.json`** — 程序可读的结构化角色设计数据
3. **生成 `character_sheet.md`** — 人类可读的角色设计文档，含完整提示词
4. **文生图生成正面图** — front.png 作为角色定稿和参考图
5. **图生图生成四视图** — views.png（基于front.png，四视角在一张图中）
6. **更新 `character_sheet.md`** — 补充参考图路径、调整描述
7. 检查一致性，如有差异可调整编辑强度重新生成
8. 最后生成表情集（可选）：expressions.png

## 输出格式

| 输出类型 | 文件名 | 说明 |
|---------|--------|------|
| 设计数据 | `design.json` | 程序可读，含完整角色数据 |
| 设计文档 | `character_sheet.md` | 人类可读，含提示词和分镜引用标签 |
| 主视图 | `front.png` | 正面单视角参考图 |
| 四视图 | `views.png` | 正面+左侧+右侧+背面 |
| 表情集 | `expressions.png` | 可选 |

## 质量检查清单

- [ ] 角色外貌与小说描述一致
- [ ] 服装与时代背景匹配
- [ ] 服装与角色身份匹配
- [ ] 颜色搭配和谐
- [ ] 表情描述完整
- [ ] Prompt 模板完整
- [ ] `design.json` 结构完整
- [ ] `character_sheet.md` 输出完整，含分镜引用标签
- [ ] 四视图保持角色一致性
- [ ] 分镜引用【中文标签】和【英文标签】准确

## 注意事项

1. **先生成主视图**：必须先生成 front.png，四视图基于它生成
2. **双输出**：每个角色必须同时有 `design.json` 和 `character_sheet.md`
3. **四视图在一张图中**：views.png 包含四个视角
4. **图生图优势**：使用图生图生成四视图可保持角色特征一致性
5. **编辑强度**：转换后角色变化过大降低强度，变化不够则提高强度
6. **特殊状态**：轮椅、道具等需在提示词和 character_sheet.md 中体现
7. **画风统一**：同一项目使用相同画风关键词
8. **文化适配**：古代用古风词，现代用现代词
9. **描述准确**：自然语言描述画面，短语描述美学风格
10. **分镜引用标签**：`character_sheet.md` 中的标签供 prompt-engineer 直接引用
