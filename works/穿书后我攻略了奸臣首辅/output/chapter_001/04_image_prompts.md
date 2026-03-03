# 图片生成提示词 - 第1章 你自尽吧

> **使用说明**:
> - 将"提示词"内容直接复制到 Nano Banana Pro
> - 负向提示词用于避免常见问题
> - 图片比例根据需要调整 --ar 参数
> - **参考图**: 第1章是首次建立角色视觉，请先上传三视图+场景大全景

---

## 风格配置（从 style.json 提取）

**风格前缀**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,
```

**风格后缀**:
```
, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style
```

**质量标签**:
```
masterpiece, best quality, 8k resolution, highly detailed, ultra detailed, elegant, beautiful, 3D render, cinematic lighting, depth of field
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look
```

---

## 角色关键帧

---

### 辛月影 系列提示词

#### KF-01: 辛月影 - 苏醒

**图片用途**: 关键帧（开篇第一个镜头）

**画面描述**:
辛月影趴在阴冷的泥地上，缓缓睁开眼睛，视线从模糊到清晰。她的脸贴在地面，能看到地面上散落的碎瓷片和泥土纹理。青灰色的色调，压抑的氛围。

**参考图来源说明**:
- 本关键帧是首次建立角色视觉（第1章）
- 参考图来源: 三视图 + 场景大全景
- 延展理由: N/A（首次生成）

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 辛月影-三视图 | 角色外观基础（首次建立） |
| 参考图2 | 辛月影-表情卡（惊恐/迷茫） | 表情参考 |
| 参考图3 | 草屋内-大全景 | 场景空间参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old young Chinese woman,
pretty and sweet face with almond-shaped eyes (xing yan), long dark eyelashes,
small delicate oval face, slightly upturned nose, soft pink lips,
petite and slender body, graceful figure,
double spiral hair bun (shuang luo ji) on sides of head, traditional Chinese hairstyle, glossy black hair,
wearing patched coarse cloth robe in dark gray and brown colors, worn-out ancient Chinese peasant dress,

lying face down on cold earthen ground, cheek pressed against the floor,
slowly opening eyes, dazed and confused expression,
disoriented look, groggy from just waking up,

ancient Chinese dilapidated cottage bedroom interior,
mud floor texture visible, scattered broken porcelain shards on ground,
dim blue oil lamp light in corner, cold moonlight through torn window paper,
oppressive and suffocating atmosphere of poverty,

close-up shot from low angle, eye-level with the floor,
depth of field blur on background, focus on her face and the floor texture,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
standing, sitting, bright lighting, clean floor, luxurious clothes, red dress
```

---

#### KF-02: 辛月影 - 轻松调侃

**图片用途**: 关键帧（以为在做梦的轻松时刻）

**画面描述**:
辛月影翻身侧卧，一手支着脸颊，另一只手放在大腿上，慵懒地望着前方，嘴角挂着轻松的笑意。她以为自己还在梦里。

**参考图来源说明**:
- 本关键帧基于 KF-01 延展
- 延展理由: 服装、外观完全一致，仅姿态和表情变化

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-01_辛月影-苏醒 | 前一关键帧（确保角色一致性） |
| 参考图2 | 辛月影-表情卡（轻松/调皮） | 新表情参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old young Chinese woman,
pretty and sweet face with almond-shaped bright eyes, playful glint in eyes,
small delicate oval face, soft smile on lips,
double spiral hair bun (shuang luo ji), glossy black hair,
petite and slender body,
wearing patched coarse cloth robe in dark gray and brown, worn-out peasant dress,

lying on side on the ground, one hand propping up cheek,
other hand resting on thigh,
relaxed and lazy posture, casual confident attitude,
slight playful smile, dreamy relaxed expression,
teasing look as if talking to someone,

ancient Chinese dilapidated cottage interior,
dim oil lamp lighting, cold moonlight through window,
scattered debris on floor,

medium close-up shot, low angle,
focus on her face and relaxed expression,
soft depth of field on background,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
standing, sitting on bed, bright lighting, scared expression, crying
```

---

#### KF-03: 辛月影 - 瞳孔骤缩

**图片用途**: 关键帧（听到"辛四娘"震惊瞬间）

**画面描述**:
辛月影的大特写，聚焦她的眼睛。听到"辛四娘"三字，她的瞳孔瞬间收缩，眼神从轻松变为震惊和恐惧。

**参考图来源说明**:
- 本关键帧基于 KF-02 延展
- 延展理由: 服装、外观完全一致，仅表情变化

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-02_辛月影-轻松调侃 | 前一关键帧（确保角色一致性） |
| 参考图2 | 辛月影-表情卡（震惊/恐惧） | 新表情参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Extreme close-up of Xin Yueying's eyes,
20 years old young Chinese woman,
almond-shaped eyes suddenly wide with shock,
pupils contracted in terror,
fear and disbelief in her gaze,
blood draining from face,

double spiral hair bun (shuang luo ji) visible at edge of frame,
wearing patched coarse cloth robe,

expression of sudden realization and horror,
moment of truth dawning on her,
frozen in shock,

dark background with faint candlelight,
dramatic lighting on her face,
high contrast shadows,

extreme close-up shot, focus on eyes,
shallow depth of field, sharp focus on pupils,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
full face, body visible, relaxed expression, smiling, bright lighting
```

---

#### KF-04: 辛月影 - 惊恐撞柱

**图片用途**: 关键帧（沈清起长剑逼来，辛月影后退撞木柱）

**画面描述**:
辛月影惊惶起身，踉跄后退，脊背猝不及防撞在了背后的木柱之上。她浑身颤抖，艰涩地开口试图解释。

**参考图来源说明**:
- 本关键帧基于 KF-03 延展
- 延展理由: 服装、外观完全一致，姿态和表情变化

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-03_辛月影-瞳孔骤缩 | 前一关键帧（确保角色一致性） |
| 参考图2 | 草屋内-大全景 | 场景空间参考（木柱位置） |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old young Chinese woman,
pretty face with almond-shaped eyes wide with terror,
pale complexion from fear, trembling lips,
small oval face, expression of desperation,
double spiral hair bun (shuang luo ji), slightly disheveled,
petite and slender body,
wearing patched coarse cloth robe in dark gray and brown,

back pressed against a rough wooden pillar,
standing but trembling, body language showing fear,
shoulders hunched, hands raised defensively,
looking up with terrified pleading eyes,

ancient Chinese dilapidated cottage interior,
wooden pillar visible behind her,
dim oil lamp casting long shadows,
cold moonlight from side window,
scattered porcelain shards on floor,
sword light glinting in foreground,

medium close-up shot, eye-level angle,
depth of field blur on background,
dramatic chiaroscuro lighting,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
sitting, lying, calm expression, smiling, bright lighting, clean room
```

---

#### KF-05: 辛月影 - 声泪俱下

**图片用途**: 关键帧（演技爆发，编造谎言求生）

**画面描述**:
辛月影声泪俱下地表演，双手合掌，眼泪恰到好处地流下。她表情真挚委屈，试图让沈清起相信她的谎言。

**参考图来源说明**:
- 本关键帧基于 KF-04 延展
- 延展理由: 服装、外观完全一致，仅姿态和表情变化

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-04_辛月影-惊恐撞柱 | 前一关键帧（确保角色一致性） |
| 参考图2 | 辛月影-表情卡（哭泣/委屈） | 新表情参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old young Chinese woman,
pretty face with almond-shaped eyes brimming with tears,
tears streaming down her cheeks, glistening in candlelight,
expression of genuine distress and pleading,
small oval face, quivering lips,
double spiral hair bun (shuang luo ji), glossy black hair,
petite and slender body,
wearing patched coarse cloth robe in dark gray and brown,

hands pressed together in pleading gesture,
kneeling or crouching position, body language showing desperation,
looking up with tearful pleading eyes,
acting distressed but calculating,

ancient Chinese dilapidated cottage interior,
dim oil lamp flickering, casting warm yellow glow on her face,
cold moonlight from window creating contrast,
emotional dramatic atmosphere,

medium close-up shot, slightly low angle looking up at her,
focus on her tearful expression,
depth of field blur on background,
cinematic emotional lighting,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
standing tall, angry expression, dry eyes, bright lighting, clean background
```

---

### 沈清起 系列提示词

#### KF-06: 沈清起 - 隐匿阴影中

**图片用途**: 关键帧（开篇神秘亮相，隐匿在黑暗中）

**画面描述**:
草屋角落的黑暗中，一个神秘人的剪影若隐若现。烛光从侧面照来，只能勉强照亮他苍白的面容，身体和座位完全隐没在阴影中。

**参考图来源说明**:
- 本关键帧是首次建立角色视觉（第1章）
- 参考图来源: 三视图 + 场景大全景
- 延展理由: N/A（首次生成）

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 沈清起-三视图 | 角色外观基础（首次建立） |
| 参考图2 | 沈清起-表情卡（冷漠/阴鸷） | 表情参考 |
| 参考图3 | 草屋内-大全景 | 场景空间参考 |

**⚠️ 隐匿元素处理**:
- 沈清起在本镜头中是**隐匿在黑暗中的**，身体和轮椅几乎看不见
- **不要直接写 "wheelchair"**，AI会生成清晰的轮椅
- 使用 "seated figure" 和 "hidden in shadow" 描述

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

In the deep dark corner of a dilapidated cottage,
a silhouette of a seated figure barely visible in the shadows,
only a pale face faintly illuminated by flickering candlelight from the side,
the rest of the figure completely hidden in darkness,
mysterious and ominous presence,

Shen Qingqi, 25 years old young Chinese man,
handsome refined face barely visible, sharp angular features,
narrow phoenix eyes (feng yan) with cold dark gaze visible in dim light,
thin lips, pale almost bloodless complexion,
long black hair tied in traditional topknot,
wearing dark ancient Chinese scholar robe, only collar visible,

faint blue oil lamp (qingdeng) as main light source,
moonlight through torn window paper creating eerie atmosphere,
dramatic chiaroscuro lighting, high contrast between light and shadow,
oppressive and tense mood,

medium shot from slight distance,
figure emerging from darkness,
atmospheric depth with volumetric shadows,
cinematic noir lighting,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
wheelchair visible, standing, walking, bright lighting, clearly visible body, happy expression, smiling
```

---

#### KF-07: 沈清起 - 月下阴鸷

**图片用途**: 关键帧（月光洒落，阴鸷面容清晰展现）

**画面描述**:
清白的月辉穿过破了洞的窗纸，泻在沈清起英挺的脸上，将那张本就毫无血色的脸庞镀了一层森森的寒光。他狭长的凤眼淬着浓烈的寒意，薄唇衔着一抹混沌的笑意。

**参考图来源说明**:
- 本关键帧基于 KF-06 延展
- 延展理由: 服装、外观完全一致，光线和角度变化

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-06_沈清起-隐匿阴影中 | 前一关键帧（确保角色一致性） |
| 参考图2 | 沈清起-表情卡（阴鸷/冷笑） | 新表情参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Shen Qingqi, 25 years old young Chinese man,
handsome and refined face, sharp angular features,
narrow phoenix eyes (feng yan) with intense cold gaze,
thin lips with a cold mysterious smile,
pale almost bloodless complexion,
long black hair tied in traditional topknot, strands catching moonlight,
wearing dark ink-black ancient Chinese scholar robe,

seated figure, upper body visible,
face illuminated by pale cold moonlight streaming through torn window paper,
moonlight creating a ghostly silver glow on his pale features,
eerie and haunting atmosphere,

ancient Chinese dilapidated cottage interior,
window with torn paper visible, moonlight beams cutting through darkness,
broken porcelain scattered on floor, dilapidated setting,

medium close-up shot focusing on face,
dramatic side lighting from moonlight,
strong contrast between lit face and dark background,
cinematic atmospheric lighting,
cold blue-white color temperature,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
wheelchair clearly visible, standing, warm lighting, smiling happily, bright colors
```

---

#### KF-08: 沈清起 - 碎瓷渗血

**图片用途**: 关键帧（特写镜头，手中碎瓷渗血）

**画面描述**:
沈清起指骨分明的手在轻轻的摩挲着碎瓷。碎瓷锋利的边缘已经割破皮肤，鲜血自他的指缝之间涔涔流出，坠在地面。他的手苍白冰冷，手背上耸着根根分明的青筋。

**参考图来源说明**:
- 本关键帧是特写镜头，不展示角色面部
- 参考图来源: KF-07（确认手的造型一致）

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-07_沈清起-月下阴鸷 | 确保手的造型与角色一致 |
| 参考图2 | 草屋内-大全景 | 场景空间参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Extreme close-up of a man's hand,
pale slender fingers with visible veins on back of hand,
long elegant fingers, bony knuckles,
cold pale skin tone,

holding a sharp broken porcelain shard,
gripping it tightly, blood dripping from between fingers,
red blood drops falling toward ground,
fresh cuts on palm from sharp edges,
blood droplets glistening in dim light,

dark background with faint candlelight glow,
blood drops catching the warm yellow light,
dramatic lighting contrast,
focus on hand and falling blood,

extreme close-up shot, macro detail,
shallow depth of field, sharp focus on hand,
blood drops in mid-fall frozen in time,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
full body, face visible, bright lighting, clean hand, no blood, healthy skin color
```

---

#### KF-09: 沈清起 - 阴鸷冷笑

**图片用途**: 关键帧（结尾悬念，阴鸷的笑容）

**画面描述**:
沈清起扬着唇角，他的笑声变得绵长，眼中闪烁着危险的光芒。他冷笑着说出"让他下黄泉去陪你"的威胁。

**参考图来源说明**:
- 本关键帧基于 KF-07 延展
- 延展理由: 服装、外观完全一致，仅表情变化

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | KF-07_沈清起-月下阴鸷 | 前一关键帧（确保角色一致性） |
| 参考图2 | 沈清起-表情卡（冷笑/威胁） | 新表情参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Shen Qingqi, 25 years old young Chinese man,
handsome refined face with cold threatening smile,
narrow phoenix eyes (feng yan) with sinister glint,
thin lips curved in chilling smirk,
pale almost bloodless complexion,
long black hair tied in traditional topknot,
wearing dark ink-black ancient Chinese scholar robe,

seated position, upper body visible,
head slightly tilted, looking down with menacing gaze,
cold calculating expression, threatening aura,
smile that doesn't reach his eyes,

ancient Chinese dilapidated cottage interior,
dim oil lamp casting dramatic shadows,
moonlight from window creating eerie atmosphere,
oppressive tense mood,

medium close-up shot focusing on face,
dramatic low-key lighting,
strong contrast between light and shadow,
cinematic noir atmosphere,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
wheelchair visible, standing, warm smile, friendly expression, bright lighting
```

---

### 霍齐 系列提示词

#### KF-10: 霍齐 - 怒视守门

**图片用途**: 关键帧（霍齐首次登场，拦住辛月影）

**画面描述**:
霍齐的仰视镜头。他蓄着络腮胡，虎目圆睁，孔武有力。月光在他身后形成轮廓光，使他的形象更加威严可怕。他愤怒地盯着辛月影。

**参考图来源说明**:
- 本关键帧是首次建立角色视觉（第1章）
- 参考图来源: 三视图 + 场景大全景
- 延展理由: N/A（首次生成）

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 霍齐-三视图 | 角色外观基础（首次建立） |
| 参考图2 | 霍齐-表情卡（愤怒） | 表情参考 |
| 参考图3 | 草屋门口-大全景 | 场景空间参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Huo Qi, 28 years old Chinese man,
rugged masculine face with full beard covering jaw,
round fierce tiger eyes glaring with anger,
tanned bronze skin, weathered features,
tall and muscular powerful build,
wearing coarse brown short jacket and worn trousers,
straw sandals, simple rope belt at waist,

standing like an iron tower, blocking the doorway,
arms crossed or at sides, intimidating posture,
furious expression, veins visible on neck from anger,
looking down with righteous wrath,

ancient Chinese cottage doorway,
old wooden door frame with peeling paint,
bright moonlight behind creating rim lighting effect,
silhouette effect with moonlight outlining his figure,

medium close-up shot from low angle looking up,
emphasizing his imposing presence,
dramatic backlighting from moon,
strong contrast between dark figure and bright moon,

, masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
clean shaven, slender build, smiling, bright frontal lighting, indoor scene
```

---

## 关键帧总表

| 编号 | 角色 | 状态 | 对应镜头 | 参考图来源 |
|------|------|------|----------|------------|
| KF-01 | 辛月影 | 苏醒 | 1-1 | 三视图（首次建立） |
| KF-02 | 辛月影 | 轻松调侃 | 1-4 | KF-01 |
| KF-03 | 辛月影 | 瞳孔骤缩 | 2-2 | KF-02 |
| KF-04 | 辛月影 | 惊恐撞柱 | 3-1 | KF-03 |
| KF-05 | 辛月影 | 声泪俱下 | 4-3 | KF-04 |
| KF-06 | 沈清起 | 隐匿阴影中 | 1-2, 1-3 | 三视图（首次建立） |
| KF-07 | 沈清起 | 月下阴鸷 | 2-1 | KF-06 |
| KF-08 | 沈清起 | 碎瓷渗血 | 2-3 | KF-07 |
| KF-09 | 沈清起 | 阴鸷冷笑 | 4-4 | KF-07 |
| KF-10 | 霍齐 | 怒视守门 | 3-4 | 三视图（首次建立） |

---

## 关键帧延展关系图

```
第1章关键帧延展链:

辛月影:
三视图 → KF-01(苏醒) → KF-02(轻松) → KF-03(震惊) → KF-04(恐惧) → KF-05(演戏)
         ↑首次建立    └──────── 基于前一帧延展 ────────────────→

沈清起:
三视图 → KF-06(隐匿) → KF-07(月下) → KF-08(手特写)
         ↑首次建立    └──── 基于前一帧延展 ────→
                              └──→ KF-09(冷笑)
                                  (基于KF-07)

霍齐:
三视图 → KF-10(怒视)
         ↑首次建立
```

---

## 隐匿元素处理说明

**KF-06（沈清起-隐匿阴影中）使用了隐匿元素处理**:
- 角色在画面中是"隐匿在黑暗中的"，身体几乎看不见
- 不直接写 "wheelchair"，AI会生成清晰的轮椅
- 使用 "seated figure"、"silhouette"、"hidden in shadow" 描述
- 只描述可见的部分：苍白的面容

---

*由 AI原画师 生成*


---

# 背景场景提示词



### BG-01: 破败草屋·主屋 - 大全景

**场景状态**: 首次建立（第1章）

**画面描述**:
破败草屋主屋的完整内部空间。昏暗的室内，只有一盏青灯和月光照明。泥土地面，土炕靠后墙，角落有柜子，满地碎瓷片。青灰色的压抑氛围。

**空间关系说明**:
- 主建筑结构: 土墙围合的长方形房间，约10-12平方米
- 土炕位置: 靠后墙，占据房间约1/3宽度
- 柜子位置: 房间角落
- 青灯位置: 角落桌上
- 窗户位置: 侧墙，窗纸有破洞
- 门的位置: 通往小厅

**光影说明**:
- 主光源: 角落青灯（昏黄、摇曳）
- 辅助光: 月光透过窗纸（冷白）
- 光影方向: 从左上角斜射
- 色彩基调: 青灰色、暗褐色、昏黄色

**场景延展说明**:
- 本场景是首次建立（第1章）
- 参考图来源: 场景参考图
- 变化描述: N/A（首次生成）

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 草屋内-布局参考 | 场景布局参考（从03_scene_refs.md） |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Wide establishing shot of ancient Chinese dilapidated cottage bedroom interior,
poverty-stricken rural home in border village,
late night scene, cold winter atmosphere,

Complete room layout:
- Packed dirt floor with scattered broken porcelain shards and spilled food remnants
- Traditional kang bed platform against back wall, worn-out cotton quilt with leaking stuffing
- Small wooden table on the kang surface
- Old wooden cabinet in corner covered in dust
- Single blue oil lamp (qingdeng) flickering on corner table
- Small window with torn paper letting in cold moonlight
- Wooden door frame leading to hallway
- Earthen walls with visible cracks and mold patches
- Low ceiling with exposed wooden beams

Lighting:
- Single flickering blue oil lamp as main warm light source in corner
- Cold pale moonlight streaming through holes in torn window paper
- Creating eerie volumetric light beams cutting through darkness
- Dramatic chiaroscuro lighting with strong contrast
- Dust particles floating visible in light beams

Atmosphere:
- Oppressive and suffocating atmosphere of poverty and desperation
- Cold blue-grey dominant color palette with warm yellow candlelight accent
- Dark and gloomy, tense mysterious mood
- Sense of decay and abandonment

Composition:
- Wide establishing shot, eye-level angle
- Full room visible from doorway perspective
- Depth of field blur on far corners
- Cinematic atmospheric depth

, masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
people, characters, person, human, figure, silhouette, face, body, wheelchair, sword, weapon, bright lighting, clean tidy room, luxurious furniture, warm cozy atmosphere
```

---

### BG-06: 草屋门口 - 月光下大全景

**场景状态**: 首次建立（第1章）

**画面描述**:
草屋门口的外景，月光洒落。破旧的木门，掉了漆皮。门口有小片空地，远处是漆黑的树林。深夜的寒冷氛围。

**空间关系说明**:
- 木门位置: 中央
- 门槛: 破旧
- 门前空地: 泥土地面
- 远处: 树林剪影
- 月光方向: 从上方/侧后方

**光影说明**:
- 主光源: 月光（冷白）
- 光影方向: 从上方斜射
- 色彩基调: 月白色、墨蓝色、暗褐色

**场景延展说明**:
- 本场景是首次建立（第1章）
- 参考图来源: 场景参考图
- 变化描述: N/A（首次生成）

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 草屋门口-布局参考 | 场景布局参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Wide establishing shot of ancient Chinese cottage doorway exterior,
rural border village at late night,
cold winter scene with pale moonlight,

Scene elements:
- Old wooden door with peeling paint and worn threshold
- Cracked mud walls of cottage exterior
- Thatched roof silhouette against night sky
- Small patch of bare earth ground in front of door
- Bare tree branches visible on sides casting shadows
- Dense forest visible in far background as dark silhouettes
- Stone step leading to doorway

Lighting:
- Cold pale moonlight as main light source from above
- Creating dramatic rim lighting on door frame edges
- Soft blue-white color temperature
- Long shadows cast by door frame and trees
- Stars faintly visible in dark blue night sky

Atmosphere:
- Eerie and mysterious nighttime atmosphere
- Cold and desolate, tense mood
- Sense of isolation and danger
- Fog near ground in distance

Composition:
- Wide shot, eye-level angle
- Door centered in frame
- Depth of field blur on distant forest
- Cinematic noir night lighting

, masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
people, characters, person, human, figure, silhouette, face, body, bright lighting, daytime, sunny, warm colors, indoor scene
```

---

## 第二层：中景/局部（基于大全景延展）

---

### BG-02: 破败草屋·角落阴影 - 中景

**基于**: BG-01 大全景

**画面描述**:
草屋内阴暗角落的特写。这里光线最暗，只有微弱的青灯光芒从远处照来。角落有旧柜子，蛛网悬挂，阴影浓重。

**场景延展说明**:
- 本场景基于 BG-01 延展
- 变化描述: 聚焦角落区域，更暗的光线

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | BG-01_草屋内-大全景 | 确保空间一致性 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Medium shot of dark corner in dilapidated cottage bedroom,
Based on the room panorama, focusing on the shadowed corner area,

Corner elements:
- Old wooden cabinet with peeling lacquer, covered in thick dust
- Spider webs hanging from ceiling to cabinet
- Cracks in earthen wall visible in faint light
- Pile of old fabric or rags on floor
- Deepest shadows in the room

Lighting:
- Very dim lighting, almost complete darkness
- Faint warm glow from distant oil lamp barely reaching this corner
- High contrast between deep shadows and faint light
- Mysterious and ominous atmosphere

Atmosphere:
- Oppressive and claustrophobic feeling
- Sense of decay and neglect
- Cold damp air suggested
- Uneasy tension

Composition:
- Medium shot, slight low angle
- Focus on the cabinet and shadows
- Depth of field on background
- Cinematic noir lighting

, masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
people, characters, person, human, figure, silhouette, face, body, bright lighting, clean corner, new furniture
```

---

### BG-03: 破败草屋·土炕区域 - 中景

**基于**: BG-01 大全景

**画面描述**:
土炕区域的中景。破旧的土炕靠墙，上面铺着漏棉花的破褥子，还有一个小木桌。月光从窗户斜照进来。

**场景延展说明**:
- 本场景基于 BG-01 延展
- 变化描述: 聚焦土炕区域，月光照射

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | BG-01_草屋内-大全景 | 确保空间一致性 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Medium shot of kang bed platform area in dilapidated cottage,
Based on the room panorama, focusing on the sleeping area,

Kang bed area elements:
- Traditional earthen kang platform against wall
- Worn-out cotton quilt with stuffing leaking out
- Tears and patches visible on the quilt fabric
- Small wooden table on the kang surface
- Simple pillow made of rough fabric
- Wall behind showing cracks and faded color
- Window visible at edge of frame with torn paper

Lighting:
- Pale cold moonlight streaming through window
- Creating diagonal light beam across the kang
- Soft shadows from window frame
- Warm candlelight from distant lamp creating color contrast
- Peaceful yet melancholic atmosphere

Atmosphere:
- Sense of poverty and hardship
- Quiet and still
- Cold winter night feeling
- Desolate but dignified

Composition:
- Medium shot, eye-level
- Kang platform centered
- Moonlight as visual focal point
- Depth of field on background

, masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
people, characters, person, human, figure, silhouette, face, body, modern bed, mattress, bright lighting, clean bedding
```

---

## 第三层：特写/细节（基于中景延展）

---

### BG-04: 破败草屋·窗户光效 - 特写

**基于**: BG-03 土炕区域

**画面描述**:
窗户的特写。破洞的窗纸，月光穿过形成光束。可以看见窗外的夜空和树影。

**场景延展说明**:
- 本场景基于 BG-03 延展
- 变化描述: 聚焦窗户细节，强调光束效果

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | BG-01_草屋内-大全景 | 空间参考 |
| 参考图2 | BG-03_土炕区域 | 细节延展参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Close-up shot of window with torn paper in ancient cottage,
Based on the kang bed area scene,

Window details:
- Traditional wooden window frame
- White paper lining with multiple tears and holes
- Moonlight streaming through holes creating light beams
- Dust particles visible floating in the light beams
- Tree branch silhouette visible through paper
- Window lattice pattern partially broken

Lighting:
- Cold pale moonlight as main light source
- Volumetric light beams cutting through darkness
- Dramatic chiaroscuro contrast
- Dust motes catching the light
- Ethereal and atmospheric

Atmosphere:
- Poetic and melancholic
- Sense of cold night outside
- Fragile beauty in decay
- Quiet stillness

Composition:
- Close-up shot, slight angle
- Window centered in frame
- Light beams as compositional element
- Shallow depth of field

, masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
people, characters, person, human, figure, silhouette, face, body, glass window, intact paper, daytime, bright lighting
```

---

### BG-05: 破败草屋·青灯特写 - 特写

**基于**: BG-02 角落阴影

**画面描述**:
青灯的特写。昏黄的火焰跳动，油灯的陶制灯身，灯光在墙上投下摇曳的影子。

**场景延展说明**:
- 本场景基于 BG-02 延展
- 变化描述: 聚焦青灯细节，强调火焰动态

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | BG-01_草屋内-大全景 | 空间参考 |
| 参考图2 | BG-02_角落阴影 | 细节延展参考 |

**提示词**:
```
3D动画渲染, Unreal Engine 5质感, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Close-up shot of traditional Chinese oil lamp (qingdeng),
Based on the dark corner scene,

Lamp details:
- Clay or ceramic oil lamp with simple elegant shape
- Small flame flickering and dancing
- Warm yellow-orange light emanating
- Oil visible in lamp bowl
- Simple wick visible
- Lamp sitting on worn wooden surface

Lighting effects:
- Warm golden glow from the flame
- Dynamic shadows dancing on nearby wall
- Flickering light creating atmospheric movement
- Bokeh effect from flame in background
- Contrast between warm light and surrounding darkness

Atmosphere:
- Intimate and focused
- Sense of fragile light in darkness
- Quiet and contemplative
- Traditional and timeless

Composition:
- Close-up shot, eye-level with lamp
- Flame as focal point
- Dark background with hint of wall texture
- Shallow depth of field

, masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, elegant composition, Unreal Engine 5 render, Octane Render, 3D animation style,
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look,
people, characters, person, human, figure, silhouette, face, body, electric light, light bulb, modern lamp, bright lighting
```

---

## 背景图总表

| 编号 | 场景名 | 层级 | 时间 | 主要光源 | 参考图来源 |
|------|--------|------|------|----------|------------|
| BG-01 | 草屋内-大全景 | 大全景 | 深夜 | 青灯+月光 | 场景参考（首次建立） |
| BG-02 | 草屋内-角落阴影 | 中景 | 深夜 | 微弱青灯 | BG-01 |
| BG-03 | 草屋内-土炕区域 | 中景 | 深夜 | 月光 | BG-01 |
| BG-04 | 草屋内-窗户光效 | 特写 | 深夜 | 月光 | BG-01, BG-03 |
| BG-05 | 草屋内-青灯特写 | 特写 | 深夜 | 青灯 | BG-01, BG-02 |
| BG-06 | 草屋门口-月光下 | 大全景 | 深夜 | 月光 | 场景参考（首次建立） |

---

## 背景延展关系图

```
第1章背景延展链:

草屋内部:
场景参考 → BG-01(大全景) → BG-02(角落) → BG-05(青灯特写)
           ↑首次建立      └── 基于BG-01延展 ──→
                         └→ BG-03(土炕) → BG-04(窗户特写)
                             └── 基于BG-01延展 ──→

草屋门口:
场景参考 → BG-06(门口大全景)
           ↑首次建立
```

---

## 与原文场景描述对应说明

| 原文描述 | 背景图编号 | 场景元素 |
|----------|------------|----------|
| "伏在阴冷的地面上，昏暗的室内只燃一盏青灯" | BG-01 | 泥土地面、青灯 |
| "视线并不明朗，在她的对面，依稀可以望见一个男人坐在一团阴翳之中" | BG-02 | 阴暗角落 |
| "清白的月辉穿过破了洞的窗纸，泻在他英挺的脸上" | BG-04 | 破洞窗纸、月光 |
| "他坐在一把破败的轮椅之上，满地碎瓷铺在他的脚边" | BG-01 | 碎瓷片、地面 |
| "残羹也渐染了他乌黑的靴子" | BG-01 | 残羹、地面 |
| "长剑...刺入她身后的木柱之上" | BG-01 | 木柱 |

---

## 场景完整性检查

**检查清单**:
- [x] 所有分镜中需要的场景元素都已包含
- [x] 光影方向在所有背景图中保持一致
- [x] 时间和天气设定连贯（都是深夜、寒冬）
- [x] 色彩基调一致（青灰、暗褐、昏黄）
- [x] 负向提示词排除了所有人物元素
- [x] 大全景已先生成
- [x] 中景和特写都上传了大全景作为参考

---

*由 AI场景搭建师 生成*
