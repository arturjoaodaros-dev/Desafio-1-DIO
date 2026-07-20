from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Client.Client import Client
    from extract import Extract


class Account:
    def __init__(self) -> None:
        self.currency = 0
        self.Id = 0
        self.agency = ''
        self.extract = Extract()
        self.client = None
    
    def AddClient(self, client: "Client", Id: float):
        if self.client is None:
            self.client = client
            self.Id = Id
            return True
        return False
    
    def draw(self, valor: float):
        if valor <= self.currency * 0.3:
            self.currency -= valor
            return True
        return False
    
    def deposit(self, valor: float):
        if valor > 0:
            self.currency += valor
