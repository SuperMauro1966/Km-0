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
    def add_item(self, item: MenuItem):
        self.items.append(item)
    def run():
        pass

class Cmd(BaseMenu):
    def __init__(self, name: str, command: Callable[[],]) -> None:
        super().__init__(name)
        self.command = command
    def run(self):
        self.command()