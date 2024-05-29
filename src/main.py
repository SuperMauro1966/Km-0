import mariadb
import sys

try:
    conn=mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="km-0"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

while True:
    email=input("digita l'email: ")
    password=input("digita la password: ")

    cur=conn.cursor()
    cur.execute(f"SELECT COUNT(idCredential) FROM tbcredential WHERE email='{email}' AND pswd='{password}';")
    row=cur.fetchone()
    if (row[0]==1):
            print("sei stato autenticato correttamente!")
            cur.close()
            conn.close()
            break
    else:
        print("\n")