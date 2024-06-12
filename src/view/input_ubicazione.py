from collections import namedtuple
from controller.db.db import ritorna_connessione
from controller.ubicazione import inserimento_ubicazione,modifica_ubicazione,elimina_ubicazione

def menu(next_menu = None):
    if next_menu:
        next_menu.run()

def inserimento_dati():
    dict = get_data_ubicazione()
    inserimento_ubicazione(dict)

def modifica_dati():
    nome = ''
    while not check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da modificare: ")
    dict = get_data_ubicazione()
    modifica_ubicazione(dict,nome)

def elimina_dati():
    nome = ''
    while not check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da eliminare: ") 
    elimina_ubicazione(nome)

def  get_data_ubicazione() -> dict:
    InputField = namedtuple('InputField', ['nome', 'etichetta', 'default', 'conv_func'])
    param = [
        InputField('nome', 'nome ubicazione', '', None), 
        InputField('citta', 'città', '', None),
        InputField('provincia', 'provincia', '', None),
        InputField('via', 'via', '', None),
        InputField('fissa', 'ubicazione fissa', None, int),
        InputField('orario', "orario di apertura dell'ubicazione", '', None),
        InputField('attivo', 'ubicazione attiva', None, int)
    ]

    reg_param = {}
    for input_el in param:
        temp_val = None
        while temp_val is None or temp_val.strip() == '':
            temp_val = input(f"Inserire campo {input_el.etichetta}: ")
        reg_param[input_el.nome] = temp_val
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