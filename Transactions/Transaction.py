import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Backend.Account import Account
from abc import ABC, abstractmethod
from datetime import date
class Transaction(ABC):
    def __init__(self, value: float) -> None:
        self._value = value
        self.date = str(date.today().timetuple()[0:3]).replace('(', '').replace(')', '').replace(',', '/').replace(' ', '')

    @property
    def value(self):
        return self._value or 0
    
    @abstractmethod
    def RegistryTransaction(self, account: Account):
        pass
