# 场景特效设计 - 第1章 你自尽吧

> **使用说明**:
> - 本文件包含本章所有场景的特效设计方案
> - 特效用于视频生成和后期制作
> - 提示词片段可直接整合到视频提示词中

---

## 章节特效总览

### 整体氛围特效

| 特效类型 | 强度 | 描述 | 贯穿场景 |
|----------|------|------|----------|
| 青灯摇曳 | 中等 | 唯一暖光源，火焰跳动 | 全章 |
| 月光光束 | 中等 | 穿过破窗纸的体积光 | 卧房场景 |
| 尘埃粒子 | 微妙 | 在光束中飘浮的尘埃 | 全章 |
| 寒风呼啸 | 微妙 | 北风吹入，烛火抖动 | 全章 |
| 阴影舞动 | 微妙 | 烛光产生的动态阴影 | 全章 |

### 关键时刻特效

| 时刻 | 镜头 | 特效 | 强度 | 描述 |
|------|------|------|------|------|
| 穿书苏醒 | 1-1-1 | 月光聚焦 | 中等 | 光束指向辛月影 |
| 病娇亮相 | 1-2-1 | 月光人脸 | 强烈 | 月光如聚光灯照沈清起 |
| 剑指咽喉 | 1-3-3 | 剑光寒芒 | 中等 | 剑身映出虹光 |
| 剑刺木柱 | 1-5-1 | 剑鸣振动 | 中等 | 剑身嗡鸣，粒子震颤 |
| 碎瓷流血 | 1-6-1 | 血滴慢动作 | 强烈 | 血滴落下的特写 |
| 阴鸷结尾 | 1-7-3 | 渐暗效果 | 中等 | 画面边缘变暗 |

---

## 场景特效详细设计

### 场景 1: 破败草屋·卧房（主场景）

#### 基础氛围特效

**1. 青灯摇曳 (Primary Light Source)**

```
效果描述: 角落里的青灯是室内唯一暖光源，火焰持续跳动
强度: 中等 (moderate)
颜色: 暖黄色 (#F4D03F)
运动: 持续微弱跳动，偶尔有明显摇曳

提示词片段:
- flickering blue oil lamp flame, dancing candlelight
- warm yellow glow pulsing gently, soft flame movement
- candlelight casting dancing shadows on walls
- flame swaying in draft from window gaps

动态参数:
- 跳动频率: 2-3次/秒
- 亮度变化: ±15%
- 阴影移动: 缓慢摇晃
```

**2. 月光体积光 (Volumetric Moonlight)**

```
效果描述: 月光穿过破窗纸的洞，形成可见的光束
强度: 中等 (moderate)
颜色: 月白色/冷蓝色 (#D5D8DC)
运动: 静态，但尘埃在其中飘浮

提示词片段:
- pale cold moonlight streaming through torn window paper
- volumetric light beams cutting through darkness
- god rays from moon, visible light shafts
- moonlight creating eerie atmosphere, cold blue tones

动态参数:
- 光束角度: 从窗户斜向下约30°
- 光束内尘埃: 微弱飘浮
- 光束强度: 稳定，无闪烁
```

**3. 尘埃粒子 (Dust Particles)**

```
效果描述: 在光束中可见的尘埃颗粒，缓慢飘浮
强度: 微妙 (subtle)
颜色: 半透明，在光中呈金色
运动: 缓慢漂浮，无规则

提示词片段:
- dust motes floating in moonlight beams
- tiny particles drifting in air, visible in light
- atmospheric dust creating depth, motes of light
- floating dust particles, gentle movement

动态参数:
- 粒子密度: 稀疏（每立方英尺约10-15个可见粒子）
- 运动速度: 极慢（0.5-1cm/秒）
- 方向: 无规则漂浮，略有下沉趋势
```

**4. 寒风效果 (Cold Wind)**

```
效果描述: 北风从破窗和墙缝吹入，导致烛火摇曳
强度: 微妙 (subtle)
表现: 烛火方向变化、窗户破损处轻微飘动
运动: 间歇性，配合音效

提示词片段:
- cold northern wind blowing through gaps
- draft making candlelight flicker
- winter air seeping through broken window
- wind causing flame to dance erratically

动态参数:
- 风的频率: 每隔5-8秒有明显一阵
- 烛火反应: 火焰明显向一边倾斜
- 伴随: 窗纸破损处轻微飘动
```

---

### 关键镜头特效设计

#### 镜头 1-1-1: 穿书苏醒

**特效组合**:
```
基础氛围:
- flickering candlelight from corner
- moonlight beam pointing toward Xin Yueying
- dust particles floating in light

强化效果:
- subtle god rays focusing on unconscious figure
- dim atmospheric haze
- soft shadows from overhead angle

提示词整合:
"dim cottage interior, flickering oil lamp in corner casting warm glow,
cold moonlight beam streaming through torn window paper forming visible light shaft pointing toward prone figure,
dust particles floating gently in the light,
oppressive eerie atmosphere, dramatic overhead shot"
```

#### 镜头 1-2-1: 病娇亮相

**特效组合**:
```
基础氛围:
- moonlight as key light illuminating Shen Qingqi's face
- candlelight from side as fill light
- sharp contrast between lit and shadow areas

强化效果:
- dramatic spotlight effect from moonlight
- cold ethereal glow on pale skin
- phoenix eyes with subtle cold glint
- porcelain pieces catching light

提示词整合:
"dramatic chiaroscuro lighting, cold pale moonlight beam as spotlight on Shen Qingqi's face,
making pale skin appear ethereal and cold,
flickering candlelight from corner casting warm accent,
broken porcelain pieces scattered on floor catching glints of light,
sharp contrast between illuminated face and dark background,
menacing beautiful atmosphere"
```

#### 镜头 1-3-3: 剑光特写

**特效组合**:
```
特效重点: 剑身寒光

效果描述:
- cold gleam running along sword blade
- rainbow-like light reflection (虹光)
- sharp metallic shine

提示词整合:
"close-up of three-foot sword blade, cold steel gleaming,
sharp edge catching light creating rainbow-like reflection,
sword tip pointing forward with menacing glint,
dramatic side lighting highlighting the blade,
cold metallic sheen, dangerous weapon"
```

#### 镜头 1-5-1: 剑刺木柱

**特效组合**:
```
特效重点: 剑身振动嗡鸣

效果描述:
- sword vibrating after impact
- wood particles from pillar
- motion blur on sword

提示词整合:
"sword embedded in wooden pillar, blade vibrating with humming sound,
wood dust particles scattered from impact point,
motion blur on sword indicating recent impact,
dramatic angle showing sword hilt to tip,
tension and danger"
```

#### 镜头 1-6-1: 碎瓷流血

**特效组合**:
```
特效重点: 血滴落下的慢动作效果

效果描述:
- blood drops falling in slow motion
- blood catching dim light
- crimson red contrasting with dark background

提示词整合:
"extreme close-up of blood drops trickling between fingers,
falling toward ground in slow motion,
crimson red blood catching dim candlelight,
droplets forming and breaking away,
dramatic lighting highlighting blood against dark background,
artistic unsettling composition"
```

#### 镜头 1-7-3: 阴鸷冷笑（结尾）

**特效组合**:
```
特效重点: 画面渐暗，悬念氛围

效果描述:
- vignette effect darkening edges
- gradual fade to darkness
- cold menacing atmosphere
- eyes with subtle sinister glint

提示词整合:
"extreme close-up on phoenix eyes, cold sinister gleam,
thin lips parted in chilling smile,
vignette effect darkening edges of frame,
cold moonlight from side creating sharp shadows,
suspenseful ominous atmosphere,
gradual fade to darkness, ending悬念"
```

---

## 场景 2: 破败草屋·门外

#### 基础氛围特效

**1. 月光轮廓光 (Rim Lighting)**

```
效果描述: 月光从背后照来，在角色身上形成轮廓光
强度: 中等 (moderate)
颜色: 银白色/冷蓝色
运动: 稳定

提示词片段:
- moonlight creating dramatic rim lighting
- silver edge glow on silhouettes
- cold backlight outlining figures
- crescent moon as key light source
```

**2. 枯叶飘散 (Dead Leaves)**

```
效果描述: 北风吹过，枯叶在地面和空中飘动
强度: 微妙到中等
颜色: 棕褐色/灰色
运动: 随风飘动，无规则

提示词片段:
- dead leaves scattering in cold wind
- dried leaves drifting across ground
- autumn leaves blowing in night breeze
- withered foliage carried by northern wind
```

**3. 远山剪影 (Distant Silhouettes)**

```
效果描述: 远处的树林和山脉在月光下的剪影
强度: 微妙 (背景元素)
颜色: 深蓝/黑色
运动: 静态

提示词片段:
- distant forest silhouettes against night sky
- mountain outlines barely visible in darkness
- dark tree line on horizon
- shadowy wilderness surrounding cottage
```

---

## 特效与视频工具对应

### Veo3.1 Fast 特效提示词

| 镜头 | 特效关键词 |
|------|-----------|
| 1-1-1 | flickering candlelight, volumetric moonlight beam, floating dust particles, dim atmospheric lighting |
| 1-2-1 | dramatic spotlight effect, cold ethereal glow, sharp chiaroscuro lighting, porcelain glinting |
| 1-5-1 | sword vibrating, wood particles scattering, motion blur, impact effect |
| 1-6-1 | blood drops in slow motion, crimson red catching light, droplets forming |
| 1-7-3 | vignette darkening, sinister eye glint, gradual fade, suspenseful atmosphere |

### 可灵动画 特效提示词

| 镜头 | 特效关键词 |
|------|-----------|
| 1-1-1 | 烛光摇曳, 月光光束, 尘埃飘浮, 压抑氛围, 电影级光影 |
| 1-2-1 | 聚光灯效果, 病态苍白光泽, 强烈明暗对比, 碎瓷反光 |
| 1-5-1 | 剑身振动, 木屑飞散, 动态模糊, 撞击效果 |
| 1-6-1 | 血滴慢动作, 鲜红血液, 光线下闪烁, 水滴形成 |
| 1-7-3 | 边缘渐暗, 阴鸷眼光, 逐渐变暗, 悬念氛围 |

---

## 特效强度指南

### 按情绪强度调整

| 情绪阶段 | 镜头范围 | 特效强度 | 描述 |
|----------|----------|----------|------|
| 困惑 | 1-1-1~1-1-2 | 微妙 | 基础氛围，不过度 |
| 惊艳 | 1-2-1 | 中等 | 强化月光效果 |
| 震惊 | 1-2-2~1-3-1 | 中等 | 强调情绪转变 |
| 紧张 | 1-3-2~1-4-2 | 中等 | 强化压迫感 |
| 绝望 | 1-5-1~1-5-3 | 中等 | 强化冲击力 |
| 转机 | 1-6-1~1-7-1 | 中等 | 平衡氛围 |
| 悬念 | 1-7-2~1-7-3 | 强烈 | 强化结尾氛围 |

---

## 特效提示词整合模板

### 完整镜头特效模板

```
[场景基础] + [光源描述] + [氛围特效] + [动态元素] + [情绪渲染]

示例 (镜头 1-1-1):
"dilapidated cottage bedroom at night" (场景基础)
"flickering oil lamp casting dancing shadows" (光源)
"moonlight beam through torn window, volumetric lighting" (氛围)
"dust particles floating in light" (动态)
"oppressive eerie atmosphere" (情绪)
```

---

## 特效检查清单

### 生成前检查
- [x] 所有场景的光源方向一致
- [x] 青灯位置固定（角落）
- [x] 月光方向固定（窗户侧）
- [x] 特效强度与情绪匹配
- [x] 特效不影响角色表现

### 生成后检查
- [ ] 光影效果自然
- [ ] 粒子效果不突兀
- [ ] 动态效果流畅
- [ ] 整体氛围统一

---

*由 AI特效师 生成*
