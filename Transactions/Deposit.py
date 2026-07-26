import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Backend.Account import Account
from Transactions.Transaction import Transaction

class Deposit(Transaction):
    def __init__(self, value) -> None:
        super().__init__(value)
    def RegistryTransaction(self, account: Account):
        i = account.deposit(self.value)
        if i:
           account.extract.AddTransaction(Deposit(self.value) )
