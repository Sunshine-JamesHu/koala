"""
Koala 漫剧生成系统 - 工具函数
"""
import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime


def clean_text(text: str) -> str:
    """清理文本，移除多余空白"""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def split_into_paragraphs(text: str) -> List[str]:
    """将文本分割成段落"""
    paragraphs = re.split(r'\n\s*\n', text)
    return [p.strip() for p in paragraphs if p.strip()]


def extract_dialogues(text: str) -> List[Dict[str, str]]:
    """从文本中提取对话"""
    dialogues = []
    # 匹配引号中的对话
    patterns = [
        r'"([^"]+)"',  # 双引号
        r'"([^"]+)"',  # 中文双引号
        r'「([^」]+)」',  # 日文引号
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            dialogues.append({"text": match, "speaker": ""})

    return dialogues


def estimate_reading_time(text: str, chars_per_second: float = 4.0) -> float:
    """估算阅读时间（秒）"""
    char_count = len(text)
    return char_count / chars_per_second


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """截断文本"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def generate_id(prefix: str = "id") -> str:
    """生成唯一ID"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}_{timestamp}"


def format_duration(seconds: float) -> str:
    """格式化时长"""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def merge_dicts(base: dict, override: dict) -> dict:
    """递归合并字典"""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def ensure_list(value: Any) -> List:
    """确保返回列表"""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def safe_get(d: dict, *keys, default=None):
    """安全获取嵌套字典值"""
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, default)
        else:
            return default
    return d


class PromptBuilder:
    """Prompt构建器"""

    def __init__(self):
        self.parts = []

    def add(self, part: str) -> "PromptBuilder":
        """添加部分"""
        if part:
            self.parts.append(part)
        return self

    def add_if(self, condition: bool, part: str) -> "PromptBuilder":
        """条件添加"""
        if condition and part:
            self.parts.append(part)
        return self

    def add_list(self, items: List[str], separator: str = ", ") -> "PromptBuilder":
        """添加列表"""
        if items:
            self.parts.append(separator.join(items))
        return self

    def build(self, separator: str = ", ") -> str:
        """构建最终Prompt"""
        return separator.join(self.parts)

    def clear(self) -> "PromptBuilder":
        """清空"""
        self.parts = []
        return self


class ColorPalette:
    """色彩调色板"""

    # 情绪色彩映射
    EMOTION_COLORS = {
        "happy": {"primary": "#FFD700", "secondary": "#FFA500", "mood": "warm_bright"},
        "sad": {"primary": "#4169E1", "secondary": "#708090", "mood": "cool_dark"},
        "angry": {"primary": "#DC143C", "secondary": "#8B0000", "mood": "hot_intense"},
        "fearful": {"primary": "#2F4F4F", "secondary": "#000000", "mood": "dark_oppressive"},
        "surprised": {"primary": "#FF6347", "secondary": "#FFFFFF", "mood": "contrasting"},
        "neutral": {"primary": "#808080", "secondary": "#D3D3D3", "mood": "balanced"},
        "contemplative": {"primary": "#483D8B", "secondary": "#B0C4DE", "mood": "soft_muted"},
        "romantic": {"primary": "#FF69B4", "secondary": "#FFE4E1", "mood": "warm_soft"},
        "mysterious": {"primary": "#4B0082", "secondary": "#191970", "mood": "dark_enigmatic"},
        "tense": {"primary": "#556B2F", "secondary": "#2F4F4F", "mood": "oppressive"},
    }

    @classmethod
    def get_emotion_colors(cls, emotion: str) -> Dict[str, str]:
        """获取情绪对应的色彩"""
        return cls.EMOTION_COLORS.get(emotion.lower(), cls.EMOTION_COLORS["neutral"])


class CameraMoveHelper:
    """运镜辅助工具"""

    # 镜头尺寸英文映射
    SHOT_SIZE_EN = {
        "extreme_close_up": "extreme close-up",
        "close_up": "close-up",
        "medium_close_up": "medium close-up",
        "medium_shot": "medium shot",
        "medium_full_shot": "medium full shot",
        "full_shot": "full shot",
        "long_shot": "long shot",
        "extreme_long_shot": "extreme long shot",
    }

    # 镜头角度英文映射
    ANGLE_EN = {
        "eye_level": "eye level",
        "high_angle": "high angle",
        "low_angle": "low angle",
        "dutch_angle": "dutch angle",
        "birds_eye": "bird's eye view",
        "worms_eye": "worm's eye view",
    }

    # 运镜英文映射
    MOVEMENT_EN = {
        "static": "static shot",
        "pan_left": "pan left",
        "pan_right": "pan right",
        "tilt_up": "tilt up",
        "tilt_down": "tilt down",
        "zoom_in": "zoom in",
        "zoom_out": "zoom out",
        "dolly_in": "dolly in",
        "dolly_out": "dolly out",
        "track": "tracking shot",
        "crane": "crane shot",
        "handheld": "handheld camera",
        "arc": "arc shot",
    }

    @classmethod
    def get_shot_size_en(cls, shot_size: str) -> str:
        return cls.SHOT_SIZE_EN.get(shot_size, shot_size)

    @classmethod
    def get_angle_en(cls, angle: str) -> str:
        return cls.ANGLE_EN.get(angle, angle)

    @classmethod
    def get_movement_en(cls, movement: str) -> str:
        return cls.MOVEMENT_EN.get(movement, movement)

    @classmethod
    def build_camera_description(cls, shot_size: str, angle: str, movement: str, speed: str = "") -> str:
        """构建镜头描述"""
        parts = []

        if movement and movement != "static":
            speed_prefix = {"very_slow": "slow ", "slow": "slow ", "medium": "", "fast": "quick ", "very_fast": "rapid "}
            prefix = speed_prefix.get(speed, "")
            parts.append(f"{prefix}{cls.get_movement_en(movement)}")

        parts.append(cls.get_shot_size_en(shot_size))

        if angle and angle != "eye_level":
            parts.append(f"from {cls.get_angle_en(angle)}")

        return ", ".join(parts)
