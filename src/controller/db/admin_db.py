from models.user import Admin
from db import ritorna_connessione

def carica_admin(id: int) -> Admin:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"SELECT email, pswd, attivo FROM vwadmin WHERE id={id};")
    dati = cur.fetchone()
    return Admin(dati['email'], dati['password'], id, dati['attivo'])