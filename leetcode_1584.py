class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = set()
        minDist = [float('inf')] * n
        minDist[0] = 0
        totalCost = 0

        for _ in range(n):
            curr = -1
            currMin = float('inf')
            for i in range(n):
                if i not in visited and minDist[i] < currMin:
                    currMin = minDist[i]
                    curr = i
            visited.add(curr)
            totalCost += currMin
            for i in range(n):
                if i not in visited:
                    x1, y1 = points[curr]
                    x2, y2 = points[i]
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    if cost < minDist[i]:
                        minDist[i] = cost
        return totalCost