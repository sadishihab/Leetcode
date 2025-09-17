import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)

print("The heap is", h)
print("Smallest element at root", h[0])                     # 2 (smallest element at root)
print("Remove the smallest element", heapq.heappop(h))      # removes 2
print("Now the heap", h)
