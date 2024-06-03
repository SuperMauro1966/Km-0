from controller import db

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

def _inputRegistrazione() -> dict:
    """
    permette all'utente di inserire i campi per registrarsi, differenziandolo tra cliente e venditore, in caso di inserimento di una mail già usata comparirà un messaggio di errore
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
    
    reg_param = {}
    reg_param['email'] = input("Digita l'email: ")

    if not _check_email(reg_param['email']):
        reg_param['password'] = input("Inserisci la password: ")
        reg_param['confirm_pwd'] = input("Inserisci nuovamente la password: ")
        while reg_param['password'] != reg_param['confirm_pwd']:
            print("Le password non corrispondono")
            reg_param['confirm_pwd'] = input("Inserisci nuovamente la password: ")
        reg_param['codice_fiscale'] = input("Inserisci il codice fiscale: ")
        reg_param['telefono'] = input("Inserisci il numero di telefono: ")

        reg_param['ruolo'] = input("Inserisci il ruolo:\nV o v per venditore\nC o c per cliente\n")
        # while reg_param['ruolo'].upper != 'C' and reg_param['ruolo'].upper != 'V':
        while reg_param['ruolo'].upper() not in ['C', 'V'] :
            reg_param['ruolo'] = input("Inserisci il ruolo:\nV o v per venditore\nC o c per cliente\n")

        if reg_param['ruolo'].upper() == 'C':
            reg_param['nome'] = input("\nInserisci il nome: ")
            reg_param['cognome'] = input("Inserisci il cognome: ")
            reg_param['via'] = input("Inserisci la via: ")    
            reg_param['citta'] = input("Inserisci la città: ")
            reg_param['provincia'] = input("Inserisci la provincia: ")
        else:
            reg_param['ragione_sociale'] = input("\nInserisci la ragione sociale: ")
            reg_param['sitoweb'] = input("Inserisci un eventuale sito web: ")
            reg_param['partitaIVA'] = int(input("Inserisci la partita IVA: "))

    return reg_param

def registrati() -> tuple[bool, str]:
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
    dati_registrazione = {}
    dati_registrazione = _inputRegistrazione()
    if _check_email(dati_registrazione['email']):
        return False, "Utente già registrato"
    else:
        conn = db.ritorna_connessione()
        cur = conn.cursor()
        conn.begin()
        #cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd) VALUES (NULL, '{dati_registrazione['email']}', '{dati_registrazione['password']}');")

        if dati_registrazione['ruolo'].upper() == 'C':
            cur.execute(f"""INSERT INTO vwcliente (citta, provincia, via, nome, cognome, CF, telefono, email, pswd) 
                        VALUES ( 
                        '{dati_registrazione['citta']}', 
                        '{dati_registrazione['provincia']}', 
                        '{dati_registrazione['via']}', 
                        '{dati_registrazione['nome']}', 
                        '{dati_registrazione['cognome']}', 
                        '{dati_registrazione['codice_fiscale']}', 
                        '{dati_registrazione['telefono']}', 
                        '{dati_registrazione['email']}'
                        '{dati_registrazione['password']}');""")
        else:
            cur.execute(f"""INSERT INTO vwvenditore (sitoweb, partitaIVA, ragioneSociale, CF, telefono, email, pswd) 
                        VALUES (
                        '{dati_registrazione['sitoweb']}', 
                         {dati_registrazione['partitaIVA']}, 
                        '{dati_registrazione['ragione_sociale']}', 
                        '{dati_registrazione['codice_fiscale']}', 
                        '{dati_registrazione['telefono']}', 
                        '{dati_registrazione['email']}'
                        '{dati_registrazione['password']}');""")
            

        conn.commit()
        cur.close()    
    
        return True, "Registrazione completata con successo!"