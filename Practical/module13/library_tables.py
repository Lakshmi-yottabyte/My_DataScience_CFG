tables = {
            "authors": """
                CREATE TABLE IF NOT EXISTS authors (
                    author_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                )""",
            "books": """
                CREATE TABLE IF NOT EXISTS books (
                    book_id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    author_name VARCHAR(255),
                    pub_year INT,
                    genre VARCHAR(100),
                    available BOOLEAN DEFAULT TRUE
                )""",
            "borrowers": """
                CREATE TABLE IF NOT EXISTS borrowers (
                    borrower_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                )""",
            "book_loans": """
                CREATE TABLE IF NOT EXISTS book_loans (
                    loan_id INT AUTO_INCREMENT PRIMARY KEY,
                    book_id INT,
                    borrower_id INT
                )"""
        }