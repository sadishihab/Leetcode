class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # sort to make duplicates adjacent
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # skip used numbers
                if used[i]:
                    continue
                # skip duplicates (only use the first unused one)
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # choose
                used[i] = True
                path.append(nums[i])

                # explore
                backtrack(path)

                # undo choice
                path.pop()
                used[i] = False

        backtrack([])
        return res
