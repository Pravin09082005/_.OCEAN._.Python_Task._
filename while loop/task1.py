# print natural numbers and sum them using while loop...


x=int(input("enter the range of the natural numbre to be summed:"))
n=1
z=0
while n<=x:
    print(n)
    z += n
    n += 1
    print("sum of natural numbers:",z)
