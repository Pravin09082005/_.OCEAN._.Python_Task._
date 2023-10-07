word = input("Enter a string: ")

def palindrome(word):
    reversed = word[::-1]  
    return word == reversed

if palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

