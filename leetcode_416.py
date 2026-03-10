class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        # If total sum is odd → impossible
        if total % 2 != 0:
            return False

        target = total // 2

        # Use knapsack template
        profit = nums
        weight = nums

        if knapsack(profit, weight, target) == target:
            return True
        return False


def knapsack(profit, weight, capacity):
    n = len(profit)

    dp = [0] * (capacity + 1)

    for i in range(n):
        for c in range(capacity, weight[i] - 1, -1):
            dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

    return dp[capacity]