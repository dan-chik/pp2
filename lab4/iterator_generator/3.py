def div(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            print(str(i) + " ", end = "")
        else:
            pass

n = int(input())
div(n)
        