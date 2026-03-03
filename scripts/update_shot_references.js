const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname, '..', 'works', '穿书后我攻略了奸臣首辅', 'output', 'chapter_001');

// 新旧编号映射: { 新shot文件夹号: { oldShot: 旧shot编号, oldScene: 旧镜头编号, newScene: 新镜头编号, prevShot: 新的上一个shot编号 } }
const MAPPING = {
  '004': { oldShot: '003', oldScene: 'S01-03', newScene: 'S01-04', prevShot: '003' },
  '005': { oldShot: '004', oldScene: 'S01-04', newScene: 'S01-05', prevShot: '004' },
  '006': { oldShot: '005', oldScene: 'S01-05', newScene: 'S01-06', prevShot: '005' },
  '007': { oldShot: '006', oldScene: 'S01-06', newScene: 'S01-07', prevShot: '006' },
  '008': { oldShot: '007', oldScene: 'S01-07', newScene: 'S01-08', prevShot: '007' },
  '009': { oldShot: '008', oldScene: 'S01-08', newScene: 'S01-09', prevShot: '008' },
  '010': { oldShot: '009', oldScene: 'S01-09', newScene: 'S01-10', prevShot: '009' },
  '011': { oldShot: '010', oldScene: 'S01-10', newScene: 'S01-11', prevShot: '010' },
  // shot_012 是新建的，不需要映射
  '013': { oldShot: '011', oldScene: 'S01-11', newScene: 'S01-13', prevShot: '012' },
  '014': { oldShot: '012', oldScene: 'S01-12', newScene: 'S01-14', prevShot: '013' },
  '015': { oldShot: '013', oldScene: 'S01-13', newScene: 'S01-15', prevShot: '014' },
  '016': { oldShot: '014', oldScene: 'S01-14', newScene: 'S01-16', prevShot: '015' },
  '017': { oldShot: '015', oldScene: 'S01-15', newScene: 'S01-17', prevShot: '016' },
  '018': { oldShot: '016', oldScene: 'S01-16', newScene: 'S01-18', prevShot: '017' },
  '019': { oldShot: '017', oldScene: 'S01-17', newScene: 'S01-19', prevShot: '018' },
  // shot_020 是新建的，不需要映射
  '021': { oldShot: '018', oldScene: 'S01-18', newScene: 'S01-21', prevShot: '020' },
};

// 上一个shot的旧编号映射（用于替换first_frame.md和guide.md中引用的上一镜头）
const PREV_SHOT_OLD = {
  '004': '002', // shot_004的上一个是shot_003(旧shot_002)，但shot_003是新增的，原来旧shot_003引用的上一个是shot_002
  '005': '003', // 旧shot_004引用的上一个是旧shot_003
  '006': '004', // 旧shot_005引用的上一个是旧shot_004
  '007': '005',
  '008': '006',
  '009': '007',
  '010': '008',
  '011': '009',
  '013': '010',
  '014': '011',
  '015': '012',
  '016': '013',
  '017': '014',
  '018': '015',
  '019': '016',
  '021': '017',
};

const MD_FILES = ['video_prompt.md', 'first_frame.md', 'last_frame.md', 'storyboard_grid.md', 'guide.md'];

let totalChanges = 0;
let totalFiles = 0;

for (const [newShotNum, mapping] of Object.entries(MAPPING)) {
  const shotDir = path.join(BASE_DIR, `shot_${newShotNum}`);

  if (!fs.existsSync(shotDir)) {
    console.log(`[SKIP] shot_${newShotNum} 目录不存在`);
    continue;
  }

  for (const mdFile of MD_FILES) {
    const filePath = path.join(shotDir, mdFile);

    if (!fs.existsSync(filePath)) {
      continue;
    }

    let content = fs.readFileSync(filePath, 'utf-8');
    const originalContent = content;

    // 1. 替换镜头编号 S01-XX
    content = content.replaceAll(mapping.oldScene, mapping.newScene);

    // 2. 替换本镜头的shot文件名引用 shot_XXX
    content = content.replaceAll(`shot_${mapping.oldShot}`, `shot_${newShotNum}`);

    // 3. 替换上一镜头的shot引用（first_frame.md和guide.md中引用上一个shot）
    const prevOld = PREV_SHOT_OLD[newShotNum];
    if (prevOld && mapping.prevShot) {
      // 只替换明确作为"上一镜头"引用的内容
      // 上一镜头的旧编号 → 新编号
      if (prevOld !== mapping.prevShot) {
        content = content.replaceAll(`shot_${prevOld}`, `shot_${mapping.prevShot}`);
      }
    }

    if (content !== originalContent) {
      fs.writeFileSync(filePath, content, 'utf-8');
      const changeCount = countDifferences(originalContent, content);
      totalChanges += changeCount;
      totalFiles++;
      console.log(`[OK] shot_${newShotNum}/${mdFile} - ${changeCount} 处替换`);
    }
  }
}

console.log(`\n===== 完成 =====`);
console.log(`总计修改 ${totalFiles} 个文件，${totalChanges} 处替换`);

function countDifferences(oldStr, newStr) {
  // 简单计数：按行对比
  const oldLines = oldStr.split('\n');
  const newLines = newStr.split('\n');
  let count = 0;
  const maxLen = Math.max(oldLines.length, newLines.length);
  for (let i = 0; i < maxLen; i++) {
    if ((oldLines[i] || '') !== (newLines[i] || '')) {
      count++;
    }
  }
  return count;
}
