from dataclasses import dataclass


@dataclass
class DefChanceable:
    glare: str
    cleanse: str
    resgain: str
    dodge: str
    block: str
    pierce_block: str
    contra: str


@dataclass
class DefApplicable:
    lastheal: str  # +-10%, activated when max_hp < 18%
    poison_resist: str
    fire_resist: str
    light_resist: str
    frost_resist: str
    armor: str
    physical_absorb: str
    magical_absorb: str


@dataclass
class DefReducable:
    dmgred: str
    critred: str
    energy_subtra: str
    mana_subtra: str
    armor_reduction_protection: str
    hp_regen_reduction: str


@dataclass
class DefChangeable:
    attack_speed: str
    energy: str
    mana: str
    health_points: str
    hp_regen: str


@dataclass(frozen=True)
class Defense:
    glare: str
    cleanse: str
    resgain: str
    dodge: str
    block: str
    pierce_block: str
    contra: str
    lastheal: str
    poison_resist: str
    fire_resist: str
    light_resist: str
    frost_resist: str
    armor: str
    physical_absorb: str
    magical_absorb: str
    dmgred: str
    critred: str
    energy_subtra: str
    mana_subtra: str
    armor_reduction_protection: str
    energy: str
    mana: str
    health_points: str
    hp_regen: str
    attack_speed: int
