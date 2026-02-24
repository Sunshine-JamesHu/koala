#!/usr/bin/env python3
"""
Action Designer - 动作设计师

设计漫剧中的打斗、动作场面。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from utils import PromptBuilder, generate_id


@dataclass
class ActionBeat:
    """动作节拍"""
    beat_id: str
    time_start: float
    time_end: float
    setup: Dict[str, Any]
    action: Dict[str, Any]
    reaction: Dict[str, Any]
    camera: Dict[str, Any]
    sfx: List[Dict[str, Any]]
    keyframe: Dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ActionSequence:
    """动作序列"""
    action_sequence_id: str
    shot_id: str
    episode: int
    overview: Dict[str, Any]
    participants: List[Dict[str, Any]]
    environment_interaction: Dict[str, Any]
    action_beats: List[ActionBeat]
    key_poses: List[Dict[str, Any]]
    combat_flow: Dict[str, Any]
    visual_effects: Dict[str, Any]
    prompt_enhancements: Dict[str, Any]

    def to_dict(self) -> dict:
        return {
            "action_sequence_id": self.action_sequence_id,
            "shot_id": self.shot_id,
            "episode": self.episode,
            "overview": self.overview,
            "participants": self.participants,
            "environment_interaction": self.environment_interaction,
            "action_beats": [b.to_dict() for b in self.action_beats],
            "key_poses": self.key_poses,
            "combat_flow": self.combat_flow,
            "visual_effects": self.visual_effects,
            "prompt_enhancements": self.prompt_enhancements
        }


class ActionDesigner:
    """动作设计师"""

    # 武器类型
    WEAPON_TYPES = {
        "sword": {"name": "剑", "style": "灵动优雅", "prompt": "flexible sword"},
        "blade": {"name": "刀", "style": "凶猛直接", "prompt": "curved blade"},
        "spear": {"name": "枪", "style": "大开大合", "prompt": "long spear"},
        "dagger": {"name": "匕首", "style": "迅捷阴狠", "prompt": "short dagger"},
        "fist": {"name": "拳脚", "style": "刚猛", "prompt": "martial arts"}
    }

    # 动作类型
    ACTION_TYPES = {
        "attack": {"name": "攻击", "prompt": "attacking strike"},
        "defense": {"name": "防御", "prompt": "defensive block"},
        "dodge": {"name": "闪避", "prompt": "dodging movement"},
        "counter": {"name": "反击", "prompt": "counter attack"},
        "retreat": {"name": "后退", "prompt": "retreating"}
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def design_action(self, episode_id: str, shot_id: str) -> ActionSequence:
        """设计动作场面"""
        # 加载分镜脚本获取上下文
        storyboard_path = self.path_config.episode_dir(episode_id) / "storyboard.json"
        shot_data = {}

        if storyboard_path.exists():
            storyboard = load_json(storyboard_path)
            for shot in storyboard.get("shots", []):
                if shot.get("shot_id") == shot_id:
                    shot_data = shot
                    break

        # 提取参与者
        participants = self._extract_participants(shot_data)

        # 生成动作节拍
        duration = shot_data.get("duration", 5.0)
        action_beats = self._generate_action_beats(participants, duration)

        # 提取关键姿态
        key_poses = self._extract_key_poses(action_beats)

        # 生成动作Prompt增强
        prompt_enhancements = self._generate_prompt_enhancements(participants, action_beats)

        return ActionSequence(
            action_sequence_id=f"action_{shot_id}",
            shot_id=shot_id,
            episode=self._extract_episode_num(episode_id),
            overview={
                "type": "combat",
                "sub_type": "sword_fight",
                "intensity": "high",
                "duration": duration,
                "narrative_purpose": "展示角色武艺"
            },
            participants=participants,
            environment_interaction={
                "location": shot_data.get("scene", {}).get("location_name", ""),
                "usable_elements": [],
                "hazards": [],
                "destroyables": []
            },
            action_beats=action_beats,
            key_poses=key_poses,
            combat_flow={
                "rhythm": "fast_start -> pause -> fast_exchange",
                "tempo_description": "开始快速，中间对峙，最后决战",
                "breathing_points": []
            },
            visual_effects={
                "motion_blur": {"enabled": True, "intensity": "high"},
                "speed_lines": {"enabled": True, "style": "anime_style"},
                "impact_effects": [{"type": "sparks", "trigger": "武器碰撞"}],
                "particle_effects": [{"type": "dust", "trigger": "落地"}]
            },
            prompt_enhancements=prompt_enhancements
        )

    def _extract_participants(self, shot_data: Dict) -> List[Dict]:
        """提取参与者信息"""
        participants = []
        characters = shot_data.get("characters", [])

        for i, char in enumerate(characters):
            role = "protagonist" if i == 0 else "antagonist"
            participants.append({
                "character_id": char.get("character_id", ""),
                "name": char.get("name", ""),
                "role": role,
                "skill_level": "expert" if role == "protagonist" else "intermediate",
                "combat_style": "轻盈灵动" if role == "protagonist" else "凶猛直接",
                "weapon": "软剑" if role == "protagonist" else "短刀",
                "special_abilities": ["轻功"] if role == "protagonist" else []
            })

        return participants

    def _generate_action_beats(self, participants: List[Dict], duration: float) -> List[ActionBeat]:
        """生成动作节拍"""
        beats = []
        beat_duration = duration / 4  # 简化：4个节拍

        if len(participants) < 2:
            return beats

        attacker = participants[0]
        defender = participants[1] if len(participants) > 1 else participants[0]

        # 节拍1：攻击
        beats.append(ActionBeat(
            beat_id="beat_001",
            time_start=0,
            time_end=beat_duration,
            setup={
                "characters_positions": {
                    attacker["name"]: "左侧，蓄势待发",
                    defender["name"]: "右侧，防御姿态"
                },
                "initial_states": {
                    attacker["name"]: "准备攻击",
                    defender["name"]: "警觉防守"
                }
            },
            action={
                "primary_actor": attacker["name"],
                "action_type": "attack",
                "description": f"{attacker['name']}挥剑直刺",
                "trajectory": "直线突刺",
                "speed": "fast"
            },
            reaction={
                "reactor": defender["name"],
                "reaction_type": "defense",
                "description": "侧身闪避",
                "timing": "攻击即将命中时"
            },
            camera={
                "shot_size": "medium_shot",
                "angle": "side_angle",
                "movement": "follow attacker"
            },
            sfx=[{"type": "sword_swing", "time": 0.3}],
            keyframe={
                "keyframe_id": "kf_action_001",
                "time_in_beat": 0.8,
                "description": "剑锋即将命中的瞬间"
            }
        ))

        # 节拍2-4：类似结构...
        for i in range(1, 4):
            beat_start = i * beat_duration
            beat_end = (i + 1) * beat_duration

            action_type = ["counter", "attack", "clash"][i - 1] if i < 4 else "clash"

            beats.append(ActionBeat(
                beat_id=f"beat_{i+1:03d}",
                time_start=beat_start,
                time_end=beat_end,
                setup={"characters_positions": {}, "initial_states": {}},
                action={
                    "primary_actor": attacker["name"] if i % 2 == 0 else defender["name"],
                    "action_type": action_type,
                    "description": f"动作{i+1}",
                    "trajectory": "",
                    "speed": "fast"
                },
                reaction={
                    "reactor": defender["name"] if i % 2 == 0 else attacker["name"],
                    "reaction_type": "counter",
                    "description": "应对",
                    "timing": ""
                },
                camera={
                    "shot_size": "medium_shot",
                    "angle": "dynamic",
                    "movement": "quick pan"
                },
                sfx=[{"type": "sword_clash", "time": 0.5}],
                keyframe={
                    "keyframe_id": f"kf_action_{i+1:03d}",
                    "time_in_beat": 0.5,
                    "description": f"关键动作{i+1}"
                }
            ))

        return beats

    def _extract_key_poses(self, action_beats: List[ActionBeat]) -> List[Dict]:
        """提取关键姿态"""
        key_poses = []

        for beat in action_beats:
            if beat.keyframe:
                key_poses.append({
                    "pose_id": f"pose_{beat.beat_id}",
                    "beat": beat.beat_id,
                    "time": beat.time_start,
                    "character": beat.action.get("primary_actor", ""),
                    "description": beat.keyframe.get("description", ""),
                    "reference": ""
                })

        return key_poses

    def _generate_prompt_enhancements(
        self,
        participants: List[Dict],
        action_beats: List[ActionBeat]
    ) -> Dict[str, Any]:
        """生成Prompt增强"""
        builder = PromptBuilder()

        # 动作关键词
        builder.add("dynamic action")
        builder.add("martial arts")
        builder.add("sword fight")

        # 角色描述
        for p in participants:
            weapon_info = self.WEAPON_TYPES.get(p.get("weapon", "sword"), {})
            builder.add(weapon_info.get("prompt", ""))

        return {
            "action_keywords": ["dynamic action", "martial arts", "sword fight"],
            "style_keywords": ["wuxia style", "anime action", "dramatic choreography"],
            "motion_keywords": ["fast movement", "fluid motion", "impact frames"],
            "full_prompt": builder.build()
        }

    def _extract_episode_num(self, episode_id: str) -> int:
        """提取剧集编号"""
        try:
            return int(episode_id.replace("episode_", ""))
        except:
            return 1

    def save_action_design(self, action: ActionSequence, episode_id: str) -> Path:
        """保存动作设计"""
        episode_dir = self.path_config.episode_dir(episode_id)
        episode_dir.mkdir(parents=True, exist_ok=True)

        output_path = episode_dir / f"action_{action.shot_id}.json"
        save_json(action.to_dict(), output_path)
        return output_path


def main():
    parser = argparse.ArgumentParser(description="动作设计师")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--episode", required=True, help="剧集ID")
    parser.add_argument("--shot", required=True, help="镜头ID")

    args = parser.parse_args()

    designer = ActionDesigner(args.project)
    action = designer.design_action(args.episode, args.shot)
    output_path = designer.save_action_design(action, args.episode)

    print(f"动作设计完成: {output_path}")
    print(f"动作序列ID: {action.action_sequence_id}")
    print(f"参与者数: {len(action.participants)}")
    print(f"动作节拍数: {len(action.action_beats)}")


if __name__ == "__main__":
    main()
