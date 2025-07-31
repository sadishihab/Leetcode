#Shuffle the array
class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])

        nums[:] = result
        return nums

sol = Solution()
nums = [2,5,1,3,4,7]
n = 3
nums = sol.shuffle(nums, n)
print(nums)


