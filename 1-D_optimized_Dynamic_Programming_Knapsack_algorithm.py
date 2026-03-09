def knapsack(profit, weight, capacity):
    n = len(profit)

    # dp[c] = maximum profit for capacity c
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse backwards to avoid reusing the same item
        for c in range(capacity, weight[i] - 1, -1):
            dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

    return dp[capacity]