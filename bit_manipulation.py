
# Counting Bits
# Using least significant bit (LSB) approach
def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1           # same as n // 2
    return count