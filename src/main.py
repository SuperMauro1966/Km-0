import sys
import mariadb
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
def registrati():
    # inserimento dati x tbcredential
    email=input("Inserisci l'e-mail: ")
    cur.execute(f"SELECT COUNT(idCredential) FROM tbcredential WHERE email='{email}';")
    check_email=cur.fetchone()[0]
    if check_email==1:
        print("è già stato creato un account con questa mail")
    else:
        pwd=input("Inserisci la password: ")
        confirm_pwd=input("Inserisci nuovamente la password: ")
        while pwd!=confirm_pwd:
            print("Le password non corrispondono")
            confirm_pwd=input("Inserisci nuovamente la password: ")
        #inserimento dei dati in comune
        codice_fiscale=input("Inserisci il codice fiscale: ")
        telefono=input("Inserisci il numero di telefono: ")
        ruolo=input("Inserisci il ruolo: \nV o v per venditore\nC o c per cliente\n")
        while ruolo!='C' and ruolo!='V' and ruolo!='c' and ruolo!='v':
            ruolo=input("\nInserisci il ruolo: \nV o v per venditore\nC o c per cliente\n")
            
        if ruolo=='C' or ruolo=='c':
            first_name=input("\nInserisci il nome: ")
            last_name=input("Inserisci il cognome: ")
            via=input("Inserisci la via: ")    
            citta=input("Inserisci la città: ")
            provincia=input("Inserisci la provincia: ")
            cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{pwd}', 1);")
            conn.commit()
            cur.execute("SELECT idCredential FROM tbcredential;")
            idC=cur.fetchone()[0]
            cur.execute(f"INSERT INTO tbcliente (idCliente, citta, provincia, via, nome, cognome, CF, telefono, `idCredential) VALUES (NULL, '{citta}', '{provincia}', '{via}', '{first_name}', '{last_name}', '{codice_fiscale}', '{telefono}', {idC[0]});")
            conn.commit()
            print("Account registrato con successo.")
        else:
            ragione_sociale=input("\nInserisci la ragione sociale: ")
            sitoweb=input("Inserisci un eventuale sito web: ")
            partitaIVA=int(input("Inserisci la partita IVA: "))
            
            cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{pwd}', 1);")
            conn.commit()
            cur.execute("SELECT idCredential FROM tbcredential;")
            idC=cur.fetchone()[0]
            cur.execute(f"INSERT INTO tbvenditore (idVenditore, sitoweb, partitaIVA, ragioneSociale, CF, telefono, idCredential) VALUES (NULL,'{sitoweb}', {partitaIVA}, '{ragione_sociale}', '{codice_fiscale}', '{telefono}', {idC[0]});")
            conn.commit()

def main():
    try:
        globals()["conn"]=mariadb.connect(
            user="root",
            password="1234",
            host="127.0.0.1",
            port=3306,
            database="km-0"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
        sys.exit(1)

    #print(globals())
    while True:
        scelta=int(input("\nScegli un'opzione: \n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
def main():
    try:
        conn=mariadb.connect(
            user="root",
            password="1234",
            host="127.0.0.1",
            port=3306,
            database="km-0"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
        sys.exit(1)

    print(globals())
    while True:
        scelta=int(input("Scegli un'opzione: \n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
        while scelta<1 or scelta>3:
            scelta=int(input("\nScegli un'opzione: \n1. per accedere\n2. per registrarsi\n3. per uscire\n"))

        print("\n")
        if scelta==1:
            email=input("digita l'email: ")
            password=input("digita la password: ")
            if accedi(email, password):
                print("Autenticato correttamente!")
            else:
                print("Errore nel login, l'utente potrebbe non esistere o disattivato dall'admin")
        elif scelta==2:
            registrati()
        else:
            conn.close()
            break

def test():
    try:
        globals()["conn"] = \
            mariadb.connect(
                user="root",
                password="1234",
                host="127.0.0.1",
                port=3306,
                database="km-0"
            )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
        sys.exit(1)
    
    assert accedi("Gabriele","1234") 
    assert accedi("Pluto2","12") ==False
    assert accedi("Pippo","5678")   
    assert accedi("Paperino","10")==False  
    assert accedi("Pluto","5678")  
    assert accedi("Topolino","11")==False
    assert accedi("Plto2","2")==False


if __name__ == "__main__":
    cmd=sys.argv[1]
    if cmd=="run":
        main()
    elif cmd=="test":
        test()
    else:
        print("main run per eseguire il programma","main test per eseguire un test", sep=';')
        


