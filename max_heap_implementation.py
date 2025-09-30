class MaxHeap:
    def __init__(self):
        self.heap = [float('-inf')]

    def push(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while idx > 1 and self.heap[idx] > self.heap[idx // 2]:
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx = idx // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        max_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._percolate_down(1)
        return max_val

    def peek(self):
        return None if len(self.heap) == 1 else self.heap[1]

    def heapify(self, arr):
        self.heap = [float('-inf')] + arr[:]
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self._percolate_down(i)

    def _percolate_down(self, idx):
        while 2 * idx < len(self.heap):
            left = 2 * idx
            right = 2 * idx + 1
            largest = left

            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                largest = right

            if self.heap[idx] < self.heap[largest]:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                break

    def __len__(self):
        return len(self.heap) - 1

    def __str__(self):
        return str(self.heap[1:])

    def is_empty(self):
        return len(self.heap) == 1
