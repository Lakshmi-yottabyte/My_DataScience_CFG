import json
my_dict={
    "name" : "Lakshmi",
    "age" : 25,
    "city" : "London"
}

#my_json_string = json.dumps(my_dict)
#print(my_json_string)
#
# converts dict to JSON

my_json_string = json.dumps(my_dict)

print(my_json_string)

# convert JSON string to a dict

astronouts_json = '''

{

  "people": [

    {

      "craft": "ISS",

      "name": "Oleg Kononenko"

    },

    {

      "craft": "ISS",

      "name": "Nikolai Chub"

    },

    {

      "craft": "ISS",

      "name": "Tracy Caldwell Dyson"

    },

    {

      "craft": "ISS",

      "name": "Matthew Dominick"

    },

    {

      "craft": "ISS",

      "name": "Michael Barratt"

    },

    {

      "craft": "ISS",

      "name": "Jeanette Epps"

    },

    {

      "craft": "ISS",

      "name": "Alexander Grebenkin"

    },

    {

      "craft": "ISS",

      "name": "Butch Wilmore"

    },

    {

      "craft": "ISS",

      "name": "Sunita Williams"

    },

    {

      "craft": "Tiangong",

      "name": "Li Guangsu"

    },

    {

      "craft": "Tiangong",

      "name": "Li Cong"

    },

    {

      "craft": "Tiangong",

      "name": "Ye Guangfu"

    }

  ],

  "number": 12,

  "message": "success"

}

'''
#adding info from json string to a dictonary
astronouts_dict = json.loads(astronouts_json)

print(astronouts_dict["number"])

##
astronouts_dict = json.loads(astronouts_json)

print(astronouts_dict["number"])

print(astronouts_dict["people"][0]["name"])