from .db.db import ritorna_connessione

def inserimento_servizio(dati_servizio: dict) -> None:
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO tbservizio (nome, descrizione) 
                VALUES (
                '{dati_servizio['nome']}',
                '{dati_servizio['descrizione']}';""")
    cur.execute(f"""INSERT INTO tboffre (idVenditore, idServizio, prezzo, quantita)
                VALUES (
                {id},
                {id},
                {dati_servizio['prezzo']},
                {dati_servizio['quantita']});""")
    conn.commit()
    cur.close() 

def modifica_ubicazione() -> None:
    pass

def elimina_ubicazione() -> None: 
    pass
    
def mostra_ubicazione() -> dict:
    pass