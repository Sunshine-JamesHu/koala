#!/usr/bin/env python3
"""
火山引擎即梦AI图生图3.0智能参考 API调用脚本

使用火山引擎官方SDK调用即梦AI图生图API，基于参考图片和文本指令生成新图片。
支持本地图片直接上传（使用base64编码）或图片URL。

环境变量:
    HS_AccessKeyID: 火山引擎 AccessKey ID
    HS_SecretAccessKey: 火山引擎 Secret Access Key

用法:
    uv run python image_to_image.py --image "图片路径或URL" --prompt "编辑指令" [选项]

Prompt建议:
    - 添加/删除实体：添加/删除xxx（删除图上的女孩/添加一道彩虹）
    - 修改实体：把xxx改成xxx（把手里的鸡腿变成汉堡）
    - 修改风格：改成xxx风格（改成漫画风格）
    - 修改色彩：把xxx改成xx颜色（把衣服改成粉色的）
    - 修改动作：修改表情动作（让他哭/笑/生气）
    - 修改环境背景：背景换成xxx，在xxx（背景换成海边/在星空下）
"""

import os
import sys
import argparse
import base64
import requests
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def load_env_file(env_path: str = None) -> None:
    """从 .env 文件加载环境变量"""
    if env_path is None:
        # image_to_image.py 在 .claude/skills/image-to-image/ 下
        # 需要向上3级到达 koala/ 目录
        script_dir = Path(__file__).parent
        project_root = script_dir.parent.parent.parent
        env_path = project_root / ".env"

    env_file = Path(env_path)
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()


# 启动时自动加载 .env 文件
load_env_file()


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


def download_image_as_base64(url: str) -> str:
    """从URL下载图片并转换为base64"""
    print(f"正在从URL下载图片: {url[:60]}...")
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return base64.b64encode(response.content).decode("utf-8")


def get_image_base64(image_source: str) -> str:
    """
    获取图片的base64编码（支持本地文件和URL）

    Args:
        image_source: 图片路径或URL

    Returns:
        base64编码的图片字符串
    """
    if is_url(image_source):
        return download_image_as_base64(image_source)
    else:
        return load_image_as_base64(image_source)


def generate_image(
    image_sources: list,
    prompt: str,
    output_dir: str = "cache/generated_images",
    scale: float = 0.5,
    width: int = None,
    height: int = None,
    filename: str = None,
    max_wait: int = 300
) -> list:
    """
    使用即梦AI图生图3.0生成图片（异步API）

    Args:
        image_sources: 参考图片路径或URL列表（注意：3.0只支持1张图片）
        prompt: 编辑指令文本
        output_dir: 输出目录
        scale: 编辑强度（0.0-1.0），值越大文本影响越大
        width: 图片宽度（可选，范围512-2016）
        height: 图片高度（可选，范围512-2016）
        filename: 自定义文件名（可选，不含扩展名）
        max_wait: 最大等待时间（秒）

    Returns:
        生成图片的本地路径列表

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

    # 图生图3.0只支持1张输入图片
    if len(image_sources) > 1:
        print("警告: 图生图3.0只支持1张输入图片，将只使用第一张")
        image_sources = [image_sources[0]]

    # 获取图片base64
    print(f"处理参考图片: {image_sources[0][:50]}...")
    image_base64 = get_image_base64(image_sources[0])

    # 延迟导入，确保在uv环境中
    from volcengine.visual.VisualService import VisualService

    # 初始化服务
    visual_service = VisualService()
    visual_service.set_ak(ak)
    visual_service.set_sk(sk)

    # 构建提交任务参数 - 图生图3.0智能参考
    submit_form = {
        "req_key": "jimeng_i2i_v30",  # 图生图3.0智能参考
        "prompt": prompt,
        "binary_data_base64": [image_base64],  # 注意：必须是数组格式
        "scale": scale
    }

    # 可选尺寸参数
    if width and height:
        submit_form["width"] = width
        submit_form["height"] = height

    print(f"正在提交任务: {prompt[:50]}...")
    print(f"编辑强度(scale): {scale}")

    # 提交任务
    submit_resp = visual_service.cv_sync2async_submit_task(submit_form)

    # 检查提交响应
    if submit_resp.get("code") != 10000:
        raise RuntimeError(f"提交任务失败: {submit_resp.get('message', submit_resp)}")

    task_id = submit_resp.get("data", {}).get("task_id")
    if not task_id:
        raise RuntimeError(f"未获取到任务ID: {submit_resp}")

    print(f"任务已提交，task_id: {task_id}")
    print("等待生成...")

    # 轮询查询结果
    start_time = time.time()
    while True:
        if time.time() - start_time > max_wait:
            raise RuntimeError(f"生成超时（超过{max_wait}秒）")

        # 查询任务状态
        query_form = {
            "req_key": "jimeng_i2i_v30",
            "task_id": task_id,
            "req_json": '{"return_url": true}'
        }

        query_resp = visual_service.cv_sync2async_get_result(query_form)

        if query_resp.get("code") != 10000:
            raise RuntimeError(f"查询任务失败: {query_resp.get('message', query_resp)}")

        status = query_resp.get("data", {}).get("status")

        if status == "done":
            # 任务完成
            image_urls = query_resp.get("data", {}).get("image_urls", [])
            if not image_urls:
                raise RuntimeError(f"生成完成但未返回图片: {query_resp}")

            print(f"生成完成，共 {len(image_urls)} 张图片")
            break
        elif status == "in_queue":
            print("任务排队中...")
            time.sleep(2)
        elif status == "generating":
            print("正在生成...")
            time.sleep(3)
        elif status in ["not_found", "expired"]:
            raise RuntimeError(f"任务异常: {status}")
        else:
            print(f"未知状态: {status}")
            time.sleep(2)

    # 确保输出目录存在
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 下载并保存所有图片
    saved_paths = []
    for i, img_url in enumerate(image_urls):
        print(f"正在下载图片 {i+1}/{len(image_urls)}...")
        print(f"图片URL: {img_url[:80]}...")

        # 生成文件名
        if filename and len(image_urls) == 1:
            final_filename = f"{filename}.jpg"  # 图生图3.0输出为jpeg格式
        elif filename:
            final_filename = f"{filename}_{i+1:02d}.jpg"
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_filename = f"image_{timestamp}_{i+1:02d}.jpg"

        filepath = output_path / final_filename

        # 下载图片
        response = requests.get(img_url, timeout=60)
        response.raise_for_status()
        filepath.write_bytes(response.content)

        saved_paths.append(str(filepath))
        print(f"已保存: {filepath}")

    return saved_paths


def main():
    parser = argparse.ArgumentParser(
        description="即梦AI图生图3.0 - 基于参考图片和文本指令生成新图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --image "photo.png" --prompt "将图片转换为水彩画风格"
  %(prog)s --image "https://example.com/img.jpg" --prompt "更换背景为樱花树"
  %(prog)s --image "char.png" --prompt "改变表情为微笑" --scale 0.3

环境变量:
  HS_AccessKeyID     火山引擎 AccessKey ID
  HS_SecretAccessKey 火山引擎 Secret Access Key

Scale说明:
  0.1-0.3: 轻微修改（表情变化、小细节调整）
  0.4-0.6: 中等修改（风格转换、背景替换）
  0.7-0.9: 大幅修改（构图调整、场景重构）

注意:
  - 图生图3.0只支持1张输入图片
  - 输出图片格式为JPEG，尺寸范围[512, 1536]
        """
    )
    parser.add_argument(
        "--image",
        required=True,
        help="参考图片路径或URL"
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
        "--scale",
        type=float,
        default=0.5,
        help="编辑强度，范围0.0-1.0 (默认: 0.5)"
    )
    parser.add_argument(
        "--width",
        type=int,
        help="图片宽度（像素，范围512-2016）"
    )
    parser.add_argument(
        "--height",
        type=int,
        help="图片高度（像素，范围512-2016）"
    )
    parser.add_argument(
        "--filename",
        help="自定义文件名（不含扩展名）"
    )
    parser.add_argument(
        "--max-wait",
        type=int,
        default=300,
        help="最大等待时间，秒 (默认: 300)"
    )
    args = parser.parse_args()

    # 验证scale范围
    if not 0 <= args.scale <= 1:
        print("错误: scale必须在0.0到1.0之间", file=sys.stderr)
        sys.exit(1)

    try:
        filepaths = generate_image(
            [args.image],  # 转换为列表
            args.prompt,
            args.output,
            args.scale,
            args.width,
            args.height,
            args.filename,
            args.max_wait
        )
        print(f"\n✅ 图片已生成:")
        for fp in filepaths:
            print(f"   {fp}")
    except FileNotFoundError as e:
        print(f"\n❌ 文件错误: {e}", file=sys.stderr)
        sys.exit(1)
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
