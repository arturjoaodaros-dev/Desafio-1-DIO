import sys
from pathlib import Path
from typing import TYPE_CHECKING
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from abc import ABC, abstractmethod
from datetime import date

if TYPE_CHECKING:
    from Backend.CurrentAccount import CurrentAccount

class Transaction(ABC):
    def __init__(self, value: float) -> None:
        self._value = value
        self.date = date.today()

    @property
    def value(self):
        return self._value or 0
    
    @abstractmethod
    def RegistryTransaction(self, account: "CurrentAccount"):
        pass
