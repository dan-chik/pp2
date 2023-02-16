# Create function
def my_function():
    print("Hello from a function")

# Calling a Function
def my_function():
  print("Hello from a function")

my_function()


# Arguments:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# This function expects 2 arguments, and gets 2 arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Expects 2 arguments, but gets only 1
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
# outcome: Error


# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


