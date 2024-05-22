import sys

import mariadb

try:
    conn=mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="km-0"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB platform: {e}")
    sys.exit(1)


email=input("Inserisci l'e-mail: ")
pwd=input("Inserisci la password: ")

cur=conn.cursor()
cur.execute(
    f"SELECT COUNT(id) FROM account WHERE email='{email}' AND password=PASSWORD('{pwd}');")

count=cur.fetchone()[0]
conn.commit()

# Verifica se c'è almeno una corrispondenza
if count==1:
    print("Accesso consentito.")
else:
    print("Nome utente o password errati.")

