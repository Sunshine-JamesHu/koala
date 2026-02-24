#!/usr/bin/env python3
"""
火山引擎即梦AI文生图3.1 API调用脚本

使用火山引擎官方SDK调用即梦AI文生图API，根据文本描述生成图片。

环境变量:
    HS_AccessKeyID: 火山引擎 AccessKey ID
    HS_SecretAccessKey: 火山引擎 Secret Access Key

用法:
    uv run python text_to_image.py --prompt "描述文本" [--output "输出目录"] [--width 宽度] [--height 高度]
"""

import os
import sys
import argparse
import requests
from datetime import datetime
from pathlib import Path


def generate_image(
    prompt: str,
    output_dir: str = "cache/generated_images",
    width: int = None,
    height: int = None,
    filename: str = None
) -> str:
    """
    使用即梦AI生成图片

    Args:
        prompt: 图片描述文本
        output_dir: 输出目录
        width: 图片宽度（可选）
        height: 图片高度（可选）
        filename: 自定义文件名（可选，不含扩展名）

    Returns:
        生成图片的本地路径

    Raises:
        ValueError: 环境变量未设置
        RuntimeError: API调用失败
    """
    # 从环境变量获取认证信息
    ak = os.environ.get("HS_AccessKeyID")
    sk = os.environ.get("HS_SecretAccessKey")

    if not ak or not sk:
        raise ValueError(
            "请设置环境变量 HS_AccessKeyID 和 HS_SecretAccessKey\n"
            "密钥申请地址: https://console.volcengine.com/iam/keymanage"
        )

    # 延迟导入，确保在uv环境中
    from volcengine.visual.VisualService import VisualService

    # 初始化服务
    visual_service = VisualService()
    visual_service.set_ak(ak)
    visual_service.set_sk(sk)

    # 构建请求参数
    form = {
        "req_key": "jimeng_high_aes_general_v21_L",  # 文生图3.1
        "prompt": prompt,
        "return_url": True
    }

    # 可选尺寸参数
    if width:
        form["width"] = width
    if height:
        form["height"] = height

    print(f"正在生成图片: {prompt[:50]}...")

    # 调用API
    resp = visual_service.cv_process(form)

    # 检查响应
    if resp.get("code") and resp.get("code") != 10000:
        raise RuntimeError(f"API错误: {resp.get('message', resp)}")

    # 获取图片URL
    image_urls = resp.get('data', {}).get('image_urls', [])
    if not image_urls:
        raise RuntimeError(f"生成失败，未返回图片URL: {resp}")

    # 下载图片
    image_url = image_urls[0]
    print(f"图片URL: {image_url}")

    # 确保输出目录存在
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    if filename:
        # 使用自定义文件名
        final_filename = f"{filename}.png"
    else:
        # 使用时间戳作为文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_filename = f"image_{timestamp}.png"
    filepath = output_path / final_filename

    # 下载并保存图片
    print("正在下载图片...")
    response = requests.get(image_url, timeout=60)
    response.raise_for_status()
    filepath.write_bytes(response.content)

    return str(filepath)


def main():
    parser = argparse.ArgumentParser(
        description="即梦AI文生图 - 使用文本描述生成图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --prompt "一只可爱的小猫在草地上奔跑"
  %(prog)s --prompt "宫崎骏风格的森林" --output "assets/scenes"
  %(prog)s --prompt "动漫女孩" --width 1280 --height 720

环境变量:
  HS_AccessKeyID     火山引擎 AccessKey ID
  HS_SecretAccessKey 火山引擎 Secret Access Key
        """
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="图片描述文本"
    )
    parser.add_argument(
        "--output",
        default="cache/generated_images",
        help="输出目录 (默认: cache/generated_images)"
    )
    parser.add_argument(
        "--width",
        type=int,
        help="图片宽度（像素）"
    )
    parser.add_argument(
        "--height",
        type=int,
        help="图片高度（像素）"
    )
    parser.add_argument(
        "--filename",
        help="自定义文件名（不含扩展名，如 front、side_l、back）"
    )
    args = parser.parse_args()

    try:
        filepath = generate_image(
            args.prompt,
            args.output,
            args.width,
            args.height,
            args.filename
        )
        print(f"\n✅ 图片已生成: {filepath}")
    except ValueError as e:
        print(f"\n❌ 配置错误: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"\n❌ 生成失败: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
