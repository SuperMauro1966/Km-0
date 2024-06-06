from typing import Callable
from abc import ABC, abstractmethod

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
        while True:
            scelta = int(input("\nScegli un'opzione:\n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
            while scelta < 1 or scelta > 3:
                scelta = int(input("\nScegli un'opzione:\n1. per accedere\n2. per registrarsi\n3. per uscire\n"))
            if scelta == 1:
                self.items[0].item.run()
            elif scelta == 2:
                self.items[1].item.run()
            else:
                break

class Cmd(BaseMenu):
    def __init__(self, name: str, command: Callable[[], None]) -> None:
        super().__init__(name)
        self.command = command
    def run(self) -> None:
        self.command()