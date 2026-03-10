class Solution:
    def findTargetSumWays(self, nums, target):

        total = sum(nums)

        if total < abs(target) or (total - target) % 2 != 0:
            return 0

        capacity = (total - target) // 2

        return knapsack(nums, nums, capacity)


def knapsack(profit, weight, capacity):

    dp = [0] * (capacity + 1)
    dp[0] = 1

    for i in range(len(profit)):
        for c in range(capacity, weight[i] - 1, -1):
            dp[c] += dp[c - weight[i]]

    return dp[capacity]