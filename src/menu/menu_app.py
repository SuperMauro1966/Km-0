from .menu import MenuItem, SubMenu, Cmd
from view.registrazione_utente import ottieni_dati as get_reg_dati 
from view.login_utente import ottieni_dati as get_log_dati
from view.lista_eventi import eventi
from controller.user_role import UserRole

# Creazione del menù principale
_cmd_menu_principale = Cmd("Menù principale", eventi)

_item_menu_principale = MenuItem("Lista Eventi", _cmd_menu_principale, [])

menu_principale_app = SubMenu("menù principale dell'applicazione")
menu_principale_app.add_item(_item_menu_principale)

# Inizializziamo il menù di accesso all'applicazione
_cmd_registra = Cmd("Registrazione", get_reg_dati)
_cmd_login = Cmd("Login", get_log_dati, next_menu = menu_principale_app)
_cmd_about = Cmd("About", None)

_item_login = MenuItem("Login", _cmd_login, {UserRole.GUEST})
_item_registra = MenuItem("Registrazione", _cmd_registra, {UserRole.GUEST})
_item_about = MenuItem("About", _cmd_about, {UserRole.VEND, UserRole.CLIENTE, UserRole.ADMIN})

menu_accesso_app = SubMenu("accedi all'applicazione")
menu_accesso_app.add_item(_item_login)
menu_accesso_app.add_item(_item_registra)
menu_accesso_app.add_item(_item_about)
menu_accesso_app.imposta_ruolo(UserRole.GUEST)