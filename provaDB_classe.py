import sys

import mariadb

try:
    conn=mariadb.connect(
        user="root",
        password="1234",
        host="127.0.0.1",
        port=3306,
        database="employees"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB platform: {e}")
    sys.exit(1)

n_studenti=input("Inserisci il numero degli studenti: ")
i=0
for i in n_studenti:
    first_name=input("Inserisci il nome del {i+1} studenti: ")
    last_name=input("Inserisci il cognome: ")

    cur=conn.cursor()
    cur.execute(
        f"INSERT INTO `employees` (`first_name`, `last_name`) VALUES ('{first_name}', '{last_name}');")    
    conn.commit()

cur.execute(
    "SELECT first_name,last_name FROM employees;")

# Print Result-set
for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")


