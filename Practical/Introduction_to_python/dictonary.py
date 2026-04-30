my_dict={
    "name" : "Lakshmi",
    "age" : 25,
    "city" : "London"
}
print (my_dict)

# update a value
my_dict["age"]=30
print(my_dict)
# add a new key value
my_dict["email"] = "abc@gmail.com"
print(my_dict)

#remove name
new_dict=my_dict.pop("city")
print(my_dict)
print(f"Deleted item is : {new_dict}")

#print all keys
print(my_dict.keys())

#print all values
print(my_dict.values())

