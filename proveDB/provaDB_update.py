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


day_DOB=input("Inserisci il giorno di nascita: ")
month_DOB=input("Inserisci il mese di nascita: ")
year_DOB=input("Inserisci anno di nascita: ")

cur=conn.cursor()
cur.execute(
    f"UPDATE `employees`.`employees` SET `DOB`='{year_DOB}-{month_DOB}-{day_DOB}' WHERE  `first_name`='Mattia' AND `last_name`='Rubbi' AND `DOB`='0000-00-00'")    
conn.commit()
