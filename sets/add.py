# The add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# The update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add any iterable
# Add elements of a list to at set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
