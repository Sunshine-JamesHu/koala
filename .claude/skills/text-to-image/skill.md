# text-to-image

使用火山引擎即梦AI文生图3.1 API生成图片。

## 用法

```bash
uv run python .claude/skills/text-to-image/text_to_image.py --prompt "描述文本" [选项]
```

## 参数

| 参数 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| `--prompt` | 是 | - | 图片描述文本 |
| `--output` | 否 | `cache/generated_images` | 输出目录 |
| `--width` | 否 | - | 图片宽度（像素） |
| `--height` | 否 | - | 图片高度（像素） |
| `--filename` | 否 | `image_{时间戳}` | 自定义文件名（不含扩展名） |

## 环境变量

需要设置以下环境变量：
- `HS_AccessKeyID`: 火山引擎 AccessKey ID
- `HS_SecretAccessKey`: 火山引擎 Secret Access Key

## 示例

```bash
# 基本用法
uv run python .claude/skills/text-to-image/text_to_image.py --prompt "一只可爱的小猫在草地上奔跑"

# 指定输出目录
uv run python .claude/skills/text-to-image/text_to_image.py --prompt "宫崎骏风格的森林场景" --output "works/my_novel/assets/scenes"

# 指定尺寸
uv run python .claude/skills/text-to-image/text_to_image.py --prompt "动漫风格的女孩" --width 1280 --height 720

# 生成角色三视图（指定文件名）
uv run python .claude/skills/text-to-image/text_to_image.py \
  --prompt "Character design, front view, full body..." \
  --output "works/穿书后我攻略了奸臣首辅/assets/characters/沈清起" \
  --filename "front"
```

## 输出

生成的图片将保存到指定目录（默认为 `cache/generated_images/`），文件名格式为 `image_YYYYMMDD_HHMMSS.png`。

脚本执行成功后会输出图片的完整路径。

## 参考文档

- [即梦AI快速入门](https://www.volcengine.com/docs/85621/1995636)
- [即梦文生图3.1接口文档](https://www.volcengine.com/docs/85621/1756900)
