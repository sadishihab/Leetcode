class Solution(object):
    def sortArray(self, nums):
        n = len(nums)

        # Helper function to maintain the max-heap property for a subtree rooted at index i
        def heapify(i, size):
            largest = i  # Assume current node i is largest
            left = 2 * i + 1  # Left child index
            right = 2 * i + 2  # Right child index

            # If left child exists and is greater than current largest, update largest
            if left < size and nums[left] > nums[largest]:
                largest = left

            # If right child exists and is greater than current largest, update largest
            if right < size and nums[right] > nums[largest]:
                largest = right

            # If largest is not the root, swap and continue heapifying
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]  # Swap
                heapify(largest, size)  # Heapify the affected subtree

        # Step 1: Build a max heap
        # Start from the last non-leaf node and heapify each node up to the root
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        # Step 2-4: Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Swap current root (largest) to the end
            heapify(0, i)  # Heapify the reduced heap

        return nums  # Return the sorted array

