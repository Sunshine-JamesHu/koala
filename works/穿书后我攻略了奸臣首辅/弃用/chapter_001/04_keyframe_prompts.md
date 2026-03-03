# 图片生成提示词 - 第1章 你自尽吧

> **使用说明**:
> - 将"提示词"内容直接复制到 Nano Banana Pro
> - 负向提示词用于避免常见问题
> - 图片比例根据需要调整 --ar 参数
> - **重要**: 按"需要上传的图片"顺序先上传参考图

---

## 生成顺序指南

**推荐生成顺序**:
1. 先生成角色表情参考卡（确保角色一致性）
2. 再生成场景背景参考图
3. 最后生成关键帧（上传表情卡和背景图作为参考）

---

## 角色表情参考卡

### 辛月影（女主）- 基础表情

**角色核心描述**（所有表情共用）:
```
Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes, long thick eyelashes,
delicate oval face, slightly upturned nose, fair porcelain skin,
petite and slender body,
wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color,
3D animation render, Chinese Donghua Style, ancient Chinese background
```

#### 表情卡生成提示词（5合1）

```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old female, two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair, beautiful almond-shaped eyes, long thick eyelashes, delicate oval face, slightly upturned nose, fair porcelain skin, petite and slender body, wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color,

| 困惑迷茫 | 刚醒来迷迷糊糊，眼神迷茫，微微皱眉，嘴唇微张 | confused, dazed, blinking slowly, slight frown, lips slightly parted |
| 惊恐万状 | 瞪大杏眼，面色苍白，嘴巴张大，浑身颤抖 | terrified, wide-eyed, pale face, mouth agape, trembling |
| 强颜欢笑 | 勉强挤出笑容，眼神慌张，嘴角僵硬 | forced smile, nervous eyes, stiff smile corners |
| 绝望无助 | 垂下眼帘，嘴角下垂，神情绝望，肩膀塌陷 | hopeless, downcast eyes, despondent expression, slumped shoulders |
| 诚恳表演 | 双手合十，表情诚恳，眼神真挚，微微仰头 | sincere, hands clasped together, pleading eyes, slightly looking up |

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style

按两行生成，第一行三个表情，第二行两个表情，只生一张 3*2 的面部表情图片
```

---

### 沈清起（男主）- 基础表情

**角色核心描述**（所有表情共用）:
```
Shen Qingqi, 25 years old male,
long black hair tied back in ancient Chinese style,
narrow phoenix eyes, thin lips, pale almost bloodless skin,
handsome and refined face with sharp defined features,
tall and slender body, sitting in worn wooden wheelchair,
wearing dark blue-black ancient Chinese scholar robe,
cold and gloomy aura,
3D animation render, Chinese Donghua Style, ancient Chinese background
```

#### 表情卡生成提示词（5合1）

```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Shen Qingqi, 25 years old male, long black hair tied back in ancient Chinese style, narrow phoenix eyes, thin lips, pale almost bloodless skin, handsome and refined face with sharp defined features, tall and slender body, sitting in worn wooden wheelchair, wearing dark blue-black ancient Chinese scholar robe, cold and gloomy aura,

| 冷漠无情 | 面无表情，眼神冰冷，目空一切，薄唇紧抿 | cold indifferent, emotionless, icy gaze, thin lips pressed |
| 阴鸷危险 | 眯起凤眼，眼神阴沉，杀意凛然，令人胆寒 | gloomy and sinister, menacing gaze, murderous intent, intimidating |
| 戏谑嘲弄 | 嘴角微扬，似笑非笑，眼神玩味，略带讥讽 | mocking smile, sarcastic expression, playful eyes, slightly mocking |
| 病态微笑 | 苍白脸上浮现诡异笑意，令人不寒而栗 | eerie smile, unsettling grin, pale sickly face, chilling |
| 淡漠审判 | 眼神平静却充满压迫感，居高临下 | indifferent judgment, calm but oppressive gaze, looking down |

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style

按两行生成，第一行三个表情，第二行两个表情，只生一张 3*2 的面部表情图片
```

---

### 霍齐（配角）- 基础表情

**角色核心描述**（所有表情共用）:
```
Huo Qi, 28 years old male,
full beard, round bull-like eyes,
bronze skin weathered from outdoor labor,
burly and muscular body, tall and strong frame,
wearing coarse cloth ancient Chinese laborer clothes, brown and earth tones,
3D animation render, Chinese Donghua Style, ancient Chinese background
```

#### 表情卡生成提示词（3合1）

```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Huo Qi, 28 years old male, full beard, round bull-like eyes, bronze skin weathered from outdoor labor, burly and muscular body, tall and strong frame, wearing coarse cloth ancient Chinese laborer clothes, brown and earth tones,

| 愤怒质问 | 圆眼怒瞪，络腮胡颤动，眉头紧锁，怒火中烧 | angry, fierce round eyes, beard trembling, furrowed brows, furious |
| 鄙视厌恶 | 眼神轻蔑，嘴角下撇，满脸不屑 | disdainful, contemptuous eyes, mouth corners down, disgusted |
| 警惕戒备 | 眼神锐利，身体紧绷，随时准备行动 | vigilant, sharp eyes, tense posture, ready to act |

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style

按一行生成，三个表情，只生一张 1*3 的面部表情图片
```

---

## 场景背景参考

### 场景 01: 破败草屋·卧房全景

**画面描述**:
昏暗的破败草屋卧房全景，深夜时分。唯一一盏青灯在角落摇曳，月光穿过破窗纸形成体积光束。泥土地面散落碎瓷片，中央有一把破旧木制轮椅，靠墙是简陋土炕。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese dilapidated cottage bedroom interior, poverty-stricken rural home,
late night scene, cold winter night,

single flickering blue oil lamp in corner, casting dancing shadows on mud walls,
cold pale moonlight streaming through holes in torn window paper, creating eerie volumetric light beams cutting through darkness,

mud floor covered with shattered porcelain pieces and spilled food remnants,
old worn wooden wheelchair sitting in center of room, broken and decrepit,
traditional kang bed platform against back wall with thin worn bedding,
small wooden table, simple wooden cabinet in corner,

moldy spotted earthen walls, thatched roof with gaps,
broken wooden window frame with torn paper,

dramatic chiaroscuro lighting, soft flickering shadows from candle,
volumetric moonlight beams, dust motes floating visible in light, atmospheric depth,

color palette: cold blue-grey dominant, warm yellow candlelight accent, pale moonlight highlights,
oppressive and eerie atmosphere, suffocating sense of poverty and desperation,

wide establishing shot, eye-level angle, depth of field blur on background,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, Octane Render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
people, characters, faces, figures, text, watermark, signature,
low quality, worst quality, blurry, distorted, deformed,
modern elements, western style, electric lights, cars, buildings, concrete,
2d flat, sketch, line art, photo realistic, plastic look,
bright colors, warm cozy atmosphere, clean tidy room, new furniture
```

---

### 场景 02: 破败草屋·卧房（沈清起视角）

**画面描述**:
卧房视角，聚焦于沈清起所在位置。月光和青灯交织照亮区域，周围是黑暗的阴影。碎瓷散落，轮椅在画面中心偏后位置。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

ancient Chinese dilapidated cottage bedroom interior focusing on center area,
late night, dramatic lighting,

moonlight and candlelight interweaving, creating dramatic light and shadow contrast,
scattered broken porcelain pieces on mud floor around center,
worn wooden wheelchair positioned in room center, old and decrepit,
traditional kang bed visible against wall in background,

atmospheric depth, dust particles in light beams,
cold blue-grey and warm yellow color contrast,
oppressive and mysterious atmosphere,

medium shot, eye-level angle, focus on wheelchair area,

masterpiece, best quality, 8k resolution, highly detailed environment, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
people, characters, faces, figures, text, watermark,
low quality, worst quality, blurry, distorted
```

---

## 角色关键帧

### 辛月影 系列提示词

#### 镜头 1-1-1 - 穿书苏醒（远景·隐匿）

**图片用途**: 关键帧 - 开场镜头

**画面描述**:
俯视远景。辛月影伏在阴冷的泥土地面上，刚刚苏醒。青灯在角落摇曳，月光光束指向她。她身着破旧粗布衣裳，一动不动。对面角落有一个模糊的剪影（沈清起隐匿在黑暗中）。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes closed, long thick eyelashes,
delicate oval face, fair porcelain skin,
petite and slender body,
wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color, clothes disheveled,

lying prone on cold mud floor, body limp, just waking up,
eyes closed, slight frown on face, unconscious pose,

in dilapidated ancient Chinese cottage bedroom, poverty-stricken rural home,
late night, single flickering blue oil lamp in corner,
cold pale moonlight beam streaming through torn window paper, pointing toward her,
scattered broken porcelain pieces on floor around her,

in the far dark corner, a silhouette of a seated figure barely visible in shadows,
mysterious presence in the darkness, ominous atmosphere,

dramatic overhead high-angle shot, wide establishing view,
cold blue-grey and warm yellow lighting contrast,
dust particles floating in moonlight beam, atmospheric depth,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, Octane Render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad hands, missing fingers,
extra limbs, disconnected limbs,
smiling, happy expression, clean clothes, bright colors,
wheelchair visible, clear figure in corner
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 辛月影-表情参考卡 | 角色一致性参考 |
| 参考图2 | 破败草屋-卧房全景 | 场景背景参考 |

**参考信息**:
- 场景: 破败草屋·卧房
- 情绪: 困惑、压抑
- 光源: 青灯（角落）+ 月光（侧面）

---

#### 镜头 1-1-2 - 以为是梦

**图片用途**: 关键帧 - 辛月影翻身

**画面描述**:
中景。辛月影翻身侧卧，一手支着脸颊，姿态慵懒。青灯从侧面照亮她困惑却带着笑意的脸。她望向对面阴影中轮椅的剪影，以为自己在做梦。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes with confused but amused look, long thick eyelashes,
delicate oval face, slightly upturned nose, fair porcelain skin,
soft smile on lips, relaxed expression,
petite and slender body,
wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color,

lying on side on cold mud floor, one hand propping up cheek,
lazy relaxed pose, looking toward shadows with curious amusement,
as if watching an interesting dream,

in dilapidated ancient Chinese cottage bedroom,
late night, warm yellow candlelight from side illuminating her face,
cold moonlight beam in background,

in the opposite dark corner, a silhouette of a seated figure barely visible in shadows,
faint outline in darkness, mysterious presence,

medium shot, eye-level angle, side lighting from candle,
warm candlelight on her face contrasting with cold blue background,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad hands, missing fingers,
scared expression, terrified, crying,
wheelchair clearly visible, clear figure in corner
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 辛月影-表情参考卡 | 角色一致性参考 |
| 参考图2 | 破败草屋-卧房全景 | 场景背景参考 |

**参考信息**:
- 场景: 破败草屋·卧房
- 情绪: 困惑、轻笑（以为在做梦）
- 光源: 青灯（侧面）

---

#### 镜头 1-2-2 - 穿书意识

**图片用途**: 关键帧 - 震惊表情

**画面描述**:
特写。辛月影听到"辛四娘"三字，瞳孔骤然收缩。表情从轻笑瞬间变为震惊和惊恐。背景虚化，青灯照亮她的脸。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes wide open in shock, pupils constricted, long thick eyelashes,
delicate oval face, slightly upturned nose, fair porcelain skin going pale,
expression changing from smile to shock and terror,
mouth slightly open, breath caught in throat,
petite and slender body,

frozen in shock, realization hitting her,
eyes wide with terror and disbelief,

in dilapidated ancient Chinese cottage bedroom,
late night, warm yellow candlelight illuminating her face,
background heavily blurred and dark,

extreme close-up on face, focusing on eyes and expression,
dramatic lighting highlighting her shocked face,
sharp focus on face, bokeh background,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad face,
smiling, happy, calm expression,
detailed background, many objects visible
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 辛月影-表情参考卡 | 角色一致性参考 |

**参考信息**:
- 场景: 破败草屋·卧房（背景虚化）
- 情绪: 震惊→惊恐
- 光源: 青灯（正面）

---

#### 镜头 1-5-2 - 撞上霍齐

**图片用途**: 关键帧 - 绝望时刻

**画面描述**:
仰视中景。辛月影冲出门口，撞上霍齐。从她的视角仰视霍齐——络腮胡、圆眼、古铜色皮肤，月光照在他魁梧的身躯上，挡住了所有去路。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes looking up in terror, long thick eyelashes,
delicate oval face, fair porcelain skin pale with fear,
expression of despair and hopelessness,
petite and slender body,
wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color,

just crashed into someone, looking up in terror and despair,
feet barely visible at bottom of frame,
small frame emphasizing vulnerability,

viewing from low angle looking up at imposing figure,
Huo Qi, 28 years old male, full beard, round angry bull-like eyes,
bronze skin weathered from outdoor labor,
burly and muscular body, tall and strong frame, blocking the doorway,
wearing coarse cloth ancient Chinese laborer clothes, brown and earth tones,
standing in doorway like a guard dog, arms crossed, looking down with contempt,

outside dilapidated cottage at night,
cold moonlight from behind creating rim lighting on Huo Qi's silhouette,
ominous and oppressive atmosphere,

medium shot, low angle looking up,
dramatic contrast between tiny Xin Yueying and massive Huo Qi,
moonlight silhouette effect, intimidating perspective,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad hands,
happy expression, calm scene,
bright lighting, indoor scene
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 辛月影-表情参考卡 | 角色一致性参考 |
| 参考图2 | 霍齐-表情参考卡 | 配角一致性参考 |

**参考信息**:
- 场景: 门外
- 情绪: 绝望、恐惧
- 光源: 月光（背后轮廓光）

---

#### 镜头 1-7-1 - 谎言表演

**图片用途**: 关键帧 - 演技全开

**画面描述**:
中景。辛月影开始她的表演。她"啪"地一声合掌，瞪大眼睛，装作震惊的样子。她的表演浮夸但全力以赴。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Xin Yueying, 20 years old female,
two spiral hair buns on sides of head, traditional Chinese shuangluoji hairstyle, black hair,
beautiful almond-shaped eyes wide with exaggerated shock, long thick eyelashes,
delicate oval face, fair porcelain skin,
dramatic exaggerated expression, eyes wide, mouth open in fake surprise,
petite and slender body,
wearing worn coarse cloth ancient Chinese peasant dress with patches, drab gray-brown color,

hands clasped together dramatically in front of chest,
acting performance, exaggerated gestures,
body language showing feigned innocence and shock,

in dilapidated ancient Chinese cottage bedroom,
late night, warm yellow candlelight and cold moonlight,
scattered broken porcelain on floor,

medium shot, eye-level angle,
dramatic lighting highlighting her theatrical performance,
contrasting emotions of performance versus fear,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad hands, missing fingers,
genuine happy expression, relaxed pose,
bright cheerful atmosphere
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 辛月影-表情参考卡 | 角色一致性参考 |
| 参考图2 | 破败草屋-卧房全景 | 场景背景参考 |

**参考信息**:
- 场景: 破败草屋·卧房
- 情绪: 假装震惊、表演中
- 光源: 青灯 + 月光

---

### 沈清起 系列提示词

#### 镜头 1-2-1 - 病娇亮相

**图片用途**: 关键帧 - 男主首次露脸

**画面描述**:
中景到近景。沈清起微微向前躬身，月光穿过破窗纸形成光束，照亮他的脸。狭长的凤眼淬着寒意，薄唇衔着混沌的笑意，苍白无血色的脸庞在月光下泛着森寒的光。他坐在破败的轮椅上，脚边散落碎瓷片。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Shen Qingqi, 25 years old male,
long black hair tied back in ancient Chinese style,
narrow phoenix eyes with cold penetrating gaze, slight sinister glint in eyes,
thin lips curving into ambiguous unsettling smile,
pale almost bloodless skin, sickly beautiful appearance, moonlight making skin appear ethereal and cold,
handsome and refined face with sharp defined features, chiseled jawline,
tall and slender body type,
sitting in worn wooden wheelchair, broken and decrepit wooden construction,
wearing dark blue-black ancient Chinese scholar robe, dark colors absorbing light,

leaning slightly forward, one hand holding a piece of broken porcelain, fingers elegant,
scattered broken porcelain pieces around wheelchair feet,
dark gloomy intimidating presence,

in dilapidated ancient Chinese cottage bedroom,
late night, dramatic lighting,
cold pale moonlight beam streaming through holes in torn window paper, illuminating his face like spotlight,
single flickering blue oil lamp in corner casting dancing shadows,

dramatic chiaroscuro lighting, moonlight as key light creating cold ethereal glow,
sharp contrast between lit face and dark surroundings,

medium to close-up shot, eye-level angle,
focus on his face and upper body,
cold blue moonlight on face, warm candlelight accent,
mysterious and dangerous atmosphere,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, Octane Render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad hands,
warm friendly expression, smiling happily, bright colors,
healthy skin tone, rosy cheeks,
standing, walking
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 沈清起-表情参考卡 | 角色一致性参考 |
| 参考图2 | 破败草屋-卧房（沈清起视角） | 场景背景参考 |

**参考信息**:
- 场景: 破败草屋·卧房
- 情绪: 阴鸷、戏谑、危险
- 光源: 月光（正面主光）+ 青灯（侧面辅助光）

---

#### 镜头 1-6-1 - 碎瓷流血

**图片用途**: 关键帧 - 危险优雅的细节

**画面描述**:
特写。沈清起的手部特写。指骨分明的手指捏着一枚碎瓷，指尖轻轻摩挲。碎瓷的锋利边缘割破了他的掌心，鲜血从指缝间涔涔流出，滴落在地上。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

extreme close-up of male hand,
Shen Qingqi's hand, slender elegant fingers, prominent knuckles,
fair pale skin, veins visible on back of hand,
holding a piece of broken porcelain, sharp jagged edges,
fingertips gently tracing the sharp edge,
blood seeping from palm where porcelain cut the skin,
crimson red blood drops trickling between fingers,
falling toward ground,

worn dark blue-black ancient Chinese robe sleeve visible at wrist,

dim lighting from flickering blue oil lamp,
dramatic chiaroscuro, deep shadows,
blood drops catching the dim light,

extreme close-up shot, shallow depth of field,
focus on hand and blood drops,
artistic and slightly unsettling composition,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy, bad hands, extra fingers, missing fingers,
bright lighting, cheerful atmosphere,
female hand, rough skin
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 沈清起-表情参考卡 | 角色手部风格参考 |

**参考信息**:
- 场景: 破败草屋·卧房（特写背景虚化）
- 情绪: 危险、优雅、压抑
- 光源: 青灯（侧面）

---

#### 镜头 1-7-3 - 阴鸷冷笑（结尾悬念）

**图片用途**: 关键帧 - 章节结尾

**画面描述**:
特写。沈清起凤眼的特写。他的笑声戛然而止，眼神变得阴鸷而危险。薄唇轻启，说出让人毛骨悚然的话。画面逐渐变暗，留下悬念。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Shen Qingqi, 25 years old male,
extreme close-up on face focusing on eyes,
narrow phoenix eyes with cold sinister glint, menacing and dangerous gaze,
thin lips slightly parted in chilling smile,
pale almost bloodless skin, cold ethereal appearance,
handsome features cast in ominous shadow,

expression of cold amusement mixed with menace,
eyes gleaming with dark intent,
unsettling and intimidating presence,

in dilapidated ancient Chinese cottage bedroom,
late night, dramatic moody lighting,
cold moonlight from side creating sharp shadows on face,
warm candlelight accent flickering,

extreme close-up shot, shallow depth of field,
focus on eyes and mouth,
vignette effect darkening edges,
suspenseful and ominous atmosphere,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad face,
warm friendly expression, happy smile, bright eyes,
healthy skin tone,
wide shot, full body
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 沈清起-表情参考卡 | 角色一致性参考 |

**参考信息**:
- 场景: 破败草屋·卧房（背景虚化）
- 情绪: 阴鸷、危险、悬念
- 光源: 月光 + 青灯（侧面）

---

### 霍齐 系列提示词

#### 镜头 1-5-2 - 守门拦人（与辛月影同镜）

**图片用途**: 关键帧 - 霍齐登场

**画面描述**:
仰视中景。霍齐站在门口，如同看门狗般守着。月光照在他魁梧的身躯上，形成压迫性的剪影。络腮胡、圆眼、古铜色皮肤，充满力量感。

**提示词**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style, 古风唯美, 精致细腻, 中国古代背景,

Huo Qi, 28 years old male,
full beard, round bull-like eyes glaring with anger,
bronze skin weathered from outdoor labor,
square rugged face,
burly and muscular body, tall and strong frame,
broad shoulders, powerful build,
wearing coarse cloth ancient Chinese laborer clothes, brown and earth tones,
thick fabric short jacket and pants,

standing in cottage doorway like a guard dog,
arms at sides, fists clenched,
blocking the exit, imposing and threatening stance,
looking down with contempt and anger,

outside dilapidated cottage at night,
cold winter night, crescent moon in dark sky,
moonlight from behind creating dramatic rim lighting,
silhouette effect emphasizing his powerful build,

medium shot, low angle looking up at him,
emphasizing his intimidating size and presence,
oppressive and hopeless atmosphere,

masterpiece, best quality, 8k resolution, highly detailed, soft cinematic lighting, depth of field blur, Unreal Engine 5 render, 3D animation style
--ar 16:9
```

**负向提示词**:
```
low quality, worst quality, blurry, distorted, deformed,
bad anatomy,
friendly expression, smiling, relaxed pose,
bright lighting, indoor scene,
slim build, clean shaven
```

**需要上传的图片**（按顺序上传）:
| 顺序 | 图片名称 | 用途 |
|------|----------|------|
| 参考图1 | 霍齐-表情参考卡 | 角色一致性参考 |

**参考信息**:
- 场景: 门外
- 情绪: 愤怒、威胁、压迫
- 光源: 月光（背后轮廓光）

---

## 图片清单

| 编号 | 类型 | 用途 | 对应镜头 | 状态 |
|------|------|------|----------|------|
| 001 | 表情卡 | 辛月影-5表情 | 全章参考 | 待生成 |
| 002 | 表情卡 | 沈清起-5表情 | 全章参考 | 待生成 |
| 003 | 表情卡 | 霍齐-3表情 | 全章参考 | 待生成 |
| 004 | 场景 | 卧房全景 | 1-1-1等 | 待生成 |
| 005 | 场景 | 卧房（沈清起视角）| 1-2-1等 | 待生成 |
| 006 | 关键帧 | 辛月影-穿书苏醒 | 1-1-1 | 待生成 |
| 007 | 关键帧 | 辛月影-以为是梦 | 1-1-2 | 待生成 |
| 008 | 关键帧 | 辛月影-穿书意识 | 1-2-2 | 待生成 |
| 009 | 关键帧 | 辛月影-撞上霍齐 | 1-5-2 | 待生成 |
| 010 | 关键帧 | 辛月影-谎言表演 | 1-7-1 | 待生成 |
| 011 | 关键帧 | 沈清起-病娇亮相 | 1-2-1 | 待生成 |
| 012 | 关键帧 | 沈清起-碎瓷流血 | 1-6-1 | 待生成 |
| 013 | 关键帧 | 沈清起-阴鸷冷笑 | 1-7-3 | 待生成 |
| 014 | 关键帧 | 霍齐-守门拦人 | 1-5-2 | 待生成 |

---

## 关键帧与原文对应说明

| 关键帧 | 原文段落 | 视觉化决策 |
|--------|----------|------------|
| 1-1-1 穿书苏醒 | 第5-7行 | 俯视远景，辛月影伏在地上，对面是隐匿的剪影 |
| 1-1-2 以为是梦 | 第11-19行 | 慵懒支颊，以为在做梦的反差感 |
| 1-2-1 病娇亮相 | 第20-28行 | 月光+青灯照亮沈清起病态美颜 |
| 1-2-2 穿书意识 | 第35-39行 | 瞳孔收缩的震惊表情 |
| 1-5-2 撞上霍齐 | 第115-127行 | 仰视霍齐的压迫感 |
| 1-6-1 碎瓷流血 | 第133-135行 | 危险优雅的手部特写 |
| 1-7-1 谎言表演 | 第141-151行 | 夸张的合掌表演动作 |
| 1-7-3 阴鸷冷笑 | 第155-157行 | 悬念结尾的阴鸷眼神 |

---

## 服装/表情变化说明

### 辛月影
- **服装**: 全章保持同一套破旧粗布衣裳，无变化
- **表情变化**: 困惑(以为梦) → 轻笑 → 震惊 → 惊恐 → 绝望 → 假装震惊(表演)
- **状态**: 从以为是梦的轻松，到意识到穿书的惊恐

### 沈清起
- **服装**: 全章保持同一套深色古装长袍，无变化
- **表情变化**: 隐匿 → 冷漠 → 戏谑 → 阴鸷
- **状态**: 始终在轮椅上，从隐藏面容到逐渐显露危险气质

### 霍齐
- **服装**: 粗布短打，无变化
- **表情变化**: 愤怒、鄙视
- **状态**: 守在门外，阻挡辛月影逃跑

---

*由 AI原画师 生成*
