from abc import ABC, abstractmethod


class ProfessionManagerPattern(ABC):
    def __init__(self, lvl: int, eq: dict[str, int], leg_bonuses_count: dict[str, int]):
        self.lvl = lvl
        self.eq = eq
        self.leg_bonuses_count = leg_bonuses_count

    @property
    @abstractmethod
    def base_stats(self) -> dict[str, int]:
        raise NotImplementedError("Base stats field has to be defined!")

    @property
    @abstractmethod
    def profession(self) -> str:
        raise NotImplementedError("Profession field has to be defined!")

    @abstractmethod
    def _load_base_features(self) -> None:
        pass
