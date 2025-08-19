# Two Sum
# While looping, check if target–num exists in map. If yes → return indices. If no → save num:index.
# Time: O(n) (one pass)
# Space: O(n) (for hash map)

nums = [2, 7, 11, 15]

class Solution(object):
    def twoSum(self, nums, target):
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i
        return []

sol = Solution()
print(sol.twoSum(nums, 9))