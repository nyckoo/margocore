from game_logic.professions_formulas.profession_manager_pattern import ProfessionPattern
from game_logic.structures.eq_builder import Eq


class BladeDancerManager(ProfessionPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'blade_dancer'

    def __init__(self, lvl: int, eq: Eq):
        super().__init__(lvl, eq)

    def get_base_features(self):
        for _ in range(2, 21):
            self.base_stats['strength'] += 3
            self.base_stats['agility'] += 2
        for i in range(21, self.lvl + 1):
            if i % 2 == 0:
                self.base_stats['strength'] += 2
                self.base_stats['agility'] += 3
            else:
                self.base_stats['strength'] += 3
                self.base_stats['agility'] += 2

    def get_tree_abilities(self):
        pass
