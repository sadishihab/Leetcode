class Solution:
    def lastStoneWeightII(self, stones):

        total = sum(stones)

        capacity = total // 2

        profit = stones
        weight = stones

        best = knapsack(profit, weight, capacity)

        return total - 2 * best


def knapsack(profit, weight, capacity):
    n = len(profit)

    dp = [0] * (capacity + 1)

    for i in range(n):
        for c in range(capacity, weight[i] - 1, -1):
            dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

    return dp[capacity]