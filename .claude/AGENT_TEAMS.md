# 漫剧 Agent Teams 架构设计

## 核心目标

**将小说章节转化为 AI 视频生成所需的完整素材和 Prompt**

最终输出：
- 关键帧图片 + 关键帧 Prompt
- 场景图片 + 运镜描述
- 角色图片（四视图）
- 视频 Prompt（用于 Sora2 / SeeDance2.0）

---

## 架构概览

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Agent Teams 架构                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   输入层    │───▶│   分析层    │───▶│   设计层    │───▶│   生成层    │ │
│  │  小说章节   │    │  故事分析   │    │  资源设计   │    │  Prompt生成 │ │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent 定义

### Layer 1: 分析层 (Analysis)

#### 1. StoryAnalyzer - 故事分析师
**职责**: 深度分析小说章节，提取核心叙事元素

**输入**:
- 章节文本 (`chapter_XXX.txt`)
- 项目上下文 (`project.json`)

**输出**: `analysis_result.json`
```json
{
  "chapter_id": "chapter_001",
  "summary": "章节摘要",
  "key_events": [
    {
      "event_id": "evt_001",
      "type": "dialogue|action|revelation|conflict|resolution",
      "description": "事件描述",
      "characters": ["角色1", "角色2"],
      "emotion": "emotional_state",
      "importance": 1-10
    }
  ],
  "character_arcs": {
    "角色名": {
      "state_before": "状态变化前",
      "state_after": "状态变化后",
      "key_moment": "关键时刻"
    }
  },
  "locations": ["场景1", "场景2"],
  "mood_curve": [
    {"position": 0.0, "intensity": 0.5, "emotion": "calm"},
    {"position": 0.5, "intensity": 0.9, "emotion": "tense"}
  ],
  "conflicts": ["冲突1", "冲突2"],
  "resolutions": ["解决1"]
}
```

**Skill 文件**: `.claude/skills/story-analyzer/`

---

#### 2. EmotionAnalyzer - 情绪分析师
**职责**: 分析情感曲线，为配乐、运镜提供情绪参考

**输入**:
- `analysis_result.json`

**输出**: `emotion_map.json`
```json
{
  "chapter_id": "chapter_001",
  "emotion_timeline": [
    {
      "segment_id": "seg_001",
      "start": 0,
      "end": 100,
      "primary_emotion": "anxious",
      "secondary_emotion": "hopeful",
      "intensity": 0.7,
      "color_mood": "冷色调偏蓝",
      "bgm_suggestion": "悬疑紧张类",
      "camera_style": "手持晃动，不安定感"
    }
  ],
  "emotion_peaks": [
    {"position": 0.3, "type": "tension_build"},
    {"position": 0.7, "type": "climax"}
  ]
}
```

**Skill 文件**: `.claude/skills/emotion-analyzer/`

---

### Layer 2: 设计层 (Design)

#### 3. StoryDirector - 分镜导演
**职责**: 将故事转化为分镜脚本，决定镜头切分

**输入**:
- `analysis_result.json`
- `emotion_map.json`

**输出**: `storyboard.json` (增强版)
```json
{
  "episode": 1,
  "title": "第1集 初遇",
  "total_shots": 12,
  "shots": [
    {
      "shot_id": "shot_001",
      "beat_type": "opening|rising|climax|falling|resolution",
      "duration": 5.0,
      "narrative_beat": "故事节拍描述",
      "scene": {
        "location_id": "loc_001",
        "location_name": "书房内",
        "time_of_day": "night",
        "weather": "rain",
        "lighting": "昏暗烛光",
        "atmosphere": "压抑紧张"
      },
      "camera": {
        "shot_size": "extreme_close_up|close_up|medium_close|medium|medium_full|full|long|extreme_long",
        "angle": "eye_level|high|low|dutch|birds_eye|worms_eye",
        "movement": "static|pan_left|pan_right|tilt_up|tilt_down|zoom_in|zoom_out|dolly_in|dolly_out|track|crane|handheld",
        "movement_speed": "slow|medium|fast",
        "framing_note": "构图说明"
      },
      "characters": [
        {
          "character_id": "char_001",
          "name": "辛月影",
          "position": "frame_left|frame_center|frame_right",
          "blocking": "站立窗前",
          "expression": "焦虑",
          "action": "来回踱步",
          "costume_version": "costume_001"
        }
      ],
      "dialogue": {
        "speaker": "辛月影",
        "text": "这究竟是怎么回事...",
        "delivery_style": "自言自语，低沉",
        "subtitle_style": "底部居中白色"
      },
      "narration": {
        "text": "穿越第三天，辛月影终于意识到...",
        "voice_style": "冷静旁白"
      },
      "sfx": [
        {"type": "rain", "intensity": "medium", "file": "assets/audio/sfx/rain_light.wav"}
      ],
      "bgm": {
        "track": "assets/audio/bgm/suspense_low.mp3",
        "volume": 0.3,
        "fade_type": "in|out|crossfade"
      },
      "transition": {
        "type": "cut|fade|dissolve|wipe|match_cut",
        "duration": 0.5
      },
      "keyframe_description": "关键帧画面描述",
      "notes": "导演备注"
    }
  ]
}
```

**Skill 文件**: `.claude/skills/story-director/`

---

#### 4. CharacterDesigner - 角色设计师
**职责**: 设计角色服化造（服装、化妆、造型）

**输入**:
- 角色基础信息
- 场景需求
- 情绪状态

**输出**: `character_design.json`
```json
{
  "character_id": "char_001",
  "name": "辛月影",
  "base_info": {
    "gender": "女性",
    "age": 18,
    "body_type": "纤细",
    "height": "165cm"
  },
  "face": {
    "skin_tone": "雪白",
    "face_shape": "鹅蛋脸",
    "eyes": "杏眼，瞳色深棕，眼神灵动",
    "eyebrows": "柳叶眉，淡黑",
    "nose": "小巧挺拔",
    "lips": "樱桃小口，唇色淡粉"
  },
  "hair": {
    "style": "长发及腰",
    "color": "乌黑如墨",
    "arrangement": "简单发髻，几缕碎发垂落"
  },
  "costumes": [
    {
      "costume_id": "costume_001",
      "name": "日常居家服",
      "era": "古代",
      "season": "春秋",
      "description": "淡青色襦裙，白色内衬，浅碧色披帛",
      "color_palette": ["#E8F5E9", "#B2DFDB", "#FAFAFA"],
      "accessories": [
        {"type": "发簪", "description": "简单玉簪", "color": "白玉色"},
        {"type": "腰佩", "description": "香囊", "color": "淡绿"}
      ],
      "prompt_template": "古代少女，身穿淡青色襦裙..."
    }
  ],
  "expressions": {
    "neutral": "平静自然",
    "happy": "眉眼弯弯，嘴角上扬",
    "sad": "眼眶微红，泪光闪烁",
    "angry": "眉头紧蹙，眼神凌厉",
    "surprised": "双眼圆睁，微微张嘴",
    "determined": "目光坚定，抿唇"
  },
  "poses": ["站立", "坐姿", "行走", "跪坐", "奔跑"]
}
```

**Skill 文件**: `.claude/skills/character-designer/`

---

#### 5. SceneDesigner - 场景设计师
**职责**: 设计场景背景，确保风格统一

**输入**:
- 分镜脚本中的场景需求
- 项目风格设定

**输出**: `scene_design.json`
```json
{
  "location_id": "loc_001",
  "name": "辛府书房",
  "type": "indoor",
  "era": "古代",
  "time_periods": {
    "day": {
      "lighting": "自然光从窗棂透入",
      "atmosphere": "明亮静谧",
      "color_temperature": "暖色"
    },
    "night": {
      "lighting": "烛光摇曳",
      "atmosphere": "昏暗神秘",
      "color_temperature": "冷色偏橙"
    }
  },
  "architecture": {
    "style": "古代中式",
    "materials": ["木质", "纸窗", "青砖"],
    "key_elements": [
      {"name": "书架", "description": "红木书架，摆满古籍", "position": "左侧"},
      {"name": "书桌", "description": "紫檀木书桌，笔墨纸砚", "position": "中央"},
      {"name": "窗棂", "description": "雕花木窗，糊白纸", "position": "后方"}
    ]
  },
  "props_placement": [
    {"prop_id": "prop_001", "name": "油灯", "position": "书桌右上角"}
  ],
  "color_palette": {
    "primary": "#8B4513",
    "secondary": "#DEB887",
    "accent": "#2F4F4F"
  },
  "prompt_template": "古代中式书房 interior，木质书架..."
}
```

**Skill 文件**: `.claude/skills/scene-designer/`

---

#### 6. PropDesigner - 道具设计师
**职责**: 设计关键道具

**输出**: `prop_design.json`
```json
{
  "prop_id": "prop_001",
  "name": "玉佩",
  "category": "饰品|武器|器物|文献|食物",
  "importance": "key|secondary|background",
  "description": "白玉质，刻有家族纹章",
  "dimensions": "5cm x 3cm",
  "color": ["#F5F5F5", "#90EE90"],
  "material": "白玉",
  "views": {
    "front": "正面视图描述",
    "side": "侧面视图描述",
    "detail": "细节特写描述"
  },
  "prompt_template": "白玉玉佩，古代饰品..."
}
```

**Skill 文件**: `.claude/skills/prop-designer/`

---

#### 7. ActionDesigner - 动作设计师
**职责**: 设计打斗、动作场面

**输入**:
- 分镜脚本中的动作镜头
- 角色能力设定

**输出**: `action_design.json`
```json
{
  "action_id": "action_001",
  "shot_id": "shot_005",
  "type": "combat|chase|escape|performance|daily",
  "intensity": "low|medium|high|extreme",
  "participants": [
    {"character_id": "char_001", "role": "attacker|defender|observer"},
    {"character_id": "char_002", "role": "defender"}
  ],
  "choreography": [
    {
      "beat": 1,
      "time": "0:00-0:02",
      "character": "char_001",
      "action": "右手拔剑，向左前方刺出",
      "camera": "跟随剑锋特写",
      "sfx": "剑出鞘声"
    },
    {
      "beat": 2,
      "time": "0:02-0:04",
      "character": "char_002",
      "action": "侧身闪避，同时右掌推出",
      "camera": "广角中景",
      "sfx": "掌风声"
    }
  ],
  "key_poses": [
    {"beat": 1, "description": "拔剑瞬间", "keyframe_id": "kf_001"},
    {"beat": 2, "description": "闪避推掌", "keyframe_id": "kf_002"}
  ],
  "environment_interaction": [
    "剑气划破书桌上的纸张",
    "掌风吹灭烛火"
  ],
  "prompt_enhancements": "武打动作参考，剑术..."
}
```

**Skill 文件**: `.claude/skills/action-designer/`

---

### Layer 3: 生成层 (Generation)

#### 8. Cinematographer - 运镜师
**职责**: 设计专业运镜，增强视觉叙事

**输出**: `camera_work.json`
```json
{
  "shot_id": "shot_001",
  "camera_plan": {
    "start_frame": {
      "shot_size": "long_shot",
      "angle": "eye_level",
      "position": "门外，透过窗框",
      "subject": "辛月影全身，书房全景"
    },
    "end_frame": {
      "shot_size": "close_up",
      "angle": "slightly_low",
      "position": "室内，正对脸部",
      "subject": "辛月影脸部特写"
    },
    "movement": {
      "type": "dolly_in",
      "path": "直线推进，穿窗入室",
      "speed_curve": "ease_in_out",
      "duration": 5.0
    },
    "focus": {
      "type": "rack_focus",
      "start_focus": "窗框前景虚化",
      "end_focus": "人物脸部清晰"
    }
  },
  "visual_effects": [
    {"type": "depth_of_field", "aperture": "f/1.8"},
    {"type": "motion_blur", "intensity": "subtle"}
  ],
  "reference_style": "王家卫式缓慢推进",
  "video_prompt": "Slow dolly shot pushing through window frame into a dimly lit ancient Chinese study..."
}
```

**Skill 文件**: `.claude/skills/cinematographer/`

---

#### 9. KeyframeExtractor - 关键帧提取师
**职责**: 提取并描述关键帧，生成图像 Prompt

**输出**: `keyframes.json`
```json
{
  "shot_id": "shot_001",
  "keyframes": [
    {
      "keyframe_id": "kf_001",
      "position": 0.0,
      "type": "start|peak|transition|end",
      "description": "镜头起始画面",
      "scene_elements": {
        "background": "古代书房，窗外雨夜",
        "characters": [
          {
            "name": "辛月影",
            "position": "frame_center",
            "pose": "站立窗前，双手交叠",
            "expression": "凝视窗外",
            "costume": "costume_001"
          }
        ],
        "props": ["油灯", "书卷"],
        "lighting": "昏暗烛光，窗外雨影"
      },
      "composition": {
        "rule": "rule_of_thirds",
        "focus_point": "人物侧脸",
        "depth_layers": ["前景:窗框", "中景:人物", "背景:书架"]
      },
      "image_prompt": "Ancient Chinese study at night, rainy atmosphere through window, young woman in pale green hanfu standing by window, candlelight illumination, dramatic shadows, anime style, cinematic composition, 8k, masterpiece"
    },
    {
      "keyframe_id": "kf_002",
      "position": 1.0,
      "type": "end",
      "description": "镜头结束画面",
      "image_prompt": "Close-up of young woman's face, ancient Chinese beauty, candlelit, rain reflection in eyes, anime style, emotional expression, 8k, masterpiece"
    }
  ]
}
```

**Skill 文件**: `.claude/skills/keyframe-extractor/`

---

#### 10. PromptEngineer - Prompt 工程师
**职责**: 整合所有元素，生成最终视频 Prompt

**输入**:
- 所有的设计 JSON
- 风格参考

**输出**: `video_prompts.json`
```json
{
  "shot_id": "shot_001",
  "target_model": "Sora2|SeeDance2.0|Kling",
  "prompts": {
    "image_generation": {
      "start_frame": "生成起始帧的完整 Prompt",
      "end_frame": "生成结束帧的完整 Prompt",
      "style_reference": "风格参考图路径"
    },
    "video_generation": {
      "primary_prompt": "用于视频生成的主体 Prompt",
      "motion_description": "运镜和动作描述",
      "character_reference": ["角色参考图路径"],
      "scene_reference": ["场景参考图路径"],
      "negative_prompt": "负面提示词",
      "parameters": {
        "duration": 5.0,
        "fps": 24,
        "aspect_ratio": "16:9",
        "style_strength": 0.8
      }
    }
  },
  "full_video_prompt": "A cinematic slow dolly shot pushing through an ancient wooden window frame into a dimly lit Chinese study room. Rain falls outside. A young woman in pale green hanfu stands by the window, her face illuminated by flickering candlelight. The camera slowly approaches her, transitioning from a full-body long shot to an intimate close-up of her contemplative expression. Traditional Chinese interior, bookshelves with ancient scrolls, dramatic chiaroscuro lighting, anime art style, 8K resolution, cinematic composition."
}
```

**Skill 文件**: `.claude/skills/prompt-engineer/`

---

## Agent 协作流程

```
                    ┌─────────────────────────────────────────┐
                    │           用户输入: 章节                 │
                    └────────────────┬────────────────────────┘
                                     │
          ┌──────────────────────────┼──────────────────────────┐
          ▼                          ▼                          │
┌─────────────────┐      ┌─────────────────┐                    │
│ StoryAnalyzer   │      │ EmotionAnalyzer │                    │
│ 故事分析师       │      │ 情绪分析师       │                    │
└────────┬────────┘      └────────┬────────┘                    │
         │                        │                             │
         └────────────┬───────────┘                             │
                      ▼                                         │
          ┌───────────────────────┐                             │
          │   StoryDirector       │                             │
          │   分镜导演             │                             │
          └───────────┬───────────┘                             │
                      │                                         │
      ┌───────────────┼───────────────┬───────────────┐         │
      ▼               ▼               ▼               ▼         │
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│Character │  │  Scene   │  │  Prop    │  │  Action  │         │
│Designer  │  │Designer  │  │Designer  │  │Designer  │         │
└────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘         │
     │             │             │             │                │
     └─────────────┴──────┬──────┴─────────────┘                │
                          ▼                                     │
              ┌───────────────────────┐                         │
              │   Cinematographer     │                         │
              │   运镜师               │                         │
              └───────────┬───────────┘                         │
                          │                                     │
                          ▼                                     │
              ┌───────────────────────┐                         │
              │  KeyframeExtractor    │                         │
              │  关键帧提取师          │                         │
              └───────────┬───────────┘                         │
                          │                                     │
                          ▼                                     │
              ┌───────────────────────┐                         │
              │   PromptEngineer      │                         │
              │   Prompt工程师        │                         │
              └───────────┬───────────┘                         │
                          │                                     │
                          ▼                                     │
              ┌───────────────────────┐                         │
              │   输出: Video Prompts │                         │
              │   + 关键帧 + 资源     │                         │
              └───────────────────────┘                         │
```

---

## Skill 目录结构

```
.claude/skills/
├── story-analyzer/           # 故事分析师
│   ├── skill.md
│   └── analyzer.py
│
├── emotion-analyzer/         # 情绪分析师
│   ├── skill.md
│   └── analyzer.py
│
├── story-director/           # 分镜导演
│   ├── skill.md
│   ├── director.py
│   └── templates/
│       └── storyboard_template.json
│
├── character-designer/       # 角色设计师
│   ├── skill.md
│   └── designer.py
│
├── scene-designer/           # 场景设计师
│   ├── skill.md
│   └── designer.py
│
├── prop-designer/            # 道具设计师
│   ├── skill.md
│   └── designer.py
│
├── action-designer/          # 动作设计师
│   ├── skill.md
│   └── designer.py
│
├── cinematographer/          # 运镜师
│   ├── skill.md
│   ├── cinematographer.py
│   └── references/
│       └── camera_moves.md
│
├── keyframe-extractor/       # 关键帧提取师
│   ├── skill.md
│   └── extractor.py
│
├── prompt-engineer/          # Prompt工程师
│   ├── skill.md
│   ├── engineer.py
│   └── templates/
│       ├── sora2_template.md
│       └── seedance_template.md
│
└── video-generator/          # 视频生成协调器（主控）
    ├── skill.md
    └── coordinator.py
```

---

## 使用方式

### 单独调用
```
/story-analyzer --chapter chapter_001 --project "穿书后我攻略了奸臣首辅"
```

### 完整流水线
```
/video-generator --chapter chapter_001 --project "穿书后我攻略了奸臣首辅" --full-pipeline
```

### 仅生成 Prompt
```
/prompt-engineer --storyboard scripts/episode_001/storyboard.json --output output/prompts/
```

---

## 风格一致性保障

### 1. 项目级风格文件
每个项目维护 `assets/styles/style_guide.json`:
```json
{
  "art_style": "古风动漫",
  "color_palette": {...},
  "character_consistency": {
    "reference_images": ["角色正面图路径"],
    "style_tags": ["anime", "ancient chinese", "detailed"]
  },
  "scene_consistency": {
    "reference_images": ["场景参考图路径"],
    "lighting_style": "dramatic chiaroscuro"
  }
}
```

### 2. 参考图系统
- 角色四视图作为强制参考
- 场景主图作为背景参考
- 风格参考图控制整体画风

### 3. Prompt 模板系统
- 统一的开头/结尾模板
- 必要的质量标签
- 风格标签注入

---

## 下一步

1. 实现各个 Skill 的 `skill.md` 定义
2. 编写核心 Python 脚本
3. 创建 Prompt 模板库
4. 建立测试用例
