#implementation using less code, more pythonic

def bucket_sort(arr):

    counts = [arr.count(0), arr.count(1), arr.count(2)]                      # Count 0s, 1s, and 2s
    return [0] * counts[0] + [1] * counts[1] + [2] * counts[2]               # Build sorted array directly





# detail Code:
  
# def bucketSort(arr):
#     counts = [0, 0, 0]                                              # Assuming arr only contains 0, 1 or 2
#     for n in arr:                                                   # Count the quantity of each val in arr
#         counts[n] += 1
#     i = 0                                                           # Fill each bucket in the original array
#     for n in range(len(counts)):
#         for _ in range(counts[n]):
#             arr[i] = n
#             i += 1
#     return arr
#
# arr = [2,0,2,1,1,0]
# print(bucketSort(arr))


