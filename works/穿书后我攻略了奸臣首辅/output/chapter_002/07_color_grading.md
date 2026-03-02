# 调色指南 - 第2章 拿命赌明天

> **使用说明**:
> - 本文件包含第2章所有场景的调色方案
> - 调色关键词可直接用于后期调色工具
> - 按"场景"和"镜头"依次实施

---

## 章节调色总览

### 整体色彩风格

| 属性 | 设定 | 说明 |
|------|------|------|
| 色彩基调 | 冷色偏暖点缀 | 深夜场景以冷色为主，青灯提供暖色点缀 |
| 饱和度 | 低-中 | 压抑氛围，降低整体饱和度 |
| 对比度 | 中-高 | 强调明暗对比，营造紧张感 |
| 参考风格 | 《魔道祖师》夜景 + 《天官赐福》情绪戏 |

### 情绪-色彩对应图

```
情绪强度
高 ┤        ╭──╮              ╭──────╮      ╭────╮
   │       ╱    ╲            ╱        ╲    ╱      ╲
中 ┤ ╭───╮╱      ╲    ╭───╮╱          ╲  ╱        ╲
   │╱     ╲        ╲  ╱    ╲            ╲╱          ╲
低 ┤       ╲        ╲╱      ╲            ╲          ╲
   └────────────────────────────────────────────────→ 镜头进度
   场1        场2        场3          场4
   谎言自证   发现自残   包扎伤口     遭遇老王

色调变化: 冷暖交织 → 冷色为主 → 暖色点缀 → 冷色悬念
```

### 本章核心色彩

| 优先级 | 色彩元素 | 出现场景 | 情绪作用 |
|--------|----------|----------|----------|
| ⭐⭐⭐ | 猩红血滴 | 场景2 | 视觉冲击，悲凉意象 |
| ⭐⭐⭐ | 冷蓝月光 | 场景1-4 | 冷漠、威胁、悬念 |
| ⭐⭐ | 暖黄青灯 | 场景1-3 | 微弱希望、温暖对比 |
| ⭐⭐ | 泪滴晶光 | 场景1、3 | 情感强化 |
| ⭐ | 铁锨寒光 | 场景4 | 威胁暗示 |

---

## 场景 1：谎言自证

### 基础调色

| 属性 | 设定 | 具体参数 |
|------|------|----------|
| 色温 | 冷暖混合 | 主体冷色 6500K + 青灯暖光 3200K |
| 曝光 | 欠曝 | -0.5EV（营造深夜压抑感） |
| 阴影 | 偏青灰 | 色相 190°，饱和度 15% |
| 高光 | 偏暖黄 | 色相 45°，饱和度 20% |

### 色彩倾向

| 类型 | 颜色 | HEX | 用途 |
|------|------|-----|------|
| 主色调 | 月白 | #D4E5F7 | 月光环境色 |
| 辅助色 | 昏黄 | #C4A35A | 青灯光源 |
| 强调色 | 泪晶 | #E8F4FF | 泪滴高光 |

### 场景1调色关键词

```
cold blue moonlight with warm candlelight accents,
low key lighting, moody atmosphere,
blue-grey shadows, warm yellow highlights,
medium-low saturation,
medium-high contrast,
dramatic chiaroscuro lighting,
Chinese period drama night scene color grading,
cinematic look
```

---

### 镜头 2-1-1：辛月影声泪俱下

**调色重点**: 暖冷对比，泪滴高光

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 5500K | 整体偏冷 |
| 色调 | +5（偏洋红） | 强化皮肤苍白 |
| 曝光 | -0.3EV | 深夜氛围 |
| 阴影 | +10 | 提亮暗部细节 |
| 高光 | -15 | 保留青灯细节 |
| 白色色阶 | -10 | 柔和高光 |

**HSL 调整**:
| 颜色 | 色相 | 饱和度 | 明度 |
|------|------|--------|------|
| 橙色（皮肤） | 0 | -10 | -5 |
| 黄色（青灯） | +5 | +15 | 0 |
| 蓝色（月光） | -5 | +10 | -10 |
| 紫色（阴影） | 0 | +10 | -5 |

**调色预设描述**:
```
Scene 1-1 Color Grade:
- Base: Cold moonlight blue (#D4E5F7) as ambient
- Key Light: Warm candlelight (#C4A35A) from side
- Shadow Tint: Subtle blue-grey
- Skin Tone: Desaturated, pale complexion
- Tear Highlights: Crystalline white with warm catch light
- Mood: Desperate pleading, tension

LUT Reference: Blue Moonlight + Candle Warmth blend
```

---

### 镜头 2-1-2：辛月影恳切的脸

**调色重点**: 肤色情绪，泪光晶莹

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 5800K | 微暖（青灯近景） |
| 色调 | +3 | 轻微洋红 |
| 曝光 | -0.2EV | 深夜 |
| 阴影 | +15 | 提亮面部阴影 |
| 清晰度 | +10 | 强化泪滴质感 |

**调色预设描述**:
```
Scene 1-2 Color Grade (Close-up):
- Focus on face and tears
- Skin: Pale with warm candlelight glow
- Tears: Crystal clear, catching warm light
- Background: Soft bokeh with warm orbs
- Mood: Sincere pleading, emotional intensity
```

---

### 镜头 2-1-3：沈清起眼眸微颤

**调色重点**: 冰封质感，冷暖分割

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 6200K | 冷色主导 |
| 色调 | 0 | 中性 |
| 曝光 | -0.5EV | 阴暗压抑 |
| 对比度 | +15 | 强化明暗 |
| 阴影 | -20 | 加深暗部 |

**分割调光**:
| 区域 | 色调 | 说明 |
|------|------|------|
| 亮面 | 暖黄（青灯） | 微弱希望 |
| 暗面 | 冷蓝（月光） | 冰封冷酷 |

**调色预设描述**:
```
Scene 1-3 Color Grade (Eye Close-up):
- Split lighting effect
- Warm side: Faint candlelight yellow
- Cold side: Ice blue moonlight
- Eye reflection: Subtle warm catch light
- Mood: Hidden turmoil beneath frozen surface
- Ice metaphor: Cold, calculated, dangerous
```

---

### 镜头 2-1-4：霍齐夺弓冲出

**调色重点**: 动态光影，室内外反差

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 渐变 | 室内暖→室外冷 |
| 曝光 | +0.3EV | 动作场面 |
| 动态模糊 | 保留 | 运动感 |

**调色预设描述**:
```
Scene 1-4 Color Grade (Action):
- Indoor: Warm candlelight tones
- Outdoor: Cold moonlight blue
- Motion blur preserves color temperature gradient
- Mood: Urgent, determined action
```

---

## 场景 2：收拾碎瓷与发现自残

### 基础调色

| 属性 | 设定 | 具体参数 |
|------|------|----------|
| 色温 | 冷色为主 | 6800K（月光主导） |
| 曝光 | 欠曝 | -0.7EV（青灯渐弱） |
| 阴影 | 偏冷蓝 | 色相 210°，饱和度 20% |
| 高光 | 微暖 | 色相 50°，饱和度 10% |

### 色彩倾向

| 类型 | 颜色 | HEX | 用途 |
|------|------|-----|------|
| 主色调 | 暗青灰 | #8B9DA8 | 破败草屋 |
| 辅助色 | 暗褐 | #5C4033 | 地面泥色 |
| 强调色 | 猩红 | #8B0000 | 血滴 ⭐ |

### 场景2调色关键词

```
cold moonlight dominating dying candlelight,
very low key lighting, tense atmosphere,
blue-grey tones with brown earth colors,
crimson red accent (blood),
low saturation except for blood,
high contrast for dramatic effect,
melancholic and shocking mood,
cinematic tragedy color grading
```

---

### 镜头 2-2-1：辛月影蹲下收拾

**调色重点**: 灰暗压抑，内心思忖

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 6800K | 偏冷 |
| 曝光 | -0.5EV | 青灯渐弱 |
| 饱和度 | -15 | 压抑氛围 |
| 阴影 | -10 | 加深暗部 |

**调色预设描述**:
```
Scene 2-1 Color Grade:
- Dim dying candlelight
- Cold blue ambient from moonlight
- Desaturated environment
- Focus on character's contemplative expression
- Mood: Quiet tension, calculating
```

---

### 镜头 2-2-2：沈清起发愣

**调色重点**: 瓷器质感，苍白美学

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 6500K | 冷色 |
| 曝光 | -0.3EV | 柔和 |
| 肤色饱和度 | -20 | 苍白如瓷 |
| 清晰度 | +5 | 瓷器质感 |

**调色预设描述**:
```
Scene 2-2 Color Grade (Porcelain Beauty):
- Skin: Extremely pale, almost translucent
- Texture: Porcelain-like sheen
- Lighting: Soft interplay of candle and moonlight
- Mood: Fragile beauty, lost in memory
- Color palette: Muted blues, pale skin tones
```

---

### 镜头 2-2-3：血滴落地 ⭐⭐⭐

**调色重点**: 猩红强调，凄美意象

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 6500K | 冷背景 |
| 曝光 | -0.5EV | 昏暗环境 |
| 对比度 | +25 | 血滴突出 |

**HSL 调整（重点）**:
| 颜色 | 色相 | 饱和度 | 明度 |
|------|------|--------|------|
| 红色（血滴） | +10 | +30 | +15 |
| 橙色 | 0 | -10 | -5 |
| 蓝色 | -5 | +10 | -10 |

**调色预设描述**:
```
Scene 2-3 Color Grade (Blood Drop - CORE VISUAL):
- Background: Dark brown earth, desaturated
- Blood drops: CRIMSON RED (#8B0000), highly saturated
- Translucent glow in dim light
- Contrast: Blood stands out dramatically
- Mood: Beautiful tragedy, fallen flower imagery
- Slow motion effect enhances color impact

Technical Notes:
- Blood red saturation: +30%
- Blood red luminosity: +15%
- Background desaturation: -25%
- Creates stark visual contrast
- Poetic tumi flower (荼蘼) imagery
```

---

### 镜头 2-2-4：沈清起眼中恨意

**调色重点**: 凤眼光芒，冷暖分割

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 分割 | 半冷半暖 |
| 曝光 | -0.5EV | 阴暗 |
| 对比度 | +20 | 强化情绪 |
| 血丝强化 | +15 | 眼部细节 |

**调色预设描述**:
```
Scene 2-4 Color Grade (Hatred):
- Split lighting: Warm/cold division
- Eyes: Bloodshot whites, intense gaze
- Shadows: Deep and cold
- Highlights: Warm but dim
- Mood: Seething hatred, deep sorrow
- Half light, half shadow = inner conflict
```

---

## 场景 3：包扎伤口与霍齐归来

### 基础调色

| 属性 | 设定 | 具体参数 |
|------|------|----------|
| 色温 | 中性偏暖 | 5500K（霍齐归来带来温度） |
| 曝光 | 欠曝渐恢复 | -0.3EV |
| 阴影 | 中性 | 无明显偏色 |
| 高光 | 暖色 | 色相 45° |

### 色彩倾向

| 类型 | 颜色 | HEX | 用途 |
|------|------|-----|------|
| 主色调 | 暖褐 | #6B4423 | 忠诚氛围 |
| 辅助色 | 丝白 | #F5F5F0 | 丝绦 |
| 强调色 | 泪光 | #FFF8E7 | 泪滴 |

### 场景3调色关键词

```
gradual warmth returning with Huo Qi's arrival,
candlelight as main source,
warm brown tones for loyal atmosphere,
white silk cord accent,
emotional tears glistening,
medium saturation,
moderate contrast,
touching and devoted mood
```

---

### 镜头 2-3-1：辛月影掰开手

**调色重点**: 手部特写，血迹对比

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 5800K | 微暖 |
| 曝光 | -0.2EV | 昏暗 |
| 手部肤色 | 偏冷 | 冰冷质感 |

**调色预设描述**:
```
Scene 3-1 Color Grade (Hands):
- Cold skin tone (blood loss implication)
- Crimson blood against pale skin
- Warm candlelight on hands
- Mood: Urgent concern, dramatic reveal
```

---

### 镜头 2-3-2：辛月影泪流满面

**调色重点**: 泪滴晶莹，情感高潮

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 5500K | 中性 |
| 曝光 | -0.2EV | 柔和 |
| 泪滴高光 | +20 | 晶莹效果 |

**调色预设描述**:
```
Scene 3-2 Color Grade (Tears):
- Tears: Crystal clear, catching candlelight
- Face: Warm candlelit glow
- Single tear track in sharp focus
- Mood: Performed grief, calculated emotion
- Pearlescent tear highlights
```

---

### 镜头 2-3-3：沈清起悲凉反问

**调色重点**: 明暗分割，诡异笑意

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 分割 | 半暖半冷 |
| 曝光 | -0.3EV | 阴暗 |
| 对比度 | +20 | 强化分割 |

**调色预设描述**:
```
Scene 3-3 Color Grade (Desolate Question):
- DRAMATIC SPLIT LIGHTING (核心光效)
- Half face: Warm candlelight
- Half face: Cold shadow
- Bloodshot eyes catching dim light
- Bitter smile in half-shadow
- Mood: "Who would feel pain for me?"
- Profound loneliness and despair
```

---

### 镜头 2-3-4：霍齐跪地包扎

**调色重点**: 忠诚温暖，丝绦光效

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 5200K | 暖色 |
| 曝光 | -0.2EV | 温馨 |
| 白色丝绦 | 暖调 | 烛光映照 |

**调色预设描述**:
```
Scene 3-4 Color Grade (Loyalty):
- Warm candlelight dominates
- White silk cord with warm glow
- Tears in Huo Qi's eyes glistening
- Mood: Touching loyalty, master-servant bond
- Warm brown tones throughout
```

---

### 镜头 2-3-5：外衫盖膝上

**调色重点**: 冷光回应，不确定氛围

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 6000K | 偏冷 |
| 曝光 | -0.3EV | 压抑 |
| 眼神寒光 | +15 | 冷酷 |

**调色预设描述**:
```
Scene 3-5 Color Grade:
- Coarse fabric texture in dim light
- Shen's cold gaze with moonlight reflection
- Mood: Uncertain truce, cold acceptance
- Tension beneath surface calm
```

---

## 场景 4：门外遭遇王屠户

### 基础调色

| 属性 | 设定 | 具体参数 |
|------|------|----------|
| 色温 | 冷色 | 7200K（月光主导） |
| 曝光 | 欠曝 | -0.5EV（深夜室外） |
| 阴影 | 偏冷蓝 | 色相 220°，饱和度 25% |
| 高光 | 银白 | 色相 200° |

### 色彩倾向

| 类型 | 颜色 | HEX | 用途 |
|------|------|-----|------|
| 主色调 | 月光蓝 | #A4C3D2 | 室外月光 |
| 辅助色 | 银白 | #C0C0C0 | 轮廓光 |
| 强调色 | 金属灰 | #71797E | 铁锨 |

### 场景4调色关键词

```
cold winter night moonlight,
high contrast silhouette effects,
silver rim lighting from moon,
menacing shadowy atmosphere,
blue-grey color palette,
cold metallic accents,
suspenseful and threatening mood,
cliffhanger color grading
```

---

### 镜头 2-4-1：辛月影跑出房门

**调色重点**: 动态模糊，冷暖过渡

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 渐变 | 室内暖→室外冷 |
| 曝光 | -0.3EV | 月光环境 |
| 轮廓光 | 银白 | 月光勾边 |

**调色预设描述**:
```
Scene 4-1 Color Grade (Escape):
- Indoor warm glow fading behind
- Outdoor cold moonlight
- Silver rim lighting on silhouette
- Motion blur with color temperature gradient
- Mood: Relief turning to fear
```

---

### 镜头 2-4-2：王屠户现身 ⭐⭐⭐

**调色重点**: 月光剪影，威胁氛围

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 7500K | 冷色 |
| 曝光 | -0.7EV | 剪影效果 |
| 轮廓光 | +30 | 月光勾边 |
| 对比度 | +25 | 强化剪影 |

**调色预设描述**:
```
Scene 4-2 Color Grade (Wang Tuhu - CORE VISUAL):
- DRAMATIC RIM LIGHTING from moon
- Menacing silhouette effect
- Backlit figure emerging from darkness
- Iron shovel with cold metallic glint
- Crescent moon in background
- Mood: Threatening, ominous presence
- Cold blue moonlight as key light from behind

Technical Notes:
- Light ratio: 1:8 (shadow:highlight)
- Color temperature: 4500K (cold moonlight)
- Rim light intensity: 60%
- Volumetric moon rays
```

---

### 镜头 2-4-3：铁锨特写

**调色重点**: 金属寒光，威胁暗示

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 7000K | 冷色 |
| 曝光 | -0.3EV | 月光 |
| 金属高光 | +20 | 寒光效果 |
| 暗角 | +15 | 威胁感 |

**调色预设描述**:
```
Scene 4-3 Color Grade (Iron Shovel):
- Rusty metal reflecting cold moonlight
- Sharp metallic highlights
- Dark vignette for threat
- Shallow depth of field
- Mood: Instrument of death/burial
- Visual symbolism of danger
```

---

### 镜头 2-4-4：黑洞洞窗户 ⭐⭐⭐

**调色重点**: 悬念氛围，渐黑效果

| 调整项 | 参数 | 说明 |
|--------|------|------|
| 色温 | 7500K | 冷色 |
| 曝光 | 渐变 | 100%→30% |
| 对比度 | +30 | 强化黑暗 |
| 饱和度 | 渐降 | 色彩消退 |

**调色预设描述**:
```
Scene 4-4 Color Grade (Dark Window - CORE VISUAL):
- Black void holes in window paper
- Cold moonlight on frame
- Subtle shadowy figures within
- GRADUAL FADE TO DARKNESS (核心效果)
- Mood: Unseen observers, suspense
- Cliffhanger ending

Technical Notes:
- Fade speed: Last 3 seconds from 100% to 30%
- High contrast to emphasize darkness
- Cold blue undertone
- Sense of being watched
```

---

## 调色资源清单

### 按场景分类

| 场景 | 主色调 | 辅助色 | 强调色 | 色温 |
|------|--------|--------|--------|------|
| 场景1 | 月白 #D4E5F7 | 昏黄 #C4A35A | 泪晶 #E8F4FF | 5500-6500K |
| 场景2 | 暗青灰 #8B9DA8 | 暗褐 #5C4033 | 猩红 #8B0000 ⭐ | 6500-6800K |
| 场景3 | 暖褐 #6B4423 | 丝白 #F5F5F0 | 泪光 #FFF8E7 | 5200-5800K |
| 场景4 | 月光蓝 #A4C3D2 | 银白 #C0C0C0 | 金属灰 #71797E | 7200-7500K |

### 按镜头类型分类

| 镜头类型 | 调色重点 | 关键词 |
|----------|----------|--------|
| 表演特写 | 肤色情绪，泪光晶莹 | warm candlelight, crystal tears |
| 沈清起特写 | 明暗分割，冰封质感 | split lighting, ice cold |
| 血滴特写 ⭐ | 猩红强调，凄美意象 | crimson red, beautiful tragedy |
| 月光场景 | 轮廓光，剪影效果 | rim lighting, silhouette |
| 悬念结尾 | 渐黑效果，冷色调 | fade to darkness, suspense |

---

## 调色预设速查表

### LUT 参考建议

| 场景 | LUT 风格 | 说明 |
|------|----------|------|
| 场景1 | Blue Candlelight | 月光+青灯混合 |
| 场景2 | Tragedy Red | 血滴强调的悲剧色调 |
| 场景3 | Warm Devotion | 忠诚温暖的褐色调 |
| 场景4 | Cold Suspense | 冷色悬念的月光调 |

### 全局调整参数

```
基础设置:
- Overall Temperature: Cool (6000-7000K)
- Overall Tint: Slightly Magenta (+5)
- Exposure: -0.3 to -0.5 EV
- Contrast: +10 to +20
- Highlights: -10 to -20
- Shadows: +5 to +15
- Whites: -10
- Blacks: -5
- Clarity: +5 to +10
- Saturation: -10 to -15
- Vibrance: +5

曲线调整:
- RGB曲线: S形曲线增加对比
- Red通道: 暗部轻微提升
- Green通道: 中间调轻微下降
- Blue通道: 暗部提升（冷色阴影）
```

---

## 与其他章节调色衔接

### 与第1章调色对比

| 要素 | 第1章 | 第2章 |
|------|-------|-------|
| 整体色调 | 青灰压抑 | 冷暖交织→冷色悬念 |
| 核心强调色 | 无 | 猩红血滴 ⭐ |
| 情绪表达 | 诡异神秘 | 紧张悲凉 |
| 光源特点 | 青灯主导 | 月光渐强 |

### 为第3章铺垫

| 铺垫要素 | 第2章结尾 | 第3章预期 |
|----------|-----------|-----------|
| 色调 | 冷色悬念 | 对峙紧张 |
| 黑暗程度 | 渐黑效果 | 可能黎明或持续黑暗 |
| 情绪 | 悬念 | 危机应对 |

---

## 质量检查清单

### 生成前检查
- [ ] 所有场景调色与情绪匹配
- [ ] 血滴红色足够醒目 ⭐
- [ ] 月光与青灯的方向一致
- [ ] 色温变化符合剧情节奏

### 生成后检查
- [ ] 场景1：泪滴晶莹效果
- [ ] 场景2：血滴凄美意象 ⭐
- [ ] 场景3：忠诚温暖氛围
- [ ] 场景4：月光剪影效果 ⭐
- [ ] 结尾：渐黑悬念效果
- [ ] 整体色调统一

---

*由 AI调色师 生成*
