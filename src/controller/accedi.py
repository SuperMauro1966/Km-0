from .db import ritorna_connessione
def accedi(email, password):
    """
    ritorna True se l'utente è autorizzato ad accedere all'applicazione con le credenziali fornite
    username (email): email
    password: password
    """
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(idCredential) FROM tbcredential WHERE email='{email}' AND pswd='{password}' AND attivo=1;")
    row = cur.fetchone()[0]
    cur.close()
    return row==1