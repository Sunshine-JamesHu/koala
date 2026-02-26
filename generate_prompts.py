import os
import json
from pathlib import Path

def generate_prompts():
    project_dir = Path(r"f:\Projects\koala\works\穿书后我攻略了奸臣首辅")
    shots_dir = project_dir / "scripts" / "episode_001" / "shots"
    output_dir = project_dir / "output" / "episode_001"
    
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        project_data = json.load(f)
        global_style = project_data.get("style", {}).get("globalPromptStyle", "古风动漫风格")
        
    for shot_idx in range(1, 5):
        shot_id = f"shot_{shot_idx:03d}"
        shot_file = shots_dir / f"{shot_id}.json"
        
        if not shot_file.exists():
            continue
            
        with open(shot_file, "r", encoding="utf-8") as f:
            shot_data = json.load(f)
            
        shot_out_dir = output_dir / shot_id
        shot_out_dir.mkdir(parents=True, exist_ok=True)
        
        scene = shot_data.get("scene", {})
        lighting = scene.get("lighting", {})
        camera = shot_data.get("camera", {})
        movement = camera.get("movement", {})
        chars = shot_data.get("characters", [])
        
        scene_desc = f"{scene.get('location_name', '')}。{scene.get('time_of_day', '')}。{lighting.get('description', '')}。{scene.get('atmosphere', '')}。环境：{','.join(scene.get('environmental_effects', []))}。"
        
        char_desc = ""
        char_refs = ""
        for c in chars:
            c_name = c.get('name', '')
            char_desc += f"{c_name}, {c.get('importance', 'primary')}角色。身穿{c.get('costume_id', '默认服装')}。{c.get('pose', '')}, {c.get('action', {}).get('main', '')}。情绪：{c.get('expression', {}).get('description', '')}。\n"
            char_refs += f"- {c_name}: works/穿书后我攻略了奸臣首辅/assets/characters/{c_name}/views.png（四视图，优先使用；如无则用 front.png）\n"

        scene_ref = f"- {scene.get('location_name', '未知')}: works/穿书后我攻略了奸臣首辅/assets/scenes/{scene.get('location_type', 'indoor')}/{scene.get('location_name', '未知')}/main.png\n"

        prev_end_path = f"works/穿书后我攻略了奸臣首辅/output/episode_001/shot_{shot_idx-1:03d}/end_latest.png" if shot_idx > 1 else "无，本镜为首镜"
        
        start_md = f"""【图片基本信息】
比例: {shot_data.get('global_settings', {}).get('aspect_ratio', '16:9')}
风格: {global_style}

【场景环境】
{scene_desc}

【角色设定】
{char_desc}
【角色参考图】
{char_refs}
【场景参考图】
{scene_ref}
【上一分镜尾帧】
- 路径: {prev_end_path}
- 说明: 生成首帧时必须将此图传入 generate_image 的 ImagePaths 参数，以保持场景和人物的视觉连贯性

【构图与运镜】
镜头类型: {camera.get('shot_size', '')}
镜头角度: {camera.get('angle', '')}
焦点: {camera.get('focus', {}).get('subject', '')}
景深: {camera.get('depth_of_field', '')}

【画面描述】
{shot_data.get('narrative', {}).get('purpose', '')}

【色调与光影】
主色调: {lighting.get('color', '')}
布光方式: {lighting.get('direction', '')}
对比度: 高
"""

        with open(shot_out_dir / "start.md", "w", encoding="utf-8") as f:
            f.write(start_md)
            
        with open(shot_out_dir / "middle.md", "w", encoding="utf-8") as f:
            f.write(start_md.replace('【上一分镜尾帧】', ''))

        with open(shot_out_dir / "end.md", "w", encoding="utf-8") as f:
            f.write(start_md.replace('【上一分镜尾帧】', ''))
            
        video_md = f"""【视频基本信息】
时长: {shot_data.get('duration', {}).get('seconds', 5.0)}秒
风格: {global_style}
比例: 16:9
帧率: 24fps

【场景环境】
{scene_desc}

【角色设定】
{char_desc}
【角色参考图】
{char_refs}
【运镜设计】
镜头类型: {camera.get('shot_size', '')}
镜头角度: {camera.get('angle', '')}
运镜方式: {movement.get('type', '')} - {movement.get('start_end_description', '')}

0-5秒【发生事件】:
{shot_data.get('narrative', {}).get('purpose', '')}

【色调与光影】
主色调: {lighting.get('color', '')}
布光方式: {lighting.get('direction', '')}

【台词】
说话人: {shot_data.get('dialogue', {}).get('speaker', '无')}
台词: "{shot_data.get('dialogue', {}).get('text', '无')}"
语气: {shot_data.get('dialogue', {}).get('delivery', {}).get('tone', '')}

【背景音乐】
类型: {shot_data.get('sound', {}).get('bgm', {}).get('mood', '无')}
"""
        with open(shot_out_dir / "video.md", "w", encoding="utf-8") as f:
            f.write(video_md)
            
        print(f"Generated prompts for {shot_id}")

generate_prompts()
