#area of a right angle triangle

a=(float(input(("Enter the value of the first side of the right angle triangle:"))))
b=(float(input(("Enter the value of the second side of the right angle triangle:"))))
c=(float(input(("Enter the value of the third side of the right angle triangle:"))))
s=(a+b+c)/2
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print("area of the right triangle is",area)

