#!/usr/bin/env python3
"""
Character Designer - 角色设计师

设计角色的服化造（服装、化妆、造型）。
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
class Costume:
    """服装"""
    costume_id: str
    name: str
    usage: str
    era: str
    season: str
    garments: Dict[str, Any]
    accessories: List[Dict[str, str]]
    color_palette: Dict[str, str]
    prompt_description: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CharacterDesign:
    """角色设计"""
    character_id: str
    name: str
    role: str
    description: str
    base_profile: Dict[str, Any]
    face: Dict[str, Any]
    hair: Dict[str, Any]
    distinctive_features: List[str]
    costumes: List[Costume]
    expressions: Dict[str, Dict[str, str]]
    poses: Dict[str, str]
    personality_traits: Dict[str, Any]
    prompt_template: Dict[str, str]

    def to_dict(self) -> dict:
        return {
            "character_id": self.character_id,
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "base_profile": self.base_profile,
            "face": self.face,
            "hair": self.hair,
            "distinctive_features": self.distinctive_features,
            "costumes": [c.to_dict() for c in self.costumes],
            "expressions": self.expressions,
            "poses": self.poses,
            "personality_traits": self.personality_traits,
            "prompt_template": self.prompt_template
        }


class CharacterDesigner:
    """角色设计师"""

    # 默认面部特征模板
    DEFAULT_FACE = {
        "shape": "oval",
        "skin_tone": "fair",
        "eyebrows": {"shape": "willow_leaf", "color": "black", "description": "柳叶眉"},
        "eyes": {"shape": "almond", "color": "dark_brown", "size": "medium"},
        "nose": {"shape": "small_straight", "description": "小巧挺拔"},
        "lips": {"shape": "cherry", "color_natural": "pale_pink", "description": "樱桃小口"}
    }

    # 默认发型模板
    DEFAULT_HAIR = {
        "length": "waist_length",
        "color": "jet_black",
        "texture": "straight_silky",
        "natural_style": "长发及腰，乌黑如墨"
    }

    # 默认表情模板
    DEFAULT_EXPRESSIONS = {
        "neutral": {"description": "平静自然", "prompt_tags": "neutral expression, calm face"},
        "happy": {"description": "眉眼弯弯，嘴角上扬", "prompt_tags": "happy expression, smiling"},
        "sad": {"description": "眼眶微红，泪光闪烁", "prompt_tags": "sad expression, teary eyes"},
        "angry": {"description": "眉头紧蹙，眼神凌厉", "prompt_tags": "angry expression, furrowed brows"},
        "surprised": {"description": "双眼圆睁，微微张嘴", "prompt_tags": "surprised expression, wide eyes"},
        "contemplative": {"description": "目光深远，若有所思", "prompt_tags": "contemplative expression, thoughtful"},
        "determined": {"description": "目光坚定，下颚微抬", "prompt_tags": "determined expression, resolute"},
        "shy": {"description": "脸颊微红，目光低垂", "prompt_tags": "shy expression, blushing"}
    }

    # 默认姿态模板
    DEFAULT_POSES = {
        "standing": "直立，双手自然下垂",
        "sitting": "端坐，背挺直",
        "walking": "缓步行走，姿态优雅",
        "kneeling": "跪坐，姿态端正"
    }

    def __init__(self, project_name: str):
        self.project_config, self.path_config = load_project_config(project_name)
        self.path_config.ensure_dirs()

    def create_character(
        self,
        name: str,
        role: str = "supporting",
        description: str = "",
        gender: str = "female",
        age: int = 18,
        body_type: str = "slender",
        height: str = "165cm"
    ) -> CharacterDesign:
        """创建角色设计"""
        character_id = f"char_{hash(name) % 1000:03d}"

        # 构建基础档案
        base_profile = {
            "gender": gender,
            "age_appearance": age,
            "height": height,
            "body_type": body_type
        }

        # 构建面部特征
        face = self.DEFAULT_FACE.copy()
        if "圆脸" in description:
            face["shape"] = "round"
        elif "瓜子脸" in description:
            face["shape"] = "heart_shaped"

        # 构建发型
        hair = self.DEFAULT_HAIR.copy()
        if "短发" in description:
            hair["length"] = "shoulder_length"
        if "长发" in description:
            hair["length"] = "waist_length"

        # 创建默认服装
        costumes = [self._create_default_costume(name, gender)]

        # 生成Prompt模板
        prompt_template = self._generate_prompt_template(
            name, base_profile, face, hair, costumes[0]
        )

        return CharacterDesign(
            character_id=character_id,
            name=name,
            role=role,
            description=description,
            base_profile=base_profile,
            face=face,
            hair=hair,
            distinctive_features=[],
            costumes=costumes,
            expressions=self.DEFAULT_EXPRESSIONS.copy(),
            poses=self.DEFAULT_POSES.copy(),
            personality_traits={"primary": [], "secondary": []},
            prompt_template=prompt_template
        )

    def _create_default_costume(self, name: str, gender: str) -> Costume:
        """创建默认服装"""
        if gender == "female":
            return Costume(
                costume_id="costume_001",
                name="日常居家服",
                usage="日常场景",
                era="ancient_chinese",
                season="spring_autumn",
                garments={
                    "outer": {"type": "ruqun", "description": "淡色襦裙", "fabric": "丝绸"},
                    "inner": {"type": "neiyi", "description": "白色内衬", "fabric": "棉质"},
                    "accessory": {"type": "pibo", "description": "披帛", "wear": "搭于双肩"}
                },
                accessories=[
                    {"type": "hairpin", "name": "玉簪", "color": "白玉色"}
                ],
                color_palette={"primary": "#E8F5E9", "secondary": "#FAFAFA"},
                prompt_description="ancient Chinese ruqun dress, elegant and simple"
            )
        else:
            return Costume(
                costume_id="costume_001",
                name="日常长袍",
                usage="日常场景",
                era="ancient_chinese",
                season="spring_autumn",
                garments={
                    "outer": {"type": "pao", "description": "素色长袍", "fabric": "棉麻"},
                    "inner": {"type": "zhongyi", "description": "中衣", "fabric": "棉质"}
                },
                accessories=[
                    {"type": "belt", "name": "腰带", "color": "深色"}
                ],
                color_palette={"primary": "#ECEFF1", "secondary": "#455A64"},
                prompt_description="ancient Chinese robe, scholarly and elegant"
            )

    def _generate_prompt_template(
        self,
        name: str,
        base_profile: Dict,
        face: Dict,
        hair: Dict,
        default_costume: Costume
    ) -> Dict[str, str]:
        """生成Prompt模板"""
        gender = "young woman" if base_profile.get("gender") == "female" else "young man"
        age = base_profile.get("age_appearance", 18)

        base_prompt = PromptBuilder() \
            .add(f"{gender}, {age} years old") \
            .add(base_profile.get("body_type", "slender")) \
            .add(face.get("skin_tone", "fair skin")) \
            .add(f"{face.get('shape', 'oval')} face") \
            .add(f"{face.get('eyes', {}).get('shape', 'almond')} eyes") \
            .add(f"{hair.get('length', 'long')} {hair.get('color', 'black')} hair") \
            .build()

        return {
            "base": f"{base_prompt}, anime style",
            "with_costume": f"{{base}}, {default_costume.prompt_description}",
            "full": f"{{base}}, {{costume_prompt}}, {{expression_prompt}}, anime style, highly detailed, 8k"
        }

    def add_costume(
        self,
        character: CharacterDesign,
        name: str,
        usage: str,
        era: str = "ancient_chinese",
        season: str = "all",
        outer_garment: str = "",
        accessories: List[Dict] = None,
        colors: Dict[str, str] = None
    ) -> Costume:
        """为角色添加服装变体"""
        costume_id = f"costume_{len(character.costumes) + 1:03d}"

        costume = Costume(
            costume_id=costume_id,
            name=name,
            usage=usage,
            era=era,
            season=season,
            garments={"outer": {"type": "custom", "description": outer_garment}},
            accessories=accessories or [],
            color_palette=colors or {"primary": "#CCCCCC"},
            prompt_description=f"ancient Chinese {name.lower()}, {outer_garment}"
        )

        character.costumes.append(costume)
        return costume

    def update_expression(
        self,
        character: CharacterDesign,
        expression_type: str,
        description: str,
        prompt_tags: str
    ):
        """更新表情描述"""
        character.expressions[expression_type] = {
            "description": description,
            "prompt_tags": prompt_tags
        }

    def generate_image_prompt(
        self,
        character: CharacterDesign,
        costume_id: str = None,
        expression: str = "neutral",
        pose: str = "standing",
        additional_tags: List[str] = None
    ) -> str:
        """生成角色图像Prompt"""
        # 获取服装
        costume = None
        if costume_id:
            for c in character.costumes:
                if c.costume_id == costume_id:
                    costume = c
                    break
        if not costume:
            costume = character.costumes[0] if character.costumes else None

        # 获取表情
        expr_data = character.expressions.get(expression, self.DEFAULT_EXPRESSIONS["neutral"])

        # 构建Prompt
        builder = PromptBuilder()

        # 基础信息
        builder.add(f"{character.base_profile.get('gender', 'female')}")
        builder.add(f"{character.base_profile.get('age_appearance', 18)} years old")
        builder.add(character.base_profile.get("body_type", "slender"))

        # 面部
        builder.add(f"{character.face.get('skin_tone', 'fair')} skin")
        builder.add(f"{character.face.get('shape', 'oval')} face")

        # 眼睛
        eyes = character.face.get("eyes", {})
        builder.add(f"{eyes.get('shape', 'almond')} {eyes.get('color', 'brown')} eyes")

        # 发型
        builder.add(f"{character.hair.get('length', 'long')} {character.hair.get('color', 'black')} hair")

        # 服装
        if costume:
            builder.add(costume.prompt_description)

        # 表情
        builder.add(expr_data.get("prompt_tags", ""))

        # 风格和质量
        builder.add("anime style")
        builder.add("ancient Chinese" if self.project_config.era_style == "ancient_chinese" else "")
        builder.add("highly detailed")
        builder.add("8k resolution")
        builder.add("masterpiece")

        # 附加标签
        if additional_tags:
            builder.add_list(additional_tags)

        return builder.build()

    def save_character(self, character: CharacterDesign) -> Path:
        """保存角色设计"""
        char_dir = self.path_config.character_dir(character.name)
        char_dir.mkdir(parents=True, exist_ok=True)

        output_path = char_dir / "design.json"
        save_json(character.to_dict(), output_path)
        return output_path

    def load_character(self, name: str) -> Optional[CharacterDesign]:
        """加载角色设计"""
        char_file = self.path_config.character_dir(name) / "design.json"
        if not char_file.exists():
            return None

        data = load_json(char_file)
        costumes = [Costume(**c) for c in data.get("costumes", [])]

        return CharacterDesign(
            character_id=data.get("character_id", ""),
            name=data.get("name", name),
            role=data.get("role", "supporting"),
            description=data.get("description", ""),
            base_profile=data.get("base_profile", {}),
            face=data.get("face", {}),
            hair=data.get("hair", {}),
            distinctive_features=data.get("distinctive_features", []),
            costumes=costumes,
            expressions=data.get("expressions", {}),
            poses=data.get("poses", {}),
            personality_traits=data.get("personality_traits", {}),
            prompt_template=data.get("prompt_template", {})
        )


def main():
    parser = argparse.ArgumentParser(description="角色设计师")
    parser.add_argument("--project", required=True, help="项目名称")
    parser.add_argument("--character", required=True, help="角色名称")
    parser.add_argument("--create", action="store_true", help="创建新角色")
    parser.add_argument("--role", default="supporting", help="角色类型")
    parser.add_argument("--description", default="", help="角色描述")
    parser.add_argument("--gender", default="female", help="性别")
    parser.add_argument("--age", type=int, default=18, help="年龄")
    parser.add_argument("--prompt", action="store_true", help="生成Prompt")
    parser.add_argument("--expression", default="neutral", help="表情")
    parser.add_argument("--costume", default="", help="服装ID")

    args = parser.parse_args()

    designer = CharacterDesigner(args.project)

    if args.create:
        character = designer.create_character(
            name=args.character,
            role=args.role,
            description=args.description,
            gender=args.gender,
            age=args.age
        )
        output_path = designer.save_character(character)
        print(f"角色创建完成: {output_path}")
        print(f"角色ID: {character.character_id}")
        print(f"默认服装: {character.costumes[0].name}")

    elif args.prompt:
        character = designer.load_character(args.character)
        if character:
            prompt = designer.generate_image_prompt(
                character,
                costume_id=args.costume if args.costume else None,
                expression=args.expression
            )
            print(f"生成的Prompt:")
            print(prompt)
        else:
            print(f"角色不存在: {args.character}")

    else:
        character = designer.load_character(args.character)
        if character:
            print(f"角色: {character.name}")
            print(f"ID: {character.character_id}")
            print(f"类型: {character.role}")
            print(f"服装数: {len(character.costumes)}")
        else:
            print(f"角色不存在: {args.character}")


if __name__ == "__main__":
    main()
