#!/usr/bin/env python3
"""
合并可灵视频提示词分段文件
将 temp_kling_part1.md ~ temp_kling_part7.md 合并为完整的 07_video_prompts_kling.md
"""

import os
from pathlib import Path

def merge_kling_parts():
    """合并所有分段文件"""
    # 获取当前脚本所在目录
    script_dir = Path(__file__).parent

    # 定义分段文件
    part_files = [
        "temp_kling_part1.md",
        "temp_kling_part2.md",
        "temp_kling_part3.md",
        "temp_kling_part4.md",
        "temp_kling_part5.md",
        "temp_kling_part6.md",
        "temp_kling_part7.md",
    ]

    # 输出文件
    output_file = script_dir / "07_video_prompts_kling.md"

    # 合并内容
    merged_content = []

    for part_file in part_files:
        part_path = script_dir / part_file
        if part_path.exists():
            with open(part_path, 'r', encoding='utf-8') as f:
                content = f.read()
                merged_content.append(content)
                print(f"✓ 已读取: {part_file}")
        else:
            print(f"✗ 文件不存在: {part_file}")

    # 写入合并后的文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(merged_content))

    print(f"\n✓ 合并完成: {output_file}")
    print(f"  总字符数: {len('\n'.join(merged_content)):,}")

    # 可选：删除临时文件
    print("\n是否删除临时分段文件？(y/n): ", end="")
    # 自动模式下不删除，保留临时文件以便检查
    print("保留临时文件以便检查")

if __name__ == "__main__":
    merge_kling_parts()
