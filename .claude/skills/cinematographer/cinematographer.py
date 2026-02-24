#!/usr/bin/env python3
"""
Cinematographer - 运镜师

设计专业的镜头运动方案，为AI视频生成提供清晰的运镜描述。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from utils import CameraMoveHelper, PromptBuilder


@dataclass
class CameraFrame:
    """镜头帧"""
    shot_size: str
    angle: str
    position_3d: Dict[str, float]
    look_at: Dict[str, float]
    fov: int
    description: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CameraMovement:
    """镜头运动"""
    type: str
    path_type: str  # linear, curved, arc
    speed_profile: str  # constant, ease_in, ease_out, ease_in_out
    duration: float
    description: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ShotCameraWork:
    """单个镜头的运镜方案"""
    shot_id: str
    camera_setup: Dict[str, CameraFrame]
    movement: CameraMovement
    focus_rack: Dict[str, Any]
    stabilization: str
    visual_effects: Dict[str, Any]
    ai_video_prompt: Dict[str, str]

    def to_dict(self) -> dict:
        return {
            "shot_id": self.shot_id,
            "camera_setup": {
                k: v.to_dict() if isinstance(v, CameraFrame) else v
                for k, v in self.camera_setup.items()
            },
            "movement": self.movement.to_dict(),
            "focus_rack": self.focus_rack,
            "stabilization": self.stabilization,
            "visual_effects": self.visual_effects,
            "ai_video_prompt": self.ai_video_prompt
        }


class Cinematographer:
    """运镜师"""

    # 镜头尺寸映射
    SHOT_SIZE_MAP = {
        "extreme_close_up": {"distance": 0.5, "fov": 85, "desc": "extreme close-up"},
        "close_up": {"distance": 1.0, "fov": 75, "desc": "close-up"},
        "medium_close_up": {"distance": 1.5, "fov": 65, "desc": "medium close-up"},
        "medium_shot": {"distance": 2.5, "fov": 50, "desc": "medium shot"},
        "medium_full_shot": {"distance": 3.5, "fov": 45, "desc": "medium full shot"},
        "full_shot": {"distance": 5.0, "fov": 35, "desc": "full shot"},
        "long_shot": {"distance": 8.0, "fov": 28, "desc": "long shot"},
        "extreme_long_shot": {"distance": 15.0, "fov": 24, "desc": "extreme long shot"},
    }

    # 角度映射
    ANGLE_MAP = {
        "eye_level": {"pitch": 0, "desc": "eye level"},
        "high_angle": {"pitch": 30, "desc": "high angle"},
        "low_angle": {"pitch": -20, "desc": "low angle"},
        "dutch_angle": {"roll": 15, "desc": "dutch angle"},
        "birds_eye": {"pitch": 80, "desc": "bird's eye view"},
        "worms_eye": {"pitch": -45, "desc": "worm's eye view"},
    }

    # 情绪-运镜映射
    EMOTION_MOVEMENT_MAP = {
        "happy": {"type": "track", "speed": "medium", "stabilization": "steadicam"},
        "sad": {"type": "static", "speed": "slow", "stabilization": "tripod"},
        "angry": {"type": "dolly_in", "speed": "fast", "stabilization": "handheld"},
        "fearful": {"type": "handheld", "speed": "medium", "stabilization": "handheld"},
        "surprised": {"type": "zoom_in", "speed": "very_fast", "stabilization": "steadicam"},
        "contemplative": {"type": "dolly_in", "speed": "slow", "stabilization": "steadicam"},
        "romantic": {"type": "arc", "speed": "very_slow", "stabilization": "steadicam"},
        "mysterious": {"type": "dolly_in", "speed": "slow", "stabilization": "steadicam"},
        "tense": {"type": "dolly_in", "speed": "medium", "stabilization": "steadicam"},
        "neutral": {"type": "static", "speed": "medium", "stabilization": "tripod"},
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def design_camera_work(self, episode_id: str) -> Dict[str, Any]:
        """为整个剧集设计运镜方案"""
        # 加载分镜脚本
        storyboard_path = self.path_config.episode_dir(episode_id) / "storyboard.json"
        if not storyboard_path.exists():
            raise FileNotFoundError(f"分镜脚本不存在: {storyboard_path}")

        storyboard = load_json(storyboard_path)
        shots = storyboard.get("shots", [])

        # 为每个镜头设计运镜
        camera_works = []
        for shot in shots:
            camera_work = self._design_shot_camera_work(shot, len(shots))
            camera_works.append(camera_work)

        return {
            "episode": storyboard.get("episode", 1),
            "shots": [cw.to_dict() for cw in camera_works]
        }

    def _design_shot_camera_work(self, shot: Dict, total_shots: int) -> ShotCameraWork:
        """为单个镜头设计运镜"""
        shot_id = shot.get("shot_id", "shot_001")
        sequence = shot.get("sequence", 1)
        camera_info = shot.get("camera", {})
        characters = shot.get("characters", [])
        duration = shot.get("duration", 5.0)

        # 获取镜头参数
        shot_size = camera_info.get("shot_size", "medium_shot")
        angle = camera_info.get("angle", "eye_level")
        movement_type = camera_info.get("movement_type", "static")
        movement_speed = camera_info.get("movement_speed", "medium")

        # 获取情绪（从角色中提取）
        emotion = "neutral"
        if characters:
            emotion = characters[0].get("expression", "neutral")

        # 获取情绪对应的运镜设置
        emotion_settings = self.EMOTION_MOVEMENT_MAP.get(emotion, self.EMOTION_MOVEMENT_MAP["neutral"])

        # 如果分镜中没有指定运镜，使用情绪映射
        if movement_type == "static" and emotion_settings["type"] != "static":
            movement_type = emotion_settings["type"]
            movement_speed = emotion_settings["speed"]

        # 创建起始帧
        start_frame = self._create_camera_frame(shot_size, angle, "start", characters)

        # 创建结束帧
        end_shot_size = self._get_end_shot_size(shot_size, movement_type)
        end_frame = self._create_camera_frame(end_shot_size, angle, "end", characters)

        # 创建运动描述
        movement = CameraMovement(
            type=movement_type,
            path_type=self._get_path_type(movement_type),
            speed_profile=self._get_speed_profile(movement_speed),
            duration=duration,
            description=self._generate_movement_description(
                movement_type, movement_speed, shot_size, end_shot_size
            )
        )

        # 变焦设置
        focus_rack = {
            "enabled": False,
            "start_focus": "主体",
            "end_focus": "主体"
        }

        # 稳定器类型
        stabilization = emotion_settings.get("stabilization", "steadicam")

        # 视觉效果
        visual_effects = {
            "depth_of_field": {
                "aperture": "f/2.8",
                "bokeh": "creamy"
            },
            "motion_blur": {
                "enabled": movement_type not in ["static"],
                "intensity": "subtle" if movement_speed == "slow" else "moderate"
            }
        }

        # AI视频Prompt
        ai_video_prompt = self._generate_ai_video_prompt(
            movement_type, movement_speed, start_frame, end_frame, shot, duration
        )

        return ShotCameraWork(
            shot_id=shot_id,
            camera_setup={
                "start_frame": start_frame,
                "end_frame": end_frame
            },
            movement=movement,
            focus_rack=focus_rack,
            stabilization=stabilization,
            visual_effects=visual_effects,
            ai_video_prompt=ai_video_prompt
        )

    def _create_camera_frame(
        self,
        shot_size: str,
        angle: str,
        frame_type: str,
        characters: List[Dict]
    ) -> CameraFrame:
        """创建镜头帧"""
        shot_info = self.SHOT_SIZE_MAP.get(shot_size, self.SHOT_SIZE_MAP["medium_shot"])
        angle_info = self.ANGLE_MAP.get(angle, self.ANGLE_MAP["eye_level"])

        distance = shot_info["distance"]
        fov = shot_info["fov"]

        # 根据帧类型调整距离
        if frame_type == "end" and shot_size != "medium_shot":
            distance = self.SHOT_SIZE_MAP.get(shot_size, self.SHOT_SIZE_MAP["medium_shot"])["distance"]

        description = f"{shot_info['desc']} from {angle_info['desc']}"

        return CameraFrame(
            shot_size=shot_size,
            angle=angle,
            position_3d={"x": 0, "y": 1.6, "z": distance},
            look_at={"x": 0, "y": 1.5, "z": 0},
            fov=fov,
            description=description
        )

    def _get_end_shot_size(self, start_size: str, movement_type: str) -> str:
        """获取结束镜头尺寸"""
        sizes = list(self.SHOT_SIZE_MAP.keys())

        if movement_type in ["dolly_in", "zoom_in"]:
            # 推进，镜头尺寸变小（更近）
            idx = sizes.index(start_size)
            return sizes[max(0, idx - 1)]
        elif movement_type in ["dolly_out", "zoom_out"]:
            # 拉远，镜头尺寸变大（更远）
            idx = sizes.index(start_size)
            return sizes[min(len(sizes) - 1, idx + 1)]

        return start_size

    def _get_path_type(self, movement_type: str) -> str:
        """获取运动路径类型"""
        if movement_type in ["arc", "crane"]:
            return "curved"
        elif movement_type in ["track", "dolly_in", "dolly_out"]:
            return "linear"
        return "linear"

    def _get_speed_profile(self, speed: str) -> str:
        """获取速度曲线"""
        speed_map = {
            "very_slow": "ease_in_out",
            "slow": "ease_in_out",
            "medium": "constant",
            "fast": "ease_out",
            "very_fast": "ease_out"
        }
        return speed_map.get(speed, "constant")

    def _generate_movement_description(
        self,
        movement_type: str,
        speed: str,
        start_size: str,
        end_size: str
    ) -> str:
        """生成运动描述"""
        movement_en = CameraMoveHelper.get_movement_en(movement_type)
        speed_desc = {
            "very_slow": "very slow",
            "slow": "slow",
            "medium": "steady",
            "fast": "quick",
            "very_fast": "rapid"
        }.get(speed, "steady")

        if movement_type == "static":
            return f"Static shot, {CameraMoveHelper.get_shot_size_en(start_size)}"

        if start_size != end_size:
            return f"{speed_desc} {movement_en}, transitioning from {CameraMoveHelper.get_shot_size_en(start_size)} to {CameraMoveHelper.get_shot_size_en(end_size)}"

        return f"{speed_desc} {movement_en}"

    def _generate_ai_video_prompt(
        self,
        movement_type: str,
        speed: str,
        start_frame: CameraFrame,
        end_frame: CameraFrame,
        shot: Dict,
        duration: float
    ) -> Dict[str, str]:
        """生成AI视频Prompt"""
        builder = PromptBuilder()

        # 运动描述
        movement_desc = self._generate_movement_description(
            movement_type, speed,
            start_frame.shot_size, end_frame.shot_size
        )
        builder.add(movement_desc)

        # 场景描述
        scene = shot.get("scene", {})
        if scene.get("location_name"):
            builder.add(f"in {scene.get('location_name')}")

        # 角色描述
        characters = shot.get("characters", [])
        if characters:
            char = characters[0]
            builder.add(f"featuring {char.get('name', 'character')}")

        # 氛围
        atmosphere = scene.get("atmosphere", "")
        if atmosphere:
            builder.add(atmosphere)

        # 风格
        builder.add("anime style")
        builder.add("cinematic")
        builder.add("high quality")

        movement_description = builder.build()

        # 完整Prompt
        full_prompt = PromptBuilder() \
            .add(movement_desc) \
            .add(start_frame.description) \
            .add(f"to {end_frame.description}") \
            .add(f"in {scene.get('location_name', 'scene')}") \
            .add(scene.get("time_of_day", "")) \
            .add(scene.get("weather", "")) \
            .add("smooth camera movement") \
            .add("cinematic lighting") \
            .add("anime style") \
            .add("highly detailed") \
            .add("8K quality") \
            .build()

        return {
            "movement_description": movement_description,
            "camera_motion_en": f"Camera {movement_desc}",
            "technical_specs": f"smooth movement, {start_frame.stabilization if hasattr(start_frame, 'stabilization') else 'steadicam'} quality",
            "full_prompt": full_prompt
        }

    def save_camera_work(self, camera_work: Dict, episode_id: str) -> Path:
        """保存运镜方案"""
        episode_dir = self.path_config.episode_dir(episode_id)
        episode_dir.mkdir(parents=True, exist_ok=True)

        output_path = episode_dir / "camera_work.json"
        save_json(camera_work, output_path)
        return output_path


def main():
    parser = argparse.ArgumentParser(description="运镜师")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--episode", required=True, help="剧集ID")

    args = parser.parse_args()

    cinematographer = Cinematographer(args.project)
    camera_work = cinematographer.design_camera_work(args.episode)
    output_path = cinematographer.save_camera_work(camera_work, args.episode)

    print(f"运镜方案生成完成: {output_path}")
    print(f"镜头数: {len(camera_work['shots'])}")

    # 显示第一个镜头的运镜描述
    if camera_work['shots']:
        first_shot = camera_work['shots'][0]
        print(f"\n第一个镜头运镜:")
        print(f"  类型: {first_shot['movement']['type']}")
        print(f"  描述: {first_shot['movement']['description']}")


if __name__ == "__main__":
    main()
