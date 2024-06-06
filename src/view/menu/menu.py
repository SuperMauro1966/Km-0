from typing import Callable
from abc import ABC, abstractmethod
from controller import db

class BaseMenu(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
    
    @abstractmethod
    def run() -> None:
        pass

class MenuItem(object):
    def __init__(self, label: str, item: BaseMenu, autorizzazioni: str) -> None:
        self.label = label
        self.item = item
        self.autorizzazioni = autorizzazioni

class SubMenu(BaseMenu):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.items = []
    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)
    def run(self):
        db.apri_connessione()
        while True:
            scelta = int(input("\nScegli un'opzione:\n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
            while scelta < 1 or scelta > 3:
                scelta = int(input("\nScegli un'opzione:\n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
            print("\n")
            if scelta == 1:
                if self.items[0].item.run():
                    print("Accesso eseguito correttamente")
                else:
                    print("Errore nel login: l'utente potrebbe essere disattivato dall'admin o non ancora registrato nell'applicazione")
            elif scelta == 2:
                status, msg = self.items[1].item.run()
                print(msg)
            else:
                db.chiudi_connessione
                break

class Cmd(BaseMenu):
    def __init__(self, name: str, command: Callable[[], None]) -> None:
        super().__init__(name)
        self.command = command
    def run(self) -> None:
        self.command()