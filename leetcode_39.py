class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])  # found a valid combo
                return
            if target < 0:
                return  # too large, stop

            for i in range(start, len(candidates)):
                path.append(candidates[i])  # choose
                backtrack(i, path, target - candidates[i])  # reuse allowed → stay at i
                path.pop()  # un-choose (backtrack)

        backtrack(0, [], target)
        return res
