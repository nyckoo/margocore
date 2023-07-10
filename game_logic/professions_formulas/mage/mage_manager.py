from game_logic.professions_formulas.profession_manager_pattern import ProfessionPattern
from game_logic.structures.eq_builder import Eq


class MageManager(ProfessionPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'mage'

    def __init__(self, lvl: int, eq: Eq):
        super().__init__(lvl, eq)

    def get_base_features(self):
        for _ in range(2, 21):
            self.base_stats['strength'] += 1
            self.base_stats['agility'] += 1
            self.base_stats['intellect'] += 3
        for _ in range(21, self.lvl + 1):
            self.base_stats['intellect'] += 5

    def get_tree_abilities(self):
        pass
