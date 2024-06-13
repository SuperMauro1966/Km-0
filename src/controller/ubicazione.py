from .db.db import ritorna_connessione
from controller.user import ottieni_utente

def inserimento_ubicazione(dati_ubicazione: dict) -> None:
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name(dati_ubicazione['nome']):
        dati_ubicazione['nome'] = input("Nome già usato, reinseriscine un altro: ") 
    cur.execute(f"""INSERT INTO tbubicazione (nome, citta, provincia, via, fissa, orario, attiva) 
                VALUES (
                '{dati_ubicazione['nome']}',
                '{dati_ubicazione['citta']}', 
                '{dati_ubicazione['provincia']}', 
                '{dati_ubicazione['via']}', 
                 {dati_ubicazione['fissa']}, 
                '{dati_ubicazione['orario']}', 
                 {dati_ubicazione['attivo']});""")
    cur.execute(f"SELECT idUbicazione FROM tbubicazione WHERE nome='{dati_ubicazione['nome']}';")
    idUbi = cur.fetchone()[0]
    cur.execute(f"INSERT INTO tbsistabiliscein (idVenditore, idUbicazione) VALUES ({current_user.id}, {idUbi});")
    conn.commit()
    cur.close()
    print("Ubicazione inserita con successo!")
    print()

def modifica_ubicazione(dati_ubicazione: dict, nome: str) -> None:
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name(dati_ubicazione['nome']):
        dati_ubicazione['nome'] = input("Nome già usato, reinseriscine un altro: ")
    cur.execute(f"""UPDATE tbubicazione SET 
                nome='{dati_ubicazione['nome']}',
                citta='{dati_ubicazione['citta']}',
                provincia='{dati_ubicazione['provincia']}',
                via='{dati_ubicazione['via']}',
                fissa={dati_ubicazione['fissa']},
                orario='{dati_ubicazione['orario']}',
                attiva={dati_ubicazione['attivo']}
                WHERE nome='{nome}';""")
    conn.commit()
    cur.close()
    print("Ubicazione aggiornata con successo!")
    print()

def elimina_ubicazione(nome: str) -> None: 
    current_user = ottieni_utente()
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idUbicazione FROM tbsistabiliscein WHERE idVenditore={current_user.id};")
    row = cur.fetchone()
    for i in range(len(row)):
        cur.execute(f"""DELETE FROM tbubicazione 
                    WHERE nome='{nome}' AND idUbicazione={row[i]};""")
    if row is not None:
        for i in range(len(row)):
            cur.execute(f"DELETE FROM tbsistabiliscein WHERE idVenditore={current_user.id} AND idUbicazione={row[i]};")
        print("Ubicazione eliminata con successo!")
    else:
        print("L'ubicazione non è stata eliminata correttamente, riprova.")
    conn.commit()
    cur.close()
    print()
    
def mostra_ubicazione(nome: str) -> None:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT nome, citta, provincia, via, fissa, orario, attiva FROM tbubicazione 
                WHERE nome='{nome}';""")
    dati = cur.fetchone()
    cur.close()
    print(f"nome: {dati['nome']}")
    print(f"città: {dati['citta']}")
    print(f"provincia: {dati['provincia']}")
    print(f"indirizzo: {dati['via']}")
    if dati['fissa'] == 0:
        print("fissa: no")
    else:
        print("fissa: sì")
    print(f"orario di apertura: {dati['orario']}")
    if dati['attiva'] == 0:
        print("attiva: no")
    else:
        print("attiva: sì")

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