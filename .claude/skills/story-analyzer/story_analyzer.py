#!/usr/bin/env python3
"""
Story Analyzer - 故事分析师

分析小说章节，提取关键事件、角色弧线、情绪曲线等。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

# 添加lib路径
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, get_chapter_text, save_json, PathConfig
from models import KeyEvent, CharacterArc, MoodPoint, AnalysisResult
from utils import clean_text, split_into_paragraphs, extract_dialogues, generate_id


class StoryAnalyzer:
    """故事分析器"""

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def analyze_chapter(self, chapter_id: str) -> AnalysisResult:
        """分析章节"""
        # 读取章节文本
        text = get_chapter_text(self.path_config, chapter_id)
        word_count = len(text)

        # 分割段落
        paragraphs = split_into_paragraphs(text)

        # 提取关键事件
        key_events = self._extract_key_events(paragraphs, text)

        # 分析角色弧线
        character_arcs = self._analyze_character_arcs(paragraphs, text)

        # 识别场景
        locations = self._identify_locations(paragraphs, text)

        # 绘制情绪曲线
        mood_curve = self._build_mood_curve(key_events)

        # 识别冲突
        conflicts = self._identify_conflicts(paragraphs, text)

        # 评估节奏
        pacing = self._assess_pacing(paragraphs, key_events)

        # 提取视觉亮点
        visual_highlights = self._extract_visual_highlights(paragraphs, text)

        # 生成摘要
        summary = self._generate_summary(text, key_events)

        return AnalysisResult(
            chapter_id=chapter_id,
            word_count=word_count,
            summary=summary,
            key_events=key_events,
            character_arcs=character_arcs,
            locations=locations,
            mood_curve=mood_curve,
            conflicts=conflicts,
            pacing=pacing,
            visual_highlights=visual_highlights
        )

    def _extract_key_events(self, paragraphs: List[str], full_text: str) -> List[KeyEvent]:
        """提取关键事件"""
        events = []

        # 提取对话
        dialogues = extract_dialogues(full_text)

        # 基于段落和对话构建事件
        event_id = 1
        for i, para in enumerate(paragraphs):
            if len(para) < 20:  # 跳过太短的段落
                continue

            # 分析事件类型
            event_type = self._classify_event_type(para)

            # 提取涉及的角色
            characters = self._extract_characters(para)

            # 评估重要性
            importance = self._assess_importance(para, event_type)

            # 评估视觉潜力
            visual_potential = self._assess_visual_potential(para, event_type)

            # 提取对话片段
            para_dialogues = [d["text"] for d in dialogues if d["text"] in para]

            event = KeyEvent(
                event_id=f"evt_{event_id:03d}",
                type=event_type,
                description=clean_text(para[:200]) if len(para) > 200 else clean_text(para),
                characters=characters,
                location="",  # 后续填充
                emotion=self._detect_emotion(para),
                importance=importance,
                visual_potential=visual_potential,
                dialogue_snippets=para_dialogues[:3]  # 最多3条
            )
            events.append(event)
            event_id += 1

        return events

    def _classify_event_type(self, text: str) -> str:
        """分类事件类型"""
        text_lower = text.lower()

        # 对话标记
        dialogue_markers = ['"', '"', '「', '说', '道', '问', '答', '笑', '叹']
        if any(m in text for m in dialogue_markers):
            return "dialogue"

        # 动作标记
        action_markers = ['走', '跑', '打', '杀', '跳', '飞', '抓', '推', '拉', '斩', '刺']
        if any(m in text for m in action_markers):
            return "action"

        # 揭示标记
        revelation_markers = ['发现', '原来', '竟是', '没想到', '突然明白', '恍然']
        if any(m in text for m in revelation_markers):
            return "revelation"

        # 冲突标记
        conflict_markers = ['冲突', '争吵', '对峙', '矛盾', '危机', '威胁']
        if any(m in text for m in conflict_markers):
            return "conflict"

        # 解决标记
        resolution_markers = ['终于', '成功', '解决', '和解', '释然', '放下']
        if any(m in text for m in resolution_markers):
            return "resolution"

        return "transition"

    def _extract_characters(self, text: str) -> List[str]:
        """提取文本中出现的角色名"""
        # 这里需要基于项目角色列表来匹配
        # 简化版本：检测常见名字模式
        characters = []

        # 从角色目录获取角色列表
        characters_dir = self.path_config.characters_dir
        if characters_dir.exists():
            for char_dir in characters_dir.iterdir():
                if char_dir.is_dir() and char_dir.name in text:
                    characters.append(char_dir.name)

        return characters

    def _assess_importance(self, text: str, event_type: str) -> int:
        """评估事件重要性 (1-10)"""
        score = 5  # 基础分

        # 根据事件类型调整
        type_scores = {
            "revelation": 8,
            "conflict": 7,
            "resolution": 8,
            "action": 6,
            "dialogue": 5,
            "transition": 3
        }
        score = type_scores.get(event_type, 5)

        # 根据文本长度调整
        if len(text) > 200:
            score += 1

        # 根据关键标记调整
        high_importance_markers = ['重要', '关键', '转折', '震惊', '意外']
        if any(m in text for m in high_importance_markers):
            score += 2

        return min(10, max(1, score))

    def _assess_visual_potential(self, text: str, event_type: str) -> str:
        """评估视觉潜力"""
        # 动作和揭示场景通常有高视觉潜力
        if event_type in ["action", "revelation"]:
            return "high"

        # 检查视觉描述标记
        visual_markers = ['看着', '望向', '映入眼帘', '出现在', '景色', '光影', '色彩']
        if any(m in text for m in visual_markers):
            return "high"

        # 检查对话为主的场景
        if event_type == "dialogue" and text.count('"') > 4:
            return "medium"

        return "medium"

    def _detect_emotion(self, text: str) -> str:
        """检测文本情绪"""
        emotion_keywords = {
            "happy": ['开心', '快乐', '欢笑', '高兴', '喜悦', '欣喜'],
            "sad": ['悲伤', '难过', '眼泪', '哭泣', '心痛', '忧伤'],
            "angry": ['愤怒', '生气', '恼火', '暴怒', '愤恨'],
            "fearful": ['恐惧', '害怕', '惊恐', '颤抖', '不安'],
            "surprised": ['惊讶', '震惊', '意外', '吃惊', '诧异'],
            "contemplative": ['沉思', '思索', '思考', '犹豫', '困惑'],
        }

        for emotion, keywords in emotion_keywords.items():
            if any(kw in text for kw in keywords):
                return emotion

        return "neutral"

    def _analyze_character_arcs(self, paragraphs: List[str], full_text: str) -> Dict[str, CharacterArc]:
        """分析角色弧线"""
        arcs = {}

        # 获取项目角色
        characters_dir = self.path_config.characters_dir
        if not characters_dir.exists():
            return arcs

        for char_dir in characters_dir.iterdir():
            if not char_dir.is_dir():
                continue

            char_name = char_dir.name
            char_paragraphs = [p for p in paragraphs if char_name in p]

            if not char_paragraphs:
                continue

            # 简化分析：基于首尾段落推断状态变化
            first_mention = char_paragraphs[0] if char_paragraphs else ""
            last_mention = char_paragraphs[-1] if char_paragraphs else ""

            arcs[char_name] = CharacterArc(
                state_before=self._detect_emotion(first_mention) or "未知状态",
                state_after=self._detect_emotion(last_mention) or "未知状态",
                emotional_journey=f"从{self._detect_emotion(first_mention)}到{self._detect_emotion(last_mention)}",
                key_moments=[p[:100] + "..." for p in char_paragraphs[:3] if len(p) > 100]
            )

        return arcs

    def _identify_locations(self, paragraphs: List[str], full_text: str) -> List[Dict[str, Any]]:
        """识别场景/位置"""
        locations = []
        seen_locations = set()

        # 常见位置标记
        location_patterns = [
            r'在([^，。？！]+里|[^，。？！]+中|[^，。？！]+内)',
            r'来到([^，。？！]+)',
            r'进入([^，。？！]+)',
            r'([^，。？！]+前|[^，。？！]+后|[^，。？！]+旁)',
        ]

        import re
        for para in paragraphs:
            for pattern in location_patterns:
                matches = re.findall(pattern, para)
                for match in matches:
                    loc = match.strip()
                    if loc and len(loc) < 20 and loc not in seen_locations:
                        seen_locations.add(loc)
                        locations.append({
                            "name": loc,
                            "type": "indoor" if any(w in loc for w in ['房', '厅', '殿', '阁', '室']) else "outdoor",
                            "first_appearance": "",
                            "atmosphere": ""
                        })

        return locations[:10]  # 最多返回10个位置

    def _build_mood_curve(self, key_events: List[KeyEvent]) -> List[MoodPoint]:
        """构建情绪曲线"""
        if not key_events:
            return [MoodPoint(position=0.0, intensity=0.5, emotion="neutral", trigger_event="")]

        curve = []
        for i, event in enumerate(key_events):
            position = i / len(key_events)

            # 根据事件重要性计算强度
            intensity = event.importance / 10.0

            curve.append(MoodPoint(
                position=round(position, 2),
                intensity=round(intensity, 2),
                emotion=event.emotion,
                trigger_event=event.event_id
            ))

        return curve

    def _identify_conflicts(self, paragraphs: List[str], full_text: str) -> List[Dict[str, Any]]:
        """识别冲突"""
        conflicts = []

        conflict_patterns = [
            (['与', '和', '跟'], '对抗', 'person_vs_person'),
            (['内心', '心里', '心中'], '挣扎', 'person_vs_self'),
            (['环境', '天气', '困境'], '对抗', 'person_vs_environment'),
        ]

        for para in paragraphs:
            for triggers, action, conflict_type in conflict_patterns:
                if any(t in para for t in triggers) and action in para:
                    conflicts.append({
                        "type": conflict_type,
                        "parties": [],
                        "description": para[:100] + "..." if len(para) > 100 else para,
                        "resolution_status": "unresolved"
                    })

        return conflicts[:5]  # 最多返回5个冲突

    def _assess_pacing(self, paragraphs: List[str], key_events: List[KeyEvent]) -> Dict[str, str]:
        """评估节奏"""
        if not key_events:
            return {"overall": "medium", "recommendation": "需要更多内容"}

        # 基于事件密度和类型评估
        high_importance_count = sum(1 for e in key_events if e.importance >= 7)
        action_count = sum(1 for e in key_events if e.type == "action")

        if high_importance_count > len(key_events) * 0.5 or action_count > len(key_events) * 0.3:
            overall = "fast"
            recommendation = "节奏较快，注意给予观众喘息时间"
        elif high_importance_count < len(key_events) * 0.2:
            overall = "slow"
            recommendation = "节奏较慢，可适当增加冲突点"
        else:
            overall = "medium"
            recommendation = "节奏适中，保持当前节奏"

        return {"overall": overall, "recommendation": recommendation}

    def _extract_visual_highlights(self, paragraphs: List[str], full_text: str) -> List[str]:
        """提取视觉亮点"""
        highlights = []

        visual_keywords = [
            '月光', '阳光', '烛光', '火光', '星光',
            '美丽', '壮观', '震撼', '绚丽', '幽暗',
            '鲜血', '泪水', '微笑', '怒容', '表情'
        ]

        for para in paragraphs:
            if any(kw in para for kw in visual_keywords):
                highlight = para[:150] + "..." if len(para) > 150 else para
                if highlight not in highlights:
                    highlights.append(highlight)

        return highlights[:5]  # 最多返回5个亮点

    def _generate_summary(self, full_text: str, key_events: List[KeyEvent]) -> str:
        """生成章节摘要"""
        if not key_events:
            return "无法生成摘要"

        # 取前3个最重要的事件作为摘要基础
        important_events = sorted(key_events, key=lambda e: e.importance, reverse=True)[:3]

        summary_parts = []
        for event in important_events:
            desc = event.description
            if len(desc) > 50:
                desc = desc[:50] + "..."
            summary_parts.append(desc)

        return "；".join(summary_parts)

    def save_analysis(self, result: AnalysisResult) -> Path:
        """保存分析结果"""
        output_path = self.path_config.analysis_cache_dir / f"{result.chapter_id}_analysis.json"
        save_json(result.to_dict(), output_path)
        return output_path


def main():
    parser = argparse.ArgumentParser(description="故事分析器")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--chapter", required=True, help="章节ID (如: chapter_001)")
    parser.add_argument("--output", help="输出文件路径 (可选)")

    args = parser.parse_args()

    analyzer = StoryAnalyzer(args.project)
    result = analyzer.analyze_chapter(args.chapter)

    if args.output:
        output_path = Path(args.output)
        save_json(result.to_dict(), output_path)
    else:
        output_path = analyzer.save_analysis(result)

    print(f"分析完成，结果保存到: {output_path}")
    print(f"摘要: {result.summary}")
    print(f"关键事件数: {len(result.key_events)}")


if __name__ == "__main__":
    main()
