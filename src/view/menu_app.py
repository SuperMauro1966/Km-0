from .menu.menu import MenuItem, SubMenu, Cmd
from ..controller.login import accedi
from . import get_reg_dati, get_log_dati

_cmd_login = Cmd("Login", get_log_dati)
_cmd_registra = Cmd("Registrazione", get_reg_dati)

_item_login = MenuItem("Login", _cmd_login, [])
_item_registra = MenuItem("Registrazione", _cmd_registra, [])

menu_accesso_app = SubMenu("accedi all'applicazione")
menu_accesso_app.add_item(_item_login)
menu_accesso_app.add_item(_item_registra)