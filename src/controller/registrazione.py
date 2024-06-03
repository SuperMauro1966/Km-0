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

    """
    while ruolo != 'C' and ruolo != 'V' and ruolo != 'c' and ruolo != 'v':
        ruolo=input("\nInserisci il ruolo:\nV o v per venditore\nC o c per cliente\n")
    """


    conn = db.ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{dati_registrazione['email']}', '{dati_registrazione['password']}', 1);")
    conn.commit()
    cur.close()

    cur = conn.cursor()
    cur.execute("SELECT idCredential FROM tbcredential WHERE email='{email}';")
    idC = cur.fetchone()[0]
    cur.close()


    if dati_registrazione['ruolo'].upper == 'C' :

        """
        first_name = input("\nInserisci il nome: ")
        last_name = input("Inserisci il cognome: ")
        via = input("Inserisci la via: ")    
        citta = input("Inserisci la città: ")
        provincia = input("Inserisci la provincia: ")
        """

        cur = conn.cursor()
        cur.execute(f"INSERT INTO tbcliente (idCliente, citta, provincia, via, nome, cognome, CF, telefono, `idCredential) VALUES (NULL, '{citta}', '{provincia}', '{via}', '{first_name}', '{last_name}', '{codice_fiscale}', '{telefono}', {idC[0]});")
        conn.commit()
        cur.close()
        print("Account registrato con successo.")
    else:
        """
        ragione_sociale = input("\nInserisci la ragione sociale: ")
        sitoweb = input("Inserisci un eventuale sito web: ")
        partitaIVA = int(input("Inserisci la partita IVA: "))
        
        conn = db.ritorna_connessione()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{password}', 1);")
        conn.commit()
        cur.close()

        cur = conn.cursor()
        cur.execute("SELECT idCredential FROM tbcredential WHERE email='{email}';")
        idC = cur.fetchone()[0]
        """

        cur.execute(f"INSERT INTO tbvenditore (idVenditore, sitoweb, partitaIVA, ragioneSociale, CF, telefono, idCredential) VALUES (NULL,'{sitoweb}', {partitaIVA}, '{ragione_sociale}', '{codice_fiscale}', '{telefono}', {idC[0]});")
        conn.commit()

    return True, "Registrazione completata con successo!"

    