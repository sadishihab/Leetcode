class Solution(object):
    def sortColors(self, nums):
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1
        i = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                nums[i] = n
                i += 1
        return nums


sol = Solution()
arr = [2,0,2,1,1,0]
print(sol.sortColors(arr))