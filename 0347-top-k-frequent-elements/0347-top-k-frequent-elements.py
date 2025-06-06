from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        minHeap = []

        for num, frq in counter.items():
            heapq.heappush(minHeap, (frq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [num for frq, num in minHeap]