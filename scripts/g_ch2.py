import os
import json
import traceback

base_dir = r"f:\Projects\koala3"
novel_dir = os.path.join(base_dir, r"novels\穿书后我攻略了奸臣首辅")
style_path = os.path.join(novel_dir, r"global_assets\style.json")
storyboard_path = os.path.join(novel_dir, r"chapters\chapter_002\03_storyboard.md")
output_path = os.path.join(novel_dir, r"chapters\chapter_002\04_prompts.md")

try:
    with open(style_path, 'r', encoding='utf-8') as f:
        style_data = json.load(f)
    style_str = f"{style_data['art_style']} {style_data['color_palette']['description']} {style_data['texture']} {style_data['lighting']['default_quality']}"

    with open(storyboard_path, 'r', encoding='utf-8') as f:
        sb_lines = f.readlines()

    shots = []
    for line in sb_lines:
        if line.startswith('| S'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6:
                shots.append({
                    "id": parts[1],
                    "camera": parts[3],
                    "desc": parts[4],
                    "transition": parts[5]
                })

    out = []
    out.append("# 穿书后我攻略了奸臣首辅 - 第002章 生图清单\n")
    out.append("## 📌 全局风格 (Global Style)\n```text\n" + style_str + "\n```\n")
    out.append("## ✅ 生图清单\n| # | 文件名 | 类型 | 垫图 | 状态 |\n|---|--------|------|------|------|")
    
    # Base references
    out.append("| 1 | 辛影月_四视图.jpg | 角色 | 无 | ☐ |")
    out.append("| 2 | 沈清起_四视图.jpg | 角色 | 无 | ☐ |")
    out.append("| 3 | 霍齐_四视图.jpg | 角色 | 无 | ☐ |")
    out.append("| 4 | 屠户王_四视图.jpg | 角色 | 无 | ☐ |")
    out.append("| 5 | 破落农舍内部_全景.jpg | 场景 | 无 | ☐ |")
    out.append("| 6 | 沈家小院_全景.jpg | 场景 | 无 | ☐ |")
    
    for i, s in enumerate(shots):
        out.append(f"| {i+7} | C02_{s['id']}.jpg | 分镜 | 上一镜 + 角色/场景参考 | ☐ |")

    out.append("\n---\n## 一、基准图生成 (Reference Bases)\n")
    out.append("- 👤 辛月影: `global_assets/characters/辛影月/xin_yueying_prompt.md`")
    out.append("- 👤 沈清起: `global_assets/characters/沈清起/shen_qingqi_prompt.md`")
    out.append("- 👤 霍齐: `global_assets/characters/霍齐/huo_qi_prompt.md`")
    out.append("- 👤 屠户王: `chapters/chapter_002/characters/butcher_wang_prompt.md`")
    out.append("- 🏡 破落农舍内部: `global_assets/scenes/破落农舍内部/ruined_cottage_interior.md`")
    out.append("- 🏡 沈家小院: `global_assets/scenes/沈家小院/shen_family_courtyard.md`\n")

    out.append("---\n## 二、分镜连续生图 (Storyboard Shots)\n")
    
    prev_pad = "破落农舍内部_全景.jpg"
    for s in shots:
        out.append(f"### 🎬 #{s['id']} `C02_{s['id']}.jpg`")
        out.append(f"> **镜头语言**: {s['camera']}")
        out.append(f"> **垫图**: 📌 上传 `{prev_pad}` + 对应四视图")
        out.append(f"> **衔接动作**: {s['transition']}\n")
        
        # Translation pseudo-logic
        chars = []
        if "辛月" in s['desc'] or "她" in s['desc']: chars.append("Xin Yueying")
        if "沈清起" in s['desc'] or "他" in s['desc']: chars.append("Shen Qingqi")
        if "霍齐" in s['desc']: chars.append("Huo Qi")
        if "老王" in s['desc'] or "屠户" in s['desc']: chars.append("Butcher Wang")
        
        c_str = ", ".join(chars) if chars else "The character"
        
        # Basic prompt
        prompt = f"Cinematic shot of {c_str}. Action: {s['desc']}. Camera: {s['camera']}. Transition: {s['transition']}. CRITICAL: Maintain precise facial features, clothing, and spatial continuity based on reference sheets."
        
        out.append("```text")
        out.append(f"{prompt}\n")
        out.append(f"{style_str}\n")
        out.append("Negative prompt: distorted geometry, bad anatomy, missing fingers, modern clothes, text, bright daylight, 2D anime, flat, watermark")
        out.append("```\n---\n")
        
        prev_pad = f"C02_{s['id']}.jpg"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(out))
    
    print(f"SUCCESS: Generated {len(shots)} prompts to {output_path}")

except Exception as e:
    print("FAILED with Exception:")
    traceback.print_exc()
