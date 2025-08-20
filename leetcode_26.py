# Remove Duplicates from Sorted Array
# Sorted array → two pointers. i to scan, k to track for unique.
# Time: O(n) → one pass through the array
# Space: O(1) → in-place, no extra memory

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:                                                           # If array is empty, return 0
            return 0
        k = 1                                                                  # Initialize pointer for the position to place unique elements
        for i in range(1, len(nums)):                                          # Iterate through the array starting from the second element
            if nums[i] != nums[i - 1]:                                         # If current element is different from the previous one, comparing adjacent elements
                nums[k] = nums[i]                                              # Place the unique element at index k
                k += 1                                                         # Increment k to point to the next position for a unique element
        return k

#Testing the solution.
sol = Solution()
nums = [0,0,3,3,4,4,4,6]
k = sol.removeDuplicates(nums)
print("Total number of unique elements", k)
print(nums[:k])