from collections import namedtuple
from controller import registrazione
# verificare la pwd e l'email.

_InputField = namedtuple('_InputField', ['nome', 'etichetta', 'default', 'conv_func'])
_param_idCredential = [
    _InputField ('email', 'email', None, None), 
    _InputField ('password', 'password', None, None),
    _InputField ('codice_fiscale', 'codice fiscale', None, None),
    _InputField ('telefono', 'numero di telefono', None, None)
]

def ottieni_dati() -> None:
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
            _InputField ('nome', 'nome', None, None), 
            _InputField ('cognome', 'cognome', None, None),
            _InputField ('citta', 'città', None, None),
            _InputField ('provincia', 'provincia', None, None),
            _InputField ('via', 'indirizzo di casa', None, None)
        ]
        dati_aggiuntivi = _input_dati(client_param)
    else:
        seller_param = [
            _InputField ('ragione_sociale', 'ragione sociale', None, None),
            _InputField ('sitoweb', 'sito web', None, None),
            _InputField ('partitaIVA', 'partita IVA', None, None)
        ]
        dati_aggiuntivi = _input_dati(seller_param)
    
    dati_cliente_venditore.update(dati_aggiuntivi)
    status, msg = registrazione.registrati(dati_cliente_venditore)
    print(msg)

def _input_dati(fields: list[_InputField]) -> dict:
    """
    Salva gli input del dizionario.
    """
    reg_param = {}

    for input_el in fields:
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