# Remove Duplicates from Sorted Array
#Approach: Two-Pointer Technique
# The problem can be solved efficiently using a two-pointer technique since the array is already sorted. it is used because:
        #In-Place Modification: The problem requires modifying the array in-place without using extra space. The two-pointer method allows us to overwrite duplicate elements with unique ones.
        #Efficient Traversal: Since the array is sorted, duplicates are adjacent. By comparing adjacent elements, we can identify unique elements in a single pass (O(n) time).
        #Track Unique Elements: One pointer (k) tracks the position where the next unique element should be placed, while the other (i) iterates through the array to find unique elements.
        #Simplicity and Order Preservation: The approach ensures unique elements are placed in the correct order (as they appear in the sorted array) with minimal operations.

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
