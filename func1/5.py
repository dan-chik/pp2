def toString(given):
    return ''.join(given)

a = input()
y = len(a)
given = list(a)

def permute(given, x, y):
    if x == y:
        print(toString(given))
    else:
        for i in range(x, y):
            given[x], given[i] = given[i], given[y]
            permute(given, x+1, y)
            given[x], given[i] = given[i], given[y]

permute(given, 0, y)