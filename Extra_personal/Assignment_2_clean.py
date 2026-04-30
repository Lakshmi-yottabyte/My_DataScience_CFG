# In this assignment, the user will be given the animation title and synopsis based on different metrics
#=============================================================================================================

#To install additonal libraries that are not included in Python as standard  - use 'pip install <module name>' command

# Additional module not used in this assignment
import math     # this is a mathematical module provides common functions such trignometric, functions, logarithms and pi
#===========================================================================
#                           Import and set-up
#===========================================================================
import requests #It is a thrid-party library. It is not part of python standard library. 
                #'request' is installed with pip install requests. It is for calling API
import json     # This module provides built-in support for working with JSON data
import csv      # This module reads and writes tabular data in CSV(Comma Separated Values) format.


#Base URL for API - trivia database
base_url = "https://api.jikan.moe/v4/top/anime?type=ona" # no API key need 

#Categories
categories = { 
    "1": "score", 
    "2": "rank", 
    "3": "popularity"
}

#===========================================================================
#                                   Functions
#===========================================================================
#Function to greet the user
def greet(name):
     print(f"Hello {name}, How are you?")

# Function to ask which category
def prompt_category():
    print("\nWhat list do you want to see from these categories?")
    for key, value in categories.items():
        print(f" {key}. {value}")
    while True: 
        choice = input("Choose a category (1, 2, or 3): ")
        if choice in categories:  
            print(f"You chose to filter by {categories[choice]}")
            return choice
        else:
            print("Invalid choice, please enter 1, 2, or 3")

# Function to find the highest score
def high_score(x):
    score_values=[]
    for anime in x:
        score_values.append(anime['score'])

    high_s = max(score_values)
    low_s = min(score_values)
    return (high_s, low_s)  

# Function to find the highest rank
def high_rank(x):
    rank_values=[]
    for anime in x:
        rank_values.append(anime['rank'])

    high_r = max(rank_values)
    low_r = min(rank_values)
    return (high_r, low_r)  

# Function to find the highest popularity
def high_popularity(x):
    popularity_values=[]
    for anime in x:
        popularity_values.append(anime['popularity'])

    high_p = max(popularity_values)
    low_p = min(popularity_values)
    return (high_p, low_p)  

#===========================================================================
#                       Registration and Greeting user
#===========================================================================

# Name validation
while True:
    n1 = input("Enter your name: ")
    name = n1.strip().capitalize()
    if name == "":
        print("Name cannot be empty, please enter your name")
        continue
    break

greet(name)


filename = f"{name}_results.csv"

#===========================================================================
#                       Get information form API
#===========================================================================
response=requests.get(base_url)

# Assign response to a vairable
info=response.json()
x = info["data"]

# Calling highest score function
high_s, low_s = high_score(x)

# Calling highest rank function
high_r, low_r = high_rank(x)

# Calling highest popularity function
high_p, low_p = high_popularity(x)

#===========================================================================
#                   Ask user choice based on category
#===========================================================================

choice = prompt_category()

#===========================================================================
#                           Category 1 - SCORE
#===========================================================================
# User inputs score and program checks if score is valid
if choice == "1":    
    while True:
        min_score = float(input(f"Enter min score between {low_s} and {high_s}: "))
        if min_score < low_s or min_score > high_s:
            print(f"Please enter a number between {low_s} and {high_s}")
            continue
        else: 
            break

    while True:
        max_score = float(input(f"Enter max score between {min_score} and {high_s}: "))
        if max_score < min_score or max_score > high_s:
            print(f"Please enter a number between {min_score} and {high_s}")
            continue
        else: 
            break
    top_list_score = int(input("How many top scored anime list you want to see:"))

#===========================================
# Open and write into a csv file
#===========================================

    with open (filename, mode="w", newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(["This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your score"])    
        csv_writer.writerow(["Your selected score range is  "])
        csv_writer.writerow(["Min score", "Max score"]) # Header
        csv_writer.writerow([min_score, max_score])     # Values
        csv_writer.writerow(["Title of Anime", "Score", "Synopsis"]) # Header


#===========================================
# For loop to get information the user wants
#===========================================

    # Using in-built function to sort list
    # lambda creates a small unnamed function in one line
    sorted_score = sorted(x, key=lambda anime: anime["score"])


    count = 0   # Initialise count 
    
    for anime in sorted_score:
        if min_score <= anime['score'] <= max_score:
            score = anime['score']
            title = anime ['title']
            synopsis = anime['synopsis']
            print(f"Title: {title} / Score: {score} / Synopsis: {synopsis}")  
        # Save information in a csv file
            with open (filename, mode= "a", newline = "") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, score, synopsis])
            
            count += 1 
            if count >= top_list_score:
                break
    if count == 0:
        print ("No records found")

#===========================================================================
#                        Category 2 - Rank
#===========================================================================
# User inputs rank and program check if the rank is valid
if choice == "2":    
    while True:
        min_rank = float(input(f"Enter min rank between {low_r} and {high_r}: "))
        if  min_rank < low_r or min_rank > high_r:
            print(f"Please enter a number between {low_r} and {high_r}")
            continue
        else: 
            break

    while True:
        max_rank = float(input(f"Enter max rank between {min_rank} and {high_r}: "))
        if max_rank < min_rank or max_rank > high_r:
            print(f"Please enter a number between {min_rank} and {high_r}")
            continue
        else: 
            break
    top_list_rank = int(input("How many top rank anime list you want to see:"))

#===========================================
# Open and write into a csv file
#===========================================   

    with open (filename, mode="w", newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(["This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your rank"])    
        csv_writer.writerow(["Your selected rank range is  "])
        csv_writer.writerow(["Min rank", "Max rank"]) # Header
        csv_writer.writerow([min_rank, max_rank])     # Values
        csv_writer.writerow(["Title of Anime", "Rank", "Synopsis"]) # Header


#===========================================
# For loop to get information the user wants 
#===========================================

    # Using in-built function to sort list
    # lambda creates a small unnamed function in one line
    sorted_rank = sorted(x, key=lambda anime: anime["rank"])

    count = 0   # Initialise count 
    
    for anime in sorted_rank:
        if min_rank <= anime['rank'] <= max_rank:
            rank = {anime['rank']}
            title = {anime ['title']}
            synopsis = {anime['synopsis']}
            if rank == None:
                print ("No records found")
            print(f"Title: {title} / Rank: {rank} / Synopsis: {synopsis}")  
        # Save information in a csv file
            with open (filename, mode= "a", newline = "") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, rank, synopsis])
            
            count += 1 
            if count >= top_list_rank:
                break
    if count == 0:
        print ("No records found")
#===========================================================================
#                        Category 3 - Popularity
#===========================================================================
# User inputs popularity and check if popularity is valid
if choice == "3":    
    while True:
        min_popularity = float(input(f"Enter min popularity between {low_p} and {high_p}: "))
        if  min_popularity < low_p or min_popularity > high_p:
            print(f"Please enter a number between {low_p} and {high_p}")
            continue
        else: 
            break

    while True:
        max_popularity = float(input(f"Enter max popularity between {min_popularity} and {high_p}: "))
        if max_popularity < min_popularity or max_popularity > high_p:
            print(f"Please enter a number between {min_popularity} and {high_p}")
            continue
        else: 
            break
    top_list_popularity = int(input("How many top popularity anime list you want to see:"))

#===========================================
# Open and write into a csv file
#===========================================    

    with open (filename, mode="w", newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(["This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your popularity"])    
        csv_writer.writerow(["Your selected popularity range is  "])
        csv_writer.writerow(["Min popularity", "Max popularity"]) # Header
        csv_writer.writerow([min_popularity, max_popularity])     # Values
        csv_writer.writerow(["Title of Anime", "Popularity", "Synopsis"]) # Header


#===========================================
# For loop to get information the user wants
#===========================================

    # Using in-built function to sort list
    # lambda creates a small unnamed function in one line
    sorted_popularity = sorted(x, key=lambda anime: anime["popularity"])
    
    count = 0   # Initialise count 
    
    for anime in sorted_popularity:
        if min_popularity <= anime['popularity'] <= max_popularity:
            popularity = {anime['popularity']}
            title = {anime ['title']}
            synopsis = {anime['synopsis']}
            print(f"Title: {title} / Popularity: {popularity} / Synopsis: {synopsis}")  
        # Save information in a csv file
            with open (filename, mode= "a", newline = "") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, popularity, synopsis])
            
            count += 1 
            if count >= top_list_popularity:
                break
    if count == 0:
        print ("No records found")


