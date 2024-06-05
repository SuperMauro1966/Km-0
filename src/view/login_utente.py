from collections import namedtuple
# verificare la pwd e l'email.

_InputField = namedtuple('_InputField', ['nome', 'etichetta', 'default', 'conv_func'])
_param = [
    _InputField ('email', 'email', '', None), 
    _InputField ('password', 'password', '', None),
]

def ottieni_dati() -> dict:
    """
    permette all'utente di inserire i campi per accedere all'applicazione
    email: email
    password: password
    """

    dati = _input_dati(_param)
    return dati

def _input_dati(fields: list[_InputField]) -> dict:
    """
    salva gli input nel dizionario
    """

    reg_param = {}
    for input_el in fields:
        temp_val = None
        while temp_val == '' or temp_val is None or temp_val.strip() == '':
            temp_val = input(f"Inserire campo {input_el.etichetta}: ")
        reg_param[input_el.nome] = temp_val
        
    return reg_param