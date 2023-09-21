from dataclasses import dataclass, field, fields

from game_logic.structures.pvp_defense_base import Defense
from game_logic.structures.pvp_offense_base import Offense
from game_logic.professions_formulas.profession_manager_pattern import ProfessionManagerPattern


@dataclass
class BattleProcessorManager:
    characters: tuple[ProfessionManagerPattern]

    def __post_init__(self):
        self._turn_effects_store: dict = field(default_factory=lambda: {
            'one': {},
            'two': {}
        })
        if self.characters[0].full_features['attack_speed'] > self.characters[0].full_features['attack_speed']:
            one = self.characters[0], two = self.characters[1]
        else:
            one = self.characters[1], two = self.characters[0]
        self._chars_off_stats = {
            'one': dict(filter(lambda key: key.name in fields(Offense), one.full_features.items())),
            'two': dict(filter(lambda key: key.name in fields(Offense), two.full_features.items()))
        }
        self._chars_def_stats = {
            'one': dict(filter(lambda key: key.name in fields(Defense), one.full_features.items())),
            'two': dict(filter(lambda key: key.name in fields(Offense), two.full_features.items()))
        }

    # Stats update queue
    # Defensive -> Offensive -> Abilities
    # Collector getting updatibles through steps, passing to opponent
    def pvp_mode(self):
        updatibles = []
        final_stats = []

    def _prep_pvp_stats(self):
        for i in range(2):
            # Reducing stats by opponents debuffs and lvl leverage
            # Initialize counter stats for enemy
            enemy_debuff_stats = self.characters[abs(i - 1)].get_counter_stats()
            # Obtaining enemy lvl
            enemy_lvl = self.characters[abs(i - 1)].lvl
            lvl_factor = 0
            if lvl_factor := abs(self.characters[i].lvl - enemy_lvl) > 5:
                lvl_factor = self.characters[i].lvl - enemy_lvl
                if lvl_factor < 0:
                    lvl_factor += 5
                else:
                    lvl_factor -= 5
            # Crit
            self._characters_stats[i]['crit_strike'] = self._characters_stats[i]['crit_strike'] - \
                enemy_debuff_stats.get('crit_reduction', 0) + lvl_factor * 3
            # Crit power
            if lvl_factor > 25:
                lvl_factor = 25
            elif lvl_factor < 0:
                lvl_factor = 0
            opp_debuff = enemy_debuff_stats.get('crit_power_reduction', 0)
            self._characters_stats[i]['physical_crit'] = self._characters_stats[i]['physical_crit'] - \
                opp_debuff + lvl_factor * 10
            self._characters_stats[i]['magical_crit'] = self._characters_stats[i]['magical_crit'] - \
                opp_debuff + lvl_factor * 10
            # Dodge
            self._characters_stats[i]['dodge'] = round(
                20 * (self._characters_stats[i]['dodge'] - enemy_debuff_stats.get('dodge_reduction', 0)) / enemy_lvl)
            # Block
            self._characters_stats[i]['block'] = round(
                20 * self._characters_stats[i].get('block', 0) / enemy_lvl)

    def __new_turn_update(self, updatibles: dict):
        # some loop updating parameters
        pass

    def __stats_turn_mechanics(self):
        pass
