# print(" ------")
# print("|      |")
# print("|   S  |")
# print("|      |")
# print(" ------ ") 

user = input("enter your name: ")

l = len(user)

# for i in range(l):
#     print(f" -----------\n|           |\n|     {user[i]}     |\n|           |\n -----------")

for i in range(l+1):
    if(i == 0 or i == 4):
        print(" -----------     " * l)
    elif(i == 1 or i == 3):
        print("|           |    " * l)
    else:
        print(f"|     {user[i]}     |    " * l)