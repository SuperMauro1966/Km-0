import sys
from  controller import db, login, registrazione
from menu import menu_accesso_app

def main() -> None:
    #print(globals())
    db.apri_connessione()
    menu_accesso_app.run()
    db.chiudi_connessione()

def test() -> None:
    db.apri_connessione()
    def test_accedi() -> None:
        assert login.accedi("Gabriele", "1234") 
        assert login.accedi("Pluto2", "12") == False
        assert login.accedi("Pippo", "5678")   
        assert login.accedi("Paperino", "10") == False  
        assert login.accedi("Pluto", "5678")  
        assert login.accedi("Topolino", "11") == False
        assert login.accedi("Plto2", "2") == False
        
    def test_registrati() -> None:
        assert registrazione.registrati({'email': "Sergio"})[0] == False
        assert registrazione.registrati({'email': "ciao"})[0]

    test_accedi()
    test_registrati() 
    db.chiudi_connessione()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "run":
        main()
    elif cmd == "test":
        test()
    else:
        print("main run per eseguire il programma", " main test per eseguire un test", sep = ';')