from .user_role import UserRole
from .db.venditore_db import carica_venditore
from .db.cliente_db import carica_cliente
from .db.admin_db import carica_admin

_current_user = None

def carica_user(id: int, ruolo: UserRole):
    if ruolo == UserRole.ADMIN:
        _current_user = carica_admin(id)
    if ruolo ==UserRole.CLIENTE:
        _current_user = carica_cliente(id)
    if ruolo == UserRole.VEND:
        _current_user = carica_venditore(id)

def ottieni_ruolo() -> UserRole:
    return _current_user.ruolo