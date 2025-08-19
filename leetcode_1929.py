# Concatenation of Array
# Concatenate the array with itself using nums + nums. Return the result.
# Time: O(n) — concatenating two lists of length n requires iterating over all elements
# Space: O(n) — a new list of size 2n is created

nums = [1,3,2,1]
class Solution(object):
    def getConcatenation(self, nums):
        # ans = [0] * (len(nums) * 2)
        # for i in range(len(nums)):
        #     ans[i] = nums[i]
        #     ans [i + len(nums)] = nums[i]
        #return ans

        return nums + nums


sol = Solution()
ans = sol.getConcatenation(nums)
print(ans)
