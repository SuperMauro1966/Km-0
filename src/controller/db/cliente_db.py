from models.user import Cliente
from db import ritorna_connessione

def carica_cliente(id: int) -> Cliente:
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT citta, provincia, via, nome, cognome, CF, telefono, email, pswd, attivo FROM vwcliente WHERE id={id};")
    dati = cur.fetchone()
    return dati