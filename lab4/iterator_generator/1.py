def gen_squares(n):
    i=1
    while i<=n:
        yield i**2
        i+=1
 
n = int(input())
g = gen_squares(n)
for i in range(n):
    print(next(g))