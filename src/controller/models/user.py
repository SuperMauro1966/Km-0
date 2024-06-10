from controller.user_role import UserRole

class BaseUsers(object):
    ruolo = None

    def __init__(self, email, password, id, attivo) -> None:
        self.email = email
        self.password = password
        self.attivo = attivo
        self.id = id

class Vend(BaseUsers):
    def __init__(self, email, password, id, sito_web, partita_IVA, ragione_sociale, codice_fiscale, telefono) -> None:
        super().__init__(email, password, id,sito_web, partita_IVA, ragione_sociale, codice_fiscale, telefono)
        self.sito_web = sito_web
        self.partita_IVA = partita_IVA
        self.ragione_sociale = ragione_sociale
        self.codice_fiscale = codice_fiscale
        self.telefono =  telefono
        ruolo = UserRole.VEND

class Cliente(BaseUsers):
    def __init__(self, email, password, id, citta, provincia, via, nome,cognome, codice_fiscale, telefono) -> None:
        super().__init__(email, password, id, citta, provincia, via, nome,cognome, codice_fiscale, telefono)
        self.citta = citta
        self.provincia = provincia
        self.via = via
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.telefono =  telefono
        ruolo = UserRole.CLIENTE

class Admin(BaseUsers):
    def __init__(self, email, password, id, attivo) -> None:
        super().__init__(email, password, id, attivo)
        ruolo = UserRole.ADMIN