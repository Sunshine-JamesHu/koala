"""
Koala 漫剧生成系统 - 配置管理模块
"""
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import json


# 项目根目录
# config.py 位于 .claude/skills/lib/ 下，需要向上4级到达项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
WORKS_DIR = PROJECT_ROOT / "works"
TEMPLATES_DIR = PROJECT_ROOT / "templates"


@dataclass
class ProjectConfig:
    """项目配置"""
    name: str
    title: str = ""
    author: str = ""
    video_resolution: str = "1920x1080"
    video_fps: int = 24
    art_style: str = "anime"
    era_style: str = "ancient_chinese"

    @classmethod
    def from_json(cls, data: dict) -> "ProjectConfig":
        video = data.get("video", {})
        style = data.get("style", {})
        return cls(
            name=data.get("name", ""),
            title=data.get("title", ""),
            author=data.get("author", ""),
            video_resolution=video.get("resolution", "1920x1080"),
            video_fps=video.get("fps", 24),
            art_style=style.get("artStyle", "anime"),
            era_style=style.get("eraStyle", "ancient_chinese")
        )


@dataclass
class PathConfig:
    """路径配置"""
    project_name: str
    base_path: Path = field(default_factory=lambda: WORKS_DIR)

    @property
    def project_dir(self) -> Path:
        return self.base_path / self.project_name

    @property
    def novel_dir(self) -> Path:
        return self.project_dir / "novel"

    @property
    def chapters_dir(self) -> Path:
        return self.novel_dir / "chapters"

    @property
    def scripts_dir(self) -> Path:
        return self.project_dir / "scripts"

    @property
    def assets_dir(self) -> Path:
        return self.project_dir / "assets"

    @property
    def characters_dir(self) -> Path:
        return self.assets_dir / "characters"

    @property
    def scenes_dir(self) -> Path:
        return self.assets_dir / "scenes"

    @property
    def props_dir(self) -> Path:
        return self.assets_dir / "props"

    @property
    def output_dir(self) -> Path:
        return self.project_dir / "output"

    @property
    def cache_dir(self) -> Path:
        return self.project_dir / "cache"

    @property
    def analysis_cache_dir(self) -> Path:
        return self.cache_dir / "analysis"

    def chapter_path(self, chapter_id: str) -> Path:
        """获取章节文件路径"""
        return self.chapters_dir / f"{chapter_id}.txt"

    def episode_dir(self, episode_id: str) -> Path:
        """获取剧集目录"""
        return self.scripts_dir / episode_id

    def character_dir(self, character_name: str) -> Path:
        """获取角色目录"""
        return self.characters_dir / character_name

    def scene_dir(self, scene_name: str) -> Path:
        """获取场景目录"""
        return self.scenes_dir / scene_name

    def ensure_dirs(self):
        """确保所有必要目录存在"""
        dirs = [
            self.project_dir,
            self.novel_dir,
            self.chapters_dir,
            self.scripts_dir,
            self.assets_dir,
            self.characters_dir,
            self.scenes_dir,
            self.props_dir,
            self.output_dir,
            self.cache_dir,
            self.analysis_cache_dir
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)


def load_project_config(project_name: str) -> tuple[ProjectConfig, PathConfig]:
    """加载项目配置"""
    path_config = PathConfig(project_name=project_name)
    config_file = path_config.project_dir / "project.json"

    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        project_config = ProjectConfig.from_json(data)
    else:
        project_config = ProjectConfig(name=project_name)

    return project_config, path_config


def get_chapter_text(path_config: PathConfig, chapter_id: str) -> str:
    """读取章节文本"""
    chapter_file = path_config.chapter_path(chapter_id)
    if not chapter_file.exists():
        raise FileNotFoundError(f"章节文件不存在: {chapter_file}")

    with open(chapter_file, "r", encoding="utf-8") as f:
        return f.read()


def save_json(data: dict, filepath: Path, indent: int = 2):
    """保存JSON文件"""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def load_json(filepath: Path) -> dict:
    """加载JSON文件"""
    if not filepath.exists():
        raise FileNotFoundError(f"文件不存在: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
