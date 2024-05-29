import sys
import mariadb

def accedi(cur):
    email=input("digita l'email: ")
    password=input("digita la password: ")

    cur.execute(f"SELECT COUNT(idCredential), attivo FROM tbcredential WHERE email='{email}' AND pswd='{password}' GROUP BY attivo;")
    row=cur.fetchone()
    if row[0]==1 and row[1]==1:
        print("sei stato autenticato correttamente!")
    elif row[0]==0:
        print("probabilmente non è ancora registrato, prema 2 nella sezione successiva")
    elif row[1]==0:
        print("account disattivato, per riattivarlo contattare l'amministratore di sistema")
    else:
        print("\n")

def registrati(cur):
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
            idC=cur.fetchone()[0]
            cur.execute(f"INSERT INTO tbcliente (idCliente, citta, provincia, via, nome, cognome, CF, telefono, `idCredential) VALUES (NULL, '{citta}', '{provincia}', '{via}', '{first_name}', '{last_name}', '{codice_fiscale}', '{telefono}', {idC});")
            print("Account registrato con successo.")
        else:
            ragione_sociale=input("\nInserisci la ragione sociale: ")
            sitoweb=input("Inserisci un eventuale sito web: ")
            partitaIVA=int(input("Inserisci la partita IVA: "))
            
            cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{pwd}', 1);")
            conn.commit()
            idC=cur.fetchone()[0]
            cur.execute(f"INSERT INTO tbvenditore (idVenditore, sitoweb, partitaIVA, ragioneSociale, CF, telefono, idCredential) VALUES (NULL,'{sitoweb}', {partitaIVA}, '{ragione_sociale}', '{codice_fiscale}', '{telefono}', {idC});")



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

cur=conn.cursor()
while True:
    scelta=int(input("Scegli un'opzione: \n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
    while scelta<1 or scelta>3:
        scelta=int(input("\nScegli un'opzione: \n1. per accedere\n2. per registrarsi\n3. per uscire\n"))

    print("\n")
    if scelta==1:
        accedi(cur)
        cur.close()
        conn.close()
    elif scelta==2:
        registrati(cur)
        cur.close()
        conn.close()
    else:
        break