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
