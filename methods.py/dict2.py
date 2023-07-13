def reversing():
    s=str(input("Enter a string to be reversed:"))
    length=len(s)
    z=" "
    while(length>0):
        length-=1
        z+=s[length]
    print(z)
    
reversing()



#--------------------------------------------------------------------------------------
print()
#-having input being fed(dynamic)
#-having input fed already(static)
#--------------------------------------------------------------------------------------


def reversing(s):
    length = len(s)
    z = ""
    while length > 0:
        length -= 1
        z += s[length]
    return z

input = "pravin"  

reversed = reversing(input)
print(reversed)