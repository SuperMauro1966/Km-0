from collections import namedtuple
# verificare la pwd e l'email.

_InputField = namedtuple('_InputField', ['nome', 'etichetta', 'default', 'conv_func'])
_param_idCredential = [
    _InputField ('email', 'email', '', None), 
    _InputField ('password', 'password', '', None),
    _InputField ('codice_fiscale', 'codice fiscale', '', None),
    _InputField ('telefono', 'numero di telefono', '', None)
]

def _convert_to_int(x: str) -> int:
    try:
        return int(x)
    except ValueError:
         print("Il campo deve essere un numero intero, non una stringa")

def ottieni_dati() -> dict:
    """
    permette all'utente di inserire i campi per registrarsi, differenziandolo tra cliente e venditore, in caso di inserimento di una mail già usata comparirà un messaggio di errore
    email: email
    password: password
    codice_fiscale: codice fiscale
    telefono: numero di telefono
    ruolo: indicare se si è clienti o venditori
    citta: città di residenza
    provincia: provincia di residenza
    via: via di residenza
    nome: nome
    cognome: cognome
    ragione_sociale: ragione sociale
    sitoweb: sito web del venditore
    partitaIVA: partita IVA
    """

    dati_cliente_venditore = _input_dati(_param_idCredential)

    conf_psw = input("Digita un'altra volta la password per confermarla: ")
    while conf_psw != dati_cliente_venditore['password']:
        conf_psw = input("Le password non coincidono, reinserirla: ")
    

    print("Inserrisci il ruolo")
    print("V o v per venditore")
    print("C o c per cliente")
    dati_cliente_venditore['ruolo'] = input()
    while dati_cliente_venditore['ruolo'].upper() not in ['C', 'V'] :
            dati_cliente_venditore['ruolo'] = input("Valore non valido (C/c/V/v consentiti): ")
    
    if dati_cliente_venditore['ruolo'].upper() == 'C':
        client_param = [
            _InputField ('nome', 'nome', '', None), 
            _InputField ('cognome', 'cognome', '', None),
            _InputField ('citta', 'città', '', None),
            _InputField ('provincia', 'provincia', '', None),
            _InputField ('via', 'indirizzo di casa', '', None)
        ]
        dati_aggiuntivi = _input_dati(client_param)
    else:
        seller_param = [
            _InputField ('ragione_sociale', 'ragione sociale', '', None),
            _InputField ('sitoweb', 'sito web', '', None),
            _InputField ('partitaIVA', 'partita IVA', None, _convert_to_int)
        ]
        dati_aggiuntivi = _input_dati(seller_param)
        
    dati_cliente_venditore.update(dati_aggiuntivi)
    return dati_cliente_venditore

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