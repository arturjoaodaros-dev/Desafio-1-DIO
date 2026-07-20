from Backend.Account import Account
from abc import ABC, abstractmethod
from datetime import date
class Transaction(ABC):
    def __init__(self, value: float, date=str(date.today().timetuple()[0:3]).replace('(', '').replace(')', '').replace(',', '/').replace(' ', '')) -> None:
        self.value = value
        self.date = date
    @abstractmethod
    def RegistryTransaction(self, account: Account):
        pass