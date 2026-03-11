def unbounded_knapsack(coins, amount):
    n = len(coins)

    # dp[c] = number of ways to make amount c
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(n):
        # Traverse forward (allow reuse of coin)
        for c in range(coins[i], amount + 1):
            dp[c] += dp[c - coins[i]]

    return dp[amount]


class Solution:
    def change(self, amount, coins):
        return unbounded_knapsack(coins, amount)