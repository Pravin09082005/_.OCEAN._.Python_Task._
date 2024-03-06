#to determine the char entered by the user:

z=input("Enter any key:")
if (z.isalpha()):
    print("the output",z,"is a alphabet")
elif (z.isdigit()):
    print("the output",z,"is a digit")
else :
    print("the output",z,"is a space")