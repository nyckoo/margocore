from game_logic.professions_formulas.profession_manager_pattern import ProfessionPattern
from game_logic.structures.eq_builder import Eq


class WarriorManager(ProfessionPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'warrior'

    def __init__(self, lvl: int, eq: Eq):
        super().__init__(lvl, eq)

    def get_base_features(self):
        for _ in range(2, 21):
            self.base_stats['strength'] += 4
            self.base_stats['agility'] += 1
        for _ in range(21, self.lvl + 1):
            self.base_stats['strength'] += 5

    def get_tree_abilities(self):
        pass
