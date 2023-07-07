def reversing():
    s=str(input("Enter a string to be reversed:"))
    length=len(s)
    z=" "
    while(length>0):
        length-=1
        z+=s[length]
    print(z)
reversing()

