def factorial():
    num = int(input("Enter a number: "))
    z = 1   #factoral
    x = 1   #counter value
    while x <= num:
        z *= x
        x += 1
    print("The factorial of", num, "is", z)


factorial()

def name_in_box():
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


name_in_box()
