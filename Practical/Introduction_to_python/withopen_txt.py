#write a program to create a file called songlist.txt and write some song names in it. Then ask the user to enter a song name and append it to the file. Finally, read the contents of the file and print it.
with open("songlist.txt", "w") as file:
    file.write("song1")
    file.write("\nsong2")
    file.write("\nsong3")
songname=input("enter a song name: ")
with open("songlist.txt", "a") as file:
    file.write(f"\n{songname}")
with open("songlist.txt", "r") as file:
    print(file.read())

