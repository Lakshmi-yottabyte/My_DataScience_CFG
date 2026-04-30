# email = "lpn@np;co.uk"
# print(email==input("enter your email address"))
# age =int(input("Enter your age:"))
# if age ==45:
#     print("you are cool")
# else:
#     print("you are star")

# SECOND CODE
# response = input("what is your favourite colour?")
# print (response.lower())
# if response.lower()=="orange":
#     print("mine too")
# else:
#     print("I don't like that colour")

# THIRD CODE
# temperature = int(input("What is today's temperature "))
# if temperature >30:
#     print ("It's too hot. Stay in shade")
# elif temperature <=30 and temperature >=20:
#     print("Nice weather. Enjoy!")
# elif temperature <20 and temperature >=10:
#     print("It is bit chilly. Stay warm")
# elif temperature <10 and temperature >=0:
#     print ("It's cold. Have a hot drink. Keep warm")
# else: print("It's freezing. Stay indoors and tun on the heating")

#FOURTH CODE
# username = input("Enter your username: ")

# password = input("Enter your password: ")

# if username == "admin" and password == "1234": # This is a simple authentication check

#     print("Login successful") # If the username and password match, the user is granted access

# else:

#     print("Access denied") # If the username or password is incorrect, access is denied

#FIFTH CODE
# for i in range(1,11):
#     print(i)

#SIXTH CODE
# my_cities=["manchester", "London", "Bristol"]
# count=1
# for i in my_cities:
#     print(f"city {count} is {i}")
#     count =count+1
# 
# SEVENTH CODE
# EVEN OR ODD NUMEBR
# number = input ("Enter a number")
# if int(number)%2==0:
#     print("number is even")
# else: print("number is odd")
#
#EIGTH CODE
#PRINT ALTERNATE NUMBERS
# for i in range(1,10,2):
#     print(i)
#
#NINTH CODE
# my_list = ["Alan", "Lakshmi", "Anshu", "Abhi", "RK"]
# name_short_name_list=[]
# for i in my_list:
#     if len(i)<=5:
#         L=len(i)
#         print(f"name {i} has {L} number of characters")
#         name_short_name_list.append(i)
# print(f"names less than equal to 5 characters: {name_short_name_list}")
#
#TENTH CODE
# counter=5
# while counter>0:
#     print(counter)
#     counter=counter-1
#
#ELEVENTH CODE
# counter = int(input("Enter a number:"))
# while counter<6:
#     print(counter)
#     counter=counter-1
#     if counter ==-10:
#         break
# print("While loop condition did not satisy")
#
#TWELFTH CODE - FUNCTIONS - no input parameter and no return value
# def greet():
#     """this function will greet user. 
#     There us no input parameter
#     """
#     print("Hello, How are you?")
    
# greet()
# #
#THIRTEENTH CODE - FUNCTIONS with input parameter and no return value
# def is_even_or_odd(number):
#     if number%2==0:
#         print("number is even")
#     else: print("number is odd")

# number=int(input("enter a number: "))
# is_even_or_odd(number)
#
#FOURTEENTH CODE - FUNCTIONS with RETURN VALUE
# def add_two_numbers(N1, N2):
#     sum=N1+N2
#     return sum
# N1=int(input("input first number: "))
# N2=int(input("input second number:"))
# sum=add_two_numbers(N1,N2)
# print(f"sum of two numbers is:  {sum}")
#
#FIFTEENTH CODE - ACTIVITY 1
age=int(input("enter your  age: "))
months = int(input("input number of years of subscription in months: "))
if age <=25:
    print("you will get 10% discount")
elif months>=12:
    print("You will get 10% discount")
else: print("you don't qualify for discount")

#SIXTEENTH CODE - ACTIVITY 2
age=int(input("enter your  age: "))
years = int(input("input number of years of subscription in years: "))
if age <=25 or age>=65 or years>=1:
    print("you will get 10% discount")
else: ("you don't qualify for discount")