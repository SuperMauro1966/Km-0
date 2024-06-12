from collections import namedtuple
from controller.login import accedi
from controller.user import ottieni_ruolo
from controller.user_role import UserRole

_InputField = namedtuple('_InputField', ['nome', 'etichetta', 'default', 'conv_func'])
_param = [
    _InputField('email', 'email', None, None), 
    _InputField('password', 'password', None, None)
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
    Salva gli input del dizionario.
    """
    reg_param = {}

    for input_el in fields:
        while True:
            print(input_el.etichetta, input_el.default)
            temp_val = input()
            if temp_val == '':
                if input_el.default:
                    reg_param[input_el.nome] = input_el.default
                    break
                else:
                    print("è necessario specificare un valore")
            if input_el.conv_func:
                try:
                    reg_param[input_el.nome] = input_el.conv_func(temp_val)
                except ValueError:
                    print("Errore nella conversione del tipo di dati")
                else:
                    break
            else:
                reg_param[input_el.nome] = temp_val
                break
    return reg_param
