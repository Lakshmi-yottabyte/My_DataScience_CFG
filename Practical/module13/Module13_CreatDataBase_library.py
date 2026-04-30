import mysql.connector as connector

from config import DB_CONFIG_NO_DB

from library_tables import tables

def create_library_system():

    try:

        connection = connector.connect(**DB_CONFIG_NO_DB)

        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS library_1_db;")

        cursor.execute("USE library_1_db;")

        print("Database library1_db has been created.")

        for table, statement in tables.items():

            cursor.execute(statement)

            print(f"Table {table} is created")

 

    except connector.Error as err:

        print(f'Something went wrong: {err}')

    finally:

        if 'cursor' in locals():

            cursor.close()

        if 'connection' in locals():

            connection.close()

if __name__ == "__main__":

    create_library_system()