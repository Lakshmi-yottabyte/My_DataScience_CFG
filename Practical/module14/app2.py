from flask import Flask, request, jsonify

from db_2 import get_all_songs,insert_song

app = Flask(__name__)

@app.route('/')

def home():

    return "Welcome to the Music Library API! Use /songs to get all songs." 

 

@app.route('/songs', methods=['GET'])

def songs():

    songs = get_all_songs()

    return jsonify(songs)

 

 

@app.route('/songs', methods=['POST'])

def add_song():

    data = request.get_json()

    insert_song(

        artist_name=data.get('artist_name'),

        song_title=data.get('song_title'),

        genre=data.get('genre'),

        release_year=data.get('release_year'),

        duration_seconds=data.get('duration_seconds')

    )

    return jsonify({"message": "Song added successfully"}), 201

 

 

if __name__ == '__main__':

    app.run(debug=True)