# Get the value of the "model" key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

# with get()
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary
x = thisdict.keys()
# outcome: dict_keys(['brand', 'model', 'year'])



# Add a new item to the original dict, keys list gets updated
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
# outcome: 
"""dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])"""




# Get a list of the values
x = thisdict.values()


# Changing orig dict, values list gets updated
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
# outcome: 
""" dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020]) """



# Add a new item to the orig dict, values list gets updated 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



# Get a list of the key:value pairs
x = thisdict.items()
# outcome: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Change in the orig dict, items list gets updated
x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



# Add a new item to the orig dict, items list gets updated
x = car.items()
print(x) #before the change

car["color"] = "red"
print(x) #after the change


# Check if Key Exists
if "model" in thisdict:
  print("Yes")
