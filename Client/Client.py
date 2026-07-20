from Backend.Account import Account
from random import randint
from Transactions.Transaction import Transaction
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

    def DoTransaction(self, account: Account, transaction: Transaction):
        if account in self.accounts:
            transaction.RegistryTransaction(account)
                


if __name__ == '__main__':
    from Backend.Account import Account

    f = Account()
    c = Client()
    print(c.adress)