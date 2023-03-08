import time
import math
def delaysqrt(n, ms):
    time.sleep(ms/1000) # 2 seconds
    print("Square root of {} after {} miliseconds is {}".format(n, ms, math.sqrt(n)))
    
n = int(input())
ms = int(input())
print(delaysqrt(n, ms))
