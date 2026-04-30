import mysql.connector as connector

from config import DB_CONFIG_NO_DB

try:

    connection = connector.connect(**DB_CONFIG_NO_DB, db='library_1_db')

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""INSERT INTO books (title, author_name, pub_year, genre) 

                   VALUES (%s, %s, %s, %s);""",

                   ('The wizard of Oz', 'Frank Baum', 1900, 'Fiction'))

    book_id = cursor.lastrowid

    cursor.execute("""INSERT INTO borrowers (name) VALUES (%s)""", ('Frank',))

    borrower_id = cursor.lastrowid

    cursor.execute("INSERT INTO book_loans (book_id, borrower_id) VALUES (%s, %s)",

                    (book_id, borrower_id))

    

   

    connection.commit()

except connector.Error as err:

    print(f'Something went wrong: {err}')

    connection.rollback()

finally:

    if 'cursor' in locals():

        cursor.close()

    if 'connection' in locals():

        connection.close()