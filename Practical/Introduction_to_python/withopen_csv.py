#create a csv file with album details and write to it, then read the file and print its contents
import csv

with open("albums.csv", mode="w", newline="") as file:  #create a csv file and with 'write' mode and new line to avoid blank lines
    csv_writer=csv.writer(file)                         # create teh write object
    csv_writer.writerow(["Title", "Artist", "Release"]) # create header row  by writing all the rows at once

#inputs from user for album
title = input("Enter album title:  ")   
artist = input("Enter artist name:  ")  
release = input("Entter release year:  ")   



#append the detials to csv file using mode = 'a'
with open("albums.csv", mode='a', newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow([title, artist, release])

# read the file  and print the content
with open("albums.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    print(file.read())
    
