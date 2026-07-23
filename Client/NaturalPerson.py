import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from .Client import Client

class NaturalPerson(Client):
    def __init__(self, name: str, birth: tuple, cpf: str):
        super().__init__()
        self.name = name
        self.birth = birth
        self.cpf = cpf
