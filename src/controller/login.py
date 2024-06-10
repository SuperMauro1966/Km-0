from .db import ritorna_connessione
from .user_role import carica_user
from .user import UserRole


def accedi(dati_login: dict) -> bool:
    """
    ritorna True se l'utente è autorizzato ad accedere all'applicazione con le credenziali fornite
    username (email): email
    password: password
    """
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"SELECT id, Ruolo FROM vwruoli_attivi WHERE email='{dati_login['email']}' AND pswd='{dati_login['password']}';")
    data_row = cur.fetchone()
    if data_row:
        # crea l'oggetto corrispondente e ne recupera i dati
        carica_user(data_row['id'], UserRole(data_row['Ruolo']))
    cur.close()
    return data_row is not None

def ottieni_ruolo(dati_login: dict) -> str:
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT Ruolo FROM vwruoli_attivi WHERE email='{dati_login['email']}' AND pswd='{dati_login['password']}';")
    data_row = cur.fetchone()[0]
    return data_row