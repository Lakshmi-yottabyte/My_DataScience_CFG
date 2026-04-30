import mysql.connector as connector

from config import DB_CONFIG

def test_connection():

    try:

        print("Attempting to connect")

        connection = connector.connect(**DB_CONFIG)

        if connection.is_connected():

            print("Connection is successful!")

        else:

            print("Connection failed!")

        cursor = connection.cursor()    

    except connector.Error as err:

        print(f'Something went wrong: {err}')

    finally:

        if 'cursor' in locals():

            cursor.close()

        if 'connection' in locals():

            connection.close()

if __name__ == '__main__':

    test_connection()