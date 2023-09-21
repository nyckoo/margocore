from game_logic.professions_formulas.profession_manager_pattern import ProfessionManagerPattern
from game_logic.professions_formulas.stats_creation_applier import StatsCreationApplier
from game_logic.professions_formulas.mage.mage_tree import MageTree


class MageManager(ProfessionManagerPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'mage'

    def __init__(self, lvl: int, eq_stats: dict[str, int], leg_bonuses_count: dict[str, int], abs_set: dict[str, int]):
        super().__init__(lvl, eq_stats, leg_bonuses_count)
        self.stats_creation_applier = StatsCreationApplier()
        self.abs_tree = MageTree(lvl, eq_stats, abs_set)

    def _load_base_features(self):
        self.base_stats['strength'] += 19
        self.base_stats['agility'] += 19
        self.base_stats['intellect'] += 57
        self.base_stats['intellect'] += (self.lvl - 20) * 5

    def get_tree_abilities(self):
        pass
