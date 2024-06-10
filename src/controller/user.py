from enum import Enum
from .db.venditore_db import carica_venditore

class UserRole(Enum):
    ADMIN = 'A'
    VEND = 'V'
    CLIENTE = 'C'
    GUEST = 'G'

_current_user = None

def carica_user(id, ruolo: UserRole):
    if ruolo == UserRole.ADMIN:
        #caricare i dati di admin
        pass
    if ruolo ==UserRole.CLIENTE:
        #caricare i dati di cliente
        pass
    if ruolo == UserRole.VEND:
        _current_user = carica_venditore(id)

def ottieni_ruolo() -> UserRole:
    return _current_user.ruolo