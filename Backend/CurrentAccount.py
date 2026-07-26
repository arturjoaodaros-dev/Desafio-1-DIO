import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Backend.Account import Account
from Client.Client import Client
from Transactions.Deposit import Deposit

class CurrentAccount(Account):

    def __init__(self) -> None:
        super().__init__()
        self.limit = 0.0
        self.DrawLimit = 0

if __name__ == '__main__':
    acc = CurrentAccount()
    client = Client('rua do rojão')
    client.AppendAccount(acc, 'Artur1')
    client.DoTransaction(client.accounts['Artur1'], Deposit(90))
    print(client.accounts['Artur1'].currency)
    print(f"Limite: {client.accounts['Artur1'].limit}")
    print(f"Limite de Saque: {client.accounts['Artur1'].DrawLimit}")