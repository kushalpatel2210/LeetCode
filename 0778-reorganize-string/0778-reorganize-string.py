import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        counter = Counter(s)
        res = ""

        for c, frq in counter.items():
            heapq.heappush(maxHeap, (-frq, c))
        
        prev = None 
        while maxHeap:
            frq, c = heapq.heappop(maxHeap)
            res += c
            frq += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                
            if frq != 0:
                prev = (frq, c)
            else:
                prev = None
        
        return res if not prev else ""