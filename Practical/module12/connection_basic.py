import mysql.connector as connector
from config import DB_CONFIG

connection = connector.connect(**DB_CONFIG)
cursor = connection.cursor()
print(cursor)
cursor.close()
connection.close()