from .db.db import ritorna_connessione
from controller.user import ottieni_utente

def inserimento_servizio(dati_servizio: dict) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name(dati_servizio['nome']):
        dati_servizio['nome'] = input("Nome già usato, reinseriscine un altro: ") 
    cur.execute(f"""INSERT INTO tbservizio (nome, descrizione) 
                VALUES (
                '{dati_servizio['nome']}',
                '{dati_servizio['descrizione']}';""")
    cur.execute(f"SELECT idServizio FROM tbservizio WHERE nome='{dati_servizio['nome']}';")
    idServ = cur.fetchone()[0]
    cur.execute(f"""INSERT INTO tboffre (idVenditore, idServizio, prezzo, quantita) 
                VALUES ({current_user.id}, {idServ}, {dati_servizio['prezzo']}, '{dati_servizio['quantita']}');""")
    conn.commit()
    cur.close()
    print("Servizio inserito con successo!")
    print()

def modifica_servizio(dati_servizio: dict, nome: str) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name(dati_servizio['nome']):
        dati_servizio['nome'] = input("Nome già usato, reinseriscine un altro: ")
    cur.execute(f"SELECT idServizio FROM tboffre WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    if row is not None:
        for i in range(len(row)):    
            cur.execute(f"""UPDATE tbservizio SET 
                        nome='{dati_servizio['nome']}',
                        descrizione='{dati_servizio['descrizione']}',
                        WHERE nome='{nome}' AND idServizio={row[i]};""")
            cur.execute(f"UPDATE tboffre SET prezzo={dati_servizio['prezzo']}, quantita='{dati_servizio['quantita']}' WHERE idVenditore={current_user.id} AND idServizio={row[i]};")
        conn.commit()
        cur.close()
        print("Servizio aggiornato con successo!")
        print()
    else:
        print("Il servizio non è stato aggiornato, riprova.")
        print()
        cur.close()

def elimina_servizio(nome: str) -> None: 
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idServizio FROM tboffre WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    if row is not None:
        for i in range(len(row)):    
            cur.execute(f"DELETE FROM tbservizio WHERE idServizio={row[i]};")
            cur.execute(f"DELETE FROM tboffre WHERE idServizio={row[i]} AND idVenditore={current_user.id};")
        conn.commit()
        print("Servizio eliminato con successo!")
    else:
        print("Il servizio non è stato eliminato, riprova.")
    print()
    cur.close()
    
def mostra_servizio(nome: str) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idServizio FROM tboffre WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    cur.close()
    if row is not None:
        cur = conn.cursor(dictionary = True)
        for i in range(len(row)):    
            cur.execute(f"SELECT nome, descrizione FROM tbservizio WHERE idServizio={row[i]} AND nome={nome};")
            data_row_servizio = cur.fetchone()
            cur.execute(f"SELECT prezzo, quantita FROM tboffre WHERE idServizio={row[i]} AND idVenditore={current_user.id};")
            data_row_offre = cur.fetchone()
            if data_row_servizio is not None and data_row_offre is not None:
                break
        conn.commit()
        print(f"nome: {nome}")
        print(f"descrizione: {data_row_servizio['descrizione']}")
        print(f"prezzo: {data_row_offre['prezzo']}")
        print(f"quantità: {data_row_offre['quantita']}")
    else:
        print("Impossibile mostrare il servizio.")
    print()
    cur.close()

def _check_name(nome: str) -> bool:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idUbicazione FROM tbsistabiliscein WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    if row is not None:
        for i in range(len(row)):
            cur.execute(f"SELECT nome FROM tbubicazione WHERE idUbicazione={row[i]} AND nome='{nome}';")
        data_row = cur.fetchone()
        cur.close()
        return data_row is not None
    else:
        cur.close()
        return None