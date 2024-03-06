n = int(input("Enter the value of n to find the nth term in the Fibonacci series: "))
def fibonacci(n):
    if n <= 0:
        return "Enter a positive integer for the nth term."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
