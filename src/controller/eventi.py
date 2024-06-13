from .db.db import ritorna_connessione
from controller.user import ottieni_utente

def inserimento_evento(dati_servizio: dict) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name(dati_servizio['nome']):
        dati_servizio['nome'] = input("Nome già usato, reinseriscine un altro: ") 
    cur.execute(f"""INSERT INTO tbevento (descrizione, dataInizio, dataFine, nome, condiviso) 
                VALUES (
                'Fiera del baccala a San Giorgio di Piano', 
                '2024-06-13 16:00:00', 
                '2024-06-13 00:00:00', 
                'Fiera del Baccalà', 
                1 );""")
    cur.execute(f"SELECT idEvento FROM tbevento WHERE nome='{dati_servizio['nome']}';")
    idEvento = cur.fetchone()[0]
    cur.execute(f"""INSERT INTO tbcrea (idVenditore, idEvento) 
                VALUES ({current_user.id}, {idEvento});""")
    conn.commit()
    cur.close()
    print("Evento creato con successo!")
    print()

def modifica_evento(dati_servizio: dict, nome: str) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name(dati_servizio['nome']):
        dati_servizio['nome'] = input("Nome già usato, reinseriscine un altro: ")
    cur.execute(f"SELECT idEvento FROM tbcrea WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    if row is not None:
        for i in range(len(row)):    
            cur.execute(f"""UPDATE tbevento SET 
                        
                        descrizione='{dati_servizio['descrizione']}',
                        dataInizio='',
                        dataFine='',
                        nome='{dati_servizio['nome']}',
                        condiviso=
                        WHERE nome='{nome}' AND idServizio={row[i]};""")
        conn.commit()
        cur.close()
        print("Servizio aggiornato con successo!")
        print()
    else:
        print("Il servizio non è stato aggiornato, riprova.")
        print()
        cur.close()

def elimina_evento() -> None: 
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idEvento FROM tbcrea WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    if row is not None:
        for i in range(len(row)):    
            cur.execute(f"DELETE FROM tbevento WHERE idServizio={row[i]};")
            cur.execute(f"DELETE FROM tbcrea WHERE idServizio={row[i]} AND idVenditore={current_user.id};")
        conn.commit()
        print("Servizio eliminato con successo!")
    else:
        print("Il servizio non è stato eliminato, riprova.")
    print()
    cur.close()
    
def mostra_evento(nome: str) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idServizio FROM tboffre WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    cur.close()
    if row is not None:
        cur = conn.cursor(dictionary = True)
        for i in range(len(row)):    
            cur.execute(f"""SELECT descrizione, dataInizio, dataFine, nome, condiviso 
                        FROM tbevento
                        WHERE idEvento={row[i]} AND nome='{nome}';""")
            data_row_evento = cur.fetchone()
            if data_row_evento is not None:
                break
        conn.commit()
        print(f"nome: {nome}")
        print(f"descrizione: {data_row_evento['descrizione']}")
        print(f"Data di inizio: {data_row_evento['dataInizio']}")
        print(f"Data di fine: {data_row_evento['dataFine']}")
        print(f"condiviso: {data_row_evento['condiviso']}")
    else:
        print("Impossibile mostrare il servizio.")
    print()
    cur.close()

def _check_name(nome: str) -> bool:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idEvento FROM tbcrea WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    if row is not None:
        for i in range(len(row)):
            cur.execute(f"SELECT nome FROM tbevento WHERE idEvento={row[i]} AND nome='{nome}';")
        data_row = cur.fetchone()
        cur.close()
        return data_row is not None
    else:
        cur.close()
        return None