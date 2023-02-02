# Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Looping Through a String
# Loop through the letters in the word "banana"
for x in "banana":
  print(x)


# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Exit the loop when x is "banana", but break before print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Do NOT print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# stop the current iteration of the loop, and continue with the next



# The range()
for x in range(6):
    print(x)
# outcome: 0 1 2 3 4 5


# Using the start parameter
for x in range(2, 6):
  print(x)
# outcome: 2 3 4 5


# Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)
# outcome: 2 5 8 11 14 17 20 23 26 29


# Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# outcome: 0 1 2 3 4 5 Finally finished!




# Break the loop when x is 3, and see what happens with the else block
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
# outcome: 0 1 2
#If the loop breaks, the else block is not executed



# Nested Loops
# Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement

