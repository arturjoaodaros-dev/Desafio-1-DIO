from Backend.Account import Account
from Transaction import Transaction

class Draw(Transaction):
    def __init__(self, value, date) -> None:
        super().__init__(value, date)
    
    def RegistryTransaction(self, account: Account):
        ...