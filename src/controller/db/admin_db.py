from controller.models.user import Admin
from .db import ritorna_connessione

def carica_admin(id: int) -> Admin:
    """
    Riprende i campi interessati dell'amministratore che ha appena effettuato l'accesso e li restituisce.
    """
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"SELECT email, pswd, attivo FROM vwadmin WHERE idCredential={id};")
    dati = cur.fetchone()
    return Admin(dati['email'], dati['pswd'], id, dati['attivo'])
