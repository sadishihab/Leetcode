class Solution:
    def subsets(self, nums):
        subsets = []
        curSet = []

        def helper(i):
            if i == len(nums):
                subsets.append(curSet.copy())
                return

            # include nums[i]
            curSet.append(nums[i])
            helper(i + 1)

            # exclude nums[i]
            curSet.pop()
            helper(i + 1)

        helper(0)
        return subsets
