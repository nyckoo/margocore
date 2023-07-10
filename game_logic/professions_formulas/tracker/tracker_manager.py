from game_logic.professions_formulas.profession_manager_pattern import ProfessionManagerPattern
from game_logic.professions_formulas.stats_creation_applier import StatsCreationApplier
from game_logic.professions_formulas.tracker.tracker_tree import TrackerTree


class TrackerManager(ProfessionManagerPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'tracker'

    def __init__(self, lvl: int, eq_stats: dict[str, int], abs_set: dict[str, int]):
        super().__init__(lvl, eq_stats)
        self.stats_creation_applier = StatsCreationApplier()
        self.abs_tree = TrackerTree(lvl, eq_stats, abs_set)

    def load_base_features(self):
        # 1-20 lvl sum of features
        self.base_stats['strength'] += 19
        self.base_stats['agility'] += 38
        self.base_stats['intellect'] += 38
        for i in range(21, self.lvl + 1):
            if i % 2 == 0:
                self.base_stats['agility'] += 2
                self.base_stats['intellect'] += 3
            else:
                self.base_stats['agility'] += 3
                self.base_stats['intellect'] += 2

    def get_abs_tree_abilities(self):
        pass

    def upgrade_stats_by_abs_tree(self):
        pass
