import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Backend.Account import Account
from Client.Client import Client
from Transactions.Deposit import Deposit
from Transactions.draw import Draw

class CurrentAccount(Account):

    def __init__(self) -> None:
        super().__init__()
        self._limit = 1000.0
        self._DrawLimit = 10

    @property
    def limit(self):
        return self._limit or 0

    @property
    def DrawLimit(self):
        return self._DrawLimit or 0

if __name__ == '__main__':
    acc = CurrentAccount()
    client = Client('rua do rojão')
    client.AppendAccount(acc, 'Artur')
    client.DoTransaction(client.accounts['Artur'], Deposit(13) )
    client.DoTransaction(client.accounts['Artur'], Draw(1))#1
    client.DoTransaction(client.accounts['Artur'], Draw(1))#2
    client.DoTransaction(client.accounts['Artur'], Draw(1))#3
    client.DoTransaction(client.accounts['Artur'], Draw(1))#4
    client.DoTransaction(client.accounts['Artur'], Draw(1))#5
    client.DoTransaction(client.accounts['Artur'], Draw(1))#6
    client.DoTransaction(client.accounts['Artur'], Draw(1))#7
    client.DoTransaction(client.accounts['Artur'], Draw(1))#8
    client.DoTransaction(client.accounts['Artur'], Draw(1))#9
    client.DoTransaction(client.accounts['Artur'], Draw(1))#10
    client.DoTransaction(client.accounts['Artur'], Draw(1))#11
    client.DoTransaction(client.accounts['Artur'], Draw(1))#12
    client.DoTransaction(client.accounts['Artur'], Draw(1))#13
    print(acc.currency)
    