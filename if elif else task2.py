# to find the current bill...


a=int(input("enter the amount of unit to calculate your bill: "))
if(a<=100):
    print("our bill is free")
elif(a>=101 and a<=200 ,):
    b=((a-100)*5)
    print("your bill is ₹",b)
elif(a>=201):
    c=(500+(a-200)*10)
    print("your bill is ₹",c)
else:
    print("invalid")

