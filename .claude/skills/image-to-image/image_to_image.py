#!/usr/bin/env python3
"""
火山引擎即梦AI图生图3.0智能参考 API调用脚本

使用火山引擎官方SDK调用即梦AI图生图API，基于参考图片和文本指令生成新图片。

环境变量:
    HS_AccessKeyID: 火山引擎 AccessKey ID
    HS_SecretAccessKey: 火山引擎 Secret Access Key

用法:
    uv run python image_to_image.py --image "图片路径" --prompt "编辑指令" [选项]
"""

import os
import sys
import argparse
import base64
import requests
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def is_url(path: str) -> bool:
    """判断路径是否为URL"""
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def load_image_as_base64(image_path: str) -> str:
    """
    将本地图片转换为base64编码

    Args:
        image_path: 本地图片路径

    Returns:
        base64编码的图片字符串

    Raises:
        FileNotFoundError: 图片文件不存在
    """
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"图片文件不存在: {image_path}")

    with open(path, "rb") as f:
        image_data = f.read()

    return base64.b64encode(image_data).decode("utf-8")


def get_image_base64(image_source: str) -> str:
    """
    获取图片的base64编码（支持本地文件和URL）

    Args:
        image_source: 图片路径或URL

    Returns:
        base64编码的图片字符串
    """
    if is_url(image_source):
        # 从URL下载图片
        print(f"正在从URL下载图片: {image_source[:50]}...")
        response = requests.get(image_source, timeout=60)
        response.raise_for_status()
        return base64.b64encode(response.content).decode("utf-8")
    else:
        # 从本地文件读取
        return load_image_as_base64(image_source)


def generate_image(
    image_source: str,
    prompt: str,
    output_dir: str = "cache/generated_images",
    strength: float = 0.5,
    width: int = None,
    height: int = None,
    filename: str = None
) -> str:
    """
    使用即梦AI图生图生成图片

    Args:
        image_source: 参考图片路径或URL
        prompt: 编辑指令文本
        output_dir: 输出目录
        strength: 编辑强度（0.0-1.0）
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

    # 获取图片base64编码
    image_base64 = get_image_base64(image_source)

    # 延迟导入，确保在uv环境中
    from volcengine.visual.VisualService import VisualService

    # 初始化服务
    visual_service = VisualService()
    visual_service.set_ak(ak)
    visual_service.set_sk(sk)

    # 构建请求参数
    form = {
        "req_key": "jimeng_i2i_v30",  # 图生图3.0智能参考
        "prompt": prompt,
        "binary_data_base64": [image_base64],  # 注意：必须是数组格式
        "scale": strength,  # 编辑强度参数名为scale
        "return_url": True
    }

    # 可选尺寸参数
    if width:
        form["width"] = width
    if height:
        form["height"] = height

    print(f"正在生成图片: {prompt[:50]}...")
    print(f"编辑强度: {strength}")

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
        description="即梦AI图生图 - 基于参考图片和文本指令生成新图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --image "photo.png" --prompt "将图片转换为水彩画风格"
  %(prog)s --image "https://example.com/img.jpg" --prompt "更换背景为樱花树"
  %(prog)s --image "char.png" --prompt "改变表情为微笑" --strength 0.3

环境变量:
  HS_AccessKeyID     火山引擎 AccessKey ID
  HS_SecretAccessKey 火山引擎 Secret Access Key

编辑强度说明:
  0.1-0.3: 轻微修改（表情变化、小细节调整）
  0.4-0.6: 中等修改（风格转换、背景替换）
  0.7-0.9: 大幅修改（构图调整、场景重构）
        """
    )
    parser.add_argument(
        "--image",
        required=True,
        help="参考图片路径（本地文件或URL）"
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="编辑指令文本"
    )
    parser.add_argument(
        "--output",
        default="cache/generated_images",
        help="输出目录 (默认: cache/generated_images)"
    )
    parser.add_argument(
        "--strength",
        type=float,
        default=0.5,
        help="编辑强度，范围0.0-1.0 (默认: 0.5)"
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
        help="自定义文件名（不含扩展名）"
    )
    args = parser.parse_args()

    # 验证编辑强度范围
    if not 0 <= args.strength <= 1:
        print("错误: 编辑强度必须在0.0到1.0之间", file=sys.stderr)
        sys.exit(1)

    try:
        filepath = generate_image(
            args.image,
            args.prompt,
            args.output,
            args.strength,
            args.width,
            args.height,
            args.filename
        )
        print(f"\n图片已生成: {filepath}")
    except FileNotFoundError as e:
        print(f"\n文件错误: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"\n配置错误: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"\n生成失败: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
