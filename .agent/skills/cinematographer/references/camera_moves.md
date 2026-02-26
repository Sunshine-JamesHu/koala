# 运镜参考手册

## 镜头尺寸 (Shot Size)

### 人物镜头

| 名称 | 缩写 | 取景范围 | 用途 |
|------|------|----------|------|
| Extreme Close-Up | ECU | 眼睛/嘴唇/细节 | 极端情绪、重要细节 |
| Close-Up | CU | 头部 | 情感表达、强调 |
| Medium Close-Up | MCU | 胸部以上 | 对话、反应镜头 |
| Medium Shot | MS | 腰部以上 | 日常对话、标准叙事 |
| Medium Full Shot | MFS | 膝盖以上 | 角色互动、轻微动作 |
| Full Shot | FS | 全身 | 角色展示、服装细节 |
| Long Shot | LS | 全身+部分环境 | 场景关系、动作空间 |
| Extreme Long Shot | ELS | 远景 | 环境主导、史诗感 |

### 镜头尺寸转换

```
ECU ← CU ← MCU ← MS ← MFS ← FS ← LS ← ELS
亲密 ←←←←←←←←←←←←←←←←←←←←←←←←→ 疏离
```

## 镜头角度 (Camera Angle)

| 角度 | 效果 | 心理暗示 | 适用场景 |
|------|------|----------|----------|
| Eye Level | 中性、平等 | 客观、日常 | 标准叙事 |
| High Angle | 俯视 | 弱小、脆弱、被压迫 | 展示困境 |
| Low Angle | 仰视 | 强大、威严、威胁 | 权力展示 |
| Dutch Angle | 倾斜 | 不安、混乱、紧张 | 心理失衡 |
| Bird's Eye | 顶视 | 全知、超然 | 全局视角 |
| Worm's Eye | 极低角度 | 极度威严、巨大 | 巨大威胁 |

## 运镜类型 (Camera Movement)

### 1. 静止 (Static)
- **效果**: 稳定、客观、正式
- **适用**: 正式对话、仪式、庄严场景
- **Prompt**: `static shot, fixed camera, no movement`

### 2. 摇镜头 (Pan)
- **方向**: 左/右
- **效果**: 展示环境、跟随视线、角色入画
- **速度**: 慢(10°/s) - 快(90°/s)
- **Prompt**: `pan left/right, camera pans horizontally`

### 3. 倾斜 (Tilt)
- **方向**: 上/下
- **效果**: 展示高度、角色出场、揭示
- **Prompt**: `tilt up/down, camera tilts vertically`

### 4. 变焦 (Zoom)
- **类型**: 放大/缩小
- **效果**: 强调/揭示，保持距离感
- **与Dolly区别**: 背景压缩感不同
- **Prompt**: `zoom in/out, lens zoom`

### 5. 推拉 (Dolly)
- **方向**: 进/出
- **效果**: 亲密感/疏离感，空间变化
- **Prompt**: `dolly in/out, camera moves forward/backward`

### 6. 跟踪 (Track/Trucking)
- **方向**: 平行/前后
- **效果**: 伴随角色、运动感
- **Prompt**: `tracking shot, camera follows subject`

### 7. 升降 (Crane/Jib)
- **方向**: 上/下
- **效果**: 高度变化、视角切换、宏大感
- **Prompt**: `crane shot, camera rises/lowers`

### 8. 环绕 (Arc/Orbit)
- **方向**: 围绕主体
- **效果**: 多角度展示、史诗感
- **Prompt**: `arc shot, orbit around subject, circling camera`

### 9. 手持 (Handheld)
- **效果**: 真实感、紧张、混乱、纪录片风格
- **参数**: 晃动强度
- **Prompt**: `handheld camera, subtle shake, documentary style`

### 10. 斯坦尼康 (Steadicam)
- **效果**: 流畅运动、稳定
- **适用**: 长镜头、跟随
- **Prompt**: `steadicam, smooth movement, floating camera`

## 运镜组合

### 经典组合

| 名称 | 组合 | 效果 | 示例场景 |
|------|------|------|----------|
| 推+摇 | Dolly + Pan | 进入场景同时展示 | 进入房间 |
| 升+摇 | Crane + Pan | 升高同时环视 | 场景揭示 |
| 跟+推 | Track + Dolly | 跟随并接近 | 追逐后对话 |
| 环绕+推 | Arc + Dolly | 环绕并接近 | 史诗出场 |

### 情绪运镜

| 情绪 | 推荐运镜 | 速度 | 特点 |
|------|----------|------|------|
| 紧张 | Dolly In | 慢 | 缓慢逼近，压迫感 |
| 恐惧 | Handheld | 中 | 不稳定，不安 |
| 悲伤 | Static/Slow Tilt | 很慢 | 凝重，仪式感 |
| 快乐 | Track | 中快 | 流畅，轻盈 |
| 愤怒 | Quick Dolly/Zoom | 快 | 冲击力 |
| 惊讶 | Snap Dolly | 很快 | 突然 |
| 浪漫 | Arc/Slow Dolly | 很慢 | 优雅，仪式感 |
| 史诗 | Crane/Arc | 慢 | 宏大，壮阔 |

## 转场类型

| 类型 | 效果 | 适用 |
|------|------|------|
| Cut | 即时切换 | 标准转场 |
| Fade In/Out | 渐变 | 时间流逝 |
| Dissolve | 叠化 | 柔和过渡 |
| Wipe | 擦除 | 动态转场 |
| Match Cut | 匹配剪辑 | 视觉关联 |
| Jump Cut | 跳跃剪辑 | 时间压缩 |
| Iris | 圆形淡入淡出 | 复古风格 |

## 构图法则

### 三分法 (Rule of Thirds)
- 主体置于交点
- 地平线在1/3或2/3处
- Prompt: `rule of thirds composition`

### 黄金分割 (Golden Ratio)
- 1:1.618 比例
- 更优雅的三分法变体
- Prompt: `golden ratio composition`

### 对称构图 (Symmetry)
- 中轴对称
- 仪式感、庄严
- Prompt: `symmetrical composition, centered`

### 引导线 (Leading Lines)
- 线条引导视线
- 深度感
- Prompt: `leading lines composition`

### 框架构图 (Frame within Frame)
- 前景框住主体
- 层次感
- Prompt: `framed composition, frame within frame`

## 运镜速度参考

| 速度 | 描述 | 移动量 | 适用 |
|------|------|--------|------|
| 很慢 | 庄严、仪式 | 0.5m/s | 情感场景 |
| 慢 | 优雅、舒适 | 1m/s | 标准叙事 |
| 中 | 自然、流畅 | 1.5m/s | 日常场景 |
| 快 | 紧迫、兴奋 | 2m/s+ | 动作场面 |
| 很快 | 冲击、紧张 | 3m/s+ | 高潮场面 |

## Prompt 模板

### 基础运镜描述
```
{Speed} {movement_type} shot, {start_framing} to {end_framing}, {subject_description}, {additional_notes}
```

### 完整镜头描述
```
{Speed} {movement_type} shot {movement_direction}. Camera {detailed_movement_description}. {Start_framing} of {start_subject}, transitioning to {end_framing} of {end_subject}. {Composition_notes}, {depth_of_field_notes}.
```

### 示例
```
Slow dolly in shot pushing forward. Camera smoothly approaches from a medium shot to a close-up. Starting with a young woman in hanfu standing by a window, transitioning to an intimate close-up of her contemplative expression. Rule of thirds composition, shallow depth of field, focus locked on subject.
```
