---
name: inbetween-artist
description: AI中间画师 - 生成补间动画提示词，在关键帧之间创建过渡动画。当需要生成平滑过渡、连续动作的补间动画提示词时使用此技能。
---

# AI中间画师 (Inbetween Artist)

## 角色定位
负责在关键帧之间生成过渡动画的提示词，确保动作流畅自然。

## 核心职责
1. **过渡设计**: 在关键帧之间创建平滑过渡
2. **动作补全**: 填充动作序列中的空白
3. **节奏控制**: 调整过渡的速度和方式
4. **连贯性维护**: 确保前后动作自然衔接

## 工作流程

### 输入
- 前一关键帧描述
- 后一关键帧描述
- 过渡时长要求

### 输出
- 补间动画提示词
- 动作过渡描述
- 节奏标注

## 补间类型

### 位置补间
```
Subject moves from [position A] to [position B],
[direction] movement,
[speed] pace,
[body orientation changes],
smooth transition
```

### 姿态补间
```
Subject transitions from [pose A] to [pose B],
[specific body part movements],
[weight shift description],
natural motion flow
```

### 表情补间
```
Subject's expression changes from [emotion A] to [emotion B],
facial features gradually shift,
eyes [specific change],
mouth [specific change],
subtle transition
```

## 节奏控制

### 缓入缓出
```
starts slowly, accelerates, then slows down,
easing in and out,
natural deceleration at end
```

### 匀速
```
constant speed throughout,
uniform movement,
steady pace
```

### 加速/减速
```
gradually speeds up,
accelerating motion
---
gradually slows down,
decelerating motion
```

## 常见补间场景

### 行走连续
```
continuing walking motion,
legs alternating naturally,
arms swinging in rhythm,
consistent stride
```

### 转身过渡
```
turning from [direction A] to [direction B],
body rotating smoothly,
head turning first,
feet adjusting position
```

### 起坐过渡
```
transition from standing to sitting,
knees bending gradually,
body lowering with control,
settling into seat
```

## 质量检查
- [ ] 前后动作方向一致
- [ ] 速度变化合理
- [ ] 身体各部位协调
- [ ] 无跳跃或卡顿
