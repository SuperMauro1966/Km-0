from controller import db
from view import input_ubicazione as inp_ubi
def inserimento_ubicazione():
    conn = db.ritorna_connessione()
    cur = conn.cursor()
    dati_ubicazione = inp_ubi.dati_ubicazione()
    cur.execute(f"INSERT INTO tbubicazione (`citta`, `provincia`, `via`, `fissa`, `orario`, `attiva`) 
                VALUES (
                '{dati_ubicazione['citta']}', 
                '{dati_ubicazione['provincia']}', 
                '{dati_ubicazione['via']}', 
                 {dati_ubicazione['fissa']}, 
                '{dati_ubicazione['orario']}', 
                 {dati_ubicazione['attivo']});")
    cur.close() 
def modifica_ubicazione():
    pass
def elimina_ubicazione():
    pass
def mostra_ubicazione():
    pass