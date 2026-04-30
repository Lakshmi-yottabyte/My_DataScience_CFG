from flask import Flask, jsonify, request
books = []

app = Flask(__name__) # this is the start point of application - intialise the application
@app.route("/") # define the route for the home page. it find endpoint to python function.
def home():
    return "Welcome to book store"



@app.route("/add_books", methods=["POST"])
def add_books():
    data = request.get_json()
    title = data.get('title', 'unknown')
    author = data.get('author', 'unknown')
    book_id = len(books)+1
    books.append({'id': book_id, 'title' : title, 'author': author})
    print(books)
    return jsonify({'message': f'Book {title} added', 'author': author})

@app.route('/books', methods = ['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:id>', methods = ['GET'])
def get_book(id):
    for book in books:
        if int(book['id']) == int(id):
            return jsonify(book)
    return jsonify({'message': 'Book not found'})







if __name__=='__main__':
    app.run(debug=True) # run the application in debug mode