const fs = require('fs');
const path = require('path');

const baseDir = String.raw:\Projects\koala3\novels\穿书后我攻略了奸臣首辅\chapters\chapter_002;
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
        const match = line.match(/([^]+)/);
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
        } else if (line.startsWith('`	ext')) {
            inCodeBlock = true;
        } else if (line.startsWith('\\\') && inCodeBlock) {
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

const narrations = [
    "为了保住我这颗刚穿过来的脑袋，我直接影后附体", // S01_01
    "声泪俱下地把下毒的锅甩给了一个根本不存在的神秘杀手！",
    "那委屈的表情，连我自己在心里都差点信了！",
    "此人意在羞辱你！杀人诛心啊！我吼得那叫一个情真意切。",
    "不过对面的大佬似乎不太吃这一套，坐在轮椅上跟个冰雕似的一动不动。",
    "那双狭长的凤眼里，甚至连一丝情绪波动都没有！",
    "就在我以为要凉透的时候，他苍白的手突然死死攥紧了碎瓷片！",
    "他扭过头，冷冷地吐出两个字：霍齐。",
    "话音刚落，门外那个像黑熊成精的神仙大护卫立刻就杀了出来！",
    "这肌肉，这压迫感！他一把就抓起了墙上的硬弓！",
    "然后带着一阵暴风雪，直接冲出去找我编造的那个刺客了！",
    "呼危机暂时解除。这傻大个还挺好支走的。", // S01_12
    "刚把护卫支走，我正蹲在地上捡碎瓷片规划下一步。", // S02_01
    "突然，这死寂的屋子里传来清脆的一声滴水声",
    "回头一看，沈清起坐在那，安静得就像一件冰冷却破碎的瓷器。",
    "顺着他的手往下看去", // S02_04
    "嗒！一滴殷红的鲜血直接砸在了脏兮兮的地板上！",
    "天塌了家人们！这疯批男主居然用手死死攥着那块长着尖牙的碎瓷片！血流得像水龙头一样！",
    "倒吸一口凉气！我这不得赶紧表现表现？",
    "我连滚带爬地扑过去，一把摁住他那只血肉模糊的铁拳！",
    "好家伙，这大哥看起来病恹恹的，手上的劲儿怎么这么大？", // S02_09
    "我挤出两滴鳄鱼的眼泪仰头哭喊：相公！你就算难过也别自残啊！",
    "他低头看我，那眼睛里布满血丝，像看死物一样冰冷！",
    "我把吃奶的劲儿都使出来了，脸憋得通红，就是掰不开他那只铁手！", // S02_12
    "亲者痛？他喉咙里滚出一声嘶哑的自嘲。",
    "接着他嘴角勾起一抹诡异又绝望的笑：我还有亲人吗？谁会为我痛？",
    "老天爷！他要发疯了！我急中生智大吼：霍齐会心疼啊！他那么忠心！",
    "还真别说！这句卖主仆CP的话居然真管用了，他的手真的松了一丝！", // S02_16
    "我赶紧像扒洋葱一样，把他的手指一根根剥开，那血肉模糊的掌心简直触目惊心！",
    "就在这时，木门突然砰地一声巨响，风雪倒灌进来！", // S03_01
    "是那只找刺客的黑熊精霍齐回来了！他一进门就怒气冲冲。",
    "没看到刺客！你这贱妇他话还没说完就被我打断了。",
    "我抢答道：相公割伤自己了！快拿纱布！",
    "这傻大个一低头，表情立刻从震怒无缝切换到了极度惊恐！", // S03_04
    "他扑通一声重重跪下，那叫一个悲痛欲绝啊！",
    "他扯下腰带给主子包扎，糙汉子的心都快碎了。",
    "就算不顾自己，也要想想九泉下的老爷夫人啊！他哭喊着。",
    "沈清起闭上眼睛，闷咳了两声，气氛压抑到了极点。", // S03_08
    "突然，他睁开眼，目光如刀子般刺向我，冷冷吐出一个字：滚。",
    "得令！可以！我顺杆爬得极快，连一秒钟都没犹豫！", // S03_10
    "我超级麻利地脱下自己那件打满补丁的破外套，头也不回地往后一抛！",
    "精准覆盖大佬残废的双膝，刷好感度，完美！",
    "然后？然后当然是脚底抹油开溜啊！霍齐在后头还喊着要宰了我呢！", // S03_13
    "一口气冲出破屋，冷风一吹，我才发现这破院子阴森得可怕。", // S04_01
    "这还没松口气呢，院墙拐角处突然慢慢走出一个提着家伙的黑影！",
    "看清那人的脸，我猛地刹住车，心脏都快骤停了！",
    "这就是原主那品味清奇看上的情夫嘛？！眯缝眼，贴膏药，猥琐至极的屠户老王！",
    "关键是，他大半夜提着一把铁锨来干嘛？这绝壁是来帮我埋尸的啊！",
    "我绝望地回头看了一眼那间刚逃出来的破屋子蜡烛竟然已经灭了。", // S04_06
    "那个像黑洞一样的破窗户，此刻仿佛正吞噬着一切。",
    "我敢打赌，那对疯批主仆此刻肯定正躲在冷血的黑暗里，等着看我怎么死在外头呢！" // S04_08
];

while (narrations.length < shots.length) {
    narrations.push("...");
}

const out = [];
out.push("# 穿书后我攻略了奸臣首辅 - 第二章 图文解说稿");
out.push("> **用途**: 短视频/推文解说配音脚本 (物理级别1:1对齐 04_prompts.md 的分镜图)");
out.push("> **配音基调**: 网感、吐槽、悬疑跌宕、极度拉扯");
out.push("---");

const dict = {
    "Xin Yueying": "辛月影",
    "Shen Qingqi": "沈清起",
    "Huo Qi": "霍齐",
    "Butcher Wang": "屠户王",
    "wheelchair": "轮椅",
    "sword": "长剑",
    "oil lamp": "青灯/油灯",
    "dirty stone floor": "脏乱的石板地",
    "moonlight": "月光",
    "wooden door": "木门",
    "wooden pillar": "木柱",
    "bloodless": "毫无血色的",
    "phoenix eyes": "狭长凤眼",
    "terrified": "惊恐的",
    "smirk": "戏谑的笑",
    "shock": "震惊",
    "tears": "眼泪",
    "broken porcelain": "碎瓷片",
    "darkness": "黑暗",
    "blood": "鲜血",
    "fist": "拳头"
};

function crudeTranslate(engDesc) {
    let cn = engDesc;
    for (const [en, zh] of Object.entries(dict)) {
        // Simple string replace for basic context mapping
        cn = cn.split(en).join(zh);
    }
    return cn;
}

for (let i = 0; i < shots.length; i++) {
    const s = shots[i];
    out.push(## 镜 (\${s.id}\));
    out.push("");
    out.push("> **对应 04_prompts.md 生图画面:**");
    out.push(> 原文配图描述: );
    out.push("");
    out.push("**推文解说画面暗示 (配音员参考)**：");
    out.push(${crudeTranslate(s.desc)});
    out.push("");
    out.push("**旁白文案**：");
    out.push(${narrations[i]});
    out.push("");
    out.push("---");
}

fs.writeFileSync(stPath, out.join("\n"), "utf8");
console.log(SUCCESS: Physically mapped  shots from 04_prompts.md to 05_storytelling.md for Chapter 2);
