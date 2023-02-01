# Packing a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# output: apple\n banana\n cherry


# Using Asterisk *
# Assign the rest of the values as a list called "red"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#output: 
""" apple
    banana
    ['cherry', 'strawberry', 'raspberry']
"""


# Add a list of values the "tropic" variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)