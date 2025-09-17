# python's default is min-heap. Just use the negative value to turn it to max-heap

import heapq

h = []

# Push elements as negatives
heapq.heappush(h, -5)
heapq.heappush(h, -2)
heapq.heappush(h, -8)

# Peek max (remember to negate)
print(-h[0])  # Output: 8

# Pop max
max_val = -heapq.heappop(h)
print(max_val)  # Output: 8

# Heap now contains 5 and 2 (negated)
print([-x for x in h])  # Output: [5, 2]
