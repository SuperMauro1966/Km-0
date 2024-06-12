from controller.models.user import Vend
from .db import ritorna_connessione

def carica_venditore(id: int) -> Vend:
    """
    Riprende i campi interessati del venditore che ha appena effettuato l'accesso e li restituisce.
    """
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT sitoweb, partitaIVA, ragioneSociale, CF,
                 telefono, email, pswd, attivo FROM vwvenditore WHERE idVenditore={id};""")
    dati = cur.fetchone()
    return Vend(dati['email'], dati['pswd'], id, dati['attivo'], dati['sitoweb'],
                dati['partitaIVA'], dati['ragioneSociale'], dati['CF'],
                dati['telefono'])
 