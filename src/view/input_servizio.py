from collections import namedtuple
from controller.servizio import inserimento_servizio

def menu_serv(next_menu = None) -> None:
    if next_menu:
        next_menu.run()

def inserimento_dati() -> None:
    dict = input_dati()
    inserimento_servizio(dict)

def modifica_dati() -> None:
    pass

def elimina_dati() -> None:
    pass
def mostra_dati() -> None:
    pass
    
def input_dati() -> dict:
    """
    Salva gli input del dizionario.
    """
    reg_param = {}
    InputField = namedtuple('InputField', ['nome', 'etichetta', 'default', 'conv_func'])
    param = [
        InputField('nome', 'nome servizio', None, None), 
        InputField('descrizione', 'descrizione del servizio', '', None),
        InputField('prezzo', 'prezzo del servizio', None, float),
        InputField('quantita', 'quantità', None, None)
    ]
    for input_el in param:
        while True:
            temp_val = input(f"{input_el.etichetta}(default: {input_el.default}): ")
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