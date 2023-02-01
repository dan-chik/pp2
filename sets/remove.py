# The remove() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)
# !!note: if the item to remove does not exist, remove() will raise an error.



# The discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
print(thisset)
# !!note: if the item to remove does not exist, will NOT raise an error.


# The pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# !!note: when using the pop() method, you do not know which item that gets removed


# The clear() method empties the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset)


# The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)