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
        title: "第一段：地狱级开局，被反派大佬逼死？",
        narration: "【01】刚穿书就被丢进这发霉的破屋子？没事，我懂流程，这绝壁是个梦！【02】“你自尽吧”——【03】这突然传来的一句冷冰冰的话让我顶着头痛吃力地睁开眼。【04】我去，刺鼻的发霉味儿冲进鼻腔！【05】我索性放松地翻了个身，【06】倒要看看入我梦的纸片人，到底是清纯小奶狗，还是腹黑老男神！【07】结果黑暗中那影子突然前倾：“莫不是要我亲自送你一程？”【08】冰冷的月光一照，卧槽！神仙颜值！但这眼神怎么跟淬了毒一样？！【09】他坐在破败的轮椅上，一地残羹碎瓷片，像个嗜血的君王。【10】“辛四娘，你在等什么？”【11】辛四娘？！卧槽！我想起了什么，笑容瞬间僵在脸上。【12】我浑身狠狠打了个哆嗦！【13】原书中他被铁链锁住、满身鲜血的惨状，【14】还有原主那个恶毒女配端着毒药靠近的阴毒嘴脸疯狂涌入脑海！【15】这哪是穿越，这特么是一开局就给权倾朝野的病娇变态反派下药的火葬场啊！！"
    },
    'S02': {
        title: "第二段：物理切片警告！",
        narration: "【01】还没等我回过神，地上的那把长剑已然反射出一缕夺命的寒芒！【02】沈清起看我的眼神，分明是要把我千刀万剐！【03】在绝对的死亡压迫下，我吓得连滚带爬地疯狂后退！【04】直到后背死死撞在木柱上，退无可退！【05】“大、大哥！如果我说我是穿越的，你能留个全尸不？！”【06】这疯批根本不按套路出牌，枯瘦如柴的手抓起了剑。【07】三尺青锋拔地而起，剑尖直指导演镜头！【08】冰冷的剑尖抵着我眉心的绝望感，谁懂啊家人们！【09】我眼珠子疯狂乱转，死死盯住了侧后方那扇破木门。【10】就在我脚尖刚试探性地往外挪了一寸的瞬间！【11】一束极具压迫感、快出残影的剑光劈面而来！【12】我尖叫一声，身体猛地朝旁边倒下！【13】“嗡——”长剑擦着我的大动脉，剧烈地震颤在柱子里！就差一寸我就物理切片了！"
    },
    'S03': {
        title: "第三段：前有狼后有虎",
        narration: "【01】这疯子真会下死手！我再也不敢作妖，不顾一切地拔腿就往外狂奔！【02】谁知道门外居然堵着人，我砰地一头撞在了一堵结实的肉墙上！【03】抬头一看，一个像铁塔一样的络腮胡黑熊精正愤怒地瞪着我！【04】“吃了熊心豹子胆！敢给二爷下毒！？”这破锣嗓门震得我耳朵疼！【05】他那粗壮的胳膊像拎小鸡一样，一把将我狠狠掀翻推了回去！【06】我又跌跌撞撞地滚回了这个阴暗的地狱开局。【07】一回头，轮椅上的沈清起正似笑非笑地看着我，就像黑猫在欣赏一只无处可退的死耗子。"
    },
    'S04': {
        title: "第四段：绝境求生，奥斯卡影后在此诞生！",
        narration: "【01】前有像半截铁塔一样的护卫挡路，后有疯批要命的病娇男主。只见沈清起修长惨白的手指危险地摩挲着碎瓷片。【02】“要么自绝于此，要么我给你一通快。”阎王爷正式下达判决！【03】我瘫坐在地上，大脑CPU开始疯狂燃烧！拼了！【04】在死亡威胁面前，每个人都是奥斯卡影后！我双眼猛地一睁！【05】双手“啪”的一合，反客为主地装傻充愣：“什么？！那居然是毒药？！”【06】我就不信我这出精湛的演技，还会有破绽？对面这一主一仆面无表情地看我飙花旦戏。【07】我急得满眼泪花，深情且恐慌地甩锅：“有人逼我的！他没说是毒药，我只能照做啊！”【08】演得简直完美……结果这大魔王居然从鼻腔里发出一声看穿一切的讥讽冷嗤！【09】我一咬牙继续发功：“他威胁我不放这就杀了我！人家真的非常无辜！”【10】我“心急如焚”地关心他：“相公你是不是得罪了什么仇家？人家要害你！”【11】听完这段精彩绝伦的狡辩，沈清起的肩膀微微颤动，竟然发出长长一串渗人的笑声，听得人头皮发麻。【12】笑声戛然而止。他看我的眼神完全是在可怜一具不知死活的尸体：“不论是谁，且让他下黄泉陪你吧。”完了！芭比Q了！被彻底看穿了！！"
    }
};

const out = [];
out.push("# 穿书后我攻略了奸臣首辅 - 第一章 图文解说稿");
out.push("> **用途**: 短视频/推文解说配音脚本");
out.push("> **配音基调**: 网感、吐槽、悬疑跌宕、带入感极强");
out.push("> **结构优化**: 采用**大段落连续播讲**，保留文案原有的趣味性和网感；同时在句首标注【序号】实现与生图的物理级 1:1 对齐映射！");
out.push("");

for (const groupName of ['S01', 'S02', 'S03', 'S04']) {
    const groupShots = grouped[groupName];
    if (!groupShots || groupShots.length === 0) continue;

    out.push(`---`);
    out.push(`## ${paragraphData[groupName].title} (共${groupShots.length}图)`);
    out.push("");

    out.push(`**🎙️ 网感连续配音文案 (剪辑师/配音员看这里)**：`);
    out.push(`> 提示：下面这一整段要一口气讲完，情绪连贯。句首括号里的数字代表此时画面**正好切到对应序号的分镜图**。`);
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
console.log('SUCCESS: Written Chapter 1 v2');
