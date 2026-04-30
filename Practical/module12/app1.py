from flask import Flask, request, jsonify

from db import get_all_songs

app = Flask(__name__)

@app.route('/')

def home():

    return "Welcome to the Music Library API! Use /songs to get all songs."

@app.route('/songs', methods=['GET'])

def songs():

    songs = get_all_songs()

    return jsonify(songs)

 

 

if __name__ == '__main__':

    app.run(debug=True)