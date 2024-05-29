import sys
import mariadb

def accedi(cur):
    email=input("digita l'email: ")
    password=input("digita la password: ")

    cur.execute(f"SELECT COUNT(idCredential), attivo FROM tbcredential WHERE email='{email}' AND pswd='{password}' GROUP BY attivo;")
    row=cur.fetchone()
    if row[0]==1 & row[1]==1:
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
    pwd=input("Inserisci la password: ")
    confirm_pwd=input("Inserisci nuovamente la password: ")
    while pwd!=confirm_pwd:
        print("Le password non corrispondono")
        confirm_pwd=input("Inserisci nuovamente la password: ")
    #inserimento dei dati in comune
    codice_fiscale=input("Inserisci il codice fiscale: ")
    telefono=input("Inserisci il numero di telefono: ")
    ruolo=input("Inserisci il ruolo: \nV per venditore\nC per cliente\n")
    while ruolo!='C' or ruolo!='V':
        ruolo=input("\nInserisci il ruolo: \nV per venditore\nC per cliente\n")
        
    if ruolo=='C':
        first_name=input("Inserisci il nome: ")
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
        ragione_sociale=input("Inserisci la ragione sociale: ")
        sitoweb=input("Inserisci un eventuale sito web: ")
        partitaIVA=int(input("Inserisci la partita IVA: "))
        cur.execute(f"INSERT INTO tbcredential (idCredential, email, pswd, attivo) VALUES (NULL, '{email}', '{pwd}', 1);")
        conn.commit()
        idC=cur.fechone()[0]
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
    scelta=int(input("Scegli un'opzione: \n1. per accedere\n2. per registrarsi\n"))
    while scelta!=1 | scelta!=2:
        scelta=int(input("\nScegli un'opzione: \n1. per accedere\n2. per registrarsi\n"))

    if scelta==1:
        accedi(cur)
        break
    elif scelta==2:
        registrati(cur)
        break