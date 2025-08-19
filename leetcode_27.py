# Remove element
# Two pointers technique
# Time: O(n) → one scan of the array.
# Space: O(1) → done in-place.

class Solution(object):
    def removeElement(self, nums, val):
        k = 0                                                   # Initialize pointer k to track position for next non-val element
        for i in range(len(nums)):                              # Loop through indices 0 to len(nums)-1 to check each element
            if nums[i] != val:                                  # Check if current element is not equal to val
                nums[k] = nums[i]                               # Copy non-val element to position k
                k += 1                                          # Increment k to point to next position for non-val element
        return k                                                # Return k, the count of non-val elements

sol = Solution()
nums = [0,1,2,2,3,0,4,2]
k = sol.removeElement(nums, 2)
print(k)
print(nums[:k])