class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = []
        curSet = []

        def helper(i):
            if i == len(nums):
                subsets.append(curSet[:])
                return

            # include
            curSet.append(nums[i])
            helper(i + 1)
            curSet.pop()

            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # exclude
            helper(i + 1)

        helper(0)
        return subsets
