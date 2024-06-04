# verificare la pwd e l'email


def ottieni_dati():
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
    first_name: nome
    last_name: cognome
    ragione_sociale: ragione sociale
    sitoweb: sito web del venditore
    partitaIVA: partita IVA
    """
    param = ['email', 'password', 'codice_fiscale', 'telefono']
    dati_cliente_venditore = _input_dati(param)
    dati_cliente_venditore['ruolo'] = input("""Inserisci il ruolo:
                                V o v per venditore
                                C o c per cliente""")
    while dati_cliente_venditore['ruolo'].upper() not in ['C', 'V'] :
            dati_cliente_venditore['ruolo'] = input("Valore non valido(c/v consentiti)")
    if dati_cliente_venditore['ruolo'].upper() == 'C':
        client_param = ['nome', 'cognome', 'citta', 'provincia', 'via']
        dati_aggiuntivi = _input_dati(client_param)
    else:
        seller_param = ['ragione_sociale', 'sitoweb', 'partitaIVA']
        dati_aggiuntivi = _input_dati(seller_param)
    dati_cliente_venditore.update(dati_aggiuntivi)
    return dati_cliente_venditore

def _input_dati(field: list) -> dict:
    reg_param = {}
    for label in field:
        reg_param[label] = input(f"Inserire campo {label}: ")
    return reg_param    
