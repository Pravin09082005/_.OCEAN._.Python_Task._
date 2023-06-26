# print(" ----------- ")
# print("|           |")
# print("|     S     |")
# print("|           |")
# print(" ----------- ") 

user = input("enter your name: ")

l = len(user)

# for i in range(l):
#     print(f" -----------\n|           |\n|     {user[i]}     |\n|           |\n -----------")

for i in range(1, 6):
    if(i == 1 or i == 5):
        print(" -----------     " * l)
    elif(i == 2 or i == 4):
        print("|           |    " * l)
    elif(i==3):
        for j in range(l):
            print(f"|     {user[j]}     |    " ,end="")
        print()
       