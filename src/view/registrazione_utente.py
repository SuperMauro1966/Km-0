from controller import registrazione
from .input_utils import InputField, input_dati
# verificare la pwd e l'email.

_param_idCredential = [
    InputField ('email', 'email', None, None), 
    InputField ('password', 'password', None, None),
    InputField ('codice_fiscale', 'codice fiscale', None, None),
    InputField ('telefono', 'numero di telefono', None, None)
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

    dati_cliente_venditore = input_dati(_param_idCredential)

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
            InputField ('nome', 'nome', None, None), 
            InputField ('cognome', 'cognome', None, None),
            InputField ('citta', 'città', None, None),
            InputField ('provincia', 'provincia', None, None),
            InputField ('via', 'indirizzo di casa', None, None)
        ]
        dati_aggiuntivi = input_dati(client_param)
    else:
        seller_param = [
            InputField ('ragione_sociale', 'ragione sociale', None, None),
            InputField ('sitoweb', 'sito web', None, None),
            InputField ('partitaIVA', 'partita IVA', None, None)
        ]
        dati_aggiuntivi = input_dati(seller_param)
    
    dati_cliente_venditore.update(dati_aggiuntivi)
    status, msg = registrazione.registrati(dati_cliente_venditore)
    print(msg)