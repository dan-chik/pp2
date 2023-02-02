# Create and print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# (un)ordered depends on version
# changeable
# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# outcome: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}



# Numbers of items
print(len(thisdict))

# Data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# <class 'dict'>

# The dict() method to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
