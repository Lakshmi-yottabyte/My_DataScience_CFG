import mysql.connector

from config import DB_CONFIG_NO_DB

def insert_record(table, data):

    db = None

    cursor = None

    try:

        db = mysql.connector.connect(**DB_CONFIG_NO_DB, database="library_1_db")

        cursor = db.cursor()

        if table == 'books':

            query = """

            INSERT INTO books (title, author_name, pub_year, genre, available)

            VALUES (%s, %s, %s, %s, %s)

            """

        elif table == 'authors':

            query = """

            INSERT INTO authors (name)

            VALUES (%s)

            """

        elif table == 'borrowers':

            query = """

            INSERT INTO borrowers (name)

            VALUES (%s)

            """

        else:

            raise ValueError(f"Unknown table: {table}")

        

        cursor.execute(query, data)

        db.commit() 

        print(f"Inserted into {table}. Last ID: {cursor.lastrowid}")

    except mysql.connector.Error as err:

        print(f"Insertion error: {err}")

    finally:

        if cursor:

            cursor.close()

        if db and db.is_connected():

            db.close()

if __name__ == "__main__":

    book_data = ("The Invisible Man", "H. G. Wells", 1897, "Sci-Fi", True)

    insert_record('books', book_data)

    #insert_record('borrowers', ('Sara',))