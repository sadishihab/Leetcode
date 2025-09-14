import random

class Solution:
    def sortArray(self, nums):
        def quick_sort(arr, start, end):
            if start >= end:
                return

            pivot_index = random.randint(start, end)
            pivot = arr[pivot_index]
            arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

            # 3-way partitioning
            lt, i, gt = start, start, end
            while i <= gt:
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1
                    i += 1
                elif arr[i] > pivot:
                    arr[i], arr[gt] = arr[gt], arr[i]
                    gt -= 1
                else:  # arr[i] == pivot
                    i += 1

            quick_sort(arr, start, lt - 1)
            quick_sort(arr, gt + 1, end)

        quick_sort(nums, 0, len(nums) - 1)
        return nums
