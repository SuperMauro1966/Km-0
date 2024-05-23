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
cur.execute("UPDATE employees SET dataN='2006-07-20' WHERE first_name='Sergio';")
cur.execute("UPDATE employees SET dataN='2006-06-21' WHERE first_name='Gabriele';")
cur.execute("SELECT first_name,last_name,dataN FROM employees;")

for (first_name, last_name, dataN) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}, Date of birth: {dataN}")