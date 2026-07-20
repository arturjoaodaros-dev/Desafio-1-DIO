from .Account import Account

class CurrentAccount(Account):

    def __init__(self) -> None:
        super().__init__()
        self.limit = float
        self.DrawLimit = int