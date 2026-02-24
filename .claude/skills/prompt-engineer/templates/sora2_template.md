# Sora 2 Prompt 模板

## 基础结构

```
[Camera Movement & Shot] + [Scene Description] + [Character Description] + [Action/Motion] + [Atmosphere & Lighting] + [Style & Quality]
```

## 镜头运动模板

### 静止镜头
```
Static shot, fixed camera position, {scene_description}
```

### 推镜头
```
Slow dolly shot pushing forward, camera moves closer to {subject}, from {start_framing} to {end_framing}
```

### 拉镜头
```
Pull back shot, camera retreats from {subject}, revealing more of {environment}
```

### 摇镜头
```
Panning shot, camera pans {left/right} from {start_subject} to {end_subject}
```

### 跟踪镜头
```
Tracking shot following {character} as they {action}
```

### 环绕镜头
```
Orbit shot circling around {subject}, 360-degree view of {description}
```

### 升降镜头
```
Crane shot rising from {low_position} to {high_position}, revealing {environment}
```

### 手持镜头
```
Handheld camera, subtle natural movement, documentary style, {scene_description}
```

## 完整模板

### 对话场景
```
{Camera movement} of {character_a} and {character_b} in {location}. {character_a_description}, {character_a_action}. {character_b_description}, {character_b_action}. {Time_of_day} lighting, {atmosphere_description}. {Dialogue cue}. {Style tags}, cinematic composition, high quality.
```

### 动作场景
```
Dynamic {camera_movement} capturing {action_description}. {character_description} performing {specific_action}. {environment_description}. Fast-paced motion, {impact_moments}. {weather/atmosphere}. {Style tags}, action choreography, motion blur, cinematic quality.
```

### 情感场景
```
Intimate {camera_movement} focusing on {character_name}. {detailed_character_description}. {subtle_expression_change}. {emotion_description}. {lighting_description}. {environment_mood}. {Style tags}, emotional depth, cinematic storytelling, high quality.
```

### 场景建立
```
{Camera_movement} establishing {location_name}. {detailed_environment_description}. {time_of_day}, {weather_conditions}. {atmospheric_elements}. {Style tags}, establishing shot, cinematic scope, detailed environment.
```

## 古风专用模板

### 标准古风场景
```
{Camera movement} of ancient Chinese {location}. {character_description_in_hanfu}. {action_description}. {traditional_architecture_elements}. {time_of_day} {weather}. {atmosphere}. Ancient Chinese setting, traditional aesthetics, anime art style, cinematic lighting, highly detailed, 8K quality.
```

### 夜景烛光
```
{Camera movement} in dimly lit {location} at night. {character_description}. Warm candlelight illumination creating dramatic shadows. {flickering_fire_effect}. {mysterious_atmosphere}. Ancient Chinese interior, chiaroscuro lighting, anime style, atmospheric, 8K.
```

### 武侠动作
```
Dynamic {camera movement} martial arts action. {character_description} wielding {weapon}. {detailed_action_sequence}. {environment_interaction}. {impact_effects}. Wuxia style, fluid motion, anime action, motion blur on fast movements, cinematic choreography, high quality.
```

### 自然风光
```
{Camera movement} of {natural_location}. {season} {time_of_day}. {vegetation_description}. {weather_effects}. {atmospheric_perspective}. Traditional Chinese landscape aesthetic, anime style, painterly quality, cinematic scope, detailed, 8K.
```

## 示例 Prompt

### 示例1：夜晚书房对话
```
A slow cinematic dolly shot pushing into an ancient Chinese study room at night. A young woman in pale green hanfu stands by an ornate wooden window, rain visible outside through the lattice. The camera smoothly approaches her, transitioning from a medium shot to an intimate close-up of her contemplative expression. Warm candlelight from a nearby oil lamp illuminates her face with dramatic shadows. Her black hair is arranged in a simple bun with a jade hairpin. Traditional Chinese interior with wooden bookshelves lined with scrolls. The atmosphere is melancholic and mysterious. Anime art style, highly detailed, cinematic composition, 8K quality.
```

### 示例2：竹林打斗
```
Dynamic handheld shot capturing a martial arts duel in a bamboo forest. A young woman in flowing hanfu wields a flexible sword, performing acrobatic dodges and swift counter-attacks. Her opponent, a masked assassin, strikes with a short blade. The camera follows the fast-paced action with quick pans and slight shakiness. Bamboo leaves swirl around them. Sunlight filters through the canopy creating dappled shadows. Wuxia style choreography, fluid motion, anime action, motion blur on fast movements, dramatic impact frames, cinematic quality.
```

### 示例3：庭院晨景
```
Static wide shot of an ancient Chinese courtyard at dawn. Morning mist lingers among carefully pruned pine trees and ornamental rocks. A young woman in light blue hanfu walks slowly along a stone path, her movements graceful. Soft golden light breaks through the mist, creating ethereal atmosphere. Red wooden corridors frame the scene. A small pond reflects the morning sky. Traditional Chinese garden aesthetic, serene atmosphere, anime style, painterly quality, cinematic scope, highly detailed, 8K.
```

## 参数建议

| 场景类型 | Duration | 建议 |
|----------|----------|------|
| 对话特写 | 3-5s | 缓慢运镜，表情细腻 |
| 动作场面 | 5-10s | 动态运镜，适当慢动作 |
| 场景建立 | 5-8s | 宏大运镜，细节丰富 |
| 情感转变 | 4-6s | 推镜头，捕捉表情变化 |
| 转场过渡 | 2-3s | 简洁流畅 |

## 质量标签

```
必选: masterpiece, best quality, highly detailed
推荐: 8K resolution, cinematic composition, anime style
可选: photorealistic, painterly, artistic
```
