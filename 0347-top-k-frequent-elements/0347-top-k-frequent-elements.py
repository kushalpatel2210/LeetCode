from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        pq = []

        for key, value in counter.items():
            heapq.heappush(pq, (-value, key))

        for _ in range(k):
            res.append(heapq.heappop(pq)[1])

        return res