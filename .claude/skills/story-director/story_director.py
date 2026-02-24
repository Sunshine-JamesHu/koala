#!/usr/bin/env python3
"""
Story Director - 分镜导演

将故事分析转化为详细的分镜脚本。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from models import (
    Shot, SceneInfo, CameraInfo, CharacterInShot, Dialogue,
    Storyboard, ShotSize, CameraAngle, CameraMovement, TimeOfDay, Weather
)
from utils import generate_id, clean_text


class StoryDirector:
    """分镜导演"""

    # 默认镜头时长
    DEFAULT_SHOT_DURATION = 5.0

    # 节拍类型映射
    BEAT_TYPE_MAP = {
        "opening": ["transition"],
        "rising_action": ["dialogue", "action", "conflict"],
        "climax": ["action", "revelation", "conflict"],
        "falling_action": ["dialogue", "resolution"],
        "resolution": ["resolution", "transition"]
    }

    # 事件类型到镜头类型的映射
    EVENT_TO_SHOT_TYPE = {
        "dialogue": "medium_shot",
        "action": "medium_full_shot",
        "revelation": "close_up",
        "conflict": "medium_shot",
        "resolution": "medium_shot",
        "transition": "long_shot"
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

        # 加载角色信息
        self.characters = self._load_characters()

    def _load_characters(self) -> Dict:
        """加载角色信息"""
        characters = {}
        char_dir = self.path_config.characters_dir

        if char_dir.exists():
            for char_folder in char_dir.iterdir():
                if char_folder.is_dir():
                    char_file = char_folder / "design.json"
                    if char_file.exists():
                        characters[char_folder.name] = load_json(char_file)

        return characters

    def create_storyboard(self, chapter_id: str, episode_id: str, title: str = "") -> Storyboard:
        """创建分镜脚本"""
        # 加载分析结果
        analysis_path = self.path_config.analysis_cache_dir / f"{chapter_id}_analysis.json"
        emotion_path = self.path_config.analysis_cache_dir / f"{chapter_id}_emotion.json"

        if not analysis_path.exists():
            raise FileNotFoundError(f"请先运行 story_analyzer: {analysis_path}")

        analysis = load_json(analysis_path)
        emotion_data = load_json(emotion_path) if emotion_path.exists() else {}

        # 提取剧集编号
        episode_num = int(episode_id.replace("episode_", ""))

        # 生成分镜
        shots = self._generate_shots(analysis, emotion_data)

        # 计算总时长
        total_duration = sum(s.duration for s in shots)

        # 生成标题
        if not title:
            title = f"第{episode_num}集"

        return Storyboard(
            episode=episode_num,
            title=title,
            source_chapter=chapter_id,
            total_duration=total_duration,
            shots=shots,
            art_style=self.project_config.art_style,
            era_style=self.project_config.era_style
        )

    def _generate_shots(self, analysis: Dict, emotion_data: Dict) -> List[Shot]:
        """生成镜头序列"""
        shots = []
        key_events = analysis.get("key_events", [])
        locations = analysis.get("locations", [])
        mood_curve = analysis.get("mood_curve", [])

        # 过滤重要事件
        important_events = [e for e in key_events if e.get("importance", 0) >= 5]

        if not important_events:
            # 如果没有重要事件，使用所有事件
            important_events = key_events

        # 根据事件生成镜头
        for i, event in enumerate(important_events):
            shot = self._create_shot_from_event(
                event=event,
                sequence=i + 1,
                total_events=len(important_events),
                locations=locations,
                emotion_data=emotion_data
            )
            shots.append(shot)

        # 添加过渡镜头（如果需要）
        shots = self._add_transition_shots(shots)

        return shots

    def _create_shot_from_event(
        self,
        event: Dict,
        sequence: int,
        total_events: int,
        locations: List[Dict],
        emotion_data: Dict
    ) -> Shot:
        """从事件创建镜头"""
        event_type = event.get("type", "dialogue")
        event_characters = event.get("characters", [])
        description = event.get("description", "")
        emotion = event.get("emotion", "neutral")

        # 确定节拍类型
        beat_type = self._determine_beat_type(sequence, total_events)

        # 创建场景信息
        scene = self._create_scene_info(event, locations)

        # 创建镜头信息
        camera = self._create_camera_info(event_type, emotion, sequence, total_events)

        # 创建角色信息
        characters = self._create_character_info(event_characters, description, emotion)

        # 创建对话信息
        dialogue = self._create_dialogue_info(event)

        # 确定时长
        duration = self._determine_duration(event_type, description)

        # 确定BGM情绪
        bgm_mood = self._determine_bgm_mood(emotion)

        return Shot(
            shot_id=f"shot_{sequence:03d}",
            sequence=sequence,
            source_event=event.get("event_id", ""),
            beat_type=beat_type,
            narrative_purpose=self._extract_narrative_purpose(description),
            duration=duration,
            scene=scene,
            camera=camera,
            characters=characters,
            dialogue=dialogue,
            narration="",
            bgm_mood=bgm_mood,
            sfx=[],
            transition_type="cut",
            notes=f"基于事件: {event.get('event_id', '')}"
        )

    def _determine_beat_type(self, sequence: int, total: int) -> str:
        """确定节拍类型"""
        if total <= 1:
            return "rising_action"

        position = sequence / total

        if position <= 0.15:
            return "opening"
        elif position <= 0.4:
            return "rising_action"
        elif position <= 0.6:
            return "climax"
        elif position <= 0.85:
            return "falling_action"
        else:
            return "resolution"

    def _create_scene_info(self, event: Dict, locations: List[Dict]) -> SceneInfo:
        """创建场景信息"""
        # 尝试匹配位置
        location_name = "未指定场景"
        location_type = "indoor"

        event_desc = event.get("description", "")
        for loc in locations:
            if loc.get("name", "") in event_desc:
                location_name = loc.get("name", "未指定场景")
                location_type = loc.get("type", "indoor")
                break

        # 推断时间段
        time_of_day = self._infer_time_of_day(event_desc)

        # 推断天气
        weather = self._infer_weather(event_desc)

        return SceneInfo(
            location_id=f"loc_{hash(location_name) % 1000:03d}",
            location_name=location_name,
            location_type=location_type,
            time_of_day=time_of_day,
            weather=weather,
            lighting="",
            atmosphere=""
        )

    def _infer_time_of_day(self, text: str) -> str:
        """推断时间段"""
        if any(w in text for w in ['夜', '月', '烛', '灯']):
            return "night"
        elif any(w in text for w in ['晨', '晓', '拂晓']):
            return "dawn"
        elif any(w in text for w in ['暮', '黄昏', '夕阳']):
            return "dusk"
        elif any(w in text for w in ['午', '正午']):
            return "noon"
        else:
            return "day"

    def _infer_weather(self, text: str) -> str:
        """推断天气"""
        if any(w in text for w in ['雨', '淋', '湿']):
            return "rain"
        elif any(w in text for w in ['雪', '飘雪']):
            return "snow"
        elif any(w in text for w in ['雾', '霾']):
            return "fog"
        elif any(w in text for w in ['风', '狂风']):
            return "storm"
        else:
            return "clear"

    def _create_camera_info(
        self,
        event_type: str,
        emotion: str,
        sequence: int,
        total: int
    ) -> CameraInfo:
        """创建镜头信息"""
        # 根据事件类型选择镜头尺寸
        shot_size = self.EVENT_TO_SHOT_TYPE.get(event_type, "medium_shot")

        # 根据情绪选择角度
        angle = self._select_camera_angle(emotion)

        # 根据位置选择运镜
        movement = self._select_camera_movement(sequence, total, emotion)

        return CameraInfo(
            shot_size=shot_size,
            angle=angle,
            movement_type=movement["type"],
            movement_direction=movement["direction"],
            movement_speed=movement["speed"],
            focus_subject=""
        )

    def _select_camera_angle(self, emotion: str) -> str:
        """选择镜头角度"""
        angle_map = {
            "happy": "eye_level",
            "sad": "high_angle",
            "angry": "low_angle",
            "fearful": "dutch_angle",
            "surprised": "eye_level",
            "contemplative": "eye_level",
            "romantic": "slightly_low",
            "mysterious": "dutch_angle"
        }
        return angle_map.get(emotion, "eye_level")

    def _select_camera_movement(self, sequence: int, total: int, emotion: str) -> Dict:
        """选择运镜方式"""
        # 基于情绪选择
        if emotion in ["angry", "fearful", "surprised"]:
            return {"type": "dolly_in", "direction": "in", "speed": "fast"}
        elif emotion in ["sad", "contemplative"]:
            return {"type": "static", "direction": "", "speed": ""}
        elif emotion in ["romantic"]:
            return {"type": "arc", "direction": "around", "speed": "slow"}
        else:
            # 基于位置选择
            if sequence == 1:
                return {"type": "dolly_in", "direction": "in", "speed": "slow"}
            elif sequence == total:
                return {"type": "dolly_out", "direction": "out", "speed": "slow"}
            else:
                return {"type": "static", "direction": "", "speed": ""}

    def _create_character_info(
        self,
        event_characters: List[str],
        description: str,
        emotion: str
    ) -> List[CharacterInShot]:
        """创建角色信息"""
        characters = []

        if not event_characters:
            # 尝试从描述中提取
            for char_name in self.characters.keys():
                if char_name in description:
                    event_characters.append(char_name)

        for i, char_name in enumerate(event_characters[:3]):  # 最多3个角色
            char_data = self.characters.get(char_name, {})

            characters.append(CharacterInShot(
                character_id=f"char_{hash(char_name) % 1000:03d}",
                name=char_name,
                importance="primary" if i == 0 else "secondary",
                position="center" if i == 0 else ("left" if i == 1 else "right"),
                pose="",
                action=self._extract_action(description),
                expression=emotion,
                expression_intensity="moderate",
                costume_id=char_data.get("costumes", [{}])[0].get("costume_id", "") if char_data else "",
                gaze_direction=""
            ))

        return characters

    def _extract_action(self, text: str) -> str:
        """提取动作描述"""
        action_verbs = ['走', '跑', '坐', '站', '躺', '跪', '转身', '抬头', '低头']
        for verb in action_verbs:
            if verb in text:
                # 尝试提取包含动词的短语
                idx = text.find(verb)
                start = max(0, idx - 5)
                end = min(len(text), idx + 10)
                return text[start:end]
        return ""

    def _create_dialogue_info(self, event: Dict) -> Optional[Dialogue]:
        """创建对话信息"""
        snippets = event.get("dialogue_snippets", [])
        if snippets:
            return Dialogue(
                speaker="",  # 需要额外分析
                text=snippets[0],
                tone="normal",
                pace="normal",
                volume="normal"
            )
        return None

    def _determine_duration(self, event_type: str, description: str) -> float:
        """确定镜头时长"""
        base_duration = self.DEFAULT_SHOT_DURATION

        # 根据事件类型调整
        type_duration = {
            "action": 4.0,
            "dialogue": 6.0,
            "revelation": 5.0,
            "conflict": 4.0,
            "transition": 3.0
        }
        base_duration = type_duration.get(event_type, base_duration)

        # 根据描述长度调整
        if len(description) > 200:
            base_duration += 1.0
        elif len(description) < 50:
            base_duration -= 1.0

        return max(2.0, min(10.0, base_duration))

    def _determine_bgm_mood(self, emotion: str) -> str:
        """确定BGM情绪"""
        mood_map = {
            "happy": "欢快明亮",
            "sad": "悲伤缓慢",
            "angry": "激烈紧张",
            "fearful": "悬疑紧张",
            "surprised": "突变",
            "contemplative": "沉思冥想",
            "romantic": "浪漫温柔",
            "mysterious": "神秘诡异"
        }
        return mood_map.get(emotion, "中性")

    def _extract_narrative_purpose(self, description: str) -> str:
        """提取叙事目的"""
        # 简化版本：截取描述前50字
        if len(description) > 50:
            return description[:50] + "..."
        return description

    def _add_transition_shots(self, shots: List[Shot]) -> List[Shot]:
        """添加过渡镜头"""
        # 简化版本：如果场景切换，添加建立镜头
        result = []
        prev_location = None

        for shot in shots:
            current_location = shot.scene.location_name if shot.scene else None

            # 如果场景变化，可以考虑添加建立镜头
            if prev_location and current_location and prev_location != current_location:
                # 这里可以插入一个场景建立镜头
                pass

            result.append(shot)
            prev_location = current_location

        return result

    def save_storyboard(self, storyboard: Storyboard, episode_id: str) -> Path:
        """保存分镜脚本"""
        episode_dir = self.path_config.episode_dir(episode_id)
        episode_dir.mkdir(parents=True, exist_ok=True)

        output_path = episode_dir / "storyboard.json"
        save_json(storyboard.to_dict(), output_path)
        return output_path


def main():
    parser = argparse.ArgumentParser(description="分镜导演")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--chapter", required=True, help="章节ID")
    parser.add_argument("--episode", required=True, help="剧集ID (如: episode_001)")
    parser.add_argument("--title", default="", help="剧集标题")

    args = parser.parse_args()

    director = StoryDirector(args.project)
    storyboard = director.create_storyboard(args.chapter, args.episode, args.title)
    output_path = director.save_storyboard(storyboard, args.episode)

    print(f"分镜脚本生成完成: {output_path}")
    print(f"剧集: {storyboard.title}")
    print(f"总镜头数: {len(storyboard.shots)}")
    print(f"总时长: {storyboard.total_duration:.1f}秒")


if __name__ == "__main__":
    main()
