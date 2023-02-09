def replace(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    return a

n = input()
l = n.split()

for i in range(len(l)):
    l[i] = int(l[i])

print(replace(l))