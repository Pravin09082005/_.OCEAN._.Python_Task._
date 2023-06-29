#Multiplication table....
num = int (input("Enter the number :"))
z=int(input("enter the range of the table:"))
print ("multiplication Table of ", num)
for i in range(1, z+1):
    print (num, "x", i,"=", num*i)

    