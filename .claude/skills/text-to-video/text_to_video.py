#!/usr/bin/env python3
"""
火山引擎即梦AI视频生成3.0 Pro API调用脚本

使用火山引擎官方SDK调用即梦AI视频生成API，根据文本描述生成视频。
支持文生视频和图生视频两种模式。

环境变量:
    HS_AccessKeyID: 火山引擎 AccessKey ID
    HS_SecretAccessKey: 火山引擎 Secret Access Key

用法:
    uv run python text_to_video.py --prompt "描述文本" [选项]
"""

import os
import sys
import argparse
import time
import requests
from datetime import datetime
from pathlib import Path


# 视频比例选项
ASPECT_RATIOS = ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"]
# 分辨率选项
RESOLUTIONS = ["720p", "1080p"]


def generate_video(
    prompt: str,
    output_dir: str = "cache/generated_videos",
    aspect_ratio: str = "16:9",
    resolution: str = "720p",
    image_url: str = None,
    max_wait: int = 600
) -> str:
    """
    使用即梦AI生成视频

    Args:
        prompt: 视频描述文本
        output_dir: 输出目录
        aspect_ratio: 视频比例
        resolution: 分辨率
        image_url: 首帧图片URL（可选，用于图生视频）
        max_wait: 最大等待时间（秒）

    Returns:
        生成视频的本地路径

    Raises:
        ValueError: 环境变量未设置或参数无效
        RuntimeError: API调用失败
        TimeoutError: 视频生成超时
    """
    # 从环境变量获取认证信息
    ak = os.environ.get("HS_AccessKeyID")
    sk = os.environ.get("HS_SecretAccessKey")

    if not ak or not sk:
        raise ValueError(
            "请设置环境变量 HS_AccessKeyID 和 HS_SecretAccessKey\n"
            "密钥申请地址: https://console.volcengine.com/iam/keymanage"
        )

    # 验证参数
    if aspect_ratio not in ASPECT_RATIOS:
        raise ValueError(f"无效的aspect_ratio: {aspect_ratio}，可选值: {ASPECT_RATIOS}")
    if resolution not in RESOLUTIONS:
        raise ValueError(f"无效的resolution: {resolution}，可选值: {RESOLUTIONS}")

    # 延迟导入，确保在uv环境中
    from volcengine.visual.VisualService import VisualService

    # 初始化服务
    visual_service = VisualService()
    visual_service.set_ak(ak)
    visual_service.set_sk(sk)

    # 构建请求参数
    req_key = "jimeng_i2v_v30" if image_url else "jimeng_t2v_v30"
    form = {
        "req_key": req_key,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution
    }

    if image_url:
        form["image_url"] = image_url
        print(f"图生视频模式，首帧图片: {image_url}")
    else:
        print(f"文生视频模式")

    print(f"正在生成视频: {prompt[:50]}...")
    print(f"参数: aspect_ratio={aspect_ratio}, resolution={resolution}")

    # 提交任务
    resp = visual_service.cv_process(form)

    # 检查响应
    if resp.get("code") and resp.get("code") != 10000:
        raise RuntimeError(f"API错误: {resp.get('message', resp)}")

    task_id = resp.get('data', {}).get('task_id')
    if not task_id:
        raise RuntimeError(f"任务提交失败，未返回task_id: {resp}")

    print(f"任务已提交，task_id: {task_id}")

    # 轮询任务状态
    video_url = poll_video_result(visual_service, task_id, max_wait)

    # 确保输出目录存在
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"video_{timestamp}.mp4"
    filepath = output_path / filename

    # 下载并保存视频
    print("正在下载视频...")
    response = requests.get(video_url, timeout=120)
    response.raise_for_status()
    filepath.write_bytes(response.content)

    return str(filepath)


def poll_video_result(
    visual_service,
    task_id: str,
    max_wait: int = 600,
    interval: int = 5
) -> str:
    """
    轮询视频生成结果

    Args:
        visual_service: VisualService实例
        task_id: 任务ID
        max_wait: 最大等待时间（秒）
        interval: 轮询间隔（秒）

    Returns:
        视频URL

    Raises:
        RuntimeError: 视频生成失败
        TimeoutError: 视频生成超时
    """
    start_time = time.time()
    print(f"等待视频生成（最长等待{max_wait}秒）...")

    while time.time() - start_time < max_wait:
        elapsed = int(time.time() - start_time)

        # 查询任务状态
        try:
            resp = visual_service.cv_process({
                "req_key": "jimeng_t2v_v30_query",
                "task_id": task_id
            })
        except Exception as e:
            print(f"查询状态出错: {e}，继续重试...")
            time.sleep(interval)
            continue

        status = resp.get('data', {}).get('status')

        if status == 'succeed':
            video_urls = resp.get('data', {}).get('video_urls', [])
            if video_urls:
                print(f"\n✅ 视频生成完成！（耗时{elapsed}秒）")
                return video_urls[0]
        elif status == 'failed':
            error_msg = resp.get('data', {}).get('message', '未知错误')
            raise RuntimeError(f"视频生成失败: {error_msg}")

        # 显示进度
        progress = resp.get('data', {}).get('progress', 0)
        print(f"\r  生成中... {progress}% ({elapsed}s)", end="", flush=True)
        time.sleep(interval)

    print()  # 换行
    raise TimeoutError(f"视频生成超时（{max_wait}秒）")


def main():
    parser = argparse.ArgumentParser(
        description="即梦AI视频生成 - 使用文本描述生成视频",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本文生视频
  %(prog)s --prompt "千军万马奔腾的场景"

  # 指定视频比例和分辨率
  %(prog)s --prompt "日落时分的海边" --aspect-ratio "21:9" --resolution "1080p"

  # 图生视频
  %(prog)s --prompt "女孩慢慢睁开眼睛" --image "https://example.com/image.png"

  # 手机竖屏视频
  %(prog)s --prompt "美食制作过程" --aspect-ratio "9:16"

环境变量:
  HS_AccessKeyID     火山引擎 AccessKey ID
  HS_SecretAccessKey 火山引擎 Secret Access Key
        """
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="视频描述文本"
    )
    parser.add_argument(
        "--output",
        default="cache/generated_videos",
        help="输出目录 (默认: cache/generated_videos)"
    )
    parser.add_argument(
        "--aspect-ratio",
        default="16:9",
        choices=ASPECT_RATIOS,
        help="视频比例 (默认: 16:9)"
    )
    parser.add_argument(
        "--resolution",
        default="720p",
        choices=RESOLUTIONS,
        help="分辨率 (默认: 720p)"
    )
    parser.add_argument(
        "--image",
        help="首帧图片URL（用于图生视频）"
    )
    parser.add_argument(
        "--max-wait",
        type=int,
        default=600,
        help="最大等待时间（秒，默认: 600）"
    )
    args = parser.parse_args()

    try:
        filepath = generate_video(
            args.prompt,
            args.output,
            args.aspect_ratio,
            args.resolution,
            args.image,
            args.max_wait
        )
        print(f"\n✅ 视频已生成: {filepath}")
    except ValueError as e:
        print(f"\n❌ 配置错误: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"\n❌ 生成失败: {e}", file=sys.stderr)
        sys.exit(1)
    except TimeoutError as e:
        print(f"\n❌ 超时: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
