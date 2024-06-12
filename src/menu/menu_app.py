from .menu import MenuItem, SubMenu, Cmd
from view.registrazione_utente import ottieni_dati as get_reg_dati 
from view.login_utente import ottieni_dati as get_log_dati
from view.lista_eventi import eventi
from view.input_ubicazione import menu, modifica_dati, inserimento_dati, elimina_dati, mostra_dati
from controller.user import UserRole

# Creazione del menù ubicazione
_cmd_inserisci_ubicazione = Cmd("Inserisci Ubicazione",inserimento_dati)
_cmd_modifica_ubicazione = Cmd("Modifica Ubicazione",modifica_dati)
_cmd_elimina_ubicazione = Cmd("Elimina Ubicazione",elimina_dati)
_cmd_mostra_ubicazione = Cmd("Mostra Ubicazione",mostra_dati)

_item_inserisci_ubicazione = MenuItem("Aggiungi Ubicazione",_cmd_inserisci_ubicazione,{UserRole.ADMIN, UserRole.VEND})
_item_modifica_ubicazione = MenuItem("Modifica Ubicazione",_cmd_modifica_ubicazione,{UserRole.ADMIN, UserRole.VEND})
_item_elimina_ubicazione = MenuItem("Elimina Ubicazione",_cmd_elimina_ubicazione,{UserRole.ADMIN, UserRole.VEND})
_item_mostra_ubicazione = MenuItem("Mostra Ubicazione",_cmd_mostra_ubicazione,{UserRole.ADMIN, UserRole.VEND})

menu_ubicazione = SubMenu("menù di ubicazione")
menu_ubicazione.add_item(_item_inserisci_ubicazione)
menu_ubicazione.add_item(_item_modifica_ubicazione)
menu_ubicazione.add_item(_item_elimina_ubicazione)
menu_ubicazione.add_item(_item_mostra_ubicazione)

# Creazione del menù principale
_cmd_menu_principale = Cmd("Lista Eventi", eventi)
_cmd_ubicazione = Cmd("Ubicazione",menu,next_menu = menu_ubicazione)

_item_menu_principale = MenuItem("Lista Eventi", _cmd_menu_principale, {UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})
_item_ubicazione = MenuItem("Gestisci Ubicazioni", _cmd_ubicazione, {UserRole.ADMIN, UserRole.VEND})

menu_principale_app = SubMenu("menù principale dell'applicazione")
menu_principale_app.add_item(_item_menu_principale)
menu_principale_app.add_item(_item_ubicazione)

# Inizializziamo il menù di accesso all'applicazione
_cmd_registra = Cmd("Registrazione", get_reg_dati)
_cmd_login = Cmd("Login", get_log_dati, next_menu = menu_principale_app)
_cmd_about = Cmd("About", None)

_item_login = MenuItem("Login", _cmd_login, {UserRole.GUEST, UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})
_item_registra = MenuItem("Registrazione", _cmd_registra, {UserRole.GUEST, UserRole.ADMIN, UserRole.CLIENTE, UserRole.VEND})
_item_about = MenuItem("About", _cmd_about, {UserRole.VEND, UserRole.CLIENTE, UserRole.ADMIN})

menu_accesso_app = SubMenu("accedi all'applicazione")
menu_accesso_app.add_item(_item_login)
menu_accesso_app.add_item(_item_about)
menu_accesso_app.add_item(_item_registra)