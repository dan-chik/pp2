# Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)
# outcome: brand model year


# All values in the dict, one by one
for x in thisdict:
  print(thisdict[x])
# outcome: Ford Mustang 1964


# The values() method to return values
for x in thisdict.values():
  print(x)


# The keys() method to return the keys
for x in thisdict.keys():
  print(x)


# Both keys and values
for x, y in thisdict.items():
  print(x, y)


