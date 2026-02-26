const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
}

function updateAssetsStyle() {
    const projectDir = "f:\\Projects\\koala\\works\\穿书后我攻略了奸臣首辅";
    const assetsDir = path.join(projectDir, "assets");

    let globalStyle = "CG插画, 柔和轮廓, 冷暖色调对比, 细腻质感, 景深效果, 超高质量, 极度细腻, 电影级画面质感";
    try {
        const projectData = JSON.parse(fs.readFileSync(path.join(projectDir, "project.json"), 'utf8'));
        if (projectData.style && projectData.style.globalPromptStyle) {
            globalStyle = projectData.style.globalPromptStyle;
        }
    } catch (e) {
        console.error("Could not read project.json", e);
    }

    console.log(`Using Global Style: ${globalStyle}`);

    const replacements = [
        ["古风动漫风格，精细细腻的线条，柔和的色调，电影级光影效果，高质量渲染，4K画质", globalStyle],
        ["古风动漫, 电影质感", globalStyle],
        ["古风动漫风格", globalStyle],
        ["anime style", "CG illustration, soft outlines, warm-cool contrast, detailed texture, depth of field, masterpiece, cinematic lighting"]
    ];

    walkDir(assetsDir, function (filePath) {
        if (filePath.endsWith('.md') || filePath.endsWith('.json')) {
            let content = fs.readFileSync(filePath, 'utf8');
            let modified = false;

            for (let [oldStr, newStr] of replacements) {
                if (content.includes(oldStr)) {
                    content = content.split(oldStr).join(newStr);
                    modified = true;
                }
            }

            if (modified) {
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Updated: ${filePath}`);
            }
        }
    });
}

updateAssetsStyle();
