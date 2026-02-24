# Swap Method
# Time O(n × n!) # Space O(n)
class Solution:
    def permute(self, nums):
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # swap back

        backtrack(0)
        return res

##########################################################################################
# Insert Method
# Time: O(n^2 * n!)
def permutationsRecursive(nums):
    return helper(0, nums)


def helper(i, nums):
    if i == len(nums):
        return [[]]

    resPerms = []
    perms = helper(i + 1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms

##############################################
# Iterative approach
# Time: O(n^2 * n!)
def permutationsIterative(nums):
    perms = [[]]

    for n in nums:
        nextPerms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerms.append(pCopy)
        perms = nextPerms
    return perms