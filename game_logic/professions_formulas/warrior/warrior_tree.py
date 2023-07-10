from dataclasses import dataclass
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class WarriorTree(ProfessionAbsTreePattern):
    blueprint = {

    }

    lvl: int
    eq_stats: dict[str, int]
    abs_set: dict[str, int]
