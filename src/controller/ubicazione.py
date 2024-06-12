from .db.db import ritorna_connessione

def inserimento_ubicazione(dati_ubicazione):
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO tbubicazione (nome, citta, provincia, via, fissa, orario, attiva) 
                VALUES (
                '{dati_ubicazione['nome']}',
                '{dati_ubicazione['citta']}', 
                '{dati_ubicazione['provincia']}', 
                '{dati_ubicazione['via']}', 
                 {dati_ubicazione['fissa']}, 
                '{dati_ubicazione['orario']}', 
                 {dati_ubicazione['attivo']});""")
    cur.close() 

def modifica_ubicazione(dati_ubicazione,nome) -> None:
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"""UPDATE tbubicazione
                SET 
                nome='{dati_ubicazione['nome']}',
                citta='{dati_ubicazione['citta']}',
                provincia='{dati_ubicazione['provincia']}',
                via='{dati_ubicazione['via']}',
                fissa='{dati_ubicazione['fissa']}',
                orario='{dati_ubicazione['orario']}',
                attivo={dati_ubicazione['attivo']}
                WHERE nome='{nome}';""")
    cur.close()

def elimina_ubicazione(nome) -> None: 
    conn = ritorna_connessione()
    cur = conn.cursor()
    cur.execute(f"""DELETE FROM tbubicazione 
                WHERE nome='{nome}';""")
    cur.close()
    
def mostra_ubicazione():
    pass