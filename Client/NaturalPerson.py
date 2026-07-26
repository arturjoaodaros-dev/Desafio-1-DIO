import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from .Client import Client

class NaturalPerson(Client):
    def __init__(self, name: str, birth: tuple, cpf: str, adress):
        super().__init__(adress)
        self._name = name
        self._birth = birth
        self._cpf = cpf

    @property
    def name(self):
        return self._name or None

    @property
    def birth(self):
        return self._birth or None

    @property
    def cpf(self):
        return self._cpf or 0
