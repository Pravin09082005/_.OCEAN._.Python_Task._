# to find neon numbers...

a=int(input("Enter a number: "))
square=a*a
print("squared value is: ",square)
z=int(input("enter the first digit if the squared value: "))
# if(z!=0):
#     print("z")

x=int(input("enter the second digit if the squared value: "))
# elif(x!=0):
#     print("x")
q=z+x
if(q==a):
    print("it is a happy number")
else:
    print("it is not a happy number")



