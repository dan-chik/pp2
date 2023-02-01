# comparing two values

print(10 > 9)
print(10 == 9)
print(10 < 9)


# print a message based on whether the condition is True or False
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# evaluate a string and a number
print(bool("Hello"))
print(bool(15))


# evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# will return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# will return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# if you have an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# returns a Boolean Value
def myFunction() :
  return True

print(myFunction())


#
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# built-in function that return a boolean value, "isinstance()", to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))