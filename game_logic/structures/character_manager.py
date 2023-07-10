import secrets
from dataclasses import dataclass, field
from stats_utils import AllStats, LegendaryBonuses
from game_logic.professions_formulas.stats_builders import ProfessionBuilder
from game_logic.professions_formulas.stats_builders import get_all_params, get_base_features


@dataclass
class Character:
    unit: ProfessionBuilder
    idx: str = field(init=False)
    full_stats: dict = field(init=False)
    # ta_stats: dict = field(init=False)
    # ta_queue: list = field(init=False)

    def __post_init__(self):
        self.idx = ''.join([secrets.choice('0123456789')
                           for _ in range(4)])
        self.full_stats = self.get_full_stats()
        # self.counter_stats = self.get_counter_stats
        # self.ta_stats = field(default_factory=lambda: {})
        # self.ta_queue = field(default_factory=lambda: [])

    # Get full stats based on profession, lvl, eq (ta_stats to be added)
    def get_full_stats(self):
        # ToDo - upgrade using builder class
        temp_stats = self.eq_stats

        b_stats = get_base_features(self.lvl, self.profession)

        base_features = ('strength', 'agility', 'intellect')

        if 'all_features' in temp_stats:
            for i in base_features:
                if i in temp_stats:
                    temp_stats[i] += temp_stats['all_features']
                else:
                    temp_stats[i] = temp_stats['all_features']
                temp_stats[i] += b_stats[i]
            del temp_stats['all_features']
        else:
            for i in base_features:
                if i in temp_stats:
                    temp_stats[i] += b_stats[i]
                else:
                    temp_stats[i] = b_stats[i]
        return get_all_params(self.lvl, temp_stats)

    # Get this character counter stats (using stats_utils mapper)
    def get_counter_stats(self):
        this_char_stats = self.get_full_stats().items()
        this_char_counter_stats = {}
        for stat in AllStats.counter:
            this_char_counter_stats[stat] = this_char_stats.get(stat, 0)
        return this_char_counter_stats

    def _convert_legendary_bonuses(self):
        char_leg_bons = {}
        for bon, power in self.bonuses.items():
            char_leg_bons[bon] = round(
                getattr(LegendaryBonuses, bon) * (1 - .5 ** power) / .5)
        return char_leg_bons
