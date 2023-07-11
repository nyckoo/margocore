from dataclasses import dataclass
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class BladeDancerTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('swift_strike', 'poisonous_thrust', 'penetrating_wound', 'triple_strike', 'better_condition', 'physical_fitness'),
        35: ('sneaky_strike', 'feisty_blow', 'suppression', 'mobility', 'inborn_dodge', 'critical_hit'),
        50: ('dispersion_blow', 'venomous_blast', 'swirling_blade', 'toxic_fumes', 'blood_call', 'inborn_speed'),
        80: ('critical_acceleration', 'insidious_cut', 'critical_cut', 'swords_mastery', 'adrenalin', 'survival'),
        120: ('fury', 'dressing_wounds', 'rage', 'painful_blow', 'persistence', 'firm_armor'),
        170: ('riposte', 'precise_hit', 'deadly_blow', 'black_blood', 'callousness', 'power_durability'),
        230: ('amok', 'jagged_blade', 'might_source', 'armouring', 'great_health', 'fear')
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_set: dict[str, int]
