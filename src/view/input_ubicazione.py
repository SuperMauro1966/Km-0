from collections import namedtuple
from controller.db.db import ritorna_connessione

def  get_data_ubicazione() -> dict:
    InputField = namedtuple('InputField', ['nome', 'etichetta', 'default', 'conv_func'])
    param = [
        InputField('nome', 'nome ubicazione', '', None), 
        InputField('citta', 'città', '', None),
        InputField('provincia', 'provincia', '', None),
        InputField('via', 'via', '', None),
        InputField('fissa', 'ubicazione fissa', None, int),
        InputField('orario', "orario di apertura dell'ubicazione", '', None),
        InputField('attiva', 'ubicazione attiva', None, int)
    ]

    reg_param = {}
    for input_el in param:
        temp_val = None
        while temp_val is None or temp_val.strip() == '':
            temp_val = input(f"Inserire campo {input_el.etichetta}: ")
            if input_el.conv_func == int or input_el.conv_func == float or temp_val < 0 or temp_val > 1:
                try:
                    int(temp_val)
                except ValueError:
                    print("Il campo deve essere un numero intero (0 = no, 1 = sì)")
        reg_param[input_el.nome] = temp_val
    return reg_param

def check_ubicazione(nome: str) -> dict:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT idUbicazione, nome, citta, provincia, via, fissa, orario, attiva
                FROM tbubicazione
                WHERE nome={nome};""")
    data_row = cur.fetchone()
    cur.close()
    return data_row is not None