# If statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

# If statement, without indentation (will raise an error)
a = 33
b = 200
if b > a:
    print("b is greater than a") 
# you will get an error

# Elif:
# 1
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# 2
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# 3
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")


# One line if else statement, with 3 conditions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# NOT
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Nested If (if inside if)
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# The pass Statement (to avoid getting an error)
a = 33
b = 200

if b > a:
  pass