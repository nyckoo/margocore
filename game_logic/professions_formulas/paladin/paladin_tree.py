from dataclasses import dataclass
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class PaladinTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('frost_push', 'fire_push', 'light_push', 'gods_wraith', 'justice_power', 'physical_fitness'),
        35: ('swift_blow', 'speed_aura', 'critical_hit', 'target_focus', 'bless_protection', 'parrying'),
        50: ('defiant_roar', 'mights_guardian', 'shield_hit', 'silver_shine', 'power_regain', 'innate_speed'),
        80: ('healing_wave', 'spirit_fortitude', 'survival', 'fire_power', 'light_power', 'frost_power'),
        120: ('critical_hit', 'penetrating_hit', 'distraction_blow', 'vitality', 'sun_shield', 'armor_buff'),
        170: ('protection_aura', 'power_durability', 'elemental_immunity', 'power_stability', 'base_resistance', 'magic_shield'),
        230: ('bright_ball', 'fear', 'great_health', 'extra_armor', 'might_source', 'life_aura')
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_data: dict[str, int]
