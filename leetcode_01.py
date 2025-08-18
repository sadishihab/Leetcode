nums = [2, 7, 11, 15]

class Solution(object):
    def twoSum(self, nums, target):
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i
        return []

sol = Solution()
print(sol.twoSum(nums, 9))


#📝 Two Sum – Flashcard Approach

#“While looping, check if target–num exists in map.
#If yes → return indices.
#If no → save num:index in map.”

# 🔑 Approach to Solve Two Sum
#
# Use a hash map (dictionary) to store numbers we’ve seen
# 
# Key = number
#
# Value = its index
#
# Iterate through the array:
#
# For each number num, compute its complement = target - num.
#
# If the complement is already in the hash map → we found a solution → return indices [index_of_complement, current_index].
#
# Otherwise, store num with its index in the hash map.
#
# Return the pair of indices when found.
#
# 📌 Big Picture:
#
# “While scanning, check if the matching number for the target is already seen. If yes, return indices. If not, save the current number for future matches.”
#
# 👉 Time: O(n) (one pass)
# 👉 Space: O(n) (for hash map)