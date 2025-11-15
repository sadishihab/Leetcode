class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize the answer array with 0s
        ans = [0] * (n + 1)

        # Fill the array using dynamic programming
        for i in range(1, n + 1):
            # Number of 1s in i = number of 1s in i//2 + last bit of i
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
