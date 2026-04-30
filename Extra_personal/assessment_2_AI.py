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

# Function to find max and min values
def get_range(x, field):
    values = [anime[field] or 0 for anime in x]
    return max(values), min(values)

## Function to validate user inputs
def get_user_range(field, low, high):
    while True:
        min_val = float(input(f"Enter min {field} between {low} and {high}: "))
        if min_val < low or min_val > high:
            print(f"Please enter a number between {low} and {high}")
            continue
        break

    while True:
        max_val = float(input(f"Enter max {field} between {min_val} and {high}: "))
        if max_val < min_val or max_val > high:
            print(f"Please enter a number between {min_val} and {high}")
            continue
        break

    return min_val, max_val

# Function to write information in file
def write_and_print(x, field, min_val, max_val, top_list, filename):
    # Write CSV header
    with open(filename, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([f"Top ONA anime filtered by {field}"])
        csv_writer.writerow([f"Min {field}", f"Max {field}"])
        csv_writer.writerow([min_val, max_val])
        csv_writer.writerow(["Title", field.capitalize(), "Synopsis"])

    # Sort by field if popularity, otherwise keep original order
    sorted_x = sorted(x, key=lambda anime: anime[field] or 0) if field == "popularity" else x

    count = 0
    for anime in sorted_x:
        if anime[field] and min_val <= anime[field] <= max_val:
            value = anime[field]
            title = anime["title"]
            synopsis = anime["synopsis"]
            print(f"Title: {title} / {field.capitalize()}: {value}")
            with open(filename, mode="a", newline="") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([title, value, synopsis])
            count += 1
            if count >= top_list:
                break

    if count == 0:
        print("No records found")

#===========================================================================
#                       Registration and Greeting
#===========================================================================

while True:
    name = input("Enter your name: ").strip().capitalize()
    if name == "":
        print("Name cannot be empty, please enter your name")
        continue
    break

greet(name)
filename = f"{name}_results.csv"

#===========================================================================
#                           Get data from API
#===========================================================================

response = requests.get(base_url)
info = response.json()
x = info["data"]

#===========================================================================
#                           Ask user for category
#===========================================================================

choice = prompt_category()
field = categories[choice]

high, low = get_range(x, field)
min_val, max_val = get_user_range(field, low, high)
top_list = int(input(f"How many anime do you want to see: "))

write_and_print(x, field, min_val, max_val, top_list, filename)