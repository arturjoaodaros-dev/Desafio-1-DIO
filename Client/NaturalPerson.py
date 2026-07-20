from .Client import Client

class NaturalPerson(Client):
    def __init__(self, name: str, birth: tuple, cpf: int):
        super().__init__()
        self.name = name
        self.birth = birth
        self.cpf = cpf