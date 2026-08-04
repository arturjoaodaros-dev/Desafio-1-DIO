import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Transactions.Transaction import Transaction
from Transactions.draw import Draw
from Transactions.Deposit import Deposit
class Extract:
    def __init__(self) -> None:
        self.TransactionHistory = []
        self._index = 0

    def AddTransaction(self, transaction: Transaction):
        sign = '+' if isinstance(transaction, Deposit) else '-' if isinstance(transaction, Draw) else '+'
        self.TransactionHistory.append(f'Value: {sign}R$ {transaction.value:.2f} | Date: {transaction.date}')

    def __iter__(self):
        self._index = 0
        return self.TransactionHistory
        
    def __next__(self):
        if self._index >= len(self.TransactionHistory):
            raise StopIteration
        item = self.TransactionHistory[self._index]
        self._index += 1
        return item