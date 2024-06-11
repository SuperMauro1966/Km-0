from .db.db import ritorna_connessione
from .user_role import UserRole
from .user import carica_user
from menu.menu import BaseMenu

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
        BaseMenu.imposta_ruolo(UserRole(data_row['Ruolo']))
        carica_user(data_row['id'], UserRole(data_row['Ruolo']))
    cur.close()
    return data_row is not None