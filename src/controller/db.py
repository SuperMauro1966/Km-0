_conn = None

def apri_connessione():
    global _conn
    try:
            _conn=mariadb.connect(
                user="root",
                password="1234",
                host="127.0.0.1",
                port=3306,
                database="km-0"
            )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")
        sys.exit(1)

def chiudi_connessione():
    _conn.close()

def ritorna_connessione():
     return _conn