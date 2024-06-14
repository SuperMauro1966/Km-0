import typing
from dataclasses import dataclass

# nome, citta, provincia, via, fissa, orario, attiva

@dataclass
class Ubicazione ():
    nome: str
    citta: str
    provincia: str
    via: str
    fissa: bool
    orario: str
    attiva: bool
