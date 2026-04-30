import mysql.connector

from config import DB_CONFIG_NO_DB

# Create a function called get_all_books which retrieves all books, 

# allow users to call this function with an optional LIMIT.

def get_all_books(limit=None):

    

    try:

        db = mysql.connector.connect(**DB_CONFIG_NO_DB, database="library_1_db")

        cursor = db.cursor(dictionary=True)

        

        query = "SELECT * FROM books"

        if limit:

            query += f" LIMIT {limit}"

            

        cursor.execute(query)

        results = cursor.fetchall() 

     

        return results

    except mysql.connector.Error as err:

        print(f"Error: {err}")

    finally:

        if 'db' in locals(): db.close()

def search_books_1(search_term=None, genre=None, pub_year=None, available=None):

    db = None

    cursor = None

    try:

        db = mysql.connector.connect(**DB_CONFIG_NO_DB, database="library_1_db")

        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM books WHERE 1=1"

        params = []

        if search_term:

            query += " AND title LIKE %s"

            like_term = f"%{search_term}%"

            params.append(like_term)

        if genre:

            query += " AND genre = %s"

            params.append(genre)

        if pub_year:

            query += " AND pub_year = %s"

            params.append(pub_year)

        if available is not None:

            query += " AND available = %s"

            params.append(available)

        cursor.execute(query, tuple(params))

        return cursor.fetchall()

    except mysql.connector.Error as err:

        print(f"Search error: {err}")

        return []

    finally:

        if cursor:

            cursor.close()

        if db and db.is_connected():

            db.close()

# Create a search_books function which allows a user to search books 

# using either a search term, by genre, by publication year, or by 

# availability. 

def search_books(genre=None):

    try:

        db = mysql.connector.connect(**DB_CONFIG_NO_DB, database="library_1_db")

        cursor = db.cursor(dictionary=True)

        

        if genre:

            query = "SELECT * FROM books WHERE genre = %s"

            cursor.execute(query, (genre,))

            return cursor.fetchall()

            

    except mysql.connector.Error as err:

        print(f"Search error: {err}")

    finally:

        if 'db' in locals(): db.close()

if __name__ == "__main__":

    # print("All Books:")

    # books = get_all_books()

    # for b in books: 

    #     print(b)

    sci_fi_books = search_books(genre='Sci-Fi')

    for b in sci_fi_books: 

        print(b)

    # sci_fi_books = search_books_1(search_term='the',genre='Sci-Fi')

    # for b in sci_fi_books: 

    #     print(b)