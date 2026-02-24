"""
Koala 漫剧生成系统 - 数据模型
"""
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any
from enum import Enum
import json


class EventType(Enum):
    """事件类型"""
    DIALOGUE = "dialogue"
    ACTION = "action"
    REVELATION = "revelation"
    CONFLICT = "conflict"
    RESOLUTION = "resolution"
    TRANSITION = "transition"


class EmotionType(Enum):
    """情绪类型"""
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    FEARFUL = "fearful"
    SURPRISED = "surprised"
    DISGUSTED = "disgusted"
    CONTEMPLATIVE = "contemplative"
    ANTICIPATION = "anticipation"
    TRUST = "trust"


class ShotSize(Enum):
    """镜头尺寸"""
    EXTREME_CLOSE_UP = "extreme_close_up"
    CLOSE_UP = "close_up"
    MEDIUM_CLOSE_UP = "medium_close_up"
    MEDIUM_SHOT = "medium_shot"
    MEDIUM_FULL_SHOT = "medium_full_shot"
    FULL_SHOT = "full_shot"
    LONG_SHOT = "long_shot"
    EXTREME_LONG_SHOT = "extreme_long_shot"


class CameraAngle(Enum):
    """镜头角度"""
    EYE_LEVEL = "eye_level"
    HIGH_ANGLE = "high_angle"
    LOW_ANGLE = "low_angle"
    DUTCH_ANGLE = "dutch_angle"
    BIRDS_EYE = "birds_eye"
    WORMS_EYE = "worms_eye"


class CameraMovement(Enum):
    """镜头运动"""
    STATIC = "static"
    PAN_LEFT = "pan_left"
    PAN_RIGHT = "pan_right"
    TILT_UP = "tilt_up"
    TILT_DOWN = "tilt_down"
    ZOOM_IN = "zoom_in"
    ZOOM_OUT = "zoom_out"
    DOLLY_IN = "dolly_in"
    DOLLY_OUT = "dolly_out"
    TRACK = "track"
    CRANE = "crane"
    HANDHELD = "handheld"
    ARC = "arc"


class TimeOfDay(Enum):
    """时间段"""
    DAWN = "dawn"
    MORNING = "morning"
    NOON = "noon"
    AFTERNOON = "afternoon"
    DUSK = "dusk"
    EVENING = "evening"
    NIGHT = "night"
    MIDNIGHT = "midnight"


class Weather(Enum):
    """天气"""
    CLEAR = "clear"
    CLOUDY = "cloudy"
    RAIN = "rain"
    SNOW = "snow"
    FOG = "fog"
    STORM = "storm"


# ============ 数据类 ============

@dataclass
class KeyEvent:
    """关键事件"""
    event_id: str
    type: str
    description: str
    characters: List[str]
    location: str = ""
    emotion: str = "neutral"
    importance: int = 5
    visual_potential: str = "medium"
    dialogue_snippets: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CharacterArc:
    """角色弧线"""
    state_before: str
    state_after: str
    emotional_journey: str
    key_moments: List[str]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class MoodPoint:
    """情绪曲线点"""
    position: float  # 0.0 - 1.0
    intensity: float  # 0.0 - 1.0
    emotion: str
    trigger_event: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AnalysisResult:
    """故事分析结果"""
    chapter_id: str
    word_count: int
    summary: str
    key_events: List[KeyEvent]
    character_arcs: Dict[str, CharacterArc]
    locations: List[Dict[str, Any]]
    mood_curve: List[MoodPoint]
    conflicts: List[Dict[str, Any]]
    pacing: Dict[str, str]
    visual_highlights: List[str]

    def to_dict(self) -> dict:
        return {
            "chapter_id": self.chapter_id,
            "word_count": self.word_count,
            "summary": self.summary,
            "key_events": [e.to_dict() for e in self.key_events],
            "character_arcs": {k: v.to_dict() for k, v in self.character_arcs.items()},
            "locations": self.locations,
            "mood_curve": [m.to_dict() for m in self.mood_curve],
            "conflicts": self.conflicts,
            "pacing": self.pacing,
            "visual_highlights": self.visual_highlights
        }


@dataclass
class SceneInfo:
    """场景信息"""
    location_id: str
    location_name: str
    location_type: str = "indoor"
    time_of_day: str = "day"
    weather: str = "clear"
    lighting: str = ""
    atmosphere: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CameraInfo:
    """镜头信息"""
    shot_size: str = "medium_shot"
    angle: str = "eye_level"
    movement_type: str = "static"
    movement_direction: str = ""
    movement_speed: str = "medium"
    focus_subject: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CharacterInShot:
    """镜头中的角色"""
    character_id: str
    name: str
    importance: str = "primary"
    position: str = "center"
    pose: str = ""
    action: str = ""
    expression: str = ""
    expression_intensity: str = "moderate"
    costume_id: str = ""
    gaze_direction: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Dialogue:
    """对话"""
    speaker: str
    text: str
    tone: str = "normal"
    pace: str = "normal"
    volume: str = "normal"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Shot:
    """镜头"""
    shot_id: str
    sequence: int
    source_event: str = ""
    beat_type: str = "rising_action"
    narrative_purpose: str = ""
    duration: float = 5.0
    scene: SceneInfo = None
    camera: CameraInfo = None
    characters: List[CharacterInShot] = field(default_factory=list)
    dialogue: Optional[Dialogue] = None
    narration: str = ""
    bgm_mood: str = ""
    sfx: List[str] = field(default_factory=list)
    transition_type: str = "cut"
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "shot_id": self.shot_id,
            "sequence": self.sequence,
            "source_event": self.source_event,
            "beat_type": self.beat_type,
            "narrative_purpose": self.narrative_purpose,
            "duration": self.duration,
            "scene": self.scene.to_dict() if self.scene else {},
            "camera": self.camera.to_dict() if self.camera else {},
            "characters": [c.to_dict() for c in self.characters],
            "dialogue": self.dialogue.to_dict() if self.dialogue else None,
            "narration": self.narration,
            "bgm_mood": self.bgm_mood,
            "sfx": self.sfx,
            "transition_type": self.transition_type,
            "notes": self.notes
        }


@dataclass
class Storyboard:
    """分镜脚本"""
    episode: int
    title: str
    source_chapter: str
    total_duration: float
    shots: List[Shot]
    art_style: str = "anime"
    era_style: str = "ancient_chinese"

    def to_dict(self) -> dict:
        return {
            "episode": self.episode,
            "title": self.title,
            "source_chapter": self.source_chapter,
            "total_duration": self.total_duration,
            "total_shots": len(self.shots),
            "global_settings": {
                "art_style": self.art_style,
                "era_style": self.era_style,
                "aspect_ratio": "16:9",
                "fps": 24
            },
            "shots": [s.to_dict() for s in self.shots],
            "metadata": {
                "status": "draft",
                "version": "1.0"
            }
        }


@dataclass
class Keyframe:
    """关键帧"""
    keyframe_id: str
    shot_id: str
    position_in_shot: float
    type: str  # start, peak, transition, end
    description: str
    scene_description: Dict[str, Any]
    characters: List[Dict[str, Any]]
    composition: Dict[str, Any]
    lighting_and_color: Dict[str, Any]
    image_prompt: str
    negative_prompt: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class VideoPrompt:
    """视频生成Prompt"""
    shot_id: str
    duration: float
    start_frame_prompt: str
    end_frame_prompt: str
    video_prompt_sora2: str
    video_prompt_seedance: str
    video_prompt_kling: str
    camera_movement: Dict[str, Any]
    style_consistency: Dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)


# ============ 工具函数 ============

def enum_to_dict(obj):
    """将包含Enum的对象转换为可序列化的字典"""
    if isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, dict):
        return {k: enum_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [enum_to_dict(item) for item in obj]
    elif hasattr(obj, 'to_dict'):
        return obj.to_dict()
    else:
        return obj
