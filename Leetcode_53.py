# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)  # reset if curSum becomes negative
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum
