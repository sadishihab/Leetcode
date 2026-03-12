class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        # your dp function unchanged
        def dp(s1, s2):
            N, M = len(s1), len(s2)
            dp = [[0] * (M+1) for _ in range(N+1)]

            for i in range(N):
                for j in range(M):
                    if s1[i] == s2[j]:
                        dp[i+1][j+1] = 1 + dp[i][j]
                    else:
                        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

            return dp[N][M]

        return dp(text1, text2)