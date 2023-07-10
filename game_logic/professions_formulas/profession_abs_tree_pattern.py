from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ProfessionAbsTreePattern(ABC):
    @property
    @abstractmethod
    def blueprint(self) -> dict[int, tuple]:
        raise NotImplementedError("Blueprint field has to be defined!")

    @property
    @abstractmethod
    def lvl(self) -> int:
        raise NotImplementedError("Level field has to be defined!")

    @property
    @abstractmethod
    def eq_stats(self) -> dict[str, int]:
        raise NotImplementedError("Equipment stats field has to be defined!")

    @property
    @abstractmethod
    def abs_set(self) -> dict[str, int]:
        raise NotImplementedError("Abilities set field has to be defined!")

