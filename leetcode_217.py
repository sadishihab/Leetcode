""" Both set and hash map (dictionary) solutions are very similar in Python because under the hood,
Python’s set is implemented using a hash table (essentially a dictionary without values)
Using Hash Map """

# Using hashmap
class Solution:
    def containsDuplicate(self, nums):
        countMap = {}

        for num in nums:
            if num in countMap:
                return True       # duplicate found
            countMap[num] = 1     # mark as seen

        return False              # no duplicates found


# Using set
# class Solution:
#     def containsDuplicate(self, nums):
#         seen = set()
#
#         for num in nums:
#             if num in seen:
#                 return True  # duplicate found
#             seen.add(num)
#
#         return False  # no duplicates found

