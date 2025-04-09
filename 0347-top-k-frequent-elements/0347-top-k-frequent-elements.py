import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        minHeap = []
        res = []

        for key, frq in counter.items():
            heapq.heappush(minHeap, (-frq, key))

        for _ in range(k):
            frq, key = heapq.heappop(minHeap)
            res.append(key)
        
        return res