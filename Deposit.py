from Backend.Account import Account
from Transaction import Transaction

class Deposit(Transaction):
    def __init__(self, value, date) -> None:
        super().__init__(value, date)
    
    def RegistryTransaction(self, account: Account):
        i = account.deposit(self.value)
        if i:
            account.extract.AddTransaction(Deposit(self.value, self.date) )