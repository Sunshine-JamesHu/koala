const fs = require('fs');
const path = require('path');

const baseDir = String.raw`f:\Projects\koala3\novels\穿书后我攻略了奸臣首辅\chapters\chapter_001`;
const promptsPath = path.join(baseDir, '04_prompts.md');
const stPath = path.join(baseDir, '05_storytelling.md');

const content = fs.readFileSync(promptsPath, 'utf8');
const lines = content.split('\n');

const shots = [];
let currentShot = null;
let inCodeBlock = false;
let codeBlockContent = [];

for (const line of lines) {
    if (line.startsWith('### S')) {
        if (currentShot) {
            shots.push(currentShot);
        }
        const match = line.match(/`([^`]+)`/);
        currentShot = {
            id: match ? match[1] : 'Unknown',
            camera: '',
            desc: ''
        };
        inCodeBlock = false;
        codeBlockContent = [];
    } else if (currentShot) {
        if (line.startsWith('> **Camera**:')) {
            currentShot.camera = line.replace('> **Camera**:', '').trim();
        } else if (line.startsWith('```text')) {
            inCodeBlock = true;
        } else if (line.startsWith('```') && inCodeBlock) {
            inCodeBlock = false;
            const descLines = [];
            for (const textLine of codeBlockContent) {
                if (textLine.trim() === '') break;
                descLines.push(textLine);
            }
            currentShot.desc = descLines.join(' ').trim();
        } else if (inCodeBlock) {
            codeBlockContent.push(line);
        }
    }
}
if (currentShot) {
    shots.push(currentShot);
}

const grouped = {
    'S01': [],
    'S02': [],
    'S03': [],
    'S04': []
};

for (const s of shots) {
    const prefix = s.id.split('_')[1];
    if (grouped[prefix]) {
        grouped[prefix].push(s);
    }
}

const dict = {
    "Xin Yueying": "辛月影", "Shen Qingqi": "沈清起", "Huo Qi": "霍齐",
    "wheelchair": "轮椅", "sword": "长剑", "oil lamp": "青灯/油灯",
    "dirty stone floor": "脏乱的石板地", "moonlight": "月光", "wooden door": "木门",
    "wooden pillar": "木柱", "bloodless": "毫无血色的", "phoenix eyes": "狭长凤眼",
    "terrified": "惊恐的", "smirk": "戏谑的笑", "shock": "震惊",
    "tears": "眼泪", "broken porcelain": "碎瓷片", "darkness": "黑暗"
};
function crudeTranslate(engDesc) {
    let cn = engDesc;
    for (const [en, zh] of Object.entries(dict)) {
        cn = cn.split(en).join(zh);
    }
    return cn;
}

const paragraphData = {
    'S01': {
        title: "第一段：深渊之遇，绝命毒酒惹杀机",
        narration: "【01】夜色如墨，发霉的破落农舍里，寒意刺骨。【02】“你自尽吧”——【03】黑暗中，一句毫无温度的声音，骤然撕裂了死寂。【04】倒在地上的辛月影吃力地睁开眼，刺鼻的霉味直冲天灵盖。【05】她慵懒地翻了个身，嘴角甚至还挂着一丝戏谑的弧度，【06】只当自己是陷入了某场光怪陆离的绮梦。【07】然而，当对面阴影中的男人微微前倾，【08】冰冷的月光，犹如一柄利刃，彻底照亮了那张宛若谪仙却淬满无尽杀意的脸庞！【09】破败的轮椅，满地的碎瓷与残羹，他端坐其上，宛如一尊从地狱归来的修罗。【10】“辛四娘，你在等什么？”薄唇轻启，字字诛心！【11】辛四娘？！这三个字犹如惊雷般在辛月影脑海中炸响，她脸上的笑容瞬间冻结！【12】刻骨的寒意从脚底直窜脊背，【13】原书中，那个被玄铁锁链洞穿琵琶骨排斥在血泊中的暴戾权臣，【14】以及原主端去的那碗见血封喉的毒药，化作无数碎片疯狂涌入她的记忆！【15】这哪里是梦？！这是她亲手给当朝第一疯批权臣喂下毒药的火葬场开局！！"
    },
    'S02': {
        title: "第二段：一线生机，青锋指剑命悬一线",
        narration: "【01】不等她理清这致命的死局，地面上一道刺目的寒芒骤然闪起！【02】沈清起居高临下，狭长的凤眼中流转的，是纯粹且极致的毁灭欲。【03】求生的本能让辛月影如同离弦之箭般连滚带爬向后狂退！【04】直到后背死死撞在破木柱上，退无可退！【05】她满头冷汗，绝望中试图求饶，可那宛若杀神的男人，根本没有多废一句话的打算。【06】枯瘦如柴的手，如同死神的镰刀，平静地握住了地上的剑柄。【07】三尺青锋铮然泛起冷光，剑尖直指眉心！【08】那股令人窒息的死亡压迫感，仿佛连周围的空气都被抽干！【09】辛月影的目光犹如惊弓之鸟，死死锁定了侧后方那扇摇摇欲坠的木门。【10】就在她的脚尖，怀着万分之一的侥幸，刚刚向外挪动一寸的刹那！【11】一束快到无法捕捉残影的凌厉剑光，裹挟着雷霆万钧之势，迎面劈斩而来！【12】“啊——！”伴随着一声凄厉的尖叫，她几乎是本能地将身体猛然砸向一旁！【13】嗡——！锋利无匹的长剑，贴着她颈动脉的肌肤，狠狠贯入身后的木柱，剧烈震颤的嗡鸣声，在死寂的夜里令人头皮发麻！"
    },
    'S03': {
        title: "第三段：身陷绝地，困兽犹斗",
        narration: "【01】生死只在毫厘之间！辛月影再也顾不得一切，爬起身疯狂冲向那扇破木门！【02】可她还未跨出门槛，便砰地一声，仿佛撞上了一尊铜墙铁壁，被狠狠反弹摔在地上！【03】抬头望去，月光下，一个体型犹如铁塔般的虬髯大汉，正怒目圆睁地俯视着她！【04】“吃了熊心豹子胆！敢给二爷下毒！？”霍齐的怒吼如同闷雷炸响！【05】只见他那粗壮生风的右臂猛地一挥，犹如拎断线的风筝一般，一把将辛月影极其粗暴地掀翻回了屋内！【06】世界天旋地转，辛月影重重摔落在阴冷潮湿的地面上，满身狼狈。【07】当她绝望地回过头，只见轮椅上的沈清起，正似笑非笑地端详着她，那眼神，就像在欣赏一只正在做徒劳挣扎的猎物。"
    },
    'S04': {
        title: "第四段：绝境飙戏，真假难辨",
        narration: "【01】退路已绝！大汉死守门外，而屋内，沈清起修长苍白的手指正危险地把玩着那枚足以割断喉咙的碎瓷片。【02】“要么自绝于此，要么……我给你一通快。”阎罗王的催命符再次掷地有声！【03】瘫坐于地的辛月影，大脑中所有的齿轮开始疯狂咬合，在十死无生的绝境中寻找那微乎其微的生门！【04】突然，她的双眼猛然大睁，瞳孔中爆发出极其夸张地不可置信！【05】随着“啪”的一声清脆的击掌，她的神情瞬间从惊恐无缝切换为极度的无辜与震撼：“什么？！那粉末……竟然是毒药？！”【06】这影后级别的爆发力，即便是冷血如铁的沈清起与霍齐，也不由得冷然静观这出荒诞的戏码。【07】辛月影眼眶通红，泪如雨下，将一个被无辜逼迫的柔弱女子演绎得淋漓尽致：“是有人逼我的！他们威胁我，我根本不知道那是毒药啊！”【08】然而，回应她的，却是沈清起鼻腔中溢出的一声讥讽冷嗤，仿佛能看穿天地间一切谎言！【09】一计不成死咬到底！辛月影咬着牙，继续层层加码：“那人凶神恶煞，我若不从便会没命的！我真的什么都不知道！”【10】她甚至反客为主，满眼关切地望向那个要杀她的男人：“相公，你难道是得罪了什么手眼通天的仇家？他们这是要借刀杀人啊！”【11】听完这堪称无懈可击的临场发挥，沈清起原本单薄的肩膀开始轻微耸动，紧接着，一串绵长、阴冷、令人毛骨悚然的低笑声，缓缓回荡在破屋之中。【12】笑声戛然而止的瞬间，他眼底的最后一丝戏谑也凝结成冰：“不论究竟是谁……且让他，下黄泉去陪你吧。”谎言被彻底看穿，死局，已成定局！！"
    }
};

const out = [];
out.push("# 穿书后我攻略了奸臣首辅 - 第一章 图文解说稿");
out.push("> **用途**: 短视频/推文/有声小说配音脚本");
out.push("> **配音基调**: 上帝视角讲述，沉浸式演播，评书级叙事张力，悬疑跌宕");
out.push("> **结构优化**: 采用**大段落连续播讲**，保留高级叙事感的故事性体验；同时在句首标注【序号】实现与生图的物理级 1:1 对齐映射！");
out.push("");

for (const groupName of ['S01', 'S02', 'S03', 'S04']) {
    const groupShots = grouped[groupName];
    if (!groupShots || groupShots.length === 0) continue;

    out.push(`---`);
    out.push(`## ${paragraphData[groupName].title} (共${groupShots.length}图)`);
    out.push("");

    out.push(`**🎙️ 评书级连续配音文案 (演播员看这里)**：`);
    out.push(`> 提示：下面这一整段要用“说书人”的沉浸式第三人称视角，配合画面讲故事。句首的数字代表此时画面**正好切到对应序号的分镜图**。`);
    out.push("");
    out.push(`${paragraphData[groupName].narration}`);
    out.push("");

    out.push(`**👁️ 1:1画图对照表 (给排版核对查错用)**：\n`);
    for (let i = 0; i < groupShots.length; i++) {
        const s = groupShots[i];
        const num = (i + 1).toString().padStart(2, '0');
        out.push(`- **【${num}】 \`${s.id}\`**: ${crudeTranslate(s.desc)}`);
    }
    out.push("");
}

fs.writeFileSync(stPath, out.join("\n"), "utf8");
console.log('SUCCESS: Written Chapter 1 Third-Person');
