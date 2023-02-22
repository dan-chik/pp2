from math import pi, tan
n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
area = (l**2)*n/(4*tan(pi/n))
print ("The area of the polygon is: ", area)