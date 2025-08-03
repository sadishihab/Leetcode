#As the final output is duplication of the same array, i can just add it with itself in python. and the commented part is the normal solution. but just adding it reduce the runtime.
#While both solutions are O(n), the concatenation approach avoids the overhead of initializing an array with zeros and manually assigning values in a loop. Python's list concatenation is highly optimized at the C level, potentially reducing constant factors in runtime.

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
