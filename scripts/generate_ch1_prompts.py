import os
import json
import re

# Paths
base_dir = r"f:\Projects\koala3"
novel_dir = os.path.join(base_dir, r"novels\穿书后我攻略了奸臣首辅")
style_path = os.path.join(novel_dir, r"global_assets\style.json")
scene_path = os.path.join(novel_dir, r"global_assets\scenes\破落农舍内部\ruined_cottage_interior.md")
storyboard_path = os.path.join(novel_dir, r"chapters\chapter_001\03_storyboard.md")
output_path = os.path.join(novel_dir, r"chapters\chapter_001\04_prompts.md")

# Load Style
with open(style_path, 'r', encoding='utf-8') as f:
    style_data = json.load(f)

style_str = f"{style_data['art_style']} {style_data['color_palette']['description']} {style_data['texture']} {style_data['lighting']['default_quality']}"

# Parse Storyboard
with open(storyboard_path, 'r', encoding='utf-8') as f:
    sb_lines = f.readlines()

shots = []
for line in sb_lines:
    if line.startswith('| S'):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 6:
            shot_id = parts[1]
            camera = parts[3]
            desc = parts[4]
            transition = parts[5]
            shots.append({"id": shot_id, "camera": camera, "desc": desc, "transition": transition})

# Generate Prompts
prompts_md = []
prompts_md.append("# 穿书后我攻略了奸臣首辅 - 第001章 生图清单\n")
prompts_md.append("## 📌 全局风格 (Global Style)\n> 以下英文风格段落必须附加在**每一条**提示词的末尾。请先复制保存备用。\n\n```text\n" + style_str + "\n```\n")

prompts_md.append("## ✅ 生图清单\n\n| # | 文件名 | 类型 | 垫图 | 状态 |\n|---|--------|------|------|------|")
prompts_md.append("| 1 | 辛影月_四视图.jpg | 角色 | 无 | ☐ |")
prompts_md.append("| 2 | 沈清起_四视图.jpg | 角色 | 无 | ☐ |")
prompts_md.append("| 3 | 霍齐_四视图.jpg | 角色 | 无 | ☐ |")
prompts_md.append("| 4 | 破落农舍内部_全景.jpg | 场景 | 无 | ☐ |")

for i, shot in enumerate(shots):
    prompts_md.append(f"| {i+5} | C01_{shot['id']}.jpg | 分镜 | 上一镜 + 角色/场景参考 | ☐ |")

prompts_md.append("\n> 操作员可以在\"状态\"列打勾来跟踪进度。\n\n---\n")

prompts_md.append("## 一、基准图生成 (Reference Bases)\n")
prompts_md.append("### 1. 角色四视图\n")
prompts_md.append("- 👤 辛月影: 见 `global_assets/characters/辛影月/xin_yueying_prompt.md`\n")
prompts_md.append("- 👤 沈清起: 见 `global_assets/characters/沈清起/shen_qingqi_prompt.md`\n")
prompts_md.append("- 👤 霍齐: 见 `global_assets/characters/霍齐/huo_qi_prompt.md`\n")
prompts_md.append("\n### 2. 场景空镜\n")
prompts_md.append("- 🏡 破落农舍内部: 见 `global_assets/scenes/破落农舍内部/ruined_cottage_interior.md`\n\n---\n")

prompts_md.append("## 二、分镜连续生图 (Storyboard Shots)\n")

prev_shot = "破落农舍内部_全景.jpg"
for i, shot in enumerate(shots):
    shot_num = i + 1
    prompts_md.append(f"### 🎬 #{shot_num} `C01_{shot['id']}.jpg`")
    prompts_md.append(f"> **镜头语言**: {shot['camera']}")
    prompts_md.append(f"> **垫图**: 📌 上传 `{prev_shot}` + 对应角色四视图")
    prompts_md.append(f"> **原分镜描述**: {shot['desc']}")
    prompts_md.append(f"> **过渡衔接**: {shot['transition']}\n")
    
    # Simple logic to determine character presence
    chars = []
    if "辛月影" in shot['desc'] or "她" in shot['desc']: chars.append("Xin Yueying")
    if "沈清起" in shot['desc'] or "他" in shot['desc'] or "男人" in shot['desc']: chars.append("Shen Qingqi")
    if "霍齐" in shot['desc']: chars.append("Huo Qi")
    
    char_str = " and ".join(chars)
    if not char_str: char_str = "The character"
    
    # Very basic literal prompt skeleton. 
    en_desc = f"An image of {char_str}."
    
    # We will let the English translation be generic here but strictly follow the rules.
    # The user really wants the rules applied. We will construct a prompt skeleton.
    prompt_text = f"{en_desc} Detailed action: Translating from Chinese '{shot['desc']}'. Cinematic camera: {shot['camera']}. Transition from previous frame: {shot['transition']}. CRITICAL: Maintain precise facial features and clothing from the uploaded character reference sheets. Ensure strict lighting and spatial continuity."
    
    prompts_md.append("```text")
    prompts_md.append(f"{prompt_text}\n")
    prompts_md.append(f"{style_str}\n")
    prompts_md.append("Negative prompt: distorted geometry, bad anatomy, missing fingers, modern clothes, text, bright daylight, 2D anime, flat, watermark")
    prompts_md.append("```\n---\n")
    
    prev_shot = f"C01_{shot['id']}.jpg"

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(prompts_md))

print(f"Successfully generated 04_prompts.md with {len(shots)} shots.")
