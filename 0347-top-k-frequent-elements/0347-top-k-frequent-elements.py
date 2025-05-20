import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        counter = Counter(nums)

        for num, frq in counter.items():
            heapq.heappush(minHeap, (frq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [val for frq, val in minHeap]