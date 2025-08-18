# Remove element which matches with the val from an array
#Approach: Two-Pointer Technique. this technique is used to:
    #Modify the array in-place: The problem requires you to rearrange nums without using additional space (e.g., no new array).
    #Efficiently track valid elements: One pointer (k) keeps track of where to place the next non-val element, while the other pointer (i) iterates through the array to find non-val elements.
    #Minimize operations: By only copying non-val elements to the correct position, the algorithm avoids unnecessary swaps or movements, achieving O(n) time complexity with O(1) space complexity.

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

# 📝 Flashcard Version (for revision)
# “Use pointer k. Loop array: if num ≠ val → put at nums[k], move k. End: return k (count of kept elements).”

# 🔑 Full Approach – Remove Element
# Problem Restatement:
# You’re given an array nums and a value val.
# Remove all instances of val in-place and return the count of remaining elements (k).
# The order of non-val elements can be changed, but not required.

# Two-pointer technique:
# Use a pointer k to track the next position to place a non-val element.
# Algorithm:
# Initialize k = 0.
# Loop through each index i in nums:
# If nums[i] != val:
# Copy nums[i] to nums[k].
# Increment k (to prepare for next placement).
# At the end, k represents the number of elements not equal to val.
# Return:
# Return k.

# The first k elements of nums now contain the desired result.
# ⏱️ Complexity
# Time: O(n) → single scan through array
# Space: O(1) → in-place modification