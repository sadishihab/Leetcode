# binary search using recursion

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)

def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr)-1)


nums = [1, 3, 3, 4, 5, 6, 7, 8]
print(binary_search(nums, 5))  # 4
print(binary_search(nums, 2))  # -1
