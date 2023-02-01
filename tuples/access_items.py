# Print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Last item
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# 3, 4, 5th items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# The items from the beginning to, but NOT included, "kiwi"
print(thistuple[:4])

# The items from "cherry" and to the end
print(thistuple[2:])

# From index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1])

# Check if "apple" is present in the tuple
if "apple" in thistuple:
  print("Yes")