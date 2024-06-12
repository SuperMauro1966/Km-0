from controller.models.user import Cliente
from .db import ritorna_connessione

def carica_cliente(id: int) -> Cliente:
    """
    Riprende i campi interessati del cliente che ha appena effettuato l'accesso e li restituisce.
    """
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT citta, provincia, via, nome, cognome, CF, 
                telefono, email, pswd, attivo FROM vwcliente WHERE idCliente={id};""")
    dati = cur.fetchone()
    return Cliente(dati['email'], 
                   dati['pswd'], 
                   id,
                   dati['attivo'], 
                   dati['citta'], 
                   dati['provincia'], 
                   dati['via'], 
                   dati['nome'], 
                   dati['cognome'], 
                   dati['CF'], 
                   dati['telefono'])
