# Basic class structures for item, eq, player relation
import secrets
from dataclasses import dataclass, field
from player_base_params import *
from pvp_utils import *


@dataclass
class Item:
    lvl: int
    prof: str
    atype: str
    name: str
    stats: dict

    def __post_init__(self):
        self.stats = self.parse_types()

    def __repr__(self):
        return f'{self.lvl}/{self.prof}/{self.atype}/{self.name}'

    def to_list(self):
        return [self.lvl, self.prof, self.atype, self.name, self.stats]

    def parse_types(self):
        return parse_custom_type(self.stats)


@dataclass
class Eq:
    items: list = field(default_factory=lambda: [])
    stats: dict = field(default_factory=lambda: {})
    bonuses: dict = field(default_factory=lambda: {})
    name_legbon: dict = field(default_factory=lambda: {})

    def check(self, item: Item):
        # Check compatibility of profs with 1st item in eq
        zipped = set(zip(self.items[0].prof, item.prof))
        for el in zipped:
            if el[0] == el[1]:
                return True
        return False

    def add(self, item: Item):
        # Append new item to eq
        self.items.append(item)
        # Legbon adding
        try:
            new_bonus = str(item.stats['legendary_bonus'])
        except KeyError:
            return KeyError
        else:
            self.name_legbon[item.name] = new_bonus
            if new_bonus not in self.bonuses:
                self.bonuses[new_bonus] = 1
            else:
                self.bonuses[new_bonus] += 1
            del item.stats['legendary_bonus']
        # Stats adding
        finally:
            for key in item.stats:
                if key in self.stats:
                    self.stats[key] += item.stats[key]
                else:
                    self.stats[key] = item.stats[key]

        # Remove item under certain condition (the same name for now)
        # self.remove(item.name)
        # Check if new item type existed before and erase if so
        # <TO DO>

    def remove(self, name: str):
        for el in self.items:
            if el.name == name:
                self.items.remove(el)
                bon_to_del = self.name_legbon[el.name]
                self.bonuses[bon_to_del] -= 1
                if self.bonuses[bon_to_del] == 0:
                    del self.bonuses[bon_to_del]
                for key in el.stats:
                    if key in self.stats:
                        self.stats[key] -= el.stats[key]
                    if self.stats[key] == 0:
                        del self.stats[key]


@dataclass
class Character:
    lvl: int
    proffesion: str
    eq_stats: dict
    bonuses: dict
    idx: str = field(init=False)
    stats: dict = field(init=False)
    # ta_stats: dict = field(init=False)
    # ta_queue: list = field(init=False)

    def __post_init__(self):
        self.idx = ''.join([secrets.choice('0123456789')
                           for _ in range(4)])
        self.stats = self.get_stats
        self.counter_stats = self.get_counter_stats
        # self.ta_stats = field(default_factory=lambda: {})
        # self.ta_queue = field(default_factory=lambda: [])

    def __repr__(self):
        return f'{self.lvl}{self.proffesion}#{self.idx}'

    # Get full stats based on proffesion, lvl, eq (ta_stats to be added)
    def get_stats(self):
        temp_stats = self.eq_stats

        b_stats = get_base_features(self.lvl, self.proffesion)

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

    # Get this character counter stats (using pvp_utils mapper)
    def get_counter_stats(self):
        this_char_stats = self.get_stats().items()
        this_char_counter_stats = {}
        for stat in counter_stats:
            this_char_counter_stats[stat] = this_char_stats.get(stat, 0)
        return this_char_counter_stats


@dataclass
class FightSimulator:
    characters: list[Character]
    _stats_types: dict = field(init=False)
    _updated_battle_stats: dict = field(init=False)

    def __post_init__(self):
        self._stats_types = field(default_factory=lambda: ({}, {}))
        self._updated_battle_stats = field(default_factory=lambda: ({}, {}))

    # Stats update queue
    # Defensive -> Offensive -> Abilities
    # Collector getting updatibles through steps, passing to opponent
    def pvp_mode(op, dp):
        op_stats, dp_stats = op.stats, dp.stats
        updatibles = []
        final_stats = []

        # is_fight_on = True
        # while is_fight_on:

    # pvp_utils 'all_types_stats' is being used inside a method.
    def starting_stats(self):
        for i in range(len(self.characters)):
            # Initialize stats for this character and enemy counter stats
            this_char_stats = self.characters[i].stats()
            enemy_debuff_stats = self.characters[abs(i - 1)].counter_stats()
            # Assigning all character stats (for now eq only)
            for key in all_types_stats:
                if key in this_char_stats:
                    self._stats_types[i][key] = this_char_stats[key]
            # Get all legendary bonuses
            for bon, power in self.characters[i].bonuses:
                self._stats_types[i][bon] = round(
                    leg_bons[bon] * (1 - .5**(power)) / .5)
            # Del strength_hp key (if needed)
            # Reducing stats by opponents debuffs and lvl leverage, obtaining enemy lvl
            enemy_lvl = self.characters[abs(i - 1)].lvl
            lvl_factor = 0
            if lvl_factor := abs(self.characters[i].lvl - enemy_lvl) > 5:
                lvl_factor = self.characters[i].lvl - enemy_lvl
                if lvl_factor < 0:
                    lvl_factor += 5
                else:
                    lvl_factor -= 5
            # Crit
            self._stats_types[i]['crit_strike'] = this_char_stats['crit_strike'] - \
                enemy_debuff_stats.get('crit_reduction', 0) + lvl_factor * 3
            # Crit power
            if lvl_factor > 25:
                lvl_factor = 25
            elif lvl_factor < 0:
                lvl_factor = 0
            opp_debuff = enemy_debuff_stats.get('crit_power_reduction', 0)
            self._stats_types[i]['physical_crit'] = this_char_stats['physical_crit'] - \
                opp_debuff + lvl_factor * 10
            self._stats_types[i]['magical_crit'] = this_char_stats['magical_crit'] - \
                opp_debuff + lvl_factor * 10
            # Dodge
            self._stats_types[i]['dodge'] = round(
                20 * (this_char_stats['dodge'] - enemy_debuff_stats.get('dodge_reduction', 0)) / enemy_lvl)
            # Block
            self._stats_types[i]['block'] = round(
                20 * this_char_stats.get('block', 0) / enemy_lvl)

    def new_turn_update(self, updatibles: dict):
        # some loop updating parameters
        pass

    def stats_turn_mechanics():
        pass
