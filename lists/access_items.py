# print the second item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# note: first item has index 0


# last item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# returns the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# note: starts at index 2 (included) and ends at index 5 (not included)


# returns from the beginning to, but NOT including, "kiwi"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# returns the items from "cherry" to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# from "orange" (-4) to, but NOT including "mango" (-1)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# check if "apple" is present in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
