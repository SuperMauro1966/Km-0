from controller.user_role import UserRole

class BaseUsers(object):
    ruolo = None

    def __init__(self, email, password, id, attivo) -> None:
        self.email = email
        self.password = password
        self.attivo = attivo
        self.id = id

class Vend(BaseUsers):
    def __init__(self, email, password, id) -> None:
        super().__init__(email, password, id)
        ruolo = UserRole.VEND

class Cliente(BaseUsers):
    def __init__(self, email, password, id, citta, provincia, via) -> None:
        super().__init__(email, password, id)
        self.citta = citta
        self.provincia = provincia
        self.via = via
        ruolo = UserRole.CLIENTE

class Admin(BaseUsers):
    def __init__(self, email, password, id, attivo) -> None:
        super().__init__(email, password, id, attivo)
        ruolo = UserRole.ADMIN