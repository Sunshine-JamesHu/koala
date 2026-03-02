# 场景参考 - 第1章

> **如何使用本文件**:
> 1. 本文件是场景设计参考，供后续背景图片生成使用
> 2. "AI提示词核心片段"可直接复制用于生成场景图
> 3. 与 04_image_prompts.md 配合使用，确保场景一致性
> 4. **重要**：必须按照"大全景→中景→特写"的顺序生成

---

## 场景卡生成优先级（重要）⭐⭐⭐

**场景卡的生成必须按照以下顺序进行，确保空间逻辑一致性：**

### 生成顺序
1. **大全景** (必须首先生成) → 建立场景整体空间架构
2. **中景/局部** → 基于大全景延展具体区域
3. **特写/细节** → 基于中景进一步细化

### 为什么这个顺序很重要？
- 大全景定义了整体空间关系（建筑位置、道具布局、光影方向）
- 后续所有局部图必须保持与大全景的空间一致性
- 先整体后局部，避免空间逻辑混乱

---

## 衍生图片一致性要求（重要）⭐⭐⭐

**当基于已生成的图片延展新图片时，必须保持以下一致性：**

### 空间一致性
- **位置关系**: 物体之间的相对位置必须与原图一致
- **透视关系**: 保持相同的视角和透视
- **比例关系**: 物体大小比例必须一致

### 元素一致性
- **道具位置**: 场景中的道具位置必须保持一致
- **材质细节**: 材质纹理必须与原图匹配
- **光影方向**: 光源位置和方向必须一致

### 色彩一致性
- **色温**: 保持相同的色温（暖光/冷光）
- **饱和度**: 色彩饱和度保持一致
- **氛围**: 整体氛围感保持一致

---

## 场景总览

| 场景编号 | 场景名 | 时间 | 天气 | 情绪氛围 |
|----------|--------|------|------|----------|
| 01 | 破败草屋·卧房 | 深夜 | 寒冬阴冷 | 压抑、紧张、诡异 |
| 02 | 破败草屋·小厅 | 深夜 | 寒冬阴冷 | 阴森、血腥、恐怖 |
| 03 | 破败草屋·门外 | 深夜 | 寒冬阴冷 | 绝望、寒冷、月光 |

---

## 场景完整布局说明

> **重要**: 此部分综合了小说多个章节中对该场景的描述，确保场景设计完整准确。

### 建筑整体结构
- **类型**: 简陋的三间草屋（一列式布局）
- **布局**: 共三间房，从左到右依次为：灶房 - 小厅 - 卧房
- **主要建筑**: 单栋土坯房，茅草屋顶，破败不堪

### 室外空间
- **院子**: 小型院落，地面泥土地，长有杂草，角落有水缸
- **围墙**: 无围墙（或极低篱笆），院落空旷
- **大门**: 简陋木门，掉漆破旧
- **其他**: 木桩（拴驴用）、远处是树林和山脉

### 室内分区
| 房间 | 功能 | 主要陈设 | 状态 |
|------|------|---------|------|
| 灶房（左） | 厨房 | 大锅、水缸、灶台、破碗筷、木头锅盖 | 凌乱破败 |
| 小厅（中） | 通道/临时住所 | 缺腿木凳、掉皮方桌、樟木箱×3 | 破旧不堪 |
| 卧房（右） | 主卧室 | 土炕、破褥子、小木桌、轮椅、破柜子 | 阴冷破败 |

### 场景平面示意图

```
                          【远处：树林/山脉】
                    ┌─────────────────────────┐
                    │                         │
                    │        院 子             │
                    │    （泥土地、杂草）        │
                    │                         │
                    │    ┌───┐      ┌───┐     │
                    │    │水缸│      │木桩│     │
                    │    └───┘      └───┘     │
                    │                         │
┌─────────────────────────────────────────────────────┐
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │          │  │          │  │          │          │
│  │   灶房   │  │   小厅   │  │   卧房   │  ←朝南   │
│  │  (厨房)  │  │  (通道)  │  │ (主场景) │          │
│  │          │  │          │  │          │          │
│  │ 灶台/锅  │  │桌/凳/箱  │  │炕/轮椅   │          │
│  │  水缸    │  │          │  │  小桌    │          │
│  │          │  │          │  │         │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│                                                     │
│                    ═══ 木门 ═══                     │
└─────────────────────────────────────────────────────┘
                          【大门朝南】
```

### 室内详细布局（卧房 - 主场景）

```
┌────────────────────────────────────┐
│                                    │
│  ┌──────┐                          │
│  │ 柜子 │           ┌──────────┐   │
│  │      │           │   轮椅   │   │
│  └──────┘           │  (中央)  │   │
│                     └──────────┘   │
│  ┌─────────────────────────────┐   │
│  │           土 炕             │   │
│  │    （破褥子、小木桌）        │   │
│  │  ┌─────────────────────┐   │   │
│  │  │ 扶手(墙上)          │   │   │
│  │  └─────────────────────┘   │   │
│  └─────────────────────────────┘   │
│                                    │
│       📍青灯                🪟窗   │
│       (角落)              (破洞)   │
└────────────────────────────────────┘
         ↑
       门口
```

---

## 场景 01: 破败草屋·卧房（主场景）

### 基础信息
- **地点类型**: 室内
- **时代风格**: 古代架空（边陲贫困山村）
- **建筑风格**: 简陋土坯房，茅草屋顶

### 时间与天气
- **时间**: 深夜（约子时至丑时）
- **天气**: 寒冬阴冷，北风呼啸
- **光线来源**: 单一青灯 + 月光

### 整体氛围
阴冷压抑、破败贫困、死亡威胁的恐怖氛围

### 空间结构
- **大小**: 小型房间，约3×4米
- **地面**: 泥土地面，散落碎瓷片和残羹
- **墙壁**: 土坯墙，发霉斑驳
- **屋顶**: 茅草顶，有漏风处
- **窗户**: 破旧木窗，窗纸破损有洞

### 主要元素
| 元素 | 位置 | 描述 |
|------|------|------|
| 土炕 | 靠后墙 | 简陋通炕，破褥子漏棉花 |
| 轮椅 | 房间中央 | 破败木制轮椅，沉重 |
| 青灯 | 角落/炕桌 | 唯一光源，火焰摇曳 |
| 小木桌 | 炕上 | 简陋木桌 |
| 柜子 | 墙角 | 破旧木柜 |
| 碎瓷 | 地面散落 | 满地碎瓷片 |
| 三尺剑 | 沈清起手边/刺入木柱 | 锋利长剑 |

### 光影设定
- **主光源**: 青灯（昏黄烛光），位置在角落或炕桌上
- **辅助光**: 月光穿过破窗纸，形成光束
- **阴影风格**: 软阴影，火焰摇曳产生动态影子
- **特殊效果**: 体积光（月光光束），尘埃粒子

### 色彩设定
- **主色调**: 青灰色、暗褐色、昏黄色
- **辅助色**: 月白色（月光）、深黑色（阴影）
- **整体色温**: 冷色为主（压抑），局部暖光（烛光）
- **情绪氛围**: 压抑、阴森、恐怖

### 氛围元素
- **空气感**: 混浊，有霉味
- **粒子效果**: 尘埃在光束中飘浮
- **动态元素**: 烛火摇曳、寒风吹入

---

## AI提示词核心片段

### 场景 01: 破败草屋·卧房

#### 基础版
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese dilapidated cottage bedroom interior,
late night, cold winter, northern wind howling outside,
single flickering blue oil lamp (qingdeng) as main light source,
pale moonlight streaming through holes in torn window paper,
mud floor covered with shattered porcelain pieces and spilled food,
old worn wooden wheelchair sitting in center of room,
traditional kang bed platform against wall with worn bedding,
oppressive and eerie atmosphere,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

#### 完整版（详细）
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese dilapidated cottage interior, poverty-stricken rural home bedroom,
late night scene, cold winter night, northern wind howling outside,

single flickering blue oil lamp (qingdeng) as main light source, casting dancing shadows on mud walls,
pale cold moonlight streaming through holes in torn window paper, creating eerie volumetric light beams cutting through darkness,

mud floor covered with shattered porcelain pieces and spilled food remnants,
dust particles floating visible in light beams, atmospheric depth,

traditional kang bed platform against back wall, thin worn bedding with exposed cotton,
small wooden table on kang, simple wooden cabinet in corner,

moldy spotted earthen walls, thatched roof with gaps letting in cold air,
broken wooden window frame with torn paper,

dramatic chiaroscuro lighting, soft flickering shadows,
volumetric moonlight beams, dust motes dancing in light,

color palette: cold blue-grey dominant (#5D6D7E), warm yellow candlelight accent (#F4D03F), pale moonlight highlights (#D5D8DC),
oppressive and eerie atmosphere, suffocating sense of poverty and desperation, threatening mood,

wide establishing shot, eye-level angle, depth of field blur on background,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, Octane Render, 3D animation style
--ar 16:9
```

### 场景 02: 破败草屋·小厅

#### 完整版
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese dilapidated cottage hallway interior, small central hall connecting rooms,
late night scene, dim lighting from adjacent rooms,

broken wooden stool with missing leg, peeling lacquer square table,
three dusty camphor wood chests stacked in corner,
blood stains on floor (recently cleaned but still visible),
cold damp atmosphere,

sparse furniture, bare earthen walls, worn wooden floor boards,
draft from gaps in walls and door,

dim ambient lighting, shadows in corners,
cold color palette: dark grey, brown, black,

medium shot, eye-level angle, focus on central space,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

### 场景 03: 破败草屋·门外

#### 完整版
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

exterior of ancient Chinese dilapidated cottage at night,
small rural courtyard with bare mud ground, wild grass growing,
old wooden door frame, worn and weathered,

cold winter night, crescent moon in dark sky, stars visible,
northern wind blowing, dead leaves scattering,

moonlight illuminating the scene, long shadows cast by building,
dim warm light visible through window cracks,

water jar in corner, wooden stake for donkey in yard,
distant forest silhouettes and mountain outlines,

cold color palette: dark blue night sky, silver moonlight, grey-brown earth,
lonely and desolate atmosphere, ominous feeling,

medium wide shot, slight low angle, moonlight as key light,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

---

## 负向提示词

**通用负向提示词**:
```
people, characters, faces, figures, text, watermark, signature,
low quality, worst quality, blurry, distorted, deformed,
modern elements, western style, electric lights, cars, buildings, concrete,
2d flat, sketch, line art, photo realistic, plastic look,
bright colors, warm cozy atmosphere, clean tidy room, new furniture
```

---

## 场景视角卡生成提示词

### 破败草屋·卧房 8视角

```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,
Interior of a dilapidated ancient Chinese cottage bedroom, poverty-stricken rural home, late night, single flickering blue oil lamp, moonlight through torn window paper, mud floor with shattered porcelain, worn wooden wheelchair in center, traditional kang bed, oppressive eerie atmosphere,

| 全景远景 | 整个卧房全貌，青灯在角落摇曳，月光照入，轮椅在中央，炕在后墙 | wide establishing shot, full room view, eye-level |
| 轮椅特写 | 聚焦破败木制轮椅，周围碎瓷散落，昏暗光线下 | close-up of worn wooden wheelchair, shattered porcelain around |
| 地面细节 | 碎瓷片和残羹散落的泥土地面，在微弱光线下，尘埃飘浮 | close-up of floor, broken porcelain shards, spilled food, dust particles |
| 窗户光效 | 月光穿过破洞窗纸，形成体积光束，尘埃粒子可见 | moonlight through torn window paper, volumetric light beams, dust particles |
| 青灯摇曳 | 青灯特写，火焰跳动，光影在墙上舞动，昏黄光芒 | flickering blue oil lamp, dancing flame, dynamic shadows on wall |
| 炕上视角 | 从炕上看向房间，轮椅剪影，门口轮廓，阴冷氛围 | view from kang platform, wheelchair silhouette, doorway outline |
| 门口视角 | 从门口看向卧房内，整体布局，青灯和月光交织 | view toward interior from doorway, room layout, lamp and moonlight |
| 俯视全景 | 从屋顶向下看，整个卧房布局，角色位置参考 | aerial top-down view, room layout, character placement reference |

masterpiece, best quality, 8k resolution, highly detailed background, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style

按2行生成，每行4个视角，只生一张 4*2 的场景8视角图片
```

---

## 场景与前后章节的时空连贯性说明

### 时间线检查
| 章节 | 时间 | 天气 | 场景状态 |
|------|------|------|----------|
| 第1章（本章） | 深夜 | 寒冬阴冷 | 破败草屋，危机四伏 |
| 第2章 | 深夜→凌晨 | 寒冬 | 延续，埋尸场景 |
| 第3章 | 白天 | 寒冬 | 灶房、小厅场景增加 |
| 第4-5章 | 白天 | 寒冬 | 开始制作轮椅，院子里场景 |

### 空间连贯性
- 第1章全部场景在卧房内
- 第2章会延伸到小厅、门外、树林
- 第4章开始大量使用院子场景

---

## 本章关键画面场景说明

### 画面1: 穿书苏醒
- **场景**: 卧房地面
- **视角**: 辛月影主观视角（仰视）
- **焦点**: 天花板、青灯光晕、远处轮椅剪影

### 画面2: 病娇亮相
- **场景**: 卧房内，轮椅位置
- **视角**: 中景，辛月影视角
- **焦点**: 沈清起脸部，月光照亮

### 画面3: 剑指咽喉
- **场景**: 卧房内，木柱旁
- **视角**: 特写
- **焦点**: 剑尖、辛月影惊恐的脸

### 画面4: 夺门被拦
- **场景**: 门口
- **视角**: 中景
- **焦点**: 辛月影撞上霍齐

### 画面5: 谎言求生
- **场景**: 卧房内
- **视角**: 中景
- **焦点**: 辛月影表演，沈清起冷笑

---

## 场景色彩参考

### 色卡

| 元素 | 颜色 | HEX |
|------|------|-----|
| 墙壁（暗部） | 青灰色 | #5D6D7E |
| 地面（泥土） | 暗褐色 | #6B4423 |
| 烛光（青灯） | 昏黄色 | #F4D03F |
| 月光 | 月白色 | #D5D8DC |
| 阴影 | 深黑色 | #1A1A2E |
| 破旧木器 | 褐色 | #8B7355 |
| 碎瓷片 | 灰白色 | #BDC3C7 |

### 光影氛围示意

```
     [月光] ──────────────→
                              ↓
         ┌─────────────────────────────────┐
         │  🌙月光光束穿过破窗             │
         │     ↓                           │
         │     ↓                           │
         │  ┌─────┐                        │
[青灯] → │  │     │   ← 烛光照亮区域       │
  🪔     │  │轮椅 │                        │
         │  │     │                        │
         │  └─────┘                        │
         │                                 │
         │     ↓ 月光继续                  │
         │  ┌─────────┐                    │
         │  │   炕     │  ← 烛光+月光混合  │
         │  └─────────┘                    │
         └─────────────────────────────────┘
```

---

*由 AI场景设计师 生成*
