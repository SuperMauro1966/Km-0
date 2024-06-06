from .menu import MenuItem, SubMenu, Cmd
from view.registrazione_utente import ottieni_dati as get_reg_dati 
from view.login_utente import ottieni_dati as get_log_dati
from view.lista_eventi import lista_eventi

# Creazione del menù principale
_cmd_menu_principale = Cmd("Menù principale",lista_eventi)

_item_menu_principale = MenuItem("Registrazione", _cmd_menu_principale, [])

menu_principale_app = SubMenu("menù principale dell'applicazione")
menu_principale_app.add_item(_item_menu_principale)

_cmd_login = Cmd("Login", get_log_dati, next_menu = menu_principale_app)

# Inizializziamo il menù di accesso all'applicazione
_cmd_registra = Cmd("Registrazione", get_reg_dati)

_item_login = MenuItem("Login", _cmd_login, [])
_item_registra = MenuItem("Registrazione", _cmd_registra, [])

menu_accesso_app = SubMenu("accedi all'applicazione")
menu_accesso_app.add_item(_item_login)
menu_accesso_app.add_item(_item_registra)