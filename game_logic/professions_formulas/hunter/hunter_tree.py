from dataclasses import dataclass
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class HunterTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('swift_arrow', 'double_arrow', 'poisoned_arrow', 'ripping_arrow', 'vigor_enhancement', 'physical_fitness'),
        35: ('devastating_wounds', 'beast_seal', 'break_freeing', 'armor_pierce', 'natural_dodge', 'critical_hit'),
        50: ('arrows_hail', 'bandaging_wounds', 'toxic_shock', 'as_agility', 'arrow_retrieval', 'inborn_speed'),
        80: ('critical_buff', 'diamond_arrow', 'cleanse', 'critical_arrow', 'painful_hit', 'survival'),
        120: ('light_tension', 'dispersion_arrow', 'venom_arrow', 'poisonous_injury', 'core_resistance', 'firm_armor'),
        170: ('foot_shot', 'insidious_arrow', 'remedy', 'wolf_instinct', 'easy_target', 'power_durability'),
        230: ('wild_zeal', 'destructive_arrows', 'might_source', 'armouring', 'great_health', 'fear')
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_data: dict[str, int]

    # get loaded abs & return to features, battle stats
    def assign_to_stats_and_features(self):
        ...
