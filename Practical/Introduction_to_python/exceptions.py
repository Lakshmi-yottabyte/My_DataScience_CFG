#FIRST CODE
# try:
#     num=int(input("Enter a number between 5 and 10: "))
#     if num<5 or num>10:
#         raise Exception
#     else:
#         print(f"number you entered is {num}")
# except:
#     print("please enter a number between 5 and 10")

# SECOND CODE
##
try:

    minutes = int(input("Enter minutes: "))

    seconds = int(input("Enter seconds: "))

    if minutes < 0 or seconds < 0:

        raise Exception

    print(f"the duration is {seconds + (minutes*60)} secs")

except ValueError:

    print("please enter a number")

except Exception:

    print("Please enter minutes/seconds more than 0")