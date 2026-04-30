import mysql.connector as connector

import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")  # Load environment variables from .env file

def get_db_connection():

    connection = connector.connect(

        host=os.getenv("DB_HOST"),

        user=os.getenv("DB_USER"),

        password=os.getenv("DB_PASSWORD"),

        database=os.getenv("DB_NAME")

    )   

    return connection