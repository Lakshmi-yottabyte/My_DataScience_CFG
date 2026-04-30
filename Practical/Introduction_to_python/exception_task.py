class invalidlength(Exception):
    pass
try:
    song_length=int(input("Enter song length in seconds: "))
    if song_length<0:
        raise invalidlength
    print(f"lenght of song is {song_length/60} in minutes")

except:
    print("please enter number greater that 0")

    ###############################
    ##############################

class LengthInvalid(Exception):

    pass

try:

    length = float(input("enter length in seconds: "))

    if length < 0:

        raise LengthInvalid("song length can't be negative")

    length_min = length/60

    

    assert length_min >= 0, "issue with duration"

    print(f"length in minutes is {length_min:.2f}")

except LengthInvalid as e:

    print(f"Error: {e}")

except ValueError:

    print("song length must be numerical")