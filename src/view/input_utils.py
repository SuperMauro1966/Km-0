from collections import namedtuple
InputField = namedtuple('InputField', ['nome', 'etichetta', 'default', 'conv_func'])

def input_dati(fields: list[InputField]) -> dict:
    """
    Salva gli input del dizionario.
    """
    reg_param = {}

    for input_el in fields:
        while True:
            temp_val = input(f"{input_el.etichetta}(default: {input_el.default}): ")
            if temp_val.strip() == '':
                if input_el.default is not None:
                    reg_param[input_el.nome] = input_el.default
                    break
                else:
                    print("È necessario specificare un valore")
            elif input_el.conv_func:
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
