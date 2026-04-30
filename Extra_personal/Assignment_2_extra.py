# In this assignment, the user will be give the animation title asked based on the score of the animation
#=============================================================================================================

#To install additonal libraries that are not included in Python as standard  - use 'pip install <module name>' command

# Additional module not used in this assignment
import math     # this is a mathematical module provides common functions such trignometric, functions, logarithms and pi

#import necessary modules
import requests # It is a thrid-party library. It is not part of python standard library. 
                #'request' is installed with pip install requests. It is for calling API 
import json     # this module provides built-in support for working with JSON data
import csv      # this module reads and writes tabular data in CSV(Comma Separated Values) format.


#Base URL for API - trivia database
base_url = "https://api.jikan.moe/v4/top/anime?type=ona" # no API key need 

#Categories
categories = { 
    "1": "score", 
    "2": "rank", 
    "3": "popularity"
}

#===========================================================================
# Functions
#============================================================================
#function to greet user
def greet(name):
     print(f"Hello {name}, How are you?")


# # fucntion to validate user category choice
# def prompt_category(choice):
#     while True: 
#         if choice in categories:  
#             print(f"You chose to filter by {categories[choice]}")
#             return categories[choice]
#         else:
#             break
#     print("Invalid choice, please enter valid number")

############################ ALTERED TO ASK AGAIN WHEN INVALID CHOICE IS ENTERED ###############
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

# function to find highest score
def high_score(x):
    score_values=[]
    for anime in x:
        score_values.append(anime['score'])

    high_s = max(score_values)
    low_s = min(score_values)
    return (high_s, low_s)  

# function to find highest rank
def high_rank(x):
    rank_values=[]
    for anime in x:
        rank_values.append(anime['rank'])

    high_r = max(rank_values)
    low_r = min(rank_values)
    return (high_r, low_r)  

# function to find highest popularity
def high_popularity(x):
    popularity_values=[]
    for anime in x:
        popularity_values.append(anime['popularity'])

    high_p = max(popularity_values)
    low_p = min(popularity_values)
    return (high_p, low_p)  

#==============================================================================
# Registration and Greeting user
#==============================================================================

################################## NAME VALIDATION SO IT WILL REASK IF EMPTY ######################
# n1= input("Enter your name: ")
# name=n1.strip() # string slicing
while True:
    n1 = input("Enter your name: ")
    name = n1.strip()
    if name == "":
        print("Name cannot be empty, please enter your name")
        continue
    break

greet(name)


filename = f"{name}_results.csv"

#================================================================================================
# Get information form API
#===============================================================================================
response=requests.get(base_url)

#assign response to a vairable
info=response.json()
x = info["data"]

######################## I DON'T THINK THIS IS NEEDED. IT'S JUST REPEATED LATER AND MAKES IT TOO CROWDED HERE ####################################################
# #calling highest score function
high_s, low_s = high_score(x)
# print (f'Minimum score is {low_s} and maximum score is {high_s}')

# #calling highest rank function
high_r, low_r = high_rank(x)
# print (f'Minimum rank is {low_r} and maximum rate is {high_r}')

# #calling highest popularity function
high_p, low_p = high_popularity(x)
# print (f'Minimum popularity is {low_p} and popularity rate is {high_p}')

#===============================================================================================
# ask user choice based on category
#===============================================================================================

#display category list
  
# print("What list do you want to see from these category? ")    DONT NEED THESE LINES ANY MORE #####################################################
# for key, value in categories.items():
#     print(f" {key}.{value}")

#user inputs about category and check if the category chose is valid
#choice = input("Choose a category:")           THIS LINE IS NOT NEEDED ################################################################
choice = prompt_category()
#===================================================================
#                           CATEGORY 1 - SCORE
#===================================================================
if choice == "1":    #user inputs score and check if score is valid
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

    top_list_score = int(input("How many top scored anime do you want to see: "))

#==============================================================================================
# open and write  csv file
# =============================================================================================    

    with open (filename, mode="w", newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(["This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your score"])    
        csv_writer.writerow(["Your selected score range is  "])
        csv_writer.writerow(["Min score", "Max score"]) # header
        csv_writer.writerow([min_score, max_score])     # values
        csv_writer.writerow(["Title of Anime", "Score", "Synopsis"]) # header


#==================================================================================================
# For loop to get information user wants  
#=================================================================================================

    count = 0   # initialize count 
    
    for anime in x:
        if min_score <= anime['score'] <= max_score:
            score = {anime['score']}
            title = {anime ['title']}
            synopsis = {anime['synopsis']}
            print(f"Title: {title} / Score: {score} / Synopsis: {synopsis}")  
        # save information in a csv file
            with open (filename, mode= "a", newline = "") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, score, synopsis])
            
            count += 1 
            if count >= top_list_score:
                break

#========================================================================
#                        CATEGORY 2 - Rank
#========================================================================
if choice == "2":    #user inputs rank and check if rank is valid
    while True:
        min_score = float(input(f"Enter min score between {low_r} and {high_s}: "))
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
    top_list_rank = int(input("How many top rank anime list you want to see:"))

#==============================================================================================
# open and write  csv file
# =============================================================================================    

    with open (filename, mode="w", newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(["This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your rank"])    
        csv_writer.writerow(["Your selected rank range is  "])
        csv_writer.writerow(["Min rank", "Max rank"]) # header
        csv_writer.writerow([min_rank, max_rank])     # values
        csv_writer.writerow(["Title of Anime", "Rank", "Synopsis"]) # header


#==================================================================================================
# For loop to get information user wants  
#=================================================================================================

    count = 0   # initialize count 
    
    for anime in x:
        if min_rank <= anime['rank'] <= max_rank:
            rank = {anime['rank']}
            title = {anime ['title']}
            synopsis = {anime['synopsis']}
            print(f"Title: {title} / Rank: {rank} / Synopsis: {synopsis}")  
        # save information in a csv file
            with open (filename, mode= "a", newline = "") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, rank, synopsis])
            
            count += 1 
            if count >= top_list_rank:
                break
#==========================================================================
#                        CATEGORY 3 - Popularity
#==========================================================================
if choice == "3":    #user inputs popularity and check if popularity is valid
    while True:
        min_popularity = float(input(f"Enter min popularity between {low_p} and {high_p}:  "))
        max_popularity = float(input(f"Enter max popularity between {low_p} and {high_p}: "))
        
        if min_popularity < low_p or max_popularity > high_p:
            print (f'Please enter numbers between {low_p} and {high_p}')
            continue
        else:
            break
    top_list_popularity = int(input("How many top popularity anime list you want to see:"))

#==============================================================================================
# open and write  csv file
# =============================================================================================    

    with open (filename, mode="w", newline="") as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(["This is your list of top rated ONS (Original Net Animation) anime according to MyAnimeList based on your popularity"])    
        csv_writer.writerow(["Your selected popularity range is  "])
        csv_writer.writerow(["Min popularity", "Max popularity"]) # header
        csv_writer.writerow([min_popularity, max_popularity])     # values
        csv_writer.writerow(["Title of Anime", "Popularity", "Synopsis"]) # header


#==================================================================================================
# For loop to get information user wants  
#=================================================================================================

    # Using in-built function to sort list
    # lambda creates a small unnamed function in one line
    """def get_popularity(anime):
        return anime["popularity"]
    This will then make the sorted_popularity
    sorted_popularity = sorted(x, key = get_popularity)"""
    sorted_popularity = sorted(x, key=lambda anime: anime["popularity"])
    
    count = 0   # initialize count 
    
    for anime in sorted_popularity:
        if min_popularity <= anime['popularity'] <= max_popularity:
            popularity = {anime['popularity']}
            title = {anime ['title']}
            synopsis = {anime['synopsis']}
            print(f"Title: {title} / Popularity: {popularity} / Synopsis: {synopsis}")  
        # save information in a csv file
            with open (filename, mode= "a", newline = "") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, popularity, synopsis])
            
            count += 1 
            if count >= top_list_popularity:
                break


