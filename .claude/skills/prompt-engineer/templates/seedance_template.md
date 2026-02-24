# SeeDance 2.0 Prompt 模板

## 特点

- 支持中英文双语
- 对古风/国风理解优秀
- 适合细节丰富的描述
- 支持角色一致性控制

## 中文模板

### 基础结构
```
[镜头描述] + [场景描述] + [角色描述] + [动作描述] + [氛围描述] + [风格标签]
```

### 对话场景
```
{镜头运动}。{场景位置}，{时间}。{角色A描述}，{角色A动作}。{角色B描述}，{角色B动作}。{光线描述}，{氛围}。古风动漫风格，高画质。
```

### 动作场景
```
{镜头运动}。{场景描述}。{角色描述}{进行什么动作}。{动作细节}。{环境互动}。{特效描述}。武侠风格，动漫动作场面，动态构图，高画质。
```

### 情感场景
```
{镜头运动}，聚焦于{角色名}。{角色详细描述}。{表情变化}。{情感描述}。{光线氛围}。古风动漫风格，细腻情感，电影感，高画质。
```

## 英文模板

### 基础结构
```
[Camera Movement] + [Scene Setup] + [Character Description] + [Action/Motion] + [Atmosphere] + [Style Tags]
```

### 完整模板
```
{Camera movement} shot in {location}. {Time_of_day}, {weather}. {Character_description}, {character_action}. {Lighting_description}, creating {atmosphere}. {Style_tags}, high quality, detailed.
```

## 古风专用模板

### 标准古风 (中文)
```
{镜头运动}。古代{场景类型}，{场景细节}。{角色名}，{年龄}岁，{外貌描述}，身穿{服装描述}，{配饰描述}。{动作描述}。{时间}，{天气}，{光线}。{氛围情绪}。古风动漫风格，精细画面，电影级构图。
```

### 夜景烛光 (中文)
```
{镜头运动}。{场景}，夜晚，烛光照明。{角色描述}，{动作}。烛火摇曳，明暗对比强烈，影子在墙上晃动。{氛围}。古风动漫风格，戏剧性光影，高画质。
```

### 武侠动作 (中文)
```
{镜头运动}。{场景描述}。{角色A描述}手持{武器}，{动作描述}。{角色B描述}{反应动作}。{招式碰撞}，{特效}。{环境影响}。武侠动漫风格，流畅动作，动态画面，高画质。
```

## 示例 Prompt

### 示例1：夜晚书房 (中文)
```
缓慢推镜头。古代中式书房，夜晚，窗外细雨。辛月影，十八岁少女，纤细身材，肤白如雪，杏眼柳眉，乌黑长发盘成简单发髻。身穿淡青色襦裙，白色内衬，浅碧色披帛，佩戴玉簪。立于雕花窗前，凝视窗外，若有所思。烛光摇曳，明暗对比强烈，营造神秘忧郁氛围。古风动漫风格，精细画面，电影级构图，8K画质。
```

### 示例2：夜晚书房 (英文)
```
Slow dolly in shot. Ancient Chinese study room, night, rain visible outside through lattice window. A young woman, 18 years old, slender figure, fair skin, almond eyes, willow eyebrows, black hair in simple bun with jade hairpin. Wearing pale green ruqun dress, white inner robe, light blue pibo shawl. Standing by carved wooden window, gazing outside contemplatively. Flickering candlelight creates dramatic shadows, mysterious and melancholic atmosphere. Ancient Chinese anime style, detailed, cinematic composition, 8K quality.
```

### 示例3：竹林打斗 (中文)
```
动态跟随镜头。竹林深处，阳光透过竹叶。辛月影，身穿淡青色襦裙，手持软剑，轻盈闪避，剑走龙蛇。刺客黑衣蒙面，手持短刀，猛力劈砍。软剑与短刀相撞，火花四溅，竹叶纷飞。竹子被剑气斩断，落叶飘散。武侠动漫风格，流畅动作，动态画面，高画质。
```

### 示例4：庭院晨景 (中文)
```
静止广角镜头。古代中式庭院，清晨，薄雾笼罩。青松翠竹环绕，假山池塘，石板小径。辛月影，身穿浅蓝色襦裙，缓步沿石径行走，姿态优雅。晨光穿过薄雾，金色光线，空灵氛围。古风园林美学，宁静祥和，动漫风格，水墨质感，电影级画面。
```

## 关键词对照表

| 中文 | 英文 |
|------|------|
| 镜头推进 | dolly in, push in |
| 镜头拉远 | dolly out, pull back |
| 跟随镜头 | tracking shot, follow shot |
| 环绕镜头 | orbit shot, circling camera |
| 升降镜头 | crane shot |
| 手持镜头 | handheld, shaky |
| 静止镜头 | static shot, fixed camera |
| 缓慢 | slow, gradual |
| 快速 | fast, quick |
| 古风 | ancient Chinese style |
| 武侠 | wuxia, martial arts |
| 襦裙 | ruqun, traditional dress |
| 烛光 | candlelight |
| 明暗对比 | chiaroscuro, dramatic shadows |

## 质量标签

### 中文
```
必选: 高画质, 精细画面
推荐: 电影级构图, 动漫风格
可选: 水墨质感, 工笔画风格
```

### 英文
```
必选: high quality, detailed
推荐: cinematic composition, anime style
可选: painterly, artistic
```

## 参数建议

| 场景 | creativity | consistency |
|------|------------|-------------|
| 对话 | 0.6 | 0.8 |
| 动作 | 0.7 | 0.7 |
| 情感 | 0.5 | 0.85 |
| 场景 | 0.7 | 0.6 |

## 角色一致性控制

使用固定角色标签：
```
(角色名: 同一角色设计, 外貌一致, 服装一致)
```

示例：
```
(辛月影: 年轻女子, 淡青襦裙, 玉簪, 乌黑长发)
```
