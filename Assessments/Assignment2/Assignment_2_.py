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


# Base URL for API - trivia database
base_url = "https://api.jikan.moe/v4/top/anime?type=ona" # no API key need 

# Categories
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

# Function returns high and low value from the data file for a given category
def value_range(x_data, fieldname):
    extract_list=[]
    for anime in x_data:
        extract_list.append(anime[fieldname])

    high_value = max(extract_list)
    low_value = min(extract_list)
    return (high_value,  low_value)  

# Function to write output to csv file
def write_file(filename, fieldname, min_value, max_value):

    with open (filename, mode="w", newline="") as file:
            csv_writer=csv.writer(file)
            csv_writer.writerow([f"This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your {field}"])    
            csv_writer.writerow([f"Your selected {fieldname} range is  "])
            csv_writer.writerow([f"Min {fieldname}", f"Max {fieldname}"]) # Header
            csv_writer.writerow([min_value, max_value])     # Values
            csv_writer.writerow([f"Title of Anime, {fieldname}", "Synopsis"]) # Header

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
#                   Ask user choice based on category
#===========================================================================

choice = prompt_category()
field = categories[choice]

#===========================================================================
#                       Get information form API
#===========================================================================
response=requests.get(base_url)

# Assign response to a vairable
info=response.json()
x = info["data"]

# Calling highest score function
max_value, min_value = value_range(x, field)

#===========================================================================
#                           Category 1 - SCORE
#===========================================================================
# User inputs score and program checks if score is valid
if choice == "1":    
    while True:
        min_score = float(input(f"Enter min {field} between {min_value} and {max_value}: "))
        if min_score < min_value or min_score > max_value:
            print(f"Please enter a number between {min_value} and {max_value}")
            continue
        else: 
            break

    while True:
        max_score = float(input(f"Enter max {field} between {min_score} and {max_value}: "))
        if max_score < min_value or max_score > max_value:
            print(f"Please enter a number between {min_score} and {max_value}")
            continue
        else: 
            break
    top_list_score = int(input(f"How many top {field} anime list you want to see:"))

#===========================================
# Open and write into a csv file
#===========================================

    write_file(filename, field, min_score, max_score)

#===========================================
# For loop to get information the user wants
#===========================================

    # Using in-built function to sort list
    # lambda creates a small unnamed function in one line
    sorted_score = sorted(x, key=lambda anime: anime[field])


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
        min_rank = float(input(f"Enter min {field} between {min_value} and {max_value}: "))
        if min_rank < min_value or min_rank > max_value:
            print(f"Please enter a number between {min_value} and {max_value}")
            continue
        else: 
            break

    while True:
        max_rank = float(input(f"Enter max {field} between {min_rank} and {max_value}: "))
        if max_rank < min_value or max_rank > max_value:
            print(f"Please enter a number between {min_rank} and {max_value}")
            continue
        else: 
            break
    top_list_rank = int(input(f"How many top {field} anime list you want to see:"))

#===========================================
# Open and write into a csv file
#===========================================   

    write_file(filename, field, min_rank, max_rank)

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
        min_popularity = float(input(f"Enter min {field} between {min_value} and {max_value}: "))
        if  min_popularity < min_value or min_popularity > max_value:
            print(f"Please enter a number between {min_value} and {max_value}")
            continue
        else: 
            break

    while True:
        max_popularity = float(input(f"Enter max {field} between {min_popularity} and {max_value}: "))
        if max_popularity < min_popularity or max_popularity > max_value:
            print(f"Please enter a number between {min_popularity} and {max_value}")
            continue
        else: 
            break
    top_list_popularity = int(input(f"How many top {field} anime list you want to see:"))

#===========================================
# Open and write into a csv file
#===========================================    

    write_file(filename, field, min_popularity, max_popularity)

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


