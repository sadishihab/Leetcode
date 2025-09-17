import heapq

class Solution(object):
    def findKthLargest(self, nums, k):

        min_heap = []                                                           # Initialize an empty min-heap
        for num in nums:                                                        # Iterate through each number in nums
            heapq.heappush(min_heap, num)                                 # Push the number into the heap
            if len(min_heap) > k:                                               # If heap exceeds size k
                heapq.heappop(min_heap)                                         # Remove the smallest element

        return min_heap[0]                                                      # The root of the min-heap is the kth largest element

# ----------------- Example usage -----------------
nums = [3, 2, 1, 5, 6, 5, 4]
k = 2
sol = Solution()
print(f"{k}th largest element is:", sol.findKthLargest(nums, k))  # Output: 5
