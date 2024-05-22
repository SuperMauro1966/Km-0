import mariadb
import sys

try:
    conn=mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="employees"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur=conn.cursor()
cur.execute("ALTER TABLE employees ADD dataN DATE NOT NULL;")
print("Data di nascita aggiunta come campo nel database")