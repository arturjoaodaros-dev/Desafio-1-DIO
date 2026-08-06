import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from random import randint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Transactions.Transaction import Transaction
    

class Client:
    def __init__(self, adress: str) -> None:
        self._adress = adress
        self.accounts = {}
    @property
    def adress(self):
        return self._adress or 0    
    def AppendAccount(self, account: "Account", name: str):
        from Backend.Account import Account
        account.AddClient(self)
        self.accounts[name] = account

    def DoTransaction(self, account: "Account", transaction: "Transaction"):
        if account in self.accounts.values():
            transaction.RegistryTransaction(account)
                


if __name__ == '__main__':
    from Backend.Account import Account

    f = Account()
    c = Client('street')
    print(c.adress)