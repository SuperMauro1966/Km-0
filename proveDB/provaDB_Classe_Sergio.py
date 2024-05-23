import mariadb
import sys

listaN=[]
listaC=[]
n=int(input("digita la quantità di alunni da inserire: "))
while n<0:
    n=int(input("ERRORE! Valore non valido, reinserirlo: "))

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
for i in range(n):
    listaN.append(input(f"digita il nome del {i+1}° alunno: "))
    listaC.append(input(f"digita il cognome del {i+1}° alunno: "))
    print("\n")

    cur.execute(f"INSERT INTO employees (first_name, last_name) VALUES ('{listaN[i]}', '{listaC[i]}');")
    conn.commit()

cur.execute("SELECT first_name,last_name FROM employees ORDER BY last_name;")
print("\n")

for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")