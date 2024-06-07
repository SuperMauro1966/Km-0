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
        self.items: list[MenuItem] = []
    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)
    def run(self) -> None:
        self._print()
        self._input_scelta()

    def _print(self):
        print(self.name)
        for pos,item in  enumerate(self.items, start=1):
            print(pos,' - ', item.label)
        print("0  -  Uscita")

    def _input_scelta(self):
        while True:
            print("Scegli un'opzione")
            scelta=int(input())
            while scelta<0 or scelta>2:
                print("Scegli un'opzione")
                scelta=int(input())
            if scelta == 0:
                    break
            else:   
                for i,s in enumerate(self.items, start=1):
                    if scelta == i:
                        self.items[i-1].item.run()
                        self._print()
        

class Cmd(BaseMenu):
    def __init__(self, name: str, command: Callable[[], None], **kwargs) -> None:
        super().__init__(name)
        self.command = command
        self.kwargs = kwargs
    def run(self) -> None:
        self.command(**self.kwargs)