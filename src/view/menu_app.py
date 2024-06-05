from .menu import MenuItem, SubMenu, Cmd
from ..controller.login import accedi
from . import get_reg_dati

cmd_login = Cmd("Login", None)
cmd_registra = Cmd("Registrazione", get_reg_dati)

item_login = MenuItem("Login", cmd_login, [])
item_registra = MenuItem("Registrazione", cmd_registra, [])

menu_accesso_app = SubMenu("accedi all'applicazione")
menu_accesso_app.add_item(item_login)
menu_accesso_app.add_item(item_registra)