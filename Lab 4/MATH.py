import math
# Ex 1
a = int(input("Input degree: "))
print("Output radian: ", math.radians(a))

# Ex 2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Expected Output: ", (a+b)*h/2)

# Ex 3
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
print("The area of the polygon is: ", (n*(a**2))/(4*math.tan(math.pi/n)))

# Ex 4
a = int(input("Length of base: "))
h = int(input("Height of parallelogram: ")) 
print("Expected Output: ", a*h)    