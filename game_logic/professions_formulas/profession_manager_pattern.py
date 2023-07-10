from abc import ABC, abstractmethod


class ProfessionManagerPattern(ABC):
    def __init__(self, lvl: int, eq: dict[str, int]):
        self.lvl = lvl
        self.eq = eq

    @property
    @abstractmethod
    def base_stats(self) -> dict[str, int]:
        raise NotImplementedError("Base stats field has to be defined!")

    @property
    @abstractmethod
    def profession(self) -> str:
        raise NotImplementedError("Profession field has to be defined!")

    @abstractmethod
    def load_base_features(self) -> None:
        pass
