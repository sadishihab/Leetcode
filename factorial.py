#Recursion implementation for factorial

def factorial(n):
    if n == 0:                  # Base case
        return 1
    return n * factorial(n-1)   #Recursive case
print(factorial(5))