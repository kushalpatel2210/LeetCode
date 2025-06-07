import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            distance = x ** 2 + y ** 2 # if you do not take sqrt, it's ok as well
            heapq.heappush(maxHeap, (-distance, (x, y)))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [list(tpl) for dist, tpl in maxHeap]