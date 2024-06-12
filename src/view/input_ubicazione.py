from collections import namedtuple
from controller.db.db import ritorna_connessione
from controller.ubicazione import inserimento_ubicazione, modifica_ubicazione, elimina_ubicazione, mostra_ubicazione

def menu_ubi(next_menu = None) -> None:
    if next_menu:
        next_menu.run()

def inserimento_dati() -> None:
    dict = input_dati()
    inserimento_ubicazione(dict)

def modifica_dati() -> None:
    nome = ''
    while not check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da modificare: ")
    dict = input_dati()
    modifica_ubicazione(dict, nome)

def elimina_dati() -> None:
    nome = ''
    while not check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da eliminare: ")
    elimina_ubicazione(nome)

def mostra_dati() -> None:
    nome = ''
    while not check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da mostrare: ") 
    mostra_ubicazione(nome)
    
def input_dati() -> dict:
    """
    Salva gli input del dizionario.
    """
    reg_param = {}
    InputField = namedtuple('InputField', ['nome', 'etichetta', 'default', 'conv_func'])
    param = [
        InputField('nome', 'nome ubicazione', None, None), 
        InputField('citta', 'città', None, None),
        InputField('provincia', 'provincia', None, None),
        InputField('via', 'via', None, None),
        InputField('fissa', 'ubicazione fissa', None, int),
        InputField('orario', "orario di apertura dell'ubicazione", None, None),
        InputField('attivo', 'ubicazione attiva', 0, int)
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

def check_ubicazione(nome: str) -> bool:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT idUbicazione, nome, citta, provincia, via, fissa, orario, attiva
                FROM tbubicazione
                WHERE nome='{nome}';""")
    data_row = cur.fetchone()
    cur.close()
    return data_row is not None