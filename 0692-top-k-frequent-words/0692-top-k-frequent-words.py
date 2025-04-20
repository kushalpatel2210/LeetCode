from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        maxHeap = []
        res = []

        for word, freq in counter.items():
            heapq.heappush(maxHeap, (-freq, word))
        
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res