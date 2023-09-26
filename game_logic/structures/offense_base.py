from dataclasses import dataclass


@dataclass
class AttackTypes:
    physical_dmg: str
    fire_dmg: str  # originally interval
    light_dmg: str  # originally interval
    frost_dmg: str
    poison_dmg: str
    wound_dmg: str
    physical_crit: str
    magical_crit: str


@dataclass
class OffChanceable:
    crit: str
    verycrit: str
    holytouch: str
    curse: str
    armor_pierce: str
    wound_chance: str


@dataclass
class OffReducable:
    frost_slow: str
    poison_slow: str
    as_reduction: str  # works once after first successful hit
    resist_reduction: str  # works when hit successful
    armor_reduction: str  # works when hit successful
    absorb_reduction: str  # works when hit successful
    mana_energy_subtra_protection: str


@dataclass
class OffChangeable:
    attack_speed: int


@dataclass(frozen=True)
class Offense:
    crit: str
    verycrit: str
    holytouch: str
    curse: str
    armor_pierce: str
    wound_chance: str
    physical_dmg: str
    fire_dmg: str
    light_dmg: str
    frost_dmg: str
    poison_dmg: str
    wound_dmg: str
    physical_crit: str
    magical_cri: str
    frost_slow: str
    poison_slow: str
    as_reduction: str
    resist_reduction: str
    armor_reduction: str
    absorb_reduction: str
    hp_regen_reduction: str
    hp_regen_reduction_2t: str
    mana_energy_subtra_protection: str
    attack_speed: int
