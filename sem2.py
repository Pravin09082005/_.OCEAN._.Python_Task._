""""
#addition using function:

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(a)
print(b)
print(a+b)


#concanination:

a=input("Enter a:")
b=input("Enter b:")
print(a)
print(b)
print(a+b)
print(type(a))
print(type(b))

x=input("Enter the string:")
print(x)
print(type(x))
print(id(x))

"""
"""
#lable
a=10
b=10
print(id(a))
print(id(b))

# multiple assignments to the variable:

a=b=c=10
print(a)
print(b)
print(c)


a,b,c=25,24,26
print(a)
print(b)
print(c)

"""
"""
string=input("Enter the string:")
print(string)
print(string[0])
print(string[1:5])
print(string[2:])
print(string *2)
print(string+"collage")
print(string[:])

"""
"""
list=[12,5.43,'d',"smvec"]
list1=['x',34.5]
print(list)
print(list1)
print(list[0])
print(list[1:3])
print(list[1:])
print(list*3)
print(list1*2)
print(list+list1)
"""
"""
tuple=(11,23.5,'d',"smvec")
tup1=('D',45)
print(tuple)
print(tup1)
print(tuple[2])
print(tuple[2:4])
print(tuple[2:])
print(tuple*3)
print(tuple+tup1) 
"""
"""
#dictionary
dict={"item":"halwa","price":100,"quantity":1}
print(dict)
print(dict["item"])
print(dict["quantity"])
print(dict.keys())
print(dict.values())
"""
"""
#arithmatic operators:

a=100
b=200
print("addition",a+b)
print("subtraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("division",b/a)
print("reminder",b%a)
print("power",a**b)
print("foor division",(10//3))
"""
"""
#comparision operator:
a=5
b=3
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
"""

"""
#assignment operator:
a=10
b=20
c=a
print("c=",c)
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
print(a!=b)
"""
"""
#logical operator:
a=5
print('Is this statement true?:',)
"""
"""
z=int(input("Enter the amount:"))
if(z<=999):
    print("You won a prize")
"""

"""
a=int(input("Enter the number needed:"))
b=int(input("Enter the number needed:"))
if (a>b):
    print(a," is grester than",b)
else:
    print(b," is grester than",a)

"""

"""
#day of the week
z=int(input("Enter the number to find the day in a week:"))
if (z==1):
    print("It is monday")
elif (z==2):
    print("It is tuesday")
elif (z==3):
    print("It is wednesday")
elif (z==4):
    print("It is thursday")
elif (z==5):
    print("It is friday")
elif (z==6):
    print("It is saturday")
elif (z==7):
    print("It is sunday")
else:
    print("Invalid input")
"""

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if(a>b):
    if(a>c):
        print(a,"is greater than",b,"and",c)
    else:
        print(b,"is greater than",a,"and",c)
else:
    if(b>c):
        print(b,"is greater than",a,"and",c)
    else:
        print(c,"is greater than",a,"and",b)






