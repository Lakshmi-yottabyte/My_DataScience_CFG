from flask import Flask, jsonify, request



app = Flask(__name__) # this is the start point of application - intialise the application


@app.route("/") # define the route for the home page. it find endpoint to python function.
def home():
    return "Welcome everyone, well done this is your first Flask App"



@app.route("/hello", methods=["GET"]) # define the route for the hello page. it find endpoint to python function.
def hello():
    name = request.args.get('name', 'there').capitalize() # get the name parameter from the query string, default to 'there' if not provided
    return f"Hello {name}"



@app.route("/getdata")
def getdata():
    data={"name":"Alan", "age":40}
    return jsonify(data)
   


# example of post requets, assign automatic unique id to each user, and store users in a list.
users=[] 
@app.route('/add_user', methods=['POST'])

def add_user():

    data = request.get_json() # post request needs Json to post data to the server, get the data from the request body and parse it as JSON

    name = data.get('name', 'Unknown')

    age = data.get('age', 'Unknown')

    user_id = len(users) +1

    users.append({'id': user_id, 'name': name, 'age': age})

    print(users)

    return jsonify({'message': f'User {name} added', 'age': age})


@app.route('/users', methods=['GET'])

def get_users():

    return jsonify({'users': users})


# get and post requests can be used together to create a simple API for managing users. 

# The /add_user endpoint allows you to add a new user by sending a POST request with 

# a JSON payload containing the user's name and age. 

# The /users endpoint allows you to retrieve the list of all users by sending a GET request.

@app.route('/users/<name>', methods=['GET',"POST"])

def get_user(name):

    if request.method == 'POST':

        data = request.get_json()

        #check if the user already exists update the age if the user already exists, otherwise add a new user        

        for user in users:

            if user['name'].lower() == name.lower():

                print(f"Updating user: {name}")

                user['age'] = data.get('age', user['age'])

                return jsonify({'message': f'User {name} updated', 'age': user['age']})

        # If the user does not exist, add a new user    

        user_id = len(users) +1 # Assign a unique ID based on the current number of users

        users.append({'id': user_id, 'name': name, 'age': data.get('age', 'Unknown')}) # Add the new user to the list

        return jsonify({'message': f'User {name.capitalize()} added', 'age': data.get('age', 'Unknown')}) 

    

    elif request.method == 'GET': # Search for the user by name and return their information if found

        for user in users: # Iterate through the list of users to find a match based on the name (case-insensitive)

            if user['name'].lower() == name.lower(): # If a match is found, return the user's information as a JSON response

                return jsonify(user) # If no match is found after iterating through the list, return a 404 response indicating that the user was not found

        return jsonify({'message': 'User not found'}), 404






if __name__=='__main__':
    app.run(debug=True) # run the application in debug mode