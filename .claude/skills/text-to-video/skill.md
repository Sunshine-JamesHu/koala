# text-to-video

使用火山引擎即梦AI视频生成3.0 Pro API生成视频。

## 用法

```bash
uv run python .claude/skills/text-to-video/text_to_video.py --prompt "描述文本" [选项]
```

## 参数

| 参数 | 必需 | 默认值 | 说明 |
|------|------|--------|------|
| `--prompt` | 是 | - | 视频描述文本 |
| `--output` | 否 | `cache/generated_videos` | 输出目录 |
| `--aspect-ratio` | 否 | `16:9` | 视频比例 |
| `--resolution` | 否 | `720p` | 分辨率 |
| `--image` | 否 | - | 首帧图片URL（图生视频） |
| `--max-wait` | 否 | `600` | 最大等待时间（秒） |

### aspect-ratio 可选值
- `16:9` - 宽屏（默认）
- `4:3` - 标准屏
- `1:1` - 正方形
- `3:4` - 竖屏
- `9:16` - 手机竖屏
- `21:9` - 超宽屏

### resolution 可选值
- `720p` - 高清（默认）
- `1080p` - 全高清

## 环境变量

需要设置以下环境变量：
- `HS_AccessKeyID`: 火山引擎 AccessKey ID
- `HS_SecretAccessKey`: 火山引擎 Secret Access Key

## 示例

```bash
# 基本文生视频
uv run python .claude/skills/text-to-video/text_to_video.py --prompt "千军万马奔腾的场景"

# 指定视频比例和分辨率
uv run python .claude/skills/text-to-video/text_to_video.py --prompt "日落时分的海边" --aspect-ratio "21:9" --resolution "1080p"

# 图生视频（首帧图片）
uv run python .claude/skills/text-to-video/text_to_video.py --prompt "女孩慢慢睁开眼睛" --image "https://example.com/image.png"

# 手机竖屏视频
uv run python .claude/skills/text-to-video/text_to_video.py --prompt "美食制作过程" --aspect-ratio "9:16"
```

## 输出

生成的视频将保存到指定目录（默认为 `cache/generated_videos/`），文件名格式为 `video_YYYYMMDD_HHMMSS.mp4`。

脚本执行成功后会输出视频的完整路径。

## 注意事项

1. 视频生成是异步任务，可能需要等待几分钟
2. 脚本会自动轮询任务状态，直到视频生成完成
3. 默认最大等待时间为10分钟（600秒），可通过 `--max-wait` 参数调整

## 参考文档

- [即梦AI快速入门](https://www.volcengine.com/docs/85621/1995636)
- [即梦AI视频生成3.0 Pro接口文档](https://www.volcengine.com/docs/85621/1777001)
