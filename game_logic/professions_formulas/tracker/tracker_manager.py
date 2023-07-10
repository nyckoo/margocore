from game_logic.structures.eq_builder import Eq
from game_logic.professions_formulas.profession_manager_pattern import ProfessionPattern
from game_logic.professions_formulas.stats_creation_applier import StatsCreationApplier
from game_logic.professions_formulas.tracker.tracker_tree import TrackerTree


class TrackerManager(ProfessionPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'tracker'

    def __init__(self, lvl: int, eq: Eq, abs_set: dict[str, int]):
        super().__init__(lvl, eq)
        self.stats_creation_applier = StatsCreationApplier()
        self.abs_tree = TrackerTree(lvl, eq, abs_set)

    def get_base_features(self):
        for _ in range(2, 21):
            self.base_stats['strength'] += 1
            self.base_stats['agility'] += 2
            self.base_stats['intellect'] += 2
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
