#marks for six subs and print avg--if avg is 75<=distinction,50-59--second class , 40-49--third class,
a=int(input("enter the first subject mark:"))
b=int(input("enter the second subject mark:"))
c=int(input("enter the third subject mark:"))
d=int(input("enter the fourth subject mark:"))
e=int(input("enter the fifth subject mark:"))
f=int(input("enter the sixth subject mark:"))

total=a+b+c+d+e+f
print("the total mark of all the subjects:",total)
avg=total/6
print("the average mark of the six subjects:",avg)

if(avg>=75):
    print("Your mark is distinction")
elif(75>avg>=60):
    print("your mark is first class")
elif(60>avg>=50):
    print("your mark id second class")
elif(50>avg>=40):
    print("your marki is third class")    
else:
    print("You failed")    