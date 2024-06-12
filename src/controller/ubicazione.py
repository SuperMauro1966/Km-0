from .db.db import ritorna_connessione
from controller.models.user import BaseUsers

def inserimento_ubicazione(dati_ubicazione: dict) -> None:
    conn = ritorna_connessione()
    cur = conn.cursor()
    while _check_name():
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
    conn.commit()
    cur.close() 

def modifica_ubicazione(dati_ubicazione: dict, nome: str) -> None:
    conn = ritorna_connessione()
    cur = conn.cursor()
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

def elimina_ubicazione(nome: str) -> None: 
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM tbubicazione 
                WHERE nome='{nome}';""")
    conn.commit()
    cur.close()
    
def mostra_ubicazione(nome: str) -> dict:
    conn = ritorna_connessione()
    cur = conn.cursor(dictionary = True)
    cur.execute(f"""SELECT nome, citta, provincia, via, fissa, orario, attiva FROM tbubicazione 
                WHERE nome='{nome}';""")
    dati=cur.fetchone()
    cur.close()
    return dati

def _check_name() -> bool:
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"SELECT idUbicazione FROM tbsistabiliscein WHERE idVenditore={BaseUsers.id};")
    row = cur.fetchone[0]
    cur.execute(f"SELECT nome FROM tbubicazione WHERE idUbicazione={row};")
    row = cur.fetchone()[0]
    cur.close()
    return row is not None