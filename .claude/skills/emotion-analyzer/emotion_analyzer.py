#!/usr/bin/env python3
"""
Emotion Analyzer - 情绪分析师

分析故事情绪曲线，为配乐、运镜、色彩等提供情绪参考。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from utils import clean_text, ColorPalette


class EmotionAnalyzer:
    """情绪分析器"""

    # 情绪关键词映射
    EMOTION_KEYWORDS = {
        "happy": ['开心', '快乐', '欢笑', '高兴', '喜悦', '欣喜', '微笑', '灿烂', '甜蜜'],
        "sad": ['悲伤', '难过', '眼泪', '哭泣', '心痛', '忧伤', '泪流', '哀伤', '凄凉'],
        "angry": ['愤怒', '生气', '恼火', '暴怒', '愤恨', '怒火', '恼怒', '震怒'],
        "fearful": ['恐惧', '害怕', '惊恐', '颤抖', '不安', '惶恐', '畏惧', '胆寒'],
        "surprised": ['惊讶', '震惊', '意外', '吃惊', '诧异', '愕然', '瞠目'],
        "disgusted": ['厌恶', '反感', '作呕', '鄙夷', '不屑', '憎恶'],
        "contemplative": ['沉思', '思索', '思考', '犹豫', '困惑', '若有所思', '冥想'],
        "anticipation": ['期待', '盼望', '等待', '渴望', '憧憬', '企盼'],
        "trust": ['信任', '相信', '依赖', '依靠', '托付', '信赖'],
        "romantic": ['温柔', '深情', '爱恋', '缠绵', '眷恋', '柔情'],
    }

    # 情绪到视觉的映射
    EMOTION_VISUAL_MAP = {
        "happy": {
            "color_mood": "明亮暖色调",
            "lighting": "明亮柔和",
            "camera_style": "流畅稳定，欢快节奏"
        },
        "sad": {
            "color_mood": "冷色调偏蓝灰",
            "lighting": "昏暗低沉",
            "camera_style": "缓慢沉稳，下沉构图"
        },
        "angry": {
            "color_mood": "红色调",
            "lighting": "强烈对比",
            "camera_style": "快速剪辑，剧烈运动"
        },
        "fearful": {
            "color_mood": "冷色调偏黑",
            "lighting": "昏暗阴影重",
            "camera_style": "手持晃动，不安定"
        },
        "surprised": {
            "color_mood": "对比强烈",
            "lighting": "突变",
            "camera_style": "快速推拉"
        },
        "contemplative": {
            "color_mood": "柔和灰色调",
            "lighting": "柔和散射",
            "camera_style": "静止或缓慢推进"
        },
        "romantic": {
            "color_mood": "粉暖色调",
            "lighting": "柔美梦幻",
            "camera_style": "缓慢环绕，柔焦"
        },
        "mysterious": {
            "color_mood": "紫蓝深色调",
            "lighting": "局部照明",
            "camera_style": "缓慢探索，阴影强调"
        },
        "tense": {
            "color_mood": "暗绿色调",
            "lighting": "压抑暗淡",
            "camera_style": "紧绷，轻微晃动"
        },
    }

    # 情绪到音乐的映射
    EMOTION_AUDIO_MAP = {
        "happy": {"bgm_style": "欢快明亮", "bgm_tempo": "upbeat", "sfx_emphasis": ["鸟鸣", "风铃"]},
        "sad": {"bgm_style": "悲伤缓慢", "bgm_tempo": "slow_adagio", "sfx_emphasis": ["雨声", "风声"]},
        "angry": {"bgm_style": "激烈紧张", "bgm_tempo": "fast_staccato", "sfx_emphasis": ["鼓点", "金属撞击"]},
        "fearful": {"bgm_style": "悬疑紧张", "bgm_tempo": "irregular", "sfx_emphasis": ["心跳", "低频"]},
        "surprised": {"bgm_style": "突变停顿", "bgm_tempo": "sudden", "sfx_emphasis": ["铃声", "弦乐突响"]},
        "contemplative": {"bgm_style": "沉思冥想", "bgm_tempo": "slow_flowing", "sfx_emphasis": ["自然音"]},
        "romantic": {"bgm_style": "浪漫温柔", "bgm_tempo": "slow_waltz", "sfx_emphasis": ["弦乐", "钢琴"]},
        "mysterious": {"bgm_style": "神秘诡异", "bgm_tempo": "unsettling", "sfx_emphasis": ["环境音放大"]},
        "tense": {"bgm_style": "紧张悬疑", "bgm_tempo": "building", "sfx_emphasis": ["低频", "环境音"]},
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def analyze_emotions(self, chapter_id: str) -> Dict[str, Any]:
        """分析章节情绪"""
        # 加载故事分析结果
        analysis_path = self.path_config.analysis_cache_dir / f"{chapter_id}_analysis.json"
        if not analysis_path.exists():
            raise FileNotFoundError(f"请先运行 story_analyzer: {analysis_path}")

        analysis = load_json(analysis_path)

        # 构建情绪时间线
        emotion_timeline = self._build_emotion_timeline(analysis)

        # 识别情绪高峰
        emotion_peaks = self._identify_emotion_peaks(emotion_timeline)

        # 分析情绪转换
        emotion_transitions = self._analyze_transitions(emotion_timeline)

        # 分析角色情绪
        character_emotions = self._analyze_character_emotions(analysis)

        # 构建整体情绪曲线
        overall_curve = self._build_overall_curve(emotion_timeline)

        # 确定整体情绪基调
        overall_mood = self._determine_overall_mood(emotion_timeline)

        return {
            "chapter_id": chapter_id,
            "overall_mood": overall_mood,
            "emotion_timeline": emotion_timeline,
            "emotion_peaks": emotion_peaks,
            "emotion_transitions": emotion_transitions,
            "character_emotions": character_emotions,
            "overall_emotion_curve": overall_curve
        }

    def _build_emotion_timeline(self, analysis: Dict) -> List[Dict]:
        """构建情绪时间线"""
        timeline = []
        key_events = analysis.get("key_events", [])

        for i, event in enumerate(key_events):
            emotion = event.get("emotion", "neutral")
            intensity = event.get("importance", 5) / 10.0

            # 获取视觉和音频推荐
            visual_rec = self.EMOTION_VISUAL_MAP.get(emotion, self.EMOTION_VISUAL_MAP["contemplative"])
            audio_rec = self.EMOTION_AUDIO_MAP.get(emotion, self.EMOTION_AUDIO_MAP["contemplative"])

            segment = {
                "segment_id": f"seg_{i+1:03d}",
                "event_reference": event.get("event_id", ""),
                "text_position": {
                    "start": 0,  # 需要实际文本位置
                    "end": 0
                },
                "emotions": {
                    "primary": {
                        "type": emotion,
                        "intensity": round(intensity, 2)
                    },
                    "secondary": self._get_secondary_emotion(event.get("description", ""))
                },
                "visual_recommendations": visual_rec,
                "audio_recommendations": audio_rec,
                "pacing": self._determine_pacing(event.get("type", ""), intensity)
            }
            timeline.append(segment)

        return timeline

    def _get_secondary_emotion(self, text: str) -> Dict:
        """获取次要情绪"""
        emotion_scores = {}

        for emotion, keywords in self.EMOTION_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in text)
            if score > 0:
                emotion_scores[emotion] = score

        if emotion_scores:
            # 取得分第二高的
            sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
            if len(sorted_emotions) > 1:
                return {"type": sorted_emotions[1][0], "intensity": 0.3}

        return {"type": "neutral", "intensity": 0.2}

    def _determine_pacing(self, event_type: str, intensity: float) -> str:
        """确定节奏"""
        if event_type == "action":
            return "fast" if intensity > 0.6 else "medium_fast"
        elif event_type == "dialogue":
            return "medium"
        elif event_type in ["revelation", "conflict"]:
            return "building"
        else:
            return "slow_build"

    def _identify_emotion_peaks(self, timeline: List[Dict]) -> List[Dict]:
        """识别情绪高峰"""
        peaks = []

        for i, segment in enumerate(timeline):
            intensity = segment["emotions"]["primary"]["intensity"]

            # 局部最大值检测
            prev_intensity = timeline[i-1]["emotions"]["primary"]["intensity"] if i > 0 else 0
            next_intensity = timeline[i+1]["emotions"]["primary"]["intensity"] if i < len(timeline)-1 else 0

            if intensity >= prev_intensity and intensity >= next_intensity and intensity > 0.6:
                peak_type = "climax" if intensity > 0.8 else "tension_build"
                peaks.append({
                    "position": round(i / len(timeline), 2),
                    "type": peak_type,
                    "intensity": intensity,
                    "description": segment["emotions"]["primary"]["type"],
                    "resolution": "后续探索" if i < len(timeline) - 1 else "本章结束"
                })

        return peaks

    def _analyze_transitions(self, timeline: List[Dict]) -> List[Dict]:
        """分析情绪转换"""
        transitions = []

        for i in range(1, len(timeline)):
            prev_emotion = timeline[i-1]["emotions"]["primary"]["type"]
            curr_emotion = timeline[i]["emotions"]["primary"]["type"]

            if prev_emotion != curr_emotion:
                transitions.append({
                    "from": prev_emotion,
                    "to": curr_emotion,
                    "position": round(i / len(timeline), 2),
                    "trigger_event": timeline[i]["event_reference"],
                    "transition_type": "sudden" if timeline[i]["emotions"]["primary"]["intensity"] > 0.7 else "gradual"
                })

        return transitions

    def _analyze_character_emotions(self, analysis: Dict) -> Dict:
        """分析角色情绪"""
        character_emotions = {}

        character_arcs = analysis.get("character_arcs", {})
        for char_name, arc in character_arcs.items():
            # 构建情绪弧线
            arc_emotions = []
            if "state_before" in arc:
                arc_emotions.append(arc["state_before"])
            if "emotional_journey" in arc:
                # 简单提取情绪词
                journey = arc["emotional_journey"]
                for emotion in ["happy", "sad", "angry", "fearful", "contemplative", "determined"]:
                    if emotion in journey.lower():
                        arc_emotions.append(emotion)
            if "state_after" in arc:
                arc_emotions.append(arc["state_after"])

            character_emotions[char_name] = {
                "arc": arc_emotions if arc_emotions else ["neutral"],
                "key_moments": arc.get("key_moments", [])
            }

        return character_emotions

    def _build_overall_curve(self, timeline: List[Dict]) -> List[Dict]:
        """构建整体情绪曲线"""
        curve = []

        for i, segment in enumerate(timeline):
            position = round(i / max(len(timeline) - 1, 1), 2)
            curve.append({
                "position": position,
                "intensity": segment["emotions"]["primary"]["intensity"],
                "emotion": segment["emotions"]["primary"]["type"]
            })

        # 确保有起点和终点
        if curve:
            if curve[0]["position"] != 0.0:
                curve.insert(0, {"position": 0.0, "intensity": 0.5, "emotion": "neutral"})
            if curve[-1]["position"] != 1.0:
                curve.append({"position": 1.0, "intensity": curve[-1]["intensity"], "emotion": curve[-1]["emotion"]})

        return curve

    def _determine_overall_mood(self, timeline: List[Dict]) -> str:
        """确定整体情绪基调"""
        if not timeline:
            return "neutral"

        # 统计各情绪出现频率
        emotion_counts = {}
        for segment in timeline:
            emotion = segment["emotions"]["primary"]["type"]
            intensity = segment["emotions"]["primary"]["intensity"]
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + intensity

        # 找出主导情绪
        if emotion_counts:
            dominant = max(emotion_counts.items(), key=lambda x: x[1])
            return f"{dominant[0]}_dominant"

        return "neutral"

    def save_analysis(self, result: Dict, chapter_id: str) -> Path:
        """保存分析结果"""
        output_path = self.path_config.analysis_cache_dir / f"{chapter_id}_emotion.json"
        save_json(result, output_path)
        return output_path


def main():
    parser = argparse.ArgumentParser(description="情绪分析器")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--chapter", required=True, help="章节ID")
    parser.add_argument("--output", help="输出文件路径")

    args = parser.parse_args()

    analyzer = EmotionAnalyzer(args.project)
    result = analyzer.analyze_emotions(args.chapter)

    if args.output:
        output_path = Path(args.output)
        save_json(result, output_path)
    else:
        output_path = analyzer.save_analysis(result, args.chapter)

    print(f"情绪分析完成，结果保存到: {output_path}")
    print(f"整体情绪基调: {result['overall_mood']}")
    print(f"情绪高峰数: {len(result['emotion_peaks'])}")


if __name__ == "__main__":
    main()
