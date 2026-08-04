import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Backend.Account import Account
from Client.Client import Client
from Transactions.Deposit import Deposit

class CurrentAccount(Account):

    def __init__(self) -> None:
        super().__init__()
        self._limit = 1000.0
        self._DrawLimit = 3

    @property
    def limit(self):
        return self._limit or 0

    @property
    def DrawLimit(self):
        return self._DrawLimit or 0

if __name__ == '__main__':
    acc = CurrentAccount()
    client = Client('rua do rojão')
    client.AppendAccount(acc, 'Artur1')
    client.DoTransaction(client.accounts['Artur1'], Deposit(90))
    print(client.accounts['Artur1'].currency)
    print(f"Limite: {client.accounts['Artur1'].limit}")
    print(client.accounts['Artur1'].Extract)
    for i in client.accounts['Artur1'].extract:
        print(i)