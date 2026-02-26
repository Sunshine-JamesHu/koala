# Shot 009 - 完整生成指南

## 分镜信息
- **分镜ID**: shot_009
- **时长**: 12秒
- **剧情**: 辛月影灵机一动，编造被神秘人威胁才下毒的谎言

---

## 生成顺序

```
步骤1: 场景背景图 (纯场景，无人物)
    ↓
步骤2: 角色参考图 (辛月影 + 沈清起)
    ↓
步骤3: 关键帧图片 (使用场景+角色进行图生图)
    ↓
步骤4: 视频生成 (首尾帧图生视频)
```

---

## 步骤1: 场景背景图

> 生成纯场景图，用于后续关键帧的背景参考

### 场景: 破旧房屋内部 (夜间)

**Prompt**:
```
Ancient Chinese dilapidated house interior at night, empty room with no people, cracked earthen walls with peeling plaster, worn wooden beams overhead with hanging cobwebs, broken window lattice with torn paper, worn uneven wooden floor boards, single bronze oil lamp on small wooden table in corner flickering with warm amber light, dusty atmosphere, deep shadows in corners, cold blue-grey atmosphere with warm amber candlelight accent from the lamp, ancient Chinese architecture in disrepair, border town poverty setting, anime art style background, cinematic lighting, dramatic chiaroscuro, environment concept art, 16:9 aspect ratio, masterpiece, best quality, highly detailed, 8k resolution --ar 16:9 --niji 6
```

**Negative**:
```
people, characters, faces, figures, human, person, bright lighting, modern elements, western style, furniture in good condition, clean, colorful, low quality
```

**生成说明**:
- 这张图将作为所有关键帧的**场景底图**
- 用ControlNet或图生图功能保持场景一致性
- 建议生成后保存为 `scene_破旧房屋_夜.png`

---

## 步骤2: 角色参考图

> 生成角色设计图，用于保持人物一致性

### 角色A: 辛月影 (全身设定图)

**Prompt**:
```
Character design sheet of young Chinese woman named Xin Yueying, full body view, early 20s, delicate beautiful features, pale skin, long flowing black hair, hazel eyes, slender elegant figure, wearing faded green traditional Chinese ruqun cross-collar dress with long sleeves, slightly disheveled and dust-stained, standing pose with hands clasped in front, multiple angles: front view, side view, three-quarter view, expression showing intelligence and vulnerability, ancient Chinese anime style, character concept art, clean white background, reference sheet layout, masterpiece, best quality, consistent character design --ar 3:4 --niji 6
```

**Negative**:
```
multiple different people, background scenery, complex background, modern clothes, western style, ugly, deformed, low quality, blurry, dark lighting
```

**生成说明**:
- 这是角色设定参考图，用于后续保持角色一致
- 建议保存为 `char_辛月影_设定.png`

---

### 角色B: 沈清起 (轮椅设定图)

**Prompt**:
```
Character design of young Chinese man named Shen Qingqi sitting in old wooden wheelchair, full body view, 22 years old, pale sickly complexion, sharp angular face, narrow suspicious phoenix eyes with cold gaze, thin pale lips, long disheveled black hair, wearing worn black traditional Chinese robe with long sleeves, hands resting on bronze sword across his lap, old wooden wheelchair with rusty wheels and torn cushion, ancient Chinese anime style, character concept art, clean background, masterpiece, best quality, consistent character design, menacing yandere aura --ar 3:4 --niji 6
```

**Negative**:
```
standing pose, healthy complexion, friendly expression, modern clothes, western style, clean new wheelchair, ugly, deformed, low quality, blurry
```

**生成说明**:
- 包含轮椅的完整设定图
- 建议保存为 `char_沈清起_轮椅设定.png`

---

## 步骤3: 关键帧图片 (图生图)

> 使用场景图 + 角色图作为参考，生成3张关键帧

### 参考图片输入:
- **场景底图**: `scene_破旧房屋_夜.png`
- **角色参考**: `char_辛月影_设定.png` + `char_沈清起_轮椅设定.png`

---

### Frame 1 - 首帧 (0秒)

**构图**: 中近景双人镜头，辛月影跪地右侧，沈清起坐轮椅左侧，烛光在中间

**Prompt** (图生图):
```
Medium close two-shot, ancient Chinese dilapidated room interior at night. RIGHT SIDE: young Chinese woman Xin Yueying kneeling on worn wooden floor, wearing faded green traditional ruqun dress, face showing desperate determination as she begins to stand up. LEFT SIDE: pale young man Shen Qingqi sitting in old wooden wheelchair, wearing worn black robe, holding bronze sword pointing at her, cold suspicious narrowed phoenix eyes. Single bronze oil lamp flickering between them creating dramatic chiaroscuro shadows. Cold blue-grey atmosphere with warm amber candlelight accent. Ancient Chinese anime style, tense life-or-death standoff. Reference scene background and character designs provided. Masterpiece, best quality, highly detailed, 8k resolution, cinematic composition --ar 16:9
```

**图生图设置**:
- Denoising strength: 0.5-0.6
- ControlNet: 使用场景图作为depth/canny参考

---

### Frame 2 - 中间帧 (6秒)

**构图**: 中近景双人镜头，辛月影已站直身体，沈清起剑势略低

**Prompt** (图生图):
```
Medium close two-shot, same ancient Chinese dilapidated room interior. RIGHT SIDE: young Chinese woman Xin Yueying now standing upright, wearing faded green ruqun, leaning forward slightly, speaking urgently with calculated sincerity, face half-illuminated by warm candlelight showing feigned vulnerability. LEFT SIDE: pale young man Shen Qingqi in old wooden wheelchair, wearing worn black robe, bronze sword now slightly lowered, suspicious phoenix eyes narrowed in thought as he listens. Bronze oil lamp between them casting dramatic chiaroscuro. Same scene background, same character designs. Masterpiece, best quality, highly detailed, 8k resolution --ar 16:9
```

---

### Frame 3 - 尾帧 (12秒)

**构图**: 中近景双人镜头，两人距离感缩短，对角线构图

**Prompt** (图生图):
```
Medium close two-shot, same ancient Chinese dilapidated room. RIGHT SIDE: young Chinese woman Xin Yueying in faded green ruqun leaning forward earnestly, eyes showing desperate sincerity, calculated performance at peak. LEFT SIDE: pale young man Shen Qingqi in wheelchair, bronze sword noticeably lowered to his side, suspicious phoenix eyes showing first signs of consideration, cold menace slightly softening. Bronze oil lamp creating more balanced warm illumination on both faces, shadows between them beginning to fade. Same scene background, same character designs. Narrative turning point moment. Masterpiece, best quality, highly detailed, 8k resolution --ar 16:9
```

---

## 步骤4: 视频生成

### Video 1: Frame 1 → Frame 2 (6秒)

**输入图片**: 首帧图 + 尾帧图

**Prompt**:
```
Slow subtle dolly in, young Chinese woman in green dress slowly rising from kneeling to standing position while speaking urgently, her expression shifting from desperate to determined, pale man in wheelchair starting to lower his sword slightly, candlelight flickering between them casting moving shadows, ancient Chinese anime style, tense psychological standoff, 6 seconds, slow ease-in-out cinematic movement
```

---

### Video 2: Frame 2 → Frame 3 (6秒)

**输入图片**: 首帧图 + 尾帧图

**Prompt**:
```
Continuing slow dolly in, young Chinese woman in green dress leaning forward more earnestly with pleading expression, pale man in wheelchair lowering his sword further to his side, his suspicious eyes gradually softening with consideration, candlelight becoming more balanced and warm, shadows softening between them, subtle power shift moment, ancient Chinese anime style, psychological persuasion climax, 6 seconds, slow ease-in-out cinematic movement
```

---

## 一键复制汇总

### 场景背景图
```
Ancient Chinese dilapidated house interior at night, empty room with no people, cracked earthen walls with peeling plaster, worn wooden beams overhead with hanging cobwebs, broken window lattice with torn paper, worn uneven wooden floor boards, single bronze oil lamp on small wooden table in corner flickering with warm amber light, dusty atmosphere, deep shadows in corners, cold blue-grey atmosphere with warm amber candlelight accent from the lamp, ancient Chinese architecture in disrepair, border town poverty setting, anime art style background, cinematic lighting, dramatic chiaroscuro, environment concept art, 16:9 aspect ratio, masterpiece, best quality, highly detailed, 8k resolution --ar 16:9 --niji 6
```

### 角色A: 辛月影
```
Character design sheet of young Chinese woman named Xin Yueying, full body view, early 20s, delicate beautiful features, pale skin, long flowing black hair, hazel eyes, slender elegant figure, wearing faded green traditional Chinese ruqun cross-collar dress with long sleeves, slightly disheveled and dust-stained, standing pose with hands clasped in front, multiple angles: front view side view three-quarter view, expression showing intelligence and vulnerability, ancient Chinese anime style, character concept art, clean white background, reference sheet layout, masterpiece, best quality, consistent character design --ar 3:4 --niji 6
```

### 角色B: 沈清起
```
Character design of young Chinese man named Shen Qingqi sitting in old wooden wheelchair, full body view, 22 years old, pale sickly complexion, sharp angular face, narrow suspicious phoenix eyes with cold gaze, thin pale lips, long disheveled black hair, wearing worn black traditional Chinese robe with long sleeves, hands resting on bronze sword across his lap, old wooden wheelchair with rusty wheels and torn cushion, ancient Chinese anime style, character concept art, clean background, masterpiece, best quality, consistent character design, menacing yandere aura --ar 3:4 --niji 6
```

### 首帧关键帧 (图生图)
```
Medium close two-shot, ancient Chinese dilapidated room interior at night. RIGHT SIDE: young Chinese woman Xin Yueying kneeling on worn wooden floor, wearing faded green traditional ruqun dress, face showing desperate determination as she begins to stand up. LEFT SIDE: pale young man Shen Qingqi sitting in old wooden wheelchair, wearing worn black robe, holding bronze sword pointing at her, cold suspicious narrowed phoenix eyes. Single bronze oil lamp flickering between them creating dramatic chiaroscuro shadows. Cold blue-grey atmosphere with warm amber candlelight accent. Ancient Chinese anime style, tense life-or-death standoff. Reference scene background and character designs provided. Masterpiece, best quality, highly detailed, 8k resolution, cinematic composition --ar 16:9
```

### 尾帧关键帧 (图生图)
```
Medium close two-shot, same ancient Chinese dilapidated room. RIGHT SIDE: young Chinese woman Xin Yueying in faded green ruqun leaning forward earnestly, eyes showing desperate sincerity, calculated performance at peak. LEFT SIDE: pale young man Shen Qingqi in wheelchair, bronze sword noticeably lowered to his side, suspicious phoenix eyes showing first signs of consideration, cold menace slightly softening. Bronze oil lamp creating more balanced warm illumination on both faces, shadows between them beginning to fade. Same scene background, same character designs. Narrative turning point moment. Masterpiece, best quality, highly detailed, 8k resolution --ar 16:9
```

### 图生视频
```
Slow dolly in two-shot, young Chinese woman in green dress rising from kneeling to standing while speaking urgently, leaning forward with pleading expression, pale man in wheelchair lowering his sword from threatening to relaxed position, his suspicious eyes softening with consideration, bronze oil lamp flickering between them, dramatic chiaroscuro shadows gradually softening, ancient Chinese anime style, psychological persuasion turning point, 12 seconds total, slow ease-in-out cinematic movement
```
