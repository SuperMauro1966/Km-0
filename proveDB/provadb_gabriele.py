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

cur=conn.cursor()
cur.execute(
    "SELECT first_name,last_name FROM employees;")

# Print Result-set
for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")
