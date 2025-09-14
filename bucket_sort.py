def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr

# implementation using less code, more pythonic
# def bucket_sort(arr):
#     # Count 0s, 1s, and 2s
#     counts = [arr.count(0), arr.count(1), arr.count(2)]
#
#     # Build sorted array directly
#     return [0] * counts[0] + [1] * counts[1] + [2] * counts[2]
