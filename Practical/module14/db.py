from config_1 import get_db_connection

def get_all_songs():

    connection = get_db_connection() # create the connnection - function in congig_1.py and then to db in dbeabver

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM songs")

    songs = cursor.fetchall()

    print(songs)

    cursor.close()

    connection.close()

    return songs