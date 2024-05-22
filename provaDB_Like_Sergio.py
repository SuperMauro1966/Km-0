import mariadb
import sys
lett=input("digita le prime lettere per cercare un cognome: ")

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
cur.execute(f"SELECT first_name,last_name FROM employees WHERE last_name LIKE '{lett}%';")

for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")