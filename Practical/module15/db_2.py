from config_2 import get_db_connection

def get_all_songs():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM songs")

    songs = cursor.fetchall()

    print(songs)

    cursor.close()

    connection.close()

    return songs

def insert_song(artist_name, song_title, genre, release_year, duration_seconds):

    connection = get_db_connection()

    cursor = connection.cursor()

    # Now insert the song with the obtained artist_id

    cursor.execute(

        "INSERT INTO songs (artist_name, song_title, genre, release_year, duration_seconds) VALUES (%s, %s, %s, %s, %s)",

        (artist_name, song_title, genre, release_year, duration_seconds)

    )

       

    connection.commit()

    cursor.close()

    connection.close()