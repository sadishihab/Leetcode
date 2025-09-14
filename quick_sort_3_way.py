# 3-way QuickSort (Dutch National Flag partitioning)

import random

def quick_sort(nums, start, end):
    if end - start + 1 <= 1:  # base case
        return

    # pick random pivot, swap it with end
    pivot_index = random.randint(start, end)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

    lt, i, gt = start, start, end

    while i <= gt:
        if nums[i] < pivot:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt += 1
            i += 1
        elif nums[i] > pivot:
            nums[gt], nums[i] = nums[i], nums[gt]
            gt -= 1
        else:  # nums[i] == pivot
            i += 1

    quick_sort(nums, start, lt - 1)
    quick_sort(nums, gt + 1, end)


# Example usage:
arr = [5, 2, 3, 1, 5, 2]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 2, 3, 5, 5]
