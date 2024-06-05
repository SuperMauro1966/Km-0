from .db import ritorna_connessione

def accedi(email, password):
    """
    ritorna True se l'utente è autorizzato ad accedere all'applicazione con le credenziali fornite
    username (email): email
    password: password
    """
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT id, Ruolo FROM vwruoli_attivi WHERE email='{email}' AND pswd='{password}';")
    data_row = cur.fetchone()
    if data_row:
        # crea l'oggetto corrispondente ene recupera i dati
        pass
    cur.close()
    return data_row is not None
