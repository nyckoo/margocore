from dataclasses import dataclass
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class WarriorTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('destructive_hit', 'accurate_hit', 'mayhem', 'swift_blow', 'energy_enhancement', 'physical_fitness'),
        35: ('stunning_hit', 'hard_head', 'unbalancing_hit', 'devastation', 'critical_hit', 'defiant_roar'),
        50: ('bloodthirsty_fury', 'aggressive_attack', 'blood_call', 'shield_cover', 'mighty_protection', 'innate_speed'),
        80: ('contra', 'endurance', 'survival', 'charge', 'adaptation', 'powerful_blow'),
        120: ('hit_reflection', 'berserk', 'stone_skin', 'exhaustion_overcome', 'critical_slowness', 'armor_buff'),
        170: ('bloody_shambles', 'heavy_wound', 'last_blow', 'vampirism', 'paralyzing_blow', 'power_durability'),
        230: ('crushing', 'fear', 'great_health', 'extra_armor', 'might_source', 'combat_roar')
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_data: dict[str, int]
