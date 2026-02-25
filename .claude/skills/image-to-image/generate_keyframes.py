#!/usr/bin/env python3
"""
关键帧生成脚本

正确的工作流程:
1. 使用 text-to-image 生成纯场景背景图，获取图片URL
2. 使用 image-to-image，以场景URL为输入，通过详细描述角色特征生成带角色的关键帧

用法:
    uv run python generate_keyframes.py --episode 001 --shot 001
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# 添加父目录到路径以便导入
sys.path.insert(0, str(Path(__file__).parent.parent))

from text_to_image.text_to_image import generate_image as text_to_image, load_env_file
from image_to_image.image_to_image import generate_image as image_to_image

# 加载环境变量
load_env_file()


# 角色特征描述（基于 prompts.md）
CHARACTER_DESCRIPTIONS = {
    "辛月影": {
        "base": "女性，24岁，175厘米高，身材纤细，九头身完美比例",
        "face": "肤色雪白透亮，鹅蛋脸，五官精致如建模，完美无瑕。杏眼优美，瞳孔漆黑明亮，柳叶眉纤细自然，鼻梁高挺秀气，樱桃小口唇色淡粉",
        "hair": "长发及腰乌黑如墨，古代仕女发型，发髻高挽，几缕碎发垂于耳侧，木簪挽发",
        "costume": "身穿素雅汉服襦裙，淡青色月白色，腰间香囊，绣花布鞋",
        "style": "古风国漫风格，清新明亮，灵动活泼中带着一丝狡黠"
    },
    "沈清起": {
        "base": "男性，23岁，消瘦病弱体型，坐在轮椅上",
        "face": "肤色苍白如白瓷，轮廓分明，棱角清晰，英挺俊美。狭长凤眼，深邃幽暗，眼神阴鸷冰冷，剑眉微微上挑，高挺笔直的鼻梁，薄唇常年紧抿，唇色淡白",
        "hair": "长发及背乌黑如墨，随意束在脑后，有些凌乱",
        "costume": "身穿黑色或深色长袍，破败旧衣，玄黑色墨青色灰白色调，残破轮椅，手中碎瓷片，黑色布靴无法行走",
        "style": "古风病娇美男风格，阴郁冷峻，冷色调低饱和度阴影较重"
    },
    "霍齐": {
        "base": "男性，25岁左右，身材高大健壮",
        "face": "面容刚毅，剑眉星目，眼神锐利",
        "hair": "短发利落",
        "costume": "身穿将军铠甲或便服",
        "style": "古风将军风格"
    }
}


def get_character_prompt(character_name: str, expression: str = "", pose: str = "") -> str:
    """生成角色描述prompt"""
    if character_name not in CHARACTER_DESCRIPTIONS:
        return ""

    char = CHARACTER_DESCRIPTIONS[character_name]
    parts = [
        char["base"],
        char["face"],
        char["hair"],
        char["costume"]
    ]

    if expression:
        parts.append(f"表情：{expression}")
    if pose:
        parts.append(f"姿势：{pose}")

    return "，".join(parts)


def generate_scene_and_keyframe(
    scene_prompt: str,
    character_name: str,
    character_expression: str,
    character_pose: str,
    output_dir: str,
    scene_filename: str,
    keyframe_filename: str,
    width: int = 2560,
    height: int = 1440,
    scale: float = 0.5
):
    """
    生成场景和关键帧

    Args:
        scene_prompt: 场景描述
        character_name: 角色名
        character_expression: 角色表情
        character_pose: 角色姿势
        output_dir: 输出目录
        scene_filename: 场景文件名
        keyframe_filename: 关键帧文件名
        width: 图片宽度
        height: 图片高度
        scale: 文本影响程度
    """
    print(f"\n{'='*60}")
    print(f"生成场景: {scene_filename}")
    print(f"{'='*60}")

    # Step 1: 生成纯场景背景，获取URL
    scene_paths, scene_urls = text_to_image(
        prompt=scene_prompt,
        output_dir=output_dir,
        filename=scene_filename,
        width=width,
        height=height,
        return_urls=True
    )

    scene_url = scene_urls[0]
    print(f"\n场景图片URL: {scene_url[:80]}...")

    # Step 2: 使用场景URL生成带角色的关键帧
    print(f"\n{'='*60}")
    print(f"生成关键帧: {keyframe_filename}")
    print(f"角色: {character_name}")
    print(f"{'='*60}")

    # 构建包含角色描述的prompt
    character_desc = get_character_prompt(character_name, character_expression, character_pose)

    keyframe_prompt = f"在场景中添加角色：{character_desc}，动漫风格，高细节，杰作"

    keyframe_paths = image_to_image(
        image_sources=[scene_url],  # 使用场景URL
        prompt=keyframe_prompt,
        output_dir=output_dir,
        filename=keyframe_filename,
        width=width,
        height=height,
        scale=scale
    )

    return scene_paths[0], keyframe_paths[0]


def process_episode_keyframes(episode_dir: str, output_dir: str):
    """
    处理一集的所有关键帧

    Args:
        episode_dir: 分镜脚本目录
        output_dir: 输出目录
    """
    keyframes_file = Path(episode_dir) / "keyframes.json"

    if not keyframes_file.exists():
        print(f"错误: 找不到 keyframes.json: {keyframes_file}")
        return

    with open(keyframes_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    keyframes = data.get("keyframes", [])
    print(f"共有 {len(keyframes)} 个关键帧需要生成")

    # 按场景分组
    scenes = {}
    for kf in keyframes:
        scene_loc = kf.get("scene_description", {}).get("location", "unknown")
        if scene_loc not in scenes:
            scenes[scene_loc] = []
        scenes[scene_loc].append(kf)

    print(f"共有 {len(scenes)} 个不同场景")

    # 为每个场景生成背景和关键帧
    generated_scenes = {}  # 缓存已生成的场景

    for i, kf in enumerate(keyframes[:10]):  # 先处理前10个作为测试
        kf_id = kf.get("keyframe_id", f"kf_{i:03d}")
        characters = kf.get("characters", [])

        print(f"\n处理关键帧 {i+1}/{min(10, len(keyframes))}: {kf_id}")

        # 如果没有角色，跳过（纯场景）
        if not characters:
            print("  无角色，跳过")
            continue

        # 获取第一个角色
        char = characters[0]
        char_name = char.get("name", "")
        char_expression = char.get("expression", {}).get("type", "")

        if not char_name:
            print("  无角色名，跳过")
            continue

        # 构建场景描述
        scene_desc = kf.get("scene_description", {})
        scene_prompt = f"古代中国{scene_desc.get('location', '房间')}，{scene_desc.get('time_of_day', '夜晚')}，{scene_desc.get('lighting', '昏暗')}，空无一人的房间，没有人物，动漫风格，高细节，电影级光影"

        # 生成场景和关键帧
        try:
            scene_file, keyframe_file = generate_scene_and_keyframe(
                scene_prompt=scene_prompt,
                character_name=char_name,
                character_expression=char_expression,
                character_pose="",
                output_dir=output_dir,
                scene_filename=f"scene_{kf_id}",
                keyframe_filename=f"keyframe_{kf_id}"
            )
            print(f"  场景: {scene_file}")
            print(f"  关键帧: {keyframe_file}")
        except Exception as e:
            print(f"  错误: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="生成关键帧图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --episode "works/穿书后我攻略了奸臣首辅/scripts/episode_001" --output "shots"
        """
    )
    parser.add_argument(
        "--episode",
        required=True,
        help="分镜脚本目录路径"
    )
    parser.add_argument(
        "--output",
        default="shots",
        help="输出目录名 (默认: shots)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="最多处理的关键帧数量 (默认: 10)"
    )
    args = parser.parse_args()

    episode_path = Path(args.episode)
    if not episode_path.exists():
        print(f"错误: 目录不存在: {episode_path}")
        sys.exit(1)

    output_dir = episode_path / args.output

    process_episode_keyframes(str(episode_path), str(output_dir))


if __name__ == "__main__":
    main()
