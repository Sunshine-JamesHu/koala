#!/usr/bin/env python3
"""
Prompt Engineer - Prompt工程师

整合所有设计元素，生成用于AI视频生成的最终Prompt。
支持 Sora2、SeeDance2.0、Kling 等模型。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from utils import PromptBuilder, CameraMoveHelper


@dataclass
class VideoPrompts:
    """视频Prompt集合"""
    shot_id: str
    duration: float
    input_assets: Dict[str, Any]
    prompts: Dict[str, Any]
    motion_guidance: Dict[str, Any]
    style_consistency: Dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)


class PromptEngineer:
    """Prompt工程师"""

    # 质量标签
    QUALITY_TAGS_EN = [
        "masterpiece", "best quality", "highly detailed",
        "8k resolution", "cinematic composition"
    ]

    QUALITY_TAGS_CN = [
        "高画质", "精细画面", "电影级构图"
    ]

    # 风格标签映射
    STYLE_TAGS = {
        "anime": "anime style",
        "ancient_chinese": "ancient Chinese",
        "cinematic": "cinematic",
        "realistic": "photorealistic"
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def generate_video_prompts(self, episode_id: str, target_model: str = "all") -> Dict[str, Any]:
        """生成视频Prompt"""
        # 加载关键帧数据
        keyframes_path = self.path_config.episode_dir(episode_id) / "keyframes.json"
        if not keyframes_path.exists():
            raise FileNotFoundError(f"关键帧数据不存在: {keyframes_path}")

        # 加载运镜方案
        camera_work_path = self.path_config.episode_dir(episode_id) / "camera_work.json"
        camera_work = {}
        if camera_work_path.exists():
            camera_work_data = load_json(camera_work_path)
            for shot in camera_work_data.get("shots", []):
                camera_work[shot["shot_id"]] = shot

        # 加载分镜脚本
        storyboard_path = self.path_config.episode_dir(episode_id) / "storyboard.json"
        storyboard = load_json(storyboard_path) if storyboard_path.exists() else {}

        keyframes_data = load_json(keyframes_path)
        keyframes = keyframes_data.get("keyframes", [])
        style_settings = keyframes_data.get("style_settings", {})

        # 按镜头组织关键帧
        shot_keyframes = {}
        for kf in keyframes:
            shot_id = kf.get("shot_id", "")
            if shot_id not in shot_keyframes:
                shot_keyframes[shot_id] = []
            shot_keyframes[shot_id].append(kf)

        # 为每个镜头生成Prompt
        video_prompts = []
        for shot_id, kfs in shot_keyframes.items():
            prompts = self._generate_shot_prompts(
                shot_id=shot_id,
                keyframes=kfs,
                camera_work=camera_work.get(shot_id, {}),
                style_settings=style_settings,
                target_model=target_model
            )
            video_prompts.append(prompts)

        return {
            "episode": storyboard.get("episode", 1),
            "target_model": target_model,
            "generation_settings": {
                "aspect_ratio": "16:9",
                "fps": 24,
                "default_duration": 5.0
            },
            "shots": [p.to_dict() for p in video_prompts]
        }

    def _generate_shot_prompts(
        self,
        shot_id: str,
        keyframes: List[Dict],
        camera_work: Dict,
        style_settings: Dict,
        target_model: str
    ) -> VideoPrompts:
        """为单个镜头生成Prompt"""
        # 获取起始帧和结束帧
        start_kf = next((kf for kf in keyframes if kf.get("type") == "start"), keyframes[0])
        end_kf = next((kf for kf in keyframes if kf.get("type") == "end"), keyframes[-1])

        # 计算时长
        duration = self._estimate_duration(keyframes)

        # 输入资源
        input_assets = self._build_input_assets(start_kf, end_kf, keyframes)

        # 生成各模型Prompt
        prompts = self._build_all_prompts(
            start_kf, end_kf, camera_work, style_settings, target_model
        )

        # 运动指导
        motion_guidance = self._build_motion_guidance(camera_work, keyframes)

        # 风格一致性
        style_consistency = self._build_style_consistency(style_settings, keyframes)

        return VideoPrompts(
            shot_id=shot_id,
            duration=duration,
            input_assets=input_assets,
            prompts=prompts,
            motion_guidance=motion_guidance,
            style_consistency=style_consistency
        )

    def _estimate_duration(self, keyframes: List[Dict]) -> float:
        """估算镜头时长"""
        # 基于关键帧数量估算
        num_keyframes = len(keyframes)
        if num_keyframes <= 2:
            return 3.0
        elif num_keyframes <= 3:
            return 5.0
        else:
            return 7.0

    def _build_input_assets(
        self,
        start_kf: Dict,
        end_kf: Dict,
        keyframes: List[Dict]
    ) -> Dict[str, Any]:
        """构建输入资源"""
        # 收集角色参考图
        character_refs = set()
        for kf in keyframes:
            for char in kf.get("characters", []):
                ref = char.get("reference_image", "")
                if ref:
                    character_refs.add(ref)

        return {
            "start_frame_image": f"keyframes/{start_kf.get('keyframe_id', '')}.png",
            "end_frame_image": f"keyframes/{end_kf.get('keyframe_id', '')}.png",
            "character_references": list(character_refs),
            "scene_reference": "",
            "style_reference": ""
        }

    def _build_all_prompts(
        self,
        start_kf: Dict,
        end_kf: Dict,
        camera_work: Dict,
        style_settings: Dict,
        target_model: str
    ) -> Dict[str, Any]:
        """构建所有模型的Prompt"""
        prompts = {
            "image_prompts": {
                "start_frame": start_kf.get("image_prompt", ""),
                "end_frame": end_kf.get("image_prompt", "")
            },
            "video_prompt": {}
        }

        # 获取运镜描述
        camera_prompt = camera_work.get("ai_video_prompt", {}).get("full_prompt", "")

        models = ["Sora2", "SeeDance", "Kling"] if target_model == "all" else [target_model]

        for model in models:
            if model == "Sora2":
                prompts["video_prompt"]["Sora2"] = self._build_sora2_prompt(
                    start_kf, end_kf, camera_work, style_settings
                )
            elif model == "SeeDance":
                prompts["video_prompt"]["SeeDance"] = self._build_seedance_prompt(
                    start_kf, end_kf, camera_work, style_settings
                )
            elif model == "Kling":
                prompts["video_prompt"]["Kling"] = self._build_kling_prompt(
                    start_kf, end_kf, camera_work, style_settings
                )

        return prompts

    def _build_sora2_prompt(
        self,
        start_kf: Dict,
        end_kf: Dict,
        camera_work: Dict,
        style_settings: Dict
    ) -> Dict[str, Any]:
        """构建Sora2 Prompt"""
        # 获取运镜描述
        camera_info = camera_work.get("ai_video_prompt", {})
        movement_desc = camera_info.get("movement_description", "")

        # 场景描述
        scene = start_kf.get("scene_description", {})
        scene_desc = PromptBuilder() \
            .add(scene.get("location", "")) \
            .add(scene.get("time_of_day", "")) \
            .add(f"{scene.get('weather', '')} weather" if scene.get("weather") != "clear" else "") \
            .build()

        # 角色描述
        characters = start_kf.get("characters", [])
        char_desc = ""
        if characters:
            char = characters[0]
            char_builder = PromptBuilder()
            char_builder.add(f"young {'woman' if 'female' in str(char) else 'man'}")
            char_builder.add(char.get("costume", {}).get("description", ""))
            char_builder.add(char.get("pose", ""))
            char_desc = char_builder.build()

        # 构建完整Prompt
        full_prompt = PromptBuilder() \
            .add(movement_desc) \
            .add(scene_desc) \
            .add(char_desc) \
            .add(scene.get("atmosphere", "")) \
            .add("anime style") \
            .add("highly detailed") \
            .add("cinematic") \
            .add("8K quality") \
            .build()

        return {
            "prompt": full_prompt,
            "parameters": {
                "duration": self._estimate_duration([start_kf, end_kf]),
                "aspect_ratio": "16:9",
                "style": "cinematic"
            }
        }

    def _build_seedance_prompt(
        self,
        start_kf: Dict,
        end_kf: Dict,
        camera_work: Dict,
        style_settings: Dict
    ) -> Dict[str, Any]:
        """构建SeeDance Prompt (中英双语)"""
        scene = start_kf.get("scene_description", {})

        # 中文Prompt
        cn_builder = PromptBuilder()
        cn_builder.add(scene.get("location", ""))
        cn_builder.add(scene.get("time_of_day", ""))

        # 运动描述
        movement = camera_work.get("movement", {})
        movement_type = movement.get("type", "static")
        movement_cn = {
            "dolly_in": "镜头推进",
            "dolly_out": "镜头拉远",
            "pan_left": "镜头左摇",
            "pan_right": "镜头右摇",
            "static": "静止镜头",
            "arc": "环绕镜头",
            "track": "跟随镜头"
        }.get(movement_type, "")
        cn_builder.add(movement_cn)

        # 角色
        characters = start_kf.get("characters", [])
        if characters:
            char = characters[0]
            cn_builder.add(char.get("name", ""))
            cn_builder.add(char.get("expression", {}).get("type", ""))

        cn_builder.add("古风动漫风格")
        cn_builder.add("高画质")
        cn_builder.add("精细画面")

        # 英文Prompt
        en_builder = PromptBuilder()
        camera_info = camera_work.get("ai_video_prompt", {})
        en_builder.add(camera_info.get("camera_motion_en", ""))
        en_builder.add(scene.get("location", ""))
        en_builder.add(scene.get("time_of_day", ""))

        if characters:
            char = characters[0]
            en_builder.add(char.get("costume", {}).get("description", ""))
            en_builder.add(char.get("pose", ""))

        en_builder.add("anime style")
        en_builder.add("cinematic")
        en_builder.add("high quality")

        return {
            "prompt": cn_builder.build(),
            "extended_prompt": en_builder.build(),
            "parameters": {
                "duration": self._estimate_duration([start_kf, end_kf]),
                "resolution": "1080p",
                "creativity": 0.7
            }
        }

    def _build_kling_prompt(
        self,
        start_kf: Dict,
        end_kf: Dict,
        camera_work: Dict,
        style_settings: Dict
    ) -> Dict[str, Any]:
        """构建Kling Prompt (简短)"""
        scene = start_kf.get("scene_description", {})
        characters = start_kf.get("characters", [])

        # Kling需要简短的关键词式Prompt
        builder = PromptBuilder()

        # 场景关键词
        builder.add(scene.get("location", ""))

        # 角色关键词
        if characters:
            char = characters[0]
            builder.add(char.get("name", ""))

        # 运动关键词
        movement = camera_work.get("movement", {})
        movement_type = movement.get("type", "static")
        movement_kw = {
            "dolly_in": "推进",
            "dolly_out": "拉远",
            "static": "静止",
            "arc": "环绕"
        }.get(movement_type, "")
        builder.add(movement_kw)

        # 风格关键词
        builder.add("古风")
        builder.add("动漫风格")

        # 情绪关键词
        if characters:
            expr = characters[0].get("expression", {}).get("type", "")
            expr_kw = {
                "sad": "忧郁",
                "happy": "欢快",
                "angry": "愤怒",
                "fearful": "恐惧",
                "contemplative": "沉思"
            }.get(expr, "")
            builder.add(expr_kw)

        return {
            "prompt": builder.build(),
            "motion_description": movement_kw,
            "parameters": {
                "duration": self._estimate_duration([start_kf, end_kf]),
                "mode": "standard"
            }
        }

    def _build_motion_guidance(
        self,
        camera_work: Dict,
        keyframes: List[Dict]
    ) -> Dict[str, Any]:
        """构建运动指导"""
        movement = camera_work.get("movement", {})
        characters = keyframes[0].get("characters", []) if keyframes else []

        return {
            "camera_movement": {
                "type": movement.get("type", "static"),
                "description": movement.get("description", ""),
                "speed": movement.get("speed_profile", "constant"),
                "smoothness": "high"
            },
            "character_motion": {
                "primary": characters[0].get("pose", "") if characters else "",
                "secondary": "",
                "subtle": "breathing motion"
            },
            "environment_motion": {
                "weather_effect": keyframes[0].get("scene_description", {}).get("weather", "clear"),
                "lighting_change": "subtle"
            }
        }

    def _build_style_consistency(
        self,
        style_settings: Dict,
        keyframes: List[Dict]
    ) -> Dict[str, Any]:
        """构建风格一致性设置"""
        return {
            "art_style": style_settings.get("art_style", "anime"),
            "era_style": style_settings.get("era_style", "ancient_chinese"),
            "color_palette": ["#2C3E50", "#E74C3C", "#ECF0F1"],  # 默认色板
            "lighting_style": "cinematic",
            "mood": keyframes[0].get("scene_description", {}).get("atmosphere", "neutral") if keyframes else "neutral"
        }

    def save_video_prompts(self, prompts_data: Dict, episode_id: str) -> Path:
        """保存视频Prompt"""
        episode_dir = self.path_config.episode_dir(episode_id)
        episode_dir.mkdir(parents=True, exist_ok=True)

        output_path = episode_dir / "video_prompts.json"
        save_json(prompts_data, output_path)
        return output_path

    def export_prompts_for_model(
        self,
        episode_id: str,
        model: str,
        output_dir: str = None
    ) -> Path:
        """导出特定模型的Prompt"""
        # 加载视频Prompts
        video_prompts_path = self.path_config.episode_dir(episode_id) / "video_prompts.json"
        if not video_prompts_path.exists():
            raise FileNotFoundError(f"视频Prompts不存在: {video_prompts_path}")

        video_prompts = load_json(video_prompts_path)

        # 提取特定模型的Prompt
        model_prompts = []
        for shot in video_prompts.get("shots", []):
            shot_prompts = {
                "shot_id": shot.get("shot_id"),
                "duration": shot.get("duration"),
                "prompt": shot.get("prompts", {}).get("video_prompt", {}).get(model, {})
            }
            model_prompts.append(shot_prompts)

        # 确定输出路径
        if output_dir:
            output_path = Path(output_dir) / f"{episode_id}_{model.lower()}_prompts.json"
        else:
            output_path = self.path_config.output_dir / episode_id / f"{model.lower()}_prompts.json"

        output_path.parent.mkdir(parents=True, exist_ok=True)
        save_json({
            "episode": video_prompts.get("episode"),
            "model": model,
            "prompts": model_prompts
        }, output_path)

        return output_path


def main():
    parser = argparse.ArgumentParser(description="Prompt工程师")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--episode", required=True, help="剧集ID")
    parser.add_argument("--model", default="all", choices=["all", "Sora2", "SeeDance", "Kling"], help="目标模型")
    parser.add_argument("--export", action="store_true", help="导出特定模型的Prompt")

    args = parser.parse_args()

    engineer = PromptEngineer(args.project)
    prompts_data = engineer.generate_video_prompts(args.episode, args.model)
    output_path = engineer.save_video_prompts(prompts_data, args.episode)

    print(f"视频Prompts生成完成: {output_path}")
    print(f"镜头数: {len(prompts_data['shots'])}")
    print(f"目标模型: {prompts_data['target_model']}")

    # 显示第一个镜头的Prompt
    if prompts_data['shots']:
        first_shot = prompts_data['shots'][0]
        print(f"\n第一个镜头 Sora2 Prompt:")
        sora2_prompt = first_shot.get('prompts', {}).get('video_prompt', {}).get('Sora2', {})
        if sora2_prompt:
            print(f"  {sora2_prompt.get('prompt', '')[:300]}...")

    # 导出
    if args.export and args.model != "all":
        for model in ["Sora2", "SeeDance", "Kling"]:
            export_path = engineer.export_prompts_for_model(args.episode, model)
            print(f"\n导出 {model} Prompts: {export_path}")


if __name__ == "__main__":
    main()
