from models.user import Vend
from db import ritorna_connessione

def carica_cliente(id: int) -> Vend :
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT citta, provincia, via, nome, cognome, CF, telefono, email, pswd, attivo FROM vwcliente WHERE id={id};")
    dati = cur.fetchone()
    return dati