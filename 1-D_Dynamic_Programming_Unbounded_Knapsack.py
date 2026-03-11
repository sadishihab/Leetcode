def unbounded_knapsack(profit, weight, capacity):
    n = len(profit)

    # dp[c] = maximum profit for capacity c
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse forward (allow reuse of same item)
        for c in range(weight[i], capacity + 1):
            dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

    return dp[capacity]