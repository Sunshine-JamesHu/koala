import os
import json
import glob
from pathlib import Path

def update_assets_style():
    project_dir = Path(r"f:\Projects\koala\works\穿书后我攻略了奸臣首辅")
    assets_dir = project_dir / "assets"
    
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        project_data = json.load(f)
        global_style = project_data.get("style", {}).get("globalPromptStyle", "")
        
    print(f"Using Global Style: {global_style}")

    # Files to process
    md_files = glob.glob(str(assets_dir / "**/*.md"), recursive=True)
    json_files = glob.glob(str(assets_dir / "**/*.json"), recursive=True)
    
    # Simple replacement rules - replacing common old styles with the new global style
    replacements = [
        ("古风动漫风格，精细细腻的线条，柔和的色调，电影级光影效果，高质量渲染，4K画质", global_style),
        ("古风动漫, 电影质感", global_style),
        ("古风动漫风格", global_style),
        ("anime style", "CG illustration, soft outlines, warm-cool contrast, detailed texture, depth of field, masterpiece, cinematic lighting")
    ]

    for fp in md_files + json_files:
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        new_content = content
        for old_str, new_str in replacements:
            if old_str in new_content:
                new_content = new_content.replace(old_str, new_str)
                modified = True
                
        if modified:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated: {fp}")

if __name__ == "__main__":
    update_assets_style()
