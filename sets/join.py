# The union() method returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# outcome: {1, 'a', 'b', 2, 3, 'c'}


# The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# note: Both union() and update() will exclude any duplicate items


# Keep ONLY the duplicates:
# The update() method (Exist in both set x, and set y)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
# outcome: {'apple'}


# The intersection() method will return a new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)



# Keep all, but NOT the duplicates:
# The symmetric_difference_update() method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# The symmetric_difference() method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)