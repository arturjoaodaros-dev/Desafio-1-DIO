from random import randint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Backend.Account import Account


class Client:
    def __init__(self) -> None:
        self.adress = ""
        self.accounts = {}
        self.Id = randint(10000, 99999)
        
    @classmethod
    def AppendAccount(cls, account: "Account", name: str):
        client = cls()
        id = client.Id
        account.AddClient(client, id)
        client.accounts[name] = account

    def DoTransaction(self, account: Account, transaction: str):
        if account in self.accounts:
            if transaction.lower() is 'deposit':
                ...
                


if __name__ == '__main__':
    from Backend.Account import Account

    f = Account()
    c = Client()
    print(c.adress)