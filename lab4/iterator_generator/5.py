def gen_nums(n):
    while n>=0:
        yield n
        n-=1

n = int(input())
for i in gen_nums(n):
    print(i)