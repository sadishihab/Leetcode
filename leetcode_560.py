class Solution:
    def subarraySum(self, nums, k):
        from collections import defaultdict

        count = 0
        cum_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty prefix sum

        for num in nums:
            cum_sum += num
            if (cum_sum - k) in prefix_counts:
                count += prefix_counts[cum_sum - k]
            prefix_counts[cum_sum] += 1

        return count
