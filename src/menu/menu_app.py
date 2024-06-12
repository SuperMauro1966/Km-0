from .menu import MenuItem, SubMenu, Cmd
from view.registrazione_utente import ottieni_dati as get_reg_dati 
from view.login_utente import ottieni_dati as get_log_dati
from view.lista_eventi import eventi
from view.input_ubicazione import menu_ubi, modifica_dati as mod_ubi, inserimento_dati as ins_ubi, elimina_dati as del_ubi, mostra_dati as show_ubi
from view.input_servizio import menu_serv, inserimento_dati as ins_serv
from controller.user import UserRole

# Creazione del menù ubicazione
_cmd_inserisci_ubicazione = Cmd("Inserisci ubicazione", ins_ubi)
_cmd_modifica_ubicazione = Cmd("Modifica ubicazione", mod_ubi)
_cmd_elimina_ubicazione = Cmd("Elimina ubicazione", del_ubi)
_cmd_mostra_ubicazione = Cmd("Mostra ubicazione", show_ubi)

_item_inserisci_ubicazione = MenuItem("Aggiungi ubicazione", _cmd_inserisci_ubicazione, {UserRole.VEND})
_item_modifica_ubicazione = MenuItem("Modifica ubicazione", _cmd_modifica_ubicazione, {UserRole.ADMIN, UserRole.VEND})
_item_elimina_ubicazione = MenuItem("Elimina ubicazione", _cmd_elimina_ubicazione, {UserRole.ADMIN, UserRole.VEND})
_item_mostra_ubicazione = MenuItem("Mostra ubicazione", _cmd_mostra_ubicazione, {UserRole.ADMIN, UserRole.VEND})

menu_ubicazione = SubMenu("Menù di ubicazione")
menu_ubicazione.add_item(_item_inserisci_ubicazione)
menu_ubicazione.add_item(_item_modifica_ubicazione)
menu_ubicazione.add_item(_item_elimina_ubicazione)
menu_ubicazione.add_item(_item_mostra_ubicazione)

# Creazione del menù per i servizi
_cmd_inserisci_servizio = Cmd("Inserisci servizio", ins_serv)

_item_inserisci_servizio = MenuItem("Aggiungi servizio", _cmd_inserisci_servizio, {UserRole.VEND})

menu_servizio = SubMenu("Menù di servizio")
menu_servizio.add_item(_item_inserisci_servizio)

# Creazione del menù principale
_cmd_menu_principale = Cmd("Lista Eventi", eventi)
_cmd_ubicazione = Cmd("Ubicazione", menu_ubi, next_menu = menu_ubicazione)
_cmd_servizio = Cmd("Servizio", menu_serv, next_menu = menu_servizio)

_item_menu_principale = MenuItem("Lista eventi", _cmd_menu_principale, {UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})
_item_ubicazione = MenuItem("Gestisci ubicazioni", _cmd_ubicazione, {UserRole.ADMIN, UserRole.VEND})
_item_servizio = MenuItem("Gestisci servizio", _cmd_servizio, {UserRole.ADMIN, UserRole.VEND})

menu_principale_app = SubMenu("Menù principale dell'applicazione")
menu_principale_app.add_item(_item_menu_principale)
menu_principale_app.add_item(_item_ubicazione)
menu_principale_app.add_item(_item_servizio)

# Inizializziamo il menù di accesso all'applicazione
_cmd_registra = Cmd("Registrazione", get_reg_dati)
_cmd_login = Cmd("Login", get_log_dati, next_menu = menu_principale_app)
_cmd_about = Cmd("About", None)

_item_login = MenuItem("Login", _cmd_login, {UserRole.GUEST, UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})
_item_registra = MenuItem("Registrazione", _cmd_registra, {UserRole.GUEST, UserRole.ADMIN, UserRole.CLIENTE, UserRole.VEND})
_item_about = MenuItem("About", _cmd_about, {UserRole.VEND, UserRole.CLIENTE, UserRole.ADMIN})

menu_accesso_app = SubMenu("Accedi all'applicazione")
menu_accesso_app.add_item(_item_login)
menu_accesso_app.add_item(_item_about)
menu_accesso_app.add_item(_item_registra)