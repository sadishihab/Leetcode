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
# “Two pointers. Use k to place non-val. For each num: if ≠ val → nums[k] = num, move k. Return k.”
# 👉 This way you’ll remember:
# Iterate all → skip val → write valid at k → return k.

# 🔑 Full Approach – Remove Element
# Observation:
# We need to remove all elements equal to val in-place.
# The new length (count of non-val elements) should be returned.
# The order of remaining elements can be preserved (this solution does preserve order).
# Two-pointer method:
# One pointer i → scans every element.
# Another pointer k → tracks the next position to place a valid element (not equal to val).

# Algorithm:
# Initialize k = 0.
# Traverse through nums:
# If nums[i] != val:
# Write nums[i] to nums[k].
# Increment k.
# If nums[i] == val, skip it.
# After the loop, all non-val elements are placed in the first k positions.

# Return:
# Return k, the count of valid (non-val) elements.

# ⏱️ Complexity
# Time: O(n) → one scan of the array.
# Space: O(1) → done in-place.