from Transaction import Transaction
from draw import Draw
from Deposit import Deposit
class Extract:
    def __init__(self) -> None:
        self.TransactionHistory = []
    def AddTransaction(self, transaction: Transaction):
        self.TransactionHistory.append(f'Value: {'+' if isinstance(transaction, Deposit) else ''}{'-' if isinstance(transaction, Draw) else ''}R$ {str(transaction.value):.2f} | Date: {transaction.date}')