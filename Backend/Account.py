from sys import path
from random import randint
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
path.insert(0, str(PROJECT_ROOT))
from ..Client.Client import Client

class Account:
    def __init__(self) -> None:
        self.currency = 0
        self.Id = 0
        self.agency = ''
        self.extract = []
        self.client = None
    
    def AddClient(self, client: Client, Id: float):
        if self.client is not None:
            self.client = client
            return True
        return False
    
    def sacar(self, valor: float):
        if valor <= self.currency * 0.3:
            self.currency -= valor
            return True
        return False
    
    def depositar(self, valor: float):
        if valor > 0:
            self.currency += valor
