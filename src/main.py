import sys
from  controller import db, login, registrazione
from view import get_reg_dati
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
            dati_registrazione = get_reg_dati()
            status, msg = registrazione.registrati(dati_registrazione)
            print(msg)
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