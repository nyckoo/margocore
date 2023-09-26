from abc import ABC, abstractmethod


class ProfessionManagerPattern(ABC):
    def __init__(self, lvl: int, eq_stats: dict[str, int], leg_bonuses_count: dict[str, int]):
        self.lvl = lvl
        self.eq_stats = eq_stats
        self.leg_bonuses_count = leg_bonuses_count

    @property
    @abstractmethod
    def base_stats(self) -> dict[str, int]:
        raise NotImplementedError("Base stats field has to be defined!")

    @property
    @abstractmethod
    def profession(self) -> str:
        raise NotImplementedError("Profession field has to be defined!")

    @property
    @abstractmethod
    def battle_stats(self) -> dict[str, int]:
        raise NotImplementedError("Battle stats field has to be defined!")

    @property
    @abstractmethod
    def full_features(self) -> dict[str, int]:
        raise NotImplementedError("Full features field has to be defined!")

    @abstractmethod
    def _load_base_features(self) -> None:
        raise NotImplementedError("Base features have to be included!")
