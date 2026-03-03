# 背景图片提示词 - 第1章 你自尽吧

> **使用说明**:
> - 将"提示词"内容直接复制到 Nano Banana Pro
> - 负向提示词用于避免常见问题
> - **背景图不含任何角色**，所有角色在关键帧中处理
> - **生成顺序**: 大全景 → 中景 → 特写

---

## 场景层级规划

### 生成顺序（重要）⭐
1. **BG-01**: 草屋内-大全景（主场景，建立空间基础）
2. **BG-02**: 草屋内-角落阴影（中景，基于大全景）
3. **BG-03**: 草屋内-土炕区域（中景，基于大全景）
4. **BG-04**: 草屋内-窗户光效（特写）
5. **BG-05**: 草屋内-青灯特写（特写）
6. **BG-06**: 草屋门口-月光下（大全景）

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

**负向提示词（基础）**:
```
low quality, worst quality, blurry, distorted, deformed, ugly, bad anatomy, bad proportions, modern elements, western style, 2d flat, sketch, line art, text, watermark, signature, photo realistic, plastic look, people, characters, person, human, figure, silhouette, face, body
```

---

## 第一层：大全景（必须首先生成）⭐

---

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
