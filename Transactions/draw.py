from typing import TYPE_CHECKING
from Backend.Account import Account
from Transactions.Transaction import Transaction

if TYPE_CHECKING:
    from Backend.CurrentAccount import CurrentAccount

class Draw(Transaction):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    def RegistryTransaction(self, account: "Account"):
        if len(account.extract.Filter()) <= account.DrawLimit:
            i = account.draw(self.value)
            if i:
                account.extract.AddTransaction(Draw(self.value))
        else:
            print('limite excedido')