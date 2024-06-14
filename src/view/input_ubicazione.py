from collections import namedtuple
from controller.db.db import ritorna_connessione
from controller.ubicazione import inserimento_ubicazione, modifica_ubicazione, elimina_ubicazione, mostra_ubicazione
from .input_utils import InputField, input_dati


_param = [
        InputField('nome', 'nome ubicazione', None, None), 
        InputField('citta', 'città', None, None),
        InputField('provincia', 'provincia', None, None),
        InputField('via', 'via', None, None),
        InputField('fissa', 'ubicazione fissa', None, bool),
        InputField('orario', "orario di apertura dell'ubicazione", None, None),
        InputField('attivo', 'ubicazione attiva', 0, bool)
    ]

def inserimento_dati() -> None:
    dict = input_dati(_param)
    inserimento_ubicazione(dict)

def modifica_dati() -> None:
    nome = ''
    while not _check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da modificare: ")
    dict = input_dati()
    modifica_ubicazione(dict, nome)

def elimina_dati() -> None:
    nome = ''
    while not _check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da eliminare: ")
    elimina_ubicazione(nome)

def mostra_dati() -> None:
    nome = ''
    while not _check_ubicazione(nome):
        nome = input("digita il nome dell'ubicazione da mostrare: ") 
    mostra_ubicazione(nome)    

def _check_ubicazione(nome: str) -> bool:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT idUbicazione, nome, citta, provincia, via, fissa, orario, attiva
                FROM tbubicazione
                WHERE nome='{nome}';""")
    data_row = cur.fetchone()
    cur.close()
    return data_row is not None