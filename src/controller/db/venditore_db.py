from controller.models.user import Vend
from .db import ritorna_connessione

def carica_venditore(id: int) -> Vend:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT idVenditore, sitoweb, partitaIVA, ragioneSociale, CF,
                 telefono, email, pswd, attivo FROM vwvenditore WHERE idVenditore={id};""")
    dati = cur.fetchone()
    return Vend(dati['email'], dati['pswd'], dati['idVenditore'], dati['sitoweb'],
                dati['partitaIVA'], dati['ragioneSociale'], dati['CF'],
                dati['telefono'])
 