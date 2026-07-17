import sys
from pathlib import Path
from random import randint
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from Backend.Account import Account


class Client:
    def __init__(self) -> None:
        self.adress = ""
        self.accounts = []
        self.Id = randint(10000, 99999)
    @classmethod
    def AppendAccount(cls, account: Account):
        client = cls()
        id = client.Id
        account.AddClient(client, id)


if __name__ == '__main__':
    f = Account()
    c = Client()
    print(c.adress)