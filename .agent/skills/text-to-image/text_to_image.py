#!/usr/bin/env python3
"""
火山引擎即梦AI 4.0 文生图 API调用脚本

使用火山引擎官方SDK调用即梦AI 4.0文生图API，根据文本描述生成图片。
即梦4.0支持深度理解意图、多图输入输出、4K超高清输出等能力。

环境变量:
    HS_AccessKeyID: 火山引擎 AccessKey ID
    HS_SecretAccessKey: 火山引擎 Secret Access Key

用法:
    uv run python text_to_image.py --prompt "描述文本" [--output "输出目录"] [--width 宽度] [--height 高度]

Prompt建议:
    - 用连贯的自然语言描述画面内容（主体+行为+环境等）
    - 用短词语描述画面美学（风格、色彩、光影、构图等）
    - 组图生成：使用"一系列""组图""帮我生成几张图"等触发组图
"""

import os
import sys
import argparse
import requests
import time
from datetime import datetime
from pathlib import Path


def load_env_file(env_path: str = None) -> None:
    """从 .env 文件加载环境变量"""
    if env_path is None:
        # 尝试从项目根目录加载 .env
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


def generate_image(
    prompt: str,
    output_dir: str = "cache/generated_images",
    width: int = None,
    height: int = None,
    filename: str = None,
    image_urls: list = None,
    scale: float = 0.5,
    force_single: bool = True,
    max_wait: int = 300,
    return_urls: bool = False
) -> list:
    """
    使用即梦AI 4.0生成图片（异步API）

    Args:
        prompt: 图片描述文本
        output_dir: 输出目录
        width: 图片宽度（可选）
        height: 图片高度（可选）
        filename: 自定义文件名（可选，不含扩展名）
        image_urls: 参考图片URL列表（可选，用于图生图）
        scale: 文本描述影响程度（0-1）
        force_single: 是否强制生成单图
        max_wait: 最大等待时间（秒）
        return_urls: 是否返回图片URL（用于后续图生图）

    Returns:
        如果 return_urls=False: 生成图片的本地路径列表
        如果 return_urls=True: (本地路径列表, 图片URL列表)

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

    # 构建提交任务参数
    submit_form = {
        "req_key": "jimeng_t2i_v40",  # 即梦4.0
        "prompt": prompt,
        "scale": scale,
        "force_single": force_single
    }

    # 添加参考图片URL（图生图场景）
    if image_urls:
        submit_form["image_urls"] = image_urls

    # 可选尺寸参数
    if width and height:
        submit_form["width"] = width
        submit_form["height"] = height

    print(f"正在提交任务: {prompt[:50]}...")

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
            "req_key": "jimeng_t2i_v40",
            "task_id": task_id,
            "req_json": '{"return_url": true}'
        }

        query_resp = visual_service.cv_sync2async_get_result(query_form)

        if query_resp.get("code") != 10000:
            raise RuntimeError(f"查询任务失败: {query_resp.get('message', query_resp)}")

        status = query_resp.get("data", {}).get("status")

        if status == "done":
            # 任务完成
            image_urls_result = query_resp.get("data", {}).get("image_urls", [])
            if not image_urls_result:
                raise RuntimeError(f"生成完成但未返回图片: {query_resp}")

            print(f"生成完成，共 {len(image_urls_result)} 张图片")
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
    for i, img_url in enumerate(image_urls_result):
        print(f"正在下载图片 {i+1}/{len(image_urls_result)}...")

        # 生成文件名
        if filename and len(image_urls_result) == 1:
            final_filename = f"{filename}.png"
        elif filename:
            final_filename = f"{filename}_{i+1:02d}.png"
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_filename = f"image_{timestamp}_{i+1:02d}.png"

        filepath = output_path / final_filename

        # 下载图片
        response = requests.get(img_url, timeout=60)
        response.raise_for_status()
        filepath.write_bytes(response.content)

        saved_paths.append(str(filepath))
        print(f"已保存: {filepath}")

    if return_urls:
        return saved_paths, image_urls_result
    return saved_paths


def main():
    parser = argparse.ArgumentParser(
        description="即梦AI 4.0 文生图 - 使用文本描述生成图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --prompt "一只可爱的小猫在草地上奔跑"
  %(prog)s --prompt "宫崎骏风格的森林" --output "assets/scenes"
  %(prog)s --prompt "动漫女孩" --width 2560 --height 1440
  %(prog)s --prompt "生成一组4张表情包" --force-single false

环境变量:
  HS_AccessKeyID     火山引擎 AccessKey ID
  HS_SecretAccessKey 火山引擎 Secret Access Key

推荐分辨率:
  2K: 2048x2048 (1:1), 2560x1440 (16:9), 2304x1728 (4:3)
  4K: 4096x4096 (1:1), 5404x3040 (16:9), 4694x3520 (4:3)
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
        help="自定义文件名（不含扩展名）"
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=0.5,
        help="文本描述影响程度，范围0-1 (默认: 0.5)"
    )
    parser.add_argument(
        "--force-single",
        type=lambda x: x.lower() == 'true',
        default=True,
        help="是否强制生成单图 (默认: true)"
    )
    parser.add_argument(
        "--max-wait",
        type=int,
        default=300,
        help="最大等待时间，秒 (默认: 300)"
    )
    args = parser.parse_args()

    try:
        filepaths = generate_image(
            args.prompt,
            args.output,
            args.width,
            args.height,
            args.filename,
            scale=args.scale,
            force_single=args.force_single,
            max_wait=args.max_wait
        )
        print(f"\n✅ 图片已生成:")
        for fp in filepaths:
            print(f"   {fp}")
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
