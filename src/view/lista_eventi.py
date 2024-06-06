from controller import db
from . import login_utente
def _check_eventi(email: str, password: str) -> str:
    cur = db.ritorna_connessione
    cur.execute(f"SELECT Ruolo FROM vwruoli_attivi WHERE email='{email}' AND pswd='{password}';")
    ruolo = cur.fetchone()[0]
    return ruolo

def eventi():
    print("Nessun evento disponibile")
    input("Premi return per uscire")