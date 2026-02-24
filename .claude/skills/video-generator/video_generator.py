#!/usr/bin/env python3
"""
Video Generator - 视频生成协调器

漫剧Agent Teams的主控协调器，统筹整个生成流程。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig


@dataclass
class PipelineStep:
    """流水线步骤"""
    name: str
    status: str  # pending, running, completed, failed
    start_time: str = ""
    end_time: str = ""
    output_path: str = ""
    error: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class VideoGenerator:
    """视频生成协调器"""

    # 流水线步骤定义
    PIPELINE_STEPS = [
        {"name": "analyze", "description": "故事分析与情绪分析"},
        {"name": "storyboard", "description": "分镜脚本生成"},
        {"name": "design", "description": "资源设计（角色/场景）"},
        {"name": "camera", "description": "运镜方案设计"},
        {"name": "keyframe", "description": "关键帧提取"},
        {"name": "prompt", "description": "视频Prompt生成"},
        {"name": "output", "description": "输出整理"}
    ]

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

        # 初始化流水线状态
        self.pipeline_status = {
            step["name"]: PipelineStep(name=step["name"], status="pending")
            for step in self.PIPELINE_STEPS
        }

    def run_full_pipeline(
        self,
        chapter_id: str,
        episode_id: str,
        episode_title: str = ""
    ) -> Dict[str, Any]:
        """运行完整流水线"""
        print(f"\n{'='*60}")
        print(f"开始处理: {chapter_id} -> {episode_id}")
        print(f"{'='*60}\n")

        report = {
            "project": self.project_config.name,
            "chapter": chapter_id,
            "episode": episode_id,
            "started_at": datetime.now().isoformat(),
            "steps": [],
            "statistics": {},
            "outputs": {},
            "errors": [],
            "warnings": []
        }

        try:
            # Step 1: 分析
            self._update_step_status("analyze", "running")
            analysis_result = self._run_analysis(chapter_id)
            self._update_step_status("analyze", "completed", analysis_result.get("output_path", ""))
            report["steps"].append(self.pipeline_status["analyze"].to_dict())

            # Step 2: 分镜
            self._update_step_status("storyboard", "running")
            storyboard_result = self._run_storyboard(chapter_id, episode_id, episode_title)
            self._update_step_status("storyboard", "completed", storyboard_result.get("output_path", ""))
            report["steps"].append(self.pipeline_status["storyboard"].to_dict())

            # Step 3: 设计（可选，如果有新角色/场景）
            self._update_step_status("design", "running")
            design_result = self._run_design(episode_id)
            self._update_step_status("design", "completed")
            report["steps"].append(self.pipeline_status["design"].to_dict())

            # Step 4: 运镜
            self._update_step_status("camera", "running")
            camera_result = self._run_camera(episode_id)
            self._update_step_status("camera", "completed", camera_result.get("output_path", ""))
            report["steps"].append(self.pipeline_status["camera"].to_dict())

            # Step 5: 关键帧
            self._update_step_status("keyframe", "running")
            keyframe_result = self._run_keyframe(episode_id)
            self._update_step_status("keyframe", "completed", keyframe_result.get("output_path", ""))
            report["steps"].append(self.pipeline_status["keyframe"].to_dict())

            # Step 6: Prompt
            self._update_step_status("prompt", "running")
            prompt_result = self._run_prompt(episode_id)
            self._update_step_status("prompt", "completed", prompt_result.get("output_path", ""))
            report["steps"].append(self.pipeline_status["prompt"].to_dict())

            # Step 7: 输出
            self._update_step_status("output", "running")
            output_result = self._generate_output(episode_id)
            self._update_step_status("output", "completed")
            report["steps"].append(self.pipeline_status["output"].to_dict())

            # 生成统计和报告
            report["statistics"] = self._collect_statistics(episode_id)
            report["outputs"] = output_result

        except Exception as e:
            report["errors"].append(str(e))
            # 标记当前步骤为失败
            for step_name, step in self.pipeline_status.items():
                if step.status == "running":
                    step.status = "failed"
                    step.error = str(e)
                    report["steps"].append(step.to_dict())
                    break

        report["completed_at"] = datetime.now().isoformat()
        report["success"] = len(report["errors"]) == 0

        # 保存报告
        report_path = self._save_report(report, episode_id)
        report["report_path"] = str(report_path)

        return report

    def _update_step_status(
        self,
        step_name: str,
        status: str,
        output_path: str = "",
        error: str = ""
    ):
        """更新步骤状态"""
        step = self.pipeline_status.get(step_name)
        if step:
            step.status = status
            if status == "running":
                step.start_time = datetime.now().isoformat()
            elif status in ["completed", "failed"]:
                step.end_time = datetime.now().isoformat()
            step.output_path = output_path
            step.error = error

            print(f"[{step_name}] {status}" + (f" -> {output_path}" if output_path else ""))

    def _run_analysis(self, chapter_id: str) -> Dict[str, Any]:
        """运行分析步骤"""
        # 导入分析器
        sys.path.insert(0, str(Path(__file__).parent.parent / "story-analyzer"))
        from story_analyzer import StoryAnalyzer

        sys.path.insert(0, str(Path(__file__).parent.parent / "emotion-analyzer"))
        from emotion_analyzer import EmotionAnalyzer

        # 故事分析
        print("  运行故事分析...")
        story_analyzer = StoryAnalyzer(self.project_config.name)
        analysis_result = story_analyzer.analyze_chapter(chapter_id)
        analysis_path = story_analyzer.save_analysis(analysis_result)

        # 情绪分析
        print("  运行情绪分析...")
        emotion_analyzer = EmotionAnalyzer(self.project_config.name)
        emotion_result = emotion_analyzer.analyze_emotions(chapter_id)
        emotion_path = emotion_analyzer.save_analysis(emotion_result, chapter_id)

        return {
            "output_path": str(analysis_path),
            "emotion_path": str(emotion_path)
        }

    def _run_storyboard(
        self,
        chapter_id: str,
        episode_id: str,
        title: str
    ) -> Dict[str, Any]:
        """运行分镜步骤"""
        sys.path.insert(0, str(Path(__file__).parent.parent / "story-director"))
        from story_director import StoryDirector

        print("  生成分镜脚本...")
        director = StoryDirector(self.project_config.name)
        storyboard = director.create_storyboard(chapter_id, episode_id, title)
        output_path = director.save_storyboard(storyboard, episode_id)

        return {"output_path": str(output_path)}

    def _run_design(self, episode_id: str) -> Dict[str, Any]:
        """运行设计步骤（检查是否需要新建角色/场景）"""
        # 加载分镜脚本
        storyboard_path = self.path_config.episode_dir(episode_id) / "storyboard.json"
        if not storyboard_path.exists():
            return {"skipped": True, "reason": "分镜脚本不存在"}

        storyboard = load_json(storyboard_path)
        shots = storyboard.get("shots", [])

        # 收集需要的角色和场景
        required_characters = set()
        required_scenes = set()

        for shot in shots:
            for char in shot.get("characters", []):
                required_characters.add(char.get("name", ""))
            scene = shot.get("scene", {})
            if scene.get("location_name"):
                required_scenes.add(scene.get("location_name"))

        # 检查现有资源
        existing_characters = set()
        existing_scenes = set()

        char_dir = self.path_config.characters_dir
        if char_dir.exists():
            for d in char_dir.iterdir():
                if d.is_dir():
                    existing_characters.add(d.name)

        scene_dir = self.path_config.scenes_dir
        if scene_dir.exists():
            for type_dir in scene_dir.iterdir():
                if type_dir.is_dir():
                    for d in type_dir.iterdir():
                        if d.is_dir():
                            existing_scenes.add(d.name)

        # 报告缺失资源
        missing_characters = required_characters - existing_characters - {""}
        missing_scenes = required_scenes - existing_scenes - {""}

        result = {
            "required_characters": list(required_characters - {""}),
            "required_scenes": list(required_scenes - {""}),
            "missing_characters": list(missing_characters),
            "missing_scenes": list(missing_scenes)
        }

        if missing_characters or missing_scenes:
            print(f"  警告: 缺少资源")
            if missing_characters:
                print(f"    缺少角色: {missing_characters}")
            if missing_scenes:
                print(f"    缺少场景: {missing_scenes}")

        return result

    def _run_camera(self, episode_id: str) -> Dict[str, Any]:
        """运行运镜步骤"""
        sys.path.insert(0, str(Path(__file__).parent.parent / "cinematographer"))
        from cinematographer import Cinematographer

        print("  设计运镜方案...")
        cinematographer = Cinematographer(self.project_config.name)
        camera_work = cinematographer.design_camera_work(episode_id)
        output_path = cinematographer.save_camera_work(camera_work, episode_id)

        return {"output_path": str(output_path)}

    def _run_keyframe(self, episode_id: str) -> Dict[str, Any]:
        """运行关键帧提取步骤"""
        sys.path.insert(0, str(Path(__file__).parent.parent / "keyframe-extractor"))
        from keyframe_extractor import KeyframeExtractor

        print("  提取关键帧...")
        extractor = KeyframeExtractor(self.project_config.name)
        keyframes_data = extractor.extract_keyframes(episode_id)
        output_path = extractor.save_keyframes(keyframes_data, episode_id)

        return {"output_path": str(output_path)}

    def _run_prompt(self, episode_id: str) -> Dict[str, Any]:
        """运行Prompt生成步骤"""
        sys.path.insert(0, str(Path(__file__).parent.parent / "prompt-engineer"))
        from prompt_engineer import PromptEngineer

        print("  生成视频Prompt...")
        engineer = PromptEngineer(self.project_config.name)
        prompts_data = engineer.generate_video_prompts(episode_id, "all")
        output_path = engineer.save_video_prompts(prompts_data, episode_id)

        return {"output_path": str(output_path)}

    def _generate_output(self, episode_id: str) -> Dict[str, Any]:
        """生成输出整理"""
        print("  整理输出...")

        episode_dir = self.path_config.episode_dir(episode_id)
        output_dir = self.path_config.output_dir / episode_id
        output_dir.mkdir(parents=True, exist_ok=True)

        outputs = {
            "storyboard": str(episode_dir / "storyboard.json"),
            "camera_work": str(episode_dir / "camera_work.json"),
            "keyframes": str(episode_dir / "keyframes.json"),
            "video_prompts": str(episode_dir / "video_prompts.json")
        }

        return outputs

    def _collect_statistics(self, episode_id: str) -> Dict[str, Any]:
        """收集统计信息"""
        stats = {}

        # 从分镜脚本获取统计
        storyboard_path = self.path_config.episode_dir(episode_id) / "storyboard.json"
        if storyboard_path.exists():
            storyboard = load_json(storyboard_path)
            stats["total_shots"] = len(storyboard.get("shots", []))
            stats["total_duration"] = storyboard.get("total_duration", 0)

        # 从关键帧获取统计
        keyframes_path = self.path_config.episode_dir(episode_id) / "keyframes.json"
        if keyframes_path.exists():
            keyframes = load_json(keyframes_path)
            stats["total_keyframes"] = len(keyframes.get("keyframes", []))

        return stats

    def _save_report(self, report: Dict, episode_id: str) -> Path:
        """保存报告"""
        output_dir = self.path_config.output_dir / episode_id
        output_dir.mkdir(parents=True, exist_ok=True)

        report_path = output_dir / "generation_report.json"
        save_json(report, report_path)

        return report_path

    def run_step(
        self,
        step_name: str,
        chapter_id: str = "",
        episode_id: str = ""
    ) -> Dict[str, Any]:
        """运行单个步骤"""
        if step_name == "analyze":
            return self._run_analysis(chapter_id)
        elif step_name == "storyboard":
            return self._run_storyboard(chapter_id, episode_id, "")
        elif step_name == "camera":
            return self._run_camera(episode_id)
        elif step_name == "keyframe":
            return self._run_keyframe(episode_id)
        elif step_name == "prompt":
            return self._run_prompt(episode_id)
        else:
            raise ValueError(f"未知步骤: {step_name}")


def main():
    parser = argparse.ArgumentParser(description="视频生成协调器")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--chapter", help="章节ID")
    parser.add_argument("--episode", help="剧集ID")
    parser.add_argument("--title", default="", help="剧集标题")
    parser.add_argument("--full-pipeline", action="store_true", help="运行完整流水线")
    parser.add_argument("--step", choices=["analyze", "storyboard", "camera", "keyframe", "prompt"], help="运行单个步骤")

    args = parser.parse_args()

    generator = VideoGenerator(args.project)

    if args.full_pipeline:
        if not args.chapter or not args.episode:
            parser.error("完整流水线需要 --chapter 和 --episode")
        report = generator.run_full_pipeline(args.chapter, args.episode, args.title)

        print(f"\n{'='*60}")
        print(f"处理完成!")
        print(f"{'='*60}")
        print(f"成功: {report['success']}")
        print(f"镜头数: {report['statistics'].get('total_shots', 0)}")
        print(f"关键帧数: {report['statistics'].get('total_keyframes', 0)}")
        print(f"报告: {report.get('report_path', '')}")

        if report['errors']:
            print(f"\n错误:")
            for err in report['errors']:
                print(f"  - {err}")

    elif args.step:
        if not args.episode:
            parser.error("单步执行需要 --episode")
        result = generator.run_step(args.step, args.chapter or "", args.episode)
        print(f"步骤 {args.step} 完成")
        print(f"结果: {json.dumps(result, ensure_ascii=False, indent=2)}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
