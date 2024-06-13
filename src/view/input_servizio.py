from collections import namedtuple
from controller.db.db import ritorna_connessione
from controller.servizio import inserimento_servizio, modifica_servizio, elimina_servizio, mostra_servizio
from .input_utils import InputField, input_dati


_param = [
        InputField('nome', 'nome servizio', None, None), 
        InputField('descrizione', 'descrizione del servizio', None, None),
        InputField('prezzo', 'prezzo', None, float),
        InputField('quantita', 'quantità', None, None)
    ]

def inserimento_dati() -> None:
    dict = input_dati(_param)
    inserimento_servizio(dict)

def modifica_dati() -> None:
    nome = ''
    while not _check_servizio(nome):
        nome = input("digita il nome dell'ubicazione da modificare: ")
    dict = input_dati()
    modifica_servizio(dict, nome)

def elimina_dati() -> None:
    nome = ''
    while not _check_servizio(nome):
        nome = input("digita il nome dell'ubicazione da eliminare: ")
    elimina_servizio(nome)

def mostra_dati() -> None:
    nome = ''
    while not _check_servizio(nome):
        nome = input("digita il nome del servizio da mostrare: ") 
    mostra_servizio(nome)    

def _check_servizio(nome: str) -> bool:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT idServizio, nome, descrizione
                FROM tbservizio
                WHERE nome='{nome}';""")
    data_row = cur.fetchone()
    cur.close()
    return data_row is not None