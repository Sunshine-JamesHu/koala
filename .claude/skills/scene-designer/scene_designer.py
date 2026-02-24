#!/usr/bin/env python3
"""
Scene Designer - 场景设计师

设计场景背景，确保风格统一。
"""
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from config import load_project_config, save_json, load_json, PathConfig
from utils import PromptBuilder, clean_text


@dataclass
class KeyElement:
    """场景关键元素"""
    name: str
    type: str  # furniture, architectural, prop, decoration
    description: str
    position: str
    size: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class TimeVariation:
    """时间段变体"""
    lighting: str
    atmosphere: str
    color_temperature: str
    shadow_quality: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class SceneDesign:
    """场景设计"""
    location_id: str
    name: str
    type: str  # indoor, outdoor
    category: str  # residence, palace, street, nature, etc.
    era: Dict[str, str]
    architectural_style: Dict[str, str]
    layout: Dict[str, Any]
    key_elements: List[KeyElement]
    lighting_sources: List[Dict[str, Any]]
    time_variations: Dict[str, TimeVariation]
    weather_variations: Dict[str, Dict[str, str]]
    color_palette: Dict[str, str]
    atmosphere_presets: Dict[str, Dict[str, str]]
    prompt_template: Dict[str, str]

    def to_dict(self) -> dict:
        return {
            "location_id": self.location_id,
            "name": self.name,
            "type": self.type,
            "category": self.category,
            "era": self.era,
            "architectural_style": self.architectural_style,
            "layout": self.layout,
            "key_elements": [e.to_dict() for e in self.key_elements],
            "lighting_sources": self.lighting_sources,
            "time_variations": {k: v.to_dict() for k, v in self.time_variations.items()},
            "weather_variations": self.weather_variations,
            "color_palette": self.color_palette,
            "atmosphere_presets": self.atmosphere_presets,
            "prompt_template": self.prompt_template
        }


class SceneDesigner:
    """场景设计师"""

    # 默认时间段变体
    DEFAULT_TIME_VARIATIONS = {
        "dawn": TimeVariation(
            lighting="微弱的晨光透窗而入",
            atmosphere="宁静、清冷",
            color_temperature="cool",
            shadow_quality="柔和长影"
        ),
        "morning": TimeVariation(
            lighting="明亮的晨光充满空间",
            atmosphere="清爽、充满活力",
            color_temperature="warm_neutral",
            shadow_quality="清晰"
        ),
        "noon": TimeVariation(
            lighting="强烈的阳光直射",
            atmosphere="明亮、活跃",
            color_temperature="neutral",
            shadow_quality="短而清晰"
        ),
        "afternoon": TimeVariation(
            lighting="温暖的午后阳光斜射",
            atmosphere="慵懒、舒适",
            color_temperature="warm",
            shadow_quality="柔和长影"
        ),
        "dusk": TimeVariation(
            lighting="金色余晖",
            atmosphere="温馨、略带忧郁",
            color_temperature="golden",
            shadow_quality="戏剧性长影"
        ),
        "evening": TimeVariation(
            lighting="主要依靠人工照明",
            atmosphere="温馨、私密",
            color_temperature="warm_orange",
            shadow_quality="强烈对比"
        ),
        "night": TimeVariation(
            lighting="昏暗，局部照明",
            atmosphere="静谧、神秘",
            color_temperature="cool_with_warm_accents",
            shadow_quality="深沉阴影"
        ),
        "midnight": TimeVariation(
            lighting="极昏暗",
            atmosphere="神秘、压抑",
            color_temperature="cool_blue",
            shadow_quality="极深阴影"
        )
    }

    # 默认天气变体
    DEFAULT_WEATHER_VARIATIONS = {
        "clear": {"description": "晴朗", "lighting_modifier": "", "atmosphere_modifier": ""},
        "cloudy": {"description": "阴天", "lighting_modifier": "光线平淡柔和", "atmosphere_modifier": "压抑感"},
        "rain": {"description": "下雨", "lighting_modifier": "昏暗阴沉", "atmosphere_modifier": "忧郁、内敛"},
        "snow": {"description": "下雪", "lighting_modifier": "银白色反光", "atmosphere_modifier": "宁静、寒冷"},
        "storm": {"description": "暴风雨", "lighting_modifier": "忽明忽暗", "atmosphere_modifier": "紧张、不安"}
    }

    # 默认氛围预设
    DEFAULT_ATMOSPHERE_PRESETS = {
        "calm": {"lighting": "柔和均匀", "shadow": "轻微", "mood": "宁静"},
        "tense": {"lighting": "强烈对比", "shadow": "戏剧性", "mood": "紧张"},
        "romantic": {"lighting": "温暖柔和", "shadow": "柔和朦胧", "mood": "浪漫"},
        "mysterious": {"lighting": "昏暗局部", "shadow": "深沉", "mood": "神秘"}
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def create_scene(
        self,
        name: str,
        scene_type: str = "indoor",
        category: str = "residence",
        description: str = "",
        era: str = "ancient_chinese"
    ) -> SceneDesign:
        """创建场景设计"""
        location_id = f"loc_{hash(name) % 1000:03d}"

        # 根据类型选择默认元素
        if scene_type == "indoor":
            key_elements = self._get_default_indoor_elements(category)
            architectural_style = self._get_indoor_architectural_style(era)
        else:
            key_elements = self._get_default_outdoor_elements(category)
            architectural_style = self._get_outdoor_architectural_style(era)

        # 默认布局
        layout = {
            "shape": "矩形" if scene_type == "indoor" else "不规则",
            "approximate_size": "5m x 6m" if scene_type == "indoor" else "广阔",
            "entrances": ["正门"],
            "windows": ["窗户"] if scene_type == "indoor" else []
        }

        # 默认光源
        lighting_sources = [
            {
                "type": "natural",
                "source": "窗户" if scene_type == "indoor" else "太阳",
                "daytime_effect": "自然光",
                "description": "自然照明"
            }
        ]
        if scene_type == "indoor":
            lighting_sources.append({
                "type": "artificial",
                "source": "油灯/蜡烛",
                "description": "人工照明"
            })

        # 生成Prompt模板
        prompt_template = self._generate_prompt_template(name, scene_type, era, category)

        return SceneDesign(
            location_id=location_id,
            name=name,
            type=scene_type,
            category=category,
            era={"period": era, "dynasty": "fictional", "description": "架空古代"},
            architectural_style=architectural_style,
            layout=layout,
            key_elements=key_elements,
            lighting_sources=lighting_sources,
            time_variations=self.DEFAULT_TIME_VARIATIONS.copy(),
            weather_variations=self.DEFAULT_WEATHER_VARIATIONS.copy(),
            color_palette={"primary": "#8B4513", "secondary": "#DEB887"},
            atmosphere_presets=self.DEFAULT_ATMOSPHERE_PRESETS.copy(),
            prompt_template=prompt_template
        )

    def _get_default_indoor_elements(self, category: str) -> List[KeyElement]:
        """获取室内默认元素"""
        elements = {
            "residence": [
                KeyElement("书桌", "furniture", "木质书桌", "房间中央", "1.5m x 0.8m"),
                KeyElement("椅子", "furniture", "木椅", "书桌旁"),
                KeyElement("书架", "furniture", "木质书架", "墙边"),
                KeyElement("窗棂", "architectural", "雕花木窗", "墙面")
            ],
            "palace": [
                KeyElement("宝座", "furniture", "金碧辉煌的宝座", "大殿中央"),
                KeyElement("柱子", "architectural", "雕龙画凤的立柱", "两侧排列"),
                KeyElement("屏风", "decoration", "山水画屏风", "宝座后")
            ],
            "commercial": [
                KeyElement("柜台", "furniture", "木质柜台", "店铺前方"),
                KeyElement("货架", "furniture", "商品陈列架", "墙边")
            ]
        }
        return elements.get(category, elements["residence"])

    def _get_default_outdoor_elements(self, category: str) -> List[KeyElement]:
        """获取室外默认元素"""
        elements = {
            "courtyard": [
                KeyElement("假山", "decoration", "太湖石假山", "庭院一角"),
                KeyElement("池塘", "architectural", "锦鲤池", "庭院中央"),
                KeyElement("回廊", "architectural", "木质回廊", "庭院四周")
            ],
            "street": [
                KeyElement("店铺", "architectural", "各色商铺", "街道两侧"),
                KeyElement("牌坊", "architectural", "石牌坊", "街道入口")
            ],
            "nature": [
                KeyElement("树木", "decoration", "古树参天", "各处"),
                KeyElement("溪流", "architectural", "清澈溪水", "流经")
            ]
        }
        return elements.get(category, [])

    def _get_indoor_architectural_style(self, era: str) -> Dict[str, str]:
        """获取室内建筑风格"""
        return {
            "overall": "传统中式风格",
            "roof": "木质梁架",
            "walls": "格扇门，纸窗",
            "floor": "青砖或木地板"
        }

    def _get_outdoor_architectural_style(self, era: str) -> Dict[str, str]:
        """获取室外建筑风格"""
        return {
            "overall": "传统中式园林风格",
            "structures": "亭台楼阁",
            "landscape": "山水相映",
            "vegetation": "四季花木"
        }

    def _generate_prompt_template(
        self,
        name: str,
        scene_type: str,
        era: str,
        category: str
    ) -> Dict[str, str]:
        """生成场景Prompt模板"""
        type_desc = "interior" if scene_type == "indoor" else "exterior"
        era_desc = "ancient Chinese" if era == "ancient_chinese" else ""

        base = f"{era_desc} {name} {type_desc}"

        return {
            "base": base,
            "with_time": f"{{base}}, {{time_of_day}} lighting",
            "with_weather": f"{{base}}, {{weather}} weather",
            "full": f"{era_desc} {name} {type_desc}, {{key_elements}}, {{time_of_day}}, {{weather}}, {{atmosphere}} atmosphere, anime style, highly detailed, cinematic"
        }

    def generate_image_prompt(
        self,
        scene: SceneDesign,
        time_of_day: str = "day",
        weather: str = "clear",
        atmosphere: str = "calm",
        additional_tags: List[str] = None
    ) -> str:
        """生成场景图像Prompt"""
        builder = PromptBuilder()

        # 基础信息
        builder.add(f"{scene.era.get('period', 'ancient Chinese').replace('_', ' ')}")
        builder.add(scene.name)
        builder.add("interior" if scene.type == "indoor" else "exterior")

        # 关键元素
        if scene.key_elements:
            elements_desc = ", ".join([e.description for e in scene.key_elements[:3]])
            builder.add(elements_desc)

        # 时间段
        time_var = scene.time_variations.get(time_of_day)
        if time_var:
            builder.add(f"{time_of_day} lighting")
            builder.add(time_var.atmosphere)

        # 天气
        weather_var = scene.weather_variations.get(weather)
        if weather_var and weather != "clear":
            builder.add(f"{weather_var.get('description', '')} weather")

        # 氛围
        atm_preset = scene.atmosphere_presets.get(atmosphere)
        if atm_preset:
            builder.add(f"{atm_preset.get('mood', '')} atmosphere")

        # 风格和质量
        builder.add("anime style")
        builder.add("highly detailed")
        builder.add("cinematic composition")
        builder.add("8k resolution")

        # 附加标签
        if additional_tags:
            builder.add_list(additional_tags)

        return builder.build()

    def add_element(
        self,
        scene: SceneDesign,
        name: str,
        element_type: str,
        description: str,
        position: str,
        size: str = ""
    ):
        """添加场景元素"""
        element = KeyElement(name, element_type, description, position, size)
        scene.key_elements.append(element)

    def save_scene(self, scene: SceneDesign) -> Path:
        """保存场景设计"""
        # 确定保存目录
        scene_type_dir = "indoor" if scene.type == "indoor" else "outdoor"
        scene_dir = self.path_config.scenes_dir / scene_type_dir / scene.name
        scene_dir.mkdir(parents=True, exist_ok=True)

        output_path = scene_dir / "design.json"
        save_json(scene.to_dict(), output_path)
        return output_path

    def load_scene(self, name: str, scene_type: str = None) -> Optional[SceneDesign]:
        """加载场景设计"""
        # 尝试在两个目录中查找
        search_dirs = []
        if scene_type:
            search_dirs.append(self.path_config.scenes_dir / scene_type / name)
        else:
            search_dirs.append(self.path_config.scenes_dir / "indoor" / name)
            search_dirs.append(self.path_config.scenes_dir / "outdoor" / name)

        for scene_dir in search_dirs:
            scene_file = scene_dir / "design.json"
            if scene_file.exists():
                return self._load_from_file(scene_file)

        return None

    def _load_from_file(self, filepath: Path) -> SceneDesign:
        """从文件加载场景"""
        data = load_json(filepath)

        key_elements = [KeyElement(**e) for e in data.get("key_elements", [])]
        time_variations = {
            k: TimeVariation(**v) for k, v in data.get("time_variations", {}).items()
        }

        return SceneDesign(
            location_id=data.get("location_id", ""),
            name=data.get("name", ""),
            type=data.get("type", "indoor"),
            category=data.get("category", "residence"),
            era=data.get("era", {}),
            architectural_style=data.get("architectural_style", {}),
            layout=data.get("layout", {}),
            key_elements=key_elements,
            lighting_sources=data.get("lighting_sources", []),
            time_variations=time_variations,
            weather_variations=data.get("weather_variations", {}),
            color_palette=data.get("color_palette", {}),
            atmosphere_presets=data.get("atmosphere_presets", {}),
            prompt_template=data.get("prompt_template", {})
        )


def main():
    parser = argparse.ArgumentParser(description="场景设计师")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--scene", required=True, help="场景名称")
    parser.add_argument("--create", action="store_true", help="创建新场景")
    parser.add_argument("--type", choices=["indoor", "outdoor"], default="indoor", help="场景类型")
    parser.add_argument("--category", default="residence", help="场景类别")
    parser.add_argument("--era", default="ancient_chinese", help="时代风格")
    parser.add_argument("--prompt", action="store_true", help="生成Prompt")
    parser.add_argument("--time", default="day", help="时间段")
    parser.add_argument("--weather", default="clear", help="天气")
    parser.add_argument("--atmosphere", default="calm", help="氛围")

    args = parser.parse_args()

    designer = SceneDesigner(args.project)

    if args.create:
        scene = designer.create_scene(
            name=args.scene,
            scene_type=args.type,
            category=args.category,
            era=args.era
        )
        output_path = designer.save_scene(scene)
        print(f"场景创建完成: {output_path}")
        print(f"场景ID: {scene.location_id}")
        print(f"关键元素数: {len(scene.key_elements)}")

    elif args.prompt:
        scene = designer.load_scene(args.scene, args.type)
        if scene:
            prompt = designer.generate_image_prompt(
                scene,
                time_of_day=args.time,
                weather=args.weather,
                atmosphere=args.atmosphere
            )
            print(f"生成的Prompt:")
            print(prompt)
        else:
            print(f"场景不存在: {args.scene}")

    else:
        scene = designer.load_scene(args.scene, args.type)
        if scene:
            print(f"场景: {scene.name}")
            print(f"ID: {scene.location_id}")
            print(f"类型: {scene.type}")
            print(f"关键元素: {len(scene.key_elements)}")
        else:
            print(f"场景不存在: {args.scene}")


if __name__ == "__main__":
    main()
