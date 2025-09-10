def fibonacci_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1                                     # f(0), f(1)
    for i in range(2, n + 1):
        a, b = b, a + b                             # shift forward
    return b

print(fibonacci_iterative(4))  # Output: 3
