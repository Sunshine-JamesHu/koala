# 特效设计 - 第1章 你自尽吧

## 章节信息
- **章节标题**: 你自尽吧
- **视觉风格**: 3D国漫渲染风格，前期青灰压抑氛围
- **特效总基调**: 阴冷、压抑、惊悚，月光与烛光交织的诡异光影

---

## 全局特效设定

### 光影基调
| 项目 | 设定 |
|------|------|
| 主光源 | 月光（冷色调，天青色偏蓝） |
| 次光源 | 青灯烛光（暖色调，昏黄色） |
| 光比 | 高反差，明暗对比强烈 |
| 阴影 | 柔和但深重的阴影，营造神秘感 |

### 粒子效果库
| 粒子类型 | 使用场景 | 特征描述 |
|----------|----------|----------|
| 尘埃粒子 | 破败草屋内 | floating dust particles, motes of light in dim air, subtle golden motes catching lamplight |
| 月光光斑 | 窗户透光处 | moonlight beams streaming through broken window paper, volumetric lighting, soft god rays |
| 烛火摇曳 | 青灯位置 | flickering candlelight, warm glow pulsing gently, dancing shadows on walls |
| 剑身寒光 | 剑锋特写 | cold steel glint, sharp blade reflection, icy blue shimmer |

### 氛围渲染
| 效果 | 描述 |
|------|------|
| 体积光 | volumetric fog, light shafts piercing through darkness, atmospheric haze |
| 寒风 | cold draft visualization, fabric and hair movement, invisible force suggestion |
| 阴影动态 | dynamic shadows from flickering light source, elongated silhouettes |

---

## 场景特效详解

### 场景1: 苏醒与审判

#### 镜头 1-1 特效 (女主眼睛特写)

**特效组合**:
```
场景描述: 黑暗中女主眼睛缓缓睁开
基础特效:
- 景深变化: depth of field transition, from blur to sharp focus
- 瞳孔反光: subtle light reflection in pupil, dim lamplight glimmer

特效提示词:
```
Extreme close-up of young woman's eye slowly opening in darkness,
depth of field blur gradually sharpening to crystal clear focus,
dim teal light reflection shimmering in pupil,
subtle floating dust particles catching faint light around eye area,
soft volumetric darkness surrounding the eye,
mysterious atmosphere, 3D animation render, cinematic lighting,
Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 微妙 (subtle)
**特效时机**: 持续渐变

---

#### 镜头 1-2 特效 (破败草屋远景)

**特效组合**:
```
场景描述: 俯视展示破败草屋全貌
基础特效:
- 月光体积光: moonlight streaming through broken window, volumetric god rays
- 尘埃粒子: floating dust motes dancing in light beams
- 烛光摇曳: flickering lamplight casting dancing shadows

特效提示词:
```
Wide establishing shot of dilapidated thatched cottage interior,
cold moonlight streaming through torn window paper creating volumetric light shafts,
floating dust particles dancing in pale blue light beams,
warm flickering candlelight in corner creating dancing shadows,
atmospheric haze and depth, mysterious gloomy atmosphere,
silhouette of man in wheelchair barely visible in shadows,
young woman lying on cold earthen floor,
high contrast lighting, cinematic composition,
3D animation render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 持续

---

#### 镜头 1-3 特效 (女主慵懒姿态)

**特效组合**:
```
场景描述: 女主翻身侧卧，慵懒姿态
基础特效:
- 环境光: dim ambient lighting with soft candlelight glow
- 衣服质感: silk fabric subtle sheen

特效提示词:
```
Medium shot of beautiful young woman in red ancient Chinese dress,
lounging lazily on cold earthen floor, cheek resting on hand,
playful teasing expression contrasting with gloomy environment,
soft warm candlelight glow on her face, subtle fabric sheen on silk dress,
dim dusty background with floating particles,
ironic contrast between her relaxed pose and ominous surroundings,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 微妙 (subtle)
**特效时机**: 持续

---

#### 镜头 1-4 特效 (沈清起脸庞特写)

**特效组合**:
```
场景描述: 沈清起从阴影中显露
基础特效:
- 动态阴影: flickering shadows from candlelight on face
- 冷光轮廓: cold moonlight rim lighting on silhouette
- 凤眼光效: sharp gleam in narrow phoenix eyes

特效提示词:
```
Close-up shot revealing handsome man's face emerging from shadows,
cold pale moonlight creating eerie rim lighting on his sharp features,
flickering candlelight casting dynamic shadows across his face,
narrow phoenix eyes gleaming with cold murderous intent,
thin lips curved in ambiguous smile, ghostly pale skin,
atmospheric volumetric lighting, dramatic chiaroscuro effect,
sinister oppressive aura, cold color palette,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 强烈 (intense)
**特效时机**: 持续，推镜头过程中渐强

---

### 场景2: 穿书觉醒

#### 镜头 2-1 特效 (女主震惊)

**特效组合**:
```
场景描述: 女主表情凝固，瞳孔收缩
基础特效:
- 视觉扭曲: subtle visual distortion effect showing inner shock
- 瞳孔变化: pupil contraction emphasis

特效提示词:
```
Close-up of young woman's face freezing in shock,
subtle visual distortion around edges suggesting mental impact,
pupils suddenly contracting, blood draining from face,
expression shifting from playful to terrified in split second,
dramatic lighting emphasizing her fear,
subtle camera shake effect, heartbeat pulsing visual,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 触发瞬间

---

#### 镜头 2-2 特效 (闪回蒙太奇)

**特效组合**:
```
场景描述: 快速闪回小说情节
基础特效:
- 画面边缘模糊: edge blur effect, vignette
- 快速切换: rapid transition effects
- 褪色效果: desaturated color grading

特效提示词 (综合):
```
Rapid flashback montage sequence,
series of quick cuts showing tragic backstory:
1.沈家蒙冤 - family being arrested, chains and prison cells, desaturated cold blue tones
2.酷刑折磨 - dark dungeon, chains, pain and suffering, harsh shadows
3.被救出逃 - desperate escape through rain, lightning flashes
4.成为权臣 - cold calculating expression in grand hall, power and corruption
5.凄惨结局 - body hanging from city gate, tragic ending

Visual effects: edge blur, desaturated colors, grain texture,
rapid cuts with motion blur transitions, dramatic lighting in each scene,
flashback memory aesthetic, dreamlike quality,
3D animation render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 持续，快速切换

---

#### 镜头 2-3 特效 (剑锋对峙)

**特效组合**:
```
场景描述: 剑锋指向女主
基础特效:
- 剑身虹光: rainbow shimmer on blade edge, sharp steel reflection
- 寒光闪烁: cold light glinting off sword
- 风动效果: cold draft visualization

特效提示词:
```
Wide shot showing tense confrontation,
three-foot sharp sword blade pointed at young woman,
cold steel gleaming with iridescent rainbow light along edge,
harsh winter wind blowing through broken window,
candlelight flickering wildly casting dancing shadows,
dust and debris floating in turbulent air,
atmospheric tension, life-threatening danger,
3D animation render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 强烈 (intense)
**特效时机**: 持续

---

#### 镜头 2-4 特效 (沈清起威胁)

**特效组合**:
```
场景描述: 沈清起摩挲碎瓷
基础特效:
- 碎瓷反光: subtle light reflection on porcelain shard
- 阴影笼罩: heavy shadow enveloping figure

特效提示词:
```
Close-up of elegant man's hand with porcelain shard,
slender fingers delicately caressing broken ceramic piece,
cold calculating expression, shadows deepening around him,
candlelight catching edge of shard creating subtle glint,
oppressive atmosphere, silent menace radiating from stillness,
low key lighting, dramatic shadow play,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 持续，推镜头渐强

---

### 场景3: 夺门逃亡

#### 镜头 3-1 特效 (女主撞柱)

**特效组合**:
```
场景描述: 女主惊惶起身撞柱
基础特效:
- 撞击震动: subtle screen shake on impact
- 恐慌氛围: chaotic lighting from movement

特效提示词:
```
Close-up of terrified young woman backing into wooden pillar,
impact vibration effect, slight camera shake on collision,
panic stricken expression, hair disheveled from sudden movement,
harsh shadows from single light source, claustrophobic framing,
desperate eyes searching for escape route,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 触发撞击瞬间

---

#### 镜头 3-2 特效 (逃跑躲避)

**特效组合**:
```
场景描述: 女主逃跑，剑光闪过
基础特效:
- 剑光动态模糊: motion blur on sword swing, light trail
- 速度线: speed lines suggesting quick movement

特效提示词:
```
Action shot of young woman dodging sword strike,
razor sharp blade swinging through air with motion blur,
cold light trail following sword arc,
desperate evasive movement, fabric and hair flying,
dynamic camera following action,
near-death escape, blade almost grazing neck,
3D animation render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 强烈 (intense)
**特效时机**: 动作瞬间

---

#### 镜头 3-3 特效 (剑刺木柱)

**特效组合**:
```
场景描述: 长剑刺入木柱嗡鸣
基础特效:
- 剑身震动: blade vibration effect, blur on edges
- 木屑飞溅: wood splinters spraying

特效提示词:
```
Extreme close-up of sword blade embedded in wooden pillar,
metal blade vibrating with visible blur effect,
wood splinters and dust particles spraying from impact point,
cold steel gleaming in dim light, sharp edge dangerously close,
resonating vibration effect, lingering danger,
3D render with particle effects, Unreal Engine 5 quality
```

**特效强度**: 中等 (moderate)
**特效时机**: 持续震动

---

#### 镜头 3-4 特效 (撞上霍齐)

**特效组合**:
```
场景描述: 女主撞上霍齐被推回
基础特效:
- 月光剪影: moonlight silhouette effect on 霍齐 figure
- 撞击效果: impact visualization

特效提示词:
```
Medium shot of collision at doorway,
large burly man with beard silhouetted in moonlight,
young woman bouncing off his solid chest,
cold night wind blowing into room,
dramatic backlighting creating menacing silhouette,
desperation turning to despair as escape is blocked,
3D animation render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 撞击瞬间

---

### 场景4: 谎言求生

#### 镜头 4-1 特效 (被推回对峙)

**特效组合**:
```
场景描述: 女主被推回与沈清起对视
基础特效:
- 烛光噼啪: candlelight flickering with occasional sparks
- 眼神压迫: oppressive gaze visualization

特效提示词:
```
Medium shot of tense standoff,
young woman stumbling back into room,
man in wheelchair watching with predatory amusement,
flickering candlelight creating shifting shadows,
oppressive atmosphere, psychological warfare visible in lighting,
cat playing with mouse energy, subtle menace in every shadow,
3D animation render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 持续

---

#### 镜头 4-2 特效 (女主开始表演)

**特效组合**:
```
场景描述: 女主灵机一动拍手表演
基础特效:
- 表情变化光效: subtle light change emphasizing expression shift
- 拍手震动: slight impact effect

特效提示词:
```
Close-up of young woman's face with sudden inspiration,
eyes widening with feigned shock, acting performance beginning,
clapping hands together for emphasis,
lighting subtly shifting to highlight her performance,
desperation masked by clever acting,
transformation from victim to performer,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 微妙 (subtle)
**特效时机**: 表情变化瞬间

---

#### 镜头 4-3 特效 (编造谎言)

**特效组合**:
```
场景描述: 女主情真意切地表演
基础特效:
- 柔和聚光: soft spotlight effect on her earnest face
- 眼神诚恳: sincere eye expression emphasis

特效提示词:
```
Medium shot of young woman delivering passionate plea,
earnest tearful expression, hands gesturing convincingly,
soft warm lighting on her face emphasizing sincerity,
desperate performance to save her life,
every word calculated for maximum effect,
authentic-seeming distress and concern,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 微妙 (subtle)
**特效时机**: 持续

---

#### 镜头 4-4 特效 (沈清起审视)

**特效组合**:
```
场景描述: 沈清起审视女主
基础特效:
- 阴冷笑声氛围: cold sinister atmosphere with his laugh
- 眼神变化: subtle gleam shift in eyes
- 侧脸阴影: dramatic side profile shadow

特效提示词:
```
Close-up of man's face with calculating expression,
cold laugh echoing, eyes narrowing with dark amusement,
shadows playing across his sharp features,
ambiguous smile playing on thin lips,
predator assessing prey's performance,
cold moonlight accentuating his sinister beauty,
3D character render, Unreal Engine 5 quality, Chinese Donghua Style
```

**特效强度**: 中等 (moderate)
**特效时机**: 持续，结尾渐弱

---

## 特效总表

| 镜头号 | 主要特效 | 强度 | 特效时机 |
|--------|----------|------|----------|
| 1-1 | 景深变化、瞳孔反光 | 微妙 | 渐变 |
| 1-2 | 体积光、尘埃粒子、烛光摇曳 | 中等 | 持续 |
| 1-3 | 环境光、衣服质感 | 微妙 | 持续 |
| 1-4 | 动态阴影、冷光轮廓、凤眼光效 | 强烈 | 渐强 |
| 2-1 | 视觉扭曲、瞳孔变化 | 中等 | 瞬间 |
| 2-2 | 边缘模糊、褪色效果、快速切换 | 中等 | 持续 |
| 2-3 | 剑身虹光、寒光闪烁、风动 | 强烈 | 持续 |
| 2-4 | 碎瓷反光、阴影笼罩 | 中等 | 渐强 |
| 3-1 | 撞击震动、恐慌氛围 | 中等 | 触发 |
| 3-2 | 动态模糊、速度线 | 强烈 | 动作瞬间 |
| 3-3 | 剑身震动、木屑飞溅 | 中等 | 持续 |
| 3-4 | 月光剪影、撞击效果 | 中等 | 瞬间 |
| 4-1 | 烛光噼啪、压迫氛围 | 中等 | 持续 |
| 4-2 | 表情变化光效、拍手震动 | 微妙 | 瞬间 |
| 4-3 | 柔和聚光、眼神诚恳 | 微妙 | 持续 |
| 4-4 | 阴冷氛围、眼神变化、侧脸阴影 | 中等 | 持续 |

---

## 特效渲染注意事项

### 光影一致性
- 保持月光冷色调(天青偏蓝)与烛光暖色调(昏黄)的对比
- 所有室内场景需同时考虑两个光源的影响
- 阴影应柔和但有深度，符合3D国漫风格

### 粒子系统
- 尘埃粒子需在光照区域可见，暗区不可见
- 粒子运动应自然缓慢，符合静止空气中的漂浮状态
- 粒子数量：低密度，营造荒凉感

### 氛围渲染
- 整体色调偏冷(青灰)，营造压抑感
- 高对比度光照，强调危机四伏的感觉
- 体积光用于强调月光穿透效果

### 特效强度控制
- 本章为开篇，特效以氛围渲染为主
- 避免过度华丽的特效，保持古风写实质感
- 特效应服务于情绪表达，不喧宾夺主

---

## 与第2章特效衔接

### 光影延续
- 第2章继续使用相同的月光/烛光双光源设定
- 氛围从压抑逐渐转向悲凉

### 特效过渡
- 血滴效果将在第2章成为重要特效元素
- 泪水特效将在第2章表演场景中强化

---

*由 AI特效师 生成*
