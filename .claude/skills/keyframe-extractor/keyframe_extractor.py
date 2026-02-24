#!/usr/bin/env python3
"""
Keyframe Extractor - 关键帧提取师

从分镜脚本中提取关键帧，并为每个关键帧生成图像生成Prompt。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from utils import PromptBuilder, ColorPalette, CameraMoveHelper


@dataclass
class KeyframeData:
    """关键帧数据"""
    keyframe_id: str
    shot_id: str
    position_in_shot: float  # 0.0 - 1.0
    type: str  # start, action_peak, emotion_peak, transition, end
    narrative_purpose: str
    scene_description: Dict[str, Any]
    characters: List[Dict[str, Any]]
    composition: Dict[str, Any]
    lighting_and_color: Dict[str, Any]
    image_prompt: str
    negative_prompt: str

    def to_dict(self) -> dict:
        return asdict(self)


class KeyframeExtractor:
    """关键帧提取师"""

    # 默认风格设置
    DEFAULT_STYLE = {
        "art_style": "anime",
        "era_style": "ancient_chinese",
        "quality_tags": [
            "masterpiece", "best quality", "highly detailed",
            "8k resolution", "cinematic composition"
        ]
    }

    # 负面提示词
    DEFAULT_NEGATIVE_PROMPT = (
        "low quality, blurry, deformed, bad anatomy, "
        "extra limbs, missing fingers, modern objects, "
        "western elements, text, watermark"
    )

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

        # 加载角色信息
        self.characters_data = self._load_characters()

    def _load_characters(self) -> Dict:
        """加载角色信息"""
        characters = {}
        char_dir = self.path_config.characters_dir

        if char_dir.exists():
            for char_folder in char_dir.iterdir():
                if char_folder.is_dir():
                    char_file = char_folder / "design.json"
                    if char_file.exists():
                        data = load_json(char_file)
                        characters[char_folder.name] = data

        return characters

    def extract_keyframes(self, episode_id: str) -> Dict[str, Any]:
        """为整个剧集提取关键帧"""
        # 加载分镜脚本
        storyboard_path = self.path_config.episode_dir(episode_id) / "storyboard.json"
        if not storyboard_path.exists():
            raise FileNotFoundError(f"分镜脚本不存在: {storyboard_path}")

        # 加载运镜方案
        camera_work_path = self.path_config.episode_dir(episode_id) / "camera_work.json"
        camera_work = {}
        if camera_work_path.exists():
            camera_work_data = load_json(camera_work_path)
            for shot in camera_work_data.get("shots", []):
                camera_work[shot["shot_id"]] = shot

        storyboard = load_json(storyboard_path)
        shots = storyboard.get("shots", [])

        # 提取所有关键帧
        all_keyframes = []
        for shot in shots:
            keyframes = self._extract_shot_keyframes(
                shot,
                camera_work.get(shot.get("shot_id", ""), {}),
                storyboard.get("global_settings", {})
            )
            all_keyframes.extend(keyframes)

        return {
            "episode": storyboard.get("episode", 1),
            "style_settings": self.DEFAULT_STYLE,
            "keyframes": [kf.to_dict() for kf in all_keyframes]
        }

    def _extract_shot_keyframes(
        self,
        shot: Dict,
        camera_work: Dict,
        global_settings: Dict
    ) -> List[KeyframeData]:
        """为单个镜头提取关键帧"""
        shot_id = shot.get("shot_id", "shot_001")
        keyframes = []

        # 确定关键帧数量和位置
        duration = shot.get("duration", 5.0)
        beat_type = shot.get("beat_type", "rising_action")

        # 根据镜头类型和时长决定关键帧
        if duration <= 3:
            # 短镜头：起始帧 + 结束帧
            keyframe_positions = [
                {"position": 0.0, "type": "start"},
                {"position": 1.0, "type": "end"}
            ]
        elif duration <= 6:
            # 中等镜头：起始帧 + 高潮帧 + 结束帧
            keyframe_positions = [
                {"position": 0.0, "type": "start"},
                {"position": 0.5, "type": "emotion_peak"},
                {"position": 1.0, "type": "end"}
            ]
        else:
            # 长镜头：起始帧 + 发展帧 + 高潮帧 + 结束帧
            keyframe_positions = [
                {"position": 0.0, "type": "start"},
                {"position": 0.33, "type": "transition"},
                {"position": 0.66, "type": "emotion_peak"},
                {"position": 1.0, "type": "end"}
            ]

        # 为每个关键帧位置生成数据
        for i, kf_pos in enumerate(keyframe_positions):
            keyframe = self._create_keyframe(
                shot_id=shot_id,
                position=kf_pos["position"],
                kf_type=kf_pos["type"],
                shot=shot,
                camera_work=camera_work,
                global_settings=global_settings,
                index=i + 1
            )
            keyframes.append(keyframe)

        return keyframes

    def _create_keyframe(
        self,
        shot_id: str,
        position: float,
        kf_type: str,
        shot: Dict,
        camera_work: Dict,
        global_settings: Dict,
        index: int
    ) -> KeyframeData:
        """创建关键帧"""
        keyframe_id = f"{shot_id}_kf_{index:03d}"

        # 场景描述
        scene_description = self._build_scene_description(shot, position)

        # 角色描述
        characters = self._build_character_descriptions(shot, position, kf_type)

        # 构图
        composition = self._build_composition(shot, camera_work, position)

        # 光影和色彩
        lighting_and_color = self._build_lighting_and_color(shot, kf_type)

        # 叙事目的
        narrative_purpose = self._get_narrative_purpose(kf_type, shot)

        # 生成图像Prompt
        image_prompt = self._generate_image_prompt(
            scene_description, characters, composition, lighting_and_color, global_settings
        )

        return KeyframeData(
            keyframe_id=keyframe_id,
            shot_id=shot_id,
            position_in_shot=position,
            type=kf_type,
            narrative_purpose=narrative_purpose,
            scene_description=scene_description,
            characters=characters,
            composition=composition,
            lighting_and_color=lighting_and_color,
            image_prompt=image_prompt,
            negative_prompt=self.DEFAULT_NEGATIVE_PROMPT
        )

    def _build_scene_description(self, shot: Dict, position: float) -> Dict[str, Any]:
        """构建场景描述"""
        scene = shot.get("scene", {})

        return {
            "location": scene.get("location_name", "未指定场景"),
            "time_of_day": scene.get("time_of_day", "day"),
            "weather": scene.get("weather", "clear"),
            "lighting": self._get_lighting_description(scene, position),
            "atmosphere": scene.get("atmosphere", ""),
            "environmental_details": self._get_environment_details(scene)
        }

    def _get_lighting_description(self, scene: Dict, position: float) -> str:
        """获取光照描述"""
        time_of_day = scene.get("time_of_day", "day")

        lighting_map = {
            "dawn": "微弱晨光，柔和散射",
            "morning": "明亮自然光",
            "noon": "强烈直射阳光",
            "afternoon": "温暖斜射光",
            "dusk": "金色余晖",
            "evening": "人工照明，暖色调",
            "night": "昏暗，局部照明",
            "midnight": "极昏暗，月光或烛光"
        }

        base_lighting = lighting_map.get(time_of_day, "自然光")

        # 根据天气调整
        weather = scene.get("weather", "clear")
        if weather == "rain":
            base_lighting += "，雨天气氛"
        elif weather == "cloudy":
            base_lighting += "，阴天柔和"

        return base_lighting

    def _get_environment_details(self, scene: Dict) -> List[str]:
        """获取环境细节"""
        details = []
        location = scene.get("location_name", "")

        # 根据场景类型添加细节
        if "书房" in location:
            details = ["书架", "书桌", "笔墨纸砚", "窗棂"]
        elif "卧房" in location:
            details = ["床榻", "屏风", "梳妆台"]
        elif "庭院" in location:
            details = ["假山", "花木", "石径"]
        elif "街道" in location:
            details = ["商铺", "行人", "牌坊"]

        return details

    def _build_character_descriptions(
        self,
        shot: Dict,
        position: float,
        kf_type: str
    ) -> List[Dict[str, Any]]:
        """构建角色描述"""
        characters = []
        shot_characters = shot.get("characters", [])

        for char in shot_characters:
            char_name = char.get("name", "")

            # 获取角色详细数据
            char_data = self.characters_data.get(char_name, {})

            # 表情强度
            expression_intensity = char.get("expression_intensity", "moderate")
            if kf_type == "emotion_peak":
                expression_intensity = "intense"
            elif kf_type == "start":
                expression_intensity = "subtle"

            character_desc = {
                "name": char_name,
                "reference_image": f"assets/characters/{char_name}/front.png" if char_data else "",
                "position_in_frame": char.get("position", "center"),
                "body_position": char.get("pose", ""),
                "pose": char.get("action", ""),
                "expression": {
                    "type": char.get("expression", "neutral"),
                    "intensity": expression_intensity
                },
                "costume": {
                    "id": char.get("costume_id", ""),
                    "description": char_data.get("costumes", [{}])[0].get("prompt_description", "") if char_data else ""
                }
            }

            characters.append(character_desc)

        return characters

    def _build_composition(
        self,
        shot: Dict,
        camera_work: Dict,
        position: float
    ) -> Dict[str, Any]:
        """构建构图信息"""
        camera = shot.get("camera", {})

        # 根据位置插值镜头尺寸
        shot_size = camera.get("shot_size", "medium_shot")
        if camera_work and position > 0:
            start_frame = camera_work.get("camera_setup", {}).get("start_frame", {})
            end_frame = camera_work.get("camera_setup", {}).get("end_frame", {})
            # 简化：如果位置>0.5，使用结束帧的镜头尺寸
            if position > 0.5:
                shot_size = end_frame.get("shot_size", shot_size)

        # 构图法则
        characters = shot.get("characters", [])
        if len(characters) > 1:
            framing_rule = "symmetrical"
        elif characters:
            position_val = characters[0].get("position", "center")
            if "left" in position_val:
                framing_rule = "rule_of_thirds"
            elif "right" in position_val:
                framing_rule = "rule_of_thirds"
            else:
                framing_rule = "center_frame"
        else:
            framing_rule = "golden_ratio"

        return {
            "shot_size": shot_size,
            "camera_angle": camera.get("angle", "eye_level"),
            "framing": framing_rule,
            "depth_layers": ["前景", "中景", "背景"],
            "focal_point": characters[0].get("name", "") if characters else "场景中心"
        }

    def _build_lighting_and_color(self, shot: Dict, kf_type: str) -> Dict[str, Any]:
        """构建光影和色彩"""
        scene = shot.get("scene", {})
        characters = shot.get("characters", [])

        # 获取情绪
        emotion = "neutral"
        if characters:
            emotion = characters[0].get("expression", "neutral")

        # 获取情绪对应的色彩
        color_info = ColorPalette.get_emotion_colors(emotion)

        # 主光源
        time_of_day = scene.get("time_of_day", "day")
        if time_of_day in ["night", "evening", "midnight"]:
            key_light = {"source": "人工照明", "direction": "侧面", "quality": "温暖"}
        else:
            key_light = {"source": "自然光", "direction": "侧面", "quality": "柔和"}

        return {
            "key_light": key_light,
            "fill_light": {"source": "环境反射", "quality": "柔和"},
            "color_temperature": "暖色调" if emotion in ["happy", "romantic"] else "冷色调" if emotion in ["sad", "fearful"] else "中性",
            "shadows": "戏剧性明暗对比" if kf_type == "emotion_peak" else "柔和阴影",
            "color_mood": color_info.get("mood", "balanced")
        }

    def _get_narrative_purpose(self, kf_type: str, shot: Dict) -> str:
        """获取叙事目的"""
        purposes = {
            "start": "建立场景" if not shot.get("characters") else "引入角色",
            "transition": "场景过渡",
            "emotion_peak": "情绪高潮",
            "action_peak": "动作高潮",
            "end": "定格情绪"
        }

        base_purpose = purposes.get(kf_type, "")

        # 结合镜头的叙事目的
        shot_purpose = shot.get("narrative_purpose", "")
        if shot_purpose:
            return f"{base_purpose} - {shot_purpose}"

        return base_purpose

    def _generate_image_prompt(
        self,
        scene_description: Dict,
        characters: List[Dict],
        composition: Dict,
        lighting_and_color: Dict,
        global_settings: Dict
    ) -> str:
        """生成图像Prompt"""
        builder = PromptBuilder()

        # 场景
        builder.add(scene_description.get("location", ""))
        builder.add(scene_description.get("time_of_day", ""))
        if scene_description.get("weather") != "clear":
            builder.add(f"{scene_description.get('weather', '')} weather")

        # 角色
        for char in characters:
            char_prompt = PromptBuilder() \
                .add(char.get("name", "")) \
                .add(char.get("costume", {}).get("description", "")) \
                .add(char.get("pose", "")) \
                .add(char.get("expression", {}).get("type", "")) \
                .build()
            if char_prompt:
                builder.add(char_prompt)

        # 构图
        builder.add(CameraMoveHelper.get_shot_size_en(composition.get("shot_size", "medium_shot")))

        # 光影
        builder.add(lighting_and_color.get("color_mood", ""))
        key_light = lighting_and_color.get("key_light", {})
        if key_light.get("source"):
            builder.add(f"{key_light.get('source')} lighting")

        # 氛围
        builder.add(scene_description.get("atmosphere", ""))

        # 风格
        builder.add(global_settings.get("art_style", "anime"))
        builder.add(global_settings.get("era_style", ""))

        # 质量标签
        quality_tags = global_settings.get("quality_tags", self.DEFAULT_STYLE["quality_tags"])
        builder.add_list(quality_tags)

        return builder.build()

    def save_keyframes(self, keyframes_data: Dict, episode_id: str) -> Path:
        """保存关键帧数据"""
        episode_dir = self.path_config.episode_dir(episode_id)
        episode_dir.mkdir(parents=True, exist_ok=True)

        output_path = episode_dir / "keyframes.json"
        save_json(keyframes_data, output_path)
        return output_path


def main():
    parser = argparse.ArgumentParser(description="关键帧提取师")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--episode", required=True, help="剧集ID")

    args = parser.parse_args()

    extractor = KeyframeExtractor(args.project)
    keyframes_data = extractor.extract_keyframes(args.episode)
    output_path = extractor.save_keyframes(keyframes_data, args.episode)

    print(f"关键帧提取完成: {output_path}")
    print(f"关键帧数: {len(keyframes_data['keyframes'])}")

    # 显示第一个关键帧的Prompt
    if keyframes_data['keyframes']:
        first_kf = keyframes_data['keyframes'][0]
        print(f"\n第一个关键帧 Prompt:")
        print(f"  {first_kf['image_prompt'][:200]}...")


if __name__ == "__main__":
    main()
