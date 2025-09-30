class MinHeap:
    def __init__(self):
        """
        Initialize heap with a dummy -inf value at index 0.
        This simplifies parent/child index calculations:
        - parent of i -> i // 2
        - left child -> 2 * i
        - right child -> 2 * i + 1
        """
        self.heap = [float('-inf')]

    def push(self, val):
        """ Insert a new value into the heap and maintain min-heap property."""
        self.heap.append(val)
        i = len(self.heap) - 1                      # index of newly added value

        # Bubble up until parent <= current
        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self):
        """ Remove and return the smallest element from the heap. Returns None if heap is empty. """
        if len(self.heap) == 1:
            # Only dummy value exists
            return None
        if len(self.heap) == 2:
            return self.heap.pop()                          # Only one real element exists

        min_val = self.heap[1]                              # Save the root (minimum value)

        self.heap[1] = self.heap.pop()                      # Move last element to root
        self._percolate_down(1)                             # start from root

        return min_val

    def peek(self):
        """Return the smallest element without removing it."""
        if len(self.heap) == 1:
            return None
        return self.heap[1]

    def heapify(self, arr):
        self.heap = [float('-inf')] + arr[:]  # copy array, keep dummy at 0
        # start from last parent
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self._percolate_down(i)

    def _percolate_down(self, i):
        while 2 * i < len(self.heap):               # while at least left child exists
            left = 2 * i
            right = 2 * i + 1
            smallest = left                          # assume left child is smallest

            # If right child exists and is smaller, update smallest
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            # If current node > smallest child, swap
            if self.heap[i] > self.heap[smallest]:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest  # move down
            else:
                break  # heap property satisfied

    def __len__(self):
        """ Return the number of real elements in the heap. """
        return len(self.heap) - 1

    def __str__(self):
        """ For easy visualization (skip dummy value) """
        return str(self.heap[1:])

    def is_empty(self):
        return len(self.heap) == 1
