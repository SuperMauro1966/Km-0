from controller.db.db import ritorna_connessione
from controller.eventi import inserimento_evento, modifica_evento, elimina_evento, mostra_evento
from .input_utils import InputField, input_dati


_param = [
        InputField('nome', 'nome evento', None, None), 
        InputField('descrizione', 'descrizione del evento', None, None),
        InputField('dataInizio', 'Data di inizio', None, float),
        InputField('dataFine', 'Data di fine', None, None),
        InputField('condiviso', 'condiviso', None, None)
    ]

def inserimento_dati() -> None:
    dict = input_dati(_param)
    inserimento_evento(dict)

def modifica_dati() -> None:
    nome = ''
    while not _check_evento(nome):
        nome = input("digita il nome dell'ubicazione da modificare: ")
    dict = input_dati()
    modifica_evento(dict, nome)

def elimina_dati() -> None:
    nome = ''
    while not _check_evento(nome):
        nome = input("digita il nome dell'ubicazione da eliminare: ")
    elimina_evento(nome)

def mostra_dati() -> None:
    nome = ''
    while not _check_evento(nome):
        nome = input("digita il nome del servizio da mostrare: ") 
    mostra_evento(nome)    

def _check_evento(nome: str) -> bool:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT descrizione, dataInizio, dataFine, nome, condiviso
                FROM tbevento
                WHERE nome='{nome}';""")
    data_row = cur.fetchone()
    cur.close()
    return data_row is not None