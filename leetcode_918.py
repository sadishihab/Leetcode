from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Standard Kadane's algorithm for normal max subarray
        def kadane(arr):
            max_sum = arr[0]
            cur_sum = 0
            for n in arr:
                cur_sum = max(cur_sum, 0)
                cur_sum += n
                max_sum = max(max_sum, cur_sum)
            return max_sum

        # Kadane for minimum subarray
        def min_kadane(arr):
            min_sum = arr[0]
            cur_sum = 0
            for n in arr:
                cur_sum = min(cur_sum, 0)
                cur_sum += n
                min_sum = min(min_sum, cur_sum)
            return min_sum

        total_sum = sum(nums)
        max_normal = kadane(nums)
        min_subarray = min_kadane(nums)

        # Edge case: all numbers negative
        if max_normal < 0:
            return max_normal

        # Max circular sum = total - min_subarray
        max_circular = total_sum - min_subarray

        return max(max_normal, max_circular)
