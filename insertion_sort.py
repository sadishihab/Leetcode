# Insertion sort implementation using iterative approach

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j -= 1

    return arr

arr = [5, 3, 2, 1, 4]
print(insertion_sort(arr))