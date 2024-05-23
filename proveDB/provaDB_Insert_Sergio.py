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
cur.execute("INSERT INTO employees (first_name, last_name) VALUES ('Debora', 'Parisi');")
conn.commit()
<<<<<<< HEAD
cur.execute("SELECT first_name,last_name FROM classe;")
=======
cur.execute("SELECT first_name,last_name FROM employees;")
>>>>>>> 38b1889dcdd0ca88ae01cc13e25c6bb6a9b16d1b

for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")