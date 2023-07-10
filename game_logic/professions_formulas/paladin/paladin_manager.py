from game_logic.professions_formulas.profession_manager_pattern import ProfessionPattern
from game_logic.structures.eq_builder import Eq


class PaladinManager(ProfessionPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'paladin'

    def __init__(self, lvl: int, eq: Eq):
        super().__init__(lvl, eq)

    def get_base_features(self):
        # small tweak from standard approach because of half values
        self.base_stats['strength'] += 2
        self.base_stats['agility'] += 1
        self.base_stats['intellect'] += 2
        # step 2 to avoid floats
        for _ in range(3, 21, 2):
            self.base_stats['strength'] += 5
            self.base_stats['agility'] += 1
            self.base_stats['intellect'] += 4
        for i in range(21, self.lvl + 1):
            if i % 2 == 0:
                self.base_stats['strength'] += 2
                self.base_stats['intellect'] += 3
            else:
                self.base_stats['strength'] += 3
                self.base_stats['intellect'] += 2

    def get_tree_abilities(self):
        pass
