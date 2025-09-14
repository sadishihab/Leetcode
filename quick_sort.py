import random


def quick_sort(arr, start, end):
    if end - start + 1 <= 1:  # base case
        return

    # pick random pivot, swap it with end
    pivot_index = random.randint(start, end)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    pivot = arr[end]
    partition_index = start  # index where pivot will finally go

    # Partition: elements smaller than pivot on the left
    for i in range(start, end):
        if arr[i] < pivot:
            arr[partition_index], arr[i] = arr[i], arr[partition_index]
            partition_index += 1

    # Place pivot in its correct position
    arr[end], arr[partition_index] = arr[partition_index], arr[end]

    # Recursively sort left and right subarrays
    quick_sort(arr, start, partition_index - 1)
    quick_sort(arr, partition_index + 1, end)

    return arr
