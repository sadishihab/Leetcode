def unbounded_knapsack(coins, amount):
    n = len(coins)

    # dp[c] = minimum coins needed for amount c
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(n):
        # Traverse forward (allow reuse of same coin)
        for c in range(coins[i], amount + 1):
            dp[c] = min(dp[c], 1 + dp[c - coins[i]])

    return dp[amount] if dp[amount] != float('inf') else -1


class Solution:
    def coinChange(self, coins, amount):
        return unbounded_knapsack(coins, amount)