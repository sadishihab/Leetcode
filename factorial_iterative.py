# Iterative implementation of factorial

def factorial_iterative(n):
    result = 1                                              # Start with 1, because factorial multiplies numbers
    for i in range(1, n + 1):
        result *= i                                         # Multiply result by each number from 1 to n
    return result

print(factorial_iterative(5))                               # Output: 120