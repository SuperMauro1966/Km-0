from .menu import MenuItem, SubMenu, Cmd
from view.registrazione_utente import ottieni_dati as get_reg_dati 
from view.login_utente import ottieni_dati as get_log_dati
from view.input_ubicazione import modifica_dati as mod_ubi, inserimento_dati as ins_ubi, elimina_dati as del_ubi, mostra_dati as show_ubi
from view.input_servizio import inserimento_dati as ins_serv, modifica_dati as mod_serv, elimina_dati as del_serv, mostra_dati as show_serv
from view.input_eventi import modifica_dati as mod_eventi, inserimento_dati as ins_eventi, elimina_dati as del_eventi, mostra_dati as show_eventi
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
_cmd_modifica_servizio = Cmd("Modifica ubicazione", mod_serv)
_cmd_elimina_servizio = Cmd("Elimina ubicazione", del_serv)
_cmd_mostra_servizio = Cmd("Mostra ubicazione", show_serv)

_item_inserisci_servizio = MenuItem("Aggiungi servizio", _cmd_inserisci_servizio, {UserRole.VEND})
_item_modifica_servizio = MenuItem("Modifica servizio", _cmd_modifica_servizio, {UserRole.ADMIN, UserRole.VEND})
_item_elimina_servizio = MenuItem("Elimina servizio", _cmd_elimina_servizio, {UserRole.ADMIN, UserRole.VEND})
_item_mostra_servizio = MenuItem("Mostra servizio", _cmd_mostra_servizio, {UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})

menu_servizio = SubMenu("Menù di servizio")
menu_servizio.add_item(_item_inserisci_servizio)
menu_servizio.add_item(_item_modifica_servizio)
menu_servizio.add_item(_item_elimina_servizio)
menu_servizio.add_item(_item_mostra_servizio)

# Creazione del menù ubicazione
_cmd_inserisci_eventi = Cmd("Inserisci evento", ins_eventi)
_cmd_modifica_eventi = Cmd("Modifica evento", mod_eventi)
_cmd_elimina_eventi = Cmd("Elimina evento", del_eventi)
_cmd_mostra_eventi = Cmd("Mostra evento", show_eventi)

_item_inserisci_eventi = MenuItem("Aggiungi evento", _cmd_inserisci_eventi, {UserRole.VEND})
_item_modifica_eventi = MenuItem("Modifica evento", _cmd_modifica_eventi, {UserRole.ADMIN, UserRole.VEND})
_item_elimina_eventi = MenuItem("Elimina evento", _cmd_elimina_eventi, {UserRole.ADMIN, UserRole.VEND})
_item_mostra_eventi = MenuItem("Mostra evento", _cmd_mostra_eventi, {UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})

menu_eventi = SubMenu("Menù degli eventi")
menu_eventi.add_item(_item_inserisci_eventi)
menu_eventi.add_item(_item_modifica_eventi)
menu_eventi.add_item(_item_elimina_eventi)
menu_eventi.add_item(_item_mostra_eventi)

# Creazione del menù principale

_item_lista_eventi = MenuItem("Eventi", menu_eventi, {UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})
_item_ubicazione = MenuItem("Ubicazioni", menu_ubicazione, {UserRole.ADMIN, UserRole.VEND})
_item_servizio = MenuItem("Servizio",menu_servizio, {UserRole.ADMIN, UserRole.VEND, UserRole.CLIENTE})

menu_principale_app = SubMenu("Menù principale dell'applicazione")
menu_principale_app.add_item(_item_lista_eventi)
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