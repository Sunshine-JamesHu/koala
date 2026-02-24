"""
Koala 漫剧生成系统 - 公共模块
"""
from .config import (
    PROJECT_ROOT,
    WORKS_DIR,
    TEMPLATES_DIR,
    ProjectConfig,
    PathConfig,
    load_project_config,
    get_chapter_text,
    save_json,
    load_json
)

from .models import (
    EventType,
    EmotionType,
    ShotSize,
    CameraAngle,
    CameraMovement,
    TimeOfDay,
    Weather,
    KeyEvent,
    CharacterArc,
    MoodPoint,
    AnalysisResult,
    SceneInfo,
    CameraInfo,
    CharacterInShot,
    Dialogue,
    Shot,
    Storyboard,
    Keyframe,
    VideoPrompt,
    enum_to_dict
)

from .utils import (
    clean_text,
    split_into_paragraphs,
    extract_dialogues,
    estimate_reading_time,
    truncate_text,
    generate_id,
    format_duration,
    merge_dicts,
    ensure_list,
    safe_get,
    PromptBuilder,
    ColorPalette,
    CameraMoveHelper
)

__all__ = [
    # Config
    "PROJECT_ROOT",
    "WORKS_DIR",
    "TEMPLATES_DIR",
    "ProjectConfig",
    "PathConfig",
    "load_project_config",
    "get_chapter_text",
    "save_json",
    "load_json",
    # Models
    "EventType",
    "EmotionType",
    "ShotSize",
    "CameraAngle",
    "CameraMovement",
    "TimeOfDay",
    "Weather",
    "KeyEvent",
    "CharacterArc",
    "MoodPoint",
    "AnalysisResult",
    "SceneInfo",
    "CameraInfo",
    "CharacterInShot",
    "Dialogue",
    "Shot",
    "Storyboard",
    "Keyframe",
    "VideoPrompt",
    "enum_to_dict",
    # Utils
    "clean_text",
    "split_into_paragraphs",
    "extract_dialogues",
    "estimate_reading_time",
    "truncate_text",
    "generate_id",
    "format_duration",
    "merge_dicts",
    "ensure_list",
    "safe_get",
    "PromptBuilder",
    "ColorPalette",
    "CameraMoveHelper",
]
