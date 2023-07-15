from game_logic.professions_formulas.profession_manager_pattern import ProfessionManagerPattern
from game_logic.professions_formulas.stats_creation_applier import StatsCreationApplier
from game_logic.professions_formulas.tracker.tracker_tree import TrackerTree


class TrackerManager(ProfessionManagerPattern):
    base_stats = {'strength': 4, 'agility': 3, 'intellect': 3}
    profession = 'tracker'
    battle_stats = None
    full_features = None

    def __init__(self, lvl: int, eq_stats: dict[str, int], abs_set: dict[str, int]):
        super().__init__(lvl, eq_stats)
        self.stats_creation_applier = StatsCreationApplier()
        self.tracker_tree = TrackerTree(lvl, eq_stats, abs_set)

    def get_upgraded_stats_and_features(self):
        self._load_base_features()
        emerging_features = self.stats_creation_applier.load_all_features(
            base_stats=self.base_stats,
            eq_stats=self.tracker_tree.eq_stats
        )
        self.full_features = self.stats_creation_applier.load_features_compounded_stats(
            summed_stats=emerging_features,
            lvl=self.tracker_tree.lvl
        )

        self.battle_stats = {}
        abs_data_distributor = self.tracker_tree.create_stats_and_features_generator()
        for _ in range(len(self.tracker_tree.abs_data)):
            # what if these values are of 'None' type?
            skill_name, stat_info, feature_info = next(abs_data_distributor)
            if stat_info:
                self.battle_stats[skill_name] = stat_info
            if feature_info:  # works only for one key:value pair
                feature_data = next(iter(feature_info))
                self.full_features[feature_data] += feature_info[feature_data]

    def _load_base_features(self):
        # 1-20 lvl sum of features
        self.base_stats['strength'] += 19
        self.base_stats['agility'] += 38
        self.base_stats['intellect'] += 38
        for i in range(21, self.lvl + 1):
            if i % 2 == 0:
                self.base_stats['agility'] += 2
                self.base_stats['intellect'] += 3
            else:
                self.base_stats['agility'] += 3
                self.base_stats['intellect'] += 2
