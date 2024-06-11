from collections import namedtuple
from controller.login import accedi
from controller.user import ottieni_ruolo
from controller.user_role import UserRole

_InputField = namedtuple('_InputField', ['nome', 'etichetta', 'default', 'conv_func'])
_param = [
    _InputField('email', 'email', '', None), 
    _InputField('password', 'password', '', None),
]
ruolo = ''

def ottieni_dati(next_menu = None, **kwargs) -> None:
    """
    Permette all'utente di inserire i campi per accedere all'applicazione.
    """
    dati = _input_dati(_param)
    
    if accedi(dati):
        print("Accesso eseguito correttamente\n")
        ruolo = ottieni_ruolo()
        if next_menu:
            next_menu.imposta_ruolo(UserRole(ruolo))
            next_menu.run()
    else:
        print("Errore nel login: l'utente potrebbe essere disattivato dall'admin o non ancora registrato nell'applicazione")

def _input_dati(fields: list[_InputField]) -> dict:
    """
    Salva gli input nel dizionario.
    """
    reg_param = {}
    for input_el in fields:
        temp_val = None
        while temp_val is None or temp_val.strip() == '':
            temp_val = input(f"Inserire campo {input_el.etichetta}: ")
        reg_param[input_el.nome] = temp_val
    return reg_param
