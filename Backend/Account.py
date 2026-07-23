from __future__ import annotations
import sys
from pathlib import Path
from typing import TYPE_CHECKING
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if TYPE_CHECKING:
    from Client.Client import Client

class Account:
    def __init__(self) -> None:
        from random import randint
        from Transactions.extract import Extract
        self._currency = 0
        self._Id = randint(10000, 99999)
        self._agency = ''
        self._extract = Extract()
        self._client = None

    @property
    def currency(self):
        return self._currency or 0
    @property
    def Id(self):
        return self._Id or 0
    @property
    def agency(self):
        return self._currency or 0
    @property
    def extract(self):
        return self._extract.TransactionHistory or None
    
    def AddClient(self, client: Client):
        if self._client is None:
            self._client = client
            return True
        return False
    
    def draw(self, valor: float):
        if valor <= self._currency * 0.3:
            self._currency -= valor
            return True
        return False
    
    def deposit(self, valor: float):
        if valor > 0:
            self._currency += valor
            return True
        return False

if __name__ == '__main__':
    a = Account()
    print(a.Id)
