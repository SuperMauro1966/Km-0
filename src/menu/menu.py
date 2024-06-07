from typing import Callable
from abc import ABC, abstractmethod
from controller.user_role import UserRole

class BaseMenu(ABC):
    ruolo_utente: UserRole = None
    def __init__(self, name: str) -> None:
        self.name = name
    
    @abstractmethod
    def run() -> None:
        pass

    @classmethod
    def imposta_ruolo(cls, ruolo: UserRole) -> None:
        cls.ruolo_utente = ruolo

class MenuItem(object):
    def __init__(self, label: str, item: BaseMenu, autorizzazioni: set[UserRole]) -> None:
        self.label = label
        self.item = item
        self.autorizzazioni = autorizzazioni

class SubMenu(BaseMenu):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def run(self) -> None:
        self._print()
        self._input_scelta()

    def _print(self) -> None:
        print(self.name)
        for pos, item in  enumerate(self.items, start=1):
            if self.ruolo_utente in item.autorizzazioni:
                print(pos,' - ', item.label)
        print("0  -  Uscita")

    def _input_scelta(self) -> None:
        while True:
            print("Scegli un'opzione")
            scelta = int(input())
            if scelta == 0:
                break
            elif scelta > 0 and scelta <= len(self.items):
                self.items[scelta-1].item.run()
                self._print()
        

class Cmd(BaseMenu):
    def __init__(self, name: str, command: Callable[[], None], **kwargs) -> None:
        super().__init__(name)
        self.command = command
        self.kwargs = kwargs

    def run(self) -> None:
        self.command(**self.kwargs)