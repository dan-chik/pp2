num = [1, 2, 3, 4, 5, 6]

for i in range (2, 7):
    num = list(filter(lambda x: x == i or x%i!=0, num))

print("prime numbers: ")
print(num)
