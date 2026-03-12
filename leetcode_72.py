class Solution:
    def minDistance(self, word1, word2):
        def dp(s1, s2):
            N, M = len(s1), len(s2)
            dp = [[0] * (M + 1) for _ in range(N + 1)]

            for i in range(N + 1):
                dp[i][0] = i
            for j in range(M + 1):
                dp[0][j] = j

            for i in range(N):
                for j in range(M):
                    if s1[i] == s2[j]:
                        dp[i+1][j+1] = dp[i][j]
                    else:
                        dp[i+1][j+1] = 1 + min(
                            dp[i][j+1],   # delete
                            dp[i+1][j],   # insert
                            dp[i][j]      # replace
                        )

            return dp[N][M]

        return dp(word1, word2)