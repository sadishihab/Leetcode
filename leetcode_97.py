class Solution(object):
    def isInterleave(self, s1, s2, s3):
        N, M = len(s1), len(s2)

        if N + M != len(s3):
            return False

        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(N + 1):
            for j in range(M + 1):
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]

                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]

        return dp[N][M]