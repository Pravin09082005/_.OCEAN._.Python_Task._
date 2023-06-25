# to print n numbers of 1...


n=int(input("Enter the number of terms: "))
sum = 0
term = 1

for i in range(n):
    sum += term
    term = term * 10 + 1

print(term)