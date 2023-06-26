user = 5
s=user - 1
for i in range(1, user):
    print(" "*s, end="")
    print("* "*i)
    s -= 1

s = 0

for i in range(user,0,-1):
    print(" "*s, end="")
    print("* "*i)
    s +=1
