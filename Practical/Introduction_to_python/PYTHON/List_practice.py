# Create lsit of cities called cities
Cities=["London", "Manchester", "Birmingham"]
# Expanded it with ["Paris, "Tokyo"]
Cities.extend(["Paris", "Tokyo"])
print(Cities)
# # check whether "London"is in your list
print("London" in Cities)
# # append your lsit with "Cape town"
Cities.append("Cape Town")
print(Cities)
# #remove "Paris" from your list
Cities.pop(3)
print(Cities)