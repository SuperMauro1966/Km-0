import sys
from  controller import db, login, registrazione

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
            if login.accedi(email, password):
                print("Autenticato correttamente!")
            else:
                print("Errore nel login, l'utente potrebbe non esistere o disattivato dall'admin")
        elif scelta == 2:
            reg_param = {}
            reg_param['email'] = input("Digita l'email: ")
            status, msg = registrazione.registrati(reg_param)
            if status:
                print(msg)
            else:
                #inserimento dei campi in comune
                reg_param['password'] = input("Inserisci la password: ")
                reg_param['confirm_pwd'] = input("Inserisci nuovamente la password: ")
                while reg_param['password'] != reg_param['confirm_pwd']:
                    print("Le password non corrispondono")
                    reg_param['confirm_pwd'] = input("Inserisci nuovamente la password: ")
                reg_param['codice_fiscale'] = input("Inserisci il codice fiscale: ")
                reg_param['telefono'] = input("Inserisci il numero di telefono: ")
                reg_param['ruolo'] = input("Inserisci il ruolo:\nV o v per venditore\nC o c per cliente\n")
                while reg_param['ruolo'].upper != 'C' and reg_param['ruolo'].upper != 'V':
                    reg_param['ruolo'] = input("Inserisci il ruolo:\nV o v per venditore\nC o c per cliente\n")
                if reg_param['ruolo'].upper == 'C':
                    reg_param['nome'] = input("\nInserisci il nome: ")
                    reg_param['cognome'] = input("Inserisci il cognome: ")
                    reg_param['via'] = input("Inserisci la via: ")    
                    reg_param['citta'] = input("Inserisci la città: ")
                    reg_param['provincia'] = input("Inserisci la provincia: ")
                else:
                    reg_param['ragione_sociale'] = input("\nInserisci la ragione sociale: ")
                    reg_param['sitoweb'] = input("Inserisci un eventuale sito web: ")
                    reg_param['partitaIVA'] = int(input("Inserisci la partita IVA: "))

                registrazione.registrati(reg_param)
        else:
            db.chiudi_connessione()
            break

def test():
    db.apri_connessione()
    def test_accedi():
        assert login.accedi("Gabriele", "1234") 
        assert login.accedi("Pluto2", "12") == False
        assert login.accedi("Pippo", "5678")   
        assert login.accedi("Paperino", "10") == False  
        assert login.accedi("Pluto", "5678")  
        assert login.accedi("Topolino", "11") == False
        assert login.accedi("Plto2", "2") == False
    def test_registrati():
        assert registrazione.registrati({'email': "Sergio"})[0] == False
        assert registrazione.registrati({'email': "ciao"})[0]

    test_accedi()
    test_registrati() 
    db.chiudi_connessione()


if __name__ == "__main__":
    cmd=sys.argv[1]
    if cmd == "run":
        main()
    elif cmd == "test":
        test()
    else:
        print("main run per eseguire il programma","main test per eseguire un test", sep=';')