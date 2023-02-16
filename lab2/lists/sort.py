# alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# descending
# reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)



# Based on how close the number is to 50
def myFunc(n):
    return abs(n-50)

lista = [100, 50, 65, 82, 23]
lista.sort(key = myFunc)
print(lista)

# Case sensitive sorting
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# outcome: ['Kiwi', 'Orange', 'banana', 'cherry']


# Case-insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


