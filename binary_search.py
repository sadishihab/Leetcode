def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid   # found at index mid
    return -1            # not found


nums = [1, 3, 3, 4, 5, 6, 7, 8]
print(binary_search(nums, 5))  # 4
print(binary_search(nums, 2))  # -1
