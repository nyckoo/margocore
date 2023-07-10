from dataclasses import dataclass, field
from stats_utils import AllStats, LegendaryBonuses
from character_manager import Character


@dataclass
class FightSimulator:
    characters: list[Character]
    # first_team_size: int = 1
    _stats_types: list = field(init=False)
    _updated_battle_stats: list = field(init=False)

    def __post_init__(self):
        self._stats_types = field(default_factory=lambda: [self._build_stats_helper(char) for char in self.characters])
        self._updated_battle_stats = field(default_factory=lambda: [{} for _ in range(len(self.characters))])

    @staticmethod
    def _build_stats_helper(char: Character):
        char_leg_bons = {}
        for bon, power in char.bonuses.items():
            char_leg_bons[bon] = round(
                getattr(LegendaryBonuses, bon) * (1 - .5 ** power) / .5)
        return {**char_leg_bons, **char.get_full_stats()}

    # Stats update queue
    # Defensive -> Offensive -> Abilities
    # Collector getting updatibles through steps, passing to opponent
    def pvp_mode(self):
        # attack_params of characters by categories (pvp_offense_base) + (ta_stats to be added)
        chars_offensive_stats, chars_defensive_stats = [], []
        for i in range(len(self.characters)):
            chars_offensive_stats.append(
                {key: val for key, val in self._stats_types[i].items() if key in attack_params_tuple})
            chars_defensive_stats.append(
                {key: val for key, val in self._stats_types[i].items() if key in defence_params_tuple})
        updatibles = []
        final_stats = []

        # is_fight_on = True
        # while is_fight_on:

    # 'AllStats.main' is being used inside a method.
    def _prep_pvp_stats(self):
        assert len(self.characters) == 2
        for i in range(2):
            # Reducing stats by opponents debuffs and lvl leverage
            # Del strength_hp key (if needed)
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
            self._stats_types[i]['crit_strike'] = self._stats_types[i]['crit_strike'] - \
                enemy_debuff_stats.get('crit_reduction', 0) + lvl_factor * 3
            # Crit power
            if lvl_factor > 25:
                lvl_factor = 25
            elif lvl_factor < 0:
                lvl_factor = 0
            opp_debuff = enemy_debuff_stats.get('crit_power_reduction', 0)
            self._stats_types[i]['physical_crit'] = self._stats_types[i]['physical_crit'] - \
                opp_debuff + lvl_factor * 10
            self._stats_types[i]['magical_crit'] = self._stats_types[i]['magical_crit'] - \
                opp_debuff + lvl_factor * 10
            # Dodge
            self._stats_types[i]['dodge'] = round(
                20 * (self._stats_types[i]['dodge'] - enemy_debuff_stats.get('dodge_reduction', 0)) / enemy_lvl)
            # Block
            self._stats_types[i]['block'] = round(
                20 * self._stats_types[i].get('block', 0) / enemy_lvl)

    def __new_turn_update(self, updatibles: dict):
        # some loop updating parameters
        pass

    def __stats_turn_mechanics(self):
        pass
