# Set items are unchangeable, but you can remove items and add new items

# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# note: sets are unordered

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
# outcome: {'banana', 'cherry', 'apple'}

# Number of items
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# <class 'set'>

# set() constructor
thisset = set(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thisset)
