from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/") # define the route for the home page. it find endpoint to python function.
def greet():
    return "Welcome, What can I do for you?"





if __name__=='__main__':
    app.run(debug=True) # run the application in debug mode