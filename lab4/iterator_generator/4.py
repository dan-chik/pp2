def gen_squares(a,b):
    #a = 1
    while a<=b:
        yield a*a
        a+=1
 
for i in gen_squares(1,5):
    print(i)