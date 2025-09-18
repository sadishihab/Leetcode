# binary search in a range and we don't know the exact target but know the conditions
def binary_search_in_range(left, right):
    while left <= right:
        mid = (left + right) // 2
        result = is_correct(mid)
        if result > 0:
            right = mid - 1
        elif result < 0:
            left = mid + 1
        else:
            return mid
    return -1

def is_correct(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0

print(binary_search_in_range(1, 100))  # 4