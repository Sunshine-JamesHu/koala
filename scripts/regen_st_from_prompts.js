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
        // Extract ID, e.g., ### S01 #01 `C01_S01_01.jpg`
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
            // The first paragraph of the code block is the description
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
    "刚穿书就被发配到发霉的破屋子？", // S01_01
    "耳边传来冷冰冰的一句‘你自尽吧’", // S01_02
    "什么情况？我顶着头痛吃力地睁开眼", // S01_03
    "刺鼻的发霉味儿冲进鼻腔，这待遇绝了", // S01_04
    "不过没事，我懂流程，这绝壁是个梦！索性翻了个身准备好好欣赏", // S01_05
    "我倒要看看，入我梦的纸片人，到底是清纯小奶狗，还是腹黑老男神？", // S01_06
    "结果对面那黑影居然凑近了，冷笑：‘莫不是要我亲自送你一程？’", // S01_07
    "月光一照，卧槽！神仙颜值！但……这眼神怎么跟淬了毒一样？", // S01_08
    "他坐在一张破败轮椅上，脚下全是碎瓷残羹，像是个落魄的暴君。", // S01_09
    "‘辛四娘，你在等什么？’他薄唇轻启，杀意扑面而来！", // S01_10
    "辛四娘？我倒吸一口凉气，笑容瞬间僵在脸上。", // S01_11
    "这名字好耳熟……我浑身打了个冷战！", // S01_12
    "原书中大反派沈清起在地牢里满身是血的画面疯狂涌入脑海！", // S01_13
    "还有作死女配‘辛四娘’端着毒药靠近他的阴毒嘴脸……", // S01_14
    "妈耶！我瞳孔大地震！我穿成了开局就给顶级病娇变态反派喂毒药的炮灰女配！", // S01_15
    "要命啊！地上的长剑正反射着刺目的寒光！", // S02_01
    "这病娇反派盯着我的眼神，简直是要把我千刀万剐！", // S02_02
    "强烈的求生欲让我连滚带爬地往门边狂退！", // S02_03
    "后背砰地撞在木柱上，退无可退，腿肚子都在发抖。", // S02_04
    "‘大…大哥！如果我说我是穿越的，你能信吗？！’", // S02_05
    "他根本不接茬，枯瘦的手像死神一样伸向了剑柄。", // S02_06
    "三尺青锋拔地而起，剑尖直指导演镜头！", // S02_07
    "主观视角暴击！冰冷的剑尖抵着我眉心，窒息感拉满，谁懂啊家人们！", // S02_08
    "我急中生智，眼神狂瞟向侧后方那扇掉漆的木门，那是唯一的生机。", // S02_09
    "就在我脚尖刚往外试探性地挪了一寸的瞬间！", // S02_10
    "一束快到带残影的凌厉剑光劈面而来！", // S02_11
    "我尖叫一声，整个人朝旁边猛地疯狂倒下规避伤害！", // S02_12
    "‘嗡——’长剑贴着我脖子大动脉划过，死死钉入木柱，剧烈震颤！差点就物理切片了！", // S02_13
    "太恐怖了！这疯批根本不按套路出牌！我转身就不顾一切地往门外狂奔！", // S03_01
    "结果还没跑出屋檐，砰地一下撞上一堵肉墙，直接给我疼惨了。", // S03_02
    "抬头一看，一个像铁塔一样的络腮胡黑熊精正愤怒地瞪着我。", // S03_03
    "‘吃了熊心豹子胆！敢给二爷下毒！’这破锣嗓门震得我耳膜生疼。", // S03_04
    "他那粗壮的胳膊像拎小鸡一样，一把将我狠狠掀翻推了回去。", // S03_05
    "我又跌跌撞撞、连滚带爬地回到了这个阴暗的地狱开局。", // 03_06
    "一回头，轮椅上的沈清起正似笑非笑地看着我，就像看着无处可逃的老鼠。", // 03_07
    "完蛋！前有黑熊护卫拦路，后有疯批反派要命。沈清起修长的手指玩弄着锋利的碎瓷片。", // 04_01
    "‘要么自绝于此，要么我给你一刀痛快。’阎王爷正式下达了终极判决书。", // 04_02
    "我瘫坐在地上，大脑CPU疯狂燃烧，飞速寻找生机对策。不能怂！", // 04_03
    "在死亡面前，每个人都是奥斯卡影后！我双眼猛地瞪大如铜铃，故作震惊！", // 04_04
    "双手‘啪’地一合，直接影后附体，反客为主：‘什么？那居然是毒药？！’", // 04_05
    "我就不信我这出精湛的装傻充愣，还糊弄不过去？这俩人冷冷地看我飙演技。", // 04_06
    "我急得眼带泪花，深情且恐慌地甩锅：‘有人逼我的！他没说是毒药，我只能照做啊！’", // 04_07
    "结果……这大魔王居然从鼻腔里发出一声极其嘲弄、看穿一切的冷嗤。", // 04_08
    "我咬咬牙，继续加码表演：‘他威胁我不放这就杀了我！我是极其无辜的！’", // 04_09
    "我用‘极其关切’的目光看着他疯狂洗白：‘相公你是不是得罪了什么仇家？人家要害你啊！’", // 04_10
    "听完我这段精彩绝伦的口才，他竟然发出一长串渗人的低笑，听得人毛骨悚然。", // 04_11
    "笑声戛然而止。他看我的眼神像是在看一具尸体：‘不论是谁，且让他下黄泉陪你吧。’ 完了，芭比Q了！演砸了！" // 04_12
];

while (narrations.length < shots.length) {
    narrations.push("...");
}

const out = [];
out.push("# 穿书后我攻略了奸臣首辅 - 第一章 图文解说稿");
out.push("> **用途**: 短视频/推文解说配音脚本 (物理级别1:1对齐 04_prompts.md 的图)");
out.push("> **配音基调**: 网感、吐槽、悬疑跌宕、绝地求生");
out.push("---");

// Simple dictionary for English to Chinese keyword mapping
const dict = {
    "Xin Yueying": "辛月影",
    "Shen Qingqi": "沈清起",
    "Huo Qi": "霍齐",
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
    "darkness": "黑暗"
};

function crudeTranslate(engDesc) {
    let cn = engDesc;
    for (const [en, zh] of Object.entries(dict)) {
        cn = cn.split(en).join(zh);
    }
    return cn;
}

for (let i = 0; i < shots.length; i++) {
    const s = shots[i];
    out.push(`## 镜${i + 1} (\`${s.id}\`)`);
    out.push("");
    out.push("> 对应 04_prompts.md 中的生图提示词画面:");
    out.push(`> **英文原文**: ${s.desc}`);
    out.push(`> **构图机位**: ${s.camera}`);
    out.push("");
    out.push("**推文解说视角描述 (基于生图)**：");
    out.push(`${crudeTranslate(s.desc)}`);
    out.push("");
    out.push("**旁白文案**：");
    out.push(`“${narrations[i]}”`);
    out.push("");
    out.push("---");
}

fs.writeFileSync(stPath, out.join("\n"), "utf8");
console.log(`SUCCESS: Physically mapped ${shots.length} shots from 04_prompts.md to 05_storytelling.md`);
