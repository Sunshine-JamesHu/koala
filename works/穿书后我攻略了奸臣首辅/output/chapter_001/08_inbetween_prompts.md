# 补间动画提示词 - 第1章 你自尽吧

> **使用说明**:
> - 本文件包含关键帧之间的过渡动画提示词
> - 用于在关键帧之间创建流畅的动作过渡
> - 可用于 Veo3.1 Fast 或 可灵动画 生成过渡视频
> - 补间动画时长通常为 3-5 秒

---

## 补间动画总览

| 编号 | 起始关键帧 | 结束关键帧 | 动作类型 | 时长 | 优先级 |
|------|------------|------------|----------|------|--------|
| IB-01 | KF-01 穿书苏醒 | KF-02 以为是梦 | 起身过渡 | 5秒 | 高 |
| IB-02 | KF-02 以为是梦 | KF-03 穿书意识 | 表情变化 | 4秒 | 高 |
| IB-03 | KF-03 穿书意识 | 后退撞柱 | 后退动作 | 5秒 | 高 |
| IB-04 | 轮椅剪影 | KF-04 病娇亮相 | 前倾亮相 | 5秒 | 高 |
| IB-05 | 剑指咽喉 | 萌生逃跑 | 眼神移动 | 4秒 | 中 |
| IB-06 | 剑指咽喉 | 夺门逃跑 | 突然起跑 | 4秒 | 高 |
| IB-07 | 奔跑动作 | KF-07 撞上霍齐 | 碰撞反弹 | 4秒 | 高 |
| IB-08 | 被推回屋 | KF-09 谎言表演 | 灵机一动 | 5秒 | 中 |
| IB-09 | KF-09 表演开始 | 沈清起反应 | 合掌表演 | 5秒 | 中 |
| IB-10 | 沈清起玩味 | KF-06 阴鸷冷笑 | 表情转变 | 5秒 | 高 |

---

## IB-01: 苏醒起身（5秒）

**起始关键帧**: KF-01 辛月影躺在地上，闭眼
**结束关键帧**: KF-02 辛月影侧卧支颊，轻笑

### 动作分解

**阶段1 (0-2秒)**: 手指微动，睫毛颤动
**阶段2 (2-3.5秒)**: 缓缓睁开眼睛，撑起上半身
**阶段3 (3.5-5秒)**: 翻身侧卧，一手托腮，露出轻笑

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:02] Xin Yueying lying unconscious on cold mud floor. Her fingers begin to twitch slightly. Eyelashes flutter. Body remains limp but showing signs of waking. Dust particles floating in moonlight beam above her.

[00:02-00:03.5] Her eyes slowly open, dazed and confused. She props herself up on one arm with effort, looking around bewilderedly. Movement is slow and groggy, like waking from deep sleep.

[00:03.5-00:05] She rolls onto her side, one hand propping up her cheek. Her expression shifts from confused to curious and slightly amused. A soft smile appears as she notices the shadowy corner.

Smooth natural motion flow, easing in and out, soft body language transition, relaxed pace, warm candlelight and cold moonlight contrast, ancient Chinese cottage setting

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影，约20岁女子，双螺髻，灰色粗布衣裳，从昏迷状态苏醒。

（运动描述）
0-2秒：躺在泥土地面上的辛月影，手指微微颤动，睫毛轻颤，身体从完全放松状态开始有反应，显示苏醒迹象。
2-3.5秒：眼睛缓缓睁开，眼神迷茫困惑，用手臂支撑着撑起上半身，动作缓慢慵懒，像从深度睡眠中醒来。
3.5-5秒：翻身侧卧，一手托着腮帮，表情从困惑转为好奇，嘴角浮现轻笑，看向角落阴影，姿态放松慵懒。

（场景描述）
破败草屋卧房，青灯摇曳，月光光束，尘埃飘浮。

（镜头语言 + 光影 + 氛围）
固定中景，缓入缓出节奏，从昏迷到苏醒的自然过渡，柔和光影，慵懒梦幻氛围。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **缓入缓出 (Ease In/Out)**: 动作开始和结束都缓慢，中间稍快
- **自然呼吸感**: 添加微小的呼吸起伏

---

## IB-02: 表情剧变（4秒）

**起始关键帧**: KF-02 辛月影慵懒轻笑
**结束关键帧**: KF-03 辛月影震惊恐惧

### 动作分解

**阶段1 (0-1秒)**: 笑容保持，眼神开始变化
**阶段2 (1-2.5秒)**: 笑容凝固，眼睛睁大，瞳孔收缩
**阶段3 (2.5-4秒)**: 完全震惊，嘴巴微张，脸色变白

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01] Close-up on Xin Yueying's face. She maintains her soft amused smile, eyes still curved with mirth. Peaceful dream-like expression.

[00:01-00:02.5] Her smile slowly freezes. Eyes begin to widen, the curve of her smile flattening. Pupils start to constrict visibly. A subtle change from amusement to confusion to dawning horror.

[00:02.5-00:04] Extreme close-up on eyes. Pupils fully constricted, eyes wide with shock and terror. Mouth slightly open, breath caught. Face paling. Expression of complete disbelief and fear. She realizes this is not a dream.

Subtle facial muscle transitions, natural expression change progression, psychological shock moment, dramatic lighting emphasizing eyes, soft focus background

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影脸部特写，表情从慵懒轻笑剧变为震惊恐惧。

（运动描述）
0-1秒：辛月影脸部近景，保持柔和的笑容，眼睛弯成月牙，沉浸在看"帅哥"的愉悦中，表情慵懒梦幻。
1-2.5秒：笑容慢慢凝固，眼睛开始睁大，笑意从嘴角消退，瞳孔开始收缩，表情从愉悦→困惑→惊恐逐渐转变。
2.5-4秒：眼睛极度睁大特写，瞳孔完全收缩，嘴巴微张，呼吸停顿，脸色变得苍白，震惊、恐惧、难以置信的表情完全呈现，意识到这不是梦。

（场景描述）
破败草屋卧房背景虚化，聚焦脸部表情变化。

（镜头语言 + 光影 + 氛围）
脸部特写，微妙的面部肌肉变化，自然的表情递进，心理震撼的瞬间，戏剧性光影强调眼睛。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **前慢后快**: 前半段缓慢变化，后半段加速
- **情绪爆发点**: 在2.5秒处达到情绪爆发

---

## IB-03: 后退撞柱（5秒）

**起始关键帧**: KF-03 辛月影震惊状态
**结束关键帧**: 背靠木柱，退无可退

### 动作分解

**阶段1 (0-1.5秒)**: 从震惊中反应过来，开始后退
**阶段2 (1.5-3秒)**: 惊惶后退，脚步踉跄
**阶段3 (3-4秒)**: 脊背撞上木柱，身体震颤
**阶段4 (4-5秒)**: 站稳，惊恐望向前方

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01.5] Xin Yueying scrambles backward in panic from her sitting position. Her body reacts before her mind catches up. Hands push against ground, feet sliding backward on mud floor.

[00:01.5-00:03] She continues retreating, panic in her movements. Camera follows her backward motion. Her breath comes in short gasps. She's not looking where she's going, eyes fixed forward in terror.

[00:03-00:04] Her back hits a thick wooden pillar with a dull thud. Body jolts from impact. Nowhere left to retreat. Her body tenses against the pillar.

[00:04-00:05] She freezes, pressed against the pillar, eyes still wide with terror. Looking forward at the threat. Shoulders hunched, defensive posture.

Panic-driven motion, backward movement, body language showing fear, impact reaction, trapped animal feeling, dramatic shadows from flickering light

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影，从震惊中反应过来，惊惶后退，撞上木柱。

（运动描述）
0-1.5秒：辛月影从震惊中反应过来，本能地开始后退。双手撑地，脚在泥地上滑动，身体向后移动，动作仓皇。
1.5-3秒：继续后退，恐慌驱动动作，镜头跟随她后退。呼吸急促，眼睛死死盯住前方威胁，不敢回头看路。
3-4秒：脊背撞上粗壮的木柱，发出闷响，身体因撞击而震颤。退无可退，身后是坚实的木柱。
4-5秒：身体紧贴木柱僵住，眼睛仍然充满恐惧，望向前方，肩膀耸起，防御姿态，无处可逃的绝望。

（场景描述）
破败草屋卧房，木柱在身后，昏暗光线，青灯摇曳。

（镜头语言 + 光影 + 氛围）
跟镜后退，恐惧驱动的动作，身体语言表达恐惧，撞击反应，被困的绝望感，烛火跳动产生的动态阴影。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **加速运动**: 后退速度逐渐加快
- **撞击停顿**: 撞柱瞬间有明显的停顿

---

## IB-04: 病娇亮相（5秒）

**起始关键帧**: 黑暗中的轮椅剪影
**结束关键帧**: KF-04 沈清起病娇面容

### 动作分解

**阶段1 (0-1.5秒)**: 黑暗中的剪影微微前倾
**阶段2 (1.5-3秒)**: 月光逐渐照亮脸部轮廓
**阶段3 (3-4秒)**: 凤眼和薄唇的细节展现
**阶段4 (4-5秒)**: 病态微笑定型，眼神寒意

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01.5] In the dark corner, a silhouette of a seated figure in wheelchair begins to lean forward. Only the faint outline visible against deeper darkness. Mysterious presence emerging.

[00:01.5-00:03] As the figure leans forward, moonlight beam gradually illuminates the face. First the sharp jawline, then the pale skin, finally revealing Shen Qingqi's features. Dramatic reveal like spotlight.

[00:03-00:04] Close-up on his face as moonlight fully illuminates it. Narrow phoenix eyes with cold penetrating gaze. Thin lips curving into ambiguous smile. Pale almost bloodless skin glowing ethereally in cold light.

[00:04-00:05] His full face now visible in moonlight, cold beautiful and dangerous. Eyes carrying cold menace, smile unsettling. A face that is both attractive and terrifying. Scattered porcelain pieces catching light around him.

Dramatic reveal, spotlight effect, moonlight as key light, chiaroscuro contrast, mysterious to menacing transition, beautiful but dangerous atmosphere

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
沈清起，从黑暗中的剪影前倾，月光照亮病娇面容。

（运动描述）
0-1.5秒：黑暗角落中，轮椅上的人影剪影微微前倾，只有模糊的轮廓可见，神秘的存在感增强。
1.5-3秒：随着身体前倾，月光光束逐渐照亮脸部。先是锋利的下颌线，然后是苍白的皮肤，最终揭示沈清起的五官。如聚光灯般的戏剧性亮相。
3-4秒：脸部近景，月光完全照亮。狭长凤眼带着寒意，薄唇弯成混沌的笑意，苍白无血色的皮肤在冷光中泛着森寒的光泽。
4-5秒：完整面容呈现，清冷俊美而危险。凤眼淬着寒意，薄唇衔着混沌笑意，美丽与恐怖并存，病态而绝美。碎瓷片在周围反射光芒。

（场景描述）
破败草屋卧房角落，月光聚光灯效果，青灯侧面补光。

（镜头语言 + 光影 + 氛围）
戏剧性亮相，聚光灯效果，月光为主光源，明暗对比强烈，从神秘到危险的转变，美丽而恐怖的氛围。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **缓慢揭示**: 动作缓慢，增加悬念
- **光影配合**: 月光揭示与动作同步

---

## IB-05: 眼神决断（4秒）

**起始关键帧**: 剑指咽喉，辛月影僵硬不动
**结束关键帧**: 眼神移向门口，萌生逃跑念头

### 动作分解

**阶段1 (0-1秒)**: 脸部僵硬，眼睛直视前方
**阶段2 (1-2.5秒)**: 眼神开始游移，瞥向门口
**阶段3 (2.5-4秒)**: 眼神定格在门口，决断形成

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01] Close-up on Xin Yueying's face, sword tip visible at edge of frame. She's frozen, eyes fixed straight ahead in terror. Breath held. Completely still.

[00:01-00:02.5] Her eyes begin to shift slightly, no longer fixed straight ahead. A subtle glance toward the side. Her mind racing, calculating chances. The wheels turning behind her terrified expression.

[00:02.5-00:04] Her gaze settles on the doorway. A spark of decision forms in her eyes. The terror remains but now mixed with desperate resolve. She's going to run. Camera pushes in slightly on her eyes, capturing that moment of do-or-die determination.

Subtle eye movement, internal calculation, decision forming moment, terror mixed with resolve, desperate hope, tension building

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影脸部特写，眼神从恐惧僵硬到萌生逃跑念头。

（运动描述）
0-1秒：辛月影脸部特写，剑尖在画面边缘可见。她僵住不动，眼睛直视前方，呼吸屏住，完全静止。
1-2.5秒：眼睛开始微微移动，不再死盯着前方。眼神向侧面瞥了一下。大脑飞速运转，计算逃脱的可能性。恐惧的表情下思绪翻涌。
2.5-4秒：目光定格在门口方向。眼中闪过一丝决断的光芒。恐惧仍在，但混合着绝望中的决意。她决定逃跑。镜头推近她的眼睛，捕捉那孤注一掷的决心瞬间。

（场景描述）
破败草屋卧房，剑光映照脸部，门口在画面一侧。

（镜头语言 + 光影 + 氛围）
眼神微动，内心计算，决策形成瞬间，恐惧与决意交织，绝望中的希望，紧张感累积。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **微妙变化**: 眼神变化幅度小但意义重大
- **情绪转折点**: 2.5秒处是决策点

---

## IB-06: 夺门逃跑（4秒）

**起始关键帧**: 辛月影靠在木柱上
**结束关键帧**: 奔向门口，剑刺入木柱

### 动作分解

**阶段1 (0-0.8秒)**: 身体紧绷，准备起跑
**阶段2 (0.8-2秒)**: 突然弹起，全力奔跑
**阶段3 (2-3秒)**: 剑贴着脖颈刺入木柱
**阶段4 (3-4秒)**: 继续冲向门口，动态模糊

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:00.8] Xin Yueying's body tenses against the pillar. Muscles coiling like a spring. Eyes locked on doorway. The split-second before explosive action.

[00:00.8-00:02] She suddenly bolts from the pillar, sprinting toward doorway with everything she has. Body low, arms pumping, dress flowing behind. Pure survival instinct driving her movement.

[00:02-00:03] Almost simultaneously, Shen Qingqi's sword whistles through air. The blade embeds into wooden pillar right where her neck was moments before, with resonating "hum". Sword vibrates. Wood dust scatters.

[00:03-00:04] Xin Yueying continues running, not looking back. Motion blur on her figure. She's almost at the doorway. The sword still vibrating in the pillar behind her. Pure adrenaline-fueled escape.

Explosive action, sudden movement, survival instinct, simultaneous sword throw, motion blur, dynamic action sequence, life-or-death stakes

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影突然起跑夺门，长剑贴着脖颈刺入木柱。

（运动描述）
0-0.8秒：辛月影身体紧绷，肌肉如弹簧般蓄力，眼睛锁定门口。爆发性动作前的最后一瞬。
0.8-2秒：她突然从木柱旁弹起，用尽全力冲向门口。身体前倾，双臂摆动，衣裳在身后飘扬。求生本能驱动每一个动作。
2-3秒：几乎同时，沈清起的长剑呼啸而过。剑刃刺入辛月影脖颈刚才所在位置的木柱，发出"嗡"的共鸣声。剑身振动，木屑飞散。
3-4秒：辛月影继续奔跑，不敢回头。动态模糊的身影。她几乎到达门口。身后的剑仍在木柱中振动。肾上腺素驱动的逃亡。

（场景描述）
破败草屋卧房，从木柱到门口的空间，剑光闪烁。

（镜头语言 + 光影 + 氛围）
爆发性动作，突然起跑，求生本能，剑掷同步，动态模糊，紧张的动作戏，生死一线。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **爆发性加速**: 从静止到全速的瞬间爆发
- **动作同步**: 奔跑与掷剑几乎同时发生

---

## IB-07: 碰撞反弹（4秒）

**起始关键帧**: 辛月影冲出门口
**结束关键帧**: KF-07 撞上霍齐，仰视视角

### 动作分解

**阶段1 (0-1秒)**: 冲出门口，撞上障碍
**阶段2 (1-2秒)**: 身体反弹，抬头仰望
**阶段3 (2-3秒)**: 看清霍齐的面容
**阶段4 (3-4秒)**: 绝望表情定型

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01] Xin Yueying bursts through doorway into cold night air. She slams into something solid - a chest like a wall. Impact stops her momentum completely. Body jolts from collision.

[00:01-00:02] She stumbles back slightly from the impact, then looks up. Camera begins low angle shot, tilting up from her perspective. What she sees makes her freeze.

[00:02-00:03] Low angle view revealing Huo Qi - burly bearded man with bronze skin, round angry bull-like eyes, powerful build. He stands in doorway like a guard dog, arms crossed. Moonlight creates dramatic rim lighting on his silhouette.

[00:03-00:04] The full impact of hopelessness hits Xin Yueying's face. Her escape route completely blocked. Looking up at this imposing figure, all hope draining away. Despair and terror mixing.

Sudden stop, collision impact, low angle reveal, imposing figure, height difference, rim lighting, hopelessness moment

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影冲出门口撞上霍齐，仰视看清阻挡者。

（运动描述）
0-1秒：辛月影冲出门口进入寒冷的夜色中。她撞上一个坚硬的障碍——如墙壁般的胸膛。冲击力完全阻止了她的冲势。身体因碰撞而震颤。
1-2秒：她因撞击而微微后退，然后抬头。镜头开始仰视角度，从她的视角向上摇。她看到的景象让她僵住。
2-3秒：仰视视角揭示霍齐——络腮胡、古铜色皮肤、圆眼怒目如牛、身材魁梧的壮汉。他像看门狗一样站在门口，双臂交叉。月光在他身躯上形成戏剧性的轮廓光。
3-4秒：绝望感完全击中辛月影的脸。她的逃跑路线被完全封锁。仰视这个压迫性的身影，所有希望都在流失。绝望与恐惧交织。

（场景描述）
草屋门外，月光照亮霍齐的剪影，寒冷夜色。

（镜头语言 + 光影 + 氛围）
突然停止，碰撞冲击，仰视揭示，压迫性身影，高度差，轮廓光，绝望时刻。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **急停效果**: 从快速到静止的突然变化
- **揭示节奏**: 霍齐的形象逐步展现

---

## IB-08: 灵机一动（5秒）

**起始关键帧**: 被推回屋内，绝望对视
**结束关键帧**: 眼神一亮，灵机一动

### 动作分解

**阶段1 (0-1.5秒)**: 被推回，踉跄站稳
**阶段2 (1.5-3秒)**: 与沈清起对视，思维飞转
**阶段3 (3-4秒)**: 突然想到什么，眼神开始变化
**阶段4 (4-5秒)**: 灵机一动，眼中亮起希望

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01.5] Xin Yueying stumbles back into the cottage after being shoved by Huo Qi. She nearly falls, catches her balance. Body language shows complete defeat and hopelessness.

[00:01.5-00:03] She looks up and meets Shen Qingqi's eyes. He sits in wheelchair with half-smile, like a lazy cat playing with cornered mouse. Her mind races desperately - there must be a way out.

[00:03-00:04] Something shifts in her expression. A realization forming. She remembers Shen Qingqi is a fugitive, always on edge, paranoid about assassins. A spark of an idea appears.

[00:04-00:05] Her eyes suddenly light up with desperate inspiration. She's going to lie about an assassin to save herself. The transformation from hopeless to calculating hope visible in her face. A tiny spark of life returning to her eyes.

Desperation to inspiration, mind racing, realization moment, idea forming, desperate hope emerging, psychological turning point

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影被推回屋内，绝望中灵机一动。

（运动描述）
0-1.5秒：辛月影被霍齐推回草屋内。她几乎摔倒，勉强站稳。身体语言显示完全的挫败和绝望。
1.5-3秒：她抬头与沈清起对视。他坐在轮椅上似笑非笑，像慵懒的猫逗弄无处可逃的小老鼠。她的大脑飞速运转——必须有出路。
3-4秒：她的表情发生了微妙变化。一个念头正在形成。她想起沈清起是逃犯，总是处于紧张状态，对刺客草木皆兵。一个想法的火花出现。
4-5秒：她的眼睛突然亮起来，灵机一动。她决定编造一个"刺客"的谎言来保全自己。从绝望到计算中的希望，变化清晰可见。眼中重新燃起生命的火花。

（场景描述）
破败草屋卧房，沈清起在轮椅上，昏暗光线。

（镜头语言 + 光影 + 氛围）
从绝望到灵感，思维飞转，醒悟瞬间，想法形成，绝望中的希望萌芽，心理转折点。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **情绪转折**: 从绝望到希望的明显转折
- **思维可视化**: 通过眼神变化表现思维活动

---

## IB-09: 合掌表演（5秒）

**起始关键帧**: 辛月影准备开始表演
**结束关键帧**: KF-09 夸张的合掌震惊姿势

### 动作分解

**阶段1 (0-1秒)**: 深吸一口气，准备表演
**阶段2 (1-2.5秒)**: 双手合掌，"啪"的一声
**阶段3 (2.5-4秒)**: 眼睛瞪大，装作震惊
**阶段4 (4-5秒)**: 嘴巴张开，完整表演姿态

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01] Xin Yueying takes a quick breath, steeling herself for the performance of her life. A moment of preparation, gathering her acting skills.

[00:01-00:02.5] Her hands come together with a loud "smack". Body language suddenly shifts to exaggerated shock and innocence. The performance begins.

[00:02.5-00:04] Her eyes go wide with theatrical shock. Mouth opens in fake surprise. Every gesture exaggerated, like a stage actor playing to the back row. "What? How could it be poison?!"

[00:04-00:05] Full performance mode. Hands still clasped, body language pleading innocence. Voice filled with "indignation" and "wronged innocence". Acting is over-the-top but desperate - her life depends on this performance.

Theatrical performance, exaggerated gestures, fake shock, desperate acting, life-or-death performance, over-the-top innocence

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
辛月影开始她的谎言表演，合掌装作震惊。

（运动描述）
0-1秒：辛月影快速吸一口气，为这场人生中最重要的表演做准备。准备时刻，调动所有演技。
1-2.5秒：双手"啪"地一声合在一起。身体语言突然转变为夸张的震惊和无辜。表演开始。
2.5-4秒：眼睛戏剧性地睁大，嘴巴张开装作惊讶。每个动作都夸张到极点，像舞台演员向后排观众表演。"什么？怎会是一包毒药？！"
4-5秒：完全进入表演模式。双手合十，身体语言恳求无辜。声音充满"愤慨"和"受委屈的无辜"。演技浮夸但全力以赴——她的命就靠这场表演了。

（场景描述）
破败草屋卧房，沈清起在背景中观看。

（镜头语言 + 光影 + 氛围）
戏剧性表演，夸张动作，假装震惊，孤注一掷的演技，生死攸关的表演，浮夸的无辜。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **表演节奏**: 明显的舞台表演节奏
- **夸张动作**: 动作幅度大，有戏剧感

---

## IB-10: 阴鸷转变（5秒）

**起始关键帧**: 沈清起玩味嘲弄
**结束关键帧**: KF-06 阴鸷冷笑

### 动作分解

**阶段1 (0-1.5秒)**: 鼻腔喷笑，玩味表情
**阶段2 (1.5-3秒)**: 笑声戛然而止
**阶段3 (3-4秒)**: 眼神转阴，危险气息
**阶段4 (4-5秒)**: 阴鸷冷笑，画面渐暗

### 提示词

**Veo3.1 Fast 版本**:
```
3D animation style, Chinese Donghua aesthetic,

[00:00-00:01.5] Shen Qingqi's reaction to Xin Yueying's performance. A nasal laugh escapes him. Expression playful and mocking. His phoenix eyes narrow slightly, clearly not believing her lie but finding it entertaining.

[00:01.5-00:03] Suddenly, his laughter stops. The playfulness vanishes from his face. A chill descends. The atmosphere shifts from amusing to dangerous in an instant.

[00:03-00:04] His gaze turns gloomy and menacing. The cold predator beneath the beautiful surface emerges. Thin lips part slightly, but the smile that forms is nothing like warmth - it's pure menace.

[00:04-00:05] Extreme close-up on his phoenix eyes. Vignette effect darkening edges of frame. His chilling voice speaks words that send shivers down the spine. Screen gradually fades darker, leaving ominous suspense.

Playful to dangerous, sudden shift, menacing transformation, ominous atmosphere, suspense building, chilling ending

--aspect_ratio 16:9
```

**可灵动画 版本**:
```
3D动画渲染, 国漫风格, Chinese Donghua Style,

（主体描述）
沈清起从玩味嘲弄转为阴鸷危险的冷笑。

（运动描述）
0-1.5秒：沈清起对辛月影表演的反应。鼻腔里喷出一丝笑意。表情玩味嘲弄。凤眼微眯，明显不信她的谎言但觉得有趣。
1.5-3秒：突然，他的笑声停止。脸上的玩味消失无踪。一股寒意降临。氛围从有趣瞬间转为危险。
3-4秒：眼神变得阴鸷危险。美丽外表下的冷酷猎食者浮现。薄唇轻启，但形成的笑容毫无温暖——纯粹的恶意。
4-5秒：凤眼极度特写。画面边缘渐暗效果（vignette）。他那让人毛骨悚然的声音说出令人胆寒的话。画面逐渐变暗，留下不祥的悬念。

（场景描述）
破败草屋卧房，月光和青灯交织，逐渐变暗。

（镜头语言 + 光影 + 氛围）
从玩味到危险，突然转变，阴鸷蜕变，不祥氛围，悬念累积，令人胆寒的结尾。

精致细节, 流畅动作, 柔和电影级光影, 景深模糊, 8k画质

--aspect_ratio 16:9
```

### 节奏控制
- **情绪突转**: 从玩味到危险的急剧转变
- **悬念积累**: 最后的渐暗效果

---

## 补间动画质量检查清单

### 生成前检查
- [x] 所有补间动画与关键帧衔接
- [x] 动作方向和速度合理
- [x] 表情变化自然流畅
- [x] 节奏控制符合情绪

### 生成后检查
- [ ] 动作流畅无跳跃
- [ ] 表情过渡自然
- [ ] 节奏感正确
- [ ] 与前后视频衔接顺畅

---

## 使用建议

### 与关键帧配合
1. 先生成关键帧图片
2. 按顺序生成补间动画
3. 在后期合成时将关键帧和补间动画拼接

### 平台选择
- **表情变化类**: 推荐 可灵动画 5秒
- **动作过渡类**: 推荐 Veo3.1 Fast 8秒 或 可灵 10秒
- **氛围渲染类**: 两个平台均可

### 时长调整
- 补间动画可根据实际需要调整时长
- 复杂动作可拆分为多个补间
- 简单过渡可缩短至 3 秒

---

*由 AI中间画师 生成*
