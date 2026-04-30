import mysql.connector as connector
from config import DB_CONFIG

try:

    connection = connector.connect(**DB_CONFIG)

    cursor = connection.cursor(dictionary=True)

    price = "7"

    cursor.execute("SELECT name, price FROM menuitems WHERE price > %s;", (price,))

    #print(cursor.fetchall())

    record = cursor.fetchone()

    while record:

        print(record)

        record = cursor.fetchone()

except connector.Error as err:

    print(f'Something went wrong: {err}')

finally:

    if 'cursor' in locals():

        cursor.close()

    if 'connection' in locals():

        connection.close()