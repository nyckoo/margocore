from dataclasses import dataclass
# [Offensive, Defensive], [Static, Dynamic]


@dataclass(frozen=True)
class LegendaryBonuses:
    verycrit: int = 13
    critred: int = 20
    lastheal: int = 40  # +-10%, activated when max_hp < 18%
    holytouch: int = 7  # 0.06 max_hp x3
    curse: int = 9
    glare: int = 9
    cleanse: int = 12
    dmgred: int = 16
    resgain: int = 16


@dataclass(frozen=True)
class StaticOffStats:
    all_features: int
    strength: int
    agility: int
    intellect: int
    crit: int
    physical_crit: int
    magical_crit: int
    dodge_reduction: int  # works before hit
    hp_regen_reduction: int  # works after first successful hit
    mana_energy_subtra_protection: int


@dataclass(frozen=True)
class DynamicOffStats:
    as_reduction: int  # works once after first successful hit
    resist_reduction: int  # works when hit successful
    armor_reduction: int  # works when hit successful
    absorb_reduction: int  # works when hit successful
    attack_speed: int
    physical_dmg: (tuple, int)  # (lowest, highest) / constant
    fire_dmg: int  # originally boundaries
    light_dmg: int  # originally boundaries
    frost_dmg: tuple  # (slow, dmg)
    armor_pierce: int
    poison_dmg: tuple  # (slow, dmg)
    wound_dmg: tuple  # (chance, dmg)
    hp_regen_reduction_2t: int  # works after first successful hit for 2 turns


@dataclass(frozen=True)
class StaticDefStats:
    energy_subtra: int
    mana_subtra: int
    dodge: int
    crit_reduction: int  # works before hit
    crit_power_reduction: int  # works before hit
    armor_reduction_protection: int  # works when hit successful
    block: int
    pierce_block: int
    strength_hp: int  # added in eq upload (at func. get_all_params)
    contra: int


@dataclass(frozen=True)
class DynamicDefStats:
    energy: int
    mana: int
    health_points: int
    hp_regen: int
    poison_resist: int
    fire_resist: int
    light_resist: int
    frost_resist: int
    armor: int
    physical_absorb: int
    magical_absorb: int


# standardized for db save
@dataclass(frozen=True)
class AllStats(StaticOffStats, DynamicOffStats, StaticDefStats, DynamicDefStats):
    frost_slow: int
    poison_slow: int
    wound_chance: int
    legendary_bonus: str


# Character counter stats altering enemy stats
# Might be updated by ta_stats
@dataclass(frozen=True)
class CounterStats:
    dodge_reduction: int  # works before hit
    hp_regen_reduction: int
    as_reduction: int  # works once after first successful hit
    resist_reduction: int  # works when hit successful
    armor_reduction: int  # works when hit successful
    absorb_reduction: int  # works when hit successful
    hp_regen_reduction_2t: int  # works after first successful hit for 2 turns
    energy_subtra: int
    mana_subtra: int
    mana_energy_subtra_protection: int
    crit_reduction: int  # works before hit
    crit_power_reduction: int  # works before hit
