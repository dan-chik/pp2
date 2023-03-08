def uplowcnt(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print("Number of upper case letters: " , u)
    print("Number of lower case letters: ", l)

s = str(input())

print(uplowcnt(s))