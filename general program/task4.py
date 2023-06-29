num = int(input("Enter a number: "))

z = 1   #factoral
x = 1   #counter value

while x <= num:
    z *= x
    x += 1

print("The factorial of", num, "is", z)