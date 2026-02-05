class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        # Step 1: Detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Find the entrance to the cycle (duplicate number)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
