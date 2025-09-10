# Recursion with memorization for optimal time and space complexity

class Solution(object):

    def __init__(self):
        self.memo = {}                                      #dictionary for memorization
    def climbStairs(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 1:                                          # base cases
            return 1
        if n == 2:
            return 2

        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)         # recursive case
        return self.memo[n]

