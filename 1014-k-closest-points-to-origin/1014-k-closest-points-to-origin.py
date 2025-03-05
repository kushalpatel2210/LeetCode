import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # (distance, (distance, (x, y)))
        kClosestPoints = []

        for point in points:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(minHeap, (distance, (x, y)))
        
        for _ in range(k):
            priority, points = heapq.heappop(minHeap)
            kClosestPoints.append(list(points))

        return kClosestPoints