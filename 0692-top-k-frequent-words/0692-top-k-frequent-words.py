from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        maxHeap = []
        res = []

        for word, frq in counter.items():
            heapq.heappush(maxHeap, (-frq, word))
        
        for _ in range(k):
            frq, word = heapq.heappop(maxHeap)
            res.append(word)

        return res