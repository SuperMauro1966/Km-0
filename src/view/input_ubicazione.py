
def  dati_ubicazione() -> dict:
    _param = ['citta', 'provincia', 'via', 'fissa', 'orario', 'attiva']
    reg_param = {}
    for input_el in _param:
        temp_val = None
        while temp_val == '' or temp_val is None or temp_val.strip() == '':
            temp_val = input(f"Inserire campo {input_el.etichetta}: ")
        reg_param[input_el.nome] = temp_val
    return reg_param

    