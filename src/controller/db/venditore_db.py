from models.user import Vend
from db import ritorna_connessione

def carica_venditore(id) -> Vend :
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT sitoweb, partitaIVA, ragioneSociale, CF, telefono, email, pswd, attivo FROM vwvenditore WHERE id='{id}';")
    dati = cur.fetchone()
    