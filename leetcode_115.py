class Solution(object):
    def numDistinct(self, s, t):
        N, M = len(s), len(t)

        # dp[i][j] = number of ways s[0..i-1] forms t[0..j-1]
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        # Base case: empty t can be formed by any prefix of s in exactly 1 way
        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s[i - 1] == t[j - 1]:
                    # Option 1: use current character → dp[i-1][j-1]
                    # Option 2: skip current character → dp[i-1][j]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Skip current character
                    dp[i][j] = dp[i - 1][j]

        return dp[N][M]