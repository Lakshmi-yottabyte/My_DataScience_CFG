import mysql.connector as connector

def get_db_connection():

    return connector.connect(

        host="localhost",

        user="root",

        password="Prassu007",

        database="music_db"

    )