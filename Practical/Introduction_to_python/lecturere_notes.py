import csv
import os

# Acitivity 2:
csv_file = "albums.csv"

# Check if the CSV file exists, if not create it with headers
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Artist", "Release Year"])  # header row

# 2: Ask the user to add a new album
title = input("Enter album title: ")
artist = input("Enter artist name: ")
release_year = input("Enter release year: ")

# 3: Append the new album to the CSV file
with open(csv_file, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([title, artist, release_year])

# 4: Display the albums
print("\nAlbums in your CSV file:")
with open(csv_file, "r", newline="") as file:
    reader = csv.reader(file)
    print(file.read())
    #for row in reader:
        #print("/ ".join(row))