# Without list comprehension you will have to write a for statement with a conditional test inside
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# output: ['apple', 'banana', 'mango']


# With list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Syntax: 
# newlist = [expression for item in iterable if condition == True]


# Only accept items that are not "apple"
newlist = [x for x in fruits if x != "apple"]

# With no if statement
newlist = [x for x in fruits]

# The iterable can be any iterable object, like a list, tuple, set etc
# The range() function to create an iterable
newlist = [x for x in range(10)]

# Same example, but with a condition
# Accept only numbers lower than 5
newlist = [x for x in range(10) if x < 5]

# Upper case
newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello'
newlist = ['hello' for x in fruits]

# Return "orange" instead of "banana"
newlist = [x if x != "banana" else "orange" for x in fruits]

