from controller.db import db

def _check_email(email: str) -> bool:
    """
    ritorna True se l'utente ha inserito una mail già usata per l'autenticazione
    email: email
    """
    conn = db.ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(idCredential) FROM tbcredential WHERE email='{email}';")
    ch_mail = cur.fetchone()[0]
    cur.close()

    return ch_mail == 1

def registrati(dati_registrazione: dict) -> tuple[bool, str]:
    """
    registra l'utente all'interno del database differenziandolo tra cliente e venditore
    email: email
    password: password
    codice_fiscale: codice fiscale
    telefono: numero di telefono
    ruolo: indicare se si è clienti o venditori
    citta: città di residenza
    provincia: provincia di residenza
    via: via di residenza
    first_name: nome
    last_name: cognome
    ragione_sociale: ragione sociale
    sitoweb: sito web del venditore
    partitaIVA: partita IVA
    """
    if _check_email(dati_registrazione['email']):
        return False, "Utente già registrato"
    
    conn = db.ritorna_connessione()
    cur = conn.cursor()
    conn.begin()
    cur.execute(f"INSERT INTO tbcredential (email, pswd) VALUES ('{dati_registrazione['email']}', '{dati_registrazione['password']}');")
    cur.execute(f"SELECT idCredential FROM tbcredential WHERE email='{dati_registrazione['email']}';")
    idC = cur.fetchone()[0]

    if dati_registrazione['ruolo'].upper() == 'C':
        cur.execute(f"""INSERT INTO tbcliente (citta, provincia, via, nome, cognome, CF, telefono, idCredential) VALUES (
                    '{dati_registrazione['citta']}', 
                    '{dati_registrazione['provincia']}', 
                    '{dati_registrazione['via']}', 
                    '{dati_registrazione['nome']}', 
                    '{dati_registrazione['cognome']}', 
                    '{dati_registrazione['codice_fiscale']}', 
                    '{dati_registrazione['telefono']}', 
                    {idC});""")
    else:
        cur.execute(f"""INSERT INTO tbvenditore (sitoweb, partitaIVA, ragioneSociale, CF, telefono, idCredential) VALUES (
                    '{dati_registrazione['sitoweb']}', 
                    {dati_registrazione['partitaIVA']}, 
                    '{dati_registrazione['ragione_sociale']}', 
                    '{dati_registrazione['codice_fiscale']}', 
                    '{dati_registrazione['telefono']}', 
                    {idC});""")


    conn.commit()
    cur.close()    

    return True, "Registrazione completata con successo!"