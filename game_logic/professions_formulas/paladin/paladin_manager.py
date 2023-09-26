from game_logic.professions_formulas.profession_manager_pattern import ProfessionManagerPattern
from game_logic.professions_formulas.stats_creation_applier import StatsCreationApplier
from game_logic.professions_formulas.paladin.paladin_tree import PaladinTree


class PaladinManager(ProfessionManagerPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'paladin'

    def __init__(self, lvl: int, eq_stats: dict[str, int], leg_bonuses_count: dict[str, int], abs_set: dict[str, int]):
        super().__init__(lvl, eq_stats, leg_bonuses_count)
        self.stats_creation_applier = StatsCreationApplier()
        self.abs_tree = PaladinTree(lvl, eq_stats, abs_set)

    def _load_base_features(self):
        self.base_stats['strength'] += 47
        self.base_stats['agility'] += 10
        self.base_stats['intellect'] += 38
        if self.lvl % 2 == 0:
            self.base_stats['strength'] += int((self.lvl-20) / 2) * 5
            self.base_stats['intellect'] += int((self.lvl-20) / 2) * 5
        else:
            self.base_stats['strength'] += int((self.lvl - 21) / 2) * 5 + 3
            self.base_stats['intellect'] += int((self.lvl - 21) / 2) * 5 + 2

    def get_tree_abilities(self):
        pass
