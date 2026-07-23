import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Transactions.Transaction import Transaction
from Transactions.draw import Draw
from Transactions.Deposit import Deposit
class Extract:
    def __init__(self) -> None:
        self.TransactionHistory = []
    def AddTransaction(self, transaction: Transaction):
        sign = '+' if isinstance(transaction, Deposit) else '-' if isinstance(transaction, Draw) else ''
        self.TransactionHistory.append(f'Value: {sign}R$ {transaction.value:.2f} | Date: {transaction.date}')
