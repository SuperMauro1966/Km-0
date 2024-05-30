import sys
from  controller import accedi,db

"""def accedi(email, password):
    
    ritorna True se l'utente è autorizzato ad accedere all'applicazione con le credenziali fornite
    username (email): email
    password: password
    
    cur=conn.cursor()
    cur.execute(f"SELECT COUNT(idCredential) FROM tbcredential WHERE email='{email}' AND pswd='{password}' AND attivo=1;")
    row=cur.fetchone()[0]
    cur.close()
    return row==1
    """
def check_email(email):
    cur=conn.cursor()
    cur.execute(f"SELECT COUNT(idCredential) FROM tbcredential WHERE email='{email}'")
    ch_mail = cur.fetchone()[0]
    cur.close()
    return ch_mail==0

def registrati(email, password, codice_fiscale, telefono, ruolo):
    # inserimento dati x tbcredential
    while ruolo != 'C' and ruolo != 'V' and ruolo != 'c' and ruolo != 'v':
        ruolo=input("\nInserisci il ruolo: \nV o v per venditore\nC o c per cliente\n")

    if ruolo == 'C' or ruolo == 'c':
        first_name = input("\nInserisci il nome: ")
        last_name = input("Inserisci il cognome: ")
        via = input("Inserisci la via: ")    
        citta = input("Inserisci la città: ")
        provincia = input("Inserisci la provincia: ")

        cur = conn.cursor()
        cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{password}', 1);")
        conn.commit()
        cur.close()

        cur = conn.cursor()
        cur.execute("SELECT idCredential FROM tbcredential WHERE email='{email}';")
        idC = cur.fetchone()[0]
        cur.close()

        cur = conn.cursor()
        cur.execute(f"INSERT INTO tbcliente (idCliente, citta, provincia, via, nome, cognome, CF, telefono, `idCredential) VALUES (NULL, '{citta}', '{provincia}', '{via}', '{first_name}', '{last_name}', '{codice_fiscale}', '{telefono}', {idC[0]});")
        conn.commit()
        cur.close()
        print("Account registrato con successo.")
    else:
        ragione_sociale = input("\nInserisci la ragione sociale: ")
        sitoweb = input("Inserisci un eventuale sito web: ")
        partitaIVA = int(input("Inserisci la partita IVA: "))
            
        cur = conn.cursor()
        cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{password}', 1);")
        conn.commit()
        cur.close()

        cur = conn.cursor()
        cur.execute("SELECT idCredential FROM tbcredential WHERE email='{email}';")
        idC = cur.fetchone()[0]
        cur.execute(f"INSERT INTO tbvenditore (idVenditore, sitoweb, partitaIVA, ragioneSociale, CF, telefono, idCredential) VALUES (NULL,'{sitoweb}', {partitaIVA}, '{ragione_sociale}', '{codice_fiscale}', '{telefono}', {idC[0]});")
        conn.commit()

def main():
    db.apri_connessione()

    #print(globals())
    while True:
        scelta = int(input("\nScegli un'opzione:\n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
        while scelta < 1 or scelta > 3:
            scelta = int(input("\nScegli un'opzione:\n1. per accedere\n2. per registrarsi\n3. per uscire\n"))

        print("\n")
        if scelta == 1:
            email = input("Digita l'email: ")
            password = input("Digita la password: ")
            if accedi(email, password):
                print("Autenticato correttamente!")
            else:
                print("Errore nel login, l'utente potrebbe non esistere o disattivato dall'admin")
        elif scelta == 2:
            email = input("Digita l'email: ")
            if check_email(email):
                print("Errore! Email già utilizzata")
                break

            #inserimento dei campi in comune
            password = input("Inserisci la password: ")
            confirm_pwd = input("Inserisci nuovamente la password: ")
            while password != confirm_pwd:
                print("Le password non corrispondono")
                confirm_pwd = input("Inserisci nuovamente la password: ")
            codice_fiscale = input("Inserisci il codice fiscale: ")
            telefono = input("Inserisci il numero di telefono: ")
            
            ruolo = input("Inserisci il ruolo: \nV o v per venditore\nC o c per cliente\n")
            registrati(email, password, codice_fiscale, telefono, ruolo)
        else:
            conn.close()
            break

def test():
    db.apri_connessione()
    assert accedi.accedi("Gabriele","1234") 
    assert accedi.accedi("Pluto2","12") == False
    assert accedi.accedi("Pippo","5678")   
    assert accedi.accedi("Paperino","10") == False  
    assert accedi.accedi("Pluto","5678")  
    assert accedi.accedi("Topolino","11") == False
    assert accedi.accedi("Plto2","2") == False


if __name__ == "__main__":
    cmd=sys.argv[1]
    if cmd == "run":
        main()
    elif cmd == "test":
        test()
    else:
        print("main run per eseguire il programma","main test per eseguire un test", sep=';')