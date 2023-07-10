from game_logic.professions_formulas.profession_manager_pattern import ProfessionManagerPattern
from game_logic.professions_formulas.stats_creation_applier import StatsCreationApplier
from game_logic.professions_formulas.paladin.paladin_tree import PaladinTree


class PaladinManager(ProfessionManagerPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'paladin'

    def __init__(self, lvl: int, eq_stats: dict[str, int], abs_set: dict[str, int]):
        super().__init__(lvl, eq_stats)
        self.stats_creation_applier = StatsCreationApplier()
        self.abs_tree = PaladinTree(lvl, eq_stats, abs_set)

    def load_base_features(self):
        self.base_stats['strength'] += 47
        self.base_stats['agility'] += 10
        self.base_stats['intellect'] += 38
        for i in range(21, self.lvl + 1):
            if i % 2 == 0:
                self.base_stats['strength'] += 2
                self.base_stats['intellect'] += 3
            else:
                self.base_stats['strength'] += 3
                self.base_stats['intellect'] += 2

    def get_tree_abilities(self):
        pass
