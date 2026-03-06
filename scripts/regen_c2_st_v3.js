const fs = require('fs');
const path = require('path');

const baseDir = String.raw`f:\Projects\koala3\novels\穿书后我攻略了奸臣首辅\chapters\chapter_002`;
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

const paragraphData = {
    'S01': {
        title: "第一段：影后级求生，谎言退杀意",
        narration: "【01】生死悬于一线！被逼至绝境的辛月影，浑身仿佛被奥斯卡影后附体！【02】她猛地扑倒在地，仿佛受尽了天大的冤屈：【03】“二位大爷！我就算再蠢，怎敢光天化日之下毒害相公？！”【04】她抬起头，满脸无辜与痛心地开始编造一个莫须有的谎言。【05】“此人逼我下药，分明是意图羞辱，杀人诛心啊！”【06】然而，对面的沈清起，却如同一尊没有呼吸的冰雕。【07】那双狭长的凤眼中，不起一丝波澜。谎言，对他而言，仿佛只是戏子的拙劣表演。【08】就在辛月影以为这招苦肉计彻底失败之时，【09】沈清起那张苍白如纸的脸微微一侧，修长且苍白的手指，死死攥紧了手中那枚残破的碎瓷片！【10】“霍齐。”他薄唇轻启，仅仅吐出两个冰冷的音节。【11】话音刚落，门外那个宛若铁塔般的虬髯大汉霍齐，猛然间杀气暴涨！【12】他一把扯下挂在墙角的硬弓，【13】仿佛一头嗅到血腥味的狂熊。没有任何犹豫，【14】霍齐卷起一股肃杀的寒风，猛地撞开那扇摇摇欲坠的木门，直接冲入了屋外那漆黑的冰天雪地之中，去追寻那个根本不存在的“刺客”！"
    },
    'S02': {
        title: "第二段：血泪对峙，徒手夺利刃",
        narration: "【01】呼呼的风雪声中，黑熊护卫被成功支走。辛月影紧绷的神经终于得到了一丝喘息，她脱力地蹲在地上，开始收拾满地的残局。【02】突然，死寂的屋内，传来一声极其细微的“滴答”声。【03】她疑惑地回过头，只见沈清起依旧安静地坐在破败的轮椅上，仿佛一尊被遗弃的瓷娃娃。【04】然而，当她的目光顺着他白皙的腕骨向下移动……【05】滴答！一滴纯粹、刺目的殷红鲜血，狠狠砸在了肮脏的石板地上！【06】辛月影的视线猛然上移——天哪！【07】这个彻头彻尾的疯批，竟然用那张苍白的手，死死地、不计后果地紧紧攥着那枚无比锋利的碎瓷片！【08】鲜血如同断了线的珠子，顺着他修长的指缝，止不住地往下淌！【09】“疯了！你真疯了！”辛月影连滚带爬地扑上前去，一把死死摁住他那只血肉模糊的铁拳！【10】看似虚弱的沈清起，手上的力道却大得惊人，宛若焊死的铁钳！【11】辛月影挤出几滴鳄鱼的眼泪，抬起头带着哭腔喊道：“相公！你这是干什么？！你难道不要命了吗？！”【12】沈清起缓缓低下头。那双被血丝填满的狭长凤眼中，唯有刺骨的冰冷与无尽的恨意！【13】辛月影把吃奶的劲都使出来了，脸颊憋得通红，青筋暴起，却依然无法撼动那只铁拳分毫！【14】“痛？”沈清起的喉咙底，滚出一声令人毛骨悚然的嘶哑自嘲，【15】随后，他的嘴角缓缓拉扯出一抹极其诡异、悲凉而又绝望的凄恻笑意：“我还有亲人吗？这世上，谁还会为我痛？”【16】绝境之中，辛月影脑中灵光一闪，她歇斯底里地脱口而出：“霍齐会心疼啊！他对你那么忠心，他看到你这样会心疼死的！”【17】这句话，如同某种古老的咒语，竟真的让那铁铸般的拳头，悄然松动了一丝！【18】辛月影毫不迟疑，立刻如同剥洋葱一般，一根一根地将那沾满鲜血的手指用力掰开。【19】那一刻，沈清起惨烈而血肉翻卷的掌心，彻底暴露在她面前，触目惊心！"
    },
    'S03': {
        title: "第三段：金蝉脱壳，风雪暗遁走",
        narration: "【01】就在这千钧一发之际，“砰！”的一声巨响，摇摇欲坠的木门被暴力撞开！暴风雪如同野兽般呼啸而入！【02】带着满身风雪的霍齐，像一尊怒目金刚般大跨步冲了进来！【03】“没看到半个刺客！你这毒妇究竟在耍什么花样——”怒吼声还在喉干打转！【04】辛月影却已猛地转过头，厉声打断他：“相公自残割伤了手！快拿去包扎啊！”【05】霍齐那张写满震怒的脸，在看清沈清起那血肉模糊的掌心时，瞬间崩塌为极度的惊恐！【06】这如铁塔般的汉子，“扑通”一声，重重地双膝跪在轮椅前！【07】他痛苦地扯下腰带，笨拙而慌乱地为主人包扎着伤口，【08】“二爷！就算不顾你自个，你、你也得全了黄泉下老爷夫人们的颜面啊！”虎目含泪，悲痛欲绝的哭号在破屋内回荡。【09】沈清起缓缓闭上双眼，眉宇间凝结着化不开的沉痛。随着两声压抑到极致的闷咳，【10】他再次睁开那双锐利如刀的凤眼，仅仅吐出一个毫无感情的字眼：“滚。”【11】如蒙大赦！辛月影几乎是在听到那字的瞬间，干净利落地转过身！动作丝滑得没有半分犹豫！【12】她毫不留恋地褪下身上那件补丁摞补丁的粗布长褂，看也不看地向后高高抛去！【13】那带着淡淡体温的破布衣，精准无误地飘落在沈清起那双早已失去知觉、冰冷的残腿上。【14】而此时的辛月影，早已脚底抹油，在扬起的尘土中，逃命般地冲向了门外的风雪之中！"
    },
    'S04': {
        title: "第四段：前路未卜，暗夜遇杀星",
        narration: "【01】一口气冲出破败的农舍，冰冷的夜风如刀割般打在脸上，辛月影这才惊觉，这座荒废的沈家小院，竟是比鬼屋还要阴森几分！【02】她大口大口地喘着粗气，还未来得及为死里逃生感到庆幸，【03】在那犹如黑洞般的院墙拐角处，一道扛着重物的黑影，竟无声无息地缓缓浮现！【04】辛月影猛地刹住脚步，瞳孔在冷月下极具收缩！心脏仿佛被人一把攥紧！【05】月光惨白，照亮了来人的面目。颧骨高耸，眼神下流，额角还贴着一块恶劣的黑狗皮膏药……王屠户！正是原主不知廉耻勾搭上的那个卑劣情夫！【06】然而，最令人毛骨悚然的并非他那张猥琐的脸，【07】而是他那双粗糙黑黄的手中，正死死地握着一把沾满泥土的生锈铁锨！【08】更深重露，满身杀气，他提着这挖坟掘墓的家伙事儿，究竟是来杀谁？又是来埋谁？！【09】辛月影手脚冰凉，本能地转过头，望向那座刚刚逃离的破旧农舍……【10】屋内那一豆微光，不知何时已然诡异地熄灭！【11】那个残缺的窗口，此刻犹如通往幽冥的入口，黑暗中，仿佛有两双潜伏在暗夜的嗜血之瞳，正静静地、玩味地注视着这一切。"
    }
};

const dict = {
    "Xin Yueying": "辛月影", "Shen Qingqi": "沈清起", "Huo Qi": "霍齐", "Butcher Wang": "屠户王",
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

const out = [];
out.push("# 穿书后我攻略了奸臣首辅 - 第二章 图文解说稿");
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
console.log('SUCCESS: Written Chapter 2 Third-Person');
