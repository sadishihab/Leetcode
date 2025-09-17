import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in nums (1-based k)
        using in-place 3-way Quickselect
        """

        def select(start, end, k):
            # Base case: only one element
            if start == end:
                return nums[start]

            # Pick a random pivot
            pivot_index = random.randint(start, end)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

            # Partition into 3 parts: < pivot, == pivot, > pivot
            lt, i, gt = start, start, end
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            # Count elements in each part
            num_greater = end - gt           # strictly greater than pivot
            num_greater_equal = end - lt + 1 # greater or equal

            # Decide which partition contains kth largest
            if k <= num_greater:
                # kth largest in "greater than pivot"
                return select(gt + 1, end, k)
            elif k <= num_greater_equal:
                # kth largest is the pivot
                return pivot
            else:
                # kth largest in "smaller than pivot"
                return select(start, lt - 1, k - num_greater_equal)

        n = len(nums)
        return select(0, n - 1, k)

# ----------------- Example usage -----------------
nums = [3, 2, 1, 5, 6, 5, 4]
k = 2
sol = Solution()
print(f"{k}th largest element is:", sol.findKthLargest(nums, k))  # Output: 5
