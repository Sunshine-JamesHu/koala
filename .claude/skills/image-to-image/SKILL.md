---
name: Image to Image
description: 使用火山引擎即梦AI图生图3.0智能参考API，基于参考图片和文本指令生成新图片。
---

# image-to-image

使用火山引擎即梦AI图生图3.0智能参考API，基于参考图片和文本指令生成新图片。

## 用法

```bash
uv run python .claude/skills/image-to-image/image_to_image.py --image "图片路径" --prompt "编辑指令" [选项]
```

## 参数

| 参数 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| `--image` | 是 | - | 参考图片路径（本地文件或URL） |
| `--prompt` | 是 | - | 编辑指令文本 |
| `--output` | 否 | `cache/generated_images` | 输出目录 |
| `--filename` | 否 | `image_{时间戳}` | 自定义文件名（不含扩展名） |
| `--strength` | 否 | `0.5` | 编辑强度（0.0-1.0），越大变化越大 |
| `--width` | 否 | - | 图片宽度（像素） |
| `--height` | 否 | - | 图片高度（像素） |

## 环境变量

需要设置以下环境变量：
- `HS_AccessKeyID`: 火山引擎 AccessKey ID
- `HS_SecretAccessKey`: 火山引擎 Secret Access Key

## 示例

```bash
# 基本用法 - 使用本地图片
uv run python .claude/skills/image-to-image/image_to_image.py \
  --image "assets/characters/沈清起/front.png" \
  --prompt "将人物转换为水彩画风格"

# 使用图片URL
uv run python .claude/skills/image-to-image/image_to_image.py \
  --image "https://example.com/reference.jpg" \
  --prompt "将背景改为樱花树下的日本庭院"

# 指定编辑强度和输出路径
uv run python .claude/skills/image-to-image/image_to_image.py \
  --image "works/穿书后我攻略了奸臣首辅/assets/scenes/garden.png" \
  --prompt "将白天场景改为夜晚，添加月光和萤火虫" \
  --strength 0.7 \
  --output "works/穿书后我攻略了奸臣首辅/assets/scenes/night"

# 生成角色不同表情
uv run python .claude/skills/image-to-image/image_to_image.py \
  --image "assets/characters/沈清起/front.png" \
  --prompt "保持人物特征不变，将表情改为微笑" \
  --strength 0.3 \
  --output "assets/characters/沈清起/expressions" \
  --filename "smile"
```

## 编辑强度说明

| 强度值 | 效果描述 | 适用场景 |
|--------|----------|----------|
| 0.1-0.3 | 轻微修改 | 表情变化、小细节调整 |
| 0.4-0.6 | 中等修改 | 风格转换、背景替换 |
| 0.7-0.9 | 大幅修改 | 构图调整、场景重构 |

## 输出

生成的图片将保存到指定目录（默认为 `cache/generated_images/`），文件名格式为 `image_YYYYMMDD_HHMMSS.png`。

脚本执行成功后会输出图片的完整路径。

## 参考文档

- [即梦图生图3.0智能参考-产品介绍](https://www.volcengine.com/docs/85621/1544716)
- [即梦图生图3.0智能参考-接口文档](https://www.volcengine.com/docs/85621/1747301)
- [火山引擎API密钥管理](https://console.volcengine.com/iam/keymanage)
