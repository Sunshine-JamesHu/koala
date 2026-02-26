const fs = require('fs');
const path = require('path');

function generatePrompts() {
    const projectDir = "f:\\Projects\\koala\\works\\穿书后我攻略了奸臣首辅";
    const shotsDir = path.join(projectDir, "scripts", "episode_001", "shots");
    const outputDir = path.join(projectDir, "output", "episode_001");

    let globalStyle = "古风动漫风格";
    try {
        const projectData = JSON.parse(fs.readFileSync(path.join(projectDir, "project.json"), 'utf8'));
        if (projectData.style && projectData.style.globalPromptStyle) {
            globalStyle = projectData.style.globalPromptStyle;
        }
    } catch (e) { }

    for (let i = 1; i <= 4; i++) {
        const shotId = `shot_${i.toString().padStart(3, '0')}`;
        const shotFile = path.join(shotsDir, `${shotId}.json`);

        if (!fs.existsSync(shotFile)) continue;

        const shotData = JSON.parse(fs.readFileSync(shotFile, 'utf8'));
        const shotOutDir = path.join(outputDir, shotId);

        if (!fs.existsSync(shotOutDir)) {
            fs.mkdirSync(shotOutDir, { recursive: true });
        }

        const scene = shotData.scene || {};
        const lighting = scene.lighting || {};
        const camera = shotData.camera || {};
        const movement = camera.movement || {};
        const chars = shotData.characters || [];

        const envEffects = scene.environmental_effects ? scene.environmental_effects.join(',') : '';
        const sceneDesc = `${scene.location_name || ''}。${scene.time_of_day || ''}。${lighting.description || ''}。${scene.atmosphere || ''}。环境：${envEffects}。`;

        let charDesc = "";
        let charRefs = "";
        for (let c of chars) {
            const cName = c.name || '';
            const actionMain = (c.action && c.action.main) ? c.action.main : '';
            const exprDesc = (c.expression && c.expression.description) ? c.expression.description : '';
            charDesc += `${cName}, ${c.importance || 'primary'}角色。身穿${c.costume_id || '默认服装'}。${c.pose || ''}, ${actionMain}。情绪：${exprDesc}。\n`;
            charRefs += `- ${cName}: works/穿书后我攻略了奸臣首辅/assets/characters/${cName}/views.png（四视图，优先使用；如无则用 front.png）\n`;
        }

        const locName = scene.location_name || '未知';
        const locType = scene.location_type || 'indoor';
        const sceneRef = `- ${locName}: works/穿书后我攻略了奸臣首辅/assets/scenes/${locType}/${locName}/main.png\n`;

        const prevEndPath = i > 1 ? `works/穿书后我攻略了奸臣首辅/output/episode_001/shot_${(i - 1).toString().padStart(3, '0')}/end_latest.png` : "无，本镜为首镜";

        const focusSubject = (camera.focus && camera.focus.subject) ? camera.focus.subject : '';
        const narrativePurpose = (shotData.narrative && shotData.narrative.purpose) ? shotData.narrative.purpose : '';

        const startMd = `【图片基本信息】
比例: ${(shotData.global_settings && shotData.global_settings.aspect_ratio) ? shotData.global_settings.aspect_ratio : '16:9'}
风格: ${globalStyle}

【场景环境】
${sceneDesc}

【角色设定】
${charDesc}
【角色参考图】
${charRefs}
【场景参考图】
${sceneRef}
【上一分镜尾帧】
- 路径: ${prevEndPath}
- 说明: 生成首帧时必须将此图传入 generate_image 的 ImagePaths 参数，以保持场景和人物的视觉连贯性

【构图与运镜】
镜头类型: ${camera.shot_size || ''}
镜头角度: ${camera.angle || ''}
焦点: ${focusSubject}
景深: ${camera.depth_of_field || ''}

【画面描述】
${narrativePurpose}

【色调与光影】
主色调: ${lighting.color || ''}
布光方式: ${lighting.direction || ''}
对比度: 高
`;

        fs.writeFileSync(path.join(shotOutDir, "start.md"), startMd, 'utf8');
        fs.writeFileSync(path.join(shotOutDir, "middle.md"), startMd.replace('【上一分镜尾帧】\n- 路径: ' + prevEndPath + '\n- 说明: 生成首帧时必须将此图传入 generate_image 的 ImagePaths 参数，以保持场景和人物的视觉连贯性\n\n', ''), 'utf8');
        fs.writeFileSync(path.join(shotOutDir, "end.md"), startMd.replace('【上一分镜尾帧】\n- 路径: ' + prevEndPath + '\n- 说明: 生成首帧时必须将此图传入 generate_image 的 ImagePaths 参数，以保持场景和人物的视觉连贯性\n\n', ''), 'utf8');

        const speaker = (shotData.dialogue && shotData.dialogue.speaker) ? shotData.dialogue.speaker : '无';
        const text = (shotData.dialogue && shotData.dialogue.text) ? shotData.dialogue.text : '无';
        const tone = (shotData.dialogue && shotData.dialogue.delivery && shotData.dialogue.delivery.tone) ? shotData.dialogue.delivery.tone : '';
        const duration = (shotData.duration && shotData.duration.seconds) ? shotData.duration.seconds : 5.0;
        const bgmMood = (shotData.sound && shotData.sound.bgm && shotData.sound.bgm.mood) ? shotData.sound.bgm.mood : '无';
        const startEndDesc = movement.start_end_description || '';

        const videoMd = `【视频基本信息】
时长: ${duration}秒
风格: ${globalStyle}
比例: 16:9
帧率: 24fps

【场景环境】
${sceneDesc}

【角色设定】
${charDesc}
【角色参考图】
${charRefs}
【运镜设计】
镜头类型: ${camera.shot_size || ''}
镜头角度: ${camera.angle || ''}
运镜方式: ${movement.type || ''} - ${startEndDesc}

0-5秒【发生事件】:
${narrativePurpose}

【色调与光影】
主色调: ${lighting.color || ''}
布光方式: ${lighting.direction || ''}

【台词】
说话人: ${speaker}
台词: "${text}"
语气: ${tone}

【背景音乐】
类型: ${bgmMood}
`;
        fs.writeFileSync(path.join(shotOutDir, "video.md"), videoMd, 'utf8');
        console.log(`Generated prompts for ${shotId}`);
    }
}

generatePrompts();
